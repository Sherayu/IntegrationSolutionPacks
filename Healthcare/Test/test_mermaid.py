"""Test mermaid rendering in Playwright - find the actual errors"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
readme = (ROOT / "README.md").read_text(encoding="utf-8")

from markdown_it import MarkdownIt
md = MarkdownIt("gfm-like", {"breaks": True, "html": True, "linkify": False})
html_body = md.render(readme)

# Extract all mermaid raw code blocks BEFORE HTML escaping
mermaid_sources = re.findall(
    r'<pre><code class="language-mermaid">(.*?)</code></pre>',
    html_body,
    flags=re.DOTALL,
)
print(f"Found {len(mermaid_sources)} mermaid code blocks\n")

for i, src in enumerate(mermaid_sources):
    src = src.strip()
    lines = src.split('\n')
    if lines and re.match(r'^\w+$', lines[0].strip()):
        src = '\n'.join(lines[1:]).strip()
    
    problems = []
    if '$' in src:
        problems.append("contains '$'")
    if '&lt;' in src or '&gt;' in src or '&amp;' in src:
        problems.append("contains HTML entities")
    if 'nbsp' in src:
        problems.append("contains nbsp")
    
    print(f"Diagram {i+1}: {len(src)} chars, {problems if problems else 'clean'}")
    print(f"  First 100: {src[:100]}")
    print()

# Now test the first diagram with mermaid via Playwright
html_test = """<!DOCTYPE html>
<html><head>
<script src="https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.min.js"></script>
</head><body>
<div id="test"></div>
<script>
async function test() {
    const div = document.getElementById('test');
    const src = `""" + mermaid_sources[0].strip().split('\n', 1)[1] + """`;
    try {
        mermaid.initialize({startOnLoad: false, theme: 'neutral', securityLevel: 'loose'});
        const result = await mermaid.render('test-svg', src);
        div.innerHTML = result.svg;
        div.innerHTML += '<div style="color:green">SUCCESS</div>';
    } catch(e) {
        div.innerHTML = '<div style="color:red">Error: ' + e.message + '</div>';
    }
}
test();
</script>
</body></html>"""

test_path = ROOT / "Test" / "test_mermaid.html"
test_path.write_text(html_test, encoding="utf-8")

from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto(f"file:///{test_path.as_posix()}", wait_until="networkidle")
    page.wait_for_timeout(10000)
    result = page.evaluate("() => document.getElementById('test').innerHTML")
    print(f"Test result: {result[:500]}")
    browser.close()
