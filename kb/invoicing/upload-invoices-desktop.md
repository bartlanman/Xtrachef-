---
title: "xtraCHEF: Upload Invoices and Receipts (Desktop)"
source: https://intercom.help/toast-central/en/articles/14232979-xtrachef-upload-invoices-and-receipts-desktop
last_updated: 2026-07-07
area: invoicing
---

## What it is
There are three ways to get documents into xtraCHEF from a computer. **Upload document** takes files, and there's an optional **Instant Upload**. **Create document** is for keying in data by hand. **Email** uses a per-location @xcinvoice.com address. Uploaded documents feed reporting and cost tracking. Food prime cost and inventory values require **xtraCHEF Pro**. Operating Summary, Budgets, and COGS are on **Essentials and Pro**.

## When you'd use it
- PDF invoices from vendor portals, scanned paper, or a damaged document you need to key in.
- Setting up email-in so vendor emails flow in automatically.

## How to do it
**Invoice vs. receipt (choose correctly)**
- **Invoice** = not yet paid. QuickBooks calls this a *bill*, and it shows as open or unpaid in accounting.
- **Receipt** = already paid. Record the payment method (check or credit card) so it can extract as paid instead of as an unpaid bill.
- Choosing wrong risks double-paying a vendor or double-posting an expense.

**Method 1: Upload document**
1. On the **Dashboard**, click **Upload document**. A sidebar opens.
2. Pick the **Location**.
3. Pick the type: **Invoice** (the usual choice; extracts to accounting once reconciled), **Receipt** (doesn't extract by default), or **Statement** (only appears if Vendor Statement Reconciliation is enabled, which is off by default).
4. Drag the file into the blue area or click **+ Browse Files**. Accepted types: **.jpg, .jpeg, .png, .pdf**. No size limit is stated.
5. Click **Submit**. A pop-up confirms the upload.

**Instant Upload** (optional; ask **support@xtrachef.com** to enable it)
- Processes **single-page** invoices immediately and suggests a category for each line. Fields that need attention, such as a new vendor to create, are highlighted in red. Look for the **Instant Upload** button. If you don't see it, use **Upload document**.

**Method 2: Create document (manual entry)**, for torn, stained, or illegible paper
1. Click the button next to **Upload document**, then **Create document**.
2. **Document type**: Invoice, Receipt, or **Credit Memo**.
3. **Vendor**: search existing vendors or type a new one. New vendors are saved to the Vendor tab.
4. **Invoice Date**: type it or use the calendar.
5. **Invoice #** (required): type it or click the **randomize** icon.
6. Click **+ Add Line Item** for each line (**Item Code**, **Description**, **Quantity**, **Unit Price**, and so on).
7. Click **Submit**. You can download a PDF of what you entered.

**Method 3: Email**
- Each **location** has its own address. **PDF** invoices sent there upload automatically.
- Find it on the **Dashboard** or the **Upload documents** page.
- To customize it: **gear icon > Locations**, select the location, **Edit Location Details**, then edit the text before **@xcinvoice.com** in **Email invoices to**. Optionally set the **Reply option** and an address for "invoice received" confirmations. Click **Save**.

## Settings, options & permissions
- Email-in accepts only **PDFs** from **senders who are users** on the account. Add staff or vendors as users (Manage User Profiles).
- **Receipt extract to QBO is off by default.**
- Instant Upload must be turned on by support.

## Rules, limits & gotchas
- **If you turn on receipt extract to QBO**, make sure no QBO bank rules or reconciliation habits will double-post. Every bank or card feed transaction has to be *matched* to the receipt expense xtraCHEF created, not added as a new one.
- **Changing the email address breaks the old one.** Mail to the old address isn't processed, so tell every vendor and staff member.
- Capture the full page: vendor name, invoice ID, totals, and all lines. Use good light and a neutral background.
- Manually created invoices may trigger a **Manual Upload** approval rule if one is set up.
- In the early weeks expect manual reconciliation. That work trains the ML.

## Automation / efficiency angles
- **Email-in everywhere:** ask every vendor (Sysco, PFG, the beer distributors, and so on) to send invoices to the location's xcinvoice address. Add the vendor's sending address as a user so the mail is accepted. Or set a Gmail filter that auto-forwards vendor invoice emails from a registered mailbox.
- Give each location (taproom, restaurant, Foundry venue) its own address so invoices land at the right location automatically.
- Use **Credit Memo** in Create document for credits that arrive without paperwork.
- Ask support to turn on Instant Upload for faster single-page processing.
- Decide on a policy for receipts that are company card purchases. If QBO already pulls the card feed, either keep receipt extract off, or turn it on and train the bookkeeper to *match* rather than *add*.

## Related articles
- [Upload Invoices and Receipts on Mobile](https://intercom.help/toast-central/en/articles/14727675-xtrachef-upload-invoices-and-receipts-on-mobile)
- [Receipt Extract for QuickBooks Online](https://intercom.help/toast-central/en/articles/14727687-xtrachef-receipt-extract-for-quickbooks-online)
- [Invoices and Invoice Status](https://intercom.help/toast-central/en/articles/14726246-xtrachef-invoices-and-invoice-status)
- [Map Invoice Items](https://intercom.help/toast-central/en/articles/14727558-xtrachef-map-invoice-items)
- [Action Needed Invoices](https://intercom.help/toast-central/en/articles/14727783-xtrachef-action-needed-invoices)
- [Vendor Statement Reconciliation](https://intercom.help/toast-central/en/articles/9309024-xtrachef-vendor-statement-reconciliation)
- Manage User Profiles: https://central.toasttab.com/s/article/xtraCHEF-Manage-User-Profiles
- Custom Categories: https://central.toasttab.com/s/article/xtraCHEF-Custom-Categories
