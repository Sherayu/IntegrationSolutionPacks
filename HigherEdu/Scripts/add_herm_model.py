"""Inject CAUDIT HERM Business Capability Model reference into README.md"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
README = ROOT / "README.md"

# HERM BRM v3.2 capability catalog
HERM_CAPABILITIES = [
    ("Learning & Teaching", "Curriculum Management","BC001","Design, develop, and maintain academic programs, courses, and curricula"),
    ("Learning & Teaching", "Curriculum Delivery","BC023","Deliver teaching and learning experiences across modalities"),
    ("Learning & Teaching", "Student Assessment","BC028","Assess, grade, and certify student learning outcomes"),
    ("Research & Innovation","Research Opportunities & Planning","BC065","Identify, evaluate, and plan research opportunities and strategy"),
    ("Research & Innovation","Research Funding","BC071","Secure, administer, and report on research funding and grants"),
    ("Research & Innovation","Research Activity","BC074","Conduct and manage research projects and investigations"),
    ("Research & Innovation","Research Dissemination","BC086","Publish, disseminate, and commercialise research outputs"),
    ("Research & Innovation","Research Management","BC093","Manage research portfolios, performance, and reporting"),
    ("Research & Innovation","Research Assurance","BC245","Ensure research integrity, ethics, and regulatory compliance"),
    ("Student Administration","Student Recruitment","BC008","Attract, engage, and recruit prospective students"),
    ("Student Administration","Student Admission","BC014","Process applications, make admission decisions, and manage offers"),
    ("Student Administration","Student Enrolment","BC019","Enrol, register, and orient students into programs"),
    ("Student Administration","Student Management","BC044","Maintain student records, progression, and academic history"),
    ("Student Administration","Student Support","BC052","Provide wellbeing, academic support, and student services"),
    ("Student Administration","Completion Management","BC032","Manage graduation, certification, and program completion"),
    ("Corporate Services","Financial Management","BC184","Manage budgeting, accounting, procurement, and financial control"),
    ("Corporate Services","Human Resource Management","BC171","Manage workforce planning, recruitment, payroll, and development"),
    ("Corporate Services","Legal Services","BC155","Provide legal counsel, contracts, and compliance advice"),
    ("Corporate Services","Governance Risk & Compliance","BC160","Oversee governance, risk management, audit, and regulatory compliance"),
    ("Corporate Services","Strategy Management","BC147","Develop institutional strategy, planning, and performance monitoring"),
    ("Corporate Services","Business Capability Management","BC206","Manage enterprise architecture and business capability evolution"),
    ("Engagement & Advancement","Marketing Management","BC107","Manage brand, communications, and market engagement"),
    ("Engagement & Advancement","Advancement Management","BC232","Manage alumni relations, fundraising, and donor stewardship"),
    ("Engagement & Advancement","Engagement & Relationship Management","BC238","Manage stakeholder engagement, partnerships, and community relations"),
    ("Infrastructure & Operations","Facilities & Estate Management","BC125","Manage campus, buildings, space, and physical infrastructure"),
    ("Infrastructure & Operations","Supporting Services","BC114","Provide ancillary services (catering, printing, transport, etc.)"),
    ("Information & Library","Library Administration","BC133","Manage library collections, access, and information services"),
    ("Information & Library","Information Management","BC135","Manage information assets, records, and data governance"),
    ("Information & Library","Publishing Management","BC250","Manage institutional publishing and university press operations"),
    ("Information & Library","Archive Management","BC255","Preserve and provide access to permanently valuable records"),
    ("Technology","ICT Management","BC201","Plan, deliver, and support information and communication technology services"),
]

SECTION_CAPABILITY_MAP = {
    "Student Administration":      ["BC008","BC014","BC019","BC044","BC052","BC032"],
    "Learning & Teaching":         ["BC001","BC023","BC028"],
    "HR & Faculty Management":     ["BC171"],
    "Finance & Resource Management":["BC184"],
    "Research Management":         ["BC065","BC071","BC074","BC086","BC093","BC245"],
    "Institutional Engagement":    ["BC107","BC232","BC238"],
    "Library & Learning Support":  ["BC133","BC135"],
    "Enterprise Data & Analytics": ["BC201","BC135"],
}

def build_herm_section():
    lines = []
    lines.append("## CAUDIT HERM Business Capability Model Reference")
    lines.append("")
    lines.append("The CAUDIT Higher Education Reference Model (HERM) **Business Reference Model v3.2** defines the standard business capabilities for higher education institutions. The table below lists all Level 2 capabilities grouped by Level 1 domain. Each process flow in this document is mapped to its relevant HERM capability codes.")
    lines.append("")

    groups = {}
    for l1, l2, code, desc in HERM_CAPABILITIES:
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

    # 1. Find insertion point
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

    # 2. Inject HERM section
    herm_text = build_herm_section()
    hern_lines = herm_text.split("\n")
    new_lines = lines[:meta_end_idx+1] + [""] + hern_lines + lines[meta_end_idx+1:toc_idx] + lines[toc_idx:]
    print(f"Inserted HERM section ({len(hern_lines)} lines) after metadata")

    # 3. Add capability codes to domain headings
    for i, line in enumerate(new_lines):
        stripped = line.strip()
        for section_name, codes in SECTION_CAPABILITY_MAP.items():
            if stripped.startswith("# ") and not stripped.startswith("##") and section_name in stripped:
                new_lines[i] = add_capability_to_heading(line, codes)
            elif stripped.startswith("## ") and not stripped.startswith("###") and section_name in stripped:
                if "BC" not in stripped:
                    new_lines[i] = add_capability_to_heading(line, codes)

    # 4. Update TOC entries
    toc_cap_map = {
        "Student Administration": "BC008, BC014, BC019, BC044, BC052, BC032",
        "Learning & Teaching": "BC001, BC023, BC028",
        "HR & Faculty Management": "BC171",
        "Finance & Resource Management": "BC184",
        "Research Management": "BC065, BC071, BC074, BC086, BC093, BC245",
        "Institutional Engagement": "BC107, BC232, BC238",
        "Library & Learning Support": "BC133, BC135",
        "Enterprise Data & Analytics": "BC201, BC135",
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

    # 5. Write back
    result = "\n".join(new_lines)
    README.write_text(result, encoding="utf-8")
    print(f"README.md written: {len(lines)} -> {len(new_lines)} lines")
    # Print summary
    toc_updates = sum(1 for l in new_lines if " - BC" in l and l.strip().startswith("- [") and not l.strip().startswith("  "))
    heading_updates = sum(1 for l in new_lines if "`BC" in l and (l.strip().startswith("# ") or l.strip().startswith("## ")))
    print(f"TOC entries updated: {toc_updates}")
    print(f"Headings updated: {heading_updates}")

if __name__ == "__main__":
    process_readme()
