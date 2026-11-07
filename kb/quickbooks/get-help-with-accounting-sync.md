---
title: Get Help With Accounting Sync
source: https://intercom.help/toast-central/en/articles/14412153-get-help-with-accounting-sync
last_updated: 2026-06-11
area: quickbooks
---
## What it is (2-4 sentences)
The master troubleshooting guide for Toast's native **Accounting Sync** (Toast Web > Finance > Accounting) to QuickBooks Online, covering both payroll and sales journal entries, plus the older xtraCHEF + Toast Payroll integration. It explains missing-page permission problems, red (failed) journal entries on the Activity calendar, and a table of specific QuickBooks error messages with fixes.

## When you'd use it
- The Finance/Accounting pages don't show up in Toast Web, or Payroll's Accounting link errors out.
- A red "sync errors were found" banner or red day appears on the Activity calendar.
- A specific QBO error comes back (closed period, AP/AR needs a vendor/customer, account doesn't exist, out-of-balance journal).
- Deciding whether to move payroll posting from xtraCHEF's Sync Monitor to Toast Web's Payroll Accounting Sync.

## How to do it (numbered steps with exact menu paths, button and field names)
**Pages missing under Finance**
1. Confirm the user has Toast Web permission **8.1 Financial Accounts** AND Toast Payroll security role **HR+**.
2. QBO **Primary Admin** is only needed for the very first connection.
3. If both are in place and pages still don't show, contact Customer Care.

**Fix a red (failed) journal on the Activity calendar**
1. Click the red day on the Activity calendar.
2. In the **journal** column, click the hyperlink for the row with status **Failed**.
3. In the journal details, click **Assign a GL**.
4. On the assignments page, look for line items whose drop-down reads "Select a GL code"; each section shows an "X incomplete" count.
5. Optionally expand the journal entry details — the unassigned line is highlighted red.
6. Pick GLs and click **Save**, then re-sync.

**One pay group across many locations**
- **Finance > Accounting > Payroll assignments** → toggle **Breakout by location** on/off; switch pay groups with the top drop-down. Either way, one journal entry posts per pay group.

**Migrate payroll from xtraCHEF to Toast Web Payroll Accounting Sync (optional)**
1. xtraCHEF: **gear icon > Payroll setup > Sync to accounting system** → turn off the **Payroll sync** toggle.
2. Toast Web: **Finance > Accounting > Connections**.
3. Run the onboarding wizard (see Get Started With Payroll Accounting Sync). Requires Toast Payroll.

**Turn off payroll sync in xtraCHEF entirely**
- **gear icon > Payroll setup > Sync to accounting system** → toggle off **Payroll sync**. Sales data still flows into xtraCHEF.

## Settings, options & permissions (which roles can do it)
- Toast Web permission **8.1 Financial Accounts** + Toast Payroll role **HR+** to see/use Accounting pages.
- QBO **Primary Admin** for the initial connection only.
- All company codes in the Toast POS management group can be synced. Legacy Stratex customers not on Toast POS are not supported; if a company code has at least one Toast POS restaurant GUID, all its pay groups/locations are supported.
- xtraCHEF: **Payroll** only appears under the gear menu for Toast Payroll customers (otherwise ask Customer Care to connect them).

## Rules, limits & gotchas (sync errors, mapping rules, what syncs vs what doesn't, timing)
Error → cause → fix (X = a specific account/vendor/etc.):
- "Journal Sync Failed. Please try again to Sync to QuickBooks Online." → generic, often too much data at once → sync each instance separately or do a manual sync.
- Journal entry matched to a bank transaction in QBO → QBO blocks editing matched entries → unmatch in QBO Bank Transactions, then manually re-sync from Toast.
- "Account X does not exist in QuickBooks." → GL deleted/inactivated in QBO → reassign lines to another GL, manual sync.
- Subscription ended/canceled/billing problem → QBO account inactive → fix with Intuit.
- "The accounting period has closed. Txn date=… is before book closing date=…" → books closed → unlock/open the period in QBO, then post.
- "Business Validation Error: When you use Accounts Payable, you must choose a vendor in the Name field." → AP GL needs a vendor → set vendor on the **GL Assignments** page.
- "Business Validation Error: When you use Accounts Receivable, you must choose a customer in the Name field." → AR GL needs a customer → set customer on **GL Assignments** (article text mistakenly says vendor).
- "Customer X configured for the GL X is not available in QuickBooks." / "Vendor X configured…" → that name no longer exists → choose another on GL Assignments.
- "Warning - Class X is not available in QuickBooks." → class deleted → remove/change class on GL Assignments.
- "Assign a GL to the new categories found to successfully sync to QuickBooks." → new earning/deduction created in Toast Payroll → map it on Payroll assignments.
- "You and X were working on this at the same time…" → only one editor per transaction → coordinate, retry from Activity.
- Journal entry deleted in QBO → syncing will post a fresh entry (decide to post or close).
- Journal entry edited in QBO → re-syncing overwrites those edits (verify first).
- "Payroll journal is out of balance." → system error → manual resync; if it persists, Customer Care.
- "Sales journal is out of balance." → usually **unpaid/open orders** → find them on the Sales Summary report for that business date; apply payment/discount or void.
- Payroll mapped to an AP or AR GL will prompt for a vendor/customer — payroll normally belongs on expense or liability GLs.
- Prime Cost labor only appears on the xtraCHEF Operating Summary after labor groups are assigned.

## Automation / efficiency angles
- Make the Activity calendar a daily/weekly checkpoint: any red day = action. Financial contacts get failure emails — make sure the right bookkeeper inbox is the financial contact.
- Keep a "do-not-touch" rule in QBO: don't edit or delete Toast-posted journal entries; fix at the source in Toast and re-sync (edits get overwritten, deletes get re-posted).
- Close-month checklist: before locking the QBO period, confirm every day in the month is green; otherwise late syncs will fail with the closed-period error.
- For Basic City (recently switched from another tool): check the old tool's posting is shut off so you don't double-post sales/payroll JEs alongside Toast's.
- Out-of-balance sales journals are an early warning of open checks in Toast — have managers close all checks nightly.

## Related articles (links)
- [Get Started With Payroll Accounting Sync](https://intercom.help/toast-central/en/articles/14728359-get-started-with-payroll-accounting-sync)
- [Manage the Payroll Accounting Sync](https://intercom.help/toast-central/en/articles/14728361-manage-the-payroll-accounting-sync)
- [Get Started With Sales Accounting Sync](https://intercom.help/toast-central/en/articles/15197015-get-started-with-sales-accounting-sync)
- [Get Started With Accounting Sync: Accounts Payable](https://intercom.help/toast-central/en/articles/15972247-get-started-with-accounting-sync-accounts-payable)
- [Manage Accounting Sync: Accounts Payable](https://intercom.help/toast-central/en/articles/15972248-manage-accounting-sync-accounts-payable)
- [Match Toast Payroll Categories to GL Codes](https://intercom.help/toast-central/en/articles/14412156-match-toast-payroll-categories-to-your-accounting-system-s-gl-codes)
- [xtraCHEF: Operating Summary](https://intercom.help/toast-central/en/articles/14728290-xtrachef-operating-summary)
