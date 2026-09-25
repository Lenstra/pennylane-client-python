"""Pennylane API client.

API base: https://app.pennylane.com (paths start with /api/external/v2)
Auth: company API token, sent as a Bearer token.
"""

from __future__ import annotations

import asyncio
import json
import logging
from collections.abc import AsyncIterator, Awaitable, Callable
from typing import Any, Self

import httpx
import jsonschema
from jsonschema.exceptions import best_match

from . import spec
from .api import PennylaneAPI
from .exceptions import PennylaneAPIError, PennylaneError, PennylaneValidationError

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Request-body validation (module-private)
# ---------------------------------------------------------------------------


def _format_schema_error(error: jsonschema.ValidationError) -> str:
    # For oneOf/anyOf failures the top-level message dumps entire schemas;
    # descend to the most relevant leaf error instead.
    leaf = error
    while leaf.context:
        leaf = best_match(leaf.context)
    json_path = "$" + "".join(f"[{p!r}]" for p in leaf.absolute_path)
    message = leaf.message
    if len(message) > 400:
        message = message[:400] + "…"
    return f"{json_path}: {message}"


def _validate_request_body(method: str, endpoint: str, body: Any) -> None:
    info = spec.match(method, endpoint)
    if info is None:
        logger.warning(
            "%s %s is not in the vendored API spec; body not validated",
            method,
            endpoint,
        )
        return
    operation_id = info.get("body_schema")
    if not operation_id:
        return
    schema = spec.schema(operation_id)
    if schema is None:
        return
    validator = jsonschema.Draft4Validator(schema)
    errors = sorted(validator.iter_errors(body), key=lambda e: list(e.absolute_path))
    if errors:
        raise PennylaneValidationError(
            endpoint, operation_id, [_format_schema_error(e) for e in errors]
        )


def _encode_params(params: dict | None) -> dict | None:
    """Drop unset params and JSON-encode structured ones.

    Pennylane expects ``filter`` as a JSON string such as
    ``[{"field": "date", "operator": "gteq", "value": "2024-01-01"}]``; a list
    of dicts is encoded for the caller.
    """
    if not params:
        return None
    return {
        key: json.dumps(value) if isinstance(value, (list, dict)) else value
        for key, value in params.items()
        if value is not None
    }


# ---------------------------------------------------------------------------
# Client
# ---------------------------------------------------------------------------


class PennylaneClient:
    """Async HTTP client for the Pennylane API.

    Usage as a context manager::

        async with PennylaneClient(api_token) as client:
            page = await client.api.customer_invoices.get_customer_invoices(limit=100)

    Or manage the lifecycle manually and call ``await client.aclose()``
    when done.

    ``client.api`` is the full generated API surface (one method per
    operation of the public spec, named after its operationId) returning the
    decoded JSON. ``client.paginate`` / ``client.fetch_all`` walk the
    cursor-paginated list operations.

    All JSON request bodies are validated against Pennylane's own schemas
    before sending (see PennylaneValidationError).
    """

    def __init__(
        self,
        api_token: str,
        base_url: str = "https://app.pennylane.com",
        max_concurrent_requests: int | None = 5,
        semaphore: asyncio.Semaphore | None = None,
        max_retries: int = 3,
        timeout: float = 30.0,
        transport: httpx.AsyncBaseTransport | None = None,
    ) -> None:
        """``max_concurrent_requests`` caps how many requests this client has
        in flight at once (default 5). Pass ``None`` to disable the cap, or
        ``semaphore`` to share one limit across multiple client instances
        (takes priority over ``max_concurrent_requests``).

        ``max_retries`` is how many times a request is retried after an HTTP
        429 (rate limit), waiting for the ``Retry-After`` header if present.
        """
        self._api_token = api_token
        self._base_url = base_url.rstrip("/")
        self._http = httpx.AsyncClient(timeout=timeout, transport=transport)
        self._semaphore = semaphore or (
            asyncio.Semaphore(max_concurrent_requests)
            if max_concurrent_requests
            else None
        )
        self._max_retries = max_retries
        self.api = PennylaneAPI(self)

    async def aclose(self) -> None:
        await self._http.aclose()

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, *_: object) -> None:
        await self.aclose()

    # ------------------------------------------------------------------
    # Internal HTTP
    # ------------------------------------------------------------------

    def _auth_headers(self) -> dict[str, str]:
        return {
            "Authorization": f"Bearer {self._api_token}",
            "Accept": "application/json",
        }

    async def request(
        self,
        method: str,
        endpoint: str,
        *,
        params: dict | None = None,
        validate: bool = True,
        **kwargs: Any,
    ) -> Any:
        """Send a request; validate any JSON body against the vendored spec first.

        ``validate=False`` skips the schema check (escape hatch for payloads
        the published spec does not describe correctly). Returns the decoded
        JSON (``{}`` for an empty response).
        """
        if validate and kwargs.get("json") is not None:
            _validate_request_body(method, endpoint, kwargs["json"])
        url = f"{self._base_url}{endpoint}"
        params = _encode_params(params)

        async def _do() -> Any:
            for attempt in range(self._max_retries + 1):
                try:
                    resp = await self._http.request(
                        method,
                        url,
                        headers=self._auth_headers(),
                        params=params,
                        **kwargs,
                    )
                except httpx.HTTPError as exc:
                    raise PennylaneError(
                        f"Request failed for {endpoint}: {exc}"
                    ) from exc
                if resp.status_code == 429 and attempt < self._max_retries:
                    delay = _retry_after(resp, attempt)
                    logger.info(
                        "rate limited on %s, retrying in %.1fs", endpoint, delay
                    )
                    await asyncio.sleep(delay)
                    continue
                if resp.is_error:
                    try:
                        detail = json.dumps(resp.json())
                    except ValueError:
                        detail = resp.text
                    raise PennylaneAPIError(resp.status_code, endpoint, detail)
                return resp.json() if resp.content else {}
            raise AssertionError("unreachable")

        if self._semaphore:
            async with self._semaphore:
                return await _do()
        return await _do()

    # ------------------------------------------------------------------
    # Pagination
    # ------------------------------------------------------------------

    async def paginate(
        self,
        operation: Callable[..., Awaitable[dict]],
        *args: Any,
        limit: int = 100,
        **kwargs: Any,
    ) -> AsyncIterator[dict]:
        """Yield every item of a cursor-paginated list operation, across pages.

        ``operation`` is a list method of ``client.api``; extra arguments are
        passed to it. Follows ``next_cursor`` until ``has_more`` is false.

        Usage::

            async for invoice in client.paginate(
                client.api.customer_invoices.get_customer_invoices,
                filter=[{"field": "date", "operator": "gteq", "value": "2026-01-01"}],
            ):
                process(invoice["invoice_number"])
        """
        cursor = None
        while True:
            page = await operation(*args, cursor=cursor, limit=limit, **kwargs)
            for item in page.get("items", []):
                yield item
            cursor = page.get("next_cursor")
            if not page.get("has_more") or not cursor:
                return

    async def fetch_all(
        self,
        operation: Callable[..., Awaitable[dict]],
        *args: Any,
        limit: int = 100,
        **kwargs: Any,
    ) -> list[dict]:
        """All items of a cursor-paginated list operation (see ``paginate``)."""
        return [
            item
            async for item in self.paginate(operation, *args, limit=limit, **kwargs)
        ]


def _retry_after(resp: httpx.Response, attempt: int) -> float:
    """Seconds to wait before retrying a 429: Retry-After, else exponential."""
    try:
        return max(0.0, float(resp.headers["Retry-After"]))
    except (KeyError, ValueError):
        return float(2**attempt)
