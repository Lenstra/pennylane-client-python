"""Generated Pennylane API surface. DO NOT EDIT.

Regenerate with scripts/fetch_spec.py + scripts/generate_api.py.

One namespace per API tag, one method per operation, covering the whole
Pennylane Company API v2.0 (175 operations). Method names are
the spec's operationIds in snake_case. Every call goes through
PennylaneClient.request(), which validates JSON request bodies against
Pennylane's own schemas before sending.

ENDPOINT_INDEX maps ("VERB", "/path/{id}") to ("group", "method") for
programmatic discovery.
"""

# fmt: off

from __future__ import annotations

from typing import Any


class BankAccountsAPI:
    """Operations tagged "bank_accounts"."""

    def __init__(self, client) -> None:
        self._client = client

    async def get_bank_accounts(self, *, cursor: str | None = None, limit: int | None = None, sort: str | None = None) -> Any:
        """GET /api/external/v2/bank_accounts (getBankAccounts)

        List bank accounts

        List bank_accounts

        > ℹ️
        > This endpoint requires one of the following scopes: `bank_accounts:all`, `bank_accounts:readonly`

        Query params:
          cursor (string): Cursor for pagination. Use this to fetch the next set of results.
            The cursor is an opaque string returned in the previous response's metadata.
            Leave empty for the first request.
          limit (integer): Number of items to return per request.
            Defaults to 20 if not specified.
            Must be between 1 and 100.
          sort (string): You can choose to sort items on specific attributes
            Sort field may be prefixed with `-` for descending order.
            Example : `id` will sort by ascending order, `-id` will sort by descending order.
            Available fields : `id`

        Paginated: pass this method to client.paginate() or client.fetch_all().
        """
        return await self._client.request("GET", "/api/external/v2/bank_accounts", params={"cursor": cursor, "limit": limit, "sort": sort})

    async def post_bank_account(self, body: Any, *, validate: bool = True) -> Any:
        """POST /api/external/v2/bank_accounts (postBankAccount)

        Create a bank account

        Create a bank account

        > ℹ️
        > This endpoint requires the following scope: `bank_accounts:all`

        Request body: JSON, validated against spec.schema("postBankAccount").
        """
        return await self._client.request("POST", "/api/external/v2/bank_accounts", json=body, validate=validate)

    async def get_bank_account(self, id: int | str) -> Any:
        """GET /api/external/v2/bank_accounts/{id} (getBankAccount)

        Retrieve a bank account

        Retrieve a bank account

        > ℹ️
        > This endpoint requires one of the following scopes: `bank_accounts:all`, `bank_accounts:readonly`
        """
        return await self._client.request("GET", f"/api/external/v2/bank_accounts/{id}")



class BankEstablishmentsAPI:
    """Operations tagged "bank_establishments"."""

    def __init__(self, client) -> None:
        self._client = client

    async def get_bank_establishments(self, *, cursor: str | None = None, limit: int | None = None, filter: str | list[dict] | None = None, sort: str | None = None) -> Any:
        """GET /api/external/v2/bank_establishments (getBankEstablishments)

        List bank establishments

        List bank establishments

        > ℹ️
        > This endpoint requires the following scope: `bank_establishments:readonly`

        Query params:
          cursor (string): Cursor for pagination. Use this to fetch the next set of results.
            The cursor is an opaque string returned in the previous response's metadata.
            Leave empty for the first request.
          limit (integer): Number of items to return per request.
            Defaults to 20 if not specified.
            Must be between 1 and 100.
          filter (string): You can choose to filter items on specific fields.
            Available fields and values:
            - `id`: `lt`, `lteq`, `gt`, `gteq`, `eq`, `not_eq`, `in`, `not_in`
          sort (string): You can choose to sort items on specific attributes
            Sort field may be prefixed with `-` for descending order.
            Example : `id` will sort by ascending order, `-id` will sort by descending order.
            Available fields : `id`

        Paginated: pass this method to client.paginate() or client.fetch_all().
        """
        return await self._client.request("GET", "/api/external/v2/bank_establishments", params={"cursor": cursor, "limit": limit, "filter": filter, "sort": sort})



class BillingSubscriptionsAPI:
    """Operations tagged "billing_subscriptions"."""

    def __init__(self, client) -> None:
        self._client = client

    async def get_billing_subscriptions(self, *, cursor: str | None = None, limit: int | None = None, filter: str | list[dict] | None = None, sort: str | None = None) -> Any:
        """GET /api/external/v2/billing_subscriptions (getBillingSubscriptions)

        List billing subscriptions

        This endpoint returns a list of subscriptions.

        > ℹ️
        > This endpoint requires one of the following scopes: `billing_subscriptions:all`, `billing_subscriptions:readonly`

        Query params:
          cursor (string): Cursor for pagination. Use this to fetch the next set of results.
            The cursor is an opaque string returned in the previous response's metadata.
            Leave empty for the first request.
          limit (integer): Number of items to return per request.
            Defaults to 20 if not specified.
            Must be between 1 and 100.
          filter (string): You can choose to filter items on specific fields.
            Available fields and values:
            - `id`, `start`, `customer_id`: `lt`, `lteq`, `gt`, `gteq`, `eq`, `not_eq`, `in`, `not_in`
            - `status`: `eq`, `not_eq`, `in`, `not_in`
          sort (string): You can choose to sort items on specific attributes
            Sort field may be prefixed with `-` for descending order.
            Example : `id` will sort by ascending order, `-id` will sort by descending order.
            Available fields : `id`

        Paginated: pass this method to client.paginate() or client.fetch_all().
        """
        return await self._client.request("GET", "/api/external/v2/billing_subscriptions", params={"cursor": cursor, "limit": limit, "filter": filter, "sort": sort})

    async def post_billing_subscriptions(self, body: Any, *, validate: bool = True) -> Any:
        """POST /api/external/v2/billing_subscriptions (postBillingSubscriptions)

        Create a billing subscription

        This endpoint allows you to create a subscription. Pennylane will generate the customer invoice each month.
        You can also link the subscription to a GoCardless mandate.


        > ℹ️
        > This endpoint requires the following scope: `billing_subscriptions:all`

        Request body: JSON, validated against spec.schema("postBillingSubscriptions").
        """
        return await self._client.request("POST", "/api/external/v2/billing_subscriptions", json=body, validate=validate)

    async def get_billing_subscription_invoice_line_sections(self, billing_subscription_id: int | str, *, cursor: str | None = None, limit: int | None = None, sort: str | None = None) -> Any:
        """GET /api/external/v2/billing_subscriptions/{billing_subscription_id}/invoice_line_sections (getBillingSubscriptionInvoiceLineSections)

        List the invoice line sections of a billing subscription

        List the invoice line sections of a billing subscription

        > ℹ️
        > This endpoint requires one of the following scopes: `billing_subscriptions:all`, `billing_subscriptions:readonly`

        Query params:
          cursor (string): Cursor for pagination. Use this to fetch the next set of results.
            The cursor is an opaque string returned in the previous response's metadata.
            Leave empty for the first request.
          limit (integer): Number of items to return per request.
            Defaults to 20 if not specified.
            Must be between 1 and 100.
          sort (string): You can choose to sort items on specific attributes
            Sort field may be prefixed with `-` for descending order.
            Example : `id` will sort by ascending order, `-id` will sort by descending order.
            Available fields : `id`

        Paginated: pass this method to client.paginate() or client.fetch_all().
        """
        return await self._client.request("GET", f"/api/external/v2/billing_subscriptions/{billing_subscription_id}/invoice_line_sections", params={"cursor": cursor, "limit": limit, "sort": sort})

    async def get_billing_subscription_invoice_lines(self, billing_subscription_id: int | str, *, cursor: str | None = None, limit: int | None = None, sort: str | None = None) -> Any:
        """GET /api/external/v2/billing_subscriptions/{billing_subscription_id}/invoice_lines (getBillingSubscriptionInvoiceLines)

        List invoice lines for a billing subscription

        List invoice lines for a billing subscription

        > ℹ️
        > This endpoint requires one of the following scopes: `billing_subscriptions:all`, `billing_subscriptions:readonly`

        Query params:
          cursor (string): Cursor for pagination. Use this to fetch the next set of results.
            The cursor is an opaque string returned in the previous response's metadata.
            Leave empty for the first request.
          limit (integer): Number of items to return per request.
            Defaults to 20 if not specified.
            Must be between 1 and 100.
          sort (string): You can choose to sort items on specific attributes
            Sort field may be prefixed with `-` for descending order.
            Example : `id` will sort by ascending order, `-id` will sort by descending order.
            Available fields : `id`

        Paginated: pass this method to client.paginate() or client.fetch_all().
        """
        return await self._client.request("GET", f"/api/external/v2/billing_subscriptions/{billing_subscription_id}/invoice_lines", params={"cursor": cursor, "limit": limit, "sort": sort})

    async def get_billing_subscription(self, id: int | str) -> Any:
        """GET /api/external/v2/billing_subscriptions/{id} (getBillingSubscription)

        Get a billing subscription

        This endpoint returns a specific billing subscription.

        > ℹ️
        > This endpoint requires one of the following scopes: `billing_subscriptions:all`, `billing_subscriptions:readonly`
        """
        return await self._client.request("GET", f"/api/external/v2/billing_subscriptions/{id}")

    async def put_billing_subscriptions(self, id: int | str, body: Any, *, validate: bool = True) -> Any:
        """PUT /api/external/v2/billing_subscriptions/{id} (putBillingSubscriptions)

        Update a billing subscription

        Update a billing subscription

        > ℹ️
        > This endpoint requires the following scope: `billing_subscriptions:all`

        Request body: JSON, validated against spec.schema("putBillingSubscriptions").
        """
        return await self._client.request("PUT", f"/api/external/v2/billing_subscriptions/{id}", json=body, validate=validate)



class CategoriesAPI:
    """Operations tagged "categories"."""

    def __init__(self, client) -> None:
        self._client = client

    async def get_categories(self, *, cursor: str | None = None, limit: int | None = None, filter: str | list[dict] | None = None, sort: str | None = None) -> Any:
        """GET /api/external/v2/categories (getCategories)

        List categories

        List categories

        > ℹ️
        > This endpoint requires one of the following scopes: `categories:all`, `categories:readonly`

        Query params:
          cursor (string): Cursor for pagination. Use this to fetch the next set of results.
            The cursor is an opaque string returned in the previous response's metadata.
            Leave empty for the first request.
          limit (integer): Number of items to return per request.
            Defaults to 20 if not specified.
            Must be between 1 and 100.
          filter (string): You can choose to filter items on specific fields.
            Available fields and values:
            - `id` : `lt`, `lteq`, `gt`, `gteq`, `eq`, `not_eq`, `in`, `not_in`
            - `label` : `start_with`, `eq`, `in`
            - `category_group_id` : `lt`, `lteq`, `gt`, `gteq`, `eq`, `not_eq`, `in`, `not_in`
            - `analytical_code` : `eq`, `not_eq`, `in`, `not_in`
          sort (string): You can choose to sort items on specific attributes
            Sort field may be prefixed with `-` for descending order.
            Example : `id` will sort by ascending order, `-id` will sort by descending order.
            Available fields : `id`

        Paginated: pass this method to client.paginate() or client.fetch_all().
        """
        return await self._client.request("GET", "/api/external/v2/categories", params={"cursor": cursor, "limit": limit, "filter": filter, "sort": sort})

    async def post_categories(self, body: Any, *, validate: bool = True) -> Any:
        """POST /api/external/v2/categories (postCategories)

        Create a category

        Create a category

        > ℹ️
        > This endpoint requires the following scope: `categories:all`

        Request body: JSON, validated against spec.schema("postCategories").
        """
        return await self._client.request("POST", "/api/external/v2/categories", json=body, validate=validate)

    async def get_category(self, id: int | str) -> Any:
        """GET /api/external/v2/categories/{id} (getCategory)

        Retrieve a category

        This endpoint returns a specific category.

        > ℹ️
        > This endpoint requires one of the following scopes: `categories:all`, `categories:readonly`
        """
        return await self._client.request("GET", f"/api/external/v2/categories/{id}")

    async def update_category(self, id: int | str, body: Any, *, validate: bool = True) -> Any:
        """PUT /api/external/v2/categories/{id} (updateCategory)

        Update a category

        This endpoint updates a category.

        > ℹ️
        > This endpoint requires the following scope: `categories:all`

        Request body: JSON, validated against spec.schema("updateCategory").
        """
        return await self._client.request("PUT", f"/api/external/v2/categories/{id}", json=body, validate=validate)

    async def get_category_groups(self, *, cursor: str | None = None, limit: int | None = None) -> Any:
        """GET /api/external/v2/category_groups (getCategoryGroups)

        List category groups

        This endpoint returns a list of category groups

        > ℹ️
        > This endpoint requires one of the following scopes: `categories:all`, `categories:readonly`

        Query params:
          cursor (string): Cursor for pagination. Use this to fetch the next set of results.
            The cursor is an opaque string returned in the previous response's metadata.
            Leave empty for the first request.
          limit (integer): Number of items to return per request.
            Defaults to 20 if not specified.
            Must be between 1 and 100.

        Paginated: pass this method to client.paginate() or client.fetch_all().
        """
        return await self._client.request("GET", "/api/external/v2/category_groups", params={"cursor": cursor, "limit": limit})



class CategoryGroupsAPI:
    """Operations tagged "category_groups"."""

    def __init__(self, client) -> None:
        self._client = client

    async def post_category_groups(self, body: Any, *, validate: bool = True) -> Any:
        """POST /api/external/v2/category_groups (postCategoryGroups)

        Create a category group

        Create a category group

        > ℹ️
        > This endpoint requires the following scope: `categories:all`

        Request body: JSON, validated against spec.schema("postCategoryGroups").
        """
        return await self._client.request("POST", "/api/external/v2/category_groups", json=body, validate=validate)

    async def get_category_group_categories(self, category_group_id: int | str, *, cursor: str | None = None, limit: int | None = None) -> Any:
        """GET /api/external/v2/category_groups/{category_group_id}/categories (getCategoryGroupCategories)

        List categories of a category group

        List categories of a category group

        > ℹ️
        > This endpoint requires one of the following scopes: `categories:all`, `categories:readonly`

        Query params:
          cursor (string): Cursor for pagination. Use this to fetch the next set of results.
            The cursor is an opaque string returned in the previous response's metadata.
            Leave empty for the first request.
          limit (integer): Number of items to return per request.
            Defaults to 20 if not specified.
            Must be between 1 and 100.

        Paginated: pass this method to client.paginate() or client.fetch_all().
        """
        return await self._client.request("GET", f"/api/external/v2/category_groups/{category_group_id}/categories", params={"cursor": cursor, "limit": limit})

    async def get_category_group(self, id: int | str) -> Any:
        """GET /api/external/v2/category_groups/{id} (getCategoryGroup)

        Retrieve a category group

        This endpoint returns a specific category group.

        > ℹ️
        > This endpoint requires one of the following scopes: `categories:all`, `categories:readonly`
        """
        return await self._client.request("GET", f"/api/external/v2/category_groups/{id}")

    async def put_category_group(self, id: int | str, body: Any, *, validate: bool = True) -> Any:
        """PUT /api/external/v2/category_groups/{id} (putCategoryGroup)

        Update a category group

        This endpoint updates a category group.

        > ℹ️
        > This endpoint requires the following scope: `categories:all`

        Request body: JSON, validated against spec.schema("putCategoryGroup").
        """
        return await self._client.request("PUT", f"/api/external/v2/category_groups/{id}", json=body, validate=validate)



