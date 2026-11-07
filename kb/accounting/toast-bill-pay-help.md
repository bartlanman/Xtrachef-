---
title: "xtraCHEF: Get Help With Toast Bill Pay"
source: https://intercom.help/toast-central/en/articles/14487975-xtrachef-get-help-with-toast-bill-pay
last_updated: "Updated over 2 weeks ago (no exact date shown)"
area: accounting
---

## What it is
xtraCHEF Bill Pay let Tenant Admins pay vendor bills (completed invoices) by ACH or check straight from xtraCHEF. **It's deprecated.** As of **August 28, 2026**, you can no longer submit new payments in xtraCHEF Bill Pay. The Dashboard and Bills tabs are gone, and only the **Payments** history view and a bills report download remain. Vendor payments now go through **Bill Pay in Toast Web** (Toast Checking).

## When you'd use it
- To look up historical payments made through xtraCHEF Bill Pay, or download the bills report.
- To understand how the old payments were recorded in QBO.
- For any new vendor payment, use Toast Web Bill Pay or QBO/your bank instead.

## How to do it (what's still available)
1. Go to **Bill Pay** in the left nav, then **Payments**, to see submitted and pending payments.
2. **View details**: select the invoice, then **three dots > View Payment Details**. This shows the payment and who submitted it.
3. **Cancel** (only for a payment still **Scheduled**): open the bill, expand payment activity, then **three dots > Cancel payment**.
4. Settings live under **gear icon > Bill Pay**. This is where the ACH toggle and the deposit bank account were.

## Settings, options & permissions
- **Tenant Admin only**. Restaurant Manager, Invoice Capture, Restaurant User and Executive had no access.
- Browsers: Chrome and Edge (desktop and mobile). Safari and other mobile browsers were not supported.

## Rules, limits & gotchas (historical behavior)
- A "bill" was an invoice with no pending reviews or exceptions. Receipts and credit memos never appeared.
- By default it pulled completed invoices uploaded in the **last 30 days**. support@xtrachef.com could change that.
- Due dates came from the invoice due date, vendor payment terms or the default term. With no default, it used due date + 1 week.
- Bank account only. The Toast deposit account was used, and ACH was off until you turned it on.
- Vendor method came from **Vendors > [vendor] > Bill Pay**. If both ACH details and a remit address existed, the vendor got ACH. Otherwise they got a check from "Toast" mailed to the remit address.
- Each invoice was charged separately, with the invoice number in the bank description. Vendors saw "Toast Payments" (ACH) or a Toast check with your memo and Customer ID.
- Statuses: **Scheduled** (cancellable), **Processing** (not cancellable; email toastbillpay@toasttab.com), **Complete**, **Returned** (contact support@xtrachef.com), **Canceled**.
- Delivery took up to **10 business days**, so payments needed scheduling more than 10 business days before the due date. Checks took about 10–12 days by First Class Mail.
- Once funds were secured, a bill payment was written to QBO and the bill marked paid.
- Payments that needed reissuing after Aug 28, 2026 (bad ACH info, for example) were **refunded to you, not re-sent**. Watch for those refunds and pay the vendors another way.

## Automation / efficiency angles
- For Basic City: if any vendor bills were paid through xtraCHEF Bill Pay before the cutoff, check in QBO that each bill payment exists, and that any refunded or returned payment was matched to a refund deposit and the bill reopened.
- Vendor ACH and remit data entered in xtraCHEF doesn't automatically carry over to Toast Web Bill Pay. Re-check vendor setup there ("Manage Vendors in Bill Pay").

## Related articles
- [Pay Vendor Bills With Toast Bill Pay](https://intercom.help/toast-central/en/articles/14725514-xtrachef-pay-vendor-bills-with-toast-bill-pay)
- [Use Bill Pay With Toast Checking](https://intercom.help/toast-central/en/articles/14213863-use-bill-pay-with-toast-checking)
- [Manage Vendors in Bill Pay](https://intercom.help/toast-central/en/articles/15606317-manage-vendors-in-bill-pay)
- [Toast Credit Card Processing and Billing FAQ](https://intercom.help/toast-central/en/articles/9308299-toast-credit-card-processing-and-billing-faq)
