# Month-end close

Order matters: purchases complete → inventory posted → COGS → tie-out to QuickBooks → close period.

1. **All invoices in.** Upload everything dated in the period, including utilities, rent and service bills (Operating Summary is only as complete as uploads). Clear every queue (see `daily.md`).
2. **All bills extracted.** Extract Monitor all green. Run **On-Demand Extract** for stragglers.
3. **All sales days posted.** Sync Monitor: no red days in the month.
4. **Final inventory count** dated the **last day of the accounting period**, then **Inventory by COGS > Post to Sync Monitor**. `kb/reporting/inventory-reports.md`, `kb/cogs/`
5. **COGS report** and **Actual vs Theoretical** (needs two counts; theoretical arrives 2–3 business days after end date). `kb/cogs/cogs-report.md`, `kb/reporting/actual-vs-theoretical.md`
6. **Tie-out to QuickBooks**:
   - **Invoice summary by GL** (xtraCHEF) vs QBO bills by vendor/GL for the same dates.
   - **Spending by GL** vs QBO P&L expense lines.
   - **Operating Summary** vs QBO P&L line by line. `kb/reporting/operating-summary.md`, `kb/reporting/profit-and-loss-statements.md`
   - Payroll: posts from Toast Web (Finance > Accounting), matched — never added — against the bank feed. `kb/quickbooks/payroll-accounting-sync-manage.md`
7. **Close the accounting period** in xtraCHEF. After close, edits to that period fail ("Account period closed") — move dates into an open period instead. `kb/accounting/accounting-periods.md`
8. Record anything learned in `memory/log.md`.

## Agent can do
Pull the xtraCHEF reports and the QBO P&L/AP via the QuickBooks connector, build the tie-out, and list every difference with its likely cause.
