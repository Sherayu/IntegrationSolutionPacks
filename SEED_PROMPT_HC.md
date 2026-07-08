# Seed Prompt — Generate All Artefacts

## Configuration Block (only these fields to change)

```yaml
business_domain: "Health Care"
framework_name: "HL7 FHIR R5 / HIMSS Healthcare Capability Model"
framework_version: "HIMSS Healthcare Capability Model v1.0"
capability_prefix: "HC"
generated_date: "2026-07-08"
```

## Instructions

Using the configuration block above, generate a complete set of artefacts inside a folder named `<business_domain>/` (e.g. `Healthcare/`). **Everything other than the five configuration fields must be researched from public sources.**

### Research Phase

For the given `business_domain`, perform web research to determine:

1. **Industry reference model** — Search for standard capability/reference models for this domain (e.g. for Higher Education: CAUDIT HERM; for Healthcare: APQC Healthcare PCF; for Banking: BIAN; for Government: FEA BRM). If `framework_name` is provided, look up its official capability catalog. Use the `capability_prefix` for code formatting.

2. **Domain sections** — Identify the primary functional areas (8-20 sections) that cover the domain end-to-end. Each section should have 1-10 sub-flows. For each sub-flow, define:
   - A sequence of 10-30 realistic system-to-system interactions
   - Source and target systems (use well-known vendor products for the domain)
   - Connector protocols (REST, SOAP, OData, SFTP, CDC, JDBC, GraphQL, etc.)
   - Integration patterns (API-led Real-time, Event-driven, Batch Scheduled, Batch ETL, Database Replication CDC)
   - Complexity ratings (Simple / Medium / High)

3. **Capability model** — If `framework_name` is provided, look up the official capability catalog and include all levels. Otherwise, derive a reasonable capability model from standard domain taxonomies.

4. **Test data** — Generate 5-50 entity types with realistic field names and values that are used consistently across all diagrams (e.g. for a Patient entity: id, name, dob, mrn, etc.).

5. **Public domain-overview diagram** — Find a publicly available diagram/image that shows the capability model overview for this domain. Use it in the README and credit the source.

6. **Acceptance Criteria** - Include appropriate acceptance criterias that are relevant for the information flows and list them in a table in each sub-section after the table listing the integrations.

### Folder Structure

```
<domain>/                  # e.g. Healthcare/
  README.md                # Master document (~1000 lines markdown)
  Scripts/
    render_pdf.py          # Converts README.md → PDF
    add_capability_model.py # Injects capability model into README
  Diagrams/
    diagram_0.html .. diagram_N.html   # Standalone HTML per flow
  Document/
    <domain>-process-flows.pdf         # Final PDF
    <domain>-brm-overview.png          # Framework overview image
  Catalogue/
    integration-details.xlsx           # Integration tables
  Test/
    verify_pdf.py                      # Verification
    test_mermaid.py                    # Debugging
    test_single.html                   # Manual test
```

### Artefacts to Generate

---

#### 1. README.md — Master Document

```markdown
# {business_domain} Process Flows — {framework_name}
> Generated on {generated_date} | Domain: {business_domain} | Framework: {framework_name}
```

##### Capability Model Reference section (## heading)
- Download a public diagram of the capability/process model for this domain → `Document/<domain>-brm-overview.png`
- Display it in the README with source credit
- For each Level-1 domain in the researched capability model, create a `###` sub-section with a markdown table: | Capability | Code | Description |

##### Table of Contents (## heading)
- List every section and sub-flow with anchor links
- Append capability codes: `[Section Name  - HCxxx, HCyyy](#...)`

##### Test Data (## heading)
- Render the researched test data as a table: | Entity | Field | Value |

##### Domain Sections (one # heading per section)
For each researched section:
1. `# {section.name}  - {capability coded badges}`
2. Description paragraph
3. For each sub-flow:
   - `### {id} {title}`
   - Description, Actors, Systems lines
   - `#### Sequence Diagram` — mermaid `sequenceDiagram` block with 10-20 interaction steps
   - `#### Integration Details` — table: | Flow | Entity | Info Flow | Source | Target | Source Conn | Target Conn | Pattern | Complexity |
4. `---` separator between sections

---

#### 2. Scripts/render_pdf.py

Python script (using `markdown-it-py`, Playwright) that:

1. Reads `README.md`, renders to HTML
2. Converts `<pre><code class="language-mermaid">` → `<div class="mermaid">`
3. Injects page breaks before `## Table of Contents` and each domain `#` heading (after first)
4. Wraps in print-styled HTML — A4 landscape, Segoe UI 8pt, table styling, `page-break-inside: avoid` on mermaid/tables, `max-width: 100%` on images and SVGs
5. Uses Playwright headless Chromium to:
   - Render mermaid → SVG (`theme: neutral`, `sequence: { showSequenceNumbers: false, mirrorActors: true }`)
   - Generate PDF with custom header (`{Domain} Process Flows` / `{Framework}`) and footer (`Generated {date}` / `Page X of Y`)
   - use `display_header_footer=True`, `margin={"top": "22mm", "bottom": "18mm", "left": "8mm", "right": "8mm"}`
6. Verify page count, clean up temp file

---

#### 3. Scripts/add_capability_model.py

Injects the capability model into README.md:
- Locates the `> Generated` metadata line and `## Table of Contents` heading
- Inserts the researched capability reference section between them
- Adds capability code badges to section headings
- Updates TOC entries with codes

---

#### 4. Diagrams/diagram_N.html

One standalone HTML file per sub-flow, each containing a single mermaid diagram with auto-render.

---

#### 5. Document/{domain}-process-flows.pdf

Generated by `render_pdf.py` — A4 landscape, all diagrams as vector graphics, section page breaks, header/footer.

---

#### 6. Catalogue/integration-details.xlsx

Excel workbook with one worksheet per domain section, columns: Flow Name | Entity | Info Flow Name | Source System | Target System | Source Connector | Target Connector | Integration Pattern | Complexity

---

#### 7. Test/ Scripts

- `verify_pdf.py` — reads PDF, counts pages, checks mermaid count
- `test_mermaid.py` — extracts mermaid blocks, checks for problematic characters
- `test_single.html` — renders one mermaid diagram for manual testing

---

### Build Pipeline

```
add_capability_model.py → README.md → render_pdf.py → Document/{domain}-process-flows.pdf
```

Run order:
```bash
python Scripts/add_capability_model.py
python Scripts/render_pdf.py
```

### Dependencies

```txt
markdown-it-py>=3.0.0
playwright>=1.40.0
openpyxl>=3.1.0
```

After pip install, run `playwright install chromium`.
