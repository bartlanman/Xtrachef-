---
title: "xtraCHEF: Get Started With QuickBooks Desktop Integration"
source: https://intercom.help/toast-central/en/articles/14728138-xtrachef-get-started-with-quickbooks-desktop-integration
last_updated: 2026-04-22
area: quickbooks
---
## What it is (2-4 sentences)
Setup guide for connecting xtraCHEF to QuickBooks Desktop through Intuit's **Web Connector** (PC) or IIF file imports (Mac / unsupported versions). Once set up you can import the chart of accounts and vendors, push invoices as Bills and credits as Vendor Credits, and post Toast sales (and payroll) as journal entries. Not relevant to Basic City (QBO) except as background.

## When you'd use it
- Your books are on QB Desktop Pro/Premier/Enterprise for PC, or on Mac/old versions needing IIF.

## How to do it (numbered steps with exact menu paths, button and field names)
**Prereq**: Onboarding Consultant enables the Desktop extract (tell them Mac or PC).

**Extract configuration**
1. **gear icon > Account setup** → **Integrations** tab.
2. Set sync frequency for **Vendor**, **GL**, **Customer**, **Payment Method**: **At Defined Intervals** or **Syncing On-Demand**.

**Web Connector**
1. Open QB Desktop, log in to the company file as **Admin**, in **single-user mode**.
2. **File** menu → look for **Update Web Services**; if missing install the Web Connector from Intuit.
3. Download the account-specific **.QWC** files from the Integrations page (one for bills/vendors/chart of accounts, one for journals).
4. **File > Update Web Services** → **Add an application** → choose the QWC → **Open** → **OK** to allow access.
5. Choose **"Yes, always; allow access even if QuickBooks is not running"** → **Continue** → **Done**.
6. Enter your xtraCHEF password in Web Connector → **Yes** to save it.
7. Auto: tick **Auto-Run** and set minutes. Manual: tick the row → **Update Selected**. First run pulls COA, GLs and vendors.
8. Repeat for each QWC (sales and invoice syncs are separate files unless IIF extract is enabled).

**Import vendors**: **gear icon > Account Setup > Integrations** → **Vendor Sync Frequency** (Defined Intervals / On-Demand) → **Save** → run Web Connector (invoice QWC → Update Selected).

**IIF (Customer Care must configure first)**
- Sales JE: **Sync Monitor** → date → **Sales** link → **Action > Download QuickBooks Desktop IIF File** → in QB **File > Utilities > Import > IIF Files** → **Import IIF** → preview → **Save & New**.
- Payroll JE: Sync Monitor → payroll day → download IIF (OK if all payroll categories mapped) → import.
- Invoices: open Extract Monitor from a **ready to extract** invoice → choose **IIF Extract** → **Submit** → **On Demand Extract**.

## Settings, options & permissions (which roles can do it)
- QB Desktop Admin/Administrator, single-user mode. The same person who downloads the .QWC must run the Web Connector setup (avoids authentication failures).

## Rules, limits & gotchas (sync errors, mapping rules, what syncs vs what doesn't, timing)
- Web Connector not supported on Mac → IIF.
- Auto-Run stops whenever Web Connector is closed or the PC is off.
- Next step after connection: Sales Setup.

## Automation / efficiency angles
- Leave the host PC on with Web Connector running, Auto-Run on, to make Desktop behave close to real-time.
- Use Clear RMS Ref to requeue invoices for the next Web Connector run.

## Related articles (links)
- [xtraCHEF: Get Started With QuickBooks Online Sales Syncing](https://intercom.help/toast-central/en/articles/9308304-xtrachef-get-started-with-quickbooks-online-sales-syncing)
- [xtraCHEF: Switch QuickBooks Integrations](https://intercom.help/toast-central/en/articles/14487875-xtrachef-switch-quickbooks-integrations)
- [xtraCHEF: Clear RMS Reference Feature for QuickBooks](https://intercom.help/toast-central/en/articles/14726363-xtrachef-clear-rms-reference-feature-for-quickbooks)
- [xtraCHEF: QuickBooks Compatibility](https://intercom.help/toast-central/en/articles/14727478-xtrachef-quickbooks-compatibility)
- [xtraCHEF: Get Help With QuickBooks Extract Errors](https://intercom.help/toast-central/en/articles/14727646-xtrachef-get-help-with-quickbooks-extract-errors)
- [xtraCHEF: Sales Setup](https://intercom.help/toast-central/en/articles/14727468-xtrachef-sales-setup)
