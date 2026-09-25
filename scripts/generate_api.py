"""Generate pennylane_client/api.py (namespaced API surface) from the spec bundle.

Operations are grouped by their OpenAPI tag into namespace classes, and each
method is named after its operationId:

    GET  /api/external/v2/customer_invoices       (getCustomerInvoices)
         -> client.api.customer_invoices.get_customer_invoices(limit=..., filter=...)
    GET  /api/external/v2/customer_invoices/{id}  (getCustomerInvoice)
         -> client.api.customer_invoices.get_customer_invoice(id)
    POST /api/external/v2/company_customers       (postCompanyCustomer)
         -> client.api.customers.post_company_customer(body)

Path parameters are positional, query parameters are keyword-only. All
methods return the decoded JSON.

Run from the package root (after scripts/fetch_spec.py):

    uv run python scripts/generate_api.py
"""

from __future__ import annotations

import gzip
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from pennylane_client.spec import snake  # noqa: E402

OUT = ROOT / "pennylane_client" / "api.py"
DOCS_OUT = ROOT / "docs" / "API.md"

PY_TYPES = {
    "string": "str",
    "integer": "int",
    "number": "float",
    "boolean": "bool",
    "array": "list",
}

DOCS_HEADER = """\
# Pennylane client: API index (generated, do not edit)

One line per method of `client.api`. Grep this file to find the right call,
then read its docstring in `pennylane_client/api.py` for the query parameters
and the request body.

Conventions:

- `client.api.<group>.<method>(...)`: all methods are async and return the
  decoded JSON. Method names are the spec's operationIds in snake_case.
- Path parameters are positional, query parameters are keyword-only.
- `[paginated]` methods return `{"items", "has_more", "next_cursor"}`: pass
  them to `client.paginate(...)` or `client.fetch_all(...)` to walk all pages.
"""

HEADER = '''"""Generated Pennylane API surface. DO NOT EDIT.

Regenerate with scripts/fetch_spec.py + scripts/generate_api.py.

One namespace per API tag, one method per operation, covering the whole
Pennylane Company API v{version} ({n_methods} operations). Method names are
the spec's operationIds in snake_case. Every call goes through
PennylaneClient.request(), which validates JSON request bodies against
Pennylane's own schemas before sending.

ENDPOINT_INDEX maps ("VERB", "/path/{id}") to ("group", "method") for
programmatic discovery.
"""

# fmt: off

from __future__ import annotations

from typing import Any
'''

API_CLASS = '''

class PennylaneAPI:
    """Namespaced access to every operation of the Pennylane API.

    Usage::

        page = await client.api.customer_invoices.get_customer_invoices(limit=100)
        invoice = await client.api.customer_invoices.get_customer_invoice(42)
    """

    def __init__(self, client) -> None:
{assignments}
'''


def class_name(group: str) -> str:
    return "".join(w.capitalize() for w in group.split("_")) + "API"


def path_params(path: str) -> list[str]:
    return [snake(m) for m in re.findall(r"\{(\w+)\}", path)]


def fstring_path(path: str) -> str:
    concrete = re.sub(r"\{(\w+)\}", lambda m: "{" + snake(m.group(1)) + "}", path)
    return ('f"' if "{" in concrete else '"') + concrete + '"'


def query_type(p: dict) -> str:
    if p["name"] == "filter":
        return "str | list[dict]"
    return PY_TYPES.get(p["type"], "Any")


def escape_doc(text: str) -> str:
    return text.replace("\\", "\\\\").replace('"""', '\\"\\"\\"')


