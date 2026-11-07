---
title: "xtraCHEF: COGS Report"
source: https://intercom.help/toast-central/en/articles/14727521-xtrachef-cogs-report
last_updated: 2026-07-13
area: reporting
---
## What it is (2-4 sentences)
The COGS report combines purchases, inventory change and Toast sales to show cost of goods and COGS % by COGS group, category, product and invoice item. Cost of Goods = Beginning Inventory + Purchases − Ending Inventory; COGS % = Cost of Goods ÷ Sales. (Linked from the reporting collection; documented as a related article.)

## When you'd use it
- Period-end food/beverage cost %, and finding unassigned or unmapped items that distort it.

## How to do it (numbered steps with exact menu paths, button and field names)
**Setup**
1. Accounting period for each location.
2. COGS mapping (sales categories and purchase categories → COGS groups).
3. Closing inventory on the **last day of every accounting period** in Sync Monitor — either **Reporting > Inventory > Inventory by COGS** → date/areas/count lists → **Submit** → **Post to Sync Monitor**, or **Sync Monitor > Action > Closing Inventory** → date → values → **Save**. Without it, only purchases and sales appear.

**Use**
1. **COGS** in left nav → **Location** → date range (custom or presets; no longer tied to accounting periods).
2. Comparison range is automatic (the immediately prior equal period); tiles like **Purchases** and **Inventory change** show green/red change. Inventory change blank on xtraCHEF Essentials.
3. **Columns** button to add e.g. **Gross Sales**; click headers to sort. **% of net sales** per category/product (product net sales = net sales of menu items whose recipes use it).
4. **>** icons to drill COGS group → category → product → invoice item; search bar.
5. **Unassigned** link at bottom (if any) → **Map invoice items** page → set **Category** drop-downs; link disappears when all assigned.

## Settings, options & permissions (which roles can do it)
- Not stated.

## Rules, limits & gotchas (sync errors, mapping rules, what syncs vs what doesn't, timing)
- **COGS Net Sales** column = Toast Sales Summary; the **Net Sales** drop-down reflects recipe mapping; **Unmapped** = difference (e.g., $100 beer sales, Budweiser $20 with no recipe → $20 Unmapped). Directional, not accounting-exact.
- Unassigned invoice items now count in the report (previously excluded).
- COGS in xtraCHEF never affects QuickBooks.

## Automation / efficiency angles
- Period end: post closing inventory → run COGS for the period → clear Unassigned → compare COGS % to QBO (COGS accounts ÷ income).

## Related articles (links)
- [xtraCHEF: COGS Mapping](https://intercom.help/toast-central/en/articles/14727476-xtrachef-cogs-mapping)
- [xtraCHEF: Add and Edit COGS Groups](https://intercom.help/toast-central/en/articles/14728289-xtrachef-add-and-edit-cogs-groups)
- [xtraCHEF: Sync Monitor](https://intercom.help/toast-central/en/articles/14728186-xtrachef-sync-monitor)
- [xtraCHEF: Review Reports in the Reporting Module](https://intercom.help/toast-central/en/articles/14727530-xtrachef-review-reports-in-the-reporting-module)
