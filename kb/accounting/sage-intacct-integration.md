---
title: "xtraCHEF: Configure Sage Intacct Integration"
source: https://intercom.help/toast-central/en/articles/14727719-xtrachef-configure-sage-intacct-integration
last_updated: 2026-07-09
area: accounting
---

## What it is
Setup steps for connecting xtraCHEF to Sage Intacct. Invoices sync to Intacct as **AP bills** (with an image link), and daily sales sync as **journal entries**. **Not relevant to Basic City** (which uses QBO), but kept for completeness.

## When you'd use it
- Only if you move to Sage Intacct.

## How to do it
Prerequisites: access to Toast Partner Integrations, and **admin access in Sage Intacct**.
1. **Add a web services user**: **Company > Subscriptions**, turn on **Web Services**. Then **Company > Web Services Users > Add**. Set User ID, First Name and Last Name to `sync_xtrachef`, use the xtraCHEF manager's email, **User type = Business**, **Admin privileges = Full**. Intacct emails a temporary password. This user is non-billable.
2. **Subscriptions**: on the `sync_xtrachef` user, click **Subscriptions** and enable all modules.
3. **Roles** (only if the account uses role-based permissions): **Company > Roles > Add**, name it "xtraCHEF Role", set **All** for every module (including Reports sections), then **Save**.
4. **Sender ID**: **Company > Company Info > Edit > Security**. Under **Web Services Authorizations**, add the Sender ID with the description "Sender ID for xtraCHEF". The xtraCHEF Sender ID is `xtraCHEFMPP`. **Save**.
5. **Invoice URL custom field**: **Company > Customization Service > Custom Fields** (sometimes under Platform Services) > **Add**. Object: **AP Bill**. Type: **URL**. **Label `Bill_Image`**, **Field ID `XC_INVOICE_URL`**, Field Set `xtraCHEF`, Show on Page: Header. Click **Done**.
6. **In xtraCHEF**: **gear icon > Account Setup > Integrations > Intacct**. Enter **Company ID** (from Sage), **User ID** `sync_xtrachef`, and the **Password** (the temporary one).
7. **Class or department by location**: **gear icon > Locations**, edit **Account Number**. Use `CLASS~` for class only, `~DEPT` for department only, or `CLASS~DEPT` for both.

## Settings, options & permissions
- Needs a Sage Intacct admin, plus a Tenant Admin in xtraCHEF.

## Rules, limits & gotchas
- For class-level invoice extraction, contact support@xtrachef.com.
- Sage Intacct support (General Support / POS Support) is available Mon–Fri, 8–5 CET.

## Automation / efficiency angles
- The `~` account-number format is the Intacct equivalent of putting the QBO class name in the location account number field.

## Related articles
- [Get Started With the Sage Intacct Integration](https://intercom.help/toast-central/en/articles/14488217-get-started-with-the-sage-intacct-integration)
- [Sync Sales Journal Entries to Intacct](https://intercom.help/toast-central/en/articles/14727596-xtrachef-sync-sales-journal-entries-to-intacct)
- [Integrations and Data Exchanges](https://intercom.help/toast-central/en/articles/14727658-xtrachef-integrations-and-data-exchanges)
- [Tenant Configuration Settings](https://intercom.help/toast-central/en/articles/14728296-xtrachef-get-started-with-tenant-configuration-settings)
