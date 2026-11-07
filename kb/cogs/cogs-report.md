---
title: "xtraCHEF: COGS Report"
source: https://intercom.help/toast-central/en/articles/14727521-xtrachef-cogs-report
last_updated: 2026-07-13
area: cogs
---

## What it is
The **COGS** report shows cost of goods (Beginning Inventory + Purchases − Ending Inventory) and COGS % (cost ÷ sales) by COGS group, with drill-down to category, product, and invoice item. It compares against the prior equivalent period automatically. It needs three things set up first: accounting periods, COGS mapping, and closing inventory in the Sync Monitor.

## When you'd use it
- Month-end food and beverage cost review.
- Finding what's driving a cost spike, such as a category, product, or item.
- Finding unmapped purchases or sales that distort the numbers.

## How to do it
**Setup (one-time, then every period)**
1. **Accounting periods**: create them per location (calendar or fiscal). See "Add New Accounting Period".
2. **Map COGS**: map both sales and purchase categories. Sales must be mapped for Toast sales to sync and for the report to generate.
3. **Closing inventory in Sync Monitor**: an inventory value on the **last day of the accounting period** is required. Without it the report shows only purchases and sales.
   - Automatic: go to **Reporting > Inventory > Inventory by COGS**, pick an inventory date, area(s), and count list(s), click **Submit**, then **Post to Sync Monitor**.
   - Manual: go to **Sync Monitor > Action > Closing Inventory**, pick a date, enter values, and click **Save**.

**Run the report**
1. Click **COGS** in the left nav.
2. Pick a **Location** and a date range. The custom picker has common presets, and you don't need to align to accounting periods any more.
3. The comparison range is fixed to the equivalent prior period (for example, last 4 weeks vs the 4 weeks before that). Tiles such as **Purchases** and **Inventory change** show green or red deltas.
4. Click **Columns** to add fields (for example, Gross Sales). Click a column header to sort.
5. **% of net sales** is shown per category and product. A product's net sales are the total net sales of every menu item whose recipe uses it.
6. Expand groups, categories, products, and items with the **>** icons, or use the search bar.

**Clean up unassigned items**
- If an **Unassigned** link appears at the bottom, some purchased items have no category. Click it to go to **Map invoice items** and assign categories. The link disappears once everything is assigned.

## Settings, options & permissions
- **Inventory change is blank or locked on xtraCHEF Essentials.** Full COGS with inventory needs Pro. *(Essentials shows purchases-based COGS.)*
- No roles are stated.

## Rules, limits & gotchas
- **Net Sales sources differ:** the COGS Net Sales column comes from the Toast Sales Summary, while Net Sales in the drop-down reflects recipe mapping. **Unmapped** is the gap between the two. Net sales figures are directional estimates, not accounting-grade.
- **Unmapped sales**: Toast sales for menu items with no xtraCHEF recipe show as Unmapped. For example, with $100 of beer sold, if Budweiser ($20) has no recipe, $20 is Unmapped.
- No closing inventory on the period's final day means COGS is just purchases ÷ sales, which swings with order timing.
- Invoice items without a category used to be silently excluded. Now they appear via the Unassigned link.

## Automation / efficiency angles
- **Month-end routine:** count inventory on the last day, run Inventory by COGS, click **Post to Sync Monitor**, then run COGS for the month. Use the automatic post rather than typing values in.
- Keep **Unassigned** and **Unmapped** at zero. Each one is a direct data-quality KPI.
- To shrink Unmapped, create recipes for every draft and packaged beer SKU on the Toast menu. Even simple one-ingredient recipes (a 16oz pour from a keg product) work.
- Follow up with Product Mix (margin by item) and Actual vs Theoretical (waste) if you use recipes and inventory.

## Related articles
- [COGS Mapping](https://intercom.help/toast-central/en/articles/14727476-xtrachef-cogs-mapping)
- [Add and Edit COGS Groups](https://intercom.help/toast-central/en/articles/14728289-xtrachef-add-and-edit-cogs-groups)
- [Introduction to Reporting and Analytics](https://intercom.help/toast-central/en/articles/14727505-xtrachef-introduction-to-reporting-and-analytics)
- [Review Reports in the Reporting Module](https://intercom.help/toast-central/en/articles/14727530-xtrachef-review-reports-in-the-reporting-module)
- Add New Accounting Period: https://central.toasttab.com/s/article/xtraCHEF-Add-New-Accounting-Period
- Sync Monitor: https://central.toasttab.com/s/article/xtraCHEF-Sync-Monitor#inventory
- Product Mix Report: https://central.toasttab.com/s/article/xtraCHEF-Recipe-Costing#pmr
- Actual vs Theoretical: https://central.toasttab.com/s/article/xtraCHEF-Inventory-Analytics
