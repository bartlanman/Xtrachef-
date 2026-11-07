---
title: "xtraCHEF: Get Started With the Setup Checklist"
source: https://intercom.help/toast-central/en/articles/14727775-xtrachef-get-started-with-the-setup-checklist
last_updated: 2026-05-29
area: getting-started
---

## What it is
New xtraCHEF accounts show a Setup Checklist during the first few sign-ins. It stays on the dashboard until all five items are done. It walks you through the minimum setup needed for xtraCHEF to produce value: activation, accounting connection, invoices, purchase categories and item mapping.

## When you'd use it
- The first weeks after purchasing xtraCHEF.
- To check whether a new location or tenant has been fully set up.

## How to do it
The checklist has five items:
1. **Complete initial setup** (account activation). Every other step depends on this. You're prompted on first login. If you skip it, return through **Initial Setup** in the checklist and click **Activate**. See [Activate Your xtraCHEF Account](activate-your-account.md).
2. **Automate your accounting**. This also goes through activation. The Onboarding team collects your info and sets up QuickBooks or another accounting integration.
3. **Upload 10+ invoices**. There are five ways to get documents in:
   - Upload files from a desktop (**Upload Document** screen).
   - Take photos in the xtraCHEF mobile app.
   - Create an invoice or receipt manually on desktop.
   - Email PDFs to the location's unique **xcinvoice** email address.
   - Set up an EDI integration with an approved vendor.
4. **Create 1+ purchase category**. Either integrate your accounting system or upload your chart of accounts (GL codes) through your Onboarding Consultant. That creates the categories used in Map Invoice Items and completes this item. To add a custom category:
   1. Click the **gear icon** (top right) > **Categories**. The page lists default and custom categories.
   2. Click **+ Add Custom Category**.
   3. Choose the **GL code** it reports to, enter a **Description** (name), and fill in any other fields.
   4. Click **+ Add**.
5. **Categorize 1+ item**:
   1. Open **Map Invoice Items** from the left nav.
   2. Pick a purchase category from the drop-down for each line item.
   3. When an invoice is fully mapped, click **Submit selected items**.
   - The page may already be empty because many items map automatically to default categories.

## Settings, options & permissions
- Category creation and the accounting integration are admin-level tasks, normally done by a Tenant Admin with the Onboarding Consultant.
- Available in the **US only**. Not offered in Australia, Canada, Ireland or the UK.

## Rules, limits & gotchas
- **Learned mapping**: once an item has been mapped and its invoice submitted, xtraCHEF applies the same mapping automatically whenever the **item number + item description + vendor** all match a previously coded item. If any of the three changes (a vendor renames an item, for example), the item comes back for manual mapping.
- **Multiple QBO companies in one tenant**: allowed, but the tenant keeps only **one COA list and one vendor list** shared by every location. Every QBO company must have **identical COA and vendor lists** before you connect. If they don't match, either make them match (recommended) or ask for separate tenants.
- Custom categories are sub-groups under a GL code. They give reporting detail but **don't push to QBO**.

## Automation / efficiency angles
- Use the xcinvoice email address as the default "bill-to" email with every vendor. Invoices then arrive with no one uploading them, which clears the "10+ invoices" step and keeps data flowing.
- Set up EDI with broadline vendors (Sysco, PFG, US Foods, where supported) to remove manual uploads altogether.
- Spend the first mapping sessions mapping carefully. Because of learned mapping, each correct mapping saves effort on every future invoice from that vendor.
- For Basic City: custom categories under one "Beer Purchases" or "Food Purchases" GL can split hops, malt, kitchen protein, produce and so on for reporting without cluttering the QBO COA.

## Related articles
- [Get Started With Onboarding](https://intercom.help/toast-central/en/articles/9303005-xtrachef-get-started-with-onboarding)
- [Get Started With QuickBooks Online Sales Syncing](https://intercom.help/toast-central/en/articles/9308304-xtrachef-get-started-with-quickbooks-online-sales-syncing)
- [Glossary and Terminology](https://intercom.help/toast-central/en/articles/14487632-xtrachef-glossary-and-terminology)
- [Get Started With Multi-Unit Onboarding](https://intercom.help/toast-central/en/articles/14487684-xtrachef-get-started-with-multi-unit-onboarding)
- [Help Center: xtraCHEF by Toast](https://intercom.help/toast-central/en/articles/14486883-help-center-xtrachef-by-toast)
