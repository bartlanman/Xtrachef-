---
title: "xtraCHEF: Invoices and Invoice Status"
source: https://intercom.help/toast-central/en/articles/14726246-xtrachef-invoices-and-invoice-status
last_updated: 2026-08-26
area: invoicing
---

## What it is
The **Invoices** page is the master list of every uploaded document, organized into status tabs. You use it to find missed uploads, watch for rejections, see what's still processing, and confirm what's completed and extracted. You can also upload from this page, change an invoice's location, archive invoices, and run natural-language searches.

## When you'd use it
- Daily and weekly AP monitoring.
- Answering "did invoice X come in, and did it reach QuickBooks?"
- Moving an invoice to the right location, or archiving junk.

## How to do it
1. Click **Invoices** in the xtraCHEF nav menu. It opens on **All invoices**.
2. Tabs:
   - **Action needed**: documents with an exception ("exceptions" is the old name). Since July 2024 these can also be reprocessed in the mobile app.
   - **Rejected**: missing info, irrelevant documents, illegible uploads, and **duplicates**. To see only duplicates, use the **Statuses** drop-down and check **Duplicate**. **Account Admins** can set custom rejection criteria.
   - **Processing**: waiting for xtraCHEF's usability review. Usually 6 to 8 hours, up to 24 hours.
   - **Completed**: approved and ready to use, in chronological order. Search by invoice number or type. Click a column header (vendor, invoice date, amount payable, and others) to sort.
     - **Ready to Extract**: the invoice is complete but the accounting system hasn't pulled it yet. Check the connection under **Account setup > Integrations**. For QuickBooks *Desktop*, running the **QuickBooks Web Connector (QWC)** pulls these.
3. Search bar: plain-English LLM search (for example, a vendor over the last 60 days, or a location under $250).
4. **Change location**: click the upload, choose from the **Location** drop-down, then click **Submit Changes**.
5. **Archive**: select the line and click **Archive** to remove it from xtraCHEF.
6. **Download all invoice images**: ask Customer Care through the blue chat button (lower right) for a bulk invoice image file. The emailed link lasts **one week**, and the file can take **24+ hours** to arrive.

## Settings, options & permissions
- **Tenant Admins** get email notifications at points in the invoice review cycle. They **can't turn these off** except by changing their user role.
- **Account Admins** can configure custom rejection criteria.
- Ready to Extract depends on an active accounting integration.

## Rules, limits & gotchas
- Allow up to 24 hours in Processing before worrying.
- With QBO (online), Ready to Extract that never clears points to an integration or connection problem. Check Integrations, vendor codes, and GL mapping.
- Archive removes the invoice from xtraCHEF. Use it for true junk, not for things you need to fix.
- Bulk delete is a separate feature (see related).

## Automation / efficiency angles
- Agent daily check: the counts on Action needed and Rejected, plus anything in Processing for more than 24 hours.
- Before close: on Completed, filter the month and make sure nothing is stuck in Ready to Extract, so QBO bills match xtraCHEF.
- Use natural-language search for ad hoc audits, such as "all invoices from [vendor] last 30 days," to compare against vendor statements.
- At year-end or for an audit, request the bulk image download and save it before the 1-week link expires.

## Related articles
- [Upload Invoices and Receipts (Desktop)](https://intercom.help/toast-central/en/articles/14232979-xtrachef-upload-invoices-and-receipts-desktop)
- [Track Invoice Status on the xtraCHEF App](https://intercom.help/toast-central/en/articles/14727570-xtrachef-track-invoice-status-on-the-xtrachef-app)
- [Invoice Rejections](https://intercom.help/toast-central/en/articles/14727594-xtrachef-invoice-rejections)
- [Action Needed Invoices](https://intercom.help/toast-central/en/articles/14727783-xtrachef-action-needed-invoices)
- [Map Invoice Items](https://intercom.help/toast-central/en/articles/14727558-xtrachef-map-invoice-items)
- [Bulk Delete Invoices](https://intercom.help/toast-central/en/articles/14095581-xtrachef-bulk-delete-invoices)
- User Roles: https://support.toasttab.com/en/article/xtraCHEF-User-Roles?lang=en_US
