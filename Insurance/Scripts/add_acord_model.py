"""Inject ACORD Business Capability Model reference into Insurance README.md"""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
README = ROOT / "README.md"

# ACORD Framework capability catalog (10 Level-1 domains, 36 Level-2 capabilities)
ACORD_CAPABILITIES = [
    # Product
    ("Product", "Product Lifecycle Management", "IN001", "Design, develop, and manage insurance products across lifecycle from concept to retirement"),
    ("Product", "Product Configuration & Rating", "IN002", "Configure product rules, rating algorithms, and coverage options"),
    ("Product", "Product Filing & Compliance", "IN003", "Manage regulatory product filings, approvals, and compliance across jurisdictions"),
    ("Product", "Product Performance Analytics", "IN004", "Monitor product profitability, loss ratios, and distribution performance"),
    # Distribution
    ("Distribution", "Channel Management", "IN005", "Manage distribution channels including agents, brokers, bancassurance, and direct"),
    ("Distribution", "Producer/Agent Lifecycle Management", "IN006", "Onboard, license, appoint, and manage producers and agents"),
    ("Distribution", "Commission Management", "IN007", "Calculate, process, and disburse commissions across compensation structures"),
    ("Distribution", "Lead & Campaign Management", "IN008", "Manage marketing campaigns, lead generation, and distribution analytics"),
    # Underwriting
    ("Underwriting", "New Business Submission", "IN009", "Receive, validate, and triage new business submissions from producers"),
    ("Underwriting", "Risk Assessment & Scoring", "IN010", "Assess risk using rules, models, and third-party data sources"),
    ("Underwriting", "Underwriting Decision", "IN011", "Make underwriting decisions with authority-based approval and referral workflows"),
    ("Underwriting", "Quote Generation & Bind", "IN012", "Generate quotes, bind coverage, and issue evidence of insurance"),
    # Policy
    ("Policy", "Policy Issuance & Administration", "IN013", "Issue policies, manage policy documents, and maintain in-force records"),
    ("Policy", "Policy Servicing & Adjustments", "IN014", "Process mid-term adjustments, endorsements, and policy changes"),
    ("Policy", "Renewal & Termination", "IN015", "Manage renewal lifecycle, non-renewal notices, cancellations, and reinstatements"),
    # Claims
    ("Claims", "First Notice of Loss", "IN016", "Capture claim notifications through multi-channel intake and triage"),
    ("Claims", "Claims Investigation & Evaluation", "IN017", "Investigate claims, gather evidence, assess liability, and estimate reserves"),
    ("Claims", "Claims Adjudication & Payment", "IN018", "Adjudicate claims, approve payments, and manage benefit disbursement"),
    ("Claims", "Subrogation & Recovery", "IN019", "Pursue subrogation, salvage, and third-party recoveries"),
    # Reinsurance
    ("Reinsurance", "Treaty Management", "IN020", "Manage proportional and non-proportional treaty agreements and session schedules"),
    ("Reinsurance", "Facultative Placement", "IN021", "Place facultative reinsurance for individual large or complex risks"),
    ("Reinsurance", "Reinsurance Accounting & Bordereaux", "IN022", "Prepare premium and loss bordereaux, manage cessions, and reconcile recoveries"),
    # Financial & Actuarial
    ("Financial & Actuarial", "Actuarial Modeling & Pricing", "IN023", "Develop pricing models, rate indications, and actuarial assumptions"),
    ("Financial & Actuarial", "Reserve Estimation & Management", "IN024", "Estimate loss reserves, IBNR, and actuarial liabilities"),
    ("Financial & Actuarial", "Catastrophe Modeling", "IN025", "Model natural and man-made catastrophe exposure and accumulation risk"),
    # Customer
    ("Customer", "Customer Onboarding & KYC", "IN026", "Onboard customers with identity verification, AML screening, and due diligence"),
    ("Customer", "Customer Relationship Management", "IN027", "Manage customer interactions, loyalty programs, and cross-sell opportunities"),
    # Risk & Compliance
    ("Risk & Compliance", "Enterprise Risk Management", "IN028", "Manage ERM framework, risk appetite, capital adequacy, and ORSA processes"),
    ("Risk & Compliance", "Regulatory Compliance", "IN029", "Ensure compliance with Solvency II, NAIC, APRA, and other regulatory regimes"),
    ("Risk & Compliance", "Internal Audit & Assurance", "IN030", "Conduct internal audits, control testing, and assurance activities"),
    # Enterprise & IT
    ("Enterprise & IT", "Billing & Collections", "IN031", "Manage premium billing, payment processing, collections, and dispute resolution"),
    ("Enterprise & IT", "IFRS 17 & Financial Accounting", "IN032", "Apply IFRS 17 accounting including CSM, PAA, GMM, VFA calculations"),
    ("Enterprise & IT", "Data Governance & MDM", "IN033", "Govern data assets, manage master data, and ensure data quality"),
    ("Enterprise & IT", "Information Security & Cybersecurity", "IN034", "Protect information assets, manage cyber risk, and ensure business continuity"),
    ("Enterprise & IT", "Enterprise Services Management", "IN035", "Manage HR, finance, procurement, legal, and facilities operations"),
    ("Enterprise & IT", "IT Operations & Digital Platforms", "IN036", "Operate IT infrastructure, cloud platforms, API management, and DevOps"),
]

