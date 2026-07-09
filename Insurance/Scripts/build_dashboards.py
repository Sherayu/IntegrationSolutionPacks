"""Generate Insurance Analytics Dashboard catalogue — HTML and Markdown outputs."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DASH_DIR = ROOT / "Dashboard"
DASH_DIR.mkdir(parents=True, exist_ok=True)

from analytics_dashboards import DASHBOARDS

# ── ACORD colour groups ─────────────────────────────────────────
ACORD_GROUPS = {
    "IN001": "#1a3c6e", "IN002": "#1a3c6e", "IN003": "#1a3c6e", "IN004": "#1a3c6e",
    "IN005": "#2e7d32", "IN006": "#2e7d32", "IN007": "#2e7d32", "IN008": "#2e7d32",
    "IN009": "#e65100", "IN010": "#e65100", "IN011": "#e65100", "IN012": "#e65100",
    "IN013": "#01579b", "IN014": "#01579b", "IN015": "#01579b",
    "IN016": "#c62828", "IN017": "#c62828", "IN018": "#c62828", "IN019": "#c62828",
    "IN020": "#4a148c", "IN021": "#4a148c", "IN022": "#4a148c",
    "IN023": "#00695c", "IN024": "#00695c", "IN025": "#00695c",
    "IN031": "#f57f17",
    "IN026": "#ad1457", "IN027": "#ad1457",
    "IN028": "#37474f", "IN029": "#37474f", "IN030": "#37474f",
    "IN032": "#0d47a1",
    "IN033": "#33691e",
    "IN034": "#b71c1c",
    "IN035": "#4e342e",
    "IN036": "#004d40",
}

def esc_pipe(val):
    return str(val).replace("|", "\\|")

# ═══════════════════════════════════════════════════════════════
#  HTML GENERATOR
# ═══════════════════════════════════════════════════════════════

def gen_html():
    dash_cards = []
    for d in DASHBOARDS:
        codes_html = " ".join(
            f'<span class="acord-badge" style="background:{ACORD_GROUPS.get(c,"#888")}">{c}</span>'
            for c in d["acord_codes"]
        )
        kpi_rows = "".join(
            f"<tr><td>{esc_pipe(k[0])}</td><td>{esc_pipe(k[1])}</td>"
            f"<td>{esc_pipe(k[2])}</td><td>{esc_pipe(k[3])}</td>"
            f"<td>{esc_pipe(k[4])}</td><td><span class='reg-ref'>{esc_pipe(k[5])}</span></td></tr>"
            for k in d["kpis"]
        )
        mermaid_code = "\n".join(d["mermaid"])
        mermaid_b64 = __import__("base64").b64encode(mermaid_code.encode()).decode()

        dash_cards.append(f"""
<div class="dash-card" data-acord="{','.join(d['acord_codes'])}" data-id="{d['id']}">
  <div class="dash-header">
    <h2>{esc_pipe(d['title'])}</h2>
    <div class="acord-row">{codes_html}</div>
  </div>
  <div class="dash-body">
    <p class="dash-desc">{esc_pipe(d['description'])}</p>
    <div class="dash-meta"><strong>Question:</strong> {esc_pipe(d['business_question'])} &nbsp;|&nbsp; <strong>Owner:</strong> {esc_pipe(d['owner'])}</div>
    <div class="dash-meta"><strong>Filters:</strong> {', '.join(d['filters'])} &nbsp;|&nbsp; <strong>Drill-down:</strong> {d['drill_down']}</div>
    <div class="kpi-section">
      <h3 onclick="this.nextElementSibling.classList.toggle('hidden');this.classList.toggle('expanded');">
        <span class="kpi-toggle">&#9654;</span> KPIs ({len(d['kpis'])})
      </h3>
      <table class="kpi-table hidden">
        <thead><tr><th>KPI</th><th>Formula / Source</th><th>Chart</th><th>Source System</th><th>Refresh</th><th>Reg Ref</th></tr></thead>
        <tbody>{kpi_rows}</tbody>
      </table>
    </div>
    <div class="mermaid-section">
      <h3 onclick="this.nextElementSibling.classList.toggle('hidden');this.classList.toggle('expanded');">
        <span class="kpi-toggle">&#9654;</span> Data Flow
      </h3>
      <div class="mermaid-container hidden">
        <div class="mermaid">{mermaid_code}</div>
      </div>
    </div>
  </div>
