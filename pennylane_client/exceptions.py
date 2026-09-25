"""Exceptions for the Pennylane client."""

from __future__ import annotations


class PennylaneError(Exception):
    """Base exception for all Pennylane client errors."""


class PennylaneAPIError(PennylaneError):
    """An HTTP error returned by the Pennylane API."""

    def __init__(self, status_code: int, endpoint: str, detail: str) -> None:
        self.status_code = status_code
        self.endpoint = endpoint
        self.detail = detail
        super().__init__(f"Pennylane {status_code} on {endpoint}: {detail}")


class PennylaneValidationError(PennylaneError):
    """The request body does not match Pennylane's published schema.

    Raised BEFORE the request is sent, with the exact violations.
    """

    def __init__(self, endpoint: str, operation_id: str, errors: list[str]) -> None:
        self.endpoint = endpoint
        self.operation_id = operation_id
        self.errors = errors
        details = "\n  - ".join(errors)
        super().__init__(
            f"Request body for {endpoint} ({operation_id}) violates the schema:\n  - {details}"
        )
