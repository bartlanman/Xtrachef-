---
title: "xtraCHEF: Recipe Configurations"
source: https://intercom.help/toast-central/en/articles/14727736-xtrachef-recipe-configurations
last_updated: 2026-04-28 (date shown on article)
area: recipes
---
## What it is
**Recipe > Configurations** holds three tenant-wide recipe settings:
- **Unit Conversion**: custom house units like a spoodle or a scoop.
- **Dining Options**: default disposables attached to every Dine-in, Takeout or Delivery transaction.
- **Delivery Fees**: percentage upcharges for off-premise channels, so the cost of delivery apps or a fleet is reflected.

## When you'd use it
- When your specs use non-standard measures (a ladle, a #16 scoop, a "pump" of syrup, a jigger).
- When to-go packaging (clamshells, cups, lids, napkins) should count toward cost on takeout and delivery orders.
- When third-party delivery commissions should be built into recipe profitability.

## How to do it
**Unit Conversion**
1. Go to **Recipe > Configurations** → **Unit Conversion** tab.
2. Click **+ Add Row**.
3. Enter a **Unit Name**, a **Conversion Factor** (how much one custom unit holds), and the **Unit of Measurement (UOM)**.
4. Click **Save**. The unit shows up in the table and can be used in recipes and prep recipes.

**Dining Options**
1. **Dining Options** tab → **Manage >** next to Dine-in, Takeout or Delivery.
2. Drag items from the left column to the right and set the measurement.
3. Click **Save**.

**Delivery Fees**
1. **Delivery Fees** tab.
2. In the **Fees** column, enter the percent upcharge for each order style.
3. Click **Save**.

## Settings, options & permissions
- No roles are listed in the article.

## Rules, limits & gotchas
- Products have to exist and be linked to an invoice item before they can be added as Dining Option defaults.
- The article's custom unit example is 1 spoodle = 6 weighted oz.

## Automation / efficiency angles
- Bar: create units like "Jigger (1.5 oz)", "Pony (1 oz)", "Pint pour (16 fl oz)" and "Taster (5 fl oz)" so recipes read like the bar spec.
- Takeout defaults: for Basic City, attach the crowler can and lid, to-go clamshell and napkins to Takeout, so to-go margins in PMIX include packaging. Online orders through Toast count as Takeout or Delivery depending on the dining option.
- Set Delivery Fees to your actual third-party commission rate so delivery profitability is realistic.

## Related articles
- Get Started With Recipes: https://intercom.help/toast-central/en/articles/14728216-xtrachef-get-started-with-recipes
- Recipe Yield and Density Calculator: https://intercom.help/toast-central/en/articles/14727732-xtrachef-recipe-yield-and-density-calculator
- Recipe - Product Mix Mapping: https://intercom.help/toast-central/en/articles/14727592-xtrachef-recipe-product-mix-mapping
- Sync With Toast Web: https://intercom.help/toast-central/en/articles/14727574-xtrachef-sync-with-toast-web
- Get Started With Multi-Unit Onboarding: https://intercom.help/toast-central/en/articles/14487684-xtrachef-get-started-with-multi-unit-onboarding
- Create Products: https://central.toasttab.com/s/article/xtraCHEF-How-to-Create-Product-Groups
