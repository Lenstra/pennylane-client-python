"""Fetch the Pennylane OpenAPI spec and vendor it into the package.

Downloads the public OpenAPI file of the Pennylane Company API v2 and writes
a single gzipped bundle:

- pennylane_client/_spec/spec.json.gz: {"api_version", "source",
  "endpoints": [...], "schemas": {operation_id: schema}}

endpoints[*]: path, methods {get/post/put/delete: {operation_id, group,
summary, description, params, body_schema, body_content_type, paginated}}
where params documents the path and query parameters. schemas: JSON request
bodies, converted to plain JSON Schema and used for pre-send validation.

Run from the package root:

    uv run python scripts/fetch_spec.py

Then regenerate the API surface with scripts/generate_api.py.
"""

from __future__ import annotations

import gzip
import json
import pathlib
from typing import Any

import httpx

SOURCE = "https://pennylane.readme.io/openapi/accounting.json"
ROOT = pathlib.Path(__file__).resolve().parent.parent
SPEC_DIR = ROOT / "pennylane_client" / "_spec"

METHODS = ("get", "post", "put", "patch", "delete")


def to_json_schema(node: Any) -> Any:
    """Convert an OpenAPI 3.0 schema to plain JSON Schema.

    OpenAPI 3.0 marks optional values with ``nullable: true``, which JSON
    Schema validators ignore: a ``null`` would then be rejected. Rewrite it as
    an explicit ``null`` type. Everything else is already valid JSON Schema.
    """
    if isinstance(node, list):
        return [to_json_schema(item) for item in node]
    if not isinstance(node, dict):
        return node
    out = {key: to_json_schema(value) for key, value in node.items()}
    if not out.pop("nullable", False):
        return out
    if "type" in out:
        types = out["type"] if isinstance(out["type"], list) else [out["type"]]
        out["type"] = [*types, "null"]
        if "enum" in out and None not in out["enum"]:
            out["enum"] = [*out["enum"], None]
        return out
    # allOf/oneOf/anyOf without a direct type
    return {"anyOf": [out, {"type": "null"}]}


def snake_tag(tag: str) -> str:
    """ "Customer Invoices" -> "customer_invoices"."""
    return "_".join(tag.lower().split())


def describe_params(operation: dict) -> list[dict]:
    params = []
    for p in operation.get("parameters", []):
        schema = p.get("schema", {})
        params.append(
            {
                "name": p["name"],
                "in": p["in"],
                "required": bool(p.get("required")),
                "type": schema.get("type", "string"),
                "description": (p.get("description") or "").strip(),
            }
        )
    return params


def request_body(operation: dict) -> tuple[str | None, dict | None]:
    """(content type, JSON Schema) of the request body, if any."""
    content = operation.get("requestBody", {}).get("content", {})
    if not content:
        return None, None
    content_type = next(iter(content))
    schema = content[content_type].get("schema")
    if content_type != "application/json" or schema is None:
        return content_type, None
    return content_type, to_json_schema(schema)


def is_paginated(operation: dict) -> bool:
    return any(p["name"] == "cursor" for p in operation.get("parameters", []))


def build_bundle(spec: dict) -> dict:
    endpoints = []
    schemas: dict[str, dict] = {}
    for path, item in sorted(spec["paths"].items()):
        methods = {}
        for verb, operation in item.items():
            if verb not in METHODS:
                continue
            op_id = operation["operationId"]
            content_type, body_schema = request_body(operation)
            if body_schema is not None:
                schemas[op_id] = body_schema
            methods[verb] = {
                "operation_id": op_id,
                "group": snake_tag(operation.get("tags", ["misc"])[0]),
                "summary": (operation.get("summary") or "").strip(),
                "description": (operation.get("description") or "").strip(),
                "params": describe_params(operation),
                "body_schema": op_id if body_schema is not None else None,
                "body_content_type": content_type,
                "body_required": bool(operation.get("requestBody", {}).get("required")),
                "paginated": is_paginated(operation),
            }
        if methods:
            endpoints.append({"path": path, "methods": methods})
    return {
        "api_version": spec["info"].get("version", "?"),
        "source": SOURCE,
        "endpoints": endpoints,
        "schemas": schemas,
    }


def main() -> None:
    resp = httpx.get(SOURCE, timeout=60.0, follow_redirects=True)
    resp.raise_for_status()
    bundle = build_bundle(resp.json())
    SPEC_DIR.mkdir(parents=True, exist_ok=True)
    out = SPEC_DIR / "spec.json.gz"
    raw = json.dumps(bundle, sort_keys=True, separators=(",", ":")).encode()
    # mtime=0 keeps the file byte-identical when the spec did not change
    out.write_bytes(gzip.compress(raw, mtime=0))
    n_methods = sum(len(e["methods"]) for e in bundle["endpoints"])
    print(
        f"wrote {out}: {len(bundle['endpoints'])} paths, {n_methods} methods, "
        f"{len(bundle['schemas'])} body schemas, {out.stat().st_size // 1024}KB"
    )


if __name__ == "__main__":
    main()