</div>""")

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Insurance Analytics Dashboards — ACORD Reference</title>
<script src="https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.min.js"></script>
<style>
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{ font-family: 'Segoe UI', Arial, sans-serif; background: #f0f2f5; color: #222; padding: 20px; }}
  .header {{ background: #1a3c6e; color: #fff; padding: 18px 28px; border-radius: 10px; margin-bottom: 20px; }}
  .header h1 {{ font-size: 22pt; margin: 0; }}
  .header p {{ font-size: 10pt; opacity: 0.85; margin-top: 4px; }}
  .filters {{ display: flex; gap: 12px; margin-bottom: 20px; flex-wrap: wrap; }}
  .filters input {{ flex: 1; min-width: 200px; padding: 10px 14px; border: 1px solid #ccc; border-radius: 6px; font-size: 10pt; }}
  .filters select {{ padding: 10px 14px; border: 1px solid #ccc; border-radius: 6px; font-size: 10pt; background: #fff; }}
  .dash-grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(480px, 1fr)); gap: 16px; }}
  .dash-card {{ background: #fff; border-radius: 10px; box-shadow: 0 1px 4px rgba(0,0,0,0.08); overflow: hidden; }}
  .dash-header {{ padding: 14px 18px; background: linear-gradient(135deg, #f8f9fa 0%, #eef1f5 100%); border-bottom: 1px solid #e0e0e0; }}
  .dash-header h2 {{ font-size: 12pt; margin: 0 0 6px 0; color: #1a3c6e; }}
  .acord-row {{ display: flex; gap: 4px; flex-wrap: wrap; }}
  .acord-badge {{ font-size: 7pt; color: #fff; padding: 2px 7px; border-radius: 3px; font-weight: 600; }}
  .dash-body {{ padding: 12px 18px 18px; }}
  .dash-desc {{ font-size: 8pt; color: #555; line-height: 1.5; margin-bottom: 8px; }}
  .dash-meta {{ font-size: 7.5pt; color: #666; margin-bottom: 4px; }}
  .kpi-section h3, .mermaid-section h3 {{ font-size: 9pt; color: #1a3c6e; cursor: pointer; padding: 6px 0; user-select: none; }}
  .kpi-toggle {{ transition: transform 0.2s; display: inline-block; margin-right: 6px; }}
  h3.expanded .kpi-toggle {{ transform: rotate(90deg); }}
  .hidden {{ display: none; }}
  .kpi-table {{ width: 100%; border-collapse: collapse; font-size: 7pt; margin: 6px 0; }}
  .kpi-table th {{ background: #1a3c6e; color: #fff; padding: 4px 6px; text-align: left; }}
  .kpi-table td {{ padding: 3px 6px; border-bottom: 1px solid #e0e0e0; }}
  .kpi-table tr:nth-child(even) {{ background: #f8f9fa; }}
  .reg-ref {{ font-size: 6.5pt; background: #e8eaf6; padding: 1px 5px; border-radius: 3px; color: #283593; white-space: nowrap; }}
  .mermaid-container {{ background: #fafafa; border-radius: 6px; padding: 8px; margin-top: 4px; overflow-x: auto; }}
  .mermaid svg {{ max-width: 100%; height: auto; }}
  .dash-count {{ font-size: 9pt; color: #666; margin-bottom: 12px; }}
  @media (max-width: 600px) {{ .dash-grid {{ grid-template-columns: 1fr; }} }}
</style>
</head>
<body>
<div class="header">
  <h1>&#9670; Insurance Analytics Dashboards</h1>
  <p>ACORD Capability Model Reference &mdash; {len(DASHBOARDS)} dashboards, {sum(len(d['kpis']) for d in DASHBOARDS)} KPIs &bull; Solvency II / NAIC / IFRS 17 / APRA / GDPR</p>
</div>
<div class="filters">
  <input type="text" id="search" placeholder="Search dashboards by name, ACORD code, or KPI..." oninput="filterCards()">
  <select id="acordFilter" onchange="filterCards()">
    <option value="">All ACORD Domains</option>
    <option value="IN001-IN004">Product Lifecycle (IN001-004)</option>
    <option value="IN005-IN008">Distribution (IN005-008)</option>
    <option value="IN009-IN012">Underwriting (IN009-012)</option>
    <option value="IN013-IN015">Policy Admin (IN013-015)</option>
    <option value="IN016-IN019">Claims (IN016-019)</option>
    <option value="IN020-IN022">Reinsurance (IN020-022)</option>
    <option value="IN023-IN025">Actuarial (IN023-025)</option>
    <option value="IN031">Billing (IN031)</option>
    <option value="IN026-IN027">Customer (IN026-027)</option>
    <option value="IN028-IN030">Risk &amp; Compliance (IN028-030)</option>
    <option value="IN032">IFRS 17 (IN032)</option>
    <option value="IN029">Reg Reporting (IN029)</option>
    <option value="IN033">Data &amp; Analytics (IN033)</option>
    <option value="IN034">Info Security (IN034)</option>
    <option value="IN035">Enterprise (IN035)</option>
    <option value="IN036">IT &amp; Digital (IN036)</option>
  </select>
</div>
<p class="dash-count" id="dashCount">Showing {len(DASHBOARDS)} dashboards</p>
<div class="dash-grid" id="dashGrid">
{''.join(dash_cards)}
</div>
<script>
async function initMermaid() {{
    await mermaid.initialize({{startOnLoad:false, theme:'neutral', sequence:{{showSequenceNumbers:false, mirrorActors:true}}, securityLevel:'loose'}});
    var divs = document.querySelectorAll('div.mermaid');
    for (var i = 0; i < divs.length; i++) {{
        try {{
            var result = await mermaid.render('svg-' + i, divs[i].textContent);
            divs[i].innerHTML = result.svg;
        }} catch(e) {{
            divs[i].innerHTML = '<div style=\"color:red;padding:4px;font-size:8pt;\">Render error: ' + e.message.substring(0,100) + '</div>';
        }}
    }}
}}
initMermaid();

function filterCards() {{
    var q = document.getElementById('search').value.toLowerCase();
    var af = document.getElementById('acordFilter').value;
    var cards = document.querySelectorAll('.dash-card');
    var shown = 0;
    cards.forEach(function(c) {{
        var acords = c.getAttribute('data-acord') || '';
        var text = c.textContent.toLowerCase();
        var matchSearch = !q || text.indexOf(q) >= 0;
        var matchAcord = !af || acords.indexOf(af.replace('-',',')) >= 0 || acords.indexOf(af) >= 0;
        if (matchSearch && matchAcord) {{ c.style.display = ''; shown++; }}
        else {{ c.style.display = 'none'; }}
    }});
    document.getElementById('dashCount').textContent = 'Showing ' + shown + ' dashboards';
}}
</script>
</body>
</html>"""

    out = DASH_DIR / "insurance-dashboards.html"
    out.write_text(html, encoding="utf-8")
    print(f"HTML written: {out} ({len(html)} bytes)")
    return html


