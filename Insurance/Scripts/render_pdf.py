"""Render Insurance README.md to PDF with Mermaid diagrams."""

import re
from pathlib import Path
from markdown_it import MarkdownIt

ROOT = Path(__file__).resolve().parent.parent
readme = (ROOT / "README.md").read_text(encoding="utf-8")
md = MarkdownIt("gfm-like", {"breaks": True, "html": True, "linkify": False})
html_body = md.render(readme)

html_body = re.sub(
    r'<pre><code class="language-mermaid">(.*?)</code></pre>',
    r'<div class="mermaid">\1</div>',
    html_body,
    flags=re.DOTALL,
)

html_body = html_body.replace("<table>", '<table class="table">')

html_body = html_body.replace(
    '<h2>Table of Contents</h2>',
    '<h2 class="page-break-before">Table of Contents</h2>',
)

h1_pattern = re.compile(r'<h1[^>]*>')
matches = list(h1_pattern.finditer(html_body))
for m in matches[1:]:
    pos = m.start()
    html_body = html_body[:pos] + '<div class="page-break-before"></div>' + html_body[pos:]

mermaid_count = html_body.count('class="mermaid"')
print(f"Mermaid divs: {mermaid_count}")

header_template = '''
<div style="width:100%; font-size:7pt; font-family:'Segoe UI',Arial,sans-serif; color:#1a3c6e; border-bottom:0.5pt solid #1a3c6e; padding:2mm 0; margin:0 8mm;">
  <span style="float:left; font-weight:600;">Insurance Domain Process Flows</span>
  <span style="float:right;">ACORD Capability Model Reference</span>
</div>
'''

footer_template = '''
<div style="width:100%; font-size:6.5pt; font-family:'Segoe UI',Arial,sans-serif; color:#888; border-top:0.5pt solid #ccc; padding:1.5mm 0; margin:0 8mm;">
  <span style="float:left;">Generated 2026-07-09</span>
  <span style="float:right;">Page <span class="pageNumber"></span> of <span class="totalPages"></span></span>
</div>
'''

