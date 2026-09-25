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


## client.api.bank_accounts

- `get_bank_accounts()` [paginated], GET /api/external/v2/bank_accounts: List bank accounts
- `post_bank_account(body)`, POST /api/external/v2/bank_accounts: Create a bank account
- `get_bank_account(id)`, GET /api/external/v2/bank_accounts/{id}: Retrieve a bank account

## client.api.bank_establishments

- `get_bank_establishments()` [paginated], GET /api/external/v2/bank_establishments: List bank establishments

## client.api.billing_subscriptions

- `get_billing_subscriptions()` [paginated], GET /api/external/v2/billing_subscriptions: List billing subscriptions
- `post_billing_subscriptions(body)`, POST /api/external/v2/billing_subscriptions: Create a billing subscription
- `get_billing_subscription_invoice_line_sections(billing_subscription_id)` [paginated], GET /api/external/v2/billing_subscriptions/{billing_subscription_id}/invoice_line_sections: List the invoice line sections of a billing subscription
- `get_billing_subscription_invoice_lines(billing_subscription_id)` [paginated], GET /api/external/v2/billing_subscriptions/{billing_subscription_id}/invoice_lines: List invoice lines for a billing subscription
- `get_billing_subscription(id)`, GET /api/external/v2/billing_subscriptions/{id}: Get a billing subscription
- `put_billing_subscriptions(id, body)`, PUT /api/external/v2/billing_subscriptions/{id}: Update a billing subscription

## client.api.categories

- `get_categories()` [paginated], GET /api/external/v2/categories: List categories
- `post_categories(body)`, POST /api/external/v2/categories: Create a category
- `get_category(id)`, GET /api/external/v2/categories/{id}: Retrieve a category
- `update_category(id, body)`, PUT /api/external/v2/categories/{id}: Update a category
- `get_category_groups()` [paginated], GET /api/external/v2/category_groups: List category groups

## client.api.category_groups

- `post_category_groups(body)`, POST /api/external/v2/category_groups: Create a category group
- `get_category_group_categories(category_group_id)` [paginated], GET /api/external/v2/category_groups/{category_group_id}/categories: List categories of a category group
- `get_category_group(id)`, GET /api/external/v2/category_groups/{id}: Retrieve a category group
- `put_category_group(id, body)`, PUT /api/external/v2/category_groups/{id}: Update a category group

## client.api.changelogs

- `get_customer_invoices_changes()` [paginated], GET /api/external/v2/changelogs/customer_invoices: Get customer invoices changes events
- `get_customer_changes()` [paginated], GET /api/external/v2/changelogs/customers: Get customer changes events
- `get_ledger_entries_category_changes()` [paginated], GET /api/external/v2/changelogs/ledger_entries_categories: Get ledger entry category change events
- `get_ledger_entry_line_changes()` [paginated], GET /api/external/v2/changelogs/ledger_entry_lines: Get ledger entry line change events
- `get_ledger_entry_lines_category_changes()` [paginated], GET /api/external/v2/changelogs/ledger_entry_lines_categories: Get ledger entry line category change events
- `get_product_changes()` [paginated], GET /api/external/v2/changelogs/products: Get product change events
- `get_supplier_invoices_changes()` [paginated], GET /api/external/v2/changelogs/supplier_invoices: Get supplier invoices changes events
- `get_supplier_changes()` [paginated], GET /api/external/v2/changelogs/suppliers: Get supplier changes events
- `get_transaction_changes()` [paginated], GET /api/external/v2/changelogs/transactions: Get transaction change events

## client.api.commercial_documents

