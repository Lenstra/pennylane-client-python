# AGENTS.md

Guide for AI agents (Claude Code, Codex, Cursor, ...) that **use** this
client in another project, or **work on** this repository.

`pennylane-client` is an async Python client for the Pennylane Company API v2,
generated from Pennylane's published OpenAPI spec: 175 operations, one method
per `operationId`.

## Using the client

### Install and connect

```bash
uv add pennylane-client   # Python >= 3.13
```

```python
from pennylane_client import PennylaneClient

async with PennylaneClient(api_token) as client:
    me = await client.api.users.get_me()  # cheap call to check the token
```

- Import name is `pennylane_client`, **not** `pennylane` (that name belongs to
  an unrelated quantum computing library).
- The token is a Pennylane company API token (Settings > Connectivity >
  Developers). Read it from the environment, never hardcode or log it.
- There is no public sandbox: test against a non-production company.

### Find the right method

1. Grep `docs/API.md`: one line per method, with its HTTP verb, path and
   summary. Example: `grep -i "supplier invoice" docs/API.md`.
2. Read the method's docstring in `pennylane_client/api.py`: it lists every
   query parameter (with the allowed `filter` fields and operators) and the
   request body schema.
3. Or look it up by endpoint:
   `pennylane_client.ENDPOINT_INDEX[("GET", "/api/external/v2/customers/{id}")]`
   returns `("customers", "get_customer")`.

Methods are `client.api.<group>.<operation_id_in_snake_case>`. Groups are the
spec's tags: `customer_invoices`, `customers`, `supplier_invoices`,
`transactions`, `suppliers`, `ledger_entries`, `bank_accounts`, ...

### Conventions

- Every method is async and returns the decoded JSON (`dict`), unchanged.
- Path parameters are positional, query parameters are keyword-only:
  `get_customer_invoice(42)`, `get_customer_invoices(limit=100, sort="-date")`.
- List operations return one page: `{"items", "has_more", "next_cursor"}`.
  `limit` is 1 to 100 (API default 20). To get everything, use the helpers:
  - `await client.fetch_all(op, **kwargs)` returns a list of all items;
  - `async for item in client.paginate(op, **kwargs)` streams them.
- `filter` takes a list of dicts, JSON-encoded for you:
  `[{"field": "date", "operator": "gteq", "value": "2026-01-01"}]`.
  The allowed fields and operators differ per operation: check the docstring.
- JSON request bodies are validated against the spec **before sending**.
  Fix the body when you get `PennylaneValidationError`; its `errors` list
  gives the exact paths. `validate=False` skips the check: only use it when
  the published spec is known to be wrong for that payload.
- HTTP 429 (rate limit) is retried automatically (`max_retries=3`, honors
  `Retry-After`). At most 5 requests are in flight per client by default
  (`max_concurrent_requests`).

### Errors

| Exception | When |
|---|---|
| `PennylaneValidationError` | request body does not match the schema (nothing was sent) |
| `PennylaneAPIError` | HTTP error from the API: `status_code`, `endpoint`, `detail` |
| `PennylaneError` | base class, also raised on network errors |

A 403 usually means the token lacks the scope listed in the method's
docstring (e.g. `customer_invoices:readonly`).

### Recipes

```python
# All customer invoices of 2026
invoices = await client.fetch_all(
    client.api.customer_invoices.get_customer_invoices,
    filter=[{"field": "date", "operator": "gteq", "value": "2026-01-01"}],
)

# One customer, from an invoice
invoice = await client.api.customer_invoices.get_customer_invoice(42)
customer = await client.api.customers.get_customer(invoice["customer"]["id"])

# Supplier invoices of one supplier, newest first
page = await client.api.supplier_invoices.get_supplier_invoices(
    filter=[{"field": "supplier_id", "operator": "eq", "value": 7}], sort="-date"
)

# Create a company customer (validated before sending)
created = await client.api.customers.post_company_customer(
    {
        "name": "Acme",
        "billing_address": {
            "address": "1 rue de la Paix",
            "postal_code": "75002",
            "city": "Paris",
            "country_alpha2": "FR",
        },
    }
)
```

## Working on this repository

### Layout

| Path | What | Edit by hand? |
|---|---|---|
| `pennylane_client/client.py` | `PennylaneClient`: auth, validation, retries, pagination | yes |
| `pennylane_client/spec.py` | loads the vendored spec, `match()` a request to its operation | yes |
| `pennylane_client/exceptions.py` | exceptions | yes |
| `pennylane_client/_spec/spec.json.gz` | vendored spec bundle | **no**, run `scripts/fetch_spec.py` |
| `pennylane_client/api.py` | generated API surface | **no**, run `scripts/generate_api.py` |
| `docs/API.md` | generated method index | **no**, run `scripts/generate_api.py` |
| `scripts/` | spec download and code generation | yes |
| `tests/` | tests, no network (`httpx.MockTransport`) | yes |

### Commands

```bash
uv sync --dev
uv run ruff format --check . && uv run ruff check .
uv run pytest
```

All three must pass before opening a PR (the `ci.yml` workflow runs them).

### Update the API surface

```bash
uv run python scripts/fetch_spec.py     # download and vendor the OpenAPI file
uv run python scripts/generate_api.py   # regenerate api.py and docs/API.md
```

Review the `docs/API.md` diff to see what changed in the API, and commit the
three generated files together. To change how methods are generated, edit
`scripts/generate_api.py` and regenerate, never `api.py` directly.

### Rules

- Keep method names equal to the snake_case `operationId`: consumers rely on
  them, and renaming one is a breaking change.
- Tests never call the real API. Mock HTTP with `httpx.MockTransport`
  (`PennylaneClient(..., transport=...)`).
- Never commit a token, even a sandbox one.
- Write docs, comments and commit messages in simple English. Commits follow
  Conventional Commits (`feat: ...`, `fix: ...`, `docs: ...`).

### Release

1. Bump `version` in `pyproject.toml` (semver: a removed or renamed method is
   a breaking change).
2. Merge to `main`, then tag and push: `git tag -a vX.Y.Z -m "vX.Y.Z" && git push origin vX.Y.Z`.
3. `publish.yml` builds and publishes to PyPI with trusted publishing. A PyPI
   version cannot be replaced: check the tests pass before tagging.
