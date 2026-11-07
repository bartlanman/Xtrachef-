---
title: Match Toast Payroll Categories to Your Accounting System's GL Codes
source: https://intercom.help/toast-central/en/articles/14412156-match-toast-payroll-categories-to-your-accounting-system-s-gl-codes
last_updated: 2026-06-04
area: quickbooks
---
## What it is (2-4 sentences)
A mapping cheat sheet showing which QuickBooks account type each Toast Payroll category (from the **Payroll Summary** report) should be mapped to when syncing payroll journal entries. It covers earnings, deductions, employee taxes, employer taxes, other expenses and payments, with example GL names. It's a reference, not a procedure.

## When you'd use it
- During Payroll Accounting Sync onboarding (Toast Web) or xtraCHEF Payroll Mapping, when assigning a GL to every payroll line.
- When a new earning/deduction appears and the sync asks you to "Assign a GL".
- When reviewing with your CPA whether payroll is hitting the right accounts.

## How to do it (numbered steps with exact menu paths, button and field names)
The article itself has no click-path; apply the table on **Finance > Accounting > Payroll assignments** (Toast Web) or **gear icon > Payroll setup > Payroll mapping** (xtraCHEF).

Key definitions: **Pay group** = employees run together in one payroll per cycle; **Location** = a business site (in QBO, a location corresponds to an account); **GL code** = numeric account ID; **Payroll journal entry** = what's posted to the QBO GL; **Account type** = QBO classification; **Chart of accounts** = QBO account list.

Mapping table (Toast category → QBO account type → example GL):
**Earnings**
- Regular, Salary, Overtime, etc. → Expense → Wages / Salary / Payroll
- Tips Owed, Gratuity Owed → Other Current Liability → Tips / Gratuity
- Tip Makeup → Expense → Wages / Payroll

**Deductions**
- 401(k) – Non-Vestwell → Other Current Liability → 401K
- Garnishment – No Vendor Set Up → Other Current Liability → Employee Tax Levy & Loan, Alimony
- Garnishment – Vendor Set Up in Toast Payroll → Bank
- Child Support – No Vendor Set Up → Other Current Liability → Child Support Garnishments
- Child Support – Vendor Set Up in Toast Payroll → Other Current Liability
- HSA/Medical – Vendor Not Paid By Toast → Other Current Liability → Insurance
- SimplyInsured → Bank → Insurance
- Benefits/Dental/Medical/Vision → Expense → Insurance
- Life Insurance → Expense → Life Insurance

**Taxes Paid (employee withholdings)** — all → Bank (operating account): State Withholding, SDI Withholding, Medicare, Federal Income Tax, FICA, Employee Taxes Deducted, Additional Medicare.

**Employer Tax Expense** → Expense: Employer FICA, Employer Taxes, FUTA – FED, SUTA.

**Other Expenses** (tax corrections, stop payments, setup fees, shipping, software) → Expense: Monthly SaaS Fees (Payroll Service / Software), Shipping Fee (Postage / Payroll Service).

**Payments** → Bank: Checks, Direct Deposit (incl. Toast Pay Card), Fees.

## Settings, options & permissions (which roles can do it)
- Mapping happens in the Payroll Accounting Sync (requires 8.1 Financial Accounts + HR+) or in xtraCHEF Payroll setup.
- Categories are driven by the Toast Payroll **Payroll Summary** report.

## Rules, limits & gotchas (sync errors, mapping rules, what syncs vs what doesn't, timing)
- Taxes withheld and paid by Toast map to **Bank** because Toast withdraws them from your bank — this is what lets the QBO bank feed match.
- Avoid mapping payroll to AP/AR accounts; QBO will then require a vendor/customer name and error otherwise.
- Article doesn't explain how to create GLs in QBO; a "setup feed" typo means "setup fee".

## Automation / efficiency angles
- Turn this table into a one-time mapping worksheet with your bookkeeper: list every line from the latest Payroll Summary, assign the Basic City GL, then bulk-apply.
- Because withdrawals map to Bank, the QBO bank feed can be matched (not added) — instruct the bookkeeper to **Match**, never **Add**, payroll withdrawals to avoid doubling expenses.
- Revisit mapping whenever a new deduction/benefit (e.g., a new 401k provider) is added in Toast Payroll.

## Related articles (links)
- [Toast Payroll: Payroll Summary Report](https://intercom.help/toast-central/en/articles/14728259-toast-payroll-payroll-summary-report)
- [Toast Payroll: Wage Garnishments FAQ](https://intercom.help/toast-central/en/articles/14486902-toast-payroll-wage-garnishments-faq)
- [Toast Payroll: Configure Vendors](https://intercom.help/toast-central/en/articles/14725459-toast-payroll-configure-vendors)
- [Toast Payroll: Get Started With Deduction Codes](https://intercom.help/toast-central/en/articles/14726163-toast-payroll-get-started-with-deduction-codes)
- [Toast Payroll: Prepare to Run Payroll](https://intercom.help/toast-central/en/articles/14725377-toast-payroll-prepare-to-run-payroll)
- [Get Started With Payroll Accounting Sync](https://intercom.help/toast-central/en/articles/14728359-get-started-with-payroll-accounting-sync)
