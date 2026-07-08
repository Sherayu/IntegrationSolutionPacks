"""Extract mermaid blocks from README.md and generate standalone HTML diagram files."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
readme_path = ROOT / "README.md"
diagrams_dir = ROOT / "Diagrams"

TEMPLATE = """<!DOCTYPE html>
<html><head><meta charset="UTF-8">
<script src="https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.min.js"></script>
<style>body{{margin:0;padding:10px;background:white}}div.mermaid{{text-align:center}}</style>
</head><body>
<div class="mermaid" id="d">{content}</div>
<script>
async function r(){{
    await mermaid.initialize({{startOnLoad:false,theme:"neutral",sequence:{{showSequenceNumbers:false,mirrorActors:true}},securityLevel:"loose"}});
    var div = document.getElementById("d");
    var svg = await mermaid.render("svg-0", div.textContent);
    div.innerHTML = svg.svg;
}}
r();
</script>
</body></html>"""

text = readme_path.read_text(encoding="utf-8")
pattern = r"```mermaid\n(.*?)```"
blocks = re.findall(pattern, text, re.DOTALL)

print(f"Found {len(blocks)} mermaid blocks")

for i, block in enumerate(blocks):
    content = block.strip()
    html = TEMPLATE.format(content=content)
    filepath = diagrams_dir / f"diagram_{i}.html"
    filepath.write_text(html, encoding="utf-8")
    print(f"  Written: {filepath.name} ({len(content)} chars)")

print(f"\nTotal: {len(blocks)} diagram files generated in {diagrams_dir}")
