---
title: "xtraCHEF: Bulk Delete Invoices"
source: https://intercom.help/toast-central/en/articles/14095581-xtrachef-bulk-delete-invoices
last_updated: 2026-04-22
area: admin-and-users
---

## What it is
How to delete many invoices at once from the Invoice Dashboard, filtered by location and date range. Deletion is **permanent**. All cost and line-item data from those invoices is removed, and the item catalog recalculates from the invoices that remain.

## When you'd use it
- Clearing out duplicate or test uploads, or a period that was loaded by mistake. One example is invoices that were also pushed to QBO through Shogo and shouldn't be in xtraCHEF.

## How to do it
1. In the left nav: **Invoice Automation > Invoices**.
2. Pick the **location** (skip this if there's only one).
3. Click the **calendar icon** and choose the date range. Working **one quarter at a time** keeps large deletions manageable.
4. Set rows per page to **10, 25, 50 or 100**.
5. Tick each invoice's checkbox, then click **Delete** at the top.
6. In the confirmation window, click **Yes, remove**.

## Settings, options & permissions
- The article doesn't name a role. It requires Invoice Dashboard access. Treat it as a Tenant Admin task.

## Rules, limits & gotchas
- **It can't be undone.** The only way back is to re-upload the documents.
- The catalog, price history and item data built from deleted invoices disappear, which can change recipe costs and price tracker history.
- Deleting in xtraCHEF does **not** delete bills already extracted to QBO. Clean those up in QBO separately.

## Automation / efficiency angles
- Before a bulk delete, export the invoice listing as CSV (the export is available to all roles) to keep a record of what was removed.
- Use 100 rows per page and a filter by quarter to clear duplicates quickly.
- Under CLAUDE.md policy, any delete needs Bart's explicit confirmation of the exact list first.

## Related articles
- [Invoices and Invoice Status](https://intercom.help/toast-central/en/articles/14726246-xtrachef-invoices-and-invoice-status)
- [Invoice Search](https://intercom.help/toast-central/en/articles/14726221-xtrachef-invoice-search)
- [Upload Invoices and Receipts (Desktop)](https://intercom.help/toast-central/en/articles/14232979-xtrachef-upload-invoices-and-receipts-desktop)
- [Invoice Rejections](https://intercom.help/toast-central/en/articles/14727594-xtrachef-invoice-rejections)
- [Change an Invoice Item's GL Code or Category](https://intercom.help/toast-central/en/articles/14727522-xtrachef-change-an-invoice-item-s-gl-code-or-category)
