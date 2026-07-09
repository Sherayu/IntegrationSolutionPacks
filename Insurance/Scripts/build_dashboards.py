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

# ═══════════════════════════════════════════════════════════════
#  BUSINESS CAPABILITY MODEL GENERATOR
# ═══════════════════════════════════════════════════════════════

BCM_DOMAINS = [
    # (Domain, L1 Acronym, ACORD Range, Standards, Description)
    ("Product Lifecycle Management", "PLM", "IN001\u2013IN004", "NAIC SERFF, NAIC SSAP 53/61, IFRS 17.55", "End-to-end product ideation, design, rate filing, launch, and performance monitoring."),
    ("Distribution & Channel Management", "DCM", "IN005\u2013IN008", "NAIC Producer Licensing, NAIC SSAP 54", "Agency onboarding, commission management, producer performance, and channel analytics."),
    ("Underwriting", "UW", "IN009\u2013IN012", "Solvency II UW Risk 1.2, Solvency II Risk Concentration, NAIC IRIS 7", "Risk assessment, scoring, underwriting decision, quote generation, and bind."),
    ("Policy Administration", "PA", "IN013\u2013IN015", "\u2014", "Policy issuance, mid-term adjustments, endorsements, renewals, cancellations."),
    ("Claims Management", "CM", "IN016\u2013IN019", "Solvency II Premium Risk, Solvency II TP 2.2, NAIC SSAP 55, NAIC Claims Handling", "FNOL, investigation, adjudication, payment, subrogation, litigation management."),
    ("Reinsurance", "RI", "IN020\u2013IN022", "Solvency II RI Risk 2.1/2.3, Solvency II Counterparty 3.1, Solvency II Cat Risk, IFRS 17.62", "Treaty admin, facultative placement, bordereaux, retrocession management."),
    ("Actuarial & Pricing", "ACT", "IN023\u2013IN025", "Solvency II Pricing, Solvency II TP 2.2/2.3/2.5, Solvency II Cat Risk 4.1, IFRS 17.37, NAIC SSAP 55", "Pricing models, rate monitoring, reserve estimation, catastrophe modelling."),
    ("Billing & Collections", "BIL", "IN031", "\u2014", "Premium billing, payment processing, arrears management, refunds, commission disbursement."),
    ("Customer Management", "CUS", "IN026\u2013IN027", "NAIC Fair Treatment, NAIC Consumer Complaints", "Onboarding, CRM, loyalty, self-service portal, complaints management."),
    ("Risk Management & Compliance", "RMC", "IN028\u2013IN030", "Solvency II SCR 3.1, Solvency II MCR 4.1, Solvency II ORSA 5.1\u20135.3, Solvency II OpRisk 6.1, IAIS ICPs, NAIC Market Conduct", "ERM framework, capital adequacy/ORSA, compliance monitoring, internal audit, conduct risk."),
    ("IFRS 17 Accounting", "IFR", "IN032", "IFRS 17.16\u201324, 17.37, 17.43\u201346, 17.53\u201358, 17.62\u201365, 17.80\u201388, 17.C1\u2013C8", "CSM calculation, PAA/GMM/VFA aggregation, revenue recognition, disclosures."),
    ("Regulatory Reporting", "RRE", "IN029", "Solvency II QRT, NAIC SSAP, APRA GPS 001, APRA LRS 750.0", "Solvency II QRT, NAIC statutory, APRA GPS/LRS filings, tax reporting."),
    ("Data & Analytics", "DAN", "IN033", "BCBS 239, Solvency II Data Quality", "Data governance, MDM, BI dashboards, predictive analytics, data quality management."),
    ("Information Security & Cybersecurity", "ISC", "IN034", "GDPR Art 33\u201334, NIST 800\u201353/800\u201361, CIS Controls, DORA, SOX", "IAM, SOC/SIEM, vulnerability management, BCM/DR, third-party risk."),
    ("Enterprise Services", "ENT", "IN035", "\u2014", "HR, payroll, finance GL, procurement, vendor management, legal, facilities."),
    ("IT & Digital Platforms", "ITD", "IN036", "\u2014", "API management, cloud infra, DevOps, testing, service desk, cloud cost management."),
]