class ChangelogsAPI:
    """Operations tagged "changelogs"."""

    def __init__(self, client) -> None:
        self._client = client

    async def get_customer_invoices_changes(self, *, cursor: str | None = None, limit: int | None = None, start_date: str | None = None) -> Any:
        """GET /api/external/v2/changelogs/customer_invoices (getCustomerInvoicesChanges)

        Get customer invoices changes events

        Returns the list of changes based on the provided `start_date`.
        If no `start_date` is provided it returns the oldest set of recorded changes.
        Changes for the last 4 weeks are retained. The items will be returned using
        `processed_at` in ASC order (oldest first).


        > ℹ️
        > This endpoint requires one of the following scopes: `customer_invoices:all`, `customer_invoices:readonly`

        Query params:
          cursor (string): Cursor for pagination. Use this to fetch the next set of results. The cursor is an opaque string returned in the previous response's metadata. Leave empty for the first request.
          limit (integer): Number of items to return per request.
            Defaults to 20 if not specified.
            Must be between 1 and 1000.
          start_date (string): Filter the changes based on the event date. The date should follow RFC3339 format. If no date is provided, the oldest changes will be returned. Changes for the last 4 weeks are retained, thus providing a `start_date` older than that will result in a 422 response. Providing both `start_date` and `cursor` parameters will result in a 400 response.

        Paginated: pass this method to client.paginate() or client.fetch_all().
        """
        return await self._client.request("GET", "/api/external/v2/changelogs/customer_invoices", params={"cursor": cursor, "limit": limit, "start_date": start_date})

    async def get_customer_changes(self, *, cursor: str | None = None, limit: int | None = None, start_date: str | None = None) -> Any:
        """GET /api/external/v2/changelogs/customers (getCustomerChanges)

        Get customer changes events

        Returns the list of changes based on the provided `start_date`.
        If no `start_date` is provided it returns the oldest set of recorded changes.
        Changes for the last 4 weeks are retained. The items will be returned using
        `processed_at` in ASC order (oldest first).


        > ℹ️
        > This endpoint requires one of the following scopes: `customers:all`, `customers:readonly`

        Query params:
          cursor (string): Cursor for pagination. Use this to fetch the next set of results. The cursor is an opaque string returned in the previous response's metadata. Leave empty for the first request.
          limit (integer): Number of items to return per request.
            Defaults to 20 if not specified.
            Must be between 1 and 1000.
          start_date (string): Filter the changes based on the event date. The date should follow RFC3339 format. If no date is provided, the oldest changes will be returned. Changes for the last 4 weeks are retained, thus providing a `start_date` older than that will result in a 422 response. Providing both `start_date` and `cursor` parameters will result in a 400 response.

        Paginated: pass this method to client.paginate() or client.fetch_all().
        """
        return await self._client.request("GET", "/api/external/v2/changelogs/customers", params={"cursor": cursor, "limit": limit, "start_date": start_date})

    async def get_ledger_entries_category_changes(self, *, cursor: str | None = None, limit: int | None = None, start_date: str | None = None) -> Any:
        """GET /api/external/v2/changelogs/ledger_entries_categories (getLedgerEntriesCategoryChanges)

        Get ledger entry category change events

        Returns the list of changes based on the provided `start_date`.
        If no `start_date` is provided it returns the oldest set of recorded changes.
        Changes for the last 4 weeks are retained. The items will be returned using
        `processed_at` in ASC order (oldest first).

        A ledger entry category change indicates that a category was added to or removed from a
        ledger entry (e.g. a customer invoice, a supplier invoice). Use `ledger_entry.id`
        and `ledger_entry.type` to identify the underlying resource to refetch.


        > ℹ️
        > This endpoint requires one of the following scopes: `ledger_entries:readonly`, `ledger_entries:all`

        Query params:
          cursor (string): Cursor for pagination. Use this to fetch the next set of results. The cursor is an opaque string returned in the previous response's metadata. Leave empty for the first request.
          limit (integer): Number of items to return per request.
            Defaults to 20 if not specified.
            Must be between 1 and 1000.
          start_date (string): Filter the changes based on the event date. The date should follow RFC3339 format. If no date is provided, the oldest changes will be returned. Changes for the last 4 weeks are retained, thus providing a `start_date` older than that will result in a 422 response. Providing both `start_date` and `cursor` parameters will result in a 400 response.

        Paginated: pass this method to client.paginate() or client.fetch_all().
        """
        return await self._client.request("GET", "/api/external/v2/changelogs/ledger_entries_categories", params={"cursor": cursor, "limit": limit, "start_date": start_date})

    async def get_ledger_entry_line_changes(self, *, cursor: str | None = None, limit: int | None = None, start_date: str | None = None) -> Any:
        """GET /api/external/v2/changelogs/ledger_entry_lines (getLedgerEntryLineChanges)

        Get ledger entry line change events

        Returns the list of changes based on the provided `start_date`.
        If no `start_date` is provided it returns the oldest set of recorded changes.
        Changes for the last 4 weeks are retained. The items will be returned using
        `processed_at` in ASC order (oldest first).


        > ℹ️
        > This endpoint requires one of the following scopes: `ledger_entries:readonly`, `ledger_entries:all`

        Query params:
          cursor (string): Cursor for pagination. Use this to fetch the next set of results. The cursor is an opaque string returned in the previous response's metadata. Leave empty for the first request.
          limit (integer): Number of items to return per request.
            Defaults to 20 if not specified.
            Must be between 1 and 1000.
          start_date (string): Filter the changes based on the event date. The date should follow RFC3339 format. If no date is provided, the oldest changes will be returned. Changes for the last 4 weeks are retained, thus providing a `start_date` older than that will result in a 422 response. Providing both `start_date` and `cursor` parameters will result in a 400 response.

        Paginated: pass this method to client.paginate() or client.fetch_all().
        """
        return await self._client.request("GET", "/api/external/v2/changelogs/ledger_entry_lines", params={"cursor": cursor, "limit": limit, "start_date": start_date})

    async def get_ledger_entry_lines_category_changes(self, *, cursor: str | None = None, limit: int | None = None, start_date: str | None = None) -> Any:
        """GET /api/external/v2/changelogs/ledger_entry_lines_categories (getLedgerEntryLinesCategoryChanges)

        Get ledger entry line category change events

        Returns the list of changes based on the provided `start_date`.
        If no `start_date` is provided it returns the oldest set of recorded changes.
        Changes for the last 4 weeks are retained. The items will be returned using
        `processed_at` in ASC order (oldest first).

        A ledger entry line category change indicates that a category was added to or removed from a
        ledger entry line. Use `ledger_entry_line.id` to identify the underlying resource to refetch.
        `ledger_entry_line` may be `null` if the ledger entry line itself was uncategoryged and deleted
        in the same operation.


        > ℹ️
        > This endpoint requires one of the following scopes: `ledger_entries:readonly`, `ledger_entries:all`

        Query params:
          cursor (string): Cursor for pagination. Use this to fetch the next set of results. The cursor is an opaque string returned in the previous response's metadata. Leave empty for the first request.
          limit (integer): Number of items to return per request.
            Defaults to 20 if not specified.
            Must be between 1 and 1000.
          start_date (string): Filter the changes based on the event date. The date should follow RFC3339 format. If no date is provided, the oldest changes will be returned. Changes for the last 4 weeks are retained, thus providing a `start_date` older than that will result in a 422 response. Providing both `start_date` and `cursor` parameters will result in a 400 response.

        Paginated: pass this method to client.paginate() or client.fetch_all().
        """
        return await self._client.request("GET", "/api/external/v2/changelogs/ledger_entry_lines_categories", params={"cursor": cursor, "limit": limit, "start_date": start_date})

    async def get_product_changes(self, *, cursor: str | None = None, limit: int | None = None, start_date: str | None = None) -> Any:
        """GET /api/external/v2/changelogs/products (getProductChanges)

        Get product change events

        Returns the list of changes based on the provided `start_date`.
        If no `start_date` is provided it returns the oldest set of recorded changes.
        Changes for the last 4 weeks are retained. The items will be returned using
        `processed_at` in ASC order (oldest first).


        > ℹ️
        > This endpoint requires one of the following scopes: `products:all`, `products:readonly`

        Query params:
          cursor (string): Cursor for pagination. Use this to fetch the next set of results. The cursor is an opaque string returned in the previous response's metadata. Leave empty for the first request.
          limit (integer): Number of items to return per request.
            Defaults to 20 if not specified.
            Must be between 1 and 1000.
          start_date (string): Filter the changes based on the event date. The date should follow RFC3339 format. If no date is provided, the oldest changes will be returned. Changes for the last 4 weeks are retained, thus providing a `start_date` older than that will result in a 422 response. Providing both `start_date` and `cursor` parameters will result in a 400 response.

        Paginated: pass this method to client.paginate() or client.fetch_all().
        """
        return await self._client.request("GET", "/api/external/v2/changelogs/products", params={"cursor": cursor, "limit": limit, "start_date": start_date})

    async def get_supplier_invoices_changes(self, *, cursor: str | None = None, limit: int | None = None, start_date: str | None = None) -> Any:
        """GET /api/external/v2/changelogs/supplier_invoices (getSupplierInvoicesChanges)

        Get supplier invoices changes events

        Returns the list of changes based on the provided `start_date`.
        If no `start_date` is provided it returns the oldest set of recorded changes.
        Changes for the last 4 weeks are retained. The items will be returned using
        `processed_at` in ASC order (oldest first).


        > ℹ️
        > This endpoint requires one of the following scopes: `supplier_invoices:all`, `supplier_invoices:readonly`

        Query params:
          cursor (string): Cursor for pagination. Use this to fetch the next set of results. The cursor is an opaque string returned in the previous response's metadata. Leave empty for the first request.
          limit (integer): Number of items to return per request.
            Defaults to 20 if not specified.
            Must be between 1 and 1000.
          start_date (string): Filter the changes based on the event date. The date should follow RFC3339 format. If no date is provided, the oldest changes will be returned. Changes for the last 4 weeks are retained, thus providing a `start_date` older than that will result in a 422 response. Providing both `start_date` and `cursor` parameters will result in a 400 response.

        Paginated: pass this method to client.paginate() or client.fetch_all().
        """
        return await self._client.request("GET", "/api/external/v2/changelogs/supplier_invoices", params={"cursor": cursor, "limit": limit, "start_date": start_date})

    async def get_supplier_changes(self, *, cursor: str | None = None, limit: int | None = None, start_date: str | None = None) -> Any:
        """GET /api/external/v2/changelogs/suppliers (getSupplierChanges)

        Get supplier changes events

        Returns the list of changes based on the provided `start_date`.
        If no `start_date` is provided it returns the oldest set of recorded changes.
        Changes for the last 4 weeks are retained. The items will be returned using
        `processed_at` in ASC order (oldest first).


        > ℹ️
        > This endpoint requires one of the following scopes: `suppliers:all`, `suppliers:readonly`

        Query params:
          cursor (string): Cursor for pagination. Use this to fetch the next set of results. The cursor is an opaque string returned in the previous response's metadata. Leave empty for the first request.
          limit (integer): Number of items to return per request.
            Defaults to 20 if not specified.
            Must be between 1 and 1000.
          start_date (string): Filter the changes based on the event date. The date should follow RFC3339 format. If no date is provided, the oldest changes will be returned. Changes for the last 4 weeks are retained, thus providing a `start_date` older than that will result in a 422 response. Providing both `start_date` and `cursor` parameters will result in a 400 response.

        Paginated: pass this method to client.paginate() or client.fetch_all().
        """
        return await self._client.request("GET", "/api/external/v2/changelogs/suppliers", params={"cursor": cursor, "limit": limit, "start_date": start_date})

    async def get_transaction_changes(self, *, cursor: str | None = None, limit: int | None = None, start_date: str | None = None) -> Any:
        """GET /api/external/v2/changelogs/transactions (getTransactionChanges)

        Get transaction change events

        Returns the list of changes based on the provided `start_date`.
        If no `start_date` is provided it returns the oldest set of recorded changes.
        Changes for the last 4 weeks are retained. The items will be returned using
        `processed_at` in ASC order (oldest first).


        > ℹ️
        > This endpoint requires one of the following scopes: `transactions:all`, `transactions:readonly`

        Query params:
          cursor (string): Cursor for pagination. Use this to fetch the next set of results. The cursor is an opaque string returned in the previous response's metadata. Leave empty for the first request.
          limit (integer): Number of items to return per request.
            Defaults to 20 if not specified.
            Must be between 1 and 1000.
          start_date (string): Filter the changes based on the event date. The date should follow RFC3339 format. If no date is provided, the oldest changes will be returned. Changes for the last 4 weeks are retained, thus providing a `start_date` older than that will result in a 422 response. Providing both `start_date` and `cursor` parameters will result in a 400 response.

        Paginated: pass this method to client.paginate() or client.fetch_all().
        """
        return await self._client.request("GET", "/api/external/v2/changelogs/transactions", params={"cursor": cursor, "limit": limit, "start_date": start_date})



class CommercialDocumentsAPI:
    """Operations tagged "commercial_documents"."""

    def __init__(self, client) -> None:
        self._client = client

    async def list_commercial_documents(self, *, cursor: str | None = None, limit: int | None = None, filter: str | list[dict] | None = None, sort: str | None = None) -> Any:
        """GET /api/external/v2/commercial_documents (listCommercialDocuments)

        List commercial documents

        This endpoint lists commercial documents.

        > ℹ️
        > This endpoint requires one of the following scopes: `commercial_documents:all`, `commercial_documents:readonly`

        Query params:
          cursor (string): Cursor for pagination. Use this to fetch the next set of results.
            The cursor is an opaque string returned in the previous response's metadata.
            Leave empty for the first request.
          limit (integer): Number of items to return per request.
            Defaults to 20 if not specified.
            Must be between 1 and 100.
          filter (string): You can choose to filter items on specific fields.
            Available fields and operators:
            - `id`, `customer_id`: `lt`, `lteq`, `gt`, `gteq`, `eq`, `not_eq`, `in`, `not_in`
            - `document_type`: `eq`, `not_eq`, `in`, `not_in`

            Available document_types:
            - proforma
            - shipping_order
            - purchasing_order
          sort (string): You can choose to sort items on specific attributes
            Sort field may be prefixed with `-` for descending order.
            Example : `id` will sort by ascending order, `-id` will sort by descending order.
            Available fields : `id`

        Paginated: pass this method to client.paginate() or client.fetch_all().
        """
        return await self._client.request("GET", "/api/external/v2/commercial_documents", params={"cursor": cursor, "limit": limit, "filter": filter, "sort": sort})

    async def post_commercial_documents(self, body: Any, *, validate: bool = True) -> Any:
        """POST /api/external/v2/commercial_documents (postCommercialDocuments)

        Create a commercial document

        This endpoint allows you to create a commercial document (proforma,
        shipping order or purchasing order).

        The document number is assigned by Pennylane, based on the numbering
        configured for this type of document.


        > ℹ️
        > This endpoint requires the following scope: `commercial_documents:all`

        Request body: JSON, validated against spec.schema("postCommercialDocuments").
        """
        return await self._client.request("POST", "/api/external/v2/commercial_documents", json=body, validate=validate)

    async def get_commercial_document_appendices(self, commercial_document_id: int | str, *, cursor: str | None = None, limit: int | None = None) -> Any:
        """GET /api/external/v2/commercial_documents/{commercial_document_id}/appendices (getCommercialDocumentAppendices)

        List appendices of a commercial document

        List appendices of a commercial document

        > ℹ️
        > This endpoint requires one of the following scopes: `commercial_documents:all`, `commercial_documents:readonly`

        Query params:
          cursor (string): Cursor for pagination. Use this to fetch the next set of results.
            The cursor is an opaque string returned in the previous response's metadata.
            Leave empty for the first request.
          limit (integer): Number of items to return per request.
            Defaults to 20 if not specified.
            Must be between 1 and 100.

        Paginated: pass this method to client.paginate() or client.fetch_all().
        """
        return await self._client.request("GET", f"/api/external/v2/commercial_documents/{commercial_document_id}/appendices", params={"cursor": cursor, "limit": limit})

    async def post_commercial_document_appendices(self, commercial_document_id: int | str, files: Any, data: dict | None = None) -> Any:
        """POST /api/external/v2/commercial_documents/{commercial_document_id}/appendices (postCommercialDocumentAppendices)

        Upload an appendix for a commercial document

        Upload a file that will be an appendix attached to a commercial document.

        Note that this will not upload a file into the DMS (GED).


        > ℹ️
        > This endpoint requires the following scope: `commercial_documents:all`

        Request body: multipart/form-data (files=..., data=...), not validated.
        """
        return await self._client.request("POST", f"/api/external/v2/commercial_documents/{commercial_document_id}/appendices", files=files, data=data)

    async def get_commercial_document_invoice_line_sections(self, commercial_document_id: int | str, *, cursor: str | None = None, limit: int | None = None, sort: str | None = None) -> Any:
        """GET /api/external/v2/commercial_documents/{commercial_document_id}/invoice_line_sections (getCommercialDocumentInvoiceLineSections)

        List invoice line sections for a commercial document

        List invoice line sections for a commercial document

        > ℹ️
        > This endpoint requires one of the following scopes: `commercial_documents:all`, `commercial_documents:readonly`

        Query params:
          cursor (string): Cursor for pagination. Use this to fetch the next set of results.
            The cursor is an opaque string returned in the previous response's metadata.
            Leave empty for the first request.
          limit (integer): Number of items to return per request.
            Defaults to 20 if not specified.
            Must be between 1 and 100.
          sort (string): You can choose to sort items on specific attributes
            Sort field may be prefixed with `-` for descending order.
            Example : `id` will sort by ascending order, `-id` will sort by descending order.
            Available fields : `id`

        Paginated: pass this method to client.paginate() or client.fetch_all().
        """
        return await self._client.request("GET", f"/api/external/v2/commercial_documents/{commercial_document_id}/invoice_line_sections", params={"cursor": cursor, "limit": limit, "sort": sort})

    async def get_commercial_document_invoice_lines(self, commercial_document_id: int | str, *, cursor: str | None = None, limit: int | None = None, sort: str | None = None) -> Any:
        """GET /api/external/v2/commercial_documents/{commercial_document_id}/invoice_lines (getCommercialDocumentInvoiceLines)

        List invoice lines for a commercial document

        List invoice lines for a commercial document

        > ℹ️
        > This endpoint requires one of the following scopes: `commercial_documents:all`, `commercial_documents:readonly`

        Query params:
          cursor (string): Cursor for pagination. Use this to fetch the next set of results.
            The cursor is an opaque string returned in the previous response's metadata.
            Leave empty for the first request.
          limit (integer): Number of items to return per request.
            Defaults to 20 if not specified.
            Must be between 1 and 100.
          sort (string): You can choose to sort items on specific attributes
            Sort field may be prefixed with `-` for descending order.
            Example : `id` will sort by ascending order, `-id` will sort by descending order.
            Available fields : `id`

        Paginated: pass this method to client.paginate() or client.fetch_all().
        """
        return await self._client.request("GET", f"/api/external/v2/commercial_documents/{commercial_document_id}/invoice_lines", params={"cursor": cursor, "limit": limit, "sort": sort})

    async def get_commercial_document(self, id: int | str) -> Any:
        """GET /api/external/v2/commercial_documents/{id} (getCommercialDocument)

        Retrieve a commercial document

        This endpoint retrieves a commercial document.

        > ℹ️
        > This endpoint requires one of the following scopes: `commercial_documents:all`, `commercial_documents:readonly`
        """
        return await self._client.request("GET", f"/api/external/v2/commercial_documents/{id}")

    async def update_commercial_document(self, id: int | str, body: Any, *, validate: bool = True) -> Any:
        """PUT /api/external/v2/commercial_documents/{id} (updateCommercialDocument)

        Update a commercial document

        This endpoint allows you to update a commercial document.

        Only the fields present in the payload are applied. The document type
        and the document number cannot be changed after creation.


        > ℹ️
        > This endpoint requires the following scope: `commercial_documents:all`

        Request body: JSON, validated against spec.schema("updateCommercialDocument").
        """
        return await self._client.request("PUT", f"/api/external/v2/commercial_documents/{id}", json=body, validate=validate)



class CustomerInvoiceTemplatesAPI:
    """Operations tagged "customer_invoice_templates"."""

    def __init__(self, client) -> None:
        self._client = client

    async def get_customer_invoice_templates(self, *, cursor: str | None = None, limit: int | None = None, sort: str | None = None) -> Any:
        """GET /api/external/v2/customer_invoice_templates (getCustomerInvoiceTemplates)

        List customer invoice templates

        List customer invoice templates

        > ℹ️
        > This endpoint requires the following scope: `customer_invoice_templates:readonly`

        Query params:
          cursor (string): Cursor for pagination. Use this to fetch the next set of results.
            The cursor is an opaque string returned in the previous response's metadata.
            Leave empty for the first request.
          limit (integer): Number of items to return per request.
            Defaults to 20 if not specified.
            Must be between 1 and 100.
          sort (string): You can choose to sort items on specific attributes
            Sort field may be prefixed with `-` for descending order.
            Example : `id` will sort by ascending order, `-id` will sort by descending order.
            Available fields : `id`

        Paginated: pass this method to client.paginate() or client.fetch_all().
        """
        return await self._client.request("GET", "/api/external/v2/customer_invoice_templates", params={"cursor": cursor, "limit": limit, "sort": sort})



