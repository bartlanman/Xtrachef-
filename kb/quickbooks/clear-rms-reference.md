---
title: "xtraCHEF: Clear RMS Reference Feature for QuickBooks"
source: https://intercom.help/toast-central/en/articles/14726363-xtrachef-clear-rms-reference-feature-for-quickbooks
last_updated: 2026-06-23
area: quickbooks
---
## What it is (2-4 sentences)
**Clear RMS Reference** is a reset applied when re-extracting an invoice that failed (or was deleted) in QuickBooks Online or Desktop. It severs xtraCHEF's stored link to the earlier QuickBooks record so the invoice is treated as never exported. That prevents "Invoice already exists" style duplication errors from half-finished syncs and puts the invoice back in the Desktop Web Connector queue.

## When you'd use it
- A re-extract keeps failing because QuickBooks holds a "ghost" record from a partial sync.
- A bill was deleted in QuickBooks and you want xtraCHEF to push it again as new.
- QB Desktop: you want the next Web Connector run to pick the invoice up fresh.

## How to do it (numbered steps with exact menu paths, button and field names)
**QuickBooks Desktop**
1. When an extract error appears, click the exclamation-mark error icon for details, then go to **Extract monitor**.
2. Filter by **Extract Date Range** (not Invoice Date) → **Submit** → find the batch.
3. Click **View Details**, find the invoice, click **Re-extract**.
4. In the pop-up listing the batch's invoices, tick the invoice(s), tick **Clear RMS Ref**, then click **Re-Extract**.
5. Run the Web Connector; the invoice downloads as new.

**QuickBooks Online**
1. Go to **Search invoice**, enter the invoice number, click **Search**.
2. On the right invoice, click the **Re-extract icon** (circular arrows).
3. In the options pop-up, select **Extract Name** (column header) and **Clear RMS Reference**.
4. Click **Re-Extract**.
5. Wait a few minutes, then confirm the bill arrived in QBO.

## Settings, options & permissions (which roles can do it)
- No specific role listed; users who can access Extract Monitor / Search invoice and re-extract.

## Rules, limits & gotchas (sync errors, mapping rules, what syncs vs what doesn't, timing)
- Filter Extract Monitor by extract date, not invoice date, or you won't find the batch.
- Only clear the RMS reference if the bill is truly NOT in QuickBooks (or you've deleted it). If the bill still exists in QB, clearing and re-extracting can create a duplicate bill — check QB first.
- QBO extraction can take several minutes.

## Automation / efficiency angles
- Standard fix playbook for "Duplicate invoice"/"already exists": search QBO for the bill number → if absent, Clear RMS + re-extract; if present, leave it and mark resolved.
- When a vendor bill was deleted in QBO to fix a coding error, fix the coding in xtraCHEF first, then Clear RMS + re-extract so QBO and xtraCHEF match.

## Related articles (links)
- [xtraCHEF: Extract Monitor](https://intercom.help/toast-central/en/articles/14727735-xtrachef-extract-monitor)
- [xtraCHEF: Get Help With QuickBooks Extract Errors](https://intercom.help/toast-central/en/articles/14727646-xtrachef-get-help-with-quickbooks-extract-errors)
- [xtraCHEF: QuickBooks Compatibility](https://intercom.help/toast-central/en/articles/14727478-xtrachef-quickbooks-compatibility)
- [xtraCHEF: Receipt Extract for QuickBooks Online](https://intercom.help/toast-central/en/articles/14727687-xtrachef-receipt-extract-for-quickbooks-online)
- [xtraCHEF: Get Started With QuickBooks Desktop Integration](https://intercom.help/toast-central/en/articles/14728138-xtrachef-get-started-with-quickbooks-desktop-integration)
