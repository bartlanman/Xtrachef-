---
title: "xtraCHEF: Pay Vendor Bills With Toast Bill Pay"
source: https://intercom.help/toast-central/en/articles/14725514-xtrachef-pay-vendor-bills-with-toast-bill-pay
last_updated: "Updated over 2 weeks ago (no exact date shown)"
area: vendors
---

## What it is
This is the how-to for the xtraCHEF Bill Pay module: the dashboard, bills, payment statuses and the bills report. **Deprecated**: since **August 28, 2026**, you can't submit payments in xtraCHEF Bill Pay. The Dashboard and Bills tabs are gone, and only the **Payments** view and the **bills report download** remain. Pay vendors with **Bill Pay in Toast Web** (Toast Checking). See also [toast-bill-pay-help](../accounting/toast-bill-pay-help.md).

## When you'd use it
- To pull a historical bills or payments report, or to check the status of a past payment.

## How to do it
**Historical dashboard behavior** (the tab has been removed): **Bill Pay > Dashboard** tiles showed amounts due by vendor, the total due, and errors. Clicking the **>** caret opened Bills already filtered (for example, **Due This Week**). There was a **By vendor / By bill** toggle, and the Overview tile had **Overdue**, **Payment Processing** and **Payment Failed** sections.

**Review payments**
1. **Bill Pay > Payments** (formerly Bills > Payment).
2. Read each bill's **Pymt status**:
   - **Scheduled**: queued.
   - **Processing**: in flight, can't be cancelled. Select the bill to see the estimated timeline.
   - **Complete**: the vendor has been paid and funds debited.
   - **Returned**: failed and sent back. It appears under Payment Failed. Contact support@xtrachef.com.
   - **Cancelled**: no funds moved.
- **Note**: scheduled payments can no longer be cancelled. Anything needing a reissue after Aug 28, 2026 is **refunded to you automatically** and not re-sent.

**Download a bills report**
1. **Bill Pay > Bills** (unpaid) or the **Payments** tab (paid), where still available.
2. Filter by **By vendor/By bill**, **date range**, **status** or **vendor**, or search by vendor or invoice number. The filters carry into the report.
3. Click **Download**. Columns: location, vendor, payment type (ACH/check), bill status, invoice number, due date, outstanding amount, vendor address.

## Settings, options & permissions
- Tenant Admin only (see Get Help With Toast Bill Pay).

## Rules, limits & gotchas
- No new payments can be made here. Any refunds for reissued payments need to be matched in QBO and the vendors paid another way.

## Automation / efficiency angles
- Download a final Payments report once and archive it outside the public repo, since it contains vendor amounts. Use it to confirm QBO bill payments match.

## Related articles
- [Get Help With Toast Bill Pay](https://intercom.help/toast-central/en/articles/14487975-xtrachef-get-help-with-toast-bill-pay)
- [Use Bill Pay With Toast Checking](https://intercom.help/toast-central/en/articles/14213863-use-bill-pay-with-toast-checking)
- [Manage Vendors in Bill Pay](https://intercom.help/toast-central/en/articles/15606317-manage-vendors-in-bill-pay)
- [Get Started With Vendors](https://intercom.help/toast-central/en/articles/14727525-xtrachef-get-started-with-vendors)
