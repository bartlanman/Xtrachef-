---
title: "xtraCHEF: Get Started With Inventory Reports"
source: https://intercom.help/toast-central/en/articles/9308181-xtrachef-get-started-with-inventory-reports
last_updated: 2026-04-28
area: reporting
---
## What it is (2-4 sentences)
Covers the four inventory value reports in the Reporting > Inventory section: Inventory by COGS, Inventory by GL, Inventory Summary and Inventory Variance. They show what's on the shelf in dollars, how it splits by COGS group or GL, and how it changed between counts.

## When you'd use it
- Month-end inventory valuation for the QBO inventory adjustment and the COGS report.

## How to do it (numbered steps with exact menu paths, button and field names)
**Prereqs (all 7)**: at least 20 invoices; products created; invoice items mapped to GL/categories; COGS mapping; pack/size/UOM configured; area setup + a count list; an inventory count.
1. **Inventory by COGS**: **Inventory Date** (only scheduled count dates) → **Area(s)** (**Select all**) → **Count List(s)** (**Select all**) → **Submit**. Output: $ and **Value %** per COGS group. **Excel** export. (Also has **Post to Sync Monitor** for COGS closing inventory.)
2. **Inventory by GL**: same inputs. $ and **Value%** per GL; drill GL → category → invoice item → area. **Excel**.
3. **Inventory Summary**: one **Inventory date** → **Submit**; all locations; **Beginning inventory** (= prior ending) and **Ending inventory**. **Excel**.
4. **Inventory Variance**: pick two prior inventory dates → **Submit**; summary then drill into areas, count lists, items; **fluctuation** column = $ and % change. No export mentioned.

## Settings, options & permissions (which roles can do it)
- Not stated (inventory is a Pro feature).

## Rules, limits & gotchas (sync errors, mapping rules, what syncs vs what doesn't, timing)
- Only dates with counts are selectable.

## Automation / efficiency angles
- Month-end: run Inventory by GL on the last-day count, export to Excel, and hand the GL totals to the bookkeeper for the QBO inventory-asset adjusting entry; also **Post to Sync Monitor** from Inventory by COGS so xtraCHEF COGS uses the same number.
- Inventory Variance between consecutive counts flags fast movers / possible shrink.

## Related articles (links)
- [xtraCHEF: Levels of Reporting](https://intercom.help/toast-central/en/articles/9307954-xtrachef-levels-of-reporting)
- [xtraCHEF: Inventory Counts](https://intercom.help/toast-central/en/articles/14727473-xtrachef-inventory-counts)
- [xtraCHEF: Mobile Inventory](https://intercom.help/toast-central/en/articles/14727545-xtrachef-mobile-inventory)
- [xtraCHEF: Review Reports in the Reporting Module](https://intercom.help/toast-central/en/articles/14727530-xtrachef-review-reports-in-the-reporting-module)
- [xtraCHEF: Glossary and Terminology](https://intercom.help/toast-central/en/articles/14487632-xtrachef-glossary-and-terminology)
