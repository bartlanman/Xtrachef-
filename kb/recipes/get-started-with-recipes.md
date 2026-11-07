---
title: "xtraCHEF: Get Started With Recipes"
source: https://intercom.help/toast-central/en/articles/14728216-xtrachef-get-started-with-recipes
last_updated: 2026-04-22 (date shown on article)
area: recipes
---
## What it is
The main guide to building **Prep recipes** (in-house components that aren't sold on their own) and **Recipes** (items sold to guests and linked to Toast menu items). Recipes are made from **Products**. They're costed by default at each ingredient's **most recent purchase price**, and once linked to Toast items they drive the PMIX, Variance and AvT reports.

## When you'd use it
- When building plate costs for the kitchen menu and pour costs for the bar or draft list.
- When creating prep components (sauces, dough, brines, batched cocktail mixes) that are used in many dishes.
- When copying recipes to another location, or printing and exporting recipe cards.

## How to do it
**Getting there:** **Recipe** is at the bottom of the left nav. Its tabs include **Recipes**, **Variance analysis** and **Configuration**. With Toast integrated you also get **Product mix mapping** and **Product mix report**.

**Quick start:** on the first visit, **Sync top 10 menu items** creates a recipe for each of your 10 best-selling Toast items, already named and linked to the menu item.

**Create:** click **+ Add recipe**, choose **Prep recipe** or **Recipe**, then **Next step**. The article suggests starting with prep recipes.

**Prep recipe**
1. *Basic details:*
   - **Prep recipe name**
   - **Prep recipe group** (e.g., Sauces, Dressings)
   - **Location** (can be copied elsewhere later)
   - **Batch size** (number plus UOM). This determines the per-unit cost when the prep recipe is used elsewhere.
   - **Yield** (% of the batch that's usable)
   - **Shelf life**
   - **Notes**
   Always set the name, group and batch size.
2. *Ingredients:* click **Select Ingredient**, choose from the drop-down, enter **Qty** and **UOM**. **Total Cost** fills in shortly after. Click **Add ingredient** for more rows.
3. *Procedures* (these don't affect cost): **Prep recipe image**, **Instructions** (English or a second language), **Prep time**, **Cook time**, allergens (**contains** and **may contain traces of**), **Tools**.
4. Click **Submit prep recipe** to publish it. It then becomes usable in other recipes and in modifier mapping. **Save changes** keeps it as a draft.

**Recipe**
1. *Basic details:*
   - **Recipe name** (edit with the blue pencil, top left)
   - **Recipe group** (e.g., Burgers)
   - **Location**
   - **Pair with Toast menu item**
   - **Serving size configuration** (a number plus a unit; replaces the need to map size modifiers)
   - **Menu Price** (fills in automatically once paired)
   - **Notes**
2. *Ingredients:* same as prep recipes. Prep recipes can be used as ingredients.
3. *Procedures:* **Recipe image**, Instructions, times, allergens, Tools.
4. Click **Submit Recipe** to make it live for mapping and reporting, or **Save changes** to keep a draft.

**Re-sync from POS:** in the **Pair with Toast menu item** drop-down, this pulls recent Toast Web menu changes. Normally they take up to a day to arrive. It's available for Recipes only, not prep recipes. It fails if the change isn't published in Toast Web or the menu holding the item is inactive.

**Copy:** recipe three-dot menu → **Copy** → edit the name, choose the **Locations** → **Copy**. You can copy to any location in the tenant.

**Download**
- All recipes: **Recipe** → choose a location → **Download all**.
- One recipe: three dots → **Download**.
- Pick **CSV** (one location or all) or **PDF**. In the PDF, **Show cost** adds Menu Price, Labor Cost, Food Cost and ingredient costs.
- PDFs build in the background. A red dot appears on the **bell** icon, and you download the **Recipe Download Export** from there.

**Conversions inside recipes**
- The **Density Calculator** pops up when a product is used in an alternate UOM (weight vs volume vs each).
- **Custom conversions:** ingredient three dots → **Product details** → set something like 1 each = 8 fl oz → **Save changes**. Yield can also be edited there.

## Settings, options & permissions
- No roles are listed in the article. Recipes require the Pro suite (per the Area Setup article).
- Further configuration (Unit Conversion, Dining Options, Delivery Fees) is covered in Recipe Configurations.

## Rules, limits & gotchas
- If an ingredient is missing from the drop-down, the product doesn't exist yet or isn't linked to an invoice item.
- Costs follow the **latest invoice price**, so one bad invoice line (wrong pack or size) throws off every recipe that uses the product.
- **Batch size** is the cost denominator for prep recipes. Get it wrong and every downstream recipe is wrong.
- Only **submitted** recipes feed PMIX mapping and reports. Drafts don't.
- Re-sync from POS doesn't work for prep recipes, unpublished menu changes, or inactive menus.

## Automation / efficiency angles
- Use **Sync top 10 menu items** on day one to get the recipe shells for the best sellers instantly.
- **Draft beer:** create a Recipe per draft menu item (or one per beer, with **Serving size configuration** for pour sizes like 5 oz, 10 oz, 16 oz) using the keg product in fl oz. xtraCHEF derives the per-oz cost from the keg's gallons.
- **Batched cocktails or house syrups:** make them prep recipes with a batch size in fl oz or L, then use them by the ounce in cocktail recipes.
- **House beer:** if brewery-to-taproom beer is set up as a product with a transfer cost, the same pour recipes apply.
- Give each recipe a group that matches the Toast menu group so PMIX review reads like the menu.
- Monthly menu price review: download all recipes as PDF with **Show cost**, or as CSV, and have an agent flag any recipe whose food cost % is above target since the last invoice price change.

## Related articles
- Recipe - Product Mix Mapping: https://intercom.help/toast-central/en/articles/14727592-xtrachef-recipe-product-mix-mapping
- Recipe Configurations: https://intercom.help/toast-central/en/articles/14727736-xtrachef-recipe-configurations
- Recipe Yield and Density Calculator: https://intercom.help/toast-central/en/articles/14727732-xtrachef-recipe-yield-and-density-calculator
- Recipe on Mobile: https://intercom.help/toast-central/en/articles/14727632-xtrachef-recipe-on-mobile
- Variance Analysis and Product Mix Reports: https://intercom.help/toast-central/en/articles/14727540-xtrachef-variance-analysis-and-product-mix-reports
- Toast Menu Considerations and Best Practices: https://intercom.help/toast-central/en/articles/14487587-xtrachef-toast-menu-considerations-and-best-practices
- Create Products: https://intercom.help/toast-central/en/articles/14727550-xtrachef-create-products
- Office Hours: https://toasttab.zoom.us/webinar/register/6817254876253/WN_HT6rtcyCS6mR2UJMastqUg#/registration