class CustomerInvoicesAPI:
    """Operations tagged "customer_invoices"."""

    def __init__(self, client) -> None:
        self._client = client

    async def get_customer_invoices(self, *, cursor: str | None = None, limit: int | None = None, filter: str | list[dict] | None = None, sort: str | None = None, include: str | None = None) -> Any:
        """GET /api/external/v2/customer_invoices (getCustomerInvoices)

        List customer invoices

        List customer invoices and credit notes

        > ℹ️
        > This endpoint requires one of the following scopes: `customer_invoices:all`, `customer_invoices:readonly`

        Query params:
          cursor (string): Cursor for pagination. Use this to fetch the next set of results.
            The cursor is an opaque string returned in the previous response's metadata.
            Leave empty for the first request.
          limit (integer): Number of items to return per request.
            Defaults to 20 if not specified.
            Must be between 1 and 100.
          filter (string): You can choose to filter items on specific fields.
            Available fields and values:
            - `id`, `date`, `customer_id`, `billing_subscription_id`, `quote_id`: `lt`, `lteq`, `gt`, `gteq`, `eq`, `not_eq`, `in`, `not_in`
            - `invoice_number`: `eq`, `not_eq`, `in`, `not_in`
            - `draft`: `eq` (boolean)
            - `credit_note`: `eq` (boolean)
            - `external_reference`: `eq`
            - `flow_id`: `eq`, `not_eq`, `in`, `not_in`
            - `category_id`: `in`
          sort (string): You can choose to sort items on specific attributes
            Sort field may be prefixed with `-` for descending order.
            Example : `id` will sort by ascending order, `-id` will sort by descending order.
            Available fields : `id`, `date`
          include (string): You can choose to include additional related resources in the response.
            When specified, related resources will be returned in a separate `included` section.
            Available includes: `invoice_lines`

            ⚠️ **Warning**: This feature is currently experimental and may change or be removed in future releases.
            We recommend using it with caution in production environments.

        Paginated: pass this method to client.paginate() or client.fetch_all().
        """
        return await self._client.request("GET", "/api/external/v2/customer_invoices", params={"cursor": cursor, "limit": limit, "filter": filter, "sort": sort, "include": include})

    async def post_customer_invoices(self, body: Any, *, validate: bool = True) -> Any:
        """POST /api/external/v2/customer_invoices (postCustomerInvoices)

        Create a customer invoice

        This endpoint allows you to create a draft or finalized customer
        invoice or credit note


        > ℹ️
        > This endpoint requires the following scope: `customer_invoices:all`

        Request body: JSON, validated against spec.schema("postCustomerInvoices").
        """
        return await self._client.request("POST", "/api/external/v2/customer_invoices", json=body, validate=validate)

    async def create_customer_invoice_from_quote(self, body: Any, *, validate: bool = True) -> Any:
        """POST /api/external/v2/customer_invoices/create_from_quote (createCustomerInvoiceFromQuote)

        Create a customer invoice from a quote

        This endpoint allows you to create a customer invoice from an existing quote.
        The invoice will inherit the quote's data (customer, lines, etc.).


        > ℹ️
        > This endpoint requires the following scope: `customer_invoices:all`

        Request body: JSON, validated against spec.schema("createCustomerInvoiceFromQuote").
        """
        return await self._client.request("POST", "/api/external/v2/customer_invoices/create_from_quote", json=body, validate=validate)

    async def create_customer_invoice_einvoice_import(self, files: Any, data: dict | None = None) -> Any:
        """POST /api/external/v2/customer_invoices/e_invoices/imports (createCustomerInvoiceEInvoiceImport)

        Import a customer e-invoice

        Import a customer invoice from an e-invoice file.
        The file must be a Factur-X PDF, a standalone UBL XML invoice, or a standalone CII XML invoice.
        Optionally provide `invoice_options` to pre-fill customer and line-level data.
        Invoice line `e_invoice_line_id` must match Factur-X BT-126 (LineID) or the UBL/CII line identifier.

        > ⚠️ **UBL and CII XML support is in alpha.**
        > A 201 response confirms the file was accepted and parsed, but invoices imported via
        > standalone UBL or CII XML have two known limitations:
        > - The uploaded file is **not displayed** in the app — no document preview is generated yet for these formats.
        > - The invoice is **not recognized as an electronic invoice** within Pennylane.
        >
        > Factur-X PDF remains the recommended format for production use.


        > ℹ️
        > This endpoint requires the following scope: `customer_invoices:all`

        Request body: multipart/form-data (files=..., data=...), not validated.
        """
        return await self._client.request("POST", "/api/external/v2/customer_invoices/e_invoices/imports", files=files, data=data)

    async def import_customer_invoices(self, body: Any, *, validate: bool = True) -> Any:
        """POST /api/external/v2/customer_invoices/import (importCustomerInvoices)

        Import an invoice with file attached

        This endpoint allows you to import an invoice. Amounts are stored exactly as provided — Pennylane does not recalculate or round them.

        ℹ️ **Amount consistency:** The amounts you send must be internally coherent:
        - `currency_amount_before_tax + currency_tax` must equal `currency_amount`.
        - The sum of invoice line `currency_tax` values must match the invoice-level `currency_tax`.
        - The sum of invoice line `currency_amount` values must match the invoice-level `currency_amount`.

        Small rounding differences are tolerated. When `convert_to_e_invoice` is `true`, stricter requirements apply — see that field's description.


        > ℹ️
        > This endpoint requires the following scope: `customer_invoices:all`

        Request body: JSON, validated against spec.schema("importCustomerInvoices").
        """
        return await self._client.request("POST", "/api/external/v2/customer_invoices/import", json=body, validate=validate)

    async def get_customer_invoice_appendices(self, customer_invoice_id: int | str, *, cursor: str | None = None, limit: int | None = None) -> Any:
        """GET /api/external/v2/customer_invoices/{customer_invoice_id}/appendices (getCustomerInvoiceAppendices)

        List appendices of a customer invoice

        List appendices of a customer invoice

        > ℹ️
        > This endpoint requires one of the following scopes: `customer_invoices:all`, `customer_invoices:readonly`

        Query params:
          cursor (string): Cursor for pagination. Use this to fetch the next set of results.
            The cursor is an opaque string returned in the previous response's metadata.
            Leave empty for the first request.
          limit (integer): Number of items to return per request.
            Defaults to 20 if not specified.
            Must be between 1 and 100.

        Paginated: pass this method to client.paginate() or client.fetch_all().
        """
        return await self._client.request("GET", f"/api/external/v2/customer_invoices/{customer_invoice_id}/appendices", params={"cursor": cursor, "limit": limit})

    async def post_customer_invoice_appendices(self, customer_invoice_id: int | str, files: Any, data: dict | None = None) -> Any:
        """POST /api/external/v2/customer_invoices/{customer_invoice_id}/appendices (postCustomerInvoiceAppendices)

        Upload an appendix for a customer invoice

        Upload a file that will be an appendix attached to a customer invoice.

        Note that this will not upload a file into the DMS (GED).


        > ℹ️
        > This endpoint requires the following scope: `customer_invoices:all`

        Request body: multipart/form-data (files=..., data=...), not validated.
        """
        return await self._client.request("POST", f"/api/external/v2/customer_invoices/{customer_invoice_id}/appendices", files=files, data=data)

    async def get_customer_invoice_categories(self, customer_invoice_id: int | str, *, cursor: str | None = None, limit: int | None = None) -> Any:
        """GET /api/external/v2/customer_invoices/{customer_invoice_id}/categories (getCustomerInvoiceCategories)

        List categories of a customer invoice

        List categories of a customer invoice

        > ℹ️
        > This endpoint requires one of the following scopes: `customer_invoices:all`, `customer_invoices:readonly`

        Query params:
          cursor (string): Cursor for pagination. Use this to fetch the next set of results.
            The cursor is an opaque string returned in the previous response's metadata.
            Leave empty for the first request.
          limit (integer): Number of items to return per request.
            Defaults to 20 if not specified.
            Must be between 1 and 100.

        Paginated: pass this method to client.paginate() or client.fetch_all().
        """
        return await self._client.request("GET", f"/api/external/v2/customer_invoices/{customer_invoice_id}/categories", params={"cursor": cursor, "limit": limit})

    async def put_customer_invoice_categories(self, customer_invoice_id: int | str, body: Any, *, validate: bool = True) -> Any:
        """PUT /api/external/v2/customer_invoices/{customer_invoice_id}/categories (putCustomerInvoiceCategories)

        Categorize a customer invoice

        This endpoint is not applicable for draft invoices.
        Update the categories of a customer invoice. You can pass categories that don't belong to the same category group. The sum of categories of a same group must equal `1`. In the following example, the two first categories belong to the same category group A, the sum of the weights is `1`. The third category belongs to a category group B, its weight is `1`.
        ```
        [
          { "id": 59, "weight": "0.5" }, // category group A
          { "id": 33, "weight": "0.5" }, // category group A
          { "id": 65, "weight": "1" } // category group B
        ]
        ```


        > ℹ️
        > This endpoint requires the following scope: `customer_invoices:all`

        Request body: JSON, validated against spec.schema("putCustomerInvoiceCategories").
        """
        return await self._client.request("PUT", f"/api/external/v2/customer_invoices/{customer_invoice_id}/categories", json=body, validate=validate)

    async def get_customer_invoice_custom_header_fields(self, customer_invoice_id: int | str, *, cursor: str | None = None, limit: int | None = None, sort: str | None = None) -> Any:
        """GET /api/external/v2/customer_invoices/{customer_invoice_id}/custom_header_fields (getCustomerInvoiceCustomHeaderFields)

        List custom header fields for a customer invoice

        List custom header fields for a customer invoice

        > ℹ️
        > This endpoint requires one of the following scopes: `customer_invoices:all`, `customer_invoices:readonly`

        Query params:
          cursor (string): Cursor for pagination. Use this to fetch the next set of results.
            The cursor is an opaque string returned in the previous response's metadata.
            Leave empty for the first request.
          limit (integer): Number of items to return per request.
            Defaults to 20 if not specified.
            Must be between 1 and 100.
          sort (string): You can choose to sort items on specific attributes
            Sort field may be prefixed with `-` for descending order.
            Example : `id` will sort by ascending order, `-id` will sort by descending order.
            Available fields : `id`

        Paginated: pass this method to client.paginate() or client.fetch_all().
        """
        return await self._client.request("GET", f"/api/external/v2/customer_invoices/{customer_invoice_id}/custom_header_fields", params={"cursor": cursor, "limit": limit, "sort": sort})

    async def get_customer_invoice_invoice_line_sections(self, customer_invoice_id: int | str, *, cursor: str | None = None, limit: int | None = None, sort: str | None = None) -> Any:
        """GET /api/external/v2/customer_invoices/{customer_invoice_id}/invoice_line_sections (getCustomerInvoiceInvoiceLineSections)

        List invoice line sections for a customer invoice

        List invoice line sections for a customer invoice

        > ℹ️
        > This endpoint requires one of the following scopes: `customer_invoices:all`, `customer_invoices:readonly`

        Query params:
          cursor (string): Cursor for pagination. Use this to fetch the next set of results.
            The cursor is an opaque string returned in the previous response's metadata.
            Leave empty for the first request.
          limit (integer): Number of items to return per request.
            Defaults to 20 if not specified.
            Must be between 1 and 100.
          sort (string): You can choose to sort items on specific attributes
            Sort field may be prefixed with `-` for descending order.
            Example : `id` will sort by ascending order, `-id` will sort by descending order.
            Available fields : `id`

        Paginated: pass this method to client.paginate() or client.fetch_all().
        """
        return await self._client.request("GET", f"/api/external/v2/customer_invoices/{customer_invoice_id}/invoice_line_sections", params={"cursor": cursor, "limit": limit, "sort": sort})

    async def get_customer_invoice_invoice_lines(self, customer_invoice_id: int | str, *, cursor: str | None = None, limit: int | None = None, sort: str | None = None) -> Any:
        """GET /api/external/v2/customer_invoices/{customer_invoice_id}/invoice_lines (getCustomerInvoiceInvoiceLines)

        List invoice lines for a customer invoice

        List invoice lines for a customer invoice

        > ℹ️
        > This endpoint requires one of the following scopes: `customer_invoices:all`, `customer_invoices:readonly`

        Query params:
          cursor (string): Cursor for pagination. Use this to fetch the next set of results.
            The cursor is an opaque string returned in the previous response's metadata.
            Leave empty for the first request.
          limit (integer): Number of items to return per request.
            Defaults to 20 if not specified.
            Must be between 1 and 100.
          sort (string): You can choose to sort items on specific attributes
            Sort field may be prefixed with `-` for descending order.
            Example : `id` will sort by ascending order, `-id` will sort by descending order.
            Available fields : `id`, `rank`

        Paginated: pass this method to client.paginate() or client.fetch_all().
        """
        return await self._client.request("GET", f"/api/external/v2/customer_invoices/{customer_invoice_id}/invoice_lines", params={"cursor": cursor, "limit": limit, "sort": sort})

    async def get_customer_invoice_matched_transactions(self, customer_invoice_id: int | str, *, cursor: str | None = None, limit: int | None = None, sort: str | None = None) -> Any:
        """GET /api/external/v2/customer_invoices/{customer_invoice_id}/matched_transactions (getCustomerInvoiceMatchedTransactions)

        List matched transactions for a customer invoice

        List matched transactions for a customer invoice

        > ℹ️
        > This endpoint requires one of the following scopes: `customer_invoices:all`, `customer_invoices:readonly`

        Query params:
          cursor (string): Cursor for pagination. Use this to fetch the next set of results.
            The cursor is an opaque string returned in the previous response's metadata.
            Leave empty for the first request.
          limit (integer): Number of items to return per request.
            Defaults to 20 if not specified.
            Must be between 1 and 100.
          sort (string): You can choose to sort items on specific attributes
            Sort field may be prefixed with `-` for descending order.
            Example : `id` will sort by ascending order, `-id` will sort by descending order.
            Available fields : `id`

        Paginated: pass this method to client.paginate() or client.fetch_all().
        """
        return await self._client.request("GET", f"/api/external/v2/customer_invoices/{customer_invoice_id}/matched_transactions", params={"cursor": cursor, "limit": limit, "sort": sort})

    async def get_customer_invoice_payments(self, customer_invoice_id: int | str, *, cursor: str | None = None, limit: int | None = None, sort: str | None = None) -> Any:
        """GET /api/external/v2/customer_invoices/{customer_invoice_id}/payments (getCustomerInvoicePayments)

        List payments for a customer invoice

        List payments for a customer invoice

        > ℹ️
        > This endpoint requires one of the following scopes: `customer_invoices:all`, `customer_invoices:readonly`

        Query params:
          cursor (string): Cursor for pagination. Use this to fetch the next set of results.
            The cursor is an opaque string returned in the previous response's metadata.
            Leave empty for the first request.
          limit (integer): Number of items to return per request.
            Defaults to 20 if not specified.
            Must be between 1 and 100.
          sort (string): You can choose to sort items on specific attributes
            Sort field may be prefixed with `-` for descending order.
            Example : `id` will sort by ascending order, `-id` will sort by descending order.
            Available fields : `id`

        Paginated: pass this method to client.paginate() or client.fetch_all().
        """
        return await self._client.request("GET", f"/api/external/v2/customer_invoices/{customer_invoice_id}/payments", params={"cursor": cursor, "limit": limit, "sort": sort})

    async def delete_customer_invoices(self, id: int | str) -> Any:
        """DELETE /api/external/v2/customer_invoices/{id} (deleteCustomerInvoices)

        Delete draft invoice

        Delete a draft customer invoice or draft credit note

        > ℹ️
        > This endpoint requires the following scope: `customer_invoices:all`
        """
        return await self._client.request("DELETE", f"/api/external/v2/customer_invoices/{id}")

    async def get_customer_invoice(self, id: int | str) -> Any:
        """GET /api/external/v2/customer_invoices/{id} (getCustomerInvoice)

        Retrieve a customer invoice

        Retrieve a customer invoice or a credit note

        > ℹ️
        > This endpoint requires one of the following scopes: `customer_invoices:all`, `customer_invoices:readonly`
        """
        return await self._client.request("GET", f"/api/external/v2/customer_invoices/{id}")

    async def update_customer_invoice(self, id: int | str, body: Any, *, validate: bool = True) -> Any:
        """PUT /api/external/v2/customer_invoices/{id} (updateCustomerInvoice)

        Update a customer invoice

        Update a customer invoice

        > ℹ️
        > This endpoint requires the following scope: `customer_invoices:all`

        Request body: JSON, validated against spec.schema("updateCustomerInvoice").
        """
        return await self._client.request("PUT", f"/api/external/v2/customer_invoices/{id}", json=body, validate=validate)

    async def finalize_customer_invoice(self, id: int | str) -> Any:
        """PUT /api/external/v2/customer_invoices/{id}/finalize (finalizeCustomerInvoice)

        Turn the draft invoice into a finalized invoice.

        Convert the draft customer invoice or credit note into a finalized
        one. Once finalized, the resource can no longer be edited.


        > ℹ️
        > This endpoint requires the following scope: `customer_invoices:all`
        """
        return await self._client.request("PUT", f"/api/external/v2/customer_invoices/{id}/finalize")

    async def link_credit_note(self, id: int | str, body: Any, *, validate: bool = True) -> Any:
        """POST /api/external/v2/customer_invoices/{id}/link_credit_note (linkCreditNote)

        Link a credit note to a customer invoice

        Link a credit note to a customer invoice

        > ℹ️
        > This endpoint requires the following scope: `customer_invoices:all`

        Request body: JSON, validated against spec.schema("linkCreditNote").
        """
        return await self._client.request("POST", f"/api/external/v2/customer_invoices/{id}/link_credit_note", json=body, validate=validate)

    async def mark_as_paid_customer_invoice(self, id: int | str) -> Any:
        """PUT /api/external/v2/customer_invoices/{id}/mark_as_paid (markAsPaidCustomerInvoice)

        Mark a customer invoice as paid

        Mark a customer invoice as paid. No automatic reconciliation will
        be done once the invoice is marked as paid


        > ℹ️
        > This endpoint requires the following scope: `customer_invoices:all`
        """
        return await self._client.request("PUT", f"/api/external/v2/customer_invoices/{id}/mark_as_paid")

    async def send_by_email_customer_invoice(self, id: int | str, body: Any = None, *, validate: bool = True) -> Any:
        """POST /api/external/v2/customer_invoices/{id}/send_by_email (sendByEmailCustomerInvoice)

        Send a customer invoice by email

        This endpoint allows you to send a finalized, imported customer invoice or credit note
        by email to your customer. This requires that the PDF file for that document
        has been generated (this process can take a few minutes), so if you just created
        the invoice in our system, we may return a 409 error. You should
        retry the request in a few minutes - if you receive a 204 response, that means
        that the email is on its way. For more information about email sending, please
        read [this guide](https://pennylane.readme.io/v2.0/docs/sending-documents-by-email).

        > ⚠️ **Warning:** If the invoice is eligible for electronic invoicing, sending
        > it by email prevents it from later being transmitted through an approved
        > platform (PA – *Plateforme Agréée*). For invoices within the scope of the
        > e-invoicing reform, transmit them through the approved platform instead of
        > sending them by email.


        > ℹ️
        > This endpoint requires the following scope: `customer_invoices:all`

        Request body: JSON, validated against spec.schema("sendByEmailCustomerInvoice").
        """
        return await self._client.request("POST", f"/api/external/v2/customer_invoices/{id}/send_by_email", json=body, validate=validate)

    async def send_to_pa_customer_invoice(self, id: int | str) -> Any:
        """POST /api/external/v2/customer_invoices/{id}/send_to_pa (sendToPaCustomerInvoice)

        Send a customer e-invoice to PA

        Send a customer e-invoice to the Partner Dematerialization Platform (PA).

        After an e-invoice import, the file may still be processing. If you call this
        endpoint before processing is finished, the API returns 409. Retry after a few
        seconds. A 204 response means the invoice is being sent to the PA.


        > ℹ️
        > This endpoint requires the following scope: `customer_invoices:all`
        """
        return await self._client.request("POST", f"/api/external/v2/customer_invoices/{id}/send_to_pa")

    async def update_imported_customer_invoice(self, id: int | str, body: Any, *, validate: bool = True) -> Any:
        """PUT /api/external/v2/customer_invoices/{id}/update_imported (updateImportedCustomerInvoice)

        Update an Imported customer invoice

        Update an imported customer invoice or credit note. It is not
        applicable for draft invoices.


        > ℹ️
        > This endpoint requires the following scope: `customer_invoices:all`

        Request body: JSON, validated against spec.schema("updateImportedCustomerInvoice").
        """
        return await self._client.request("PUT", f"/api/external/v2/customer_invoices/{id}/update_imported", json=body, validate=validate)



class CustomersAPI:
    """Operations tagged "customers"."""

    def __init__(self, client) -> None:
        self._client = client

    async def post_company_customer(self, body: Any, *, validate: bool = True) -> Any:
        """POST /api/external/v2/company_customers (postCompanyCustomer)

        Create a company customer

        This endpoint returns the created company customer.

        > ℹ️
        > This endpoint requires the following scope: `customers:all`

        Request body: JSON, validated against spec.schema("postCompanyCustomer").
        """
        return await self._client.request("POST", "/api/external/v2/company_customers", json=body, validate=validate)

    async def get_company_customer(self, id: int | str) -> Any:
        """GET /api/external/v2/company_customers/{id} (getCompanyCustomer)

        Retrieve a company customer

        This endpoint returns a company customer.

        > ℹ️
        > This endpoint requires one of the following scopes: `customers:all`, `customers:readonly`
        """
        return await self._client.request("GET", f"/api/external/v2/company_customers/{id}")

    async def put_company_customer(self, id: int | str, body: Any, *, validate: bool = True) -> Any:
        """PUT /api/external/v2/company_customers/{id} (putCompanyCustomer)

        Update a company customer

        This endpoint returns the updated company customer.

        > ℹ️
        > This endpoint requires the following scope: `customers:all`

        Request body: JSON, validated against spec.schema("putCompanyCustomer").
        """
        return await self._client.request("PUT", f"/api/external/v2/company_customers/{id}", json=body, validate=validate)

    async def get_customers(self, *, cursor: str | None = None, limit: int | None = None, filter: str | list[dict] | None = None, sort: str | None = None) -> Any:
        """GET /api/external/v2/customers (getCustomers)

        List customers (company and individual)

        This endpoint returns a list of both company and individual customers

        > ℹ️
        > This endpoint requires one of the following scopes: `customers:all`, `customers:readonly`

        Query params:
          cursor (string): Cursor for pagination. Use this to fetch the next set of results.
            The cursor is an opaque string returned in the previous response's metadata.
            Leave empty for the first request.
          limit (integer): Number of items to return per request.
            Defaults to 20 if not specified.
            Must be between 1 and 100.
          filter (string): You can choose to filter items on specific fields.
            Available fields and values:
            - `id`: `lt`, `lteq`, `gt`, `gteq`, `eq`, `not_eq`, `in`, `not_in`
            - `customer_type`: `eq`, `not_eq`
            - `ledger_account_id`: `eq`, `not_eq`
            - `name`: `start_with`, `eq`
            - `external_reference`: `start_with`, `eq`, `not_eq`, `in`, `not_in`
            - `reg_no`: `eq`, `not_eq`, `in`, `not_in`
            - `emails`: `in`
          sort (string): You can choose to sort items on specific attributes
            Sort field may be prefixed with `-` for descending order.
            Example : `id` will sort by ascending order, `-id` will sort by descending order.
            Available fields : `id`

        Paginated: pass this method to client.paginate() or client.fetch_all().
        """
        return await self._client.request("GET", "/api/external/v2/customers", params={"cursor": cursor, "limit": limit, "filter": filter, "sort": sort})

    async def get_customer_categories(self, customer_id: int | str, *, cursor: str | None = None, limit: int | None = None) -> Any:
        """GET /api/external/v2/customers/{customer_id}/categories (getCustomerCategories)

        List categories of a customer

        List categories of a customer

        > ℹ️
        > This endpoint requires one of the following scopes: `customers:readonly`, `customers:all`

        Query params:
          cursor (string): Cursor for pagination. Use this to fetch the next set of results.
            The cursor is an opaque string returned in the previous response's metadata.
            Leave empty for the first request.
          limit (integer): Number of items to return per request.
            Defaults to 20 if not specified.
            Must be between 1 and 100.

        Paginated: pass this method to client.paginate() or client.fetch_all().
        """
        return await self._client.request("GET", f"/api/external/v2/customers/{customer_id}/categories", params={"cursor": cursor, "limit": limit})

    async def put_customer_categories(self, customer_id: int | str, body: Any, *, validate: bool = True) -> Any:
        """PUT /api/external/v2/customers/{customer_id}/categories (putCustomerCategories)

        Categorize a customer

        Update the categories of a customer. You can pass categories that don't belong to the same category group. The sum of categories of a same group must equal `1`. In the following example, the two first categories belong to the same category group A, the sum of the weights is `1`. The third category belongs to a category group B, its weight is `1`.
        ```
        [
          { "id": 59, "weight": "0.5" }, // category group A
          { "id": 33, "weight": "0.5" }, // category group A
          { "id": 65, "weight": "1" }    // category group B
        ]
        ```


        > ℹ️
        > This endpoint requires the following scope: `customers:all`

        Request body: JSON, validated against spec.schema("putCustomerCategories").
        """
        return await self._client.request("PUT", f"/api/external/v2/customers/{customer_id}/categories", json=body, validate=validate)

    async def get_customer_contacts(self, customer_id: int | str, *, cursor: str | None = None, limit: int | None = None, sort: str | None = None) -> Any:
        """GET /api/external/v2/customers/{customer_id}/contacts (getCustomerContacts)

        List contacts of a customer

        List contacts of a customer

        > ℹ️
        > This endpoint requires one of the following scopes: `customers:all`, `customers:readonly`

        Query params:
          cursor (string): Cursor for pagination. Use this to fetch the next set of results.
            The cursor is an opaque string returned in the previous response's metadata.
            Leave empty for the first request.
          limit (integer): Number of items to return per request.
            Defaults to 20 if not specified.
            Must be between 1 and 100.
          sort (string): You can choose to sort items on specific attributes
            Sort field may be prefixed with `-` for descending order.
            Example : `id` will sort by ascending order, `-id` will sort by descending order.
            Available fields : `id`

        Paginated: pass this method to client.paginate() or client.fetch_all().
        """
        return await self._client.request("GET", f"/api/external/v2/customers/{customer_id}/contacts", params={"cursor": cursor, "limit": limit, "sort": sort})

    async def post_customer_contact(self, customer_id: int | str, body: Any, *, validate: bool = True) -> Any:
        """POST /api/external/v2/customers/{customer_id}/contacts (postCustomerContact)

        Create a contact of a customer

        Create a contact of a customer.
        Contacts are a separate resource: creating one does not add its email address
        to the invoice recipients of the customer.


        > ℹ️
        > This endpoint requires the following scope: `customers:all`

        Request body: JSON, validated against spec.schema("postCustomerContact").
        """
        return await self._client.request("POST", f"/api/external/v2/customers/{customer_id}/contacts", json=body, validate=validate)

    async def delete_customer_contact(self, customer_id: int | str, id: int | str) -> Any:
        """DELETE /api/external/v2/customers/{customer_id}/contacts/{id} (deleteCustomerContact)

        Delete a contact of a customer

        Delete a contact of a customer.
        Contacts are a separate resource: deleting one does not remove its email address
        from the invoice recipients of the customer.


        > ℹ️
        > This endpoint requires the following scope: `customers:all`
        """
        return await self._client.request("DELETE", f"/api/external/v2/customers/{customer_id}/contacts/{id}")

    async def get_customer_contact(self, customer_id: int | str, id: int | str) -> Any:
        """GET /api/external/v2/customers/{customer_id}/contacts/{id} (getCustomerContact)

        Retrieve a contact of a customer

        Retrieve a contact of a customer

        > ℹ️
        > This endpoint requires one of the following scopes: `customers:all`, `customers:readonly`
        """
        return await self._client.request("GET", f"/api/external/v2/customers/{customer_id}/contacts/{id}")

    async def put_customer_contact(self, customer_id: int | str, id: int | str, body: Any, *, validate: bool = True) -> Any:
        """PUT /api/external/v2/customers/{customer_id}/contacts/{id} (putCustomerContact)

        Update a contact of a customer

        Update a contact of a customer.
        Only the submitted fields are updated, the others are left unchanged.
        Contacts are a separate resource: updating one does not change the invoice
        recipients of the customer.


        > ℹ️
        > This endpoint requires the following scope: `customers:all`

        Request body: JSON, validated against spec.schema("putCustomerContact").
        """
        return await self._client.request("PUT", f"/api/external/v2/customers/{customer_id}/contacts/{id}", json=body, validate=validate)

    async def get_customer(self, id: int | str) -> Any:
        """GET /api/external/v2/customers/{id} (getCustomer)

        Retrieve a customer

        This endpoint returns a customer.

        > ℹ️
        > This endpoint requires one of the following scopes: `customers:all`, `customers:readonly`
        """
        return await self._client.request("GET", f"/api/external/v2/customers/{id}")

    async def post_individual_customer(self, body: Any, *, validate: bool = True) -> Any:
        """POST /api/external/v2/individual_customers (postIndividualCustomer)

        Create an individual customer

        This endpoint returns the created individual customer.

        > ℹ️
        > This endpoint requires the following scope: `customers:all`

        Request body: JSON, validated against spec.schema("postIndividualCustomer").
        """
        return await self._client.request("POST", "/api/external/v2/individual_customers", json=body, validate=validate)

    async def get_individual_customer(self, id: int | str) -> Any:
        """GET /api/external/v2/individual_customers/{id} (getIndividualCustomer)

        Retrieve an individual customer

        This endpoint returns an individual customer.

        > ℹ️
        > This endpoint requires one of the following scopes: `customers:all`, `customers:readonly`
        """
        return await self._client.request("GET", f"/api/external/v2/individual_customers/{id}")

    async def put_individual_customer(self, id: int | str, body: Any, *, validate: bool = True) -> Any:
        """PUT /api/external/v2/individual_customers/{id} (putIndividualCustomer)

        Update an individual customer

        This endpoint returns the updated individual customer.

        > ℹ️
        > This endpoint requires the following scope: `customers:all`

        Request body: JSON, validated against spec.schema("putIndividualCustomer").
        """
        return await self._client.request("PUT", f"/api/external/v2/individual_customers/{id}", json=body, validate=validate)



