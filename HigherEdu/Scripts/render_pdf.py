import re
from pathlib import Path
from markdown_it import MarkdownIt

ROOT = Path(__file__).resolve().parent.parent
readme = (ROOT / "README.md").read_text(encoding="utf-8")
md = MarkdownIt("gfm-like", {"breaks": True, "html": True, "linkify": False})
html_body = md.render(readme)

# Convert <pre><code class="language-mermaid"> to <div class="mermaid">
html_body = re.sub(
    r'<pre><code class="language-mermaid">(.*?)</code></pre>',
    r'<div class="mermaid">\1</div>',
    html_body,
    flags=re.DOTALL,
)

html_body = html_body.replace("<table>", '<table class="table">')

# Count mermaid divs
mermaid_count = html_body.count('class="mermaid"')
print(f"Mermaid divs: {mermaid_count}")

page_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Higher Education Process Flows - CAUDIT HERM</title>
<script src="https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.min.js"></script>
<style>
  @page {{ size: A4 landscape; margin: 10mm; }}
  body {{ font-family: 'Segoe UI', Arial, sans-serif; font-size: 8pt; color: #222; line-height: 1.35; }}
  h1 {{ font-size: 14pt; color: #1a3c6e; border-bottom: 2px solid #1a3c6e; padding-bottom: 3px; }}
  h2 {{ font-size: 12pt; color: #2b5797; margin-top: 14px; }}
  h3 {{ font-size: 10pt; color: #3b6cb0; }}
  h4 {{ font-size: 9pt; color: #444; }}
  table {{ border-collapse: collapse; width: 100%; margin: 4px 0; font-size: 6.5pt; }}
  th, td {{ border: 1px solid #aaa; padding: 2px 4px; text-align: left; }}
  th {{ background: #1a3c6e; color: #fff; }}
  tr:nth-child(even) {{ background: #f0f4fa; }}
  code {{ background: #eef; padding: 1px 3px; font-size: 7pt; }}
  pre {{ background: #f5f5f5; border: 1px solid #ddd; padding: 4px; overflow-x: auto; }}
  hr {{ border: none; border-top: 1px solid #ccc; margin: 10px 0; }}
  .mermaid {{ page-break-inside: avoid; margin: 10px 0; }}
</style>
</head>
<body>
{html_body}
<script>
async function renderAll() {{
    try {{
        await mermaid.initialize({{startOnLoad:false,theme:"neutral",sequence:{{showSequenceNumbers:false,mirrorActors:true}},securityLevel:"loose"}});
        var divs = document.querySelectorAll("div.mermaid");
        for(var i=0; i<divs.length; i++) {{
            try {{
                var result = await mermaid.render("svg-"+i, divs[i].textContent);
                divs[i].innerHTML = result.svg;
            }} catch(e) {{
                divs[i].innerHTML = "<div style='color:red'>"+e.message.substring(0,100)+"</div>";
            }}
        }}
    }} catch(e) {{ console.error(e); }}
    document.body.setAttribute("data-done","1");
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
    
    # Check rendered count
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

    # Simple full-page screenshot
    page.screenshot(path=str(ROOT / "_full_page.png"), full_page=True)
    print("Full page screenshot saved")
    
    # Generate PDF
    out_pdf = str(ROOT / "Document" / "higher-education-process-flows.pdf")
    page.pdf(
        path=out_pdf,
        format="A4",
        landscape=True,
        margin={"top": "8mm", "bottom": "8mm", "left": "8mm", "right": "8mm"},
        print_background=True,
    )
    print(f"PDF generated: {out_pdf}")
    
    browser.close()

# Verify
pdf_size = Path(out_pdf).stat().st_size
with open(out_pdf, "rb") as f:
    data = f.read()
text = data.decode("latin-1")
svg_count = text.count("<svg")
print(f"PDF size: {pdf_size/1024:.0f} KB, SVG in PDF: {svg_count}")

html_path.unlink(missing_ok=True)

if svg_count >= 20:
    print("SUCCESS: All diagrams rendered as SVG in PDF!")
else:
    print(f"WARNING: Only {svg_count} SVGs found - trying alternative...")
