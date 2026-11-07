---
title: "xtraCHEF: Chart of Accounts"
source: https://intercom.help/toast-central/en/articles/14727682-xtrachef-chart-of-accounts
last_updated: 2026-04-22
area: gl-and-journal-entries
---

## What it is
The **chart of accounts (COA)** is the list of accounts, divided into assets, liabilities, revenue, equity, COGS, and expenses, with GL codes underneath each. In xtraCHEF it's the framework for the **Invoice, Sales, and Payroll syncs** with QuickBooks, and for reports down to the cent. The article gives a sample mapping from Toast sales components to GL accounts, plus a basic and a detailed restaurant COA.

## When you'd use it
- Setting up the xtraCHEF to QBO connection.
- Deciding how detailed COGS accounts should be, for example a single Food COGS account or one per category.
- Mapping Toast sales components (tips, taxes, payments, gift cards, fees) for the sales journal sync.

## How to do it
**Get your COA into xtraCHEF**
1. **COA in QBO or QB Desktop** (Basic City's case): connect the integration and import (see GL Codes).
2. **COA but no QuickBooks**: the onboarding consultant uploads it, or you add GL codes manually.
3. **No COA**: build it as you go by creating GL codes.

**Sample Toast-to-GL mapping (for sales sync)**
| Toast component | GL account | Type |
|---|---|---|
| Sales (Food, LBW) | Sales | Income |
| Discounts (Food, LBW) | Sales | Income |
| Credit Card Tips | Tips Payable | Other Current Liability |
| Sales Taxes | Sales Tax Payable | Other Current Liability |
| Payment: Credit Card | Business Checking | Bank |
| Payment: Cash | Undeposited Funds | Other Current Asset |
| Payment: Gift Card / Deferred Gift Card | Gift Card | Other Current Liability |
| Payment: Prepaid Order / Deferred Paid In Total | Prepaid Orders | Other Current Liability |
| Payment Fees (AMEX, V/MC/D) | CC Processing Fees | Expense |
| Cash Over/Shortage | Cash Over/Shortage | Expense |
| Refund & Refund Adjustment | Refunds | Income |
| Tips Shortage | Cash On Hand | Bank |

**Example COA structures** (paraphrased)
- *Basic:* Assets 1000–1999, Equity 3000s, Revenue 4100–4950 (food, NA beverage, bottle/draft beer, liquor, wine by bottle/glass, shift drinks, and discount contra-accounts for service recovery, marketing, ownership, goodwill), Direct Costs 5000–5540 (purchases by category such as dry goods, dairy, produce, beef, pork, poultry, seafood, plus liquor, beer, and NA beverage), Expenses 6100–7030, and liabilities for sales and meals tax.
- *Detailed:* adds inventory asset accounts (food, beverage, bar, consumables), gift cards outstanding, tips payable, payroll clearing, income split by daypart, comps and discounts, merchandise and catering income, COGS by category plus **Change in Food/Beverage Inventory**, merchandise cost, a full payroll and opex breakdown, and other income and expense (8000s/9000).

## Settings, options & permissions
- No roles are stated. The article carries a disclaimer that it isn't accounting, legal, or tax advice.

## Rules, limits & gotchas
- There's no standard COA. Design it around your operation with your bookkeeper. Toast support won't pick codes for you.
- Too many GL codes clutter QBO. Use detailed **purchase categories** in xtraCHEF that roll up to fewer GL codes.

## Automation / efficiency angles
- Example of the payoff: weekly purchases rose by $300, and the Food Cost Weekly report combined with COGS GL codes shows the increase was food. Granular COGS GL codes plus xtraCHEF reports explain cost swings fast.
- For a brewery-restaurant, consider separate COGS GLs for Food, House Beer (ingredients and packaging), Resale Beer/Wine/Spirits, NA Beverage, and Merchandise. Matching revenue GLs make the xtraCHEF COGS groups tie to the QBO P&L.
- Use the sample mapping table as a checklist when auditing the Toast sales sync to QBO (tips, gift cards, and deferred revenue are the usual errors).

## Related articles
- [General Ledger (GL) Codes](https://intercom.help/toast-central/en/articles/14725478-xtrachef-general-ledger-gl-codes)
- [COGS Mapping](https://intercom.help/toast-central/en/articles/14727476-xtrachef-cogs-mapping)
- [Add and Edit COGS Groups](https://intercom.help/toast-central/en/articles/14728289-xtrachef-add-and-edit-cogs-groups)
- [Operating Summary](https://intercom.help/toast-central/en/articles/14728290-xtrachef-operating-summary)
- [Glossary and Terminology](https://intercom.help/toast-central/en/articles/14487632-xtrachef-glossary-and-terminology)
- Food Cost Weekly: https://central.toasttab.com/s/article/xtraCHEF-Analytics-Food-Cost-Weekly
- Video: https://play.vidyard.com/LvRyeDkCpyoNbPtyagcq3a
