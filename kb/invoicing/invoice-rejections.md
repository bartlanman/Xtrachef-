---
title: "xtraCHEF: Invoice Rejections"
source: https://intercom.help/toast-central/en/articles/14727594-xtrachef-invoice-rejections
last_updated: 2026-04-22
area: invoicing
---

## What it is
xtraCHEF rejects documents it can't or shouldn't process: duplicates, illegible scans, non-invoices, documents with missing data, and so on. **Rejected invoices are deleted from the system**. Nothing gets processed until you re-upload. Every rejection carries a reason code that tells you what to do next.

## When you'd use it
- Daily, check for new rejections so no vendor bill gets lost.
- When an expected invoice never shows up in QuickBooks Online.

## How to do it
**Where to see rejections**
1. Dashboard **Invoices** task tile, **Rejected** section. You get alerted to recent rejections here.
2. **Invoices > Rejected**: the reason appears in the **Status** column.
3. **Reconciliation** page: the **Rejections** column.

**Rejection reasons**
- **Duplicate Invoice**: the same invoice ID and date were already processed. This is the most common reason.
- **Bad Image Quality**: the document can't be read.
- **Non-Invoice Image**: the document isn't an invoice or receipt.
- **Missing Invoice Data**: line items or totals are missing.
- **Missing Vendor Name**: there's no vendor on the document.
- **Batch Contains Multiple Invoices**: several invoices were uploaded as one file.
- **Zero Dollar Invoice**: the document has no cost.
- **Bad Server Request**: an outage happened during processing. Re-upload, and contact support if it repeats.

**What to do with each one**
- **Nothing**: the rejection was correct (for example, a true duplicate). **Archive** it so the dashboard count stays accurate.
- **Reupload**: re-capture and upload the invoice correctly, then archive the rejection.
- **Reprocess**: the rejection was wrong. Upload again, then archive.

**Mobile**
1. Tap the home-screen **Tasks** tile. It includes rejected invoices, grouped when they're similar.
2. For **Poor image quality**: tap the invoice, optionally view the **Uploaded file** tab, tap **Re-upload invoice**, fill the frame with the page, use **+ Add page** for multi-page invoices, then tap **Submit**.
3. Some tasks, such as "Info missing: unbalanced invoice", have to be done on desktop.

## Settings, options & permissions
- No specific roles are listed.

## Rules, limits & gotchas
- Rejected documents are deleted, so if you ignore one, that bill never reaches costing or QBO.
- Duplicates are matched on **invoice ID + date**. Two genuinely different invoices with the same number and date (common with auto-numbered receipts) can be falsely rejected.
- Uploading a batch PDF holding several invoices gets rejected. Split them first.
- To prevent rejections, make sure the vendor name, every line item and dollar amount, and the final total are all legible.

## Automation / efficiency angles
- Archive rejections every week so the rejected count only shows open problems.
- Split multi-invoice PDFs (for example, vendor statement bundles) before you email or upload them.
- Look at the reasons over time. Repeated Bad Image Quality points to a receiving-dock training issue. Repeated Duplicate means a vendor is emailing twice or invoices are being uploaded both by email and by phone.
- Agent check: a vendor whose invoice was rejected this week and that has no matching processed invoice means a bill may be missing from QBO.

## Related articles
- [Action Needed Invoices](https://intercom.help/toast-central/en/articles/14727783-xtrachef-action-needed-invoices)
- [Rejected and Action Needed Invoices](https://intercom.help/toast-central/en/articles/14727567-xtrachef-rejected-and-action-needed-invoices)
- [Upload Invoices and Receipts (Desktop)](https://intercom.help/toast-central/en/articles/14232979-xtrachef-upload-invoices-and-receipts-desktop)
- [Upload Invoices and Receipts on Mobile](https://intercom.help/toast-central/en/articles/14727675-xtrachef-upload-invoices-and-receipts-on-mobile)
- [Invoices and Invoice Status](https://intercom.help/toast-central/en/articles/14726246-xtrachef-invoices-and-invoice-status)
