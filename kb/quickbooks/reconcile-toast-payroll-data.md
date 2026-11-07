---
title: "xtraCHEF: Reconcile Toast Payroll Data"
source: https://intercom.help/toast-central/en/articles/14725454-xtrachef-reconcile-toast-payroll-data
last_updated: 2026-04-22
area: quickbooks
---
## What it is (2-4 sentences)
How to verify that payroll amounts captured in xtraCHEF's Sync Monitor match Toast Payroll's own reports. It covers fixing a "Payroll Failed" day and comparing totals, earnings, taxes, deductions, fees and payments.

## When you'd use it
- After each payroll (or monthly) to prove the payroll JE matches Toast Payroll before trusting it in QBO and the Operating Summary.

## How to do it (numbered steps with exact menu paths, button and field names)
1. **Sync Monitor** → a day showing **Payroll Failed** → click for reason (e.g., missing GL) → open the pay group's journal link (e.g., **WEEKLY**) → red-highlighted lines need fixing.
2. Total: Toast Payroll **Payroll Summary** report vs xtraCHEF payroll **Payments** total (Net Pay).
3. Earnings: Sync monitor → green payroll date → payroll link → expand **Earnings** (caret) → compare to **Labor distribution by job** (Toast Payroll: **Payroll > Past Payrolls > View**, near the bottom), e.g., Server – REGULAR, Server – TIP Makeup.
4. Deductions, employee taxes, employer taxes, fees, payments: compare Payroll Details to the Payroll Summary report.

## Settings, options & permissions (which roles can do it)
- Not stated; needs xtraCHEF access plus Toast Payroll report access.

## Rules, limits & gotchas (sync errors, mapping rules, what syncs vs what doesn't, timing)
- A failed payroll day blocks the JE until every line has a GL.

## Automation / efficiency angles
- Pair with the QBO Journal report check (see Manage the Payroll Accounting Sync) for a three-way match: Toast Payroll ↔ xtraCHEF ↔ QBO.

## Related articles (links)
- [xtraCHEF: Sync Monitor](https://intercom.help/toast-central/en/articles/14728186-xtrachef-sync-monitor)
- [Toast Payroll: Review Payroll Reports](https://intercom.help/toast-central/en/articles/14727548-toast-payroll-review-payroll-reports)
- [Get Started With Payroll Accounting Sync](https://intercom.help/toast-central/en/articles/14728359-get-started-with-payroll-accounting-sync)
- [Manage the Payroll Accounting Sync](https://intercom.help/toast-central/en/articles/14728361-manage-the-payroll-accounting-sync)
