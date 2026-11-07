---
title: "xtraCHEF: Receipt Extract for QuickBooks Online"
source: https://intercom.help/toast-central/en/articles/14727687-xtrachef-receipt-extract-for-quickbooks-online
last_updated: 2026-04-28
area: quickbooks
---
## What it is (2-4 sentences)
Receipt extract sends documents uploaded as **receipts** (already-paid purchases) to QuickBooks Online as **Expenses**, separate from invoices, which go as Bills. It is QBO-only and off by default; Customer Care turns it on. It requires mapping each xtraCHEF payment method to a QBO GL/bank/card account.

## When you'd use it
- You pay some vendors at the counter/by card (e.g., Costco, Amazon, hardware store) and want those to land in QBO as paid expenses rather than open bills.

## How to do it (numbered steps with exact menu paths, button and field names)
**Enable**: email support@xtrachef.com asking for receipt extract; they'll then ask you to do Payment Method Mapping.

**Payment Method Mapping**
1. **gear icon** (top right) > **Payment Methods**.
2. Methods synced from QBO appear. If none, sync them from **Account Setup** (also under the gear).
3. Highlight a method → **Edit Payment Method**.
4. Choose the **GL Account** the method draws from → **Update**.

**Handle payment method exceptions**
1. **Invoices > Action Needed** → open the receipt (status **Info Missing**).
2. Scroll down, pick from **Payment method used**.
3. Optional: tick **Set as default method for this vendor**.
4. **Submit Changes**. The receipt goes back to processing and extracts as an expense once reconciled.

## Settings, options & permissions (which roles can do it)
- Enabled only by Customer Care. Payment Methods setup under gear menu (admin-level).
- During QBO onboarding, the question "extract receipts to QBO?" — Toast recommends **No** unless you need it.

## Rules, limits & gotchas (sync errors, mapping rules, what syncs vs what doesn't, timing)
- QBO only.
- Receipts from vendors with no default payment method are held as Info Missing until assigned.
- Payment method names must match QBO exactly (**Settings > All Lists > Payment Methods**) or you'll get "Payment 'XXXXX' does not exist in QuickBooks".
- Receipts (RC doc type) without a payment method cause "There is no row at position 0."
- Uploading a receipt for a purchase that also hits the bank/credit card feed: match it in QBO rather than adding, or you double-count.

## Automation / efficiency angles
- Set a default payment method on every card-paid vendor once — eliminates recurring Info Missing exceptions.
- Weekly: filter Action Needed for Info Missing.
- Decide policy with the bookkeeper: if credit-card feed already categorizes these, keep receipt extract off and use receipts only for xtraCHEF cost reporting.

## Related articles (links)
- [xtraCHEF: Upload Invoices and Receipts (Desktop)](https://intercom.help/toast-central/en/articles/14232979-xtrachef-upload-invoices-and-receipts-desktop)
- [xtraCHEF: Extract Monitor](https://intercom.help/toast-central/en/articles/14727735-xtrachef-extract-monitor)
- [xtraCHEF: QuickBooks Compatibility](https://intercom.help/toast-central/en/articles/14727478-xtrachef-quickbooks-compatibility)
- [xtraCHEF: Get Help With QuickBooks Extract Errors](https://intercom.help/toast-central/en/articles/14727646-xtrachef-get-help-with-quickbooks-extract-errors)
- [xtraCHEF: Get Started With QuickBooks Online Sales Syncing](https://intercom.help/toast-central/en/articles/9308304-xtrachef-get-started-with-quickbooks-online-sales-syncing)
