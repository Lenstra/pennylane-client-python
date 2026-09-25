"""Tests for PennylaneClient.request: auth, params, errors, retries, validation (no network)."""

import asyncio
import json

import httpx
import pytest

from pennylane_client import (
    PennylaneAPIError,
    PennylaneClient,
    PennylaneError,
    PennylaneValidationError,
)

CUSTOMERS = "/api/external/v2/company_customers"

VALID_CUSTOMER = {
    "name": "Lenstra",
    "billing_address": {
        "address": "1 rue de la Paix",
        "postal_code": "75002",
        "city": "Paris",
        "country_alpha2": "FR",
    },
}


def make_client(responses: list[httpx.Response] | None = None, **kwargs):
    """Client whose HTTP calls are answered by ``responses`` in order and logged."""
    calls: list[httpx.Request] = []
    queue = list(responses or [httpx.Response(200, json={})])

    def handler(request: httpx.Request) -> httpx.Response:
        calls.append(request)
        return queue.pop(0)

    client = PennylaneClient(
        "secret-token", transport=httpx.MockTransport(handler), **kwargs
    )
    return client, calls


def run(coro):
    return asyncio.run(coro)


def test_bearer_auth_and_url():
    client, calls = make_client([httpx.Response(200, json={"id": 42})])
    assert run(client.api.customer_invoices.get_customer_invoice(42)) == {"id": 42}
    assert calls[0].headers["Authorization"] == "Bearer secret-token"
    assert (
        str(calls[0].url)
        == "https://app.pennylane.com/api/external/v2/customer_invoices/42"
    )


def test_unset_params_dropped_and_filter_encoded():
    client, calls = make_client()
    filters = [{"field": "date", "operator": "gteq", "value": "2026-01-01"}]
    run(client.api.customer_invoices.get_customer_invoices(limit=10, filter=filters))
    params = dict(calls[0].url.params)
    assert params == {"limit": "10", "filter": json.dumps(filters)}


def test_empty_response_is_empty_dict():
    client, _ = make_client([httpx.Response(204)])
    assert run(client.request("DELETE", "/api/external/v2/customer_invoices/42")) == {}


def test_http_error_raises_api_error():
    client, _ = make_client([httpx.Response(404, json={"error": "Not found"})])
    with pytest.raises(PennylaneAPIError) as exc:
        run(client.api.customer_invoices.get_customer_invoice(42))
    assert exc.value.status_code == 404
    assert "Not found" in exc.value.detail


def test_rate_limit_is_retried():
    client, calls = make_client(
        [
            httpx.Response(429, headers={"Retry-After": "0"}),
            httpx.Response(200, json={"ok": True}),
        ]
    )
    assert run(client.api.customer_invoices.get_customer_invoice(42)) == {"ok": True}
    assert len(calls) == 2


def test_rate_limit_gives_up_after_max_retries():
    client, calls = make_client(
        [httpx.Response(429, headers={"Retry-After": "0"})] * 2, max_retries=1
    )
    with pytest.raises(PennylaneAPIError) as exc:
        run(client.api.customer_invoices.get_customer_invoice(42))
    assert exc.value.status_code == 429
    assert len(calls) == 2


def test_network_error_raises_client_error():
    def handler(request):
        raise httpx.ConnectError("boom")

    client = PennylaneClient("t", transport=httpx.MockTransport(handler))
    with pytest.raises(PennylaneError, match="boom"):
        run(client.api.customer_invoices.get_customer_invoice(42))


class TestBodyValidation:
    def test_valid_body_is_sent(self):
        client, calls = make_client()
        run(client.api.customers.post_company_customer(VALID_CUSTOMER))
        assert json.loads(calls[0].content) == VALID_CUSTOMER

    def test_nullable_field_accepts_null(self):
        client, calls = make_client()
        run(
            client.api.customers.post_company_customer(
                {**VALID_CUSTOMER, "reference": None}
            )
        )
        assert len(calls) == 1

    def test_missing_required_field_fails_before_sending(self):
        client, calls = make_client()
        with pytest.raises(PennylaneValidationError) as exc:
            run(client.api.customers.post_company_customer({"name": "Lenstra"}))
        assert "billing_address" in str(exc.value)
        assert exc.value.operation_id == "postCompanyCustomer"
        assert calls == []

    def test_unknown_field_fails(self):
        client, calls = make_client()
        with pytest.raises(PennylaneValidationError):
            run(
                client.api.customers.post_company_customer(
                    {**VALID_CUSTOMER, "nope": 1}
                )
            )
        assert calls == []

    def test_validate_false_skips_the_check(self):
        client, calls = make_client()
        run(
            client.api.customers.post_company_customer(
                {"name": "Lenstra"}, validate=False
            )
        )
        assert len(calls) == 1

    def test_path_not_in_spec_is_sent_unvalidated(self):
        client, calls = make_client()
        run(client.request("POST", "/api/external/v2/not_in_spec", json={"x": 1}))
        assert len(calls) == 1
        assert str(calls[0].url).endswith(
            CUSTOMERS.replace("company_customers", "not_in_spec")
        )
