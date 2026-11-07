---
title: "xtraCHEF: COGS Mapping"
source: https://intercom.help/toast-central/en/articles/14727476-xtrachef-cogs-mapping
last_updated: 2026-04-22
area: cogs
---

## What it is
COGS in xtraCHEF is reported by **COGS Group** (for example, Food, Beer, NA Beverage, Supplies). Each group links **sales categories** (from Toast) to **purchase categories** (in xtraCHEF), so purchases and sales of the same type line up. COGS = Beginning Inventory + Purchases − Ending Inventory. **This is reporting only. It doesn't post anything to QuickBooks or any accounting platform.**

## When you'd use it
- During initial setup, before the COGS report can work.
- Whenever a new Toast sales category or a new purchase category is added.

## How to do it
**Map sales categories**
1. Go to **gear icon > Sales setup** (near the bottom), then **Sales mapping**.
2. Wherever the COGS column says **Select COGS**, choose a COGS group from the drop-down. For example, Appetizers maps to the Food Supply Cost group.
3. Click **Save** once every sales category is mapped.

**Map purchase categories (one at a time)**
1. Go to **gear icon > Purchase Categories**.
2. Click the category row to highlight it, then click **Edit Category**.
3. Choose the **COGS Group** and check **Include for COGS**.
4. Click **Save**.

**Map many purchase categories at once**
1. Check the box next to each category.
2. Click **Action > Edit COGS Mapping**, choose the group, and click **Save**.

## Settings, options & permissions
- Default COGS groups exist, and you can create custom ones (see Add and Edit COGS Groups).
- No roles or tier are listed.

## Rules, limits & gotchas
- A purchase category without **Include for COGS** checked is left out of COGS entirely. Use this deliberately for non-COGS spend such as repairs or utilities.
- Unmapped sales categories mean no sales for that group, which inflates or distorts COGS %.
- New Toast sales categories show up as **Select COGS** and need mapping, so check after any menu restructure.

## Automation / efficiency angles
- Use bulk **Action > Edit COGS Mapping** during setup to map dozens of purchase categories in one pass.
- Suggested group structure for a brewery/restaurant: Food, Draft Beer (house), Packaged Beer, Guest Beer/Wine/Spirits, NA Beverage, Merchandise, To-Go/Paper. Map Toast sales categories to match, so COGS % per group is meaningful.
- After every Toast menu change, open Sales mapping and look for **Select COGS** lines.

## Related articles
- [COGS Report](https://intercom.help/toast-central/en/articles/14727521-xtrachef-cogs-report)
- [Add and Edit COGS Groups](https://intercom.help/toast-central/en/articles/14728289-xtrachef-add-and-edit-cogs-groups)
- [Map Invoice Items](https://intercom.help/toast-central/en/articles/14727558-xtrachef-map-invoice-items)
- [Sync With Toast Web](https://intercom.help/toast-central/en/articles/14727574-xtrachef-sync-with-toast-web)
- [Chart of Accounts](https://intercom.help/toast-central/en/articles/14727682-xtrachef-chart-of-accounts)
- Video: https://play.vidyard.com/inNjVuJ2keSwtJVfNeVADo
