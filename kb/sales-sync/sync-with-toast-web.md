---
title: "xtraCHEF: Sync With Toast Web"
source: https://intercom.help/toast-central/en/articles/14727574-xtrachef-sync-with-toast-web
last_updated: 2026-07-07
area: sales-sync
---

## What it is
This covers the link between Toast Web (POS data) and xtraCHEF. Once it's connected, daily sales, menu items, modifiers (including nested modifiers) and related data flow into xtraCHEF. Reporting stays empty until Sales Setup, COGS mapping and (on Pro) Product Mix Mapping are finished.

## When you'd use it
- At initial setup.
- When sales reporting is empty and you're checking whether the Toast link exists.
- Before starting recipe and menu mapping on Pro.

## How to do it
1. **Integration**: the Toast team links the two accounts. You don't set this up yourself. To confirm it's live, ask your Onboarding Consultant or email **support@xtrachef.com**.
2. **Sales Setup**: click the **gear icon > Sales setup**. Configure General settings and map Toast sales categories to COGS groups (and GL codes if sales sync to QBO is on). See [Sales Setup](sales-setup.md).
3. **COGS mapping**: map purchase categories to the same COGS groups so purchases and sales line up.
4. **Menu item mapping (Pro)**: all existing Toast menu items and modifiers sync automatically. Use **Product Mix Mapping** to tie each menu item or modifier to a recipe so xtraCHEF can compare menu price and sales with prime cost.

## Settings, options & permissions
- Sales Setup and COGS mapping are Tenant Admin configuration tasks. COGS groups can only be added or modified by a Tenant Admin.
- Product Mix Mapping requires Pro, and Recipe access (TA/RM).

## Rules, limits & gotchas
- xtraCHEF captures **every** menu item and modifier, including old and duplicate ones. Archive or remove unwanted or duplicate items **before** Product Mix Mapping. You can do this manually or ask Customer Care (support@xtrachef.com).
- No reporting appears until the three mapping steps are done.

## Automation / efficiency angles
- Before mapping, export the Toast menu and flag retired seasonal beers, old event items and duplicate "Pint – X" buttons. Archive them in one pass so you aren't mapping dead items.
- New beers added to Toast sync into xtraCHEF automatically, but they have no recipe or cost until mapped. Add a "new Toast items not yet mapped" check to the weekly routine.

## Related articles
- [Toast Menu Considerations and Best Practices](https://intercom.help/toast-central/en/articles/14487587-xtrachef-toast-menu-considerations-and-best-practices)
- [Get Started: Use xtraCHEF With Toast](https://intercom.help/toast-central/en/articles/14487751-get-started-use-xtrachef-with-toast)
- [Recipe - Product Mix Mapping](https://intercom.help/toast-central/en/articles/14727592-xtrachef-recipe-product-mix-mapping)
- [Get Help With Sales Syncs to QuickBooks](https://intercom.help/toast-central/en/articles/14728156-xtrachef-get-help-with-sales-syncs-to-quickbooks)
- [Sales Setup](https://intercom.help/toast-central/en/articles/14727468-xtrachef-sales-setup)
