import re
with open(r'D:\RakeshPractice\AIProjects\FunctionalFlows\Banking\README.md', encoding='utf-8') as f:
    content = f.read()
ct = len(re.findall(r'```mermaid', content))
print(f'Total mermaid diagrams: {ct}')

from pathlib import Path
pdf_path = Path(r'D:\RakeshPractice\AIProjects\FunctionalFlows\Banking\Document\banking-process-flows.pdf')
if pdf_path.exists():
    pdf_content = pdf_path.read_bytes()
    pdf_text = pdf_content.decode('latin-1')
    svg_count = pdf_text.count('svg')
    print(f'PDF file size: {len(pdf_content)/1024:.0f} KB')
    print(f'SVG references in PDF: {svg_count}')
    if svg_count > 5:
        print('SUCCESS: PDF contains rendered SVG diagrams')
    else:
        print('WARNING: PDF may not have rendered diagram images')
else:
    print('PDF not yet generated - run render_pdf.py first')
