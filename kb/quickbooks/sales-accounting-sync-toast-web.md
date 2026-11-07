---
title: Get Started With Sales Accounting Sync
source: https://intercom.help/toast-central/en/articles/15197015-get-started-with-sales-accounting-sync
last_updated: 2026-08-18
area: quickbooks
---
## What it is (2-4 sentences)
Toast Web's built-in connector that posts daily sales journal entries straight to QuickBooks Online, without xtraCHEF. It's currently in **limited release for Toast Retail customers** only. Linked from the QuickBooks collection; documented here because it's the likely future replacement for xtraCHEF sales sync.

## When you'd use it
- If/when Toast offers it to restaurant accounts — not currently for Basic City (restaurant), which uses xtraCHEF Sales Setup.

## How to do it (numbered steps with exact menu paths, button and field names)
1. Access: **Finance > Accounting > Connections** (Toast Web), **Accounting** (Toast Payroll), or **Connect to QuickBooks** on a Confirmation step. Log out of all QBO tabs first.
2. **Log in to QuickBooks Online** → credentials → choose company → **Next**.
3. Tick Toast POS locations for this QBO company → **Continue**; (Payroll customers) choose pay groups → **Continue**.
4. Sales settings: **Start date**, **Discounts**, **Journal update frequency**, **Posting method** (sales & card deposits; future only), **Cash Activity** (include drawer activity; future only), **Payments/fee posting method**.
5. **Continue to assignments** → **Sales breakout** (class use, default class per location; line-item classes override).
6. Assign **GL code** and **Class** for: Sales categories, Service charges, Tips, Discounts, Taxes, Payments, Withholdings, Payment fees, Deferrals, Refunds, Cash activity, Adjustments → **Save**.

## Settings, options & permissions (which roles can do it)
- QBO only (no Desktop); Toast Retail customer; 8.1 Financial Accounts (necessary, not sufficient); QBO Primary Admin.

## Rules, limits & gotchas (sync errors, mapping rules, what syncs vs what doesn't, timing)
- Every location's lines must be mapped before its JEs post.
- Check that no JEs already exist after the start date (duplicates).
- Never run this AND xtraCHEF sales sync for the same location — double revenue.

## Automation / efficiency angles
- Watch for a rollout to restaurants; if migrating, turn off xtraCHEF **Sales Sync** (Sales Setup step 5) the same day you set this start date.

## Related articles (links)
- [Get Help With Accounting Sync](https://intercom.help/toast-central/en/articles/14412153-get-help-with-accounting-sync)
- [xtraCHEF: Get Help With Sales Syncs to QuickBooks](https://intercom.help/toast-central/en/articles/14728156-xtrachef-get-help-with-sales-syncs-to-quickbooks)
- [Get Started With Payroll Accounting Sync](https://intercom.help/toast-central/en/articles/14728359-get-started-with-payroll-accounting-sync)
- [Get Started With Accounting Sync: Accounts Payable](https://intercom.help/toast-central/en/articles/15972247-get-started-with-accounting-sync-accounts-payable)