class ExportsAPI:
    """Operations tagged "exports"."""

    def __init__(self, client) -> None:
        self._client = client

    async def export_analytical_general_ledger(self, body: Any, *, validate: bool = True) -> Any:
        """POST /api/external/v2/exports/analytical_general_ledgers (exportAnalyticalGeneralLedger)

        Create an Analytical General Ledger export

        This endpoint allows you to create an Analytical General Ledger export. The generated export file is an xlsx file, using the in-line analytical mode by default.

        > ℹ️
        > This endpoint requires the following scope: `exports:agl`

        Request body: JSON, validated against spec.schema("exportAnalyticalGeneralLedger").
        """
        return await self._client.request("POST", "/api/external/v2/exports/analytical_general_ledgers", json=body, validate=validate)

    async def get_analytical_general_ledger_export(self, id: int | str) -> Any:
        """GET /api/external/v2/exports/analytical_general_ledgers/{id} (getAnalyticalGeneralLedgerExport)

        Retrieve an Analytical General Ledger export

        The endpoint returns a specific Analytical General Ledger export. The export file is an xlsx file, using the in-line analytical mode.

        > ℹ️
        > This endpoint requires the following scope: `exports:agl`
        """
        return await self._client.request("GET", f"/api/external/v2/exports/analytical_general_ledgers/{id}")

    async def export_fec(self, body: Any, *, validate: bool = True) -> Any:
        """POST /api/external/v2/exports/fecs (exportFec)

        Create a FEC export

        This endpoint allows you to create a FEC export

        > ℹ️
        > This endpoint requires the following scope: `exports:fec`

        Request body: JSON, validated against spec.schema("exportFec").
        """
        return await self._client.request("POST", "/api/external/v2/exports/fecs", json=body, validate=validate)

    async def get_fec_export(self, id: int | str) -> Any:
        """GET /api/external/v2/exports/fecs/{id} (getFecExport)

        Retrieve a FEC export

        The endpoint returns a specific FEC export

        > ℹ️
        > This endpoint requires the following scope: `exports:fec`
        """
        return await self._client.request("GET", f"/api/external/v2/exports/fecs/{id}")

    async def export_general_ledger(self, body: Any, *, validate: bool = True) -> Any:
        """POST /api/external/v2/exports/general_ledgers (exportGeneralLedger)

        Create a General Ledger export

        This endpoint allows you to create a General Ledger export. The generated export file is an xlsx file.

        > ℹ️
        > This endpoint requires the following scope: `exports:gl`

        Request body: JSON, validated against spec.schema("exportGeneralLedger").
        """
        return await self._client.request("POST", "/api/external/v2/exports/general_ledgers", json=body, validate=validate)

    async def get_general_ledger_export(self, id: int | str) -> Any:
        """GET /api/external/v2/exports/general_ledgers/{id} (getGeneralLedgerExport)

        Retrieve a General Ledger export

        The endpoint returns a specific General Ledger export. The export file is an xlsx file.

        > ℹ️
        > This endpoint requires the following scope: `exports:gl`
        """
        return await self._client.request("GET", f"/api/external/v2/exports/general_ledgers/{id}")



class FileAttachmentsAPI:
    """Operations tagged "file_attachments"."""

    def __init__(self, client) -> None:
        self._client = client

    async def post_file_attachments(self, files: Any, data: dict | None = None) -> Any:
        """POST /api/external/v2/file_attachments (postFileAttachments)

        Upload a file

        Upload a file to attach to any resource that provides a `file_attachment_id`.

        The maximum allowed file size is 100MB.
        Note that this will not upload a file into the DMS (GED).


        > ℹ️
        > This endpoint requires the following scope: `file_attachments:all`

        Request body: multipart/form-data (files=..., data=...), not validated.
        """
        return await self._client.request("POST", "/api/external/v2/file_attachments", files=files, data=data)



class FiscalYearsAPI:
    """Operations tagged "fiscal_years"."""

    def __init__(self, client) -> None:
        self._client = client

    async def company_fiscal_years(self, *, cursor: str | None = None, limit: int | None = None, sort: str | None = None) -> Any:
        """GET /api/external/v2/fiscal_years (company-fiscal-years)

        List Company's Fiscal Years

        This endpoint returns a list of fiscal years of the company.
        By default, returns fiscal years ordered by descending IDs.
        A `sort` query parameter is available allowing to sort by `id` or `start` attributes.


        > ℹ️
        > This endpoint requires the following scope: `fiscal_years:readonly`

        Query params:
          cursor (string): Cursor for pagination. Use this to fetch the next set of results.
            The cursor is an opaque string returned in the previous response's metadata.
            Leave empty for the first request.
          limit (integer): Number of items to return per request.
            Defaults to 20 if not specified.
            Must be between 1 and 100.
          sort (string): You can choose to sort items on specific attributes
            Sort field may be prefixed with `-` for descending order.
            Example : `id` will sort by ascending order, `-id` will sort by descending order.
            Available fields :
            - `id`, `start`

        Paginated: pass this method to client.paginate() or client.fetch_all().
        """
        return await self._client.request("GET", "/api/external/v2/fiscal_years", params={"cursor": cursor, "limit": limit, "sort": sort})



class JournalsAPI:
    """Operations tagged "journals"."""

    def __init__(self, client) -> None:
        self._client = client

    async def get_journals(self, *, cursor: str | None = None, limit: int | None = None, filter: str | list[dict] | None = None, sort: str | None = None) -> Any:
        """GET /api/external/v2/journals (getJournals)

        List journals

        List journals.
        By default, returns journals ordered by descending IDs.


        > ℹ️
        > This endpoint requires one of the following scopes: `journals:readonly`, `journals:all`

        Query params:
          cursor (string): Cursor for pagination. Use this to fetch the next set of results.
            The cursor is an opaque string returned in the previous response's metadata.
            Leave empty for the first request.
          limit (integer): Number of items to return per request.
            Defaults to 20 if not specified.
            Must be between 1 and 100.
          filter (string): You can choose to filter items on specific fields.
            Available fields and values:
            - `type`: `eq`, `not_eq`, `in`, `not_in`
          sort (string): You can choose to sort items on specific attributes
            Sort field may be prefixed with `-` for descending order.
            Example : `id` will sort by ascending order, `-id` will sort by descending order.
            Available fields :
            - `id`

        Paginated: pass this method to client.paginate() or client.fetch_all().
        """
        return await self._client.request("GET", "/api/external/v2/journals", params={"cursor": cursor, "limit": limit, "filter": filter, "sort": sort})

    async def post_journals(self, body: Any, *, validate: bool = True) -> Any:
        """POST /api/external/v2/journals (postJournals)

        Create a journal

        Create a journal

        > ℹ️
        > This endpoint requires the following scope: `journals:all`

        Request body: JSON, validated against spec.schema("postJournals").
        """
        return await self._client.request("POST", "/api/external/v2/journals", json=body, validate=validate)

    async def get_journal(self, id: int | str) -> Any:
        """GET /api/external/v2/journals/{id} (getJournal)

        Retrieve a journal

        Retrieve a journal

        > ℹ️
        > This endpoint requires one of the following scopes: `journals:readonly`, `journals:all`
        """
        return await self._client.request("GET", f"/api/external/v2/journals/{id}")



class LedgerAccountsAPI:
    """Operations tagged "ledger_accounts"."""

    def __init__(self, client) -> None:
        self._client = client

    async def get_ledger_accounts(self, *, cursor: str | None = None, limit: int | None = None, filter: str | list[dict] | None = None, sort: str | None = None) -> Any:
        """GET /api/external/v2/ledger_accounts (getLedgerAccounts)

        List Ledger Accounts

        List Ledger Accounts


        > ℹ️
        > This endpoint requires one of the following scopes: `ledger_accounts:readonly`, `ledger_accounts:all`

        Query params:
          cursor (string): Cursor for pagination. Use this to fetch the next set of results.
            The cursor is an opaque string returned in the previous response's metadata.
            Leave empty for the first request.
          limit (integer): Number of items to return per request.
            Defaults to 20 if not specified.
            Must be between 1 and 1000.
          filter (string): You can choose to filter items on specific fields.
            Available fields and values:
            - `id`: `lt`, `lteq`, `gt`, `gteq`, `eq`, `not_eq`, `in`, `not_in`
            - `number`: `start_with`, `eq`, `in`
            - `enabled`: `eq`
          sort (string): You can choose to sort items on specific attributes
            Sort field may be prefixed with `-` for descending order.
            Example : `id` will sort by ascending order, `-id` will sort by descending order.
            Available fields :
            - `id`

        Paginated: pass this method to client.paginate() or client.fetch_all().
        """
        return await self._client.request("GET", "/api/external/v2/ledger_accounts", params={"cursor": cursor, "limit": limit, "filter": filter, "sort": sort})

    async def post_ledger_accounts(self, body: Any, *, validate: bool = True) -> Any:
        """POST /api/external/v2/ledger_accounts (postLedgerAccounts)

        Create a ledger account

        Create a ledger account


        > ℹ️
        > This endpoint requires the following scope: `ledger_accounts:all`

        Request body: JSON, validated against spec.schema("postLedgerAccounts").
        """
        return await self._client.request("POST", "/api/external/v2/ledger_accounts", json=body, validate=validate)

    async def get_ledger_account(self, id: int | str) -> Any:
        """GET /api/external/v2/ledger_accounts/{id} (getLedgerAccount)

        Get a ledger account

        Get a ledger account


        > ℹ️
        > This endpoint requires one of the following scopes: `ledger_accounts:readonly`, `ledger_accounts:all`
        """
        return await self._client.request("GET", f"/api/external/v2/ledger_accounts/{id}")

    async def update_ledger_account(self, id: int | str, body: Any, *, validate: bool = True) -> Any:
        """PUT /api/external/v2/ledger_accounts/{id} (updateLedgerAccount)

        Update a ledger account

        Update a ledger account

        > ℹ️
        > This endpoint requires the following scope: `ledger_accounts:all`

        Request body: JSON, validated against spec.schema("updateLedgerAccount").
        """
        return await self._client.request("PUT", f"/api/external/v2/ledger_accounts/{id}", json=body, validate=validate)



class LedgerAttachmentsAPI:
    """Operations tagged "ledger_attachments"."""

    def __init__(self, client) -> None:
        self._client = client

    async def post_ledger_attachments(self, files: Any, data: dict | None = None) -> Any:
        """POST /api/external/v2/ledger_attachments (postLedgerAttachments)

        Upload a file

        Upload a file to attach to a ledger entry. The maximum allowed file size is 100MB.
        Note that this will not upload a file into the DMS (GED).

        > ‼️
        > This endpoint is **DEPRECATED**
        > As an alternative, please use the [File Attachments: Upload a file](https://pennylane.readme.io/reference/postfileattachments#/) endpoint.

        > ℹ️
        > This endpoint requires the following scope: `ledger`

        Request body: multipart/form-data (files=..., data=...), not validated.
        """
        return await self._client.request("POST", "/api/external/v2/ledger_attachments", files=files, data=data)



class LedgerEntriesAPI:
    """Operations tagged "ledger_entries"."""

    def __init__(self, client) -> None:
        self._client = client

    async def get_ledger_entries(self, *, cursor: str | None = None, limit: int | None = None, filter: str | list[dict] | None = None, sort: str | None = None) -> Any:
        """GET /api/external/v2/ledger_entries (getLedgerEntries)

        List Ledger Entries

        Returns a list of ledger entries.

        > ℹ️
        > This endpoint requires one of the following scopes: `ledger_entries:readonly`, `ledger_entries:all`

        Query params:
          cursor (string): Cursor for pagination. Use this to fetch the next set of results.
            The cursor is an opaque string returned in the previous response's metadata.
            Leave empty for the first request.
          limit (integer): Number of items to return per request.
            Defaults to 20 if not specified.
            Must be between 1 and 100.
          filter (string): You can choose to filter items on specific fields.
            Available fields and values:
            - `id`: `lt`, `lteq`, `gt`, `gteq`, `eq`, `not_eq`, `in`, `not_in`
            - `date`: `lt`, `lteq`, `gt`, `gteq`, `eq`, `not_eq`
            - `journal_id`: `lt`, `lteq`, `gt`, `gteq`, `eq`, `not_eq`, `in`, `not_in`
          sort (string): You can choose to sort items on specific attributes
            Sort field may be prefixed with `-` for descending order.
            Example : `date` will sort by ascending order, `-date` will sort by descending order.
            Available fields :
            - `id`
            - `date`

        Paginated: pass this method to client.paginate() or client.fetch_all().
        """
        return await self._client.request("GET", "/api/external/v2/ledger_entries", params={"cursor": cursor, "limit": limit, "filter": filter, "sort": sort})

    async def post_ledger_entries(self, body: Any, *, validate: bool = True) -> Any:
        """POST /api/external/v2/ledger_entries (postLedgerEntries)

        Create a ledger entry

        Create a ledger entry


        > ℹ️
        > This endpoint requires the following scope: `ledger_entries:all`

        Request body: JSON, validated against spec.schema("postLedgerEntries").
        """
        return await self._client.request("POST", "/api/external/v2/ledger_entries", json=body, validate=validate)

    async def get_ledger_entry(self, id: int | str) -> Any:
        """GET /api/external/v2/ledger_entries/{id} (getLedgerEntry)

        Retrieve a Ledger entry

        Retrieve a ledger entry


        > ℹ️
        > This endpoint requires one of the following scopes: `ledger_entries:readonly`, `ledger_entries:all`
        """
        return await self._client.request("GET", f"/api/external/v2/ledger_entries/{id}")

    async def put_ledger_entries(self, id: int | str, body: Any, *, validate: bool = True) -> Any:
        """PUT /api/external/v2/ledger_entries/{id} (putLedgerEntries)

        Update a ledger entry

        Update a ledger entry


        > ℹ️
        > This endpoint requires the following scope: `ledger_entries:all`

        Request body: JSON, validated against spec.schema("putLedgerEntries").
        """
        return await self._client.request("PUT", f"/api/external/v2/ledger_entries/{id}", json=body, validate=validate)

    async def get_ledger_entries_ledger_entry_lines(self, ledger_entry_id: int | str, *, cursor: str | None = None, limit: int | None = None, filter: str | list[dict] | None = None, sort: str | None = None) -> Any:
        """GET /api/external/v2/ledger_entries/{ledger_entry_id}/ledger_entry_lines (getLedgerEntriesLedgerEntryLines)

        List ledger entry lines of a Ledger Entry

        List ledger entry lines of a Ledger Entry


        > ℹ️
        > This endpoint requires one of the following scopes: `ledger_entries:readonly`, `ledger_entries:all`

        Query params:
          cursor (string): Use this to fetch the next set of results. The cursor is an opaque string returned in the previous response's metadata. Leave empty for the first request.
          limit (integer): Number of items to return per request.
            Defaults to 20 if not specified.
            Must be between 1 and 100.
          filter (string): You can choose to filter items on specific fields.
            Available fields : `ledger_account_id`
            Available operators : `lt`, `lteq`, `gt`, `gteq`, `eq`, `not_eq`, `in`, `not_in`
          sort (string): You can choose to sort items on specific attributes
            Sort field may be prefixed with `-` for descending order.
            Example : `id` will sort by ascending order, `-id` will sort by descending order.
            Available fields :
            - `id`

        Paginated: pass this method to client.paginate() or client.fetch_all().
        """
        return await self._client.request("GET", f"/api/external/v2/ledger_entries/{ledger_entry_id}/ledger_entry_lines", params={"cursor": cursor, "limit": limit, "filter": filter, "sort": sort})



class LedgerEntryLinesAPI:
    """Operations tagged "ledger_entry_lines"."""

    def __init__(self, client) -> None:
        self._client = client

    async def get_ledger_entry_lines(self, *, cursor: str | None = None, limit: int | None = None, filter: str | list[dict] | None = None, sort: str | None = None) -> Any:
        """GET /api/external/v2/ledger_entry_lines (getLedgerEntryLines)

        List ledger entry lines

        List ledger entry lines

        > ℹ️
        > This endpoint requires one of the following scopes: `ledger_entries:readonly`, `ledger_entries:all`

        Query params:
          cursor (string): Cursor for pagination. Use this to fetch the next set of results.
            The cursor is an opaque string returned in the previous response's metadata.
            Leave empty for the first request.
          limit (integer): Number of items to return per request.
            Defaults to 20 if not specified.
            Must be between 1 and 100.
          filter (string): You can choose to filter items on specific fields.
            Available fields : `id`, `journal_id`, `ledger_account_id`, `date`
            Available operators : `lt`, `lteq`, `gt`, `gteq`, `eq`, `not_eq`, `in`, `not_in`
          sort (string): You can choose to sort items on specific attributes
            Sort field may be prefixed with `-` for descending order.
            Example : `id` will sort by ascending order, `-id` will sort by descending order.
            Available fields : `id`, `date`

        Paginated: pass this method to client.paginate() or client.fetch_all().
        """
        return await self._client.request("GET", "/api/external/v2/ledger_entry_lines", params={"cursor": cursor, "limit": limit, "filter": filter, "sort": sort})

    async def delete_ledger_entry_lines_unletter(self, body: Any, *, validate: bool = True) -> Any:
        """DELETE /api/external/v2/ledger_entry_lines/lettering (deleteLedgerEntryLinesUnletter)

        Unletter ledger entry lines

        This endpoint lets you unletter ledger entry lines.

        > ℹ️
        > This endpoint requires the following scope: `ledger_entries:all`

        Request body: JSON, validated against spec.schema("deleteLedgerEntryLinesUnletter").
        """
        return await self._client.request("DELETE", "/api/external/v2/ledger_entry_lines/lettering", json=body, validate=validate)

    async def post_ledger_entry_lines_letter(self, body: Any, *, validate: bool = True) -> Any:
        """POST /api/external/v2/ledger_entry_lines/lettering (postLedgerEntryLinesLetter)

        Letter ledger entry lines

        This endpoint lets you letter ledger entry lines together. All
        received entry lines will be lettered together. If a passed entry line is
        already lettered, then the lettering will be applied to its associated lettered
        entry lines as well.

        > ℹ️
        > This endpoint requires the following scope: `ledger_entries:all`

        Request body: JSON, validated against spec.schema("postLedgerEntryLinesLetter").
        """
        return await self._client.request("POST", "/api/external/v2/ledger_entry_lines/lettering", json=body, validate=validate)

    async def get_ledger_entry_line(self, id: int | str) -> Any:
        """GET /api/external/v2/ledger_entry_lines/{id} (getLedgerEntryLine)

        Retrieve a Ledger entry line

        Retrieve a ledger entry line

        > ℹ️
        > This endpoint requires one of the following scopes: `ledger_entries:readonly`, `ledger_entries:all`
        """
        return await self._client.request("GET", f"/api/external/v2/ledger_entry_lines/{id}")

    async def get_ledger_entry_lines_categories(self, ledger_entry_line_id: int | str, *, cursor: str | None = None, limit: int | None = None, sort: str | None = None) -> Any:
        """GET /api/external/v2/ledger_entry_lines/{ledger_entry_line_id}/categories (getLedgerEntryLinesCategories)

        List categories of a Ledger Entry line

        List categories of a Ledger Entry line


        > ℹ️
        > This endpoint requires one of the following scopes: `ledger_entries:readonly`, `ledger_entries:all`

        Query params:
          cursor (string): Cursor for pagination. Use this to fetch the next set of results.
            The cursor is an opaque string returned in the previous response's metadata.
            Leave empty for the first request.
          limit (integer): Number of items to return per request.
            Defaults to 20 if not specified.
            Must be between 1 and 100.
          sort (string): You can choose to sort items on specific attributes
            Sort field may be prefixed with `-` for descending order.
            Example : `id` will sort by ascending order, `-id` will sort by descending order.
            Available fields :
            - `id`

        Paginated: pass this method to client.paginate() or client.fetch_all().
        """
        return await self._client.request("GET", f"/api/external/v2/ledger_entry_lines/{ledger_entry_line_id}/categories", params={"cursor": cursor, "limit": limit, "sort": sort})

    async def put_ledger_entry_lines_categories(self, ledger_entry_line_id: int | str, body: Any, *, validate: bool = True) -> Any:
        """PUT /api/external/v2/ledger_entry_lines/{ledger_entry_line_id}/categories (putLedgerEntryLinesCategories)

        Link Analytical Categories to a Ledger Entry line

        This endpoint replaces already existing categories on the Ledger Entry line with new values.
        If an empty array of categories_ids is provided, it will remove all categories from the Ledger Entry line.


        > ℹ️
        > This endpoint requires the following scope: `ledger_entries:all`

        Request body: JSON, validated against spec.schema("putLedgerEntryLinesCategories").
        """
        return await self._client.request("PUT", f"/api/external/v2/ledger_entry_lines/{ledger_entry_line_id}/categories", json=body, validate=validate)

    async def get_ledger_entry_lines_lettered_ledger_entry_lines(self, ledger_entry_line_id: int | str, *, cursor: str | None = None, limit: int | None = None, sort: str | None = None) -> Any:
        """GET /api/external/v2/ledger_entry_lines/{ledger_entry_line_id}/lettered_ledger_entry_lines (getLedgerEntryLinesLetteredLedgerEntryLines)

        List ledger entry lines lettered to a given ledger entry line

        List ledger entry lines lettered to a given ledger entry line


        > ℹ️
        > This endpoint requires one of the following scopes: `ledger_entries:readonly`, `ledger_entries:all`

        Query params:
          cursor (string): Cursor for pagination. Use this to fetch the next set of results.
            The cursor is an opaque string returned in the previous response's metadata.
            Leave empty for the first request.
          limit (integer): Number of items to return per request.
            Defaults to 20 if not specified.
            Must be between 1 and 100.
          sort (string): Only available in the new version of the API.

            You can choose to sort items on specific attributes
            Sort field may be prefixed with `-` for descending order.
            Example : `id` will sort by ascending order, `-id` will sort by descending order.
            Available fields : `id`, `date`

        Paginated: pass this method to client.paginate() or client.fetch_all().
        """
        return await self._client.request("GET", f"/api/external/v2/ledger_entry_lines/{ledger_entry_line_id}/lettered_ledger_entry_lines", params={"cursor": cursor, "limit": limit, "sort": sort})