def gen_bcm():
    lines = []

    # ── Introduction ────────────────────────────────────────────
    lines.append('<div style="page-break-before: avoid;"></div>\n')
    lines.append("## Business Capability Model\n")
    lines.append(
        "The Insurance Business Capability Model defines **16 Level-1 (L1) domains** "
        "and **36 Level-2 (L2) capabilities** aligned to the "
        "[ACORD Capability Model](https://www.acord.org/standards-architecture/capability-model) "
        "(codes IN001\u2013IN036). Each capability maps to one or more regulatory standards: "
        "Solvency II (SCR, MCR, ORSA, TP), NAIC (SSAP, IRIS, SERFF), "
        "IFRS 17 (paragraphs 16\u2013C8), APRA (GPS 001, LRS 750.0), "
        "BCBS 239, GDPR, NIST 800-53, and DORA.\n"
    )
    lines.append(
        "The model serves as the organising framework for the 16 analytics dashboards "
        "defined in this catalogue. Each dashboard monitors KPIs that directly assess the "
        "health, efficiency, and regulatory compliance of its corresponding capabilities.\n"
    )

    # ── L1 Domain Decomposition Table ──────────────────────────
    lines.append("### L1 Domain Decomposition\n")
    lines.append("| # | L1 Domain | Acronym | ACORD Codes | Regulatory Standards |")
    lines.append("|---|-----------|---------|-------------|---------------------|")
    for i, (domain, acr, arange, stds, _) in enumerate(BCM_DOMAINS, 1):
        lines.append(f"|{i}|{domain}|{acr}|`{arange}`|{stds}|")
    lines.append("")

    # ── ACORD L2 Capability Detail ─────────────────────────────
    lines.append("### ACORD L2 Capability Detail (IN001\u2013IN036)\n")
    lines.append("| ACORD | L2 Capability | L1 Domain | Description |")
    lines.append("|-------|---------------|-----------|-------------|")

    acord_detail = [
        ("IN001", "Product Concept & Design", "Product Lifecycle Management", "Ideation, market research, feasibility assessment, coverage design."),
        ("IN002", "Rate & Form Filing", "Product Lifecycle Management", "Actuarial rate development, regulatory filing, approval tracking."),
        ("IN003", "Product Launch", "Product Lifecycle Management", "Market launch, distribution activation, training, documentation."),
        ("IN004", "Product Performance Monitoring", "Product Lifecycle Management", "In-force tracking, LR/ER/combined ratio, profitability analysis."),
        ("IN005", "Agency & Producer Onboarding", "Distribution & Channel Management", "Producer contracting, licensing verification, appointment, training."),
        ("IN006", "Commission Management", "Distribution & Channel Management", "Commission schedule setup, calculation, disbursement, reconciliation."),
        ("IN007", "Producer Performance", "Distribution & Channel Management", "Scorecards, premium tracking, loss ratio monitoring, tier management."),
        ("IN008", "Distribution Analytics", "Distribution & Channel Management", "Channel mix, CAC, conversion funnel, cost-to-serve, optimisation."),
        ("IN009", "Risk Assessment & Scoring", "Underwriting", "Submission intake, data enrichment, risk scoring, predictive models."),
        ("IN010", "Underwriting Decision", "Underwriting", "Referral workflow, authority limits, declination, counter-offer."),
        ("IN011", "Quote Generation", "Underwriting", "Rating engine execution, premium calculation, discount application."),
        ("IN012", "Bind & Evidence", "Underwriting", "Policy binding, evidence of insurance issuance, downstream notification."),
        ("IN013", "Policy Issuance", "Policy Administration", "Policy schedule creation, document generation, welcome pack."),
        ("IN014", "Mid-Term Adjustments", "Policy Administration", "Endorsements, cancellations, reinstatements, coverage changes."),
        ("IN015", "Renewal Processing", "Policy Administration", "Renewal offer generation, premium adjustment, retention tracking."),
        ("IN016", "First Notice of Loss", "Claims Management", "FNOL intake, triage, coverage verification, claim file creation."),
        ("IN017", "Claims Investigation", "Claims Management", "Evidence gathering, statement collection, expert engagement."),
        ("IN018", "Claims Adjudication", "Claims Management", "Liability assessment, coverage determination, settlement authority."),
        ("IN019", "Payment & Settlement", "Claims Management", "Payment execution, reserve adjustment, closure, recovery referral."),
        ("IN020", "Treaty Administration", "Reinsurance", "Treaty setup, contract management, limits, retention scheduling."),
        ("IN021", "Facultative Placement", "Reinsurance", "Risk-by-risk cession, quote, placement, documentation."),
        ("IN022", "Retrocession Management", "Reinsurance", "Retrocession structure, placement, monitoring, recoveries."),
        ("IN023", "Pricing Model Development", "Actuarial & Pricing", "Model design, calibration, validation, regulatory approval."),
        ("IN024", "Rate Monitoring", "Actuarial & Pricing", "Rate adequacy tracking, competitor analysis, experience monitoring."),
        ("IN025", "Reserve Estimation", "Actuarial & Pricing", "Chain-ladder, BF, IBNR estimation, reserve adequacy testing."),
        ("IN026", "Customer Onboarding & KYC", "Customer Management", "Identity verification, AML screening, policy setup, welcome."),
        ("IN027", "Customer Relationship Management", "Customer Management", "Interaction history, 360 view, cross-sell, retention, complaints."),
        ("IN028", "Enterprise Risk Management", "Risk Management & Compliance", "Risk framework, risk appetite, KRI monitoring, ORSA."),
        ("IN029", "Regulatory Compliance", "Risk Management & Compliance", "Compliance monitoring, regulatory change, conduct risk."),
        ("IN030", "Capital Adequacy & ORSA", "Risk Management & Compliance", "SCR/MCR calculation, capital planning, stress testing."),
        ("IN031", "Billing & Collections", "Billing & Collections", "Invoice generation, payment processing, arrears, refunds."),
        ("IN032", "IFRS 17 Accounting", "IFRS 17 Accounting", "CSM, RA, PAA/GMM/VFA, revenue recognition, disclosure."),
        ("IN033", "Data & Analytics", "Data & Analytics", "Data governance, MDM, BI dashboards, ML models, DQ management."),
        ("IN034", "Information Security", "Information Security & Cybersecurity", "IAM, SOC, vulnerability, BCM, third-party risk."),
        ("IN035", "Enterprise Services", "Enterprise Services", "HR, procurement, finance, legal, facilities management."),
        ("IN036", "IT & Digital Platforms", "IT & Digital Platforms", "API platform, cloud infra, DevOps, ITSM, cost management."),
    ]
    for code, cap, domain, desc in acord_detail:
        lines.append(f"|`{code}`|{cap}|{domain}|{desc}|")
    lines.append("")

    # ── Capability Model Diagram ────────────────────────────────
    lines.append("### Capability Model Diagram\n")
    lines.append("```mermaid")
    lines.append("graph TD")
    lines.append("    INS[Insurance Enterprise]")
    lines.append("")
    for i, (domain, acr, _, _, _) in enumerate(BCM_DOMAINS, 1):
        safe_dom = domain.replace(" & ", " &<br/>").replace(" &amp; ", " &<br/>")
        lines.append(f"    L1_{i}[\"{safe_dom}\"]")
        lines.append(f"    INS-->L1_{i}")
    lines.append("")
    # L1 to L2 connections
    l2_idx = 1
    for i, (domain, acr, arange, _, _) in enumerate(BCM_DOMAINS, 1):
        codes = acord_detail_for_domain(domain)
        for code, cap, _, _ in codes:
            safe_cap = cap.replace(" & ", " &<br/>").replace(" &amp; ", " &<br/>")
            lines.append(f"    L2_{l2_idx}[\"({code})<br/>{safe_cap}\"]")
            lines.append(f"    L1_{i}-->L2_{l2_idx}")
            l2_idx += 1
    lines.append("```\n")

    # ── Standards Mapping ───────────────────────────────────────
    lines.append("### Regulatory Standards Mapping\n")
    lines.append("| Standard | Scope | Applicable L1 Domains |")
    lines.append("|----------|-------|----------------------|")

    std_mapping = [
        ("Solvency II \u2013 SCR (Art. 100\u2013127)", "Capital adequacy, risk quantification", "Risk Management & Compliance, Actuarial & Pricing"),
        ("Solvency II \u2013 MCR (Art. 128\u2013131)", "Minimum capital floor", "Risk Management & Compliance"),
        ("Solvency II \u2013 ORSA (Art. 45)", "Own risk and solvency assessment", "Risk Management & Compliance"),
        ("Solvency II \u2013 Technical Provisions (Art. 76\u201386)", "Best estimate, risk margin, TP adequacy", "Actuarial & Pricing, Claims Management"),
        ("Solvency II \u2013 UW Risk (1.2)", "Premium and reserve risk", "Underwriting, Actuarial & Pricing"),
        ("Solvency II \u2013 Cat Risk (4.1)", "Natural and man-made catastrophe risk", "Actuarial & Pricing, Reinsurance"),
        ("Solvency II \u2013 RI Risk (2.1/2.3)", "Reinsurance counterparty and coverage risk", "Reinsurance"),
        ("Solvency II \u2013 OpRisk (6.1)", "Operational loss events", "Risk Management & Compliance"),
        ("NAIC SSAP 53", "Property and casualty loss reserves", "Claims Management, Actuarial & Pricing"),
        ("NAIC SSAP 54/61", "Reinsurance, expense accounting", "Reinsurance, Product Lifecycle"),
        ("NAIC SSAP 55", "Loss reserve discounting", "Claims Management, Actuarial & Pricing"),
        ("NAIC IRIS Ratios", "Insurance regulatory information system", "Product Lifecycle, Underwriting"),
        ("NAIC SERFF", "Rate and form filing system", "Product Lifecycle"),
        ("NAIC Producer Licensing", "Agent and broker licensing", "Distribution & Channel Management"),
        ("NAIC Market Conduct", "Fair treatment of policyholders", "Risk Management & Compliance, Customer Management"),
        ("IFRS 17 (Full standard)", "Insurance contracts accounting", "IFRS 17 Accounting, Product Lifecycle"),
        ("APRA GPS 001", "Prudential framework for insurers", "Regulatory Reporting, Risk Management"),
        ("APRA LRS 750.0", "Life insurance reporting standards", "Regulatory Reporting"),
        ("BCBS 239", "Risk data aggregation and reporting", "Data & Analytics, Risk Management"),
        ("GDPR Art. 33\u201334", "Personal data breach notification", "Information Security & Cybersecurity"),
        ("NIST SP 800-53", "Security and privacy controls", "Information Security & Cybersecurity"),
        ("DORA (EU 2022/2554)", "Digital operational resilience", "Information Security & Cybersecurity, IT & Digital Platforms"),
        ("IAIS ICPs", "Insurance core principles", "Risk Management & Compliance"),
    ]
    for std, scope, domains in std_mapping:
        lines.append(f"|{std}|{scope}|{domains}|")
    lines.append("")

    return lines


