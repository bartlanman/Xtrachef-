---
title: "xtraCHEF: Invoice Search"
source: https://intercom.help/toast-central/en/articles/14726221-xtrachef-invoice-search
last_updated: 2026-04-28
area: invoicing
---

## What it is
There are two ways to find processed invoices. The **Search Invoices** page has structured basic and advanced filters. The **Invoices** page search bar takes natural-language (LLM) queries. Documents are searchable after processing, which usually takes about 24 hours.

## When you'd use it
- Matching vendor statements, answering vendor disputes, and pulling an invoice for a price check.
- Finding all invoices that carry freight charges or discounts, or that hit a specific GL code.

## How to do it
**Structured search**
1. Click **Search Invoices** in the sidebar.
2. **Basic search** (the default): vendor name, invoice number, invoice date, invoice status, location.
3. Click **Advanced Search** for more filters: **GL codes**, **discounts**, **freight charges**, and others.
4. Click **Search**.
5. Results show Invoice Date, Invoice Amount, and Location, plus reconciliation information (Invoice Status, Extract, and more). You can open the original scan.

**Natural-language search**
1. Go to **Invoices** and type in the search bar. For example, "invoices from XYZ vendor for the last 60 days" or "all invoices for XYZ location under $250".

## Settings, options & permissions
- No roles or limits are stated.
- For vendors without invoice numbers, use the per-vendor setting to auto-assign the invoice date as the ID, which keeps search and duplicate detection working.

## Rules, limits & gotchas
- Invoices still in processing (under about 24 hours) may not show up yet.

## Automation / efficiency angles
- Monthly freight and discount audit: Advanced Search for freight charges by vendor, to spot rising delivery fees and negotiate minimums.
- Use the GL code filter to explain a P&L line in QBO. Pull every invoice behind a GL total.
- Natural-language search is the fastest way for an agent to answer "show me X." Phrase queries with vendor, location, date window, and amount.

## Related articles
- [Invoices and Invoice Status](https://intercom.help/toast-central/en/articles/14726246-xtrachef-invoices-and-invoice-status)
- [Assign Invoice Date as Invoice ID](https://intercom.help/toast-central/en/articles/14726301-xtrachef-assign-invoice-date-as-invoice-id)
- [Change an Invoice Item's GL Code or Category](https://intercom.help/toast-central/en/articles/14727522-xtrachef-change-an-invoice-item-s-gl-code-or-category)
- [Map Invoice Items](https://intercom.help/toast-central/en/articles/14727558-xtrachef-map-invoice-items)
- [Invoice Rejections](https://intercom.help/toast-central/en/articles/14727594-xtrachef-invoice-rejections)
- [Upload Invoices and Receipts (Desktop)](https://intercom.help/toast-central/en/articles/14232979-xtrachef-upload-invoices-and-receipts-desktop)
