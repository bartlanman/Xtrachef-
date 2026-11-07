---
title: "xtraCHEF: Recipe - Product Mix Mapping"
source: https://intercom.help/toast-central/en/articles/14727592-xtrachef-recipe-product-mix-mapping
last_updated: 2026-07-07 (date shown on article)
area: recipes
---
## What it is
Product Mix (PMIX) Mapping links each synced Toast **menu item** to an xtraCHEF **Recipe**, and each Toast **modifier** to a **Product** or **Prep Recipe** with a measurement. Until mapping is done, the **Product Mix Report**, **Actual vs Theoretical** and **Depleting Inventory** reports stay empty.

## When you'd use it
- After building recipes, so sales can drive theoretical usage.
- Whenever menu items or modifiers are added in Toast (new beer on tap, new burger add-on).
- For modifiers that add or remove ingredients (add bacon, no cheese), and for size modifiers (pour sizes).

## How to do it
**Prerequisites:** the Toast POS integration is syncing menu and modifier data, and recipes and prep recipes exist.

Go to **Recipe > Product Mix Mapping**. You'll see **Menu Item Mapping** and **Modifiers Mapping**.

**Menu items**
1. Open **Menu Item Mapping**. All menu items are listed.
2. Choose the matching recipe in the **Recipe** field.
3. Click the **green checkmark** to save. On a narrow window, scroll right to find it.
4. Repeat for every active item.

**Modifiers**
1. Open **Modifier Mapping**.
2. In the **Product/Prep Recipe** drop-down, search for and choose the match.
3. Enter the **Measurement** (number plus UOM) the modifier uses.
4. If the modifier *removes* an ingredient, scroll right and turn on **Subtract** so its cost comes off the recipe.
5. Click the **green checkmark** to save.
6. **Same-name modifiers:** xtraCHEF may ask whether to copy the measurement to all of them. Choose **Yes** if they're the same, or **No** if the amount differs by dish, and set those at the menu-item level.
7. Click a modifier's name to see which menu items use it.
- **Nested modifiers** (Pro customers) can also be mapped, and they deplete inventory and AvT.

**Menu-item-specific modifiers** (when the amount differs by dish, or for size modifiers). The menu item must already be mapped to a recipe.
1. In **Menu Item Mapping**, click the menu item row. You'll see its recipe ingredients, modifiers and sizes.
2. Open the **Modifiers** tab, choose a **Product/Prep Recipe**, enter the measurement, and click **Save Modifiers**.

**Size modifiers** (scaling portions to size pricing)
1. Click the menu item title → **Sizes** tab.
2. The recipe needs a **Serving size** set in its **Details** tab first. It isn't set by default, and sizes are locked without it.
3. Mark one size as the **default serving size**. Ideally it should match the recipe's serving size.
4. Enter measurements for the other sizes and click **Save Sizes**.

**Missing items / sync timing**
- Items can be missing because the change wasn't published in Toast Web, or because the menu is inactive.
- Published changes take up to **24 hours** to sync.
- To speed it up: **Recipes** tab → open the recipe → **Pair with Toast menu item** → **Re-sync from POS**. This pulls the last 24 hours of changes and counts as mapping. Recipes only, not prep recipes.

## Settings, options & permissions
- No roles are stated in the article. Nested modifier mapping is Pro-only.

## Rules, limits & gotchas
- Map **every** active menu item. Unmapped items quietly understate theoretical usage.
- The Subtract toggle is per modifier. Without it, "no X" modifiers add cost instead of removing it.
- Copying a measurement across duplicate-name modifiers is convenient but wrong when portions differ between dishes.
- Size mapping needs a recipe serving size.

## Automation / efficiency angles
- **Draft beer by size:** set each draft beer recipe's serving size to its default pour (e.g., 16 fl oz) and map the size modifiers (e.g., 5 oz taster, 10 oz, 32 oz crowler fill, 64 oz growler fill) in the **Sizes** tab. Theoretical keg depletion is then accurate in ounces. As an alternative, the recipe-level **Serving size configuration** can stand in for size-modifier mapping.
- **Flights:** map flight taster modifiers to the specific keg products at 4–5 oz each.
- **Add-ons:** map "Add bacon", "Sub GF bun" and similar with a measurement. Use **Subtract** for "no cheese" type options.
- Weekly agent check: list unmapped menu items and modifiers (anything without a green check) after new beers go on tap, and fix or re-sync before the next AvT run.
- Publish Toast menu changes first, then **Re-sync from POS** on the recipe. This skips the 24-hour wait on tap-change days.

## Related articles
- Get Started With Recipes: https://intercom.help/toast-central/en/articles/14728216-xtrachef-get-started-with-recipes
- Toast Menu Considerations and Best Practices: https://intercom.help/toast-central/en/articles/14487587-xtrachef-toast-menu-considerations-and-best-practices
- Variance Analysis and Product Mix Reports: https://intercom.help/toast-central/en/articles/14727540-xtrachef-variance-analysis-and-product-mix-reports
- Sync With Toast Web: https://intercom.help/toast-central/en/articles/14727574-xtrachef-sync-with-toast-web
- Recipe on Mobile: https://intercom.help/toast-central/en/articles/14727632-xtrachef-recipe-on-mobile
- Building Nested Modifiers: https://central.toasttab.com/s/article/Building-Nested-Modifiers
- Size Pricing on Modifier Groups: https://central.toasttab.com/s/article/Product-Guide-Configuring-Size-Pricing-on-Modifier-Groups-and-Modifier-Options
- Video: https://play.vidyard.com/SJ17RxijepwgWKHnBN1i7z