- `list_commercial_documents()` [paginated], GET /api/external/v2/commercial_documents: List commercial documents
- `post_commercial_documents(body)`, POST /api/external/v2/commercial_documents: Create a commercial document
- `get_commercial_document_appendices(commercial_document_id)` [paginated], GET /api/external/v2/commercial_documents/{commercial_document_id}/appendices: List appendices of a commercial document
- `post_commercial_document_appendices(commercial_document_id, files)`, POST /api/external/v2/commercial_documents/{commercial_document_id}/appendices: Upload an appendix for a commercial document
- `get_commercial_document_invoice_line_sections(commercial_document_id)` [paginated], GET /api/external/v2/commercial_documents/{commercial_document_id}/invoice_line_sections: List invoice line sections for a commercial document
- `get_commercial_document_invoice_lines(commercial_document_id)` [paginated], GET /api/external/v2/commercial_documents/{commercial_document_id}/invoice_lines: List invoice lines for a commercial document
- `get_commercial_document(id)`, GET /api/external/v2/commercial_documents/{id}: Retrieve a commercial document
- `update_commercial_document(id, body)`, PUT /api/external/v2/commercial_documents/{id}: Update a commercial document

## client.api.customer_invoice_templates

- `get_customer_invoice_templates()` [paginated], GET /api/external/v2/customer_invoice_templates: List customer invoice templates

## client.api.customer_invoices

- `get_customer_invoices()` [paginated], GET /api/external/v2/customer_invoices: List customer invoices
- `post_customer_invoices(body)`, POST /api/external/v2/customer_invoices: Create a customer invoice
- `create_customer_invoice_from_quote(body)`, POST /api/external/v2/customer_invoices/create_from_quote: Create a customer invoice from a quote
- `create_customer_invoice_einvoice_import(files)`, POST /api/external/v2/customer_invoices/e_invoices/imports: Import a customer e-invoice
- `import_customer_invoices(body)`, POST /api/external/v2/customer_invoices/import: Import an invoice with file attached
- `get_customer_invoice_appendices(customer_invoice_id)` [paginated], GET /api/external/v2/customer_invoices/{customer_invoice_id}/appendices: List appendices of a customer invoice
- `post_customer_invoice_appendices(customer_invoice_id, files)`, POST /api/external/v2/customer_invoices/{customer_invoice_id}/appendices: Upload an appendix for a customer invoice
- `get_customer_invoice_categories(customer_invoice_id)` [paginated], GET /api/external/v2/customer_invoices/{customer_invoice_id}/categories: List categories of a customer invoice
- `put_customer_invoice_categories(customer_invoice_id, body)`, PUT /api/external/v2/customer_invoices/{customer_invoice_id}/categories: Categorize a customer invoice
- `get_customer_invoice_custom_header_fields(customer_invoice_id)` [paginated], GET /api/external/v2/customer_invoices/{customer_invoice_id}/custom_header_fields: List custom header fields for a customer invoice
- `get_customer_invoice_invoice_line_sections(customer_invoice_id)` [paginated], GET /api/external/v2/customer_invoices/{customer_invoice_id}/invoice_line_sections: List invoice line sections for a customer invoice
- `get_customer_invoice_invoice_lines(customer_invoice_id)` [paginated], GET /api/external/v2/customer_invoices/{customer_invoice_id}/invoice_lines: List invoice lines for a customer invoice
- `get_customer_invoice_matched_transactions(customer_invoice_id)` [paginated], GET /api/external/v2/customer_invoices/{customer_invoice_id}/matched_transactions: List matched transactions for a customer invoice
- `get_customer_invoice_payments(customer_invoice_id)` [paginated], GET /api/external/v2/customer_invoices/{customer_invoice_id}/payments: List payments for a customer invoice
- `delete_customer_invoices(id)`, DELETE /api/external/v2/customer_invoices/{id}: Delete draft invoice
- `get_customer_invoice(id)`, GET /api/external/v2/customer_invoices/{id}: Retrieve a customer invoice
- `update_customer_invoice(id, body)`, PUT /api/external/v2/customer_invoices/{id}: Update a customer invoice
- `finalize_customer_invoice(id)`, PUT /api/external/v2/customer_invoices/{id}/finalize: Turn the draft invoice into a finalized invoice.
- `link_credit_note(id, body)`, POST /api/external/v2/customer_invoices/{id}/link_credit_note: Link a credit note to a customer invoice
- `mark_as_paid_customer_invoice(id)`, PUT /api/external/v2/customer_invoices/{id}/mark_as_paid: Mark a customer invoice as paid
- `send_by_email_customer_invoice(id, body)`, POST /api/external/v2/customer_invoices/{id}/send_by_email: Send a customer invoice by email
- `send_to_pa_customer_invoice(id)`, POST /api/external/v2/customer_invoices/{id}/send_to_pa: Send a customer e-invoice to PA
- `update_imported_customer_invoice(id, body)`, PUT /api/external/v2/customer_invoices/{id}/update_imported: Update an Imported customer invoice

