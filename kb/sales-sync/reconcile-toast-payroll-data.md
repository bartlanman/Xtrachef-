---
title: "xtraCHEF: Reconcile Toast Payroll Data"
source: https://intercom.help/toast-central/en/articles/14725454-xtrachef-reconcile-toast-payroll-data
last_updated: 2026-04-22
area: sales-sync
---

## What it is
How to check that the payroll journal xtraCHEF captures from Toast Payroll (shown in Sync Monitor) matches Toast Payroll's own reports, and how to fix a failed payroll sync.

## When you'd use it
- After each payroll run, if payroll JEs flow through xtraCHEF.
- When the Sync Monitor shows **Payroll Failed**.

## How to do it
**Fix a failed payroll sync**
1. Open **Sync Monitor** in the left nav.
2. Click a day marked **Payroll Failed** to see the reason (for example, a payroll line with no GL code).
3. Click the **WEEKLY** (payroll journal) link. Lines that need attention show in **red**. Fix the mapping, then retry the sync.

**Reconcile, at four levels**
1. **Total**: compare the Toast Payroll **Payroll Summary** report with the xtraCHEF payroll **Payments** total.
2. **Earnings**: in xtraCHEF, go to **Sync monitor**, click a green payroll date, click the named payroll link, then use the **caret** to expand **Earnings** (role lines such as "Server - REGULAR" and "Server - TIP Makeup"). In Toast Payroll, go to **Payroll > Past Payrolls > View** and use the **Labor distribution by job** report at the bottom. Compare the two line by line.
3. **Deductions, employee taxes, employer taxes, fees, payments**: compare xtraCHEF **Payroll Details** with the Toast **Payroll summary** report.

## Settings, options & permissions
- Sync Monitor is available to TA, EX, RM and RU. Payroll setup and GL fixes need a TA.
- Requires the Toast Payroll + xtraCHEF integration and Payroll Setup.

## Rules, limits & gotchas
- A missing GL on any payroll line fails the whole payroll journal.
- If you use Toast Payroll's **direct Payroll Accounting Sync** to QBO instead, don't also sync payroll from xtraCHEF.

## Automation / efficiency angles
- After each payroll run, check the Sync Monitor (Payroll filter). Green is fine, red means fix it. A quick total check (Payments vs Payroll Summary net and gross) catches most problems without a line-by-line review.
- When a new job code or earning type is created in Toast Payroll, map its GL straight away so the next payroll doesn't fail.

## Related articles
- [Sync Monitor](https://intercom.help/toast-central/en/articles/14728186-xtrachef-sync-monitor)
- [Toast Payroll: Review Payroll Reports](https://intercom.help/toast-central/en/articles/14727548-toast-payroll-review-payroll-reports)
- [Get Started With Payroll Accounting Sync](https://intercom.help/toast-central/en/articles/14728359-get-started-with-payroll-accounting-sync)
- [Manage the Payroll Accounting Sync](https://intercom.help/toast-central/en/articles/14728361-manage-the-payroll-accounting-sync)
- [Pay Group Assignment Email](https://intercom.help/toast-central/en/articles/14488040-xtrachef-pay-group-assignment-email)
