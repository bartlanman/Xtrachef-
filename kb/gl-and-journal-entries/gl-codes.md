---
title: "xtraCHEF: General Ledger (GL) Codes"
source: https://intercom.help/toast-central/en/articles/14725478-xtrachef-general-ledger-gl-codes
last_updated: 2026-08-20
area: gl-and-journal-entries
---

## What it is
GL codes are the accounts in your chart of accounts (a code plus a description, for example 1001 Food Purchases). They're grouped as Assets, Liabilities, Revenue, Equity, COGS, and Expenses. In xtraCHEF, purchase categories map to GL codes, and that mapping decides where invoice lines post in accounting. With QuickBooks Online the codes are **imported from QBO**. Without QuickBooks you create them in xtraCHEF.

## When you'd use it
- During setup: pull in the QBO chart of accounts.
- After adding a new account in QBO: re-import it so categories can map to it.
- When creating purchase categories directly from GL codes.

## How to do it
**Import from QuickBooks Online**
1. Go to **gear icon > Account setup > Integrations**. A **Disconnect from QuickBooks** button means QBO is connected.
   - No Integrations tab means QBO isn't enabled, or you use **QuickBooks at location level**. In that case check **gear icon > Locations**, select the location, click **Edit Location Details**, and confirm a QuickBooks location name appears in **Account Details**.
   - If QBO doesn't appear in the integrations list, disconnect and reconnect before importing.
2. Go to **gear icon > GL codes > Import GL from QuickBooks Online > Import**.
3. Check the codes you want and click **Import**.

**QuickBooks Desktop**
1. Go to **gear icon > Account setup > Integrations > GL Sync Frequency**. Choose **Defined Intervals** or **On Demand**, then click **Save**.
2. In the QB Web Connector, select the invoice .QWC file and click **Update Selected**.

**Create manually (non-QB)**
1. Go to **gear icon > GL codes > + Add GL Code**.
2. Enter **GL Code** and **Description** (both required). Account type and taxable are optional. If you don't use numbers, repeat the description in the code field.
3. Click **+ Add**.

**Edit or deactivate**: select the code and click **Edit GL Code**, then **Save**. To deactivate, uncheck **Active** or use **Actions > Deactivate**. Changes apply immediately.

**Create a purchase category from a GL code**: in **gear icon > GL Codes**, highlight the code, then **Action > Create Purchase Category**. It appears in the Map Invoice Items queue within 2 to 3 minutes.

**Print the list**: there's no export or print button. Open **gear icon > GL codes**, which shows everything on one page, and use the browser's print or save-as-PDF (Ctrl/Cmd+P).

## Settings, options & permissions
- No roles are stated. QBO must be connected to import.
- **Customer Care can't assign, recommend, or change GL codes.** That's your bookkeeper's job.
- If you have a COA but no QuickBooks, your onboarding consultant can upload it.

## Rules, limits & gotchas
- The QBO import only brings in the codes you select. New QBO accounts don't appear automatically, so re-import. *(The article describes the import as user-initiated.)*
- Deactivated codes can't be used for new mappings. Re-map their categories first.

## Automation / efficiency angles
- Keep QBO as the single source of truth. Create accounts in QBO, then import them. Never hand-create duplicates in xtraCHEF when QBO is connected.
- Use **Create Purchase Category** from GL codes to scaffold categories quickly, then split them into finer categories as needed.
- Agent check after a QBO chart change: compare the QBO account list with xtraCHEF GL codes (print to PDF) and import any that are missing.

## Related articles
- [Chart of Accounts](https://intercom.help/toast-central/en/articles/14727682-xtrachef-chart-of-accounts)
- [Change an Invoice Item's GL Code or Category](https://intercom.help/toast-central/en/articles/14727522-xtrachef-change-an-invoice-item-s-gl-code-or-category)
- [Create and Edit Purchase Categories](https://intercom.help/toast-central/en/articles/14728208-xtrachef-create-and-edit-purchase-categories)
- [Sales Setup](https://intercom.help/toast-central/en/articles/14727468-xtrachef-sales-setup)
- [Spending by GL Analytics](https://intercom.help/toast-central/en/articles/14728263-xtrachef-get-started-with-spending-by-gl-analytics)
- QBO integration: https://central.toasttab.com/s/article/xtraCHEF-QuickBooks-Online-Integration-for-Toast-Sync
- Video: https://play.vidyard.com/LvRyeDkCpyoNbPtyagcq3a
