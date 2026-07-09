"""Verify Insurance Analytics Dashboard PDF and Markdown."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DASH_DIR = ROOT / "Dashboard"

PDF_PATH = DASH_DIR / "insurance-dashboards.pdf"
MD_PATH = DASH_DIR / "insurance-dashboards.md"
HTML_PATH = DASH_DIR / "insurance-dashboards.html"

print("=" * 60)
print("  DASHBOARD CATALOGUE VERIFICATION")
print("=" * 60)

checks = []

# ── Files exist ────────────────────────────────────────────────
files = [
    ("PDF", PDF_PATH),
    ("Markdown", MD_PATH),
    ("HTML", HTML_PATH),
]
for label, path in files:
    exists = path.exists()
    checks.append((f"{label} exists", exists))

# ── PDF stats ──────────────────────────────────────────────────
if PDF_PATH.exists():
    pdf_size = PDF_PATH.stat().st_size
    with open(PDF_PATH, "rb") as f:
        data = f.read()
    page_count = data.count(b"/Type /Page") - data.count(b"/Type /Pages")
    checks.append(("PDF size > 200 KB", pdf_size > 200_000))
    checks.append(("PDF pages >= 20", page_count >= 20))
    print(f"  PDF:    {page_count} pages, {pdf_size/1024:.0f} KB")
else:
    page_count = 0

# ── Markdown stats ─────────────────────────────────────────────
if MD_PATH.exists():
    md_text = MD_PATH.read_text(encoding="utf-8")
    md_lines = md_text.split("\n")
    h2_count = sum(1 for l in md_lines if l.strip().startswith("## ") and not l.strip().startswith("### "))
    h3_count = sum(1 for l in md_lines if l.strip().startswith("### "))
    mermaid_count = md_text.count("```mermaid")
    kpi_tables = md_text.count("| KPI | Formula / Source | Chart")

    checks.append(("H2 sections >= 16", h2_count >= 16))
    checks.append(("Mermaid blocks >= 16", mermaid_count >= 16))
    checks.append(("KPI tables >= 16", kpi_tables >= 16))

    print(f"  Markdown: {len(md_lines)} lines, {h2_count} sections, {mermaid_count} mermaid")
else:
    h2_count = 0

# ── HTML stats ─────────────────────────────────────────────────
if HTML_PATH.exists():
    html_size = HTML_PATH.stat().st_size
    html_text = HTML_PATH.read_text(encoding="utf-8")
    kb = html_size / 1024
    print(f"  HTML:    {kb:.0f} KB")
else:
    kb = 0

print()

ALL_CHECKS = [
    ("PDF exists", PDF_PATH.exists()),
    ("HTML exists", HTML_PATH.exists()),
    ("Markdown exists", MD_PATH.exists()),
    ("PDF >= 20 pages", page_count >= 20),
    ("PDF > 200 KB", pdf_size > 200_000),
    ("MD sections >= 16", h2_count >= 16),
    ("MD mermaid >= 16", mermaid_count >= 16),
    ("MD KPI tables >= 16", kpi_tables >= 16),
]

all_pass = True
print("  Checks:")
for label, passed in ALL_CHECKS:
    status = "PASS" if passed else "FAIL"
    if not passed:
        all_pass = False
    print(f"    [{status}] {label}")

print()
if all_pass:
    print("  RESULT: ALL CHECKS PASSED")
else:
    print("  RESULT: SOME CHECKS FAILED")
    exit(1)