page_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Insurance Domain Process Flows - ACORD</title>
<script src="https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.min.js"></script>
<style>
  @page {{ size: A4 landscape; }}
  * {{ box-sizing: border-box; }}
  body {{
    font-family: 'Segoe UI', Arial, sans-serif;
    font-size: 8pt;
    color: #222;
    line-height: 1.4;
    margin: 0;
    padding: 0;
  }}
  h1 {{
    font-size: 14pt;
    color: #1a3c6e;
    border-bottom: 2px solid #1a3c6e;
    padding-bottom: 3px;
    margin-top: 3mm;
    page-break-before: always;
  }}
  h1:first-of-type {{ page-break-before: avoid; margin-top: 0; }}
  h2 {{
    font-size: 12pt;
    color: #2b5797;
    margin-top: 4mm;
    page-break-after: avoid;
  }}
  h3 {{ font-size: 10pt; color: #3b6cb0; page-break-after: avoid; margin-top: 3mm; }}
  h4 {{ font-size: 9pt; color: #444; page-break-after: avoid; }}
  p {{ margin: 1.5mm 0; }}
  table {{
    border-collapse: collapse;
    width: 100%;
    margin: 3px 0;
    font-size: 6.5pt;
    page-break-inside: avoid;
  }}
  th, td {{ border: 0.5pt solid #aaa; padding: 1.5px 3px; text-align: left; }}
  th {{ background: #1a3c6e; color: #fff; font-weight: 600; }}
  tr:nth-child(even) {{ background: #f0f4fa; }}
  code {{ background: #eef; padding: 1px 3px; font-size: 7pt; border-radius: 2px; }}
  pre {{
    background: #f5f5f5;
    border: 0.5pt solid #ddd;
    padding: 3px;
    overflow-x: auto;
    page-break-inside: avoid;
    font-size: 7pt;
  }}
  hr {{ border: none; border-top: 0.5pt solid #ccc; margin: 6px 0; }}
  img {{ max-width: 100%; height: auto; page-break-inside: avoid; display: block; margin: 4mm auto; }}
  blockquote {{ margin: 2mm 0; padding: 1mm 3mm; border-left: 3px solid #2b5797; background: #f8faff; font-style: italic; color: #555; }}
  ul, ol {{ margin: 1.5mm 0; padding-left: 5mm; }}
  li {{ margin: 0.5mm 0; }}
  .mermaid {{ page-break-inside: avoid; margin: 6px 0; max-width: 100%; overflow: hidden; }}
  .mermaid svg {{ max-width: 100%; height: auto; }}
  .page-break-before {{ page-break-before: always; }}
  .table {{ page-break-inside: avoid; }}
</style>
</head>
<body>
{html_body}
<script>
async function renderAll() {{
    try {{
        await mermaid.initialize({{
            startOnLoad: false,
            theme: "neutral",
            sequence: {{ showSequenceNumbers: false, mirrorActors: true }},
            securityLevel: "loose",
        }});
        var divs = document.querySelectorAll("div.mermaid");
        for (var i = 0; i < divs.length; i++) {{
            try {{
                var result = await mermaid.render("svg-" + i, divs[i].textContent);
                divs[i].innerHTML = result.svg;
            }} catch (e) {{
                divs[i].innerHTML = "<div style='color:red;padding:4px;'>Render error: " + e.message.substring(0, 120) + "</div>";
            }}
        }}
    }} catch (e) {{ console.error(e); }}
    document.body.setAttribute("data-done", "1");
}}
renderAll();
</script>
</body>
</html>"""

html_path = ROOT / "_full_render.html"
html_path.write_text(page_html, encoding="utf-8")
print(f"HTML written ({len(page_html)} bytes)")

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(viewport={"width": 1280, "height": 900})

    page.goto(html_path.as_uri(), wait_until="load", timeout=120000)
    print("Page loaded, waiting for mermaid rendering...")

    try:
        page.wait_for_function(
            "() => document.body.getAttribute('data-done') === '1'",
            timeout=120000,
        )
        print("All mermaid rendered")
    except:
        print("Timeout, checking partial results...")

    result = page.evaluate("""
        () => {
            const divs = document.querySelectorAll('div.mermaid');
            let ok = 0, err = 0;
            divs.forEach(d => {
                if (d.querySelector('svg')) ok++;
                else err++;
            });
            return {total: divs.length, ok, err};
        }
    """)
    print(f"Mermaid render: {result}")

    out_pdf = str(ROOT / "Document" / "insurance-domain-process-flows.pdf")
    page.pdf(
        path=out_pdf,
        format="A4",
        landscape=True,
        margin={"top": "22mm", "bottom": "18mm", "left": "8mm", "right": "8mm"},
        print_background=True,
        display_header_footer=True,
        header_template=header_template,
        footer_template=footer_template,
    )
    print(f"PDF generated: {out_pdf}")

    browser.close()

pdf_size = Path(out_pdf).stat().st_size
page_count = 0
with open(out_pdf, "rb") as f:
    data = f.read()
    page_count = data.count(b"/Type /Page") - data.count(b"/Type /Pages")
print(f"PDF: {pdf_size/1024:.0f} KB, {page_count} pages, mermaid: {result['ok']}/{result['total']} OK")

if result["err"] > 0:
    err_log = ROOT / "_mermaid_errors.txt"
    with open(html_path, encoding="utf-8") as f:
        err_html = f.read()
    errs = re.findall(r'Render error: ([^<]+)', err_html)
    err_log.write_text("\n".join(f"#{i}: {e}" for i, e in enumerate(errs)), encoding="utf-8")
    print(f"Mermaid error log: {err_log}")
else:
    html_path.unlink(missing_ok=True)

if result["ok"] == result["total"] and result["total"] > 0:
    print(f"SUCCESS: All {result['total']} mermaid diagrams rendered in PDF ({page_count} pages)!")
else:
    print(f"WARNING: {result['err']} diagrams failed to render")
