import re
from pathlib import Path

OUT = Path(r"D:\RakeshPractice\AIProjects\FunctionalFlows\Banking")
readme = (OUT / "README.md").read_text(encoding="utf-8")

from markdown_it import MarkdownIt
md = MarkdownIt("gfm-like", {"breaks": True, "html": True, "linkify": False})
html_body = md.render(readme)

mermaid_sources = re.findall(
    r'<pre><code class="language-mermaid">(.*?)</code></pre>',
    html_body,
    flags=re.DOTALL,
)
print(f"Found {len(mermaid_sources)} mermaid code blocks\n")

for i, src in enumerate(mermaid_sources):
    src = src.strip()
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

test_path = OUT / "Test" / "test_mermaid.html"
test_path.write_text(html_test, encoding="utf-8")
print(f"Test HTML written to {test_path}")
