---
title: "xtraCHEF: Get Started With User Roles"
source: https://intercom.help/toast-central/en/articles/13730305-xtrachef-get-started-with-user-roles
last_updated: 2026-07-07
area: admin-and-users
---

## What it is
xtraCHEF has five roles: **Tenant Administrator, Executive, Restaurant Manager, Restaurant User, Invoice Capture**. Each one sets which modules and actions a user can reach. Higher roles include the privileges of lower ones, so **assign one role per user**.

## When you'd use it
- Adding staff, tightening access, or working out why someone can't see a module.

## How to do it (change a role)
1. **gear icon > Users**, then search for the user.
2. Click the **pencil icon** and open the **User Access** tab.
3. Tick the role (and locations), then click **+Update**.
4. To remove access entirely, **untick every box** on User Access.

## Roles
- **Tenant Admin**: owners and regional or supervising managers. There's no limit on how many, but choose carefully. Only TAs can manage locations, users, accounting integrations, GL codes, custom categories, COGS groups, tenant configuration, approval rules, cost centers, product verification, payment terms and receipt payment methods.
- **Executive**: described as view-only (investors, silent partners, report readers). The feature table actually shows some write abilities (edit invoices, reject or approve, edit vendors, manage the catalog), so test before you rely on it being read-only. Executives can't use Orders, Order Guides, Recipe or Inventory. A few reports are hidden from them: **GL Distribution, GL Summary, Contracted Price Variance, Top 100 Product Purchase**.
- **Restaurant Manager**: GMs and chefs. Must be assigned **per location**. Can export data, create orders, manage recipes, view the Extract Monitor, assign payment terms to vendors, and set up inventory.
- **Restaurant User**: shift leads and assistant managers. Must be assigned **per location**. Handles daily uploads, reconciliation, approvals, inventory counts, orders, order guides and budgets. Can't do Recipe, Vendor management, Exceptions, Map Inventory or Item Library.
- **Invoice Capture**: cooks and bartenders. **Upload only** (mobile, desktop, email). Sees only their own uploaded documents. Can capture and apply credits and see the Reconciliation report.

## Feature access highlights
| Capability | TA | EX | RM | RU | IC |
|---|---|---|---|---|---|
| Upload / invoice listing / CSV export | ✓ | ✓ | ✓ | ✓ | ✓ (own only) |
| Edit invoice header/lines, reject | ✓ | ✓ | ✓ | ✓ | – |
| Approve invoices, reconcile, Sync Monitor | ✓ | ✓ | ✓ | ✓ | – |
| Exceptions, Item Library, Vendor Hub edit, Invoice Search, Operating Summary | ✓ | ✓ | ✓ | – | – |
| Extract Monitor, assign vendor payment terms | ✓ | – | ✓ | – | – |
| Recipe module | ✓ | – | ✓ | – | – |
| Orders, order guides, budgets, inventory setup/waste/analytics | ✓ | – | ✓ | ✓ | – |
| Users, locations, GL, categories, COGS groups, tenant config, approval rules, cost centers, payment terms | ✓ | – | – | – | – |

## Rules, limits & gotchas
- Multiple roles on one user can break login or access. Keep it to one role.
- RM and RU only see the locations they're assigned to.

## Automation / efficiency angles
- For Basic City: owner and bookkeeper are Tenant Admin. The kitchen manager and bar or brew lead are Restaurant Manager (for recipes). Shift leads are Restaurant User. Anyone receiving deliveries gets Invoice Capture, so invoices are photographed at the dock.
- Investors who only need reports get Executive, but check the write access first.

## Related articles
- [Add and Manage User Profiles](https://intercom.help/toast-central/en/articles/14726283-xtrachef-add-and-manage-user-profiles)
- [Access to Inventory Features by Role](https://intercom.help/toast-central/en/articles/14727495-xtrachef-access-to-inventory-features-by-role)
- [Levels of Reporting](https://intercom.help/toast-central/en/articles/9307954-xtrachef-levels-of-reporting)
- [Glossary and Terminology](https://intercom.help/toast-central/en/articles/14487632-xtrachef-glossary-and-terminology)
