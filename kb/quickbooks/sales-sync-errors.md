---
title: "xtraCHEF: Get Help With Sales Syncs to QuickBooks"
source: https://intercom.help/toast-central/en/articles/14728156-xtrachef-get-help-with-sales-syncs-to-quickbooks
last_updated: 2026-07-07
area: quickbooks
---
## What it is (2-4 sentences)
How to read and resolve alerts on daily sales journal entries that xtraCHEF posts from Toast to QuickBooks, using the **Sync Monitor**. Sales syncs depend entirely on Sales Setup mapping; bad or missing mapping shows as red-dot alerts. It also shows how to view and edit a day's sales journal entry (e.g., to add off-POS sales).

## When you'd use it
- A red dot appears on a Sync Monitor day.
- You need to add food truck / festival / off-POS sales to a day's JE.
- Checking what a day's sales JE contained.

## How to do it (numbered steps with exact menu paths, button and field names)
**Resolve alerts**
1. Left nav **Sync Monitor**; review daily sales pulled from Toast Web.
2. A **red dot** in a day's corner = alert; fix promptly.
- **GL Mapping Needed** → a sales line has no GL → map it in Sales Setup.
- **Business Validation Error** → line mapped to an AP or AR GL (not supported) → choose another GL or change the account type in QB.
- **The data is modified after the previous sync** → Toast data changed after that day synced → check the numbers; re-upload the JE if needed.
- **The account does not exist in QuickBooks** → GL removed in QB before remapping → reassign lines to a current GL.
- **Journal out of balance** → an open check/item in Toast POS for that date → close/reconcile it in POS, re-sync the day.
- **Object not found** → line mapped to an inactive QB GL → use an active GL.
- Other (e.g., unmapped headers) → support@xtrachef.com.

**View a JE**: click the calendar day → **Sales** link. Sections: Sales Categories/Revenue Center, Service Charges, Tips, Discount, Tax, Payments, Payments Fees, Deferrals, Refunds — each with debit/credit.

**Edit a JE**
1. Switch from **View** to **Edit** mode.
2. **+ Add adjustment** → pick adjustment type → confirm GL → enter **Debit** or **Credit**.
3. Usually add a matching opposite entry to keep it balanced → **Save** when balanced.

## Settings, options & permissions (which roles can do it)
- Not specified. Adjustment types can also be managed in Sales Mapping.

## Rules, limits & gotchas (sync errors, mapping rules, what syncs vs what doesn't, timing)
- Every JE must balance to post.
- AP/AR GLs are not allowed on sales lines.
- New Toast menu sales categories / tender types / discounts appear unmapped → GL Mapping Needed.
- Late Toast changes (voids, tip edits) after sync flag "data is modified".

## Automation / efficiency angles
- Daily 2-minute check: Sync Monitor current month, any red dot → fix. Add to opening manager checklist.
- Whenever Toast menu/discount/tender setup changes, immediately visit Sales Mapping to map the new lines.
- Use the JE adjustment feature for event sales taken on other systems (e.g., ticketing) so revenue lands in QBO through one path.
- Monthly: compare QBO income by account vs Toast Sales Summary for the month; differences point to failed/unsynced days.

## Related articles (links)
- [xtraCHEF: Sync Monitor](https://intercom.help/toast-central/en/articles/14728186-xtrachef-sync-monitor)
- [xtraCHEF: Sales Setup](https://intercom.help/toast-central/en/articles/14727468-xtrachef-sales-setup)
- [xtraCHEF: Get Started With QuickBooks Online Sales Syncing](https://intercom.help/toast-central/en/articles/9308304-xtrachef-get-started-with-quickbooks-online-sales-syncing)
- [Get Help With Accounting Sync](https://intercom.help/toast-central/en/articles/14412153-get-help-with-accounting-sync)
- [xtraCHEF: Sync Sales Journal Entries to Intacct](https://intercom.help/toast-central/en/articles/14727596-xtrachef-sync-sales-journal-entries-to-intacct)
