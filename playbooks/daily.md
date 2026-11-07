# Daily routine (10–15 min)

Goal: every invoice reaches QuickBooks, every day's sales journal entry posts, nothing sits in a queue.

## 1. Invoices waiting on us
- **Action Needed / Exceptions** — clear rejections and missing info. See `kb/invoicing/action-needed-invoices.md`, `kb/invoicing/rejected-and-action-needed-invoices.md`.
  - Rejected invoices can't be edited — re-upload (whole invoice, all pages via **Add Page**).
  - "Invoice from unregistered user" → accept to register the sender for email-in.
- **Map Invoice Items** — new items/vendors block the invoice. Map, then **Submit Selected Items** (never Reprocess). `kb/invoicing/map-invoice-items.md`
- **Product Verification** and **Approvals** queues — approve or fix. `kb/invoicing/approvals.md`, `kb/getting-started/product-verification.md`
- Processing normally takes 6–8 hours, max 24. Anything older than a day in Reconciliation → investigate. `kb/invoicing/get-started-with-reconciliation.md`

## 2. Bills to QuickBooks
- **Extract Monitor** — anything not green → **View Details** → fix → **Re-Extract**. Error→fix table: `playbooks/troubleshooting.md`.
- "Ready to Extract" sitting too long → check vendor code, GL mapping, integration status.

## 3. Sales to QuickBooks
- **Sync Monitor** — a red dot on a day = the sales JE didn't post. Fix and resync (up to 7 days at a time). `kb/quickbooks/sales-sync-errors.md`
- Most common: a new Toast menu category/tender/discount needs a GL in Sales Setup; an open check in Toast ("Journal out of balance").

## 4. Capture
- Snap paper invoices the same day (mobile app, one upload per invoice, Add Page for multi-page). `kb/invoicing/upload-invoices-mobile.md`
- Log waste as it happens (blown keg, spoiled product): Inventory > Manage Waste. `kb/count-lists/manage-waste.md`

## Agent can do
Read-only sweep of all four queues + Extract Monitor + Sync Monitor and report a short list: what's stuck, why, the exact fix. Changes only after Bart approves.