## client.api.customers

- `post_company_customer(body)`, POST /api/external/v2/company_customers: Create a company customer
- `get_company_customer(id)`, GET /api/external/v2/company_customers/{id}: Retrieve a company customer
- `put_company_customer(id, body)`, PUT /api/external/v2/company_customers/{id}: Update a company customer
- `get_customers()` [paginated], GET /api/external/v2/customers: List customers (company and individual)
- `get_customer_categories(customer_id)` [paginated], GET /api/external/v2/customers/{customer_id}/categories: List categories of a customer
- `put_customer_categories(customer_id, body)`, PUT /api/external/v2/customers/{customer_id}/categories: Categorize a customer
- `get_customer_contacts(customer_id)` [paginated], GET /api/external/v2/customers/{customer_id}/contacts: List contacts of a customer
- `post_customer_contact(customer_id, body)`, POST /api/external/v2/customers/{customer_id}/contacts: Create a contact of a customer
- `delete_customer_contact(customer_id, id)`, DELETE /api/external/v2/customers/{customer_id}/contacts/{id}: Delete a contact of a customer
- `get_customer_contact(customer_id, id)`, GET /api/external/v2/customers/{customer_id}/contacts/{id}: Retrieve a contact of a customer
- `put_customer_contact(customer_id, id, body)`, PUT /api/external/v2/customers/{customer_id}/contacts/{id}: Update a contact of a customer
- `get_customer(id)`, GET /api/external/v2/customers/{id}: Retrieve a customer
- `post_individual_customer(body)`, POST /api/external/v2/individual_customers: Create an individual customer
- `get_individual_customer(id)`, GET /api/external/v2/individual_customers/{id}: Retrieve an individual customer
- `put_individual_customer(id, body)`, PUT /api/external/v2/individual_customers/{id}: Update an individual customer

## client.api.exports

- `export_analytical_general_ledger(body)`, POST /api/external/v2/exports/analytical_general_ledgers: Create an Analytical General Ledger export
- `get_analytical_general_ledger_export(id)`, GET /api/external/v2/exports/analytical_general_ledgers/{id}: Retrieve an Analytical General Ledger export
- `export_fec(body)`, POST /api/external/v2/exports/fecs: Create a FEC export
- `get_fec_export(id)`, GET /api/external/v2/exports/fecs/{id}: Retrieve a FEC export
- `export_general_ledger(body)`, POST /api/external/v2/exports/general_ledgers: Create a General Ledger export
- `get_general_ledger_export(id)`, GET /api/external/v2/exports/general_ledgers/{id}: Retrieve a General Ledger export

## client.api.file_attachments

- `post_file_attachments(files)`, POST /api/external/v2/file_attachments: Upload a file

## client.api.fiscal_years

- `company_fiscal_years()` [paginated], GET /api/external/v2/fiscal_years: List Company's Fiscal Years

## client.api.journals

- `get_journals()` [paginated], GET /api/external/v2/journals: List journals
- `post_journals(body)`, POST /api/external/v2/journals: Create a journal
- `get_journal(id)`, GET /api/external/v2/journals/{id}: Retrieve a journal

## client.api.ledger_accounts

- `get_ledger_accounts()` [paginated], GET /api/external/v2/ledger_accounts: List Ledger Accounts
- `post_ledger_accounts(body)`, POST /api/external/v2/ledger_accounts: Create a ledger account
- `get_ledger_account(id)`, GET /api/external/v2/ledger_accounts/{id}: Get a ledger account
- `update_ledger_account(id, body)`, PUT /api/external/v2/ledger_accounts/{id}: Update a ledger account

## client.api.ledger_attachments

