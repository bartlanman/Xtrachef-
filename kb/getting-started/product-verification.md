---
title: "xtraCHEF: Product Verification"
source: https://intercom.help/toast-central/en/articles/14727562-xtrachef-product-verification
last_updated: 2026-04-28
area: getting-started
---

## What it is
Product Verification is a **legacy** step for manually approving invoice line items: confirming pack and size details, the category and the product before items count toward recipe and inventory costs. **Item Review** has replaced it. It's still enabled for some legacy accounts and for certain third-party integrations, where it's a required step before invoices reconcile or extract.

## When you'd use it
- Only if your tenant still shows a **Product Verification** tab in the left menu.
- New accounts use Item Review instead. The field definitions below still apply there and are the most useful part of this note.

## How to do it
1. Open the **Product Verification** tab in the left menu. It lists every invoice item waiting for verification.
2. Click **Edit** in the Edit column for an item.
3. The original invoice image appears beside the fields, with the line number to cross-check.
4. Accept the AI-suggested Size/Pack, pick a different preset, or type values into **Pack** and **Size**.
5. Set **Category** (a GL code or custom category) and **Product** (the ingredient it rolls up to).

## Field definitions (also used in Item Review)
- **UOM**: the purchasing unit on the invoice (Case, Bag, Keg, Lb, Bottle).
- **Pack**: how many countable units are in the UOM. Defaults to 1.
- **Size**: the numeric amount per unit (750 for a 750 ml bottle).
- **Unit**: the measure for Size (ml, Liter, Lb, Gal).
- **Item UOM**: the name of the inner unit when Pack is more than 1 (Bottle). Defaults to "each".
- **Category**: GL code or custom category for accounting and reporting.
- **Product**: the ingredient grouping used by Recipes and Inventory.

## Configuration examples
| Purchase | UOM | Pack | Size | Unit | Item UOM |
|---|---|---|---|---|---|
| Case, 6 × 1 L gin ($233.94 → $38.99/bottle and /L) | Case | 6 | 1 | Liter | Bottle |
| Case, 10 × 750 ml | Case | 10 | 750 | Ml | Bottle |
| 10 lb case of apples (count by lb) | Case | 10 | 1 | Lb | Lb |
| 10 lb case of apples (count by case) | Case | 1 | 10 | Lb | N/A |
| 5 lb bag of sugar | Bag | 5 | 1 | Lb | Lb (or Bag/1/5/Lb) |
| **1/5 barrel keg** | Keg | 1 | 15.5 | Gal | N/A |
| Flank steak, catch weight | Lb | 1 | 1 | Lb | N/A |
| Single 750 ml bottle | Bottle | 1 | 750 | Ml | N/A |

## Settings, options & permissions
- Product Verification is listed as **Tenant Admin only** in the User Roles feature table.

## Rules, limits & gotchas
- Items waiting for verification **can't be used in Recipes or Inventory until the whole invoice is verified**.
- How you set Pack and Size should match how you count inventory (by case or by lb). Pick one approach and use it everywhere.
- **Keg note**: the article's example "1/5 barrel keg = 15.5 gal" is wrong. A 1/2 barrel is 15.5 gal, a 1/4 barrel (pony) is 7.75 gal, and a 1/6 barrel is 5.16 gal. Use the correct gallons for each keg size, or pour costs will be badly off.

## Automation / efficiency angles
- For Basic City: standardize keg setup as UOM Keg, Pack 1, Size = gallons (15.5 / 7.75 / 5.16), Unit Gal. Or use fl oz (1984 / 992 / 661) so cocktail and pour recipes cost directly in ounces.
- Canned beer and soda: Case | 24 | 12 | fl oz | Can.
- Verify in batches by vendor. Once a vendor's item is set up correctly, later invoices reuse it.

## Related articles
- [Get Started With the Item Library](https://intercom.help/toast-central/en/articles/14727460-xtrachef-get-started-with-the-item-library)
- [Create Products](https://intercom.help/toast-central/en/articles/14727550-xtrachef-create-products)
- [Assign Invoice Items to Products](https://intercom.help/toast-central/en/articles/14727680-xtrachef-assign-invoice-items-to-products)
- [Recipe - Product Mix Mapping](https://intercom.help/toast-central/en/articles/14727592-xtrachef-recipe-product-mix-mapping)
- [Glossary and Terminology](https://intercom.help/toast-central/en/articles/14487632-xtrachef-glossary-and-terminology)