SECTION_CAPABILITY_MAP = {
    "Product Lifecycle Management":          ["IN001", "IN002", "IN003", "IN004"],
    "Distribution & Channel Management":     ["IN005", "IN006", "IN007", "IN008"],
    "Underwriting":                          ["IN009", "IN010", "IN011", "IN012"],
    "Policy Administration":                 ["IN013", "IN014", "IN015"],
    "Claims Management":                     ["IN016", "IN017", "IN018", "IN019"],
    "Reinsurance":                           ["IN020", "IN021", "IN022"],
    "Actuarial & Pricing":                   ["IN023", "IN024", "IN025"],
    "Billing & Collections":                 ["IN031"],
    "Customer Management":                   ["IN026", "IN027"],
    "Risk Management & Compliance":          ["IN028", "IN029", "IN030"],
    "IFRS 17 Accounting & Finance":          ["IN032"],
    "Regulatory Reporting":                  ["IN029"],
    "Data & Analytics":                      ["IN033"],
    "Information Security & Cybersecurity":  ["IN034"],
    "Enterprise Services":                   ["IN035"],
    "IT & Digital Platforms":                ["IN036"],
}

def build_acord_section():
    lines = []
    lines.append("## ACORD Business Capability Model Reference")
    lines.append("")
    lines.append("The ACORD (Association for Cooperative Operations Research and Development) Capability Model defines the standard business capabilities for insurance institutions. The table below lists all relevant capabilities across 10 Level-1 domains. Each process flow in this document is mapped to its relevant ACORD capability codes.")
    lines.append("")

    groups = {}
    for l1, l2, code, desc in ACORD_CAPABILITIES:
        groups.setdefault(l1, []).append((l2, code, desc))

    for domain, caps in groups.items():
        lines.append(f"### {domain}")
        lines.append("")
        lines.append("| Capability | Code | Description |")
        lines.append("|-----------|------|-------------|")
        for l2_name, code, desc in caps:
            lines.append(f"| **{l2_name}** | `{code}` | {desc} |")
        lines.append("")

    lines.append("---")
    lines.append("")
    return "\n".join(lines)

def add_capability_to_heading(line, codes):
    badges = " ".join(f"`{c}`" for c in codes)
    return f"{line.rstrip()}  - {badges}"

def process_readme():
    text = README.read_text(encoding="utf-8")
    lines = text.split("\n")

    toc_idx = None
    meta_end_idx = None
    for i, line in enumerate(lines):
        if line.strip().startswith("> Generated"):
            meta_end_idx = i
        if line.strip() == "## Table of Contents":
            toc_idx = i
            break

    if meta_end_idx is None or toc_idx is None:
        print("ERROR: Could not find insertion points")
        return

    acord_text = build_acord_section()
    acord_lines = acord_text.split("\n")
    new_lines = lines[:meta_end_idx+1] + [""] + acord_lines + lines[meta_end_idx+1:toc_idx] + lines[toc_idx:]
    print(f"Inserted ACORD section ({len(acord_lines)} lines) after metadata")

    for i, line in enumerate(new_lines):
        stripped = line.strip()
        for section_name, codes in SECTION_CAPABILITY_MAP.items():
            if stripped.startswith("# ") and not stripped.startswith("##") and section_name in stripped:
                new_lines[i] = add_capability_to_heading(line, codes)

    README.write_text("\n".join(new_lines), encoding="utf-8")
    print(f"Updated: {README}")
    print(f"Total lines: {len(new_lines)}")

if __name__ == "__main__":
    process_readme()
