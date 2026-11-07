---
title: "xtraCHEF: Integrations and Data Exchanges"
source: https://intercom.help/toast-central/en/articles/14727658-xtrachef-integrations-and-data-exchanges
last_updated: 2026-08-13
area: accounting
---

## What it is
A reference listing the accounting and back-office platforms xtraCHEF can send data to. There are only two **true integrations**, which move data automatically with no user action: **Toast** and **QuickBooks** (Online and Desktop). Every other platform is a **data exchange**, meaning a CSV file the customer has to download and import. Both tiers (Essentials and Pro) include this.

## When you'd use it
- Choosing or changing accounting software.
- Checking whether xtraCHEF can feed R365, Xero, Bill.com and similar systems.
- Deciding whether payroll JEs should come from xtraCHEF or from Toast Payroll's own sync.

## How to do it
1. Email Customer Care (**support@xtrachef.com**) to have the tenant set up for your accounting integration or data exchange.
2. For QBO or QBD, follow the QuickBooks Online or Desktop integration guide.
3. For CSV platforms, download extract files from the **Extract Monitor** and import them into the other system.

## Compatibility table
| Platform | Invoice | Sales | Payroll | Receipts |
|---|---|---|---|---|
| **QuickBooks Online** (integration) | ✓ | ✓ | ✓ | ✓ |
| **QuickBooks Desktop** (integration) | ✓ | ✓ | ✓ | ✓ |
| Sage Intacct | ✓ | ✓ | | |
| Bill.com, CHEFTEC, Compeat, CrunchTime, CTUIT, Expressway, Jonas, Microsoft Dynamics (Great Plains), NCR Back Office (MenuLink), NetSuite, Northstar, Oracle EBS, Restaurant365, Rosnet, Sage 50, Sage 100, Salido, Xero, Yardi VendorCafe | ✓ | | | |

## Settings, options & permissions
- Accounting integrations can only be added or edited by a **Tenant Admin**, and setup goes through Customer Care.

## Rules, limits & gotchas
- Everything except Toast and QuickBooks needs manual CSV handling.
- **Toast Payroll + QBO**: Toast Payroll has its own direct QBO sync ("Get Started With Payroll Accounting Sync"). If you use both, choose **one** source for payroll JEs, or you'll post payroll twice.
- Third-party connections are governed by each provider's own terms and security. Review them before connecting.

## Automation / efficiency angles
- For Basic City (QBO): invoices, receipts and sales JEs all flow automatically. The only decision is payroll. If Toast Payroll is in use, check whether payroll JEs come from the Toast Payroll Accounting Sync or from xtraCHEF, and turn the other off. Add this to the cutover check.
- Bill.com is invoice-only by CSV. If you use it to pay vendors, QBO still gets bills from xtraCHEF directly, so avoid importing the same bills a second time.

## Related articles
- [Get Started With QuickBooks Online Sales Syncing](https://intercom.help/toast-central/en/articles/9308304-xtrachef-get-started-with-quickbooks-online-sales-syncing)
- [Configure Sage Intacct Integration](https://intercom.help/toast-central/en/articles/14727719-xtrachef-configure-sage-intacct-integration)
- [Sync With Toast Web](https://intercom.help/toast-central/en/articles/14727574-xtrachef-sync-with-toast-web)
- [Sync Monitor](https://intercom.help/toast-central/en/articles/14728186-xtrachef-sync-monitor)
- [Extract Monitor](https://intercom.help/toast-central/en/articles/14727735-xtrachef-extract-monitor)
