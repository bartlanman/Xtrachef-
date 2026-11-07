---
title: "xtraCHEF: Sync Monitor"
source: https://intercom.help/toast-central/en/articles/14728186-xtrachef-sync-monitor
last_updated: 2026-07-07
area: sales-sync
---

## What it is
The **Sync Monitor** is a calendar showing the raw Toast sales data synced into xtraCHEF, plus the log of each **sales and payroll journal entry** sent to QuickBooks. It's also where you record events, closing inventory and goods adjustments, view audit trails, and re-sync failed days. Invoice extracts are tracked separately in the Extract Monitor.

## When you'd use it
- Every day or week, to confirm the previous day's sales JE posted.
- When a QBO deposit doesn't match.
- When re-pulling sales from Toast after menu or mapping fixes.
- At month end, for closing inventory.

## How to do it
**Navigate**: **Sync Monitor** in the left nav. It defaults to the current month and the first location.
- **Location** drop-down (one location at a time). Move between months with the arrows or the month drop-down.
- **Show All** filter: Sales, Payroll, Events, Errors, Goods adjustments, Closing inventory.

**Status colors**
- **Green ✓**: in xtraCHEF **and** synced to accounting.
- **Red ✗**: the accounting sync **failed**.
- **Gray (no icon)**: in xtraCHEF but not set to sync anywhere.

**Actions** (button at top right): Sync Sales from POS, Event, Sales entry, Goods adjustment, Closing inventory, View audit, Sync to QuickBooks.

**See the posted JE**: click a date, then the journal link. This is the JE that went to QBO. For the line detail, use **View Details > Show Sync Entries**.

**Fix a failed sales sync**
1. Click the red date to read the reason. A common one is "GL code not found in QuickBooks".
2. Fix it: rename the GL in xtraCHEF to match QBO, add the GL in QBO, or map the missing item in Sales Setup.
3. **Actions > Sync to QuickBooks**.

**Bulk re-sync**: **Actions > Sync Sales from POS** (re-pull from Toast) or **Sync Sales to Quickbooks**. Choose a range of **up to 7 days**, then click **Sync**. It can take a few minutes.

**Events**: **Actions > Event**, add a title (required), date and time, then **Add event**. Use this to mark buyouts, fundraisers, promos, storms and the like. Click an event to edit or delete it.

**Closing inventory**: **Actions > Closing inventory**, pick the date, enter values by COGS group, then **Save**. Pro users can instead go to **Inventory > Reports > Inventory by COGS**, pick a date, and click **Post to Sync Monitor**.

**Goods adjustments**: **Actions > Goods adjustment**. Use **Goods in** for transfers or receipts and **Goods out** for transfers out or waste.

**Audit**: **Actions > View audit** (Sales tab) shows manual changes and who made them.

**Notifications**: a red dot on **Notifications** means there are flagged items. Open it to see details and recommendations.

**Payroll**: requires the Toast Payroll integration and Payroll Setup. Click a payroll date, then the payroll link to open the **Payroll Journal Entry**. **Action** offers **View Audit**, **Export To CSV**, and **Sync to QuickBooks** (QBO) or **Download QuickBooks Desktop IIF File** (QBD).

## Settings, options & permissions
- Available to all roles except Invoice Capture (the "monthly calendar of sales entered" permission).

## Rules, limits & gotchas
- Closing inventory must be dated the **last day of the accounting period**, or it's left out of COGS. It becomes the next period's opening inventory.
- **Goods adjustments don't sync to accounting.** They only affect xtraCHEF reports (for example, Inventory by COGS).
- Bulk sync is capped at **7 days** per run.
- Toast also offers a direct **payroll-only** QBO sync from Toast Web. Pick one payroll route.

## Automation / efficiency angles
- **Daily check (2 min)**: open Sync Monitor and look for red on yesterday's date. Filter by **Errors** for the month to see every failure at once.
- **After any Sales Setup mapping fix**: use Sync Sales to QuickBooks in 7-day windows to backfill the failed dates.
- Log events (beer releases, festivals, private buyouts, snow closures) so sales anomalies are explained when reviewing analytics later.
- Use View Audit to check whether anyone manually edited sales before reconciling deposits.
- Month end: post closing inventory by COGS group on the last day, then pull the COGS report.

## Related articles
- [Get Help With Sales Syncs to QuickBooks](https://intercom.help/toast-central/en/articles/14728156-xtrachef-get-help-with-sales-syncs-to-quickbooks)
- [Integrations and Data Exchanges](https://intercom.help/toast-central/en/articles/14727658-xtrachef-integrations-and-data-exchanges)
- [Get Started With Payroll Accounting Sync](https://intercom.help/toast-central/en/articles/14728359-get-started-with-payroll-accounting-sync)
- [Manage the Payroll Accounting Sync](https://intercom.help/toast-central/en/articles/14728361-manage-the-payroll-accounting-sync)
- [Resolving Unmatched Deposits](https://intercom.help/toast-central/en/articles/15705519-xtrachef-resolving-unmatched-deposits)
