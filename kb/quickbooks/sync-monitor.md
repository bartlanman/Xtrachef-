---
title: "xtraCHEF: Sync Monitor"
source: https://intercom.help/toast-central/en/articles/14728186-xtrachef-sync-monitor
last_updated: 2026-07-07
area: quickbooks
---
## What it is (2-4 sentences)
The Sync Monitor is xtraCHEF's calendar hub for data coming in from Toast (sales, payroll) and going out to QuickBooks as journal entries. It also records events, goods adjustments, and closing inventory used by COGS reporting. Color coding shows what synced, failed, or isn't configured to sync.

## When you'd use it
- Daily check of sales JE sync status; resync failed days.
- Entering closing inventory at period end for the COGS report.
- Annotating unusual days (festivals, snowstorms, buyouts).

## How to do it (numbered steps with exact menu paths, button and field names)
- Open **Sync Monitor** (left nav). Colors: **green check** = synced to accounting; **red X** = failed; **gray** = in xtraCHEF but not set to sync.
- Default = current month, first location. **Location** drop-down (one at a time); arrows / **month** drop-down for dates; **Show All** filter: Sales, Payroll, Events, Errors, Goods adjustments, Closing inventory.
- **Notifications** (red dot when items need review). **Actions**: Sync Sales from POS, Event, Sales entry, Goods adjustment, Closing inventory.

**Event**: Actions > Event → title (required), date, time → **Add event** (click to edit/delete).
**Closing inventory**: Actions > Closing inventory → date → values by **COGS group** → **Save**. Or from **Inventory > Reports > Inventory by COGS** → **Post to Sync Monitor**.
**Goods adjustment**: Actions > Goods adjustment → date → Goods in (transfers/receipts) or Goods out (transfers/waste).
**View audit**: Actions > View audit → **Sales** tab (who changed what, when).
**Resync a failed day**: click the date for the reason (e.g., GL not found in QB) → fix (rename GL in xtraCHEF or add matching GL in QB) → **Actions > Sync to QuickBooks**.
**Multiple dates**: Actions → **Sync Sales from POS** or **Sync Sales to Quickbooks** → range up to **7 days** → **Sync** (takes a few minutes).
**Payroll**: click payroll date → payroll link → **Action**: View Audit, **Export To CSV**, Sync to QuickBooks (QBO) or **Download QuickBooks Desktop IIF File** (Desktop).

## Settings, options & permissions (which roles can do it)
- Payroll requires Toast Payroll integration + Payroll Setup.

## Rules, limits & gotchas (sync errors, mapping rules, what syncs vs what doesn't, timing)
- Closing inventory must be on the **last day of the accounting period** to count in COGS; it becomes next period's opening.
- Goods adjustments are xtraCHEF reporting only — never sync to accounting.
- Multi-date sync max 7 days per run.
- Legacy payroll via Sync Monitor unsupported for new customers since March 2026.

## Automation / efficiency angles
- Daily: filter **Show All → Errors** for the month; zero errors = done.
- Month-end: post closing inventory from the Inventory by COGS report (no retyping).
- Log events (e.g., brewery festivals, releases) so later sales/COGS swings are explainable.
- Export payroll JE to CSV for the bookkeeper's reconciliation.

## Related articles (links)
- [xtraCHEF: Get Help With Sales Syncs to QuickBooks](https://intercom.help/toast-central/en/articles/14728156-xtrachef-get-help-with-sales-syncs-to-quickbooks)
- [xtraCHEF: Integrations and Data Exchanges](https://intercom.help/toast-central/en/articles/14727658-xtrachef-integrations-and-data-exchanges)
- [Get Started With Payroll Accounting Sync](https://intercom.help/toast-central/en/articles/14728359-get-started-with-payroll-accounting-sync)
- [Manage the Payroll Accounting Sync](https://intercom.help/toast-central/en/articles/14728361-manage-the-payroll-accounting-sync)
- [xtraCHEF: COGS Report](https://intercom.help/toast-central/en/articles/14727521-xtrachef-cogs-report)
