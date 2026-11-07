---
title: "Get Started With Accounting Sync: Accounts Payable / Manage Accounting Sync: Accounts Payable"
source: https://intercom.help/toast-central/en/articles/15972247-get-started-with-accounting-sync-accounts-payable
last_updated: 2026-09-28 (Get Started); Manage = "updated this week" as of 2026-11-07
area: quickbooks
---
## What it is (2-4 sentences)
Toast Web's native AP sync that posts vendor bills processed in Toast (Retail AI invoice scanning) directly to QuickBooks Online under the right vendor, expense account, class and location. Currently **Toast Retail only**; covered because the QuickBooks collection links to it and it parallels xtraCHEF's invoice extract. Second source: https://intercom.help/toast-central/en/articles/15972248-manage-accounting-sync-accounts-payable

## When you'd use it
- Retail accounts using Toast's invoice scanning instead of xtraCHEF. Not Basic City's current path.

## How to do it (numbered steps with exact menu paths, button and field names)
**Setup**
1. Connect QBO (Log in to QuickBooks Online → pick company → **Next** → tick POS locations → **Continue**).
2. **Retail > Settings > Accounts Payable** → **Post to accounting system** → choose location(s) → **Select location** → **Save**.
3. Expense categories: **GL codes** → select → **Create [n] selected**; **Add category** to add more; click a category to edit → **Save**.
4. **Retail > Item catalog** → set **Expense category** per item → **Update**; bulk: select items → **Select expense category** → **Update items**; **Filter** → Expense category = **Blank** to find gaps → **Publish**.

**Manage** (Finance > Accounting): **Activity** (green/red calendar, banners, failure emails), **AP Bill Assignments** (Finance > Assignments > AP Bill Assignments: class per location, GL per expense category, vendors from Retail Suppliers list), **Settings**, **Connections** (Connected status, edit pencil, three-dot reconnect, Add QuickBooks Online account).

Settings: **Post to accounting system** (daily AP entry per location), **Sync start date**, **Bill posting method** = **Summarized by Expense Category** (one line per category) or **Detailed by product** (one line per product, name in description).

## Settings, options & permissions (which roles can do it)
- QBO only, 8.1 Financial Accounts, QBO Primary Admin, Toast Retail.

## Rules, limits & gotchas (sync errors, mapping rules, what syncs vs what doesn't, timing)
- Sales sync and AP sync share location connections — changing one affects the other.
- Bill assignments follow Connections, not locations.
- Click **Save** before leaving Settings.
- Start date overlap → duplicates.

## Automation / efficiency angles
- Not applicable to Basic City today; if ever adopted, xtraCHEF invoice extract must be disabled for the same locations to avoid duplicate bills.

## Related articles (links)
- [Manage Accounting Sync: Accounts Payable](https://intercom.help/toast-central/en/articles/15972248-manage-accounting-sync-accounts-payable)
- [Get Started With Sales Accounting Sync](https://intercom.help/toast-central/en/articles/15197015-get-started-with-sales-accounting-sync)
- [Get Help With Accounting Sync](https://intercom.help/toast-central/en/articles/14412153-get-help-with-accounting-sync)
- [xtraCHEF: Get Started With QuickBooks Online Sales Syncing](https://intercom.help/toast-central/en/articles/9308304-xtrachef-get-started-with-quickbooks-online-sales-syncing)