class MandatesAPI:
    """Operations tagged "mandates"."""

    def __init__(self, client) -> None:
        self._client = client

    async def get_gocardless_mandates(self, *, cursor: str | None = None, limit: int | None = None, filter: str | list[dict] | None = None, sort: str | None = None) -> Any:
        """GET /api/external/v2/gocardless_mandates (getGocardlessMandates)

        List gocardless mandates

        List gocardless mandates

        > ℹ️
        > This endpoint requires one of the following scopes: `customer_mandates:all`, `customer_mandates:readonly`

        Query params:
          cursor (string): Cursor for pagination. Use this to fetch the next set of results.
            The cursor is an opaque string returned in the previous response's metadata.
            Leave empty for the first request.
          limit (integer): Number of items to return per request.
            Defaults to 20 if not specified.
            Must be between 1 and 100.
          filter (string): You can choose to filter items on specific fields.
            Available fields and values:
            - `id`: `lt`, `lteq`, `gt`, `gteq`, `eq`, `not_eq`, `in`, `not_in`
            - `customer_id`: `lt`, `lteq`, `gt`, `gteq`, `eq`, `not_eq`, `in`, `not_in`
            - `external_reference`: `eq`
          sort (string): You can choose to sort items on specific attributes.
            Sort field may be prefixed with `-` for descending order.
            Example: `id` will sort by ascending order, `-id` will sort by descending order.
            Available fields: `id`

        Paginated: pass this method to client.paginate() or client.fetch_all().
        """
        return await self._client.request("GET", "/api/external/v2/gocardless_mandates", params={"cursor": cursor, "limit": limit, "filter": filter, "sort": sort})

    async def post_gocardless_mandate_mail_requests(self, body: Any, *, validate: bool = True) -> Any:
        """POST /api/external/v2/gocardless_mandates/mail_requests (postGocardlessMandateMailRequests)

        Send a GoCardless mandate email request

        This endpoint allows you to send an email request for a GoCardless mandate to a recipient.

        > ℹ️
        > This endpoint requires the following scope: `customer_mandates:all`

        Request body: JSON, validated against spec.schema("postGocardlessMandateMailRequests").
        """
        return await self._client.request("POST", "/api/external/v2/gocardless_mandates/mail_requests", json=body, validate=validate)

    async def post_gocardless_mandate_associations(self, gocardless_mandate_id: int | str, body: Any, *, validate: bool = True) -> Any:
        """POST /api/external/v2/gocardless_mandates/{gocardless_mandate_id}/associations (postGocardlessMandateAssociations)

        Associate a GoCardless mandate to a customer

        This endpoint allows you to associate a GoCardless mandate to a customer.

        > ℹ️
        > This endpoint requires the following scope: `customer_mandates:all`

        Request body: JSON, validated against spec.schema("postGocardlessMandateAssociations").
        """
        return await self._client.request("POST", f"/api/external/v2/gocardless_mandates/{gocardless_mandate_id}/associations", json=body, validate=validate)

    async def post_gocardless_mandate_cancellations(self, gocardless_mandate_id: int | str) -> Any:
        """POST /api/external/v2/gocardless_mandates/{gocardless_mandate_id}/cancellations (postGocardlessMandateCancellations)

        Cancel a Gocardless mandate

        Cancels a specific Gocardless mandate by ID. The mandate must be in a cancellable state, having one of the following statuses: `pending_submission`, `submitted` or `active`.

        > ℹ️
        > This endpoint requires the following scope: `customer_mandates:all`
        """
        return await self._client.request("POST", f"/api/external/v2/gocardless_mandates/{gocardless_mandate_id}/cancellations")

    async def get_gocardless_mandate(self, id: int | str) -> Any:
        """GET /api/external/v2/gocardless_mandates/{id} (getGocardlessMandate)

        Get a Gocardless mandate

        This endpoint allows you to retrieve a specific Gocardless mandate by ID.

        > ℹ️
        > This endpoint requires one of the following scopes: `customer_mandates:all`, `customer_mandates:readonly`
        """
        return await self._client.request("GET", f"/api/external/v2/gocardless_mandates/{id}")

    async def get_pro_account_mandate_migrations(self, *, cursor: str | None = None, limit: int | None = None, filter: str | list[dict] | None = None, sort: str | None = None) -> Any:
        """GET /api/external/v2/pro_account/mandate_migrations (getProAccountMandateMigrations)

        List mandate migration candidates

        This endpoint allows you to retrieve all mandate migration candidates
        for your company. These are mandates that can be migrated to a Pro Account.

        Requirements:
        - Company must have a Pro Account (returns 404 if not)
        - Company must have an enabled merchant profile (returns 403 if not)


        > ℹ️
        > This endpoint requires one of the following scopes: `customer_mandates:readonly`, `customer_mandates:all`

        Query params:
          cursor (string): Cursor for pagination. Use this to fetch the next set of results.
            The cursor is an opaque string returned in the previous response's metadata.
            Leave empty for the first request.
          limit (integer): Number of items to return per request.
            Defaults to 20 if not specified.
            Must be between 1 and 100.
          filter (string): You can choose to filter items on specific fields.
            Available fields and values:
            - `customer_id`: `lt`, `lteq`, `gt`, `gteq`, `eq`, `not_eq`, `in`, `not_in`
            - `status`: `lt`, `lteq`, `gt`, `gteq`, `eq`, `not_eq`, `in`, `not_in`
          sort (string): You can choose to sort items on specific attributes.
            Sort field may be prefixed with `-` for descending order.
            Example: `id` will sort by ascending order, `-id` will sort by descending order.
            Available fields: `id`

        Paginated: pass this method to client.paginate() or client.fetch_all().
        """
        return await self._client.request("GET", "/api/external/v2/pro_account/mandate_migrations", params={"cursor": cursor, "limit": limit, "filter": filter, "sort": sort})

    async def post_pro_account_mandate_migrations(self, body: Any, *, validate: bool = True) -> Any:
        """POST /api/external/v2/pro_account/mandate_migrations (postProAccountMandateMigrations)

        Migrate a mandate to Pro Account

        This endpoint allows you to migrate a mandate to a Pro Account.
        Only mandates with status 'available' are eligible for migration.

        **Requirements:**
        - Company must have a Pro Account (returns 404 if not)
        - Company must have an enabled merchant profile (returns 403 if not)


        > ℹ️
        > This endpoint requires the following scope: `customer_mandates:all`

        Request body: JSON, validated against spec.schema("postProAccountMandateMigrations").
        """
        return await self._client.request("POST", "/api/external/v2/pro_account/mandate_migrations", json=body, validate=validate)

    async def post_pro_account_mandate_mail_requests(self, body: Any, *, validate: bool = True) -> Any:
        """POST /api/external/v2/pro_account/mandate_requests (postProAccountMandateMailRequests)

        Send a Pro Account SEPA mandate request

        This endpoint allows you to send a mandate request for a Pro Account
        SEPA Direct Debit mandate to a customer.

        Requirements:
        - Company must have a Pro Account (returns 404 if not)
        - Company must have an enabled merchant profile (returns 403 if not)


        > ℹ️
        > This endpoint requires the following scope: `customer_mandates:all`

        Request body: JSON, validated against spec.schema("postProAccountMandateMailRequests").
        """
        return await self._client.request("POST", "/api/external/v2/pro_account/mandate_requests", json=body, validate=validate)

    async def get_pro_account_mandates(self, *, cursor: str | None = None, limit: int | None = None, filter: str | list[dict] | None = None, sort: str | None = None) -> Any:
        """GET /api/external/v2/pro_account/mandates (getProAccountMandates)

        List Pro Account payment mandates

        This endpoint allows you to retrieve all payment mandates associated
        with your company's pro account.

        Requirements:
        - Company must have a Pro Account (returns 404 if not)
        - Company must have an enabled merchant profile (returns 403 if not)


        > ℹ️
        > This endpoint requires one of the following scopes: `customer_mandates:readonly`, `customer_mandates:all`

        Query params:
          cursor (string): Cursor for pagination. Use this to fetch the next set of results.
            The cursor is an opaque string returned in the previous response's metadata.
            Leave empty for the first request.
          limit (integer): Number of items to return per request.
            Defaults to 20 if not specified.
            Must be between 1 and 100.
          filter (string): You can choose to filter items on specific fields.
            Available fields and operators:
            - `status`: `eq`, `not_eq`, `in`, `not_in`
            - `customer_id`: `lt`, `lteq`, `gt`, `gteq`, `eq`, `not_eq`, `in`, `not_in`
          sort (string): You can choose to sort items on specific attributes.
            Sort field may be prefixed with `-` for descending order.
            Example: `id` will sort by ascending order, `-id` will sort by descending order.
            Available fields: `id`

        Paginated: pass this method to client.paginate() or client.fetch_all().
        """
        return await self._client.request("GET", "/api/external/v2/pro_account/mandates", params={"cursor": cursor, "limit": limit, "filter": filter, "sort": sort})

    async def get_sepa_mandates(self, *, cursor: str | None = None, limit: int | None = None, filter: str | list[dict] | None = None, sort: str | None = None) -> Any:
        """GET /api/external/v2/sepa_mandates (getSepaMandates)

        List SEPA mandates

        This endpoint allows you to retrieve all SEPA mandates associated with your company

        > ℹ️
        > This endpoint requires one of the following scopes: `customer_mandates:all`, `customer_mandates:readonly`

        Query params:
          cursor (string): Cursor for pagination. Use this to fetch the next set of results.
            The cursor is an opaque string returned in the previous response's metadata.
            Leave empty for the first request.
          limit (integer): Number of items to return per request.
            Defaults to 20 if not specified.
            Must be between 1 and 100.
          filter (string): You can choose to filter items on specific fields.
            Available fields and values:
            - `id`: `lt`, `lteq`, `gt`, `gteq`, `eq`, `not_eq`, `in`, `not_in`
            - `customer_id`: `lt`, `lteq`, `gt`, `gteq`, `eq`, `not_eq`, `in`, `not_in`
          sort (string): You can choose to sort items on specific attributes.
            Sort field may be prefixed with `-` for descending order.
            Example: `id` will sort by ascending order, `-id` will sort by descending order.
            Available fields: `id`

        Paginated: pass this method to client.paginate() or client.fetch_all().
        """
        return await self._client.request("GET", "/api/external/v2/sepa_mandates", params={"cursor": cursor, "limit": limit, "filter": filter, "sort": sort})

    async def post_sepa_mandates(self, body: Any, *, validate: bool = True) -> Any:
        """POST /api/external/v2/sepa_mandates (postSepaMandates)

        Create a SEPA mandate

        This endpoint allows you to create a SEPA mandate to enable direct debit payments

        > ℹ️
        > This endpoint requires the following scope: `customer_mandates:all`

        Request body: JSON, validated against spec.schema("postSepaMandates").
        """
        return await self._client.request("POST", "/api/external/v2/sepa_mandates", json=body, validate=validate)

    async def delete_sepa_mandate(self, id: int | str) -> Any:
        """DELETE /api/external/v2/sepa_mandates/{id} (deleteSepaMandate)

        Delete a SEPA mandate

        This endpoint allows you to delete a specific SEPA mandate

        > ℹ️
        > This endpoint requires the following scope: `customer_mandates:all`
        """
        return await self._client.request("DELETE", f"/api/external/v2/sepa_mandates/{id}")

    async def get_sepa_mandate(self, id: int | str) -> Any:
        """GET /api/external/v2/sepa_mandates/{id} (getSepaMandate)

        Get a SEPA mandate

        This endpoint allows you to retrieve a specific SEPA mandate by ID

        > ℹ️
        > This endpoint requires one of the following scopes: `customer_mandates:all`, `customer_mandates:readonly`
        """
        return await self._client.request("GET", f"/api/external/v2/sepa_mandates/{id}")

    async def put_sepa_mandate(self, id: int | str, body: Any, *, validate: bool = True) -> Any:
        """PUT /api/external/v2/sepa_mandates/{id} (putSepaMandate)

        Update a SEPA mandate

        This endpoint allows you to update an existing SEPA mandate

        > ℹ️
        > This endpoint requires the following scope: `customer_mandates:all`

        Request body: JSON, validated against spec.schema("putSepaMandate").
        """
        return await self._client.request("PUT", f"/api/external/v2/sepa_mandates/{id}", json=body, validate=validate)



class NumberingsAPI:
    """Operations tagged "numberings"."""

    def __init__(self, client) -> None:
        self._client = client

    async def get_numberings(self, *, cursor: str | None = None, limit: int | None = None, sort: str | None = None) -> Any:
        """GET /api/external/v2/numberings (getNumberings)

        List document numberings

        List the document numbering configuration of the company.

        Numbering is configured per document type, and a document type that has never been
        configured is absent from this list. Creating a document of a type that is missing here
        fails, so this endpoint can be used to check before calling the endpoints it gates:

        - `invoice` gates finalizing a customer invoice
        - `estimate` gates numbering a quote
        - `proforma`, `shipping_order` and `purchasing_order` gate creating the matching commercial document

        Numbering can only be configured from the Pennylane application.


        > ℹ️
        > This endpoint requires one of the following scopes: `customer_invoices:all`, `customer_invoices:readonly`, `quotes:all`, `quotes:readonly`, `commercial_documents:all`, `commercial_documents:readonly`

        Query params:
          cursor (string): Cursor for pagination. Use this to fetch the next set of results.
            The cursor is an opaque string returned in the previous response's metadata.
            Leave empty for the first request.
          limit (integer): Number of items to return per request.
            Defaults to 20 if not specified.
            Must be between 1 and 100.
          sort (string): You can choose to sort items on specific attributes
            Sort field may be prefixed with `-` for descending order.
            Example : `id` will sort by ascending order, `-id` will sort by descending order.
            Available fields : `id`

        Paginated: pass this method to client.paginate() or client.fetch_all().
        """
        return await self._client.request("GET", "/api/external/v2/numberings", params={"cursor": cursor, "limit": limit, "sort": sort})



class PaRegistrationsAPI:
    """Operations tagged "pa_registrations"."""

    def __init__(self, client) -> None:
        self._client = client

    async def get_pa_registrations(self) -> Any:
        """GET /api/external/v2/pa_registrations (getPaRegistrations)

        List PA Registrations

        Returns all PA (Plateforme Agrée) registrations for the company,
        including activation status and exchange direction. Use this to determine whether the company has completed
        PA onboarding. Records with a `null` `siret` represent the SIREN-level
        (head office), other records represent establishments.


        > ℹ️
        > This endpoint requires the following scope: `pa_registrations:readonly`
        """
        return await self._client.request("GET", "/api/external/v2/pa_registrations")



class ProductsAPI:
    """Operations tagged "products"."""

    def __init__(self, client) -> None:
        self._client = client

    async def get_products(self, *, cursor: str | None = None, limit: int | None = None, filter: str | list[dict] | None = None, sort: str | None = None) -> Any:
        """GET /api/external/v2/products (getProducts)

        List products

        List products

        > ℹ️
        > This endpoint requires one of the following scopes: `products:all`, `products:readonly`

        Query params:
          cursor (string): Cursor for pagination. Use this to fetch the next set of results.
            The cursor is an opaque string returned in the previous response's metadata.
            Leave empty for the first request.
          limit (integer): Number of items to return per request.
            Defaults to 20 if not specified.
            Must be between 1 and 100.
          filter (string): You can choose to filter items on specific fields.
            Available fields and values:
            - `id` : `lt`, `lteq`, `gt`, `gteq`, `eq`, `not_eq`, `in`, `not_in`
            - `label` : `eq`, `in`
            - `reference` : `eq`, `in`
            - `external_reference` : `eq`, `not_eq`, `in`, `not_in`
          sort (string): You can choose to sort items on specific attributes
            Sort field may be prefixed with `-` for descending order.
            Example : `id` will sort by ascending order, `-id` will sort by descending order.
            Available fields : `id`

        Paginated: pass this method to client.paginate() or client.fetch_all().
        """
        return await self._client.request("GET", "/api/external/v2/products", params={"cursor": cursor, "limit": limit, "filter": filter, "sort": sort})

    async def post_products(self, body: Any, *, validate: bool = True) -> Any:
        """POST /api/external/v2/products (postProducts)

        Create a product

        Create a product

        > ℹ️
        > This endpoint requires the following scope: `products:all`

        Request body: JSON, validated against spec.schema("postProducts").
        """
        return await self._client.request("POST", "/api/external/v2/products", json=body, validate=validate)

    async def get_product(self, id: int | str) -> Any:
        """GET /api/external/v2/products/{id} (getProduct)

        Retrieve a product

        Retrieve a product

        > ℹ️
        > This endpoint requires one of the following scopes: `products:all`, `products:readonly`
        """
        return await self._client.request("GET", f"/api/external/v2/products/{id}")

    async def put_product(self, id: int | str, body: Any, *, validate: bool = True) -> Any:
        """PUT /api/external/v2/products/{id} (putProduct)

        Update a product

        Update a product

        > ℹ️
        > This endpoint requires the following scope: `products:all`

        Request body: JSON, validated against spec.schema("putProduct").
        """
        return await self._client.request("PUT", f"/api/external/v2/products/{id}", json=body, validate=validate)



class PurchaseRequestsAPI:
    """Operations tagged "purchase_requests"."""

    def __init__(self, client) -> None:
        self._client = client

    async def get_purchase_requests(self, *, cursor: str | None = None, limit: int | None = None, filter: str | list[dict] | None = None, sort: str | None = None) -> Any:
        """GET /api/external/v2/purchase_requests (getPurchaseRequests)

        List purchase requests

        List purchase requests

        > ℹ️
        > This endpoint requires one of the following scopes: `purchase_requests:all`, `purchase_requests:readonly`

        Query params:
          cursor (string): Cursor for pagination. Use this to fetch the next set of results.
            The cursor is an opaque string returned in the previous response's metadata.
            Leave empty for the first request.
          limit (integer): Number of items to return per request.
            Defaults to 20 if not specified.
            Must be between 1 and 100.
          filter (string): You can choose to filter items on specific fields.
            Available fields and values:
            - `id`: `lt`, `lteq`, `gt`, `gteq`, `eq`, `not_eq`, `in`, `not_in`
            - `reviewed_by_id`: `eq`, `not_eq`, `in`, `not_in`
            - `user_id`: `eq`, `not_eq`, `in`, `not_in`
            - `supplier_id`: `eq`, `not_eq`, `in`, `not_in`
          sort (string): You can choose to sort items on specific attributes
            Sort field may be prefixed with `-` for descending order.
            Example : `id` will sort by ascending order, `-id` will sort by descending order.
            Available fields : `id`

        Paginated: pass this method to client.paginate() or client.fetch_all().
        """
        return await self._client.request("GET", "/api/external/v2/purchase_requests", params={"cursor": cursor, "limit": limit, "filter": filter, "sort": sort})

    async def create_purchase_request_import(self, body: Any, *, validate: bool = True) -> Any:
        """POST /api/external/v2/purchase_requests/imports (createPurchaseRequestImport)

        Import a purchase order.

        Import a purchase order. This will create a purchase request with an existing purchase order attached.
        The purchase request will be **automatically validated**.


        > ℹ️
        > This endpoint requires the following scope: `purchase_requests:all`

        Request body: JSON, validated against spec.schema("createPurchaseRequestImport").
        """
        return await self._client.request("POST", "/api/external/v2/purchase_requests/imports", json=body, validate=validate)

    async def get_purchase_request(self, id: int | str) -> Any:
        """GET /api/external/v2/purchase_requests/{id} (getPurchaseRequest)

        Retrieve a purchase request

        Retrieve a purchase request

        > ℹ️
        > This endpoint requires one of the following scopes: `purchase_requests:all`, `purchase_requests:readonly`
        """
        return await self._client.request("GET", f"/api/external/v2/purchase_requests/{id}")



