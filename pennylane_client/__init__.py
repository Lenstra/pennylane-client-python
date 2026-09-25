"""Async Python client for the Pennylane API, driven by its published spec.

Two layers:

1. Full generated surface: ``client.api.<group>.<method>()`` covers every
   operation of the Pennylane Company API v2 and returns the decoded JSON.
   Methods are named after the spec's operationIds (``getCustomerInvoices``
   -> ``client.api.customer_invoices.get_customer_invoices``). Find methods
   by grepping ``docs/API.md`` or via ``pennylane_client.api.ENDPOINT_INDEX``;
   each docstring lists the query parameters and the request body.
2. Pagination helpers on ``PennylaneClient``: ``paginate`` and ``fetch_all``
   walk any cursor-paginated list operation.

Every JSON request body is validated against Pennylane's own schemas before
sending (``PennylaneValidationError``).
"""

from .api import ENDPOINT_INDEX, PennylaneAPI
from .client import PennylaneClient
from .exceptions import PennylaneAPIError, PennylaneError, PennylaneValidationError

__all__ = [
    "ENDPOINT_INDEX",
    "PennylaneAPI",
    "PennylaneAPIError",
    "PennylaneClient",
    "PennylaneError",
    "PennylaneValidationError",
]
