---
title: "Get Help With Error: We Couldn't Connect to QuickBooks"
source: https://intercom.help/toast-central/en/articles/14488203-get-help-with-error-we-couldn-t-connect-to-quickbooks
last_updated: 2026-04-08
area: quickbooks
---
## What it is (2-4 sentences)
A very short article for the "We couldn't connect to QuickBooks" error. It says the error is generally a connection problem between QuickBooks and xtraCHEF and directs you to Customer Care. No self-serve steps are listed.

## When you'd use it
- You see "We couldn't connect to QuickBooks" while connecting or syncing.

## How to do it (numbered steps with exact menu paths, button and field names)
Official guidance: contact Customer Care. Practical pre-checks drawn from related articles before calling:
1. Log out of every QBO session in all browser tabs, disable pop-up blockers.
2. In xtraCHEF (Tenant Admin): **gear icon > Account Setup > Integrations** → **Disconnect from QuickBooks**, then **Connect to QuickBooks** and sign in with a QBO Admin.
3. Confirm the QBO subscription is active and is Essentials/Plus/Advanced.
4. Run a manual sync / On-Demand Extract to confirm.

## Settings, options & permissions (which roles can do it)
- Reconnect requires xtraCHEF Tenant Admin + QBO Admin.

## Rules, limits & gotchas (sync errors, mapping rules, what syncs vs what doesn't, timing)
- Root cause is usually expired auth tokens, billing lapse, a changed QBO password/email, or an unsupported QBO tier.

## Automation / efficiency angles
- Any QBO password/email change for the admin user should trigger a reconnect in both xtraCHEF and Toast Web Connections the same day.

## Related articles (links)
- [xtraCHEF: Get Help With QuickBooks Extract Errors](https://intercom.help/toast-central/en/articles/14727646-xtrachef-get-help-with-quickbooks-extract-errors)
- [xtraCHEF: Switch QuickBooks Integrations](https://intercom.help/toast-central/en/articles/14487875-xtrachef-switch-quickbooks-integrations)
- [Get Help With Error: Error Processing Void Reversal](https://intercom.help/toast-central/en/articles/12476066-get-help-with-error-error-processing-void-reversal)
- [Get Help with Payment Processing Error: Error Voiding or Refunding](https://intercom.help/toast-central/en/articles/14488131-get-help-with-payment-processing-error-error-voiding-or-refunding)
- [Get Help With Payroll Error: Sorry, We Couldn't Load the Paper Check Info](https://intercom.help/toast-central/en/articles/14488182-get-help-with-payroll-error-sorry-we-couldn-t-load-the-paper-check-info)
