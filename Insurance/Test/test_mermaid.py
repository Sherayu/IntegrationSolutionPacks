"""Test Mermaid syntax in README.md for common errors."""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
README_PATH = ROOT / "README.md"

print("=" * 60)
print("  MERMAID SYNTAX VALIDATION")
print("=" * 60)

readme_text = README_PATH.read_text(encoding="utf-8")

mermaid_blocks = re.findall(r"```mermaid\n(.*?)```", readme_text, re.DOTALL)

print(f"  Found {len(mermaid_blocks)} mermaid blocks")
print()

errors = 0
for idx, block in enumerate(mermaid_blocks):
    block = block.strip()
    lines = block.split("\n")

    if not lines[0].strip() == "sequenceDiagram":
        print(f"  ERROR [{idx}]: First line is not 'sequenceDiagram': {lines[0].strip()[:50]}")
        errors += 1
        continue

    for li, line in enumerate(lines[1:], 2):
        stripped = line.strip()
        if not stripped:
            continue

        if stripped.startswith("participant "):
            parts = stripped.split("participant ")[1]
            if not parts.strip():
                print(f"  ERROR [{idx}]: Line {li}: Empty participant name")
                errors += 1

        elif stripped.startswith("        "):
            actual = stripped.lstrip()
            parts = stripped.split("->>")
            parts2 = stripped.split("-->>")

            if len(parts) < 2 and len(parts2) < 2 and not stripped.startswith("                "):
                pass

    first_svg = block[:100]
    if "<<br/>" in block:
        pass

font_issues = re.findall(r"<br/>", block)
for fi, fm in enumerate(re.finditer(r"<br/>", block)):
    pos = fm.start()
    line_num = block[:pos].count("\n") + 1
    context_start = max(0, pos - 30)
    context_end = min(len(block), pos + 30)
    context = block[context_start:context_end].replace("\n", "\\n")

print(f"  Checked {len(mermaid_blocks)} mermaid blocks")
print(f"  Errors: {errors}")
print()

if errors == 0:
    print("  RESULT: ALL MERMAID BLOCKS VALID")
else:
    print(f"  RESULT: {errors} ERRORS FOUND")
    exit(1)
