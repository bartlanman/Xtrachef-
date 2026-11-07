---
title: "Manage Vendors in Bill Pay"
source: https://intercom.help/toast-central/en/articles/15606317-manage-vendors-in-bill-pay
last_updated: 2026-09-17
area: vendors
---

## What it is
Vendor management for **Toast Web Bill Pay** (part of Toast Checking). This is the replacement for xtraCHEF Bill Pay, which stopped taking payments on Aug 28, 2026. It's a **separate vendor list** from the xtraCHEF Vendor Hub. You keep each vendor's name, address, account number, remittance email, ACH details and check remittance address here.

## When you'd use it
- Setting up vendors so you can pay them from Toast Web Bill Pay.
- Updating a vendor's bank details or address.

## How to do it
**View**: **Toast Web > Bill Pay > Vendors**.

**Add**
1. Click **Add vendor**.
2. Enter **Vendor name** (required), **Address** (required), **Customer account number** (optional) and **Vendor remittance email** (optional).
3. Click **Save**. You can also add a vendor, or its account number, while submitting a payment.

**Edit**: click the **pencil icon**, update the details, then **Save**. The change applies from the next payment.

**ACH details**: click the vendor name, then **Add bank details** or **Edit bank details**. Enter the account number, routing number and account type (checking or savings), then **Save**.

**Check remittance address**: click the vendor name, then **Add remittance address** or **Edit remittance address**. Enter the mailing address, then **Save**.
- If a vendor has both ACH and a remit address saved, you pick the method on each payment.

**Delete**: click the **trashcan icon** and confirm. This **can't be undone**.

## Settings, options & permissions
- Requires the Toast Web permission **8.1 Financial Accounts**.
- The **account Owner gets an email whenever a vendor's payment info changes**. This is a fraud safeguard.

## Rules, limits & gotchas
- Vendor data, including ACH details, from xtraCHEF Bill Pay or the Vendor Hub doesn't carry over. Re-enter it here.
- A deleted vendor can't be selected for payments and can't be restored.

## Automation / efficiency angles
- The agent must **never** enter bank or routing numbers (see CLAUDE.md). Bart does that. The agent can prepare the vendor list (names, addresses, remittance emails) for Bart to enter.
- Treat the owner's "payment info changed" email as a security alert. If a change wasn't expected, check it straight away, because vendor-impersonation ACH fraud is common.

## Related articles
- [Use Bill Pay With Toast Checking](https://intercom.help/toast-central/en/articles/14213863-use-bill-pay-with-toast-checking)
- [xtraCHEF: Get Help With Toast Bill Pay](https://intercom.help/toast-central/en/articles/14487975-xtrachef-get-help-with-toast-bill-pay)
- [xtraCHEF: Pay Vendor Bills With Toast Bill Pay](https://intercom.help/toast-central/en/articles/14725514-xtrachef-pay-vendor-bills-with-toast-bill-pay)
- [Toast Payroll: Configure Vendors](https://intercom.help/toast-central/en/articles/14725459-toast-payroll-configure-vendors)
- [Manage Your Invoices](https://intercom.help/toast-central/en/articles/14756000-manage-your-invoices)
