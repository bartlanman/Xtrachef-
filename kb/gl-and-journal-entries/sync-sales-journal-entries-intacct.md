---
title: "xtraCHEF: Sync Sales Journal Entries to Intacct"
source: https://intercom.help/toast-central/en/articles/14727596-xtrachef-sync-sales-journal-entries-to-intacct
last_updated: 2026-04-22
area: gl-and-journal-entries
---

## What it is
For **Sage Intacct** users, xtraCHEF posts each day's Toast sales as a journal entry. Using **Sync Monitor** you can view a day's entry, add balanced debit and credit adjustments for sales the POS missed, check the sync audit trail, and then find the result under Intacct's Sales Journals. *Basic City uses QBO, not Intacct.* The Sync Monitor view, edit, and audit pattern is similar for QBO sales syncs (see the Sync Monitor and QBO sales sync articles).

## When you'd use it
- To add off-POS revenue, such as a food truck, a special event, or an off-site festival, to the day's sales JE.
- To investigate a failed sales sync.

## How to do it
**View**
1. Click **Sync Monitor** in the left nav.
2. Pick a date and click a journal entry link.

**Edit (adjustments)**
1. Switch the entry from **View** to **Edit** mode. You can only change data in Edit.
2. Click **+ Add adjustment** at the bottom.
3. Choose the adjustment type from the first drop-down. Its **GL Code** displays.
4. Enter a **Debit** or **Credit**. Normally you add a matching pair so the JE stays balanced.
5. When it balances, click **Save**.

**Audit**
1. Click **Actions > View Audit** to see sync start and end times. A sales audit trail is available the same way.
2. **Green** means synced to Intacct. **Red** means an error. For details, click **Notifications** in the upper right.

**In Intacct**: go to **Sales Journals** to see the posted entries.

## Settings, options & permissions
- Requires the Sage Intacct integration (see Configure Sage Intacct Integration). No roles are stated.

## Rules, limits & gotchas
- Adjustments should be entered in balanced debit and credit pairs.
- *Inference:* edits made after a day has synced may need a re-sync. The article doesn't say whether saving re-pushes.

## Automation / efficiency angles
- Have a standard adjustment playbook for off-POS revenue, such as festival cash sales, so a manager enters them the same way every time.
- Daily: check that every Sync Monitor date is green. Red means open Notifications.

## Related articles
- [Sync Monitor](https://intercom.help/toast-central/en/articles/14728186-xtrachef-sync-monitor)
- [Sales Setup](https://intercom.help/toast-central/en/articles/14727468-xtrachef-sales-setup)
- [Configure Sage Intacct Integration](https://intercom.help/toast-central/en/articles/14727719-xtrachef-configure-sage-intacct-integration)
- [Get Help With Sales Syncs to QuickBooks](https://intercom.help/toast-central/en/articles/14728156-xtrachef-get-help-with-sales-syncs-to-quickbooks)
- [QuickBooks Desktop Integration](https://intercom.help/toast-central/en/articles/14728138-xtrachef-get-started-with-quickbooks-desktop-integration)
