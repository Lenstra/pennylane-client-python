"""Vendored Pennylane API spec: endpoint registry + request-body schemas.

The bundle (_spec/spec.json.gz) is generated from Pennylane's public OpenAPI
file by scripts/fetch_spec.py. It drives two things:

- pre-send request-body validation, so a malformed payload fails with the
  exact violations instead of an opaque 4xx from the API;
- the generated method surface in api.py.
"""

from __future__ import annotations

import gzip
import json
import keyword
import re
from functools import lru_cache
from importlib import resources


@lru_cache(maxsize=1)
def _bundle() -> dict:
    data = (resources.files("pennylane_client") / "_spec" / "spec.json.gz").read_bytes()
    return json.loads(gzip.decompress(data))


def api_version() -> str:
    return _bundle()["api_version"]


def endpoints() -> list[dict]:
    """All endpoints: [{"path": "/api/external/v2/customers/{id}", "methods": {...}}, ...]"""
    return _bundle()["endpoints"]


def schema(operation_id: str) -> dict | None:
    """Request-body JSON schema of an operation (e.g. "postCompanyCustomer")."""
    return _bundle()["schemas"].get(operation_id)


def snake(name: str) -> str:
    """camelCase operationId / path parameter -> python identifier."""
    s = re.sub(r"(?<=[a-z0-9])([A-Z])", r"_\1", name.replace("-", "_")).lower()
    return s + "_" if keyword.iskeyword(s) else s


@lru_cache(maxsize=1)
def _routes() -> list[tuple[list[str], dict]]:
    return [(e["path"].strip("/").split("/"), e) for e in endpoints()]


@lru_cache(maxsize=256)
def match(method: str, path: str) -> dict | None:
    """Find the endpoint method entry for a concrete request.

    Returns {"path": ..., "operation_id": ..., "body_schema": ..., ...} or
    None if the path is not in the spec. Literal segments beat {param}
    segments, so /customer_invoices/import resolves before
    /customer_invoices/{id}.
    """
    method = method.lower()
    segments = path.strip("/").split("/")
    best: tuple[int, dict] | None = None
    for tmpl, entry in _routes():
        if len(tmpl) != len(segments) or method not in entry["methods"]:
            continue
        literals = 0
        for t, s in zip(tmpl, segments):
            if t.startswith("{"):
                continue
            if t != s:
                break
            literals += 1
        else:
            if best is None or literals > best[0]:
                best = (literals, entry)
    if best is None:
        return None
    entry = best[1]
    return {"path": entry["path"], **entry["methods"][method]}
