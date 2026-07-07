import re
with open(r'D:\RakeshPractice\AIProjects\FunctionalFlows\Utilities\_full_render.html', encoding='utf-8') as f:
    content = f.read()
ct = len(re.findall(r'<div class="mermaid">', content))
cc = len(re.findall(r'language-mermaid', content))
cs = len(re.findall(r'<svg', content))
print(f'div.mermaid elements: {ct}')
print(f'code.language-mermaid elements: {cc}')
print(f'svg elements in HTML: {cs}')
print(f'HTML size: {len(content)/1024:.0f} KB')

with open(r'D:\RakeshPractice\AIProjects\FunctionalFlows\Utilities\Document\utilities-process-flows.pdf', 'rb') as f:
    pdf_content = f.read()
pdf_text = pdf_content.decode('latin-1')
svg_count = pdf_text.count('svg')
mermaid_text_count = pdf_text.count('sequenceDiagram')
print(f'PDF file size: {len(pdf_content)/1024:.0f} KB')
print(f'SVG references in PDF: {svg_count}')
print(f'Mermaid script text in PDF: {mermaid_text_count}')
if svg_count > 5:
    print('SUCCESS: PDF contains rendered SVG diagrams')
else:
    print('WARNING: PDF may not have rendered diagram images')