class QuotesAPI:
    """Operations tagged "quotes"."""

    def __init__(self, client) -> None:
        self._client = client

    async def get_quote_changes(self, *, cursor: str | None = None, limit: int | None = None, start_date: str | None = None) -> Any:
        """GET /api/external/v2/changelogs/quotes (getQuoteChanges)

        Get quotes changes events

        Returns the list of changes based on the provided `start_date`.
        If no `start_date` is provided it returns the oldest set of recorded changes.
        Changes for the last 4 weeks are retained. The items will be returned using
        `processed_at` in ASC order (oldest first).


        > ℹ️
        > This endpoint requires one of the following scopes: `quotes:all`, `quotes:readonly`

        Query params:
          cursor (string): Cursor for pagination. Use this to fetch the next set of results. The cursor is an opaque string returned in the previous response's metadata. Leave empty for the first request.
          limit (integer): Number of items to return per request.
            Defaults to 20 if not specified.
            Must be between 1 and 1000.
          start_date (string): Filter the changes based on the event date. The date should follow RFC3339 format. If no date is provided, the oldest changes will be returned. Changes for the last 4 weeks are retained, thus providing a `start_date` older than that will result in a 422 response. Providing both `start_date` and `cursor` parameters will result in a 400 response.

        Paginated: pass this method to client.paginate() or client.fetch_all().
        """
        return await self._client.request("GET", "/api/external/v2/changelogs/quotes", params={"cursor": cursor, "limit": limit, "start_date": start_date})

    async def list_quotes(self, *, cursor: str | None = None, limit: int | None = None, filter: str | list[dict] | None = None, sort: str | None = None) -> Any:
        """GET /api/external/v2/quotes (listQuotes)

        List quotes

        Lists quotes

        > ℹ️
        > This endpoint requires one of the following scopes: `quotes:all`, `quotes:readonly`

        Query params:
          cursor (string): Cursor for pagination. Use this to fetch the next set of results.
            The cursor is an opaque string returned in the previous response's metadata.
            Leave empty for the first request.
          limit (integer): Number of items to return per request.
            Defaults to 20 if not specified.
            Must be between 1 and 100.
          filter (string): You can choose to filter items on specific fields.
            Available fields and operators:
            - `id`, `customer_id`: `lt`, `lteq`, `gt`, `gteq`, `eq`, `not_eq`, `in`, `not_in`
            - `status`: `eq`, `not_eq`, `in`, `not_in`

            Available statuses:
            - accepted: a quote that has been accepted
            - denied: a quote that has been denied
            - expired: a quote that has expired
            - invoiced: a quote that has been invoiced
            - pending: a quote waiting to be denied or accepted
          sort (string): You can choose to sort items on specific attributes
            Sort field may be prefixed with `-` for descending order.
            Example : `id` will sort by ascending order, `-id` will sort by descending order.
            Available fields : `id`

        Paginated: pass this method to client.paginate() or client.fetch_all().
        """
        return await self._client.request("GET", "/api/external/v2/quotes", params={"cursor": cursor, "limit": limit, "filter": filter, "sort": sort})

    async def post_quotes(self, body: Any, *, validate: bool = True) -> Any:
        """POST /api/external/v2/quotes (postQuotes)

        Create a quote

        This endpoint allows you to create a quote

        > ℹ️
        > This endpoint requires the following scope: `quotes:all`

        Request body: JSON, validated against spec.schema("postQuotes").
        """
        return await self._client.request("POST", "/api/external/v2/quotes", json=body, validate=validate)

    async def get_quote(self, id: int | str) -> Any:
        """GET /api/external/v2/quotes/{id} (getQuote)

        Retrieve a quote

        This endpoint retrieves a quote.

        > ℹ️
        > This endpoint requires one of the following scopes: `quotes:all`, `quotes:readonly`
        """
        return await self._client.request("GET", f"/api/external/v2/quotes/{id}")

    async def update_quote(self, id: int | str, body: Any, *, validate: bool = True) -> Any:
        """PUT /api/external/v2/quotes/{id} (updateQuote)

        Update a quote

        This endpoint allows you to update a quote

        > ℹ️
        > This endpoint requires the following scope: `quotes:all`

        Request body: JSON, validated against spec.schema("updateQuote").
        """
        return await self._client.request("PUT", f"/api/external/v2/quotes/{id}", json=body, validate=validate)

    async def send_by_email_quote(self, id: int | str, body: Any = None, *, validate: bool = True) -> Any:
        """POST /api/external/v2/quotes/{id}/send_by_email (sendByEmailQuote)

        Send a quote by email

        This endpoint allows you to send a quote by email to your customer.
        This requires that the PDF file for that document has been generated
        (this process can take a few minutes), so if you just created
        the quote in our system, we may return a 409 error. You should
        retry the request in a few minutes - if you receive a 204 response, that means
        that the email is on its way. For more information about email sending, please
        read \\[this guide\\](https://pennylane.readme.io/v2.0/docs/sending-documents-by-email).


        > ℹ️
        > This endpoint requires the following scope: `quotes:all`

        Request body: JSON, validated against spec.schema("sendByEmailQuote").
        """
        return await self._client.request("POST", f"/api/external/v2/quotes/{id}/send_by_email", json=body, validate=validate)

    async def update_status_quote(self, id: int | str, body: Any, *, validate: bool = True) -> Any:
        """PUT /api/external/v2/quotes/{id}/update_status (updateStatusQuote)

        Update status of a quote

        This endpoint allows you to update the status of a quote

        > ℹ️
        > This endpoint requires the following scope: `quotes:all`

        Request body: JSON, validated against spec.schema("updateStatusQuote").
        """
        return await self._client.request("PUT", f"/api/external/v2/quotes/{id}/update_status", json=body, validate=validate)

    async def get_quote_appendices(self, quote_id: int | str, *, cursor: str | None = None, limit: int | None = None) -> Any:
        """GET /api/external/v2/quotes/{quote_id}/appendices (getQuoteAppendices)

        List appendices of a quote

        List appendices of a quote

        > ℹ️
        > This endpoint requires one of the following scopes: `quotes:all`, `quotes:readonly`

        Query params:
          cursor (string): Cursor for pagination. Use this to fetch the next set of results.
            The cursor is an opaque string returned in the previous response's metadata.
            Leave empty for the first request.
          limit (integer): Number of items to return per request.
            Defaults to 20 if not specified.
            Must be between 1 and 100.

        Paginated: pass this method to client.paginate() or client.fetch_all().
        """
        return await self._client.request("GET", f"/api/external/v2/quotes/{quote_id}/appendices", params={"cursor": cursor, "limit": limit})

    async def post_quote_appendices(self, quote_id: int | str, files: Any, data: dict | None = None) -> Any:
        """POST /api/external/v2/quotes/{quote_id}/appendices (postQuoteAppendices)

        Upload an appendix for a quote

        Upload a file that will be an appendix attached to a quote.

        Note that this will not upload a file into the DMS (GED).


        > ℹ️
        > This endpoint requires the following scope: `quotes:all`

        Request body: multipart/form-data (files=..., data=...), not validated.
        """
        return await self._client.request("POST", f"/api/external/v2/quotes/{quote_id}/appendices", files=files, data=data)

    async def get_quote_invoice_line_sections(self, quote_id: int | str, *, cursor: str | None = None, limit: int | None = None, sort: str | None = None) -> Any:
        """GET /api/external/v2/quotes/{quote_id}/invoice_line_sections (getQuoteInvoiceLineSections)

        List invoice line sections for a quote

        List invoice line sections for a quote

        > ℹ️
        > This endpoint requires one of the following scopes: `quotes:all`, `quotes:readonly`

        Query params:
          cursor (string): Cursor for pagination. Use this to fetch the next set of results.
            The cursor is an opaque string returned in the previous response's metadata.
            Leave empty for the first request.
          limit (integer): Number of items to return per request.
            Defaults to 20 if not specified.
            Must be between 1 and 100.
          sort (string): You can choose to sort items on specific attributes
            Sort field may be prefixed with `-` for descending order.
            Example : `id` will sort by ascending order, `-id` will sort by descending order.
            Available fields : `id`

        Paginated: pass this method to client.paginate() or client.fetch_all().
        """
        return await self._client.request("GET", f"/api/external/v2/quotes/{quote_id}/invoice_line_sections", params={"cursor": cursor, "limit": limit, "sort": sort})

    async def get_quote_invoice_lines(self, quote_id: int | str, *, cursor: str | None = None, limit: int | None = None, sort: str | None = None) -> Any:
        """GET /api/external/v2/quotes/{quote_id}/invoice_lines (getQuoteInvoiceLines)

        List invoice lines for a quote

        List invoice lines for a quote

        > ℹ️
        > This endpoint requires one of the following scopes: `quotes:all`, `quotes:readonly`

        Query params:
          cursor (string): Cursor for pagination. Use this to fetch the next set of results.
            The cursor is an opaque string returned in the previous response's metadata.
            Leave empty for the first request.
          limit (integer): Number of items to return per request.
            Defaults to 20 if not specified.
            Must be between 1 and 100.
          sort (string): You can choose to sort items on specific attributes
            Sort field may be prefixed with `-` for descending order.
            Example : `id` will sort by ascending order, `-id` will sort by descending order.
            Available fields : `id`

        Paginated: pass this method to client.paginate() or client.fetch_all().
        """
        return await self._client.request("GET", f"/api/external/v2/quotes/{quote_id}/invoice_lines", params={"cursor": cursor, "limit": limit, "sort": sort})



class SupplierInvoicesAPI:
    """Operations tagged "supplier_invoices"."""

    def __init__(self, client) -> None:
        self._client = client

    async def get_supplier_invoices(self, *, cursor: str | None = None, limit: int | None = None, filter: str | list[dict] | None = None, sort: str | None = None) -> Any:
        """GET /api/external/v2/supplier_invoices (getSupplierInvoices)

        List supplier invoices

        This endpoint returns a list of supplier invoices.

        > ℹ️
        > This endpoint requires one of the following scopes: `supplier_invoices:all`, `supplier_invoices:readonly`

        Query params:
          cursor (string): Cursor for pagination. Use this to fetch the next set of results.
            The cursor is an opaque string returned in the previous response's metadata.
            Leave empty for the first request.
          limit (integer): Number of items to return per request.
            Defaults to 20 if not specified.
            Must be between 1 and 100.
          filter (string): You can choose to filter items on specific fields.
            Available fields and values:
            - `id`: `lt`, `lteq`, `gt`, `gteq`, `eq`, `not_eq`, `in`, `not_in`
            - `supplier_id`: `lt`, `lteq`, `gt`, `gteq`, `eq`, `not_eq`, `in`, `not_in`
            - `invoice_number`: `eq`, `not_eq`, `in`, `not_in`
            - `date`: `lt`, `lteq`, `gt`, `gteq`, `eq`, `not_eq`, `in`, `not_in`
            - `category_id`: `in`
            - `external_reference`: `eq`, `not_eq`, `in`, `not_in`
            - `payment_status`: `eq`, `not_eq`, `in`, `not_in`
            - `flow_id`: `eq`, `not_eq`, `in`, `not_in`
          sort (string): You can choose to sort items on specific attributes
            Sort field may be prefixed with `-` for descending order.
            Example : `id` will sort by ascending order, `-id` will sort by descending order.
            Available fields : `id`, `date`

        Paginated: pass this method to client.paginate() or client.fetch_all().
        """
        return await self._client.request("GET", "/api/external/v2/supplier_invoices", params={"cursor": cursor, "limit": limit, "filter": filter, "sort": sort})

    async def create_supplier_invoice_einvoice_import(self, files: Any, data: dict | None = None) -> Any:
        """POST /api/external/v2/supplier_invoices/e_invoices/imports (createSupplierInvoiceEInvoiceImport)

        Import a supplier e-invoice

        Import a supplier invoice from an e-invoice file.
        The file must be a Factur-X PDF, a standalone UBL XML invoice, or a standalone CII XML invoice.
        Optionally provide `invoice_options` to pre-fill supplier and line-level data.
        Invoice line `e_invoice_line_id` must match Factur-X BT-126 (LineID) or the UBL/CII line identifier.

        > ⚠️ **UBL and CII XML support is in alpha.**
        > A 201 response confirms the file was accepted and parsed, but invoices imported via
        > standalone UBL or CII XML have two known limitations:
        > - The uploaded file is **not displayed** in the app — no document preview is generated yet for these formats.
        > - The invoice is **not recognized as an electronic invoice** within Pennylane.
        >
        > Factur-X PDF remains the recommended format for production use.


        > ℹ️
        > This endpoint requires the following scope: `supplier_invoices:all`

        Request body: multipart/form-data (files=..., data=...), not validated.
        """
        return await self._client.request("POST", "/api/external/v2/supplier_invoices/e_invoices/imports", files=files, data=data)

    async def import_supplier_invoice(self, body: Any, *, validate: bool = True) -> Any:
        """POST /api/external/v2/supplier_invoices/import (importSupplierInvoice)

        Import a supplier invoice with a file attached

        This endpoint allows you to import a supplier invoice with a file
        attached.


        > ℹ️
        > This endpoint requires the following scope: `supplier_invoices:all`

        Request body: JSON, validated against spec.schema("importSupplierInvoice").
        """
        return await self._client.request("POST", "/api/external/v2/supplier_invoices/import", json=body, validate=validate)

    async def get_supplier_invoice(self, id: int | str) -> Any:
        """GET /api/external/v2/supplier_invoices/{id} (getSupplierInvoice)

        Retrieve a supplier invoice

        This endpoint returns a supplier invoice.

        > ℹ️
        > This endpoint requires one of the following scopes: `supplier_invoices:all`, `supplier_invoices:readonly`
        """
        return await self._client.request("GET", f"/api/external/v2/supplier_invoices/{id}")

    async def put_supplier_invoice(self, id: int | str, body: Any, *, validate: bool = True) -> Any:
        """PUT /api/external/v2/supplier_invoices/{id} (putSupplierInvoice)

        Update a supplier invoice

        This endpoint allows you to update a supplier invoice.

        > ℹ️
        > This endpoint requires the following scope: `supplier_invoices:all`

        Request body: JSON, validated against spec.schema("putSupplierInvoice").
        """
        return await self._client.request("PUT", f"/api/external/v2/supplier_invoices/{id}", json=body, validate=validate)

    async def validate_accounting_supplier_invoice(self, id: int | str) -> Any:
        """PUT /api/external/v2/supplier_invoices/{id}/validate_accounting (ValidateAccountingSupplierInvoice)

        Validate the accounting of a supplier invoice

        Turn the supplier invoice into a Complete state.

        > ℹ️
        > This endpoint requires the following scope: `supplier_invoices:all`
        """
        return await self._client.request("PUT", f"/api/external/v2/supplier_invoices/{id}/validate_accounting")

    async def get_supplier_invoice_categories(self, supplier_invoice_id: int | str, *, cursor: str | None = None, limit: int | None = None) -> Any:
        """GET /api/external/v2/supplier_invoices/{supplier_invoice_id}/categories (getSupplierInvoiceCategories)

        List categories of a supplier invoice

        List categories of a supplier invoice

        > ℹ️
        > This endpoint requires one of the following scopes: `supplier_invoices:all`, `supplier_invoices:readonly`

        Query params:
          cursor (string): Cursor for pagination. Use this to fetch the next set of results.
            The cursor is an opaque string returned in the previous response's metadata.
            Leave empty for the first request.
          limit (integer): Number of items to return per request.
            Defaults to 20 if not specified.
            Must be between 1 and 100.

        Paginated: pass this method to client.paginate() or client.fetch_all().
        """
        return await self._client.request("GET", f"/api/external/v2/supplier_invoices/{supplier_invoice_id}/categories", params={"cursor": cursor, "limit": limit})

    async def put_supplier_invoice_categories(self, supplier_invoice_id: int | str, body: Any, *, validate: bool = True) -> Any:
        """PUT /api/external/v2/supplier_invoices/{supplier_invoice_id}/categories (putSupplierInvoiceCategories)

        Categorize a supplier invoice

        Update the categories of a supplier invoice. You can pass categories that don't belong to the same category group. The sum of categories of a same group must equal `1`. In the following example, the two first categories belong to the same category group A, the sum of the weights is `1`. The third category belongs to a category group B, its weight is `1`.
        ```
        [
          { "id": 59, "weight": "0.5" }, // category group A
          { "id": 33, "weight": "0.5" }, // category group A
          { "id": 65, "weight": "1" } // category group B
        ]
        ```


        > ℹ️
        > This endpoint requires the following scope: `supplier_invoices:all`

        Request body: JSON, validated against spec.schema("putSupplierInvoiceCategories").
        """
        return await self._client.request("PUT", f"/api/external/v2/supplier_invoices/{supplier_invoice_id}/categories", json=body, validate=validate)

    async def put_supplier_invoice_einvoice_status(self, supplier_invoice_id: int | str, body: Any, *, validate: bool = True) -> Any:
        """PUT /api/external/v2/supplier_invoices/{supplier_invoice_id}/e_invoice_status (putSupplierInvoiceEInvoiceStatus)

        Update e-invoice status for a supplier invoice

        Applies an electronic invoicing lifecycle transition to a supplier invoice received via the PA.

        Invoices arrive with a `null` e-invoicing status, which means implicitly approved — no action is required to accept them.

        Allowed transitions:
        - **Dispute** (`status: "disputed"`): allowed when the current e-invoicing status is `null`, `approved`, or `waiting_for_validation`, the invoice is not archived, and it has no linked payments. Requires a `reason`.
        - **Refuse** (`status: "refused"`): allowed when the invoice is not archived and has no linked payments. Requires a `reason`. This is a terminal action — the invoice will be archived and cannot be disputed or refused again.
        - **Undispute** (`status: "approved"`): allowed only when the current e-invoicing status is `disputed`. Removes the dispute and restores the invoice to approved. No reason required.

        Returns 422 if the transition is not allowed given the current status (e.g. undisputing a non-disputed invoice, or disputing/refusing a collected invoice).


        > ℹ️
        > This endpoint requires the following scope: `supplier_invoices:all`

        Request body: JSON, validated against spec.schema("putSupplierInvoiceEInvoiceStatus").
        """
        return await self._client.request("PUT", f"/api/external/v2/supplier_invoices/{supplier_invoice_id}/e_invoice_status", json=body, validate=validate)

    async def get_supplier_invoice_lines(self, supplier_invoice_id: int | str, *, cursor: str | None = None, limit: int | None = None, sort: str | None = None) -> Any:
        """GET /api/external/v2/supplier_invoices/{supplier_invoice_id}/invoice_lines (getSupplierInvoiceLines)

        List invoice lines for a supplier invoice

        List invoice lines for a supplier invoice

        > ℹ️
        > This endpoint requires one of the following scopes: `supplier_invoices:all`, `supplier_invoices:readonly`

        Query params:
          cursor (string): Cursor for pagination. Use this to fetch the next set of results.
            The cursor is an opaque string returned in the previous response's metadata.
            Leave empty for the first request.
          limit (integer): Number of items to return per request.
            Defaults to 20 if not specified.
            Must be between 1 and 100.
          sort (string): You can choose to sort items on specific attributes
            Sort field may be prefixed with `-` for descending order.
            Example : `id` will sort by ascending order, `-id` will sort by descending order.
            Available fields : `id`

        Paginated: pass this method to client.paginate() or client.fetch_all().
        """
        return await self._client.request("GET", f"/api/external/v2/supplier_invoices/{supplier_invoice_id}/invoice_lines", params={"cursor": cursor, "limit": limit, "sort": sort})

    async def post_supplier_invoice_linked_purchase_requests(self, supplier_invoice_id: int | str, body: Any, *, validate: bool = True) -> Any:
        """POST /api/external/v2/supplier_invoices/{supplier_invoice_id}/linked_purchase_requests (postSupplierInvoiceLinkedPurchaseRequests)

        Link a purchase request to a supplier invoice

        This endpoint allows you to link a purchase request to a supplier invoice.

        You can link one purchase request with one supplier invoice at a time. To link multiple purchase request to a supplier invoice, you need to call this endpoint multiple times.
        It's possible to link a purchase request to multiple supplier invoices too.


        > ℹ️
        > This endpoint requires the following scope: `supplier_invoices:all`

        Request body: JSON, validated against spec.schema("postSupplierInvoiceLinkedPurchaseRequests").
        """
        return await self._client.request("POST", f"/api/external/v2/supplier_invoices/{supplier_invoice_id}/linked_purchase_requests", json=body, validate=validate)

    async def get_supplier_invoice_matched_transactions(self, supplier_invoice_id: int | str, *, cursor: str | None = None, limit: int | None = None, sort: str | None = None) -> Any:
        """GET /api/external/v2/supplier_invoices/{supplier_invoice_id}/matched_transactions (getSupplierInvoiceMatchedTransactions)

        List matched transactions for a supplier invoice

        List matched transactions for a supplier invoice

        > ℹ️
        > This endpoint requires one of the following scopes: `supplier_invoices:all`, `supplier_invoices:readonly`

        Query params:
          cursor (string): Cursor for pagination. Use this to fetch the next set of results.
            The cursor is an opaque string returned in the previous response's metadata.
            Leave empty for the first request.
          limit (integer): Number of items to return per request.
            Defaults to 20 if not specified.
            Must be between 1 and 100.
          sort (string): You can choose to sort items on specific attributes
            Sort field may be prefixed with `-` for descending order.
            Example : `id` will sort by ascending order, `-id` will sort by descending order.
            Available fields : `id`

        Paginated: pass this method to client.paginate() or client.fetch_all().
        """
        return await self._client.request("GET", f"/api/external/v2/supplier_invoices/{supplier_invoice_id}/matched_transactions", params={"cursor": cursor, "limit": limit, "sort": sort})

    async def update_supplier_invoice_payment_status(self, supplier_invoice_id: int | str, body: Any, *, validate: bool = True) -> Any:
        """PUT /api/external/v2/supplier_invoices/{supplier_invoice_id}/payment_status (updateSupplierInvoicePaymentStatus)

        Update a supplier invoice payment status

        This endpoint allows you to update the payment status of a supplier
        invoice.


        > ℹ️
        > This endpoint requires the following scope: `supplier_invoices:all`

        Request body: JSON, validated against spec.schema("updateSupplierInvoicePaymentStatus").
        """
        return await self._client.request("PUT", f"/api/external/v2/supplier_invoices/{supplier_invoice_id}/payment_status", json=body, validate=validate)

    async def get_supplier_invoice_payments(self, supplier_invoice_id: int | str, *, cursor: str | None = None, limit: int | None = None, sort: str | None = None) -> Any:
        """GET /api/external/v2/supplier_invoices/{supplier_invoice_id}/payments (getSupplierInvoicePayments)

        List payments for a supplier invoice

        List payments for a supplier invoice

        > ℹ️
        > This endpoint requires one of the following scopes: `supplier_invoices:all`, `supplier_invoices:readonly`

        Query params:
          cursor (string): Cursor for pagination. Use this to fetch the next set of results.
            The cursor is an opaque string returned in the previous response's metadata.
            Leave empty for the first request.
          limit (integer): Number of items to return per request.
            Defaults to 20 if not specified.
            Must be between 1 and 100.
          sort (string): You can choose to sort items on specific attributes
            Sort field may be prefixed with `-` for descending order.
            Example : `id` will sort by ascending order, `-id` will sort by descending order.
            Available fields : `id`

        Paginated: pass this method to client.paginate() or client.fetch_all().
        """
        return await self._client.request("GET", f"/api/external/v2/supplier_invoices/{supplier_invoice_id}/payments", params={"cursor": cursor, "limit": limit, "sort": sort})



