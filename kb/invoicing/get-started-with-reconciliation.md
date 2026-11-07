---
title: "xtraCHEF: Get Started With Reconciliation"
source: https://intercom.help/toast-central/en/articles/14727480-xtrachef-get-started-with-reconciliation
last_updated: 2026-08-18
area: invoicing
---

## What it is
The **Reconciliation** page is the pipeline view for every uploaded invoice and receipt. It shows how many are in each processing stage and lets you drill into problems. It has three parts: the **Reconciliation Dashboard** (a bar graph of status columns), **Invoice Detail** (a row per upload with who uploaded it and its status), and the **Inbox** (everything received through your "xcinvoice" email-in address).

## When you'd use it
- Weekly AP review, to see what's stuck and where.
- Bookkeeper checks of vendor statements against individual invoices, without chasing the chef or GM.
- Confirming that an emailed invoice was accepted.

## How to do it
1. Click **Reconciliation** in the xtraCHEF nav bar.
2. **Dashboard**: it defaults to the current week. Filter by **location**, **date range**, and **uploading source**.
   - **Uploaded** (leftmost column): every upload in the range. Clicking it opens **Invoice Detail**.
   - Status columns: clicking **Rejected**, **Info missing**, or **Extract failed: Missing vendor code** opens those invoices on the **Invoices** page so you can fix them. Clicking any other status column opens them in Invoice Detail.
3. **Invoice Detail**: click a column or the **Invoice Detail** tab. Rows are sorted by **Uploaded Date**.
   - Use **Search** (top right of the **Transaction Status Details** table) to find a specific invoice.
   - Each row shows the upload date, the uploader, and the status (green = processed, yellow = processing).
   - Click **^** under **Batch Details** to expand more information.
   - Click the invoice icon under **View Invoice** to see the original scan and its lines.
4. **Inbox**: lists emails sent to the xcinvoice address from registered users, newest first. Green = accepted, red = rejected.

## Settings, options & permissions
- No roles are stated.
- Email-in only accepts emails from **registered users** of the xtraCHEF account that carry a **PDF** invoice.

## Rules, limits & gotchas
- **You can't export** the filtered Reconciliation or Invoice Detail lists as a report. You can only filter on screen.
- Emails from unregistered senders, or without a PDF, aren't accepted (they show red in the Inbox or end up as "Invoice from unregistered user").
- The default range is the current week. Widen it at month-end.

## Automation / efficiency angles
- **Email-in is the biggest efficiency lever.** Have every vendor that emails PDFs send them, or set auto-forwarding, to the xtraCHEF xcinvoice address. Make sure the forwarding mailbox is a registered user.
- Weekly agent routine: open Reconciliation for the last 7 days and confirm the Rejected, Info missing, and Extract failed columns are zero. Then check the Inbox for red rows.
- Filter by **uploading source** to see whether one channel (mobile, email, or desktop) produces most of the rejections.
- Since there's no export, an agent can read the screen or use the browser to compile counts into a log.

## Related articles
- [Vendor Statement Reconciliation](https://intercom.help/toast-central/en/articles/9309024-xtrachef-vendor-statement-reconciliation)
- [Invoices and Invoice Status](https://intercom.help/toast-central/en/articles/14726246-xtrachef-invoices-and-invoice-status)
- [Rejected and Action Needed Invoices](https://intercom.help/toast-central/en/articles/14727567-xtrachef-rejected-and-action-needed-invoices)
- [Track Invoice Status on the xtraCHEF App](https://intercom.help/toast-central/en/articles/14727570-xtrachef-track-invoice-status-on-the-xtrachef-app)
- [Invoice Rejections](https://intercom.help/toast-central/en/articles/14727594-xtrachef-invoice-rejections)