- `post_ledger_attachments(files)`, POST /api/external/v2/ledger_attachments: Upload a file

## client.api.ledger_entries

- `get_ledger_entries()` [paginated], GET /api/external/v2/ledger_entries: List Ledger Entries
- `post_ledger_entries(body)`, POST /api/external/v2/ledger_entries: Create a ledger entry
- `get_ledger_entry(id)`, GET /api/external/v2/ledger_entries/{id}: Retrieve a Ledger entry
- `put_ledger_entries(id, body)`, PUT /api/external/v2/ledger_entries/{id}: Update a ledger entry
- `get_ledger_entries_ledger_entry_lines(ledger_entry_id)` [paginated], GET /api/external/v2/ledger_entries/{ledger_entry_id}/ledger_entry_lines: List ledger entry lines of a Ledger Entry

## client.api.ledger_entry_lines

- `get_ledger_entry_lines()` [paginated], GET /api/external/v2/ledger_entry_lines: List ledger entry lines
- `delete_ledger_entry_lines_unletter(body)`, DELETE /api/external/v2/ledger_entry_lines/lettering: Unletter ledger entry lines
- `post_ledger_entry_lines_letter(body)`, POST /api/external/v2/ledger_entry_lines/lettering: Letter ledger entry lines
- `get_ledger_entry_line(id)`, GET /api/external/v2/ledger_entry_lines/{id}: Retrieve a Ledger entry line
- `get_ledger_entry_lines_categories(ledger_entry_line_id)` [paginated], GET /api/external/v2/ledger_entry_lines/{ledger_entry_line_id}/categories: List categories of a Ledger Entry line
- `put_ledger_entry_lines_categories(ledger_entry_line_id, body)`, PUT /api/external/v2/ledger_entry_lines/{ledger_entry_line_id}/categories: Link Analytical Categories to a Ledger Entry line
- `get_ledger_entry_lines_lettered_ledger_entry_lines(ledger_entry_line_id)` [paginated], GET /api/external/v2/ledger_entry_lines/{ledger_entry_line_id}/lettered_ledger_entry_lines: List ledger entry lines lettered to a given ledger entry line

## client.api.mandates

- `get_gocardless_mandates()` [paginated], GET /api/external/v2/gocardless_mandates: List gocardless mandates
- `post_gocardless_mandate_mail_requests(body)`, POST /api/external/v2/gocardless_mandates/mail_requests: Send a GoCardless mandate email request
- `post_gocardless_mandate_associations(gocardless_mandate_id, body)`, POST /api/external/v2/gocardless_mandates/{gocardless_mandate_id}/associations: Associate a GoCardless mandate to a customer
- `post_gocardless_mandate_cancellations(gocardless_mandate_id)`, POST /api/external/v2/gocardless_mandates/{gocardless_mandate_id}/cancellations: Cancel a Gocardless mandate
- `get_gocardless_mandate(id)`, GET /api/external/v2/gocardless_mandates/{id}: Get a Gocardless mandate
- `get_pro_account_mandate_migrations()` [paginated], GET /api/external/v2/pro_account/mandate_migrations: List mandate migration candidates
- `post_pro_account_mandate_migrations(body)`, POST /api/external/v2/pro_account/mandate_migrations: Migrate a mandate to Pro Account
- `post_pro_account_mandate_mail_requests(body)`, POST /api/external/v2/pro_account/mandate_requests: Send a Pro Account SEPA mandate request
- `get_pro_account_mandates()` [paginated], GET /api/external/v2/pro_account/mandates: List Pro Account payment mandates
- `get_sepa_mandates()` [paginated], GET /api/external/v2/sepa_mandates: List SEPA mandates
- `post_sepa_mandates(body)`, POST /api/external/v2/sepa_mandates: Create a SEPA mandate
- `delete_sepa_mandate(id)`, DELETE /api/external/v2/sepa_mandates/{id}: Delete a SEPA mandate
- `get_sepa_mandate(id)`, GET /api/external/v2/sepa_mandates/{id}: Get a SEPA mandate
- `put_sepa_mandate(id, body)`, PUT /api/external/v2/sepa_mandates/{id}: Update a SEPA mandate