def acord_detail_for_domain(domain):
    """Return ACORD capabilities for a given L1 domain."""
    mapping = {
        "Product Lifecycle Management": [
            ("IN001", "Product Concept & Design", "Product Lifecycle Management", ""),
            ("IN002", "Rate & Form Filing", "Product Lifecycle Management", ""),
            ("IN003", "Product Launch", "Product Lifecycle Management", ""),
            ("IN004", "Product Performance Monitoring", "Product Lifecycle Management", ""),
        ],
        "Distribution & Channel Management": [
            ("IN005", "Agency & Producer Onboarding", "Distribution & Channel Management", ""),
            ("IN006", "Commission Management", "Distribution & Channel Management", ""),
            ("IN007", "Producer Performance", "Distribution & Channel Management", ""),
            ("IN008", "Distribution Analytics", "Distribution & Channel Management", ""),
        ],
        "Underwriting": [
            ("IN009", "Risk Assessment & Scoring", "Underwriting", ""),
            ("IN010", "Underwriting Decision", "Underwriting", ""),
            ("IN011", "Quote Generation", "Underwriting", ""),
            ("IN012", "Bind & Evidence", "Underwriting", ""),
        ],
        "Policy Administration": [
            ("IN013", "Policy Issuance", "Policy Administration", ""),
            ("IN014", "Mid-Term Adjustments", "Policy Administration", ""),
            ("IN015", "Renewal Processing", "Policy Administration", ""),
        ],
        "Claims Management": [
            ("IN016", "First Notice of Loss", "Claims Management", ""),
            ("IN017", "Claims Investigation", "Claims Management", ""),
            ("IN018", "Claims Adjudication", "Claims Management", ""),
            ("IN019", "Payment & Settlement", "Claims Management", ""),
        ],
        "Reinsurance": [
            ("IN020", "Treaty Administration", "Reinsurance", ""),
            ("IN021", "Facultative Placement", "Reinsurance", ""),
            ("IN022", "Retrocession Management", "Reinsurance", ""),
        ],
        "Actuarial & Pricing": [
            ("IN023", "Pricing Model Development", "Actuarial & Pricing", ""),
            ("IN024", "Rate Monitoring", "Actuarial & Pricing", ""),
            ("IN025", "Reserve Estimation", "Actuarial & Pricing", ""),
        ],
        "Billing & Collections": [
            ("IN031", "Billing & Collections", "Billing & Collections", ""),
        ],
        "Customer Management": [
            ("IN026", "Customer Onboarding & KYC", "Customer Management", ""),
            ("IN027", "Customer Relationship Management", "Customer Management", ""),
        ],
        "Risk Management & Compliance": [
            ("IN028", "Enterprise Risk Management", "Risk Management & Compliance", ""),
            ("IN029", "Regulatory Compliance", "Risk Management & Compliance", ""),
            ("IN030", "Capital Adequacy & ORSA", "Risk Management & Compliance", ""),
        ],
        "IFRS 17 Accounting": [
            ("IN032", "IFRS 17 Accounting", "IFRS 17 Accounting", ""),
        ],
        "Regulatory Reporting": [
            ("IN029", "Regulatory Compliance", "Regulatory Reporting", ""),
        ],
        "Data & Analytics": [
            ("IN033", "Data & Analytics", "Data & Analytics", ""),
        ],
        "Information Security & Cybersecurity": [
            ("IN034", "Information Security", "Information Security & Cybersecurity", ""),
        ],
        "Enterprise Services": [
            ("IN035", "Enterprise Services", "Enterprise Services", ""),
        ],
        "IT & Digital Platforms": [
            ("IN036", "IT & Digital Platforms", "IT & Digital Platforms", ""),
        ],
    }
    return mapping.get(domain, [])


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

    # Business Capability Model (prepended before dashboard sections)
    bcm_lines = gen_bcm()
    md = "\n".join(toc_lines + bcm_lines + sections + xref_lines)

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
