---
title: "xtraCHEF: Edit Invoice Line Items"
source: https://intercom.help/toast-central/en/articles/9333507-xtrachef-edit-invoice-line-items
last_updated: 2026-09-08
area: invoicing
---

## What it is
xtraCHEF's AI pulls the vendor, invoice number and date, line items (description, quantity, unit price), totals, and other details from each document. Sometimes it misreads them because of cropping, smudges, handwritten adjustments, or partly illegible scans. This article covers fixing the header fields and line items so the invoice balances and reprocesses.

## When you'd use it
- For invoices in **Action needed** with **Info Missing** statuses, especially an **imbalanced invoice**.
- When a driver's handwritten short or credit isn't reflected in the lines.

## How to do it
1. Go to **Invoices > Action needed**.
2. Optional: filter with the **Statuses** drop-down. Info Missing statuses usually mean line edits are needed.
3. Open the invoice. The required action is shown at the top.
4. In **Invoice Details**, fix header fields: invoice amount, date, document type, invoice number, and so on. A **red asterisk** marks required fields.
5. On the left, scroll to **Line Item Details**. Click the **edit pencil** to change a line, or **+ Add invoice item** to add one.
6. When the amount balances and all required fields are filled, **Submit Changes** becomes active. Click it to reprocess.

**Balancing an exception**
- A red-outlined **Imbalanced Invoice** tile appears at the top when the invoice doesn't balance.
- The rule is **Invoiced Amount = Item Subtotal + Other Charges**.
- Look at the line items first, since they're the most likely culprit. Then look at the **Other Charges (Freight, Sales Tax, Discounts, Other)** tile, where **+ Add charge** adds a charge.
- Edit the top **Invoiced Amount** field **last**, and only if nothing else fixes it.
- If xtraCHEF badly misread the invoice, email **support@xtrachef.com** to have Customer Care reprocess it.

## Settings, options & permissions
- No roles are stated. Required fields have to be filled before you can submit.

## Rules, limits & gotchas
- **Warning:** hand-editing lines on a processing invoice can create unbalanced or inaccurate bills. Confirm the totals before you submit.
- Don't "plug" the difference by changing the invoiced amount. That hides missing lines and corrupts item prices.
- A missing page usually means you should reject and re-upload rather than edit.

## Automation / efficiency angles
- Freight, fuel surcharges, deposits, and tax belong in **Other Charges**, not as fake items. Keg deposits are an example. This keeps item unit costs clean.
- For chronic misreads from one vendor (bad scans, dot-matrix invoices), switch that vendor to email or PDF delivery instead of correcting every invoice.
- Send heavy misreads to support for reprocessing instead of spending staff time on them.

## Related articles
- [Action Needed Invoices](https://intercom.help/toast-central/en/articles/14727783-xtrachef-action-needed-invoices)
- [Map Invoice Items](https://intercom.help/toast-central/en/articles/14727558-xtrachef-map-invoice-items)
- [Change an Invoice Item's GL Code or Category](https://intercom.help/toast-central/en/articles/14727522-xtrachef-change-an-invoice-item-s-gl-code-or-category)
- [Invoice Rejections](https://intercom.help/toast-central/en/articles/14727594-xtrachef-invoice-rejections)
- [Upload Invoices and Receipts (Desktop)](https://intercom.help/toast-central/en/articles/14232979-xtrachef-upload-invoices-and-receipts-desktop)
- Invoice Exceptions: https://support.toasttab.com/en/article/xtraCHEF-Invoice-Exceptions
