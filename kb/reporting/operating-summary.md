---
title: "xtraCHEF: Operating Summary"
source: https://intercom.help/toast-central/en/articles/14728290-xtrachef-operating-summary
last_updated: 2026-04-28
area: reporting
---
## What it is (2-4 sentences)
xtraCHEF's P&L-style view for one location and one month/week: revenue, prime cost (COGS + labor), gross profit, operating costs and net profit, each compared to budget. It combines Toast sales, uploaded expenses and (if integrated) Toast Payroll. It's the closest thing Toast offers to a native P&L.

## When you'd use it
- Monthly review of profitability before the bookkeeper closes QBO; compare against the QBO P&L to find missing invoices or mis-coded expenses.

## How to do it (numbered steps with exact menu paths, button and field names)
1. Click **Operating Summary** in the nav bar (also listed in Reporting > Cost management).
2. Defaults to current month/week of your accounting period, last-used location (prompts to create an accounting period if none).
3. Filters: **Month or week**, **Year**, **Location** — page refreshes automatically.
4. Click any row to expand components and see budget comparison.

Rows / formulas:
- **Revenue** — month (or MTD) income before deductions.
- **Prime Cost** = COGS + Payroll (COGS $ and % of revenue by COGS group; Payroll $ and %).
- **Gross Profit** = Revenue − Total COGS.
- **Operating Costs** — rent, maintenance, repairs, equipment, etc.
- **Net Profit** = Gross Profit − (Payroll + Operating Costs); green if positive, red if negative.

## Settings, options & permissions (which roles can do it)
Setup needed for full data:
1. Accounting period (Add New Accounting Period).
2. COGS mapping.
3. Toast Payroll integration + payroll setup (populates Payroll; labor groups required).
4. Budget (populates Budget column).
No role restrictions stated.

## Rules, limits & gotchas (sync errors, mapping rules, what syncs vs what doesn't, timing)
- Only as complete as your uploads — any expense not uploaded to xtraCHEF (rent, utilities paid by autopay) is missing unless you upload those bills too.
- Payroll appears only after labor groups are assigned.
- Payroll reporting allocation (spread over pay period vs last day) changes weekly views.

## Automation / efficiency angles
- Month-end: line-by-line compare Operating Summary to QBO P&L (via QBO connector). Differences = invoices not uploaded, receipts not extracted, or GL mismatches.
- Upload recurring non-food bills (utilities, CO2, linen, rent) so Operating Costs is real.
- Use Basic City targets as Budget so the Budget column flags overruns automatically.

## Related articles (links)
- [xtraCHEF: Get Started With Budget Reporting](https://intercom.help/toast-central/en/articles/14728192-xtrachef-get-started-with-budget-reporting)
- [xtraCHEF: Review Reports in the Reporting Module](https://intercom.help/toast-central/en/articles/14727530-xtrachef-review-reports-in-the-reporting-module)
- [xtraCHEF: Chart of Accounts](https://intercom.help/toast-central/en/articles/14727682-xtrachef-chart-of-accounts)
- [xtraCHEF: Glossary and Terminology](https://intercom.help/toast-central/en/articles/14487632-xtrachef-glossary-and-terminology)
- [Profit & Loss Statements](https://intercom.help/toast-central/en/articles/14412151-profit-loss-statements)
