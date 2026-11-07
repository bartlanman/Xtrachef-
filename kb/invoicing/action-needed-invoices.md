---
title: "xtraCHEF: Action Needed Invoices"
source: https://intercom.help/toast-central/en/articles/14727783-xtrachef-action-needed-invoices
last_updated: 2026-04-22
area: invoicing
---

## What it is
"Action Needed" is the holding bucket for invoices that xtraCHEF cannot finish processing on its own. Usually a critical field (amount, date, or invoice number) is missing or unreadable, though post-processing tasks also land here: categorizing, approving, and fixing extract problems. Invoice data does not feed cost insights, inventory count lists, or recipes until these invoices are cleared.

## When you'd use it
- Daily or weekly AP hygiene: clear stuck invoices so food and beverage costs stay current.
- When the dashboard Invoice tile shows a non-zero Action Needed count.
- Before month-end close, so every invoice has extracted to QuickBooks Online.

## How to do it
**Find stuck invoices (desktop)**
1. Dashboard route: on the xtraCHEF dashboard, open the **Invoice** tile and go to its **Action Needed** tab. Entries that start with **"Info Missing"** are blocked on missing critical data. Click one to jump to those invoices.
2. Invoices page route: go to **Invoices** and click **Action Needed** at the top. The **Status** column shows why each invoice was flagged.
3. Click anywhere on the row except the Invoice Number to open **Invoice Details**. Review and edit the data there.

**Fix by status**
- **Missing invoice date**: type in the date. Reports use it to pick which price applies.
- **Missing invoice number**: type in the number, which is xtraCHEF's duplicate guard. If the vendor never prints numbers, or you want a receipt handled like an invoice, check **Always auto-assign invoice numbers for this vendor** so xtraCHEF generates a unique ID for that vendor. If the document is really a receipt, switch its document type to Receipt. Receipts don't need a number, so the error clears.
- **Invoice total missing**: confirm the total by hand. xtraCHEF normally checks line items against the total, so you have to vouch that it was read correctly.
- **Invoice or line totals don't match**: the line items don't add up to the captured total. Verify or edit the lines. If a page was never uploaded, reject the invoice and re-upload the full document.
- **Payment method mandatory**: shows up only for a QuickBooks Online extract with **payment method processing** turned on, which books receipts as expenses. Enter the payment method used and make sure it maps to the matching QBO payment method.
- **Invoice from unregistered user**: the sender's email isn't a registered user. Verify the invoice and accept it. Accepting registers that address as an **Invoice Capture** user, so future emails from it won't be flagged.
- **Missing vendor code**: an accounting extract is on and the vendor has no vendor code (the vendor's display name in the accounting system). Add the code. These invoices no longer block processing; they now show **Extract pending**.

**Other Action Needed states (after processing)**
- **Ready to categorize**: the invoice has items processed for the first time that still need a category.
- **Ready to approve**: approval rules flagged the invoice and it hasn't been approved yet.
- **Extract pending / Extract failed**: the invoice can't export to accounting, typically because of a missing vendor code or a GL mapping error. Use the Extract Monitor to fix it.

**Mobile**
1. On the app home screen, tap the **Tasks** tile. It includes Action Needed invoices.
2. Similar items are grouped. For example, "Extract pending: Map vendor to QuickBooks Online" can cover 4 invoices in one task.
3. Tap a task. For a missing vendor code, accept a suggested vendor, create a new vendor name, or search the vendor list. For a missing vendor name or invoice number, type the value, check the **Invoice** tab to see the image, then tap **Submit changes** to reprocess.

## Settings, options & permissions
- **Always auto-assign invoice numbers for this vendor**: a per-vendor toggle.
- **Payment method processing** (QBO extract setting): turning it on creates the "Payment method mandatory" requirement.
- Accepting an invoice from an unregistered sender gives that address the Invoice Capture role.
- The article names no specific role requirement for resolving these. Approvals require being an assigned approver.

## Rules, limits & gotchas
- Some tasks can only be done on desktop. "Info missing: unbalanced invoice" cannot be resolved on mobile.
- A missing page is the usual cause of total mismatches. Reject and re-upload rather than forcing the lines to balance.
- Missing vendor codes no longer stop processing but still hold back the accounting extract (Extract pending).
- Uncategorized items on a vendor's first invoice will hold that invoice in Ready to categorize.

## Automation / efficiency angles
- Turn on auto-assign invoice numbers for vendors that never print numbers, such as farmers' market, hardware store, and taproom cash purchases. This removes a recurring exception.
- Set vendor codes for every vendor up front, matching QBO vendor display names, to prevent Extract pending.
- Register every staff member who emails invoices as an Invoice Capture user so their uploads never stall.
- Work grouped tasks in the mobile app to clear many invoices with one action.
- A manager or agent can review **Invoices > Action Needed** once a day sorted by Status, then once a week confirm the Extract pending/failed count is zero before close.

## Related articles
- [Invoice Rejections](https://intercom.help/toast-central/en/articles/14727594-xtrachef-invoice-rejections)
- [Rejected and Action Needed Invoices](https://intercom.help/toast-central/en/articles/14727567-xtrachef-rejected-and-action-needed-invoices)
- [Invoices and Invoice Status](https://intercom.help/toast-central/en/articles/14726246-xtrachef-invoices-and-invoice-status)
- [Approvals](https://intercom.help/toast-central/en/articles/14726182-xtrachef-approvals)
- [Edit Invoice Line Items](https://intercom.help/toast-central/en/articles/9333507-xtrachef-edit-invoice-line-items)
- [Upload Invoices and Receipts (Desktop)](https://intercom.help/toast-central/en/articles/14232979-xtrachef-upload-invoices-and-receipts-desktop)
- Extract Monitor: https://central.toasttab.com/s/article/xtraCHEF-Extract-Monitor
- User Roles: https://central.toasttab.com/s/article/xtraCHEF-User-Roles
