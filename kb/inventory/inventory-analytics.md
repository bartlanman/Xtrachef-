---
title: "xtraCHEF: Review Inventory Analytics"
source: https://intercom.help/toast-central/en/articles/14727647-xtrachef-review-inventory-analytics
last_updated: 2026-04-22 (date shown on article)
area: inventory
---
## What it is
Inventory Analytics has two reports built from counts, Toast sales and recipes.
- **Actual vs Theoretical Analysis** compares what you should have used (recipes × items sold) with what you actually used (counts and purchases), and shows the variance.
- **Depleting Inventory** estimates current on-hand stock from the last count, purchases, waste and theoretical usage, then compares it to PAR to suggest a **To be ordered** quantity.

## When you'd use it
- After every count cycle, to find shrink, over-pouring, waste or theft (variance).
- Between counts, to see roughly what's on hand and what to order without counting again.
- To audit whether recipes and PMIX mapping are set up correctly. Bad setup shows up as odd theoretical numbers.

## How to do it
**Prerequisites:** submitted inventory counts, recipes, and completed product mix mapping.

**Run either report**
1. Go to **Reporting** and scroll to the **Inventory** section.
2. Pick **Actual vs theoretical** or **Depleting inventory**.
3. Choose a start date and an end date. Only dates with a submitted count can be selected. Opening inventory comes from the **From** date's count and closing inventory from the **To** date's count.
4. When asked how to treat purchases and sales, choose whether to include them starting from the start date or from the end date.
5. Click **Submit**.

**Actual vs Theoretical**
- Use the **Cost** / **Quantity** slider to switch views. Scroll sideways for more columns, including a unit price column.

**Depleting Inventory**
- Use the **All** / **PAR Level** slider to switch views.

## Settings, options & permissions
- No roles are stated in the article. PAR levels are set per product on each count list (Inventory Configuration).

## Rules, limits & gotchas
- **Theoretical consumption** = recipe quantity × units sold, at current ingredient cost, assuming perfect portions and zero waste. Example from the article: 100 avocado toasts × 1 avocado = 100 avocados.
- **Actual consumption** = opening count + purchases − closing count. Example: 50 + 100 − 60 = 90.
- **Variance** = actual − theoretical. Causes include waste, portioning, theft, unrung sales and counting errors. Actual is usually higher than theoretical. (The article's example labels its variance "10", but by its own formula 90 − 100 = −10. Watch the sign when reading it.)
- **Wastage** is whatever was logged through **Inventory > Manage Waste**. Logging waste pulls known losses out of the unexplained variance.
- Depleting Inventory definitions:
  - Inventory on hand = opening + purchases − wastage − theoretical consumption.
  - PAR = the target stock level, set on count lists.
  - To be ordered = the gap between PAR and on hand.
- **Troubleshooting theoretical numbers** (they come entirely from recipes linked to Toast items through **Pair with Toast menu item** or PMIX mapping):
  1. Look for **alert icons** in the AvT report. They flag products not used in any recipe, or recipes not linked to a menu item. Zero theoretical can also just mean no sales in that window.
  2. Check the recipe's UOMs and quantities. Search a product in the recipe search bar to find every recipe that uses it. If the ingredient price is wrong, fix the item units in the Item Library.
  3. Check any prep recipes nested inside the recipe the same way.
  4. Check the products, measurements and UOMs on mapped modifiers.
- **Troubleshooting actual numbers:** these come only from counts. Look for mis-keyed or skipped items in the opening and closing counts.

## Automation / efficiency angles
- **Draft beer variance:** with pour recipes (for example a 16 oz pour of a keg product) mapped to Toast draft items and their size modifiers, AvT by keg product shows ounces lost to foam, comps and spillage. Log a blown or dumped keg in Manage Waste so it doesn't land in variance.
- Run AvT on a fixed cadence (weekly or each period close) using the same day-of-week counts. An agent can pull the top 10 variance products by cost and send them to the KM and bar manager.
- Use Depleting Inventory with PARs as a between-count order guide, especially for high-turn items (fryer oil, buns, popular guest kegs).
- Treat any **alert icon** as a setup task: every product should be in a recipe, and every sold menu item should be mapped.

## Related articles
- Get Started With Actual vs. Theoretical Analysis Reports: https://intercom.help/toast-central/en/articles/9309126-xtrachef-get-started-with-actual-vs-theoretical-analysis-reports
- Manage Waste: https://intercom.help/toast-central/en/articles/14727686-xtrachef-manage-waste
- Introduction to Reporting and Analytics: https://intercom.help/toast-central/en/articles/14727505-xtrachef-introduction-to-reporting-and-analytics
- Train on Advanced Inventory: https://intercom.help/toast-central/en/articles/14487654-xtrachef-train-on-advanced-inventory
- Recipe - Product Mix Mapping: https://intercom.help/toast-central/en/articles/14727592-xtrachef-recipe-product-mix-mapping
- Video walkthrough: https://play.vidyard.com/Nd19xhV2r6RBXL2RriQFfR