class SuppliersAPI:
    """Operations tagged "suppliers"."""

    def __init__(self, client) -> None:
        self._client = client

    async def get_suppliers(self, *, cursor: str | None = None, limit: int | None = None, filter: str | list[dict] | None = None, sort: str | None = None) -> Any:
        """GET /api/external/v2/suppliers (getSuppliers)

        List suppliers

        List suppliers

        > ℹ️
        > This endpoint requires one of the following scopes: `suppliers:all`, `suppliers:readonly`

        Query params:
          cursor (string): Cursor for pagination. Use this to fetch the next set of results.
            The cursor is an opaque string returned in the previous response's metadata.
            Leave empty for the first request.
          limit (integer): Number of items to return per request.
            Defaults to 20 if not specified.
            Must be between 1 and 100.
          filter (string): You can choose to filter items on specific fields.
            Available fields and values:
            - `id`: `lt`, `lteq`, `gt`, `gteq`, `eq`, `not_eq`, `in`, `not_in`
            - `ledger_account_id`: `eq`, `not_eq`
            - `name`: `start_with`
            - `external_reference`: `eq`, `not_eq`, `in`, `not_in`
            - `emails`: `in`
          sort (string): You can choose to sort items on specific attributes
            Sort field may be prefixed with `-` for descending order.
            Example : `id` will sort by ascending order, `-id` will sort by descending order.
            Available fields : `id`

        Paginated: pass this method to client.paginate() or client.fetch_all().
        """
        return await self._client.request("GET", "/api/external/v2/suppliers", params={"cursor": cursor, "limit": limit, "filter": filter, "sort": sort})

    async def post_supplier(self, body: Any, *, validate: bool = True) -> Any:
        """POST /api/external/v2/suppliers (postSupplier)

        Create a Supplier

        This endpoint returns the created supplier.

        > ℹ️
        > This endpoint requires the following scope: `suppliers:all`

        Request body: JSON, validated against spec.schema("postSupplier").
        """
        return await self._client.request("POST", "/api/external/v2/suppliers", json=body, validate=validate)

    async def get_supplier(self, id: int | str) -> Any:
        """GET /api/external/v2/suppliers/{id} (getSupplier)

        Retrieve a supplier

        This endpoint returns a supplier.

        > ℹ️
        > This endpoint requires one of the following scopes: `suppliers:all`, `suppliers:readonly`
        """
        return await self._client.request("GET", f"/api/external/v2/suppliers/{id}")

    async def put_supplier(self, id: int | str, body: Any, *, validate: bool = True) -> Any:
        """PUT /api/external/v2/suppliers/{id} (putSupplier)

        Update a supplier

        This endpoint returns the updated supplier.

        > ℹ️
        > This endpoint requires the following scope: `suppliers:all`

        Request body: JSON, validated against spec.schema("putSupplier").
        """
        return await self._client.request("PUT", f"/api/external/v2/suppliers/{id}", json=body, validate=validate)

    async def get_supplier_categories(self, supplier_id: int | str, *, cursor: str | None = None, limit: int | None = None) -> Any:
        """GET /api/external/v2/suppliers/{supplier_id}/categories (getSupplierCategories)

        List categories of a supplier

        List categories of a supplier

        > ℹ️
        > This endpoint requires one of the following scopes: `suppliers:readonly`, `suppliers:all`

        Query params:
          cursor (string): Cursor for pagination. Use this to fetch the next set of results.
            The cursor is an opaque string returned in the previous response's metadata.
            Leave empty for the first request.
          limit (integer): Number of items to return per request.
            Defaults to 20 if not specified.
            Must be between 1 and 100.

        Paginated: pass this method to client.paginate() or client.fetch_all().
        """
        return await self._client.request("GET", f"/api/external/v2/suppliers/{supplier_id}/categories", params={"cursor": cursor, "limit": limit})

    async def put_supplier_categories(self, supplier_id: int | str, body: Any, *, validate: bool = True) -> Any:
        """PUT /api/external/v2/suppliers/{supplier_id}/categories (putSupplierCategories)

        Categorize a supplier

        Update the categories of a supplier. You can pass categories that don't belong to the same category group. The sum of categories of a same group must equal `1`. In the following example, the two first categories belong to the same category group A, the sum of the weights is `1`. The third category belongs to a category group B, its weight is `1`.
        ```
        [
          { "id": 59, "weight": "0.5" }, // category group A
          { "id": 33, "weight": "0.5" }, // category group A
          { "id": 65, "weight": "1" }    // category group B
        ]
        ```


        > ℹ️
        > This endpoint requires the following scope: `suppliers:all`

        Request body: JSON, validated against spec.schema("putSupplierCategories").
        """
        return await self._client.request("PUT", f"/api/external/v2/suppliers/{supplier_id}/categories", json=body, validate=validate)



class TransactionsAPI:
    """Operations tagged "transactions"."""

    def __init__(self, client) -> None:
        self._client = client

    async def post_customer_invoice_matched_transactions(self, customer_invoice_id: int | str, body: Any, *, validate: bool = True) -> Any:
        """POST /api/external/v2/customer_invoices/{customer_invoice_id}/matched_transactions (postCustomerInvoiceMatchedTransactions)

        Match a transaction to a customer invoice

        This endpoint allows you to match a transaction to a customer invoice. It is not applicable for draft invoices.

        You can match one transaction with one customer invoice at a time. To match multiple transactions to a customer invoice, you need to call this endpoint multiple times.
        It's possible to match a transaction to multiple customer invoices too.


        > ℹ️
        > This endpoint requires the following scope: `customer_invoices:all`

        Request body: JSON, validated against spec.schema("postCustomerInvoiceMatchedTransactions").
        """
        return await self._client.request("POST", f"/api/external/v2/customer_invoices/{customer_invoice_id}/matched_transactions", json=body, validate=validate)

    async def delete_customer_invoice_matched_transactions(self, customer_invoice_id: int | str, id: int | str) -> Any:
        """DELETE /api/external/v2/customer_invoices/{customer_invoice_id}/matched_transactions/{id} (deleteCustomerInvoiceMatchedTransactions)

        Unmatch a transaction to a customer invoice

        This endpoint allows you to unmatch a transaction to a customer invoice. It is not applicable for draft invoices.


        > ℹ️
        > This endpoint requires the following scope: `customer_invoices:all`
        """
        return await self._client.request("DELETE", f"/api/external/v2/customer_invoices/{customer_invoice_id}/matched_transactions/{id}")

    async def post_supplier_invoice_matched_transactions(self, supplier_invoice_id: int | str, body: Any, *, validate: bool = True) -> Any:
        """POST /api/external/v2/supplier_invoices/{supplier_invoice_id}/matched_transactions (postSupplierInvoiceMatchedTransactions)

        Match a transaction to a supplier invoice

        This endpoint allows you to match a transaction to a supplier invoice.

        You can match one transaction with one supplier invoice at a time. To match multiple transactions to a supplier invoice, you need to call this endpoint multiple times.
        It's possible to match a transaction to multiple supplier invoices too.


        > ℹ️
        > This endpoint requires the following scope: `supplier_invoices:all`

        Request body: JSON, validated against spec.schema("postSupplierInvoiceMatchedTransactions").
        """
        return await self._client.request("POST", f"/api/external/v2/supplier_invoices/{supplier_invoice_id}/matched_transactions", json=body, validate=validate)

    async def delete_supplier_invoice_matched_transactions(self, supplier_invoice_id: int | str, id: int | str) -> Any:
        """DELETE /api/external/v2/supplier_invoices/{supplier_invoice_id}/matched_transactions/{id} (deleteSupplierInvoiceMatchedTransactions)

        Unmatch a transaction to a supplier invoice

        This endpoint allows you to unmatch a transaction to a supplier
        invoice.


        > ℹ️
        > This endpoint requires the following scope: `supplier_invoices:all`
        """
        return await self._client.request("DELETE", f"/api/external/v2/supplier_invoices/{supplier_invoice_id}/matched_transactions/{id}")

    async def get_transactions(self, *, cursor: str | None = None, limit: int | None = None, filter: str | list[dict] | None = None, sort: str | None = None) -> Any:
        """GET /api/external/v2/transactions (getTransactions)

        List transactions

        List transactions

        > ℹ️
        > This endpoint requires one of the following scopes: `transactions:readonly`, `transactions:all`

        Query params:
          cursor (string): Cursor for pagination. Use this to fetch the next set of results.
            The cursor is an opaque string returned in the previous response's metadata.
            Leave empty for the first request.
          limit (integer): Number of items to return per request.
            Defaults to 20 if not specified.
            Must be between 1 and 100.
          filter (string): You can choose to filter items on specific fields.
            Available fields and values:
            - `id`: `eq`, `not_eq`, `in`, `not_in`
            - `bank_account_id`: `eq`, `not_eq`, `in`, `not_in`
            - `journal_id`: `eq`, `not_eq`, `in`, `not_in`
            - `date`: `eq`, `not_eq`, `gt`, `lt`, `lteq`, `gteq`
          sort (string): You can choose to sort items on specific attributes
            Sort field may be prefixed with `-` for descending order.
            Example : `id` will sort by ascending order, `-id` will sort by descending order.
            Available fields : `id`

        Paginated: pass this method to client.paginate() or client.fetch_all().
        """
        return await self._client.request("GET", "/api/external/v2/transactions", params={"cursor": cursor, "limit": limit, "filter": filter, "sort": sort})

    async def create_transaction(self, body: Any, *, validate: bool = True) -> Any:
        """POST /api/external/v2/transactions (createTransaction)

        Create a transaction

        Create a banking transaction

        > ℹ️
        > This endpoint requires the following scope: `transactions:all`

        Request body: JSON, validated against spec.schema("createTransaction").
        """
        return await self._client.request("POST", "/api/external/v2/transactions", json=body, validate=validate)

    async def get_transaction(self, id: int | str) -> Any:
        """GET /api/external/v2/transactions/{id} (getTransaction)

        Retrieve a transaction

        Retrieve a transaction

        > ℹ️
        > This endpoint requires one of the following scopes: `transactions:readonly`, `transactions:all`
        """
        return await self._client.request("GET", f"/api/external/v2/transactions/{id}")

    async def update_transaction(self, id: int | str, body: Any, *, validate: bool = True) -> Any:
        """PUT /api/external/v2/transactions/{id} (updateTransaction)

        Update a transaction

        This endpoint returns the updated transaction.

        > ℹ️
        > This endpoint requires the following scope: `transactions:all`

        Request body: JSON, validated against spec.schema("updateTransaction").
        """
        return await self._client.request("PUT", f"/api/external/v2/transactions/{id}", json=body, validate=validate)

    async def get_transaction_categories(self, transaction_id: int | str, *, cursor: str | None = None, limit: int | None = None) -> Any:
        """GET /api/external/v2/transactions/{transaction_id}/categories (getTransactionCategories)

        List categories of a bank transaction

        List categories of a bank transaction

        > ℹ️
        > This endpoint requires one of the following scopes: `transactions:readonly`, `transactions:all`

        Query params:
          cursor (string): Cursor for pagination. Use this to fetch the next set of results.
            The cursor is an opaque string returned in the previous response's metadata.
            Leave empty for the first request.
          limit (integer): Number of items to return per request.
            Defaults to 20 if not specified.
            Must be between 1 and 100.

        Paginated: pass this method to client.paginate() or client.fetch_all().
        """
        return await self._client.request("GET", f"/api/external/v2/transactions/{transaction_id}/categories", params={"cursor": cursor, "limit": limit})

    async def put_transaction_categories(self, transaction_id: int | str, body: Any, *, validate: bool = True) -> Any:
        """PUT /api/external/v2/transactions/{transaction_id}/categories (putTransactionCategories)

        Categorize a bank transaction

        Update the categories of a transaction. You can pass categories that don't belong to the same category group. The sum of categories of a same group must equal `1`. In the following example, the two first categories belong to the same category group A, the sum of the weights is `1`. The third category belongs to a category group B, its weight is `1`.
        ```
        [
          { "id": 59, "weight": "0.5" }, // category group A
          { "id": 33, "weight": "0.5" }, // category group A
          { "id": 65, "weight": "1" } // category group B
        ]
        ```


        > ℹ️
        > This endpoint requires the following scope: `transactions:all`

        Request body: JSON, validated against spec.schema("putTransactionCategories").
        """
        return await self._client.request("PUT", f"/api/external/v2/transactions/{transaction_id}/categories", json=body, validate=validate)

    async def get_transaction_matched_invoices(self, transaction_id: int | str, *, cursor: str | None = None, limit: int | None = None) -> Any:
        """GET /api/external/v2/transactions/{transaction_id}/matched_invoices (getTransactionMatchedInvoices)

        List invoices matched to a bank transaction

        List invoices matched to a bank transaction

        > ℹ️
        > This endpoint requires one of the following scopes: `transactions:readonly`, `transactions:all`

        Query params:
          cursor (string): Cursor for pagination. Use this to fetch the next set of results.
            The cursor is an opaque string returned in the previous response's metadata.
            Leave empty for the first request.
          limit (integer): Number of items to return per request.
            Defaults to 20 if not specified.
            Must be between 1 and 100.

        Paginated: pass this method to client.paginate() or client.fetch_all().
        """
        return await self._client.request("GET", f"/api/external/v2/transactions/{transaction_id}/matched_invoices", params={"cursor": cursor, "limit": limit})



class TrialBalanceAPI:
    """Operations tagged "trial_balance"."""

    def __init__(self, client) -> None:
        self._client = client

    async def get_trial_balance(self, *, period_start: str, period_end: str, is_auxiliary: bool | None = None, cursor: str | None = None, limit: int | None = None) -> Any:
        """GET /api/external/v2/trial_balance (getTrialBalance)

        Get the trial balance

        This endpoint returns the trial balance of the current company
        for the given period.

        > ℹ️
        > This endpoint requires the following scope: `trial_balance:readonly`

        Query params:
          period_start (string, REQUIRED): The start of the period you want the trial balance for.
          period_end (string, REQUIRED): The end of the period you want the trial balance for.
          is_auxiliary (boolean): Whether to include auxiliary accounts or not.
          cursor (string): Cursor for pagination. Use this to fetch the next set of results.
            The cursor is an opaque string returned in the previous response's metadata.
            Leave empty for the first request.
          limit (integer): Number of items to return per request.
            Defaults to 20 if not specified.
            Must be between 1 and 1000.

        Paginated: pass this method to client.paginate() or client.fetch_all().
        """
        return await self._client.request("GET", "/api/external/v2/trial_balance", params={"period_start": period_start, "period_end": period_end, "is_auxiliary": is_auxiliary, "cursor": cursor, "limit": limit})



class UsersAPI:
    """Operations tagged "users"."""

    def __init__(self, client) -> None:
        self._client = client

    async def get_me(self) -> Any:
        """GET /api/external/v2/me (getMe)

        User Profile

        This endpoint returns information about the company and the user associated to the token.
        """
        return await self._client.request("GET", "/api/external/v2/me")



class WebhooksAPI:
    """Operations tagged "webhooks"."""

    def __init__(self, client) -> None:
        self._client = client

    async def get_webhook_subscriptions(self, *, cursor: str | None = None, limit: int | None = None) -> Any:
        """GET /api/external/v2/webhook_subscriptions (getWebhookSubscriptions)

        List webhook subscriptions

        Returns all webhook subscriptions for the authenticated token, paginated.
        Note that the secret is not included in the response.

        Query params:
          cursor (string): Opaque cursor from a previous response to retrieve the next page
          limit (integer): Number of items to return per page

        Paginated: pass this method to client.paginate() or client.fetch_all().
        """
        return await self._client.request("GET", "/api/external/v2/webhook_subscriptions", params={"cursor": cursor, "limit": limit})

    async def post_webhook_subscriptions(self, body: Any, *, validate: bool = True) -> Any:
        """POST /api/external/v2/webhook_subscriptions (postWebhookSubscriptions)

        Create a webhook subscription

        Creates a webhook subscription to receive real-time notifications for events occurring within your company or companies.

        **Authentication & Scope**

        Subscription scope:
        - **Company-scoped token** (developer token or OAuth token bound to a specific company): the subscription is scoped to that single company.
        - **App-bound token** (OAuth token without a company context): the subscription covers all companies accessible by the OAuth application.

        **Limits**
        Up to 10 webhook subscriptions are allowed per company (for company-scoped tokens) or per subscriber (for app-bound tokens).

        **Secret**
        The secret will be auto-generated.

        > 🔒 The secret is **only returned in the creation response** and cannot be retrieved afterwards. Make sure to store it securely.

        Request body: JSON, validated against spec.schema("postWebhookSubscriptions").
        """
        return await self._client.request("POST", "/api/external/v2/webhook_subscriptions", json=body, validate=validate)

    async def delete_webhook_subscription(self, id: int | str) -> Any:
        """DELETE /api/external/v2/webhook_subscriptions/{id} (deleteWebhookSubscription)

        Delete a webhook subscription

        This endpoint allows you to delete a webhook subscription by ID.
        """
        return await self._client.request("DELETE", f"/api/external/v2/webhook_subscriptions/{id}")

    async def get_webhook_subscription(self, id: int | str) -> Any:
        """GET /api/external/v2/webhook_subscriptions/{id} (getWebhookSubscription)

        Get a webhook subscription

        This endpoint allows you to retrieve a webhook subscription by ID.
        Note that the secret is not included in the response.
        """
        return await self._client.request("GET", f"/api/external/v2/webhook_subscriptions/{id}")

    async def put_webhook_subscription(self, id: int | str, body: Any, *, validate: bool = True) -> Any:
        """PUT /api/external/v2/webhook_subscriptions/{id} (putWebhookSubscription)

        Update a webhook subscription

        This endpoint allows you to update a webhook subscription by ID.

        Request body: JSON, validated against spec.schema("putWebhookSubscription").
        """
        return await self._client.request("PUT", f"/api/external/v2/webhook_subscriptions/{id}", json=body, validate=validate)



class PennylaneAPI:
    """Namespaced access to every operation of the Pennylane API.

    Usage::

        page = await client.api.customer_invoices.get_customer_invoices(limit=100)
        invoice = await client.api.customer_invoices.get_customer_invoice(42)
    """

    def __init__(self, client) -> None:
        self.bank_accounts = BankAccountsAPI(client)
        self.bank_establishments = BankEstablishmentsAPI(client)
        self.billing_subscriptions = BillingSubscriptionsAPI(client)
        self.categories = CategoriesAPI(client)
        self.category_groups = CategoryGroupsAPI(client)
        self.changelogs = ChangelogsAPI(client)
        self.commercial_documents = CommercialDocumentsAPI(client)
        self.customer_invoice_templates = CustomerInvoiceTemplatesAPI(client)
        self.customer_invoices = CustomerInvoicesAPI(client)
        self.customers = CustomersAPI(client)
        self.exports = ExportsAPI(client)
        self.file_attachments = FileAttachmentsAPI(client)
        self.fiscal_years = FiscalYearsAPI(client)
        self.journals = JournalsAPI(client)
        self.ledger_accounts = LedgerAccountsAPI(client)
        self.ledger_attachments = LedgerAttachmentsAPI(client)
        self.ledger_entries = LedgerEntriesAPI(client)
        self.ledger_entry_lines = LedgerEntryLinesAPI(client)
        self.mandates = MandatesAPI(client)
        self.numberings = NumberingsAPI(client)
        self.pa_registrations = PaRegistrationsAPI(client)
        self.products = ProductsAPI(client)
        self.purchase_requests = PurchaseRequestsAPI(client)
        self.quotes = QuotesAPI(client)
        self.supplier_invoices = SupplierInvoicesAPI(client)
        self.suppliers = SuppliersAPI(client)
        self.transactions = TransactionsAPI(client)
        self.trial_balance = TrialBalanceAPI(client)
        self.users = UsersAPI(client)
        self.webhooks = WebhooksAPI(client)


