import re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
readme = (ROOT / "README.md").read_text(encoding="utf-8")

mermaid_blocks = re.findall(r'```mermaid\n(.*?)```', readme, re.DOTALL)
print(f"Found {len(mermaid_blocks)} mermaid blocks")

errors = []
for i, block in enumerate(mermaid_blocks):
    lines = block.strip().split("\n")
    if not lines[0].startswith("sequenceDiagram"):
        errors.append(f"Block {i}: first line is not 'sequenceDiagram': {lines[0][:60]}")
        continue
    for j, line in enumerate(lines[1:], 2):
        stripped = line.strip()
        if not stripped:
            continue
        if "<br/>" in stripped:
            parts = stripped.split("<br/>", 1)
            main_part = parts[0]
        else:
            main_part = stripped
        if not re.match(r'^(?:[A-Za-z0-9_\-]+|"[^"]*")->>(?:[A-Za-z0-9_\-]+|"[^"]*"):', main_part):
            errors.append(f"Block {i}, line {j}: invalid syntax: {stripped[:80]}")

if errors:
    for e in errors[:10]:
        print(f"  ERROR: {e}")
    if len(errors) > 10:
        print(f"  ... and {len(errors)-10} more errors")
    print(f"FAILED: {len(errors)} validation errors")
    sys.exit(1)
else:
    print("SUCCESS: All mermaid blocks have valid syntax")
