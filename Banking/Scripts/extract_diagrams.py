import re
from pathlib import Path
import html

readme = Path("D:/RakeshPractice/AIProjects/FunctionalFlows/Banking/README.md").read_text(encoding="utf-8")

pattern = r"```mermaid\n(.*?)```"
matches = re.findall(pattern, readme, re.DOTALL)

diagrams_dir = Path("D:/RakeshPractice/AIProjects/FunctionalFlows/Banking/Diagrams")

for i, mermaid_code in enumerate(matches):
    code = mermaid_code.strip()
    escaped = html.escape(code)

    html_content = (
        '<!DOCTYPE html>\n'
        '<html><head><meta charset="UTF-8">\n'
        '<script src="https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.min.js"></script>\n'
        '<style>body{margin:0;padding:10px;background:white}div.mermaid{text-align:center}</style>\n'
        '</head><body>\n'
        '<div class="mermaid" id="d">' + escaped + '</div>\n'
        '<script>\n'
        'async function r(){\n'
        '    await mermaid.initialize({startOnLoad:false,theme:"neutral",sequence:{showSequenceNumbers:false,mirrorActors:true},securityLevel:"loose"});\n'
        '    var div = document.getElementById("d");\n'
        '    var svg = await mermaid.render("svg-0", div.textContent);\n'
        '    div.innerHTML = svg.svg;\n'
        '}\n'
        'r();\n'
        '</script>\n'
        '</body></html>'
    )

    filepath = diagrams_dir / f"diagram_{i}.html"
    filepath.write_text(html_content, encoding="utf-8")
    print(f"diagram_{i}.html ({len(code)} chars)")

print(f"\nTotal: {len(matches)} diagram files created")
