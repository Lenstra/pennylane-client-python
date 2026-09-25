"""Tests for the vendored spec bundle, the spec conversion and the generated surface."""

import importlib.util
import pathlib

from pennylane_client import ENDPOINT_INDEX, PennylaneClient, spec

_FETCH_SPEC = (
    pathlib.Path(__file__).resolve().parent.parent / "scripts" / "fetch_spec.py"
)
_spec = importlib.util.spec_from_file_location("fetch_spec", _FETCH_SPEC)
fetch_spec = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(fetch_spec)


def test_bundle_is_the_v2_api():
    assert spec.api_version() == "2.0"
    n_methods = sum(len(e["methods"]) for e in spec.endpoints())
    assert n_methods > 100


def test_every_spec_method_is_generated():
    client = PennylaneClient("token")
    n_methods = sum(len(e["methods"]) for e in spec.endpoints())
    assert len(ENDPOINT_INDEX) == n_methods
    for (verb, path), (group, name) in ENDPOINT_INDEX.items():
        method = getattr(getattr(client.api, group), name)
        assert method.__doc__.startswith(f"{verb} {path}")


def test_match_prefers_literal_segments():
    info = spec.match("POST", "/api/external/v2/customer_invoices/import")
    assert info["operation_id"] == "importCustomerInvoices"
    info = spec.match("GET", "/api/external/v2/customer_invoices/42")
    assert info["operation_id"] == "getCustomerInvoice"


def test_match_unknown_path():
    assert spec.match("GET", "/api/external/v2/nope") is None


def test_snake():
    assert spec.snake("getCustomerInvoices") == "get_customer_invoices"
    assert spec.snake("customer_invoice_id") == "customer_invoice_id"


class TestToJsonSchema:
    def test_nullable_type(self):
        assert fetch_spec.to_json_schema({"type": "string", "nullable": True}) == {
            "type": ["string", "null"]
        }

    def test_nullable_enum(self):
        converted = fetch_spec.to_json_schema(
            {"type": "string", "enum": ["a", "b"], "nullable": True}
        )
        assert converted == {"type": ["string", "null"], "enum": ["a", "b", None]}

    def test_nullable_without_type(self):
        converted = fetch_spec.to_json_schema(
            {"allOf": [{"type": "object"}], "nullable": True}
        )
        assert converted == {
            "anyOf": [{"allOf": [{"type": "object"}]}, {"type": "null"}]
        }

    def test_nested_and_untouched(self):
        schema = {
            "type": "object",
            "properties": {
                "label": {"type": "string", "nullable": True},
                "id": {"type": "integer"},
            },
        }
        converted = fetch_spec.to_json_schema(schema)
        assert converted["properties"]["label"] == {"type": ["string", "null"]}
        assert converted["properties"]["id"] == {"type": "integer"}

    def test_no_nullable_left_in_bundle(self):
        assert all("nullable" not in str(s) for s in spec._bundle()["schemas"].values())
