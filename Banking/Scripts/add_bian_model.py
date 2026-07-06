from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
README = ROOT / "README.md"

BIAN_CAPABILITIES = [
    ("Channels", "Branch Services","BC001","Manage physical branch operations, teller services, and lobby management"),
    ("Channels", "Contact Center","BC002","Operate call center, IVR, and customer service desk"),
    ("Channels", "Digital Channels","BC003","Deliver internet banking, mobile banking, and digital self-service"),
    ("Channels", "Channel Management","BC004","Orchestrate omnichannel consistency, channel analytics, and channel optimization"),
    ("Finance & Risk Management","Financial Accounting","BC010","Manage general ledger, accounts payable/receivable, and financial close"),
    ("Finance & Risk Management","Management Accounting","BC011","Perform cost allocation, profitability analysis, and management reporting"),
    ("Finance & Risk Management","Risk Management","BC012","Identify, assess, monitor, and mitigate credit, market, operational, and liquidity risk"),
    ("Finance & Risk Management","Compliance","BC013","Ensure regulatory compliance, AML/CTF, sanctions screening, and conduct risk"),
    ("Finance & Risk Management","Treasury Management","BC014","Manage liquidity, funding, investments, and interest rate risk"),
    ("Customers","Customer Relationship Management","BC031","Manage customer interactions, campaigns, loyalty programs, and relationship lifecycle"),
    ("Customers","Customer Onboarding","BC032","Onboard new customers including identity verification, KYC, and account setup"),
    ("Customers","Customer Due Diligence","BC033","Perform KYC/CDD/EDD checks, risk rating, and ongoing monitoring"),
    ("Customers","Customer Servicing","BC034","Handle customer inquiries, service requests, complaints, and case management"),
    ("Operations","Payment Operations","BC060","Execute and manage domestic and cross-border payment instruments"),
    ("Operations","Settlement & Clearing","BC061","Clear and settle payments, securities, and financial transactions"),
    ("Operations","Reconciliation","BC062","Reconcile accounts, transactions, and nostro/vostro positions"),
    ("Operations","Trade Operations","BC063","Process trade finance, letters of credit, and document handling"),
    ("Products","Lending","BC070","Originate, service, and manage consumer and mortgage loans"),
    ("Products","Credit Cards","BC071","Issue, authorize, settle, and manage credit and debit card programs"),
    ("Products","Deposits","BC072","Manage current accounts, savings accounts, and demand deposits"),
    ("Products","Term Deposits & Savings","BC073","Manage term deposits, structured savings, and investment products"),
    ("Business Management","Strategy Management","BC080","Define corporate strategy, business planning, and performance management"),
    ("Business Management","Product Management","BC081","Design, develop, price, and manage banking products throughout lifecycle"),
    ("Business Management","Marketing Management","BC082","Plan and execute marketing campaigns, brand management, and market intelligence"),
    ("Resource Management","Human Resource Management","BC050","Manage workforce planning, recruitment, performance, and payroll"),
    ("Resource Management","Training & Development","BC051","Manage employee training, certifications, and competence development"),
]

SECTION_CAPABILITY_MAP = {
    "Customer Onboarding & Account Management": ["BC032","BC033","BC031"],
    "Payments & Transfers": ["BC060","BC061"],
    "Lending & Credit Management": ["BC070"],
    "Cards Management": ["BC071"],
    "Deposits & Savings Products": ["BC072","BC073"],
    "Risk & Compliance": ["BC012","BC013"],
    "Channels & Digital Banking": ["BC001","BC003","BC002"],
    "Finance, Treasury & Settlement": ["BC010","BC014","BC061","BC062"],
}

def build_bian_section():
    lines = []
    lines.append("## BIAN Capability Model Reference")
    lines.append("")
    lines.append("The BIAN (Banking Industry Architecture Network) Capability Model defines the standard business capabilities for banking institutions. The table below lists all relevant capabilities grouped by domain. Each process flow in this document is mapped to its relevant BIAN capability codes.")
    lines.append("")

    groups = {}
    for l1, l2, code, desc in BIAN_CAPABILITIES:
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

    bian_text = build_bian_section()
    bian_lines = bian_text.split("\n")
    new_lines = lines[:meta_end_idx+1] + [""] + bian_lines + lines[meta_end_idx+1:toc_idx] + lines[toc_idx:]
    print(f"Inserted BIAN section ({len(bian_lines)} lines) after metadata")

    for i, line in enumerate(new_lines):
        stripped = line.strip()
        for section_name, codes in SECTION_CAPABILITY_MAP.items():
            if stripped.startswith("# ") and not stripped.startswith("##") and section_name in stripped:
                new_lines[i] = add_capability_to_heading(line, codes)
            elif stripped.startswith("## ") and not stripped.startswith("###") and section_name in stripped:
                if "BC" not in stripped:
                    new_lines[i] = add_capability_to_heading(line, codes)

    toc_cap_map = {
        "Customer Onboarding & Account Management": "BC032, BC033, BC031",
        "Payments & Transfers": "BC060, BC061",
        "Lending & Credit Management": "BC070",
        "Cards Management": "BC071",
        "Deposits & Savings Products": "BC072, BC073",
        "Risk & Compliance": "BC012, BC013",
        "Channels & Digital Banking": "BC001, BC003, BC002",
        "Finance, Treasury & Settlement": "BC010, BC014, BC061, BC062",
    }
    for i, line in enumerate(new_lines):
        stripped = line.strip()
        for section_name, codes_str in toc_cap_map.items():
            if stripped.startswith("- [") and section_name in stripped and "]" in stripped:
                if stripped.startswith("  -") or stripped.startswith("\t-"):
                    continue
                new_line = line.rstrip().replace(
                    f"[{section_name}]",
                    f"[{section_name}  - {codes_str}]",
                )
                if new_line != line:
                    new_lines[i] = new_line

    result = "\n".join(new_lines)
    README.write_text(result, encoding="utf-8")
    print(f"README.md written: {len(lines)} -> {len(new_lines)} lines")

    toc_updates = sum(1 for l in new_lines if " - BC" in l and l.strip().startswith("- [") and not l.strip().startswith("  "))
    heading_updates = sum(1 for l in new_lines if "`BC" in l and (l.strip().startswith("# ") or l.strip().startswith("## ")))
    print(f"TOC entries updated: {toc_updates}")
    print(f"Headings updated: {heading_updates}")

if __name__ == "__main__":
    process_readme()
