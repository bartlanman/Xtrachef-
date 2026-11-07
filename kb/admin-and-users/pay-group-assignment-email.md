---
title: "xtraCHEF: Pay Group Assignment Email"
source: https://intercom.help/toast-central/en/articles/14488040-xtrachef-pay-group-assignment-email
last_updated: 2026-04-08
area: admin-and-users
---

## What it is
Tenant Admins get an automated email when the account has **Toast Payroll pay groups that aren't mapped to an xtraCHEF location**. Until each pay group is mapped, payroll data can't be assigned to a location for labor and prime-cost reporting or for the payroll extract.

## When you'd use it
- When the email arrives.
- After adding a new Toast Payroll pay group or a new location.

## How to do it
1. Log in to xtraCHEF.
2. **Settings gear icon > Payroll setup**.
3. On **General Setup**, scroll to **Location Processing**.
4. For each Toast Payroll pay group, pick the matching xtraCHEF location from the drop-down.
5. Click **Save**.

## Settings, options & permissions
- **Tenant Admin**. The email only goes to TAs.

## Rules, limits & gotchas
- Every pay group needs a location. Unmapped groups are left out of location-level payroll data.
- If payroll JEs reach QBO through Toast Payroll's own Accounting Sync, avoid also extracting payroll from xtraCHEF (double posting). See Integrations and Data Exchanges.

## Automation / efficiency angles
- Add "map any new pay group" to the checklist for creating a new Toast Payroll pay group (for example, a separate brewery production pay group).

## Related articles
- [Get Started With Payroll Accounting Sync](https://intercom.help/toast-central/en/articles/14728359-get-started-with-payroll-accounting-sync)
- [Reconcile Toast Payroll Data](https://intercom.help/toast-central/en/articles/14725454-xtrachef-reconcile-toast-payroll-data)
- [Get Started With QuickBooks Online Sales Syncing](https://intercom.help/toast-central/en/articles/9308304-xtrachef-get-started-with-quickbooks-online-sales-syncing)
- [Sales Setup](https://intercom.help/toast-central/en/articles/14727468-xtrachef-sales-setup)
