---
title: "xtraCHEF: Resolving Unmatched Deposits"
source: https://intercom.help/toast-central/en/articles/15705519-xtrachef-resolving-unmatched-deposits
last_updated: 2026-09-23
area: accounting
---

## What it is
This explains why the daily sales journal entries (JEs) xtraCHEF posts often don't match the credit card deposits in your bank feed or QuickBooks, and gives three ways to fix it. xtraCHEF posts one JE per business date, based on what sold in that 24-hour period. Toast deposits can combine more than one business day.

## When you'd use it
- A QBO bank-feed deposit won't match a single xtraCHEF sales JE.
- The undeposited or bank account balance drifts because deposits cover several days.
- After a day when a POS terminal was offline at close-out.
- When you're setting up sales sync for the first time. Choosing the clearing-account design up front avoids the problem entirely.

## Root causes
1. **Timing/batching**: Toast sometimes settles several days of card sales in one deposit. A manual batch capture run during open hours also shifts the deposit schedule.
2. **Offline terminal at close**: if a terminal was offline when the day closed, Toast often rolls those transactions into the next day or days.

## How to do it

### Option 1 (preferred): stop mid-day manual batching
1. Find out whether staff are triggering a manual credit card batch or capture during service.
2. Ask Toast Support to reduce or restrict that capture permission, called **CLOSE_OUT_DAY_BIT**, so capture only happens once the sales day is done.
3. The Toast article "Deposit Schedules Overview" (support.toasttab.com) explains how manual capture changes deposits.

### Option 2: use a Cash Clearing GL account (best structural fix)
A clearing account goes by several names: wash account, due to/due from, or funds in transit. It's a balance-sheet holding account where money sits until it's moved to its final account.
1. In QBO, create a balance-sheet account such as "Toast CC Clearing".
2. In xtraCHEF, go to **gear icon > Sales Setup > Sales mapping > Payments** tab. Map the credit card payment types to the clearing GL instead of the bank GL, then **Save**.
3. Each daily sales JE now debits the clearing account for that business date's expected Toast card total.
4. When the real deposit lands in the bank, transfer exactly that amount from the clearing GL to the bank GL. In QBO, categorize the bank-feed deposit to the clearing account.
5. Watch the balance. It should net toward zero and normally hold only 1–3 days of in-transit card money.
- **Pro tip**: create a QBO bank rule that automatically categorizes all Toast card deposits to the clearing GL.
- Do the same for third-party delivery payouts (UberEats, Grubhub, DoorDash), with a separate clearing account per provider so each liability can be tracked.

### Option 3: manually split batched deposits
1. In QBO, confirm the deposit's settled date and exact amount.
2. In Toast Web, go to **Reports > Payments > Payout Overview**.
3. Filter a wide date window around the deposit. For a problem on 5/18, use 5/15–5/22.
4. For each deposit, note its total, its settlement date and which sales dates it covers. Example from the article: a $10,851.38 deposit settled 5/18 covered 5/16 and 5/17 sales, and a $7,025.68 deposit settled 5/19 covered 5/17.
5. In xtraCHEF, open **Sync Monitor**, pick the sales date, then **View Details > Show Sync Entries**, and read the Credit Card Deposit line. In the example, 5/16 JE = $10,896.38 and 5/17 JE = $6,980.68. Repeat for each date.
6. Calculate the variance (deposit minus JE). $7,025.68 − $6,980.68 = $45.00, so the 5/19 deposit held $45 that belongs to 5/16. Check Payout Overview for refunds that explain any variance. The example showed $45 in refunds on the 5/18 payout.
7. In QBO, split the 5/19 deposit into two lines ($6,980.68 and $45.00). Match the $6,980.68 line to the 5/17 JE. Apply the $45.00 to the 5/18 deposit so it totals $10,896.38 and matches the 5/16 JE.
- **Gotcha**: the article's own arithmetic for 5/16 is shown as "-.45", but $10,896.38 − $10,851.38 is $45.00. Always do the arithmetic yourself.

## Settings, options & permissions
- Clearing GL mapping is set in **Sales Setup > Sales mapping** (Payments tab). That needs access to Sales Setup, normally a Tenant Admin.
- Changing CLOSE_OUT_DAY_BIT is a Toast POS permission change made through Toast Support.

## Rules, limits & gotchas
- xtraCHEF JEs are by **business date**. Toast deposits are by **settlement**. A 1:1 match is not guaranteed.
- Refunds and offline-terminal days are the usual sources of small variances.
- If the clearing account holds more than about 3 days of funds, something is unmatched or a JE is missing. Check Sync Monitor for failed syncs.
- The Payment Fees and MCA Repayment lines in the JE also affect net deposit amounts. Confirm they're mapped correctly.

## Automation / efficiency angles
- For Basic City: use Option 2 plus a QBO bank rule ("Toast" + deposit → Toast CC Clearing). Deposits then never need manual matching, and reconciliation becomes a weekly check that the clearing balance is about 1–3 days of card sales.
- A weekly agent check could pull the clearing account balance from QBO and compare it to the last 3 days of card sales in the xtraCHEF Sync Monitor JEs. Anything above that threshold gets flagged.
- Set up DoorDash, UberEats and Grubhub clearing accounts at the same time, with their own bank rules.
- For leftover mismatches, export Payout Overview for the week and line it up against the Sync Monitor CC Deposit amounts in a spreadsheet to find split deposits in bulk.
- Restrict manual batch capture on the taproom POS so bar staff can't batch mid-shift.

## Related articles
- [Sales Setup](https://intercom.help/toast-central/en/articles/14727468-xtrachef-sales-setup)
- [Sync Monitor](https://intercom.help/toast-central/en/articles/14728186-xtrachef-sync-monitor)
- [Get Help With Sales Syncs to QuickBooks](https://intercom.help/toast-central/en/articles/14728156-xtrachef-get-help-with-sales-syncs-to-quickbooks)
- [Reconcile Toast Payroll Data](https://intercom.help/toast-central/en/articles/14725454-xtrachef-reconcile-toast-payroll-data)
- [Help Center: xtraCHEF by Toast](https://intercom.help/toast-central/en/articles/14486883-help-center-xtrachef-by-toast)
