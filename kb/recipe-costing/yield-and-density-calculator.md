---
title: "xtraCHEF: Recipe Yield and Density Calculator"
source: https://intercom.help/toast-central/en/articles/14727732-xtrachef-recipe-yield-and-density-calculator
last_updated: 2026-04-28 (date shown on article)
area: recipe-costing
---
## What it is
This covers how xtraCHEF adjusts ingredient cost when less than 100% of the purchased amount ends up on the plate, and how it converts between weight, volume and each.
- **Yield** treats the loss as waste and raises the effective cost.
- **Consumable Portion** (usable yield) means the trimmed part gets used elsewhere, so cost isn't adjusted.
- The **Density Calculator** handles weight↔volume and mass↔each conversions.

## When you'd use it
- Trimmed or cooked proteins (raw-to-cooked loss), produce trim, and anything else that shrinks.
- Ingredients bought by weight but measured by volume (shredded cheese by the cup), or bought by weight and used by each (an 8 oz chicken breast).
- Setting a product-wide default yield so every recipe picks it up.

## How to do it
**Yield or consumable portion inside a recipe**
1. **Recipe** → open the recipe → add the ingredient (set **Quantity** and **UOM**).
2. Ingredient **three dots (overflow)** → **Ingredient yield**.
3. Type the **Yield** or **Consumable portion** % → **Done**.
4. Click **Save**. Yield changes don't stick until you save.

**Product-wide default yield**
1. **Item library > View products** → choose the product (the sidebar shows the latest invoice's purchase details) → **Edit product**.
2. Enter the **yield percent** → **Save changes**. It becomes the default in every recipe that uses the product, and individual recipes can still override it.
- Tip: product three dots → **Product details** lists every recipe using the product (middle tile).

**Density Calculator in a recipe**
- Entering an alternate UOM for an ingredient (volume for a weight product, weight for a volume product, or **each** for a mass or volume product) opens the calculator automatically.
- Define the relationship with the drop-downs, e.g., 1 cup mozzarella ≈ 6 oz by weight, or 8 oz chicken breast = 1 each, then **Save**.

**Density on the product (applies to all future recipes)**
1. **Item Library > View Products** → product → **Edit product**.
2. At the bottom of the sidebar, enter "1 (unit) = (number) (unit)".
3. Click **Save changes**. You can do this before the product is ever used in an alternate UOM.

## Settings, options & permissions
- No roles are listed in the article.

## Rules, limits & gotchas
- The default yield is **100%**.
- Yield example: an 8 oz steak served needs 10 oz raw ribeye, so yield = **80%**.
- Consumable-portion examples: an egg where only the yolk is used = **50%**; a lemon where the rind is used for zest = **85%**.
- Recipes **don't natively convert mass to each**. The Density Calculator is the only route. Example: chicken at $16.00 per 4 lb works out to $0.25/oz, so 8 oz = 1 each costs $2.00.
- A recipe-level yield sits on top of the product default for that recipe only.

## Automation / efficiency angles
- Set product-level yields once for high-trim items (brisket, wings, whole produce) and density once for cheese, sauces and similar. Every new recipe is then right from the start.
- Kegs and beer don't need density (volume to volume). Do set a **foam/line-loss yield** (e.g., 90–95%) on draft keg products if you want plate cost to reflect real pour loss. The other approach is to leave yield at 100% and let the AvT variance show the loss. Pick one approach and stick with it.
- Spent grain or other brewery by-products used in the kitchen: if they're tracked as products with a cost, model them with a consumable portion and don't inflate the cost.
- Agent check: list products used in recipes by a different UOM family than their purchase unit that have no density set. Those are cost errors waiting to happen.

## Related articles
- Get Started With Recipes: https://intercom.help/toast-central/en/articles/14728216-xtrachef-get-started-with-recipes
- Recipe Configurations: https://intercom.help/toast-central/en/articles/14727736-xtrachef-recipe-configurations
- Recipe - Product Mix Mapping: https://intercom.help/toast-central/en/articles/14727592-xtrachef-recipe-product-mix-mapping
- Recipe on Mobile: https://intercom.help/toast-central/en/articles/14727632-xtrachef-recipe-on-mobile
- Get Started With Products: https://intercom.help/toast-central/en/articles/9303010-xtrachef-get-started-with-products
- Item Library: https://intercom.help/toast-central/en/articles/14727460-xtrachef-get-started-with-the-item-library