## client.api.numberings

- `get_numberings()` [paginated], GET /api/external/v2/numberings: List document numberings

## client.api.pa_registrations

- `get_pa_registrations()`, GET /api/external/v2/pa_registrations: List PA Registrations

## client.api.products

- `get_products()` [paginated], GET /api/external/v2/products: List products
- `post_products(body)`, POST /api/external/v2/products: Create a product
- `get_product(id)`, GET /api/external/v2/products/{id}: Retrieve a product
- `put_product(id, body)`, PUT /api/external/v2/products/{id}: Update a product

## client.api.purchase_requests

- `get_purchase_requests()` [paginated], GET /api/external/v2/purchase_requests: List purchase requests
- `create_purchase_request_import(body)`, POST /api/external/v2/purchase_requests/imports: Import a purchase order.
- `get_purchase_request(id)`, GET /api/external/v2/purchase_requests/{id}: Retrieve a purchase request

## client.api.quotes

- `get_quote_changes()` [paginated], GET /api/external/v2/changelogs/quotes: Get quotes changes events
- `list_quotes()` [paginated], GET /api/external/v2/quotes: List quotes
- `post_quotes(body)`, POST /api/external/v2/quotes: Create a quote
- `get_quote(id)`, GET /api/external/v2/quotes/{id}: Retrieve a quote
- `update_quote(id, body)`, PUT /api/external/v2/quotes/{id}: Update a quote
- `send_by_email_quote(id, body)`, POST /api/external/v2/quotes/{id}/send_by_email: Send a quote by email
- `update_status_quote(id, body)`, PUT /api/external/v2/quotes/{id}/update_status: Update status of a quote
- `get_quote_appendices(quote_id)` [paginated], GET /api/external/v2/quotes/{quote_id}/appendices: List appendices of a quote
- `post_quote_appendices(quote_id, files)`, POST /api/external/v2/quotes/{quote_id}/appendices: Upload an appendix for a quote
- `get_quote_invoice_line_sections(quote_id)` [paginated], GET /api/external/v2/quotes/{quote_id}/invoice_line_sections: List invoice line sections for a quote
- `get_quote_invoice_lines(quote_id)` [paginated], GET /api/external/v2/quotes/{quote_id}/invoice_lines: List invoice lines for a quote

## client.api.supplier_invoices

- `get_supplier_invoices()` [paginated], GET /api/external/v2/supplier_invoices: List supplier invoices
- `create_supplier_invoice_einvoice_import(files)`, POST /api/external/v2/supplier_invoices/e_invoices/imports: Import a supplier e-invoice
- `import_supplier_invoice(body)`, POST /api/external/v2/supplier_invoices/import: Import a supplier invoice with a file attached
- `get_supplier_invoice(id)`, GET /api/external/v2/supplier_invoices/{id}: Retrieve a supplier invoice
- `put_supplier_invoice(id, body)`, PUT /api/external/v2/supplier_invoices/{id}: Update a supplier invoice
- `validate_accounting_supplier_invoice(id)`, PUT /api/external/v2/supplier_invoices/{id}/validate_accounting: Validate the accounting of a supplier invoice
- `get_supplier_invoice_categories(supplier_invoice_id)` [paginated], GET /api/external/v2/supplier_invoices/{supplier_invoice_id}/categories: List categories of a supplier invoice
- `put_supplier_invoice_categories(supplier_invoice_id, body)`, PUT /api/external/v2/supplier_invoices/{supplier_invoice_id}/categories: Categorize a supplier invoice
- `put_supplier_invoice_einvoice_status(supplier_invoice_id, body)`, PUT /api/external/v2/supplier_invoices/{supplier_invoice_id}/e_invoice_status: Update e-invoice status for a supplier invoice
- `get_supplier_invoice_lines(supplier_invoice_id)` [paginated], GET /api/external/v2/supplier_invoices/{supplier_invoice_id}/invoice_lines: List invoice lines for a supplier invoice
- `post_supplier_invoice_linked_purchase_requests(supplier_invoice_id, body)`, POST /api/external/v2/supplier_invoices/{supplier_invoice_id}/linked_purchase_requests: Link a purchase request to a supplier invoice
- `get_supplier_invoice_matched_transactions(supplier_invoice_id)` [paginated], GET /api/external/v2/supplier_invoices/{supplier_invoice_id}/matched_transactions: List matched transactions for a supplier invoice
- `update_supplier_invoice_payment_status(supplier_invoice_id, body)`, PUT /api/external/v2/supplier_invoices/{supplier_invoice_id}/payment_status: Update a supplier invoice payment status
- `get_supplier_invoice_payments(supplier_invoice_id)` [paginated], GET /api/external/v2/supplier_invoices/{supplier_invoice_id}/payments: List payments for a supplier invoice