ENDPOINT_INDEX: dict[tuple[str, str], tuple[str, str]] = {
    ("DELETE", "/api/external/v2/customer_invoices/{customer_invoice_id}/matched_transactions/{id}"): ("transactions", "delete_customer_invoice_matched_transactions"),
    ("DELETE", "/api/external/v2/customer_invoices/{id}"): ("customer_invoices", "delete_customer_invoices"),
    ("DELETE", "/api/external/v2/customers/{customer_id}/contacts/{id}"): ("customers", "delete_customer_contact"),
    ("DELETE", "/api/external/v2/ledger_entry_lines/lettering"): ("ledger_entry_lines", "delete_ledger_entry_lines_unletter"),
    ("DELETE", "/api/external/v2/sepa_mandates/{id}"): ("mandates", "delete_sepa_mandate"),
    ("DELETE", "/api/external/v2/supplier_invoices/{supplier_invoice_id}/matched_transactions/{id}"): ("transactions", "delete_supplier_invoice_matched_transactions"),
    ("DELETE", "/api/external/v2/webhook_subscriptions/{id}"): ("webhooks", "delete_webhook_subscription"),
    ("GET", "/api/external/v2/bank_accounts"): ("bank_accounts", "get_bank_accounts"),
    ("GET", "/api/external/v2/bank_accounts/{id}"): ("bank_accounts", "get_bank_account"),
    ("GET", "/api/external/v2/bank_establishments"): ("bank_establishments", "get_bank_establishments"),
    ("GET", "/api/external/v2/billing_subscriptions"): ("billing_subscriptions", "get_billing_subscriptions"),
    ("GET", "/api/external/v2/billing_subscriptions/{billing_subscription_id}/invoice_line_sections"): ("billing_subscriptions", "get_billing_subscription_invoice_line_sections"),
    ("GET", "/api/external/v2/billing_subscriptions/{billing_subscription_id}/invoice_lines"): ("billing_subscriptions", "get_billing_subscription_invoice_lines"),
    ("GET", "/api/external/v2/billing_subscriptions/{id}"): ("billing_subscriptions", "get_billing_subscription"),
    ("GET", "/api/external/v2/categories"): ("categories", "get_categories"),
    ("GET", "/api/external/v2/categories/{id}"): ("categories", "get_category"),
    ("GET", "/api/external/v2/category_groups"): ("categories", "get_category_groups"),
    ("GET", "/api/external/v2/category_groups/{category_group_id}/categories"): ("category_groups", "get_category_group_categories"),
    ("GET", "/api/external/v2/category_groups/{id}"): ("category_groups", "get_category_group"),
    ("GET", "/api/external/v2/changelogs/customer_invoices"): ("changelogs", "get_customer_invoices_changes"),
    ("GET", "/api/external/v2/changelogs/customers"): ("changelogs", "get_customer_changes"),
    ("GET", "/api/external/v2/changelogs/ledger_entries_categories"): ("changelogs", "get_ledger_entries_category_changes"),
    ("GET", "/api/external/v2/changelogs/ledger_entry_lines"): ("changelogs", "get_ledger_entry_line_changes"),
    ("GET", "/api/external/v2/changelogs/ledger_entry_lines_categories"): ("changelogs", "get_ledger_entry_lines_category_changes"),
    ("GET", "/api/external/v2/changelogs/products"): ("changelogs", "get_product_changes"),
    ("GET", "/api/external/v2/changelogs/quotes"): ("quotes", "get_quote_changes"),
    ("GET", "/api/external/v2/changelogs/supplier_invoices"): ("changelogs", "get_supplier_invoices_changes"),
    ("GET", "/api/external/v2/changelogs/suppliers"): ("changelogs", "get_supplier_changes"),
    ("GET", "/api/external/v2/changelogs/transactions"): ("changelogs", "get_transaction_changes"),
    ("GET", "/api/external/v2/commercial_documents"): ("commercial_documents", "list_commercial_documents"),
    ("GET", "/api/external/v2/commercial_documents/{commercial_document_id}/appendices"): ("commercial_documents", "get_commercial_document_appendices"),
    ("GET", "/api/external/v2/commercial_documents/{commercial_document_id}/invoice_line_sections"): ("commercial_documents", "get_commercial_document_invoice_line_sections"),
    ("GET", "/api/external/v2/commercial_documents/{commercial_document_id}/invoice_lines"): ("commercial_documents", "get_commercial_document_invoice_lines"),
    ("GET", "/api/external/v2/commercial_documents/{id}"): ("commercial_documents", "get_commercial_document"),
    ("GET", "/api/external/v2/company_customers/{id}"): ("customers", "get_company_customer"),
    ("GET", "/api/external/v2/customer_invoice_templates"): ("customer_invoice_templates", "get_customer_invoice_templates"),
    ("GET", "/api/external/v2/customer_invoices"): ("customer_invoices", "get_customer_invoices"),
    ("GET", "/api/external/v2/customer_invoices/{customer_invoice_id}/appendices"): ("customer_invoices", "get_customer_invoice_appendices"),
    ("GET", "/api/external/v2/customer_invoices/{customer_invoice_id}/categories"): ("customer_invoices", "get_customer_invoice_categories"),
    ("GET", "/api/external/v2/customer_invoices/{customer_invoice_id}/custom_header_fields"): ("customer_invoices", "get_customer_invoice_custom_header_fields"),
    ("GET", "/api/external/v2/customer_invoices/{customer_invoice_id}/invoice_line_sections"): ("customer_invoices", "get_customer_invoice_invoice_line_sections"),
    ("GET", "/api/external/v2/customer_invoices/{customer_invoice_id}/invoice_lines"): ("customer_invoices", "get_customer_invoice_invoice_lines"),
    ("GET", "/api/external/v2/customer_invoices/{customer_invoice_id}/matched_transactions"): ("customer_invoices", "get_customer_invoice_matched_transactions"),
    ("GET", "/api/external/v2/customer_invoices/{customer_invoice_id}/payments"): ("customer_invoices", "get_customer_invoice_payments"),
    ("GET", "/api/external/v2/customer_invoices/{id}"): ("customer_invoices", "get_customer_invoice"),
    ("GET", "/api/external/v2/customers"): ("customers", "get_customers"),
    ("GET", "/api/external/v2/customers/{customer_id}/categories"): ("customers", "get_customer_categories"),
    ("GET", "/api/external/v2/customers/{customer_id}/contacts"): ("customers", "get_customer_contacts"),
    ("GET", "/api/external/v2/customers/{customer_id}/contacts/{id}"): ("customers", "get_customer_contact"),
    ("GET", "/api/external/v2/customers/{id}"): ("customers", "get_customer"),
    ("GET", "/api/external/v2/exports/analytical_general_ledgers/{id}"): ("exports", "get_analytical_general_ledger_export"),
    ("GET", "/api/external/v2/exports/fecs/{id}"): ("exports", "get_fec_export"),
    ("GET", "/api/external/v2/exports/general_ledgers/{id}"): ("exports", "get_general_ledger_export"),
    ("GET", "/api/external/v2/fiscal_years"): ("fiscal_years", "company_fiscal_years"),
    ("GET", "/api/external/v2/gocardless_mandates"): ("mandates", "get_gocardless_mandates"),
    ("GET", "/api/external/v2/gocardless_mandates/{id}"): ("mandates", "get_gocardless_mandate"),
    ("GET", "/api/external/v2/individual_customers/{id}"): ("customers", "get_individual_customer"),
    ("GET", "/api/external/v2/journals"): ("journals", "get_journals"),
    ("GET", "/api/external/v2/journals/{id}"): ("journals", "get_journal"),
    ("GET", "/api/external/v2/ledger_accounts"): ("ledger_accounts", "get_ledger_accounts"),
    ("GET", "/api/external/v2/ledger_accounts/{id}"): ("ledger_accounts", "get_ledger_account"),
    ("GET", "/api/external/v2/ledger_entries"): ("ledger_entries", "get_ledger_entries"),
    ("GET", "/api/external/v2/ledger_entries/{id}"): ("ledger_entries", "get_ledger_entry"),
    ("GET", "/api/external/v2/ledger_entries/{ledger_entry_id}/ledger_entry_lines"): ("ledger_entries", "get_ledger_entries_ledger_entry_lines"),
    ("GET", "/api/external/v2/ledger_entry_lines"): ("ledger_entry_lines", "get_ledger_entry_lines"),
    ("GET", "/api/external/v2/ledger_entry_lines/{id}"): ("ledger_entry_lines", "get_ledger_entry_line"),
    ("GET", "/api/external/v2/ledger_entry_lines/{ledger_entry_line_id}/categories"): ("ledger_entry_lines", "get_ledger_entry_lines_categories"),
    ("GET", "/api/external/v2/ledger_entry_lines/{ledger_entry_line_id}/lettered_ledger_entry_lines"): ("ledger_entry_lines", "get_ledger_entry_lines_lettered_ledger_entry_lines"),
    ("GET", "/api/external/v2/me"): ("users", "get_me"),
    ("GET", "/api/external/v2/numberings"): ("numberings", "get_numberings"),
    ("GET", "/api/external/v2/pa_registrations"): ("pa_registrations", "get_pa_registrations"),
    ("GET", "/api/external/v2/pro_account/mandate_migrations"): ("mandates", "get_pro_account_mandate_migrations"),
    ("GET", "/api/external/v2/pro_account/mandates"): ("mandates", "get_pro_account_mandates"),
    ("GET", "/api/external/v2/products"): ("products", "get_products"),
    ("GET", "/api/external/v2/products/{id}"): ("products", "get_product"),
    ("GET", "/api/external/v2/purchase_requests"): ("purchase_requests", "get_purchase_requests"),
    ("GET", "/api/external/v2/purchase_requests/{id}"): ("purchase_requests", "get_purchase_request"),
    ("GET", "/api/external/v2/quotes"): ("quotes", "list_quotes"),
    ("GET", "/api/external/v2/quotes/{id}"): ("quotes", "get_quote"),
    ("GET", "/api/external/v2/quotes/{quote_id}/appendices"): ("quotes", "get_quote_appendices"),
    ("GET", "/api/external/v2/quotes/{quote_id}/invoice_line_sections"): ("quotes", "get_quote_invoice_line_sections"),
    ("GET", "/api/external/v2/quotes/{quote_id}/invoice_lines"): ("quotes", "get_quote_invoice_lines"),
    ("GET", "/api/external/v2/sepa_mandates"): ("mandates", "get_sepa_mandates"),
    ("GET", "/api/external/v2/sepa_mandates/{id}"): ("mandates", "get_sepa_mandate"),
    ("GET", "/api/external/v2/supplier_invoices"): ("supplier_invoices", "get_supplier_invoices"),
    ("GET", "/api/external/v2/supplier_invoices/{id}"): ("supplier_invoices", "get_supplier_invoice"),
    ("GET", "/api/external/v2/supplier_invoices/{supplier_invoice_id}/categories"): ("supplier_invoices", "get_supplier_invoice_categories"),
    ("GET", "/api/external/v2/supplier_invoices/{supplier_invoice_id}/invoice_lines"): ("supplier_invoices", "get_supplier_invoice_lines"),
    ("GET", "/api/external/v2/supplier_invoices/{supplier_invoice_id}/matched_transactions"): ("supplier_invoices", "get_supplier_invoice_matched_transactions"),
    ("GET", "/api/external/v2/supplier_invoices/{supplier_invoice_id}/payments"): ("supplier_invoices", "get_supplier_invoice_payments"),
    ("GET", "/api/external/v2/suppliers"): ("suppliers", "get_suppliers"),
    ("GET", "/api/external/v2/suppliers/{id}"): ("suppliers", "get_supplier"),
    ("GET", "/api/external/v2/suppliers/{supplier_id}/categories"): ("suppliers", "get_supplier_categories"),
    ("GET", "/api/external/v2/transactions"): ("transactions", "get_transactions"),
    ("GET", "/api/external/v2/transactions/{id}"): ("transactions", "get_transaction"),
    ("GET", "/api/external/v2/transactions/{transaction_id}/categories"): ("transactions", "get_transaction_categories"),
    ("GET", "/api/external/v2/transactions/{transaction_id}/matched_invoices"): ("transactions", "get_transaction_matched_invoices"),
    ("GET", "/api/external/v2/trial_balance"): ("trial_balance", "get_trial_balance"),
    ("GET", "/api/external/v2/webhook_subscriptions"): ("webhooks", "get_webhook_subscriptions"),
    ("GET", "/api/external/v2/webhook_subscriptions/{id}"): ("webhooks", "get_webhook_subscription"),
    ("POST", "/api/external/v2/bank_accounts"): ("bank_accounts", "post_bank_account"),
    ("POST", "/api/external/v2/billing_subscriptions"): ("billing_subscriptions", "post_billing_subscriptions"),
    ("POST", "/api/external/v2/categories"): ("categories", "post_categories"),
    ("POST", "/api/external/v2/category_groups"): ("category_groups", "post_category_groups"),
    ("POST", "/api/external/v2/commercial_documents"): ("commercial_documents", "post_commercial_documents"),
    ("POST", "/api/external/v2/commercial_documents/{commercial_document_id}/appendices"): ("commercial_documents", "post_commercial_document_appendices"),
    ("POST", "/api/external/v2/company_customers"): ("customers", "post_company_customer"),
    ("POST", "/api/external/v2/customer_invoices"): ("customer_invoices", "post_customer_invoices"),
    ("POST", "/api/external/v2/customer_invoices/create_from_quote"): ("customer_invoices", "create_customer_invoice_from_quote"),
    ("POST", "/api/external/v2/customer_invoices/e_invoices/imports"): ("customer_invoices", "create_customer_invoice_einvoice_import"),
    ("POST", "/api/external/v2/customer_invoices/import"): ("customer_invoices", "import_customer_invoices"),
    ("POST", "/api/external/v2/customer_invoices/{customer_invoice_id}/appendices"): ("customer_invoices", "post_customer_invoice_appendices"),
    ("POST", "/api/external/v2/customer_invoices/{customer_invoice_id}/matched_transactions"): ("transactions", "post_customer_invoice_matched_transactions"),
    ("POST", "/api/external/v2/customer_invoices/{id}/link_credit_note"): ("customer_invoices", "link_credit_note"),
    ("POST", "/api/external/v2/customer_invoices/{id}/send_by_email"): ("customer_invoices", "send_by_email_customer_invoice"),
    ("POST", "/api/external/v2/customer_invoices/{id}/send_to_pa"): ("customer_invoices", "send_to_pa_customer_invoice"),
    ("POST", "/api/external/v2/customers/{customer_id}/contacts"): ("customers", "post_customer_contact"),
    ("POST", "/api/external/v2/exports/analytical_general_ledgers"): ("exports", "export_analytical_general_ledger"),
    ("POST", "/api/external/v2/exports/fecs"): ("exports", "export_fec"),
    ("POST", "/api/external/v2/exports/general_ledgers"): ("exports", "export_general_ledger"),
    ("POST", "/api/external/v2/file_attachments"): ("file_attachments", "post_file_attachments"),
    ("POST", "/api/external/v2/gocardless_mandates/mail_requests"): ("mandates", "post_gocardless_mandate_mail_requests"),
    ("POST", "/api/external/v2/gocardless_mandates/{gocardless_mandate_id}/associations"): ("mandates", "post_gocardless_mandate_associations"),
    ("POST", "/api/external/v2/gocardless_mandates/{gocardless_mandate_id}/cancellations"): ("mandates", "post_gocardless_mandate_cancellations"),
    ("POST", "/api/external/v2/individual_customers"): ("customers", "post_individual_customer"),
    ("POST", "/api/external/v2/journals"): ("journals", "post_journals"),
    ("POST", "/api/external/v2/ledger_accounts"): ("ledger_accounts", "post_ledger_accounts"),
    ("POST", "/api/external/v2/ledger_attachments"): ("ledger_attachments", "post_ledger_attachments"),
    ("POST", "/api/external/v2/ledger_entries"): ("ledger_entries", "post_ledger_entries"),
    ("POST", "/api/external/v2/ledger_entry_lines/lettering"): ("ledger_entry_lines", "post_ledger_entry_lines_letter"),
    ("POST", "/api/external/v2/pro_account/mandate_migrations"): ("mandates", "post_pro_account_mandate_migrations"),
    ("POST", "/api/external/v2/pro_account/mandate_requests"): ("mandates", "post_pro_account_mandate_mail_requests"),
    ("POST", "/api/external/v2/products"): ("products", "post_products"),
    ("POST", "/api/external/v2/purchase_requests/imports"): ("purchase_requests", "create_purchase_request_import"),
    ("POST", "/api/external/v2/quotes"): ("quotes", "post_quotes"),
    ("POST", "/api/external/v2/quotes/{id}/send_by_email"): ("quotes", "send_by_email_quote"),
    ("POST", "/api/external/v2/quotes/{quote_id}/appendices"): ("quotes", "post_quote_appendices"),
    ("POST", "/api/external/v2/sepa_mandates"): ("mandates", "post_sepa_mandates"),
    ("POST", "/api/external/v2/supplier_invoices/e_invoices/imports"): ("supplier_invoices", "create_supplier_invoice_einvoice_import"),
    ("POST", "/api/external/v2/supplier_invoices/import"): ("supplier_invoices", "import_supplier_invoice"),
    ("POST", "/api/external/v2/supplier_invoices/{supplier_invoice_id}/linked_purchase_requests"): ("supplier_invoices", "post_supplier_invoice_linked_purchase_requests"),
    ("POST", "/api/external/v2/supplier_invoices/{supplier_invoice_id}/matched_transactions"): ("transactions", "post_supplier_invoice_matched_transactions"),
    ("POST", "/api/external/v2/suppliers"): ("suppliers", "post_supplier"),
    ("POST", "/api/external/v2/transactions"): ("transactions", "create_transaction"),
    ("POST", "/api/external/v2/webhook_subscriptions"): ("webhooks", "post_webhook_subscriptions"),
    ("PUT", "/api/external/v2/billing_subscriptions/{id}"): ("billing_subscriptions", "put_billing_subscriptions"),
    ("PUT", "/api/external/v2/categories/{id}"): ("categories", "update_category"),
    ("PUT", "/api/external/v2/category_groups/{id}"): ("category_groups", "put_category_group"),
    ("PUT", "/api/external/v2/commercial_documents/{id}"): ("commercial_documents", "update_commercial_document"),
    ("PUT", "/api/external/v2/company_customers/{id}"): ("customers", "put_company_customer"),
    ("PUT", "/api/external/v2/customer_invoices/{customer_invoice_id}/categories"): ("customer_invoices", "put_customer_invoice_categories"),
    ("PUT", "/api/external/v2/customer_invoices/{id}"): ("customer_invoices", "update_customer_invoice"),
    ("PUT", "/api/external/v2/customer_invoices/{id}/finalize"): ("customer_invoices", "finalize_customer_invoice"),
    ("PUT", "/api/external/v2/customer_invoices/{id}/mark_as_paid"): ("customer_invoices", "mark_as_paid_customer_invoice"),
    ("PUT", "/api/external/v2/customer_invoices/{id}/update_imported"): ("customer_invoices", "update_imported_customer_invoice"),
    ("PUT", "/api/external/v2/customers/{customer_id}/categories"): ("customers", "put_customer_categories"),
    ("PUT", "/api/external/v2/customers/{customer_id}/contacts/{id}"): ("customers", "put_customer_contact"),
    ("PUT", "/api/external/v2/individual_customers/{id}"): ("customers", "put_individual_customer"),
    ("PUT", "/api/external/v2/ledger_accounts/{id}"): ("ledger_accounts", "update_ledger_account"),
    ("PUT", "/api/external/v2/ledger_entries/{id}"): ("ledger_entries", "put_ledger_entries"),
    ("PUT", "/api/external/v2/ledger_entry_lines/{ledger_entry_line_id}/categories"): ("ledger_entry_lines", "put_ledger_entry_lines_categories"),
    ("PUT", "/api/external/v2/products/{id}"): ("products", "put_product"),
    ("PUT", "/api/external/v2/quotes/{id}"): ("quotes", "update_quote"),
    ("PUT", "/api/external/v2/quotes/{id}/update_status"): ("quotes", "update_status_quote"),
    ("PUT", "/api/external/v2/sepa_mandates/{id}"): ("mandates", "put_sepa_mandate"),
    ("PUT", "/api/external/v2/supplier_invoices/{id}"): ("supplier_invoices", "put_supplier_invoice"),
    ("PUT", "/api/external/v2/supplier_invoices/{id}/validate_accounting"): ("supplier_invoices", "validate_accounting_supplier_invoice"),
    ("PUT", "/api/external/v2/supplier_invoices/{supplier_invoice_id}/categories"): ("supplier_invoices", "put_supplier_invoice_categories"),
    ("PUT", "/api/external/v2/supplier_invoices/{supplier_invoice_id}/e_invoice_status"): ("supplier_invoices", "put_supplier_invoice_einvoice_status"),
    ("PUT", "/api/external/v2/supplier_invoices/{supplier_invoice_id}/payment_status"): ("supplier_invoices", "update_supplier_invoice_payment_status"),
    ("PUT", "/api/external/v2/suppliers/{id}"): ("suppliers", "put_supplier"),
    ("PUT", "/api/external/v2/suppliers/{supplier_id}/categories"): ("suppliers", "put_supplier_categories"),
    ("PUT", "/api/external/v2/transactions/{id}"): ("transactions", "update_transaction"),
    ("PUT", "/api/external/v2/transactions/{transaction_id}/categories"): ("transactions", "put_transaction_categories"),
    ("PUT", "/api/external/v2/webhook_subscriptions/{id}"): ("webhooks", "put_webhook_subscription"),
}
