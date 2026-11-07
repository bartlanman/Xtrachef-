---
title: Manage the Payroll Accounting Sync
source: https://intercom.help/toast-central/en/articles/14728361-manage-the-payroll-accounting-sync
last_updated: "Updated over 2 weeks ago (no exact date shown; fetched 2026-11-07)"
area: quickbooks
---
## What it is (2-4 sentences)
The day-to-day guide for Toast Web's Payroll Accounting Sync to QuickBooks Online after setup. It walks through the four pages under **Finance > Accounting** (Activity, Payroll assignments, Connections, Payroll settings), manual re-syncs, the legacy xtraCHEF Sync Monitor equivalent, and a step-by-step reconciliation of synced payroll against Toast Payroll reports and QBO.

## When you'd use it
- A payroll sync failed or a new earning/deduction needs a GL.
- Changing posting date, paper check handling, or the connected QBO company.
- Monthly payroll reconciliation between Toast Payroll, the JE, and QBO.

## How to do it (numbered steps with exact menu paths, button and field names)
**Activity** (Finance > Accounting > Activity)
- Calendar of all syncs; filter by **pay group** and **location** (multi-select) upper right. Green = synced; red + red dot = failed. Banner at top when action is needed. Financial contacts get failure emails.
- **Assign a GL alert**: click the **Payroll journal** link for the Failed sync → **Assign a GL** in the pink box → on Payroll assignments find blank drop-downs ("X incomplete") → choose GL → **Save**.

**Payroll assignments**
- Pick pay group (upper right). Gear icon → Payroll settings. Blank line → **Select GL code** → or **View all GL types** → or **+ Add GL code** (creates in QBO). **Breakout by location** toggle for class users with multiple locations per pay group. Empty page = no payroll posted yet or manual sync needed.

**Connections** — tabs:
- **Connected Accounts**: status should read **Connected**; **edit pencil** connects/disconnects pay groups; **three-dot menu** reconnects (after billing lapse, QBO errors, or QBO email/password change); **Add QuickBooks Online account** for a new company.
- **GL Codes**: choose QBO account; **Show** = Active only (default) / Inactive only / All; search; edit pencil (edits in both systems); **+Add GL code**; **Sync from QuickBooks Online** pulls new GLs.
- **Classes** (only if QBO classes exist): same as GL Codes.

**Payroll settings**: choose pay group tile → **Connected account**; **Posting date** (Pay period end date / Check date — affects future only); **Paper checks** (Individual / Summary); **Sync toggle** + **Sync start date** (off = post manually).

**Manual sync — one payroll**: Activity → failed day → **View details** → **Sync to QuickBooks Online** (pick pay group on the left if several).
**Manual sync — multiple**: Activity → **Actions** → **Sync from Toast Payroll**. Locked QBO periods show failures (ignore if previously synced).

**Legacy xtraCHEF**: Sync Monitor → date with **Payroll** tag → red: read pink box, open **Payroll journal** link → fix → **Actions > Sync to QuickBooks**.

**How the money matches**: Toast makes 2–3 withdrawals (direct deposits, taxes, paper checks). They appear in the QBO **Bank Feed**; the Toast JE splits totals to GLs → click **Match** in the bank feed.

**Reconcile**
1. Totals: Sync Monitor/Activity total vs Toast Payroll **Payroll Summary** (**Payroll > Past Payrolls > View**) — use **Cash Requirements** under **Cash Flow Summary**.
2. Earnings: open the JE, expand **Earnings**, compare to **Labor distribution by job** (e.g., Server – REGULAR, Server – TIP Makeup).
3. Employee taxes: Payroll Summary **Taxes Total** vs Toast Web **Bank withdrawals > Payroll Taxes** (xtraCHEF: **Taxes Paid**).
4. Employer taxes: Payroll Summary **ER Taxes > Total** vs Toast Web Payroll Taxes expanded (xtraCHEF: **Payroll Tax Expense**).
5. In QBO: **Reports > Standard Reports** → search **Journal** (or **Recent transactions** for very recent) → filter by the sync date → review GLs and amounts.

## Settings, options & permissions (which roles can do it)
- Requires Toast Payroll + QBO; same permissions as setup (8.1 Financial Accounts, HR+).
- Typically one QBO account per FEIN/bank; multiple pay groups can share one.

## Rules, limits & gotchas (sync errors, mapping rules, what syncs vs what doesn't, timing)
- Bulk syncing many payrolls can fail on large data — review results.
- Posting date changes are not retroactive.
- Class warning: sync assumes **location→class**. If QBO classes are by job, either reorganize classes by location, switch to location tracking, or skip classes (risking errors).
- Pay groups without a Toast Web location can still connect.

## Automation / efficiency angles
- After each payroll run, check Activity for green the next morning; make Bart/bookkeeper the financial contact so failures email immediately.
- Monthly reconciliation checklist = the 5 steps above; can be scripted with the QBO connector (pull Journal report for payroll dates and compare to Toast Payroll Summary totals).
- In QBO bank feed, always **Match** payroll withdrawals to the Toast JE.

## Related articles (links)
- [Get Started With Payroll Accounting Sync](https://intercom.help/toast-central/en/articles/14728359-get-started-with-payroll-accounting-sync)
- [Get Help With Accounting Sync](https://intercom.help/toast-central/en/articles/14412153-get-help-with-accounting-sync)
- [xtraCHEF: Sync Monitor](https://intercom.help/toast-central/en/articles/14728186-xtrachef-sync-monitor)
- [xtraCHEF: Reconcile Toast Payroll Data](https://intercom.help/toast-central/en/articles/14725454-xtrachef-reconcile-toast-payroll-data)
- [Get Started With Sales Accounting Sync](https://intercom.help/toast-central/en/articles/15197015-get-started-with-sales-accounting-sync)
- [Manage Accounting Sync: Accounts Payable](https://intercom.help/toast-central/en/articles/15972248-manage-accounting-sync-accounts-payable)
