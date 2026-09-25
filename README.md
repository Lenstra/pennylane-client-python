# pennylane-client

Async Python client for the [Pennylane API](https://pennylane.readme.io/)
(Company API v2).

```bash
uv add pennylane-client
```

Using an AI coding agent? Point it to [`AGENTS.md`](AGENTS.md): how to find
the right method, conventions, recipes and pitfalls.

## Why it's built this way

The client is generated from Pennylane's own published OpenAPI spec, the same
way [boondmanager-client](https://github.com/Lenstra/boondmanager-client-python)
is generated from BoondManager's spec:

- `pennylane_client/_spec/spec.json.gz`: vendored bundle with the full
  operation registry (175 operations) and every JSON request-body schema,
  extracted from the public OpenAPI file.
- `pennylane_client/api.py`: generated surface, one method per operation,
  named after the spec's `operationId` (so the names match Pennylane's docs).
- Every JSON request body is validated against the matching schema **before
  sending**: a mismatch raises `PennylaneValidationError` with the exact
  violations, instead of an opaque 4xx from the API.

## Usage

```python
from pennylane_client import PennylaneClient

async with PennylaneClient(api_token) as client:
    # One page of a list operation: {"items", "has_more", "next_cursor"}
    page = await client.api.customer_invoices.get_customer_invoices(limit=100)

    # A single object
    invoice = await client.api.customer_invoices.get_customer_invoice(42)

    # Every item of a cursor-paginated list, across pages
    async for invoice in client.paginate(
        client.api.customer_invoices.get_customer_invoices,
        filter=[{"field": "date", "operator": "gteq", "value": "2026-01-01"}],
    ):
        print(invoice["invoice_number"])

    # Or all at once
    customers = await client.fetch_all(client.api.customers.get_customers)

    # Writes are validated against the spec before sending
    await client.api.customers.post_company_customer(
        {"name": "Acme", "billing_address": {...}}
    )
```

- `client.api.<group>.<method>(...)`: groups are the spec's tags
  (`customer_invoices`, `customers`, `supplier_invoices`, `transactions`, ...).
  Path parameters are positional, query parameters are keyword-only, and every
  method returns the decoded JSON.
- `filter` accepts a list of dicts, JSON-encoded for you.
- Find the right method by grepping [`docs/API.md`](docs/API.md) or with
  `pennylane_client.ENDPOINT_INDEX`; each method's docstring lists its query
  parameters and request body.

### Client options

- `max_concurrent_requests` (default 5) caps the requests in flight, or pass
  `semaphore` to share one limit across clients.
- `max_retries` (default 3): HTTP 429 (rate limit) responses are retried,
  waiting for the `Retry-After` header.
- `validate=False` on a write method skips the schema check (escape hatch
  for a payload the published spec does not describe correctly).

### Errors

- `PennylaneValidationError`: the request body does not match the schema
  (raised before sending).
- `PennylaneAPIError`: the API returned an HTTP error (`status_code`,
  `endpoint`, `detail`).
- `PennylaneError`: base class, also raised on network errors.

## Development

```bash
uv sync --dev
uv run ruff format --check . && uv run ruff check .
uv run pytest
```

### Updating the spec

```bash
uv run python scripts/fetch_spec.py     # download and vendor the OpenAPI file
uv run python scripts/generate_api.py   # regenerate api.py and docs/API.md
```

Review the diff of `docs/API.md` to see what changed in the API.

### Releasing

Bump `version` in `pyproject.toml`, merge, then push a tag:

```bash
git tag v0.1.0 && git push origin v0.1.0
```

The `publish.yml` workflow builds the package and publishes it to PyPI with
trusted publishing (no token needed).
