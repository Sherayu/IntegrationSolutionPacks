"""Verify Insurance PDF structure and content."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PDF_PATH = ROOT / "Document" / "insurance-domain-process-flows.pdf"
README_PATH = ROOT / "README.md"

print("=" * 60)
print("  PDF VERIFICATION")
print("=" * 60)

if not PDF_PATH.exists():
    print(f"  FAIL: PDF not found at {PDF_PATH}")
    exit(1)

pdf_size = PDF_PATH.stat().st_size
with open(PDF_PATH, "rb") as f:
    data = f.read()
    page_count = data.count(b"/Type /Page") - data.count(b"/Type /Pages")

print(f"  PDF:    {PDF_PATH.name}")
print(f"  Size:   {pdf_size / 1024:.0f} KB")
print(f"  Pages:  {page_count}")
print()

if not README_PATH.exists():
    print(f"  FAIL: README not found at {README_PATH}")
    exit(1)

readme_text = README_PATH.read_text(encoding="utf-8")
readme_lines = readme_text.split("\n")

h1_count = sum(1 for l in readme_lines if l.strip().startswith("# ") and not l.strip().startswith("## "))
h3_count = sum(1 for l in readme_lines if l.strip().startswith("### ") and not l.strip().startswith("#### "))
mermaid_count = readme_text.count("```mermaid")
int_tables = readme_text.count("| Flow | Entity | Info Flow")
ac_tables = readme_text.count("| Flow | Entity | Acceptance")

print(f"  README: {README_PATH.name}")
print(f"  Lines:      {len(readme_lines)}")
print(f"  Sections:   {h1_count}")
print(f"  Sub-flows:  {h3_count}")
print(f"  Mermaid:    {mermaid_count}")
print(f"  Int Tables: {int_tables}")
print(f"  AC Tables:  {ac_tables}")
print()

ALL_CHECKS = [
    ("Sections >= 16", h1_count >= 17),
    ("Sub-flows >= 80", h3_count >= 80),
    ("Mermaid >= 80", mermaid_count >= 80),
    ("Integration Tables >= 80", int_tables >= 80),
    ("PDF exists", PDF_PATH.exists()),
    ("PDF pages >= 20", page_count >= 20),
    ("PDF size > 1MB", pdf_size > 1_000_000),
]

print("  Checks:")
all_pass = True
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
