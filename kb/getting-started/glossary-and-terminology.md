---
title: "xtraCHEF: Glossary and Terminology"
source: https://intercom.help/toast-central/en/articles/14487632-xtrachef-glossary-and-terminology
last_updated: 2026-07-07
area: getting-started
---

## What it is
The official vocabulary for xtraCHEF, grouped by module. The definitions below are paraphrased.

## When you'd use it
- To interpret any other article, or to explain terms to staff and the bookkeeper.

## Terms
**Account setup**
- **Tenant**: one xtraCHEF account. It can hold several locations.
- **Location**: a restaurant inside a tenant.
- **POS**: the Toast ordering and payment system.
- **Users**: people with access. Roles are Tenant Admin, Executive, Restaurant Manager, Restaurant User and Invoice Capture.
- **Vendors list**: vendors imported or created for the tenant.

**AP & accounting**
- **Accounting period**: the reporting timeframe, usually monthly.
- **Approvals**: hold invoices until a named user approves them.
- **Custom category**: a sub-group under a GL code for reporting. It **doesn't push to accounting**.
- **COA / GL code**: the chart of accounts and its numbered accounts (for example, 1001 – Food Purchases).
- **Class**: QBO class tracking (location, department and so on).
- **Credit memo**: a vendor credit for wrong, spoiled, short or unordered items, or a price error.
- **EDI**: an electronic invoice feed from a vendor, with no upload needed.
- **Exceptions**: missing invoice fields that block reconciliation until fixed.
- **Extract**: revenue, expense or payroll data sent to the accounting system.
- **Map Invoice Items**: the reconciliation step that assigns line items to a GL code or category.
- **Journal entry, line items, receipt, invoice, statement**: standard meanings.
- **Reconciliation**: the invoice workflow. Clear exceptions and map items, then the invoice reconciles and extracts.
- **Rejected invoice**: missing too much information, or the image is unreadable.
- **Sync**: automatic transfer of revenue, expenses and payroll.

**Item Library**
- **Close watch item**: an item with volatile pricing (avocados, for example) flagged for review.
- **Item number/code**: the vendor SKU.
- **Pack / Size / Unit / UOM / Item UOM**: the packaging fields. In "case of 12 × 750 ml", UOM = Case, Pack = 12, Size = 750, Unit = ml, Item UOM = Bottle (the count unit).
- **Products**: ingredient or inventory groupings of similar invoice items.
- **Product catalog**: all captured invoice items (**Item library > View products**).
- **Purchase unit**: by weight, by volume or by each.

**Inventory**
- **Areas / secondary areas**: count locations (Walk-in > Top Shelf).
- **Beginning / ending inventory**: the start value equals the prior period's end value. The ending value is calculated when a count is submitted.
- **Count lists**: what to count and where. They're **Published** (ready) or **Unpublished** (grey, in progress).
- **PAR level**: minimum stock plus a buffer.
- **Schedule**: when a count list is open for counting.
- **Variance**: the change between beginning and ending inventory, in $ and %.

**Recipe**
- **Prime cost**: the costed recipe and plate for a menu item.
- **Published / unpublished recipe**: whether it's available for Product Mix Mapping.
- **Recipe costing**: ingredient and labor cost compared with sale price.
- **Variance (recipe)**: the change in prime cost as purchase prices move.

**Reporting**
- **AvT (Actual vs. Theoretical)**: counted usage compared with theoretical usage from sales. It shows waste, theft and shrink.
- **Analytics**: quick-view data sets.
- **COGS**: beginning inventory + purchases − ending inventory. Needs COGS mapping. **Doesn't affect accounting.**
- **DSR**: the Daily Sales Report in the mobile app.
- **Declining budget**: sales compared with COGS, showing spend remaining against a cost % goal.
- **Depleting inventory**: consumption from sales. Needs recipe mapping and at least one count.
- **Inventory Analytics**: the page holding AvT and Depleting Inventory.
- **Margin, P&L, bottom line, price fluctuation**: standard meanings.
- **Operating Summary**: a mini P&L.
- **PMIX**: menu item sales ranking with cost and price.
- **Reporting**: CSV-downloadable cost, accounting and operations reports.

## Rules, limits & gotchas
- Custom categories and COGS groups are xtraCHEF-only reporting layers. Only GL codes reach QBO.

## Automation / efficiency angles
- Use these exact terms when searching the help center or briefing an agent. "Action Needed" and "Exceptions" refer to the same thing.

## Related articles
- [Levels of Reporting](https://intercom.help/toast-central/en/articles/9307954-xtrachef-levels-of-reporting)
- [Introduction to Reporting and Analytics](https://intercom.help/toast-central/en/articles/14727505-xtrachef-introduction-to-reporting-and-analytics)
- [Review Reports in the Reporting Module](https://intercom.help/toast-central/en/articles/14727530-xtrachef-review-reports-in-the-reporting-module)
- [xtraCHEF 101](https://intercom.help/toast-central/en/articles/14727601-xtrachef-101)
