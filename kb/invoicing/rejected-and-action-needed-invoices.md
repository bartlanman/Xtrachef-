---
title: "xtraCHEF: Rejected and Action Needed Invoices"
source: https://intercom.help/toast-central/en/articles/14727567-xtrachef-rejected-and-action-needed-invoices
last_updated: 2026-04-22
area: invoicing
---

## What it is
This is an overview of the two early-stage blockers in reconciliation. **Rejection** means the document was refused and has to be re-uploaded; it can't be fixed in place. **Action Needed** means the document is paused until you supply missing information, and it can be fixed in place. Nothing is extracted to accounting or analytics from a document in either state.

## When you'd use it
- When you're first learning the reconciliation flow, or training staff on it.
- When you need to decide whether to re-upload or edit.

## How to do it
**Rejections**
- Review them on the **Dashboard** invoices status breakdown (check the date range) or on **Invoices > Rejected** with a custom date range.
- Reasons: Duplicate Invoice (same ID and date, the most common), Bad Image Quality (blurry, cropped, missing info, or low light), Non-Invoice Image, Missing Invoice Data, Missing Vendor Name, Batch Contains Multiple Invoices, Zero Dollar Invoice.
- Options: **Do Nothing**, **Re-upload** (fix the problem and capture again), or **Reprocess** (ask support when the rejection was wrong).

**Action Needed**
- Review them on the **Dashboard** in the **Info missing** tab of the status breakdown, or on **Invoices > Action needed** with a custom date range.
- Reasons:
  - **Missing vendor code**: an accounting extract is on and the vendor has no accounting display name.
  - **Missing invoice date**: needed for cataloging.
  - **Missing invoice number**: needed for cataloging and as the duplicate guard.
  - **Review header and line detail**: no header total was captured, so you have to verify the read.
  - **Invoice or line totals don't match**: the lines don't add up to the total.
  - **Payment method mandatory**: QBO extract with payment method processing on, receipts booked as expenses.
  - **Invoice from unregistered user**: verify it. Accepting registers the sender as an Invoice Capture user.
- Fix by adding the missing data. Most of these can now be reprocessed in the mobile app.

**Next step**: after rejections and Action Needed items are cleared, invoices with new items go to **Map Invoice Items** to assign a category and GL code. Mapping is required for the accounting extract and for Analytics and Reports.

## Settings, options & permissions
- No roles are specified.

## Rules, limits & gotchas
- Rejections can't be edited. Only re-upload, or ask support to reprocess.
- Always check the dashboard date range. Old problems can be hidden outside it.
- New vendors are the main source of Action Needed items.

## Automation / efficiency angles
- Before activating a new vendor, set its vendor code, decide on auto-assign invoice IDs, and map its items on the first invoice. That way the second invoice flows through without touch.
- Weekly KPI: rejected (unarchived) count plus Action Needed count, with a target of 0 before the weekly AP run.

## Related articles
- [Action Needed Invoices](https://intercom.help/toast-central/en/articles/14727783-xtrachef-action-needed-invoices)
- [Invoice Rejections](https://intercom.help/toast-central/en/articles/14727594-xtrachef-invoice-rejections)
- [Map Invoice Items](https://intercom.help/toast-central/en/articles/14727558-xtrachef-map-invoice-items)
- [Invoices and Invoice Status](https://intercom.help/toast-central/en/articles/14726246-xtrachef-invoices-and-invoice-status)
- [Upload Invoices and Receipts (Desktop)](https://intercom.help/toast-central/en/articles/14232979-xtrachef-upload-invoices-and-receipts-desktop)
- [Upload Invoices and Receipts on Mobile](https://intercom.help/toast-central/en/articles/14727675-xtrachef-upload-invoices-and-receipts-on-mobile)
