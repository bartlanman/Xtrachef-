# Automation map — what an agent can take off Bart's plate

The help center documents no customer-facing xtraCHEF API, so automation runs through: (a) xtraCHEF's own built-in automations, (b) the QuickBooks Online connector, (c) a browser session in Toast Web that Bart signs into, (d) email.

## Turn on inside xtraCHEF (one-time setup, then it runs itself)
| Feature | What it automates | Note |
|---|---|---|
| Email-in address per location (…@xcinvoice.com) | Vendors email PDFs straight in | Only registered senders, PDFs only. `kb/invoicing/upload-invoices-desktop.md` |
| Approval rules — Contract Price Variance, Manual Upload | Flags price creep and hand-entered invoices | Tenant Admin. `kb/invoicing/approvals.md` |
| Auto assign unique Invoice ID | Stops duplicate rejections for vendors without numbers | Per vendor |
| Purchase Summary extract preference | No line mapping for non-inventory vendors | Per vendor |
| Mobile notifications / mobile approval | Approvals from the phone | `kb/invoicing/mobile-*.md` |
| Price tracker Close Watch | Watches key items' prices | `kb/reporting/price-tracker.md` |
| Instant Upload | Single-page immediate processing | Ask support@xtrachef.com |
| EDI (PFG, Sysco via dashboard tile; beverage distributors via Fintech) | Invoices arrive electronically — no uploads at all | Fintech needs matching Secondary Vendor ID. `kb/vendors/edi-integration-with-vendors.md` |
| Scheduled order guides (Order > Order Guides > Schedule, Auto Submission) | Standing orders send themselves | Vendor needs a sales rep contact. `kb/orders/order-guides.md` |
| Bid-sheet import into order guides (.csv/.xls/.xlsx) | Loads vendor price lists for comparison | `kb/orders/order-guides.md` |
| Import GL codes and payment terms from QBO | Keeps xtraCHEF in step with QuickBooks | Re-import after adding QBO accounts. `kb/gl-and-journal-entries/gl-codes.md` |

## Agent routines (scheduled tasks)
| Routine | Cadence | How |
|---|---|---|
| Queue sweep (Action Needed, Map Items, Approvals, Extract Monitor, Sync Monitor) | Daily | Browser, read-only → short report |
| AP tie-out: xtraCHEF bills vs QBO AP | Weekly | QBO connector + Invoice summary by GL export |
| Price creep report | Weekly | Contracted price variance + `pfg-sysco-price-check` |
| Month-end close checklist + tie-out | Monthly | `playbooks/month-end.md` |
| Cutover check (Shogo → xtraCHEF) | Until clean | `xtrachef-cutover-check` skill |
| Vendor-invoice email triage | Daily | Gmail: find invoice emails not forwarded to the xcinvoice address |

Anything that changes data waits for Bart's yes.
