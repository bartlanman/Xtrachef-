---
title: "xtraCHEF: Create and Edit Purchase Categories"
source: https://intercom.help/toast-central/en/articles/14728208-xtrachef-create-and-edit-purchase-categories
last_updated: 2026-09-24
area: purchase-categories
---

## What it is
**Purchase Categories** (formerly "custom categories") break a GL code into finer reporting groups, for example splitting "Food Purchases" into Produce, Protein, Dairy and so on. Each category points to a **GL code** (which drives the accounting extract) and optionally a **COGS group** (which drives COGS reporting). The category itself **doesn't change what posts to accounting**. It only adds reporting detail. The current UI lists everything at **gear icon > Purchase Categories**. There's no separate "Categories" item anymore.

## When you'd use it
- When setting up the reporting layer under the COA.
- When a new GL is added in QBO and needs a category.
- When reorganizing COGS groups.
- When retiring categories you no longer use.

## How to do it
**Create**
1. **gear icon** (top right) **> Purchase Categories**. Defaults may already be listed.
2. Click **+ Add Category**.
3. Enter the name.
4. Pick the **GL Code Mapping** and **COGS Group Mapping** it breaks out from.
5. Tick **Include for COGS** if purchases in this category should count in COGS.
6. Click **+Add**.
- There's also an in-app guided tour, **Learn to Create Purchase Categories**, and a 4-minute video.

**Edit**
1. **gear icon > Purchase Categories**, tick the category, then click **Edit Category**.
2. Change the name, **COGS Group Mapping** or **GL Code Mapping**.
3. To remove the COGS link, set the drop-down to **Select** and untick **Include for COGS**.
4. To deactivate, untick **Active**.
5. Click **Save**. Changes apply immediately.

**Deactivate / activate**
- Deactivate: tick the categories, then **Action > Deactivate Category**.
- Activate: turn on the **Include Inactive Categories** filter, tick the categories, then **Action > Activate Category**.

**Bulk edit**
1. Tick several categories.
2. **Action > Edit COGS Mapping** or **Edit GL Code Mapping**.
3. Pick the target COGS group or GL, then **Save**.

## Settings, options & permissions
- **Tenant Admin** (custom categories and GL codes are TA-only).
- **Access gotcha**: being a Toast Web admin or owner does **not** make you an xtraCHEF admin. If the gear icon is greyed out or Purchase Categories is missing, it's a role problem. Another xtraCHEF Tenant Admin grants access under **gear icon > Users**. If nobody can: (1) sign in directly at **app.xtrachef.com** in a new or incognito window, (2) clear cache and cookies, (3) ask another TA to confirm your role.
- Creating custom categories can be turned off tenant-wide (Tenant Configuration > Custom Category, through support).

## Rules, limits & gotchas
- Inactive categories stay visible, but **no new items can be assigned** to them.
- Changing a category's GL mapping changes where **future** extracts post. Bills already in QBO stay as they are.
- Only GL codes reach QBO. Categories and COGS groups exist only in xtraCHEF.
- If **Include for COGS** is unticked, that spend is excluded from the COGS report even when it's food or beverage.

## Automation / efficiency angles
- For Basic City, a suggested structure (under each QBO GL):
  - Food Purchases → Protein, Produce, Dairy, Dry Goods, Bakery (COGS: Food, Include for COGS)
  - Beer Purchases (guest kegs, cans) → Guest Draft, Guest Package (COGS: Beer)
  - Brewing Ingredients → Malt, Hops, Yeast, Adjuncts. Decide whether these go to COGS: Beer, or stay off restaurant COGS if brewery COGS is tracked separately.
  - Wine/Spirits/Cider → (COGS: Liquor & Wine)
  - NA Beverage → Soda/Syrup, Coffee (COGS: NA Bev)
  - Paper & Disposables, Cleaning/Chem → not Include for COGS (operating expense)
- Use **bulk edit** to re-point many categories when a QBO GL is renamed or merged. Do this **before** the next extract to avoid "account does not exist" failures.
- Review categories quarterly. Deactivate unused ones so the Map Invoice Items drop-down stays short, which speeds up coding.

## Related articles
- [General Ledger (GL) Codes](https://intercom.help/toast-central/en/articles/14725478-xtrachef-general-ledger-gl-codes)
- [COGS Mapping](https://intercom.help/toast-central/en/articles/14727476-xtrachef-cogs-mapping)
- [Add and Edit COGS Groups](https://intercom.help/toast-central/en/articles/14728289-xtrachef-add-and-edit-cogs-groups)
- [Change an Invoice Item's GL Code or Category](https://intercom.help/toast-central/en/articles/14727522-xtrachef-change-an-invoice-item-s-gl-code-or-category)
- [Sales Setup](https://intercom.help/toast-central/en/articles/14727468-xtrachef-sales-setup)