# ═══════════════════════════════════════════════════════════════
#  MARKDOWN GENERATOR
# ═══════════════════════════════════════════════════════════════

def esc_md(val):
    return str(val).replace("|", "\\|")

def gen_markdown():
    toc_lines = ["# Insurance Analytics Dashboards \u2014 ACORD Capability Reference\n"]
    toc_lines.append(f"> {len(DASHBOARDS)} master dashboards \u2022 {sum(len(d['kpis']) for d in DASHBOARDS)} KPIs \u2022 Solvency II / NAIC / IFRS 17 / APRA / GDPR / NIST\n")
    toc_lines.append("## Table of Contents\n")
    for d in DASHBOARDS:
        codes = ", ".join(d["acord_codes"])
        toc_lines.append(f"- [{d['id']:02d}. {d['title']}](#dashboard-{d['id']:02d}) \u2014 {codes}")
    toc_lines.append(f"- [ACORD Capability Cross-Reference](#acord-capability-cross-reference)")
    toc_lines.append("")

    sections = []
    for d in DASHBOARDS:
        lines = []
        lines.append(f"## Dashboard {d['id']:02d}: {d['title']}\n")
        codes_fmt = " \u2022 ".join(f"`{c}`" for c in d["acord_codes"])
        lines.append(f"**ACORD:** {codes_fmt}  ")
        lines.append(f"**Business Question:** {d['business_question']}  ")
        lines.append(f"**Owner:** {d['owner']}  \n")
        lines.append(f"{d['description']}\n")

        # KPI table
        lines.append("### KPIs\n")
        lines.append("| KPI | Formula / Source | Chart | Source System | Refresh | Reg Ref |")
        lines.append("|-----|-----------------|-------|--------------|---------|---------|")
        for k in d["kpis"]:
            lines.append(f"|{esc_md(k[0])}|{esc_md(k[1])}|{esc_md(k[2])}|{esc_md(k[3])}|{esc_md(k[4])}|{esc_md(k[5])}|")
        lines.append("")

        # Filters and drill-down
        lines.append("### Filters & Drill-Down\n")
        lines.append(f"**Filters:** {', '.join(d['filters'])}  ")
        lines.append(f"**Drill-Down Path:** `{d['drill_down']}`  \n")

        # Mermaid data-flow diagram
        lines.append("### Data Flow Diagram\n")
        lines.append("```mermaid")
        for m in d["mermaid"]:
            lines.append(m)
        lines.append("```\n")

        # Page break for PDF
        lines.append('<div style="page-break-before: always;"></div>\n')

        sections.append("\n".join(lines))

    # ACORD cross-reference table
    xref_lines = [
        "## ACORD Capability Cross-Reference\n",
        "| ACORD Code | Capability | Dashboard(s) |",
        "|------------|-----------|--------------|",
    ]
    acord_map = {
        "IN001": "Product Concept & Design", "IN002": "Rate & Form Filing", "IN003": "Product Launch", "IN004": "Product Performance Monitoring",
        "IN005": "Agency & Producer Onboarding", "IN006": "Commission Management", "IN007": "Producer Performance", "IN008": "Distribution Analytics",
        "IN009": "Risk Assessment & Scoring", "IN010": "Underwriting Decision", "IN011": "Quote Generation", "IN012": "Bind & Evidence",
        "IN013": "Policy Issuance", "IN014": "Mid-Term Adjustments", "IN015": "Renewal Processing",
        "IN016": "First Notice of Loss", "IN017": "Claims Investigation", "IN018": "Claims Adjudication", "IN019": "Payment & Settlement",
        "IN020": "Treaty Administration", "IN021": "Facultative Placement", "IN022": "Retrocession Management",
        "IN023": "Pricing Model Development", "IN024": "Rate Monitoring", "IN025": "Reserve Estimation",
        "IN031": "Billing & Collections",
        "IN026": "Customer Onboarding", "IN027": "Customer Relationship Management",
        "IN028": "Enterprise Risk Management", "IN029": "Regulatory Compliance", "IN030": "Capital Adequacy & ORSA",
        "IN032": "IFRS 17 Accounting",
        "IN033": "Data & Analytics",
        "IN034": "Information Security",
        "IN035": "Enterprise Services",
        "IN036": "IT & Digital Platforms",
    }
    for code, cap in sorted(acord_map.items()):
        linked = [f"#{d['id']:02d}" for d in DASHBOARDS if code in d["acord_codes"]]
        xref_lines.append(f"| `{code}` | {cap} | Dashboard {', '.join(linked) if linked else '\u2014'} |")

    md = "\n".join(toc_lines + sections + xref_lines)

    out = DASH_DIR / "insurance-dashboards.md"
    out.write_text(md, encoding="utf-8")
    print(f"Markdown written: {out} ({len(md)} bytes)")
    return md


# ═══════════════════════════════════════════════════════════════
#  MAIN
# ═══════════════════════════════════════════════════════════════

if __name__ == "__main__":
    print("=" * 60)
    print("  BUILDING ANALYTICS DASHBOARD CATALOGUE")
    print("=" * 60)
    print(f"\n  Dashboards: {len(DASHBOARDS)}")

    gen_html()
    gen_markdown()

    total_kpis = sum(len(d["kpis"]) for d in DASHBOARDS)
    total_mermaid = len([d for d in DASHBOARDS if d.get("mermaid")])

    print(f"\n  Summary:")
    print(f"    Dashboards:  {len(DASHBOARDS)}")
    print(f"    KPIs:        {total_kpis}")
    print(f"    Mermaid:     {total_mermaid}")
    print(f"\n  Written to: {DASH_DIR}")
