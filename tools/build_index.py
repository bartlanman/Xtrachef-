"""Rebuild kb/INDEX.md from the frontmatter of every note in kb/.

Run from the repo root:  python3 tools/build_index.py
"""
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
KB = ROOT / "kb"

AREA_ORDER = [
    ("getting-started", "Getting started & onboarding"),
    ("admin-and-users", "Admin, users & roles"),
    ("invoicing", "Invoicing"),
    ("vendors", "Vendors"),
    ("purchase-categories", "Purchase categories"),
    ("orders", "Orders"),
    ("gl-and-journal-entries", "GL codes & journal entries"),
    ("cogs", "COGS"),
    ("accounting", "Accounting, periods & integrations"),
    ("quickbooks", "QuickBooks integration"),
    ("sales-sync", "Sales sync"),
    ("reporting", "Reporting & analytics"),
    ("inventory", "Inventory"),
    ("count-lists", "Count lists & waste"),
    ("recipes", "Recipes"),
    ("recipe-costing", "Recipe costing"),
    ("misc", "Other"),
]


def frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---", text, re.S)
    data = {}
    if m:
        for line in m.group(1).splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                data[k.strip()] = v.strip().strip('"')
    return data


def first_sentence(text):
    m = re.search(r"## What it is[^\n]*\n+(.+?)(?:\n\n|\n##)", text, re.S)
    if not m:
        return ""
    s = " ".join(m.group(1).split())
    s = re.split(r"(?<=[.!?])\s", s)[0]
    return s[:200]


def main():
    lines = [
        "# xtraCHEF Knowledge Base — Index",
        "",
        "One note per official xtraCHEF help-center article, written in our own words.",
        "Regenerate with `python3 tools/build_index.py`.",
        "",
    ]
    total = 0
    known = {a for a, _ in AREA_ORDER}
    extra = sorted(p.name for p in KB.iterdir() if p.is_dir() and p.name not in known)
    for area, label in AREA_ORDER + [(e, e) for e in extra]:
        d = KB / area
        notes = sorted(d.glob("*.md")) if d.exists() else []
        if not notes:
            continue
        lines += [f"## {label}", "", "| Note | Summary | Source |", "|---|---|---|"]
        for p in notes:
            t = p.read_text(encoding="utf-8")
            fm = frontmatter(t)
            title = fm.get("title", p.stem).replace("|", "/")
            summary = first_sentence(t).replace("|", "/")
            src = fm.get("source", "")
            src_md = f"[link]({src})" if src.startswith("http") else ""
            lines.append(f"| [{title}]({area}/{p.name}) | {summary} | {src_md} |")
            total += 1
        lines.append("")
    lines.insert(4, f"**{total} notes.** Playbooks: [`../playbooks/`](../playbooks/).\n")
    (KB / "INDEX.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"Indexed {total} notes")


if __name__ == "__main__":
    main()
