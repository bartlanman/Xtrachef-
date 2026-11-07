---
title: "xtraCHEF: Get Started With Budget Reporting"
source: https://intercom.help/toast-central/en/articles/14728192-xtrachef-get-started-with-budget-reporting
last_updated: 2026-04-28
area: reporting
---
## What it is (2-4 sentences)
The Budget module lets you set estimated sales and target COGS % per accounting period and COGS group, then tracks actual Toast sales and reconciled purchases against it as a declining budget. The dashboard shows remaining budget and available daily spend. It also feeds the Operating Summary's Budget column.

## When you'd use it
- Setting monthly purchasing limits for kitchen/bar/brewing and checking mid-month whether you can still afford orders.

## How to do it (numbered steps with exact menu paths, button and field names)
**Prereqs**: COGS mapping; accounting period; ≥1 month of consistent invoice/receipt uploads; Toast POS integration + Sales Setup; historical monthly sales and a forecast; target food cost %.

**Open**: **Budget** in left nav → tabs **Dashboard** (default), **Budget**, **Import**.

**Manual budget**
1. **Budget** tab → choose **Location** and **Fiscal Year**.
2. **+ Create New Budget** → **Copy Previous Month Budget** or **Empty Budget**.
3. Empty: enter **Sales Estimate for COGS** (period total); optionally split by **COGS Group** via **Sales Forecast** in % or $.
4. Enter **Target COGS (%)** per period/group.
5. **Save** (confirmation shown).

**Import**
1. **Import** tab → **Download Budget Template** (BudgetTemplate.xlsx; Notes tab has guidance).
2. On the **Budget** tab: don't edit Row 1 (Accounting Period), Row 2 (Sales Forecast / Target COGS labels), or Column A (COGS Group/GL).
3. Fill **Sales Forecast** $ and **Target COGS** % per period → save.
4. **Import Budget** → choose file (multi-unit: correct location).

**Dashboard**: **Location**/**Fiscal Year** drop-downs; slider **Declining View** (default) / **Estimated View**.
- Row 1: **Target COGS**, **Estimated Sales**, **Actual Sales** (Toast), **Actual COGS**, **Estimated Budget** (Sales Estimate × Target COGS %), **Actual Spent** (reconciled invoices), **Remaining Budget** = Estimated Budget − Actual Spend, **Avbl. Daily Spend** = Remaining Budget ÷ days left.
- Row 2: **COGS Group Cost**, **Actual Sales Vs Purchases** chart, **Estimated Budget Vs Actual**, **Estimated Sales Vs Actual**, **Category** (spend & cost ratio).
- Pies: **Sales by COGS**, **Purchase by COGS**, **Year to Date Budget & Sales**.

## Settings, options & permissions (which roles can do it)
- No roles listed. COGS groups can't be edited from the Budget tab.

## Rules, limits & gotchas (sync errors, mapping rules, what syncs vs what doesn't, timing)
- Actual Spent only counts uploaded & reconciled invoices — lagging uploads make you look under budget.
- Target COGS % is of revenue and need not equal the sales split.

## Automation / efficiency angles
- Build the annual budget once in Excel from QBO history and import via the template.
- Share **Avbl. Daily Spend** with the kitchen lead/brewer before placing big orders.
- Upload invoices same day so the declining budget is truthful.

## Related articles (links)
- [xtraCHEF: COGS Report](https://intercom.help/toast-central/en/articles/14727521-xtrachef-cogs-report)
- [xtraCHEF: Operating Summary](https://intercom.help/toast-central/en/articles/14728290-xtrachef-operating-summary)
- [xtraCHEF: Introduction to Reporting and Analytics](https://intercom.help/toast-central/en/articles/14727505-xtrachef-introduction-to-reporting-and-analytics)
- [xtraCHEF: Review Reports in the Reporting Module](https://intercom.help/toast-central/en/articles/14727530-xtrachef-review-reports-in-the-reporting-module)
- [xtraCHEF: Glossary and Terminology](https://intercom.help/toast-central/en/articles/14487632-xtrachef-glossary-and-terminology)
