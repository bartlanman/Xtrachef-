---
title: "xtraCHEF: Reassign Product Unit for Products and Associated Items"
source: https://intercom.help/toast-central/en/articles/14726299-xtrachef-reassign-product-unit-for-products-and-associated-items
last_updated: 2026-04-22
area: invoicing
---

## What it is
Every product has a **Product unit**, the unit that inventory and recipe costs are expressed in. Every invoice item linked to that product has a **Size unit**. To change a product's unit, you also have to update the Size unit on every linked item so they stay in the same unit family: weight, volume, or each/count.

## When you'd use it
- A product was set up in the wrong unit (for example, "each" when you cost it by the lb).
- Changing how you count or cost something, such as moving cheese from a count of blocks to weight.
- Fixing recipe costs that look wrong because of a unit mismatch.

## How to do it
1. Go to **Item library > View products**.
2. Click the product.
3. Click **Edit product** in the lower right.
4. In the sidebar, change **Product unit** to the new unit.
5. Scroll down and set the **Size unit** on **every** associated invoice item to a unit of the same type. For example, if the product unit is gram or lb, every item's size unit has to be a weight.
6. Once every item matches, **Save changes** turns blue. Click it.

## Settings, options & permissions
- There are three unit families: **weight**, **volume**, and **each/count**, each with several size units.
- No roles are stated.

## Rules, limits & gotchas
- **Save changes** stays disabled until every linked item's Size unit matches the Product unit family.
- If you need to cross families (for example, volume to weight for flour), you need density or yield information. See the Recipe Yield and Density Calculator. *(Inference from related links.)*
- Changing units affects inventory count values and recipe costing going forward. Re-check recipes that use the product.

## Automation / efficiency angles
- Pick the product unit when you create the product, based on how recipes call for the item (oz or lb for proteins, fl oz or gal for liquids, each for buns). Getting it right up front avoids this cleanup.
- Audit: in View products, look for products whose unit family doesn't match how they're counted in inventory.

## Related articles
- [Get Started With the Item Library](https://intercom.help/toast-central/en/articles/14727460-xtrachef-get-started-with-the-item-library)
- [Create Products](https://intercom.help/toast-central/en/articles/14727550-xtrachef-create-products)
- [Product Verification](https://intercom.help/toast-central/en/articles/14727562-xtrachef-product-verification)
- [Assign Invoice Items to Products](https://intercom.help/toast-central/en/articles/14727680-xtrachef-assign-invoice-items-to-products)
- [Recipe Yield and Density Calculator](https://intercom.help/toast-central/en/articles/14727732-xtrachef-recipe-yield-and-density-calculator)
