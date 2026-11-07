---
title: "xtraCHEF: Assign Invoice Date as Invoice ID"
source: https://intercom.help/toast-central/en/articles/14726301-xtrachef-assign-invoice-date-as-invoice-id
last_updated: 2026-04-22
area: invoicing
---

## What it is
Some vendors never print an invoice number, so their uploads keep landing in Action Needed ("Missing invoice number"). A per-vendor checkbox tells xtraCHEF to auto-generate the invoice ID from the **invoice date**, so you don't need a support ticket.

## When you'd use it
- Farmers, small local suppliers, hardware or big-box receipts, and any vendor whose documents have no number.

## How to do it
1. In the left nav rail, click **Vendors**.
2. Open the vendor.
3. Go to the **Configuration** tab.
4. Check **Auto assign unique Invoice ID**.
5. Save. From then on, invoices from this vendor use the invoice date as the invoice ID.

## Settings, options & permissions
- This is a per-vendor setting in the Vendor Hub's **Configuration** tab. No roles are stated.
- This is the same idea as the "Always auto-assign invoice numbers for this vendor" option offered from an Action Needed invoice.

## Rules, limits & gotchas
- It only applies to invoices uploaded **after** you check the box. Earlier invoices aren't changed. To reprocess past ones, contact Customer Care.
- *Inference:* because the duplicate check is invoice ID plus date, two genuine invoices from the same vendor on the same day could collide and be rejected as duplicates. Watch for this with vendors who deliver more than once a day.

## Automation / efficiency angles
- When onboarding a vendor, decide right away whether it needs auto-assigned IDs. This prevents a permanent stream of exceptions.
- Review the Action Needed list for repeat "Missing invoice number" vendors once a month and turn this on for them.

## Related articles
- [Action Needed Invoices](https://intercom.help/toast-central/en/articles/14727783-xtrachef-action-needed-invoices)
- [Invoice Search](https://intercom.help/toast-central/en/articles/14726221-xtrachef-invoice-search)
- [Invoices and Invoice Status](https://intercom.help/toast-central/en/articles/14726246-xtrachef-invoices-and-invoice-status)
- [Map Invoice Items](https://intercom.help/toast-central/en/articles/14727558-xtrachef-map-invoice-items)
- [Rejected and Action Needed Invoices](https://intercom.help/toast-central/en/articles/14727567-xtrachef-rejected-and-action-needed-invoices)
- [Invoice Rejections](https://intercom.help/toast-central/en/articles/14727594-xtrachef-invoice-rejections)
