---
title: "xtraCHEF: Get Started With Spending by GL Analytics"
source: https://intercom.help/toast-central/en/articles/14728263-xtrachef-get-started-with-spending-by-gl-analytics
last_updated: 2026-04-28
area: reporting
---
## What it is (2-4 sentences)
The default Analytics view: a pie chart + table of spend by GL code for a location and date range, drilling GL → category → invoice item → invoices. Because GLs mirror QBO, it's the best xtraCHEF view to reconcile against QuickBooks expenses.

## When you'd use it
- Checking how spend is allocated across GLs; reconciling to QBO by account.

## How to do it (numbered steps with exact menu paths, button and field names)
1. **Reports** (left side) → **Cost visualization** → **Spending by GL** (also Analytics default).
2. Default: most recent calendar week (respects your tenant week-start setting). Choose **location** and **date range** → **Refresh**.
3. **GL view**: GL list right of the chart — click to remove/restore; **Deselect All**; spending slider under chart.
4. Click a GL → **Categories view** (deselect/slider).
5. Click a category → **Invoice Item view** (select items/**Deselect All**, price slider).
6. Click an item → **Invoices** timeline; click a point or table row to open the source invoice.

Cost Visualization variant (formerly **Spend Summary by GL**): pick date range → **Generate Report** → totals of purchases and credits per location → **downward arrow** in **View** column for GL detail → **View** on a GL row for category breakdown.

## Settings, options & permissions (which roles can do it)
- None stated; week start from Tenant Configuration settings.

## Rules, limits & gotchas (sync errors, mapping rules, what syncs vs what doesn't, timing)
- Reflects invoices in xtraCHEF by invoice date; QBO bills may have different dates if edited — compare like-for-like dates.

## Automation / efficiency angles
- Month-end: export Spending by GL for the month and compare each GL to QBO P&L lines (via QBO connector). Any GL where QBO > xtraCHEF suggests bills entered directly in QBO or the bank feed; xtraCHEF > QBO suggests failed extracts.

## Related articles (links)
- [xtraCHEF: General Ledger (GL) Codes](https://intercom.help/toast-central/en/articles/14725478-xtrachef-general-ledger-gl-codes)
- [xtraCHEF: Review Analytics Reports](https://intercom.help/toast-central/en/articles/14727580-xtrachef-review-analytics-reports)
- [xtraCHEF: Get Started With Spending by Vendor Analytics](https://intercom.help/toast-central/en/articles/14728264-xtrachef-get-started-with-spending-by-vendor-analytics)
- [xtraCHEF: Get Started With Category Weekly Analytics](https://intercom.help/toast-central/en/articles/14728266-xtrachef-get-started-with-category-weekly-analytics)
- [xtraCHEF: Tenant Configuration Settings Overview](https://central.toasttab.com/s/article/xtraCHEF-Tenant-Configuration-Settings-Overview)
