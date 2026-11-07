---
title: "xtraCHEF: Switch QuickBooks Integrations"
source: https://intercom.help/toast-central/en/articles/14487875-xtrachef-switch-quickbooks-integrations
last_updated: 2026-04-22
area: quickbooks
---
## What it is (2-4 sentences)
Explains how to change xtraCHEF's extract configuration between QuickBooks Desktop and QuickBooks Online. The switch is done by xtraCHEF support, not self-serve. Migrating the QuickBooks company file itself (Desktop → Online) is Intuit's job, not xtraCHEF's.

## When you'd use it
- Moving the books from QB Desktop to QBO (or the reverse) and needing xtraCHEF to point at the new system.

## How to do it (numbered steps with exact menu paths, button and field names)
1. Email **support@xtraCHEF.com** with:
   - **Current integration** (QB version you're on now)
   - **New integration** (QB version you want)
   - **Tenant name** (shown in the upper-right of the xtraCHEF dashboard)
2. xtraCHEF switches the extract.
3. Reconnect:
   - QBO → follow "Get Started With QuickBooks Online Integration", section **Connect to QuickBooks Online** (gear > Account setup > Integrations > Connect to QuickBooks).
   - Desktop → follow "Get Started With QuickBooks Desktop Integration", section **Set Up Your Web Connector**.
4. For the file migration itself, use Intuit's "Move your QuickBooks Desktop file to QuickBooks Online".

## Settings, options & permissions (which roles can do it)
- No self-service toggle; support performs the change. Reconnecting needs QB Admin credentials (and Tenant Admin in xtraCHEF).

## Rules, limits & gotchas (sync errors, mapping rules, what syncs vs what doesn't, timing)
- After the switch, re-verify GL codes, vendor codes (QBO "Display Name As" vs Desktop "Vendor Name") and the extract start date so you don't re-push or skip invoices.

## Automation / efficiency angles
- Have the tenant name and both versions ready in one email to avoid back-and-forth.
- Immediately after reconnecting, run an Extract Monitor check and an On-Demand Extract on a test invoice before letting the schedule run.

## Related articles (links)
- [xtraCHEF: QuickBooks Compatibility](https://intercom.help/toast-central/en/articles/14727478-xtrachef-quickbooks-compatibility)
- [xtraCHEF: Get Started With QuickBooks Online Sales Syncing](https://intercom.help/toast-central/en/articles/9308304-xtrachef-get-started-with-quickbooks-online-sales-syncing)
- [xtraCHEF: Get Started With QuickBooks Desktop Integration](https://intercom.help/toast-central/en/articles/14728138-xtrachef-get-started-with-quickbooks-desktop-integration)
- [xtraCHEF: Integrations and Data Exchanges](https://intercom.help/toast-central/en/articles/14727658-xtrachef-integrations-and-data-exchanges)
- [xtraCHEF: Receipt Extract for QuickBooks Online](https://intercom.help/toast-central/en/articles/14727687-xtrachef-receipt-extract-for-quickbooks-online)