## client.api.suppliers

- `get_suppliers()` [paginated], GET /api/external/v2/suppliers: List suppliers
- `post_supplier(body)`, POST /api/external/v2/suppliers: Create a Supplier
- `get_supplier(id)`, GET /api/external/v2/suppliers/{id}: Retrieve a supplier
- `put_supplier(id, body)`, PUT /api/external/v2/suppliers/{id}: Update a supplier
- `get_supplier_categories(supplier_id)` [paginated], GET /api/external/v2/suppliers/{supplier_id}/categories: List categories of a supplier
- `put_supplier_categories(supplier_id, body)`, PUT /api/external/v2/suppliers/{supplier_id}/categories: Categorize a supplier

## client.api.transactions

- `post_customer_invoice_matched_transactions(customer_invoice_id, body)`, POST /api/external/v2/customer_invoices/{customer_invoice_id}/matched_transactions: Match a transaction to a customer invoice
- `delete_customer_invoice_matched_transactions(customer_invoice_id, id)`, DELETE /api/external/v2/customer_invoices/{customer_invoice_id}/matched_transactions/{id}: Unmatch a transaction to a customer invoice
- `post_supplier_invoice_matched_transactions(supplier_invoice_id, body)`, POST /api/external/v2/supplier_invoices/{supplier_invoice_id}/matched_transactions: Match a transaction to a supplier invoice
- `delete_supplier_invoice_matched_transactions(supplier_invoice_id, id)`, DELETE /api/external/v2/supplier_invoices/{supplier_invoice_id}/matched_transactions/{id}: Unmatch a transaction to a supplier invoice
- `get_transactions()` [paginated], GET /api/external/v2/transactions: List transactions
- `create_transaction(body)`, POST /api/external/v2/transactions: Create a transaction
- `get_transaction(id)`, GET /api/external/v2/transactions/{id}: Retrieve a transaction
- `update_transaction(id, body)`, PUT /api/external/v2/transactions/{id}: Update a transaction
- `get_transaction_categories(transaction_id)` [paginated], GET /api/external/v2/transactions/{transaction_id}/categories: List categories of a bank transaction
- `put_transaction_categories(transaction_id, body)`, PUT /api/external/v2/transactions/{transaction_id}/categories: Categorize a bank transaction
- `get_transaction_matched_invoices(transaction_id)` [paginated], GET /api/external/v2/transactions/{transaction_id}/matched_invoices: List invoices matched to a bank transaction

## client.api.trial_balance

- `get_trial_balance(period_start=..., period_end=...)` [paginated], GET /api/external/v2/trial_balance: Get the trial balance

## client.api.users

- `get_me()`, GET /api/external/v2/me: User Profile

## client.api.webhooks

- `get_webhook_subscriptions()` [paginated], GET /api/external/v2/webhook_subscriptions: List webhook subscriptions
- `post_webhook_subscriptions(body)`, POST /api/external/v2/webhook_subscriptions: Create a webhook subscription
- `delete_webhook_subscription(id)`, DELETE /api/external/v2/webhook_subscriptions/{id}: Delete a webhook subscription
- `get_webhook_subscription(id)`, GET /api/external/v2/webhook_subscriptions/{id}: Get a webhook subscription
- `put_webhook_subscription(id, body)`, PUT /api/external/v2/webhook_subscriptions/{id}: Update a webhook subscription