def gen_method(verb: str, path: str, info: dict) -> tuple[str, str]:
    name = snake(info["operation_id"])
    query = [p for p in info["params"] if p["in"] == "query"]
    content_type = info["body_content_type"]
    is_json = content_type == "application/json"
    is_multipart = content_type == "multipart/form-data"

    args = ["self"] + [f"{p}: int | str" for p in path_params(path)]
    if is_json:
        args.append("body: Any" if info["body_required"] else "body: Any = None")
    elif is_multipart:
        args += ["files: Any", "data: dict | None = None"]
    kwonly = [
        f"{snake(p['name'])}: {query_type(p)}"
        + ("" if p["required"] else " | None = None")
        for p in query
    ]
    if is_json:
        kwonly.append("validate: bool = True")
    sig = ", ".join(args + (["*"] + kwonly if kwonly else []))

    doc_lines = [f"{verb.upper()} {path} ({info['operation_id']})"]
    if info["summary"]:
        doc_lines += ["", info["summary"]]
    if info["description"] and info["description"] != info["summary"]:
        doc_lines += [""] + info["description"].splitlines()
    if query:
        doc_lines += ["", "Query params:"]
        for p in query:
            head = f"  {p['name']} ({p['type']}{', REQUIRED' if p['required'] else ''})"
            desc = p["description"].splitlines()
            doc_lines.append(head + (f": {desc[0]}" if desc else ""))
            doc_lines += [f"    {line}" for line in desc[1:]]
    if info["paginated"]:
        doc_lines += [
            "",
            "Paginated: pass this method to client.paginate() or client.fetch_all().",
        ]
    if is_json and info["body_schema"]:
        doc_lines += [
            "",
            f'Request body: JSON, validated against spec.schema("{info["body_schema"]}").',
        ]
    elif is_multipart:
        doc_lines += [
            "",
            "Request body: multipart/form-data (files=..., data=...), not validated.",
        ]
    lines = [escape_doc(line).rstrip() for line in doc_lines]
    doc = "\n".join(
        [lines[0]] + [f"        {line}" if line else "" for line in lines[1:]]
    )

    call_args = [f'"{verb.upper()}"', fstring_path(path)]
    if query:
        call_args.append(
            "params={"
            + ", ".join(f'"{p["name"]}": {snake(p["name"])}' for p in query)
            + "}"
        )
    if is_json:
        call_args += ["json=body", "validate=validate"]
    elif is_multipart:
        call_args += ["files=files", "data=data"]

    code = (
        f"    async def {name}({sig}) -> Any:\n"
        f'        """{doc}\n        """\n'
        f"        return await self._client.request({', '.join(call_args)})\n"
    )
    return name, code


def docs_line(name: str, verb: str, path: str, info: dict) -> str:
    args = path_params(path)
    if info["body_content_type"] == "application/json":
        args.append("body")
    elif info["body_content_type"] == "multipart/form-data":
        args.append("files")
    required = [
        p["name"] for p in info["params"] if p["in"] == "query" and p["required"]
    ]
    args += [f"{r}=..." for r in required]
    tag = " [paginated]" if info["paginated"] else ""
    summary = f": {info['summary']}" if info["summary"] else ""
    return f"- `{name}({', '.join(args)})`{tag}, {verb.upper()} {path}{summary}"


def main() -> None:
    bundle = json.loads(
        gzip.decompress(
            (ROOT / "pennylane_client" / "_spec" / "spec.json.gz").read_bytes()
        )
    )

    # group -> list of (verb, path, info)
    groups: dict[str, list[tuple[str, str, dict]]] = {}
    for endpoint in bundle["endpoints"]:
        for verb, info in endpoint["methods"].items():
            groups.setdefault(info["group"], []).append((verb, endpoint["path"], info))

    n_methods = sum(len(v) for v in groups.values())
    out = HEADER.replace("{version}", str(bundle["api_version"])).replace(
        "{n_methods}", str(n_methods)
    )
    index: list[str] = []
    docs = [DOCS_HEADER]

    for group in sorted(groups):
        out += f"\n\nclass {class_name(group)}:\n"
        out += f'    """Operations tagged "{group}"."""\n\n'
        out += (
            "    def __init__(self, client) -> None:\n        self._client = client\n\n"
        )
        docs.append(f"\n## client.api.{group}\n")
        taken: set[str] = set()
        for verb, path, info in sorted(groups[group], key=lambda t: (t[1], t[0])):
            name, code = gen_method(verb, path, info)
            if name in taken:
                raise SystemExit(
                    f"duplicate method name {group}.{name} ({verb} {path})"
                )
            taken.add(name)
            out += code + "\n"
            docs.append(docs_line(name, verb, path, info))
            index.append(f'    ("{verb.upper()}", "{path}"): ("{group}", "{name}"),')

    assignments = "\n".join(
        f"        self.{group} = {class_name(group)}(client)"
        for group in sorted(groups)
    )
    out += API_CLASS.replace("{assignments}", assignments)

    out += "\n\nENDPOINT_INDEX: dict[tuple[str, str], tuple[str, str]] = {\n"
    out += "\n".join(sorted(index)) + "\n}\n"

    OUT.write_text(out)
    DOCS_OUT.parent.mkdir(exist_ok=True)
    DOCS_OUT.write_text("\n".join(docs) + "\n")
    print(
        f"wrote {OUT}: {len(groups)} groups, {n_methods} methods, {len(out) // 1024}KB"
    )
    print(f"wrote {DOCS_OUT}: {len(DOCS_OUT.read_text()) // 1024}KB")


if __name__ == "__main__":
    main()
