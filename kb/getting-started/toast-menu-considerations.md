---
title: "xtraCHEF: Toast Menu Considerations and Best Practices"
source: https://intercom.help/toast-central/en/articles/14487587-xtrachef-toast-menu-considerations-and-best-practices
last_updated: 2026-04-28
area: getting-started
---

## What it is
Guidance on building the Toast menu so xtraCHEF's recipe costing, Product Mix (PMIX) and Inventory Analytics (AvT) work. In xtraCHEF, every **menu item maps to a Recipe**, and every **modifier maps to a Product (ingredient) or a Prep Recipe**. A menu that works fine at the POS can be impossible to cost. Toast describes this as suggestions only, and you remain responsible for your menu.

## When you'd use it
- Before Product Mix Mapping (Pro).
- When adding new menu items, cocktails, beer sizes or modifier groups.
- When AvT or PMIX numbers look wrong.

## How to do it (design rules)
Ask two questions for every item: can a standard recipe be written for it, and are its modifiers used as intended?
- **Same recipe as an existing item?** Copy the item or modifier group. **Different portion or ingredients?** Create a new item or group.

**Food**
- Combo, choose-your-own and "Combo Platter" items are too vague. Make specific items ("Burger Platter") and keep add-ons as modifiers.
- Build-your-own pizza: create items per crust or base ("BYO Regular", "BYO Gluten Free", "BYO White GF"). Toppings are modifiers.
- **Menu-specific pricing** (lunch/dinner, happy hour) only works if the portion is identical. Different portions need separate items. The same applies to modifiers (1.5 oz vodka at both prices is fine).
- **Open price** items only work if the recipe never changes. A daily fish special with a changing fish needs an item or recipe for each fish.

**Beverage**
- Cocktails should be **menu items**, and spirits should be **modifiers** (Item: Old Fashioned; Modifier group: Whiskey Cocktails; Modifiers: Jack Daniels / Jim Beam / Woodford). The reverse setup needs a separate recipe for every spirit and cocktail combination.

**Size modifiers** (a special modifier type, different from a regular modifier named "Large")
- Lets you set how many portions each size equals (a 12 oz bowl = 2 × the 6 oz cup recipe).
- Works only when the **whole recipe scales proportionally**. Examples that work: **draft beer at 12/16/24 oz**, single or double shots.
- Doesn't work: coffee sizes with different cups or syrup amounts, 12 oz vs 16 oz Budweiser (different packaged products), large vs small empanadas (different prep items), 12 oz vs 16 oz prime rib (the sides don't scale). Use separate items for these.
- Can't substitute packaging by size. Different packaging needs a separate item.

**Modifiers**
- **Nested modifiers** (Pro) are mapped in Product Mix Mapping and deplete for inventory and AvT.
- A modifier can **add or remove** an ingredient, not both. Make separate "Add Onion" and "No Onion" modifiers.
- Keep modifier groups to a minimum. Only split groups when portions differ. Modifiers with **exactly the same name** and the same amount can be mapped together.
- **Pre-modifiers (NO/ADD/LITE/XTRA) don't work** with xtraCHEF. Instead, create separate modifier groups for NO, ADD, LITE and XTRA.

## Settings, options & permissions
- Toast menu edits happen in Toast Web (menu builder). Mapping happens in xtraCHEF Recipe > Product Mix Mapping (TA/RM, Pro).
- Toast and xtraCHEF must be integrated. Menu and sales data sync daily.

## Rules, limits & gotchas
- Vague items can't be costed and create noise in AvT.
- Packaged beer (cans, bottles) needs a separate menu item per package size, not a size modifier.

## Automation / efficiency angles
- For Basic City: set draft beers up as **one menu item per beer with a Toast size modifier** (taster / 10 oz / 16 oz / 20 oz and so on). One recipe based on the keg cost per oz then costs every pour size. Crowlers, growler fills and 4-packs to go are separate items.
- Taproom cocktails and spirits: the cocktail is the item, the spirit is the modifier.
- Before each seasonal menu change, review new items against these rules. Fixing the Toast setup up front avoids mapping problems that are hard to fix later.

## Related articles
- [Recipe - Product Mix Mapping](https://intercom.help/toast-central/en/articles/14727592-xtrachef-recipe-product-mix-mapping)
- [Get Started With Recipes](https://intercom.help/toast-central/en/articles/14728216-xtrachef-get-started-with-recipes)
- [Sync With Toast Web](https://intercom.help/toast-central/en/articles/14727574-xtrachef-sync-with-toast-web)
- [Post-Onboarding Best Practices](https://intercom.help/toast-central/en/articles/14487667-xtrachef-post-onboarding-best-practices)
