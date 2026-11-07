---
title: Get Started With Payroll Accounting Sync
source: https://intercom.help/toast-central/en/articles/14728359-get-started-with-payroll-accounting-sync
last_updated: 2026-05-20
area: quickbooks
---
## What it is (2-4 sentences)
Setup guide for posting Toast Payroll journal entries to QuickBooks Online. As of spring 2026 the go-forward path is **Payroll Accounting Sync** in Toast Web (Finance > Accounting); the legacy xtraCHEF Sync Monitor payroll route is unsupported for new customers since March 2026 and existing users migrate later in 2026. The article covers both the Toast Web wizard and the legacy xtraCHEF Payroll setup.

## When you'd use it
- Basic City runs Toast Payroll and wants payroll JEs in QBO.
- Choosing posting date (cash vs accrual), paper check treatment, start date.

## How to do it (numbered steps with exact menu paths, button and field names)
**Before you start**: clean the QBO chart of accounts (deactivate unused/duplicate GLs, settle naming; have the CPA review).

**Toast Web wizard**
1. Verify access: QBO **Primary Admin**; Toast Payroll **HR+**; Toast Web **8.1 Financial Accounts**.
2. Open via **Finance > Accounting > Connections** (Toast Web), **Accounting** (Toast Payroll left rail), or **Connect to QuickBooks** on a payroll's Confirmation step.
3. Log out of all QBO sessions in every tab.
4. **Log into QuickBooks Online** → enter credentials in the pop-up (pick the company if several; disable pop-up blocker if needed).
5. Tick each pay group to connect → **Continue**.
6. Settings (apply to all pay groups/QBO accounts):
   - **Start date** — up to 1 year back; catch up older payrolls with a manual multi-sync.
   - **Posting date** — **Check date** (cash basis) or **Pay period end date** (accrual).
   - **Paper checks** — **Summary** (few paper checks) or **Individual** (track each check clearing).
7. **Continue to assignments** → map each expense/liability (Descriptions come from the latest Payroll Summary report; not editable) to a GL and class if used.
8. Nothing posts until a payroll runs after setup.

**Legacy xtraCHEF route (pre-spring-2026 customers)**
1. **gear icon > Account setup** → **Integrations** → **Connect to QuickBooks** → sign in → choose company → **Authorize** → **Continue**.
2. Complete sales data sync ("Sync GL Codes, Vendors and More") — cannot be skipped.
3. **gear icon > Payroll setup** (if missing, email support@xtrachef.com).
4. General configuration:
   - **Reporting allocation**: **Spread over pay period** (weekly average) or **Last day of pay period** (lumpy weeks on biweekly payroll).
   - **Location processing**: map each pay group to one xtraCHEF location (many groups → one location OK; one group cannot split).
5. Sync to accounting system: **Payroll sync** toggle (on), **Start date**, **Post by class**, **Journal entry posting date** (last day of pay period or check date), **Summaries** (Taxes Paid, Employer Tax Expenses, Other Expenses summarized by default; for Payments: summarize if Toast funds checks in one draw, don't if you fund each check) → **Save**.
6. **Payroll mapping**: per tab, set **GL Description**, **Class**, **Labor Group** (expense lines only). Use header checkbox + **Bulk update**; **View all GL descriptions**; **+ Add GL code** (syncs to QBO); **+ Create** labor group. **Save**. Multi-location: **Copy from** another location.

## Settings, options & permissions (which roles can do it)
- Toast Web path: HR+, 8.1 Financial Accounts, QBO Primary Admin.
- No QBO: Toast Payroll Pro GL module → export **GL by Level** report for other systems.

## Rules, limits & gotchas (sync errors, mapping rules, what syncs vs what doesn't, timing)
- Payroll Accounting Sync is QBO-only.
- Posting-date choice must match your accounting basis.
- Labor shows on Operating Summary / Prime Cost only if lines have a Labor Group (xtraCHEF route).
- Non-restaurant businesses may find the job-based Payroll Summary structure less useful.
- Don't run both routes at once — disable xtraCHEF Payroll sync if moving to Toast Web (double JEs otherwise).

## Automation / efficiency angles
- Choose **Check date** if Basic City books cash-basis, so JEs line up with bank feed withdrawals for one-click matching.
- If you keep xtraCHEF payroll for the Operating Summary's prime cost, you can still post to QBO from Toast Web — just keep xtraCHEF's posting toggle off and labor groups mapped (confirm with support that labor still feeds the Operating Summary).
- Set start date = cutover date from the previous tool to avoid duplicate historical JEs.

## Related articles (links)
- [Manage the Payroll Accounting Sync](https://intercom.help/toast-central/en/articles/14728361-manage-the-payroll-accounting-sync)
- [Match Toast Payroll Categories to GL Codes](https://intercom.help/toast-central/en/articles/14412156-match-toast-payroll-categories-to-your-accounting-system-s-gl-codes)
- [Get Help With Accounting Sync](https://intercom.help/toast-central/en/articles/14412153-get-help-with-accounting-sync)
- [xtraCHEF: Sync Monitor](https://intercom.help/toast-central/en/articles/14728186-xtrachef-sync-monitor)
- [Get Started With Sales Accounting Sync](https://intercom.help/toast-central/en/articles/15197015-get-started-with-sales-accounting-sync)
- [xtraCHEF: Set up QuickBooks Class or Location Tracking](https://intercom.help/toast-central/en/articles/14727813-xtrachef-set-up-quickbooks-class-or-location-tracking)
