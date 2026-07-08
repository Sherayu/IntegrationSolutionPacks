"""Inject HL7 FHIR / HIMSS Healthcare Capability Model reference into README.md"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
README = ROOT / "README.md"

# HIMSS Healthcare Capability Model v1.0 capability catalog
HC_CAPABILITIES = [
    ("Patient Administration", "Patient Registration & Demographics","HC001","Register, maintain, and manage patient demographic data and unique identifiers"),
    ("Patient Administration", "Patient Identity Management","HC002","Manage patient identity matching, MPI, and record linkage across systems"),
    ("Patient Administration", "Consent & Privacy Management","HC003","Manage patient consent directives, HIPAA authorizations, and privacy preferences"),
    ("Patient Administration", "Patient Portal & Self-Service","HC004","Provide patient access to health records, appointments, billing, and secure messaging"),
    ("Patient Administration", "Advance Directives & Goals of Care","HC005","Capture and manage advance directives, living wills, and goals of care documentation"),
    ("Clinical Documentation & EHR", "Clinical Note Management","HC010","Create, manage, and store clinical documentation including H&P, progress notes, and summaries"),
    ("Clinical Documentation & EHR", "Order Entry & Management (CPOE)","HC011","Computerized provider order entry for medications, labs, radiology, and procedures"),
    ("Clinical Documentation & EHR", "Problem List & Medical History","HC012","Maintain patient problem list, past medical history, allergies, and social determinants"),
    ("Laboratory & Diagnostics", "Lab Order & Specimen Management","HC020","Order laboratory tests, collect specimens, and track throughout the testing lifecycle"),
    ("Laboratory & Diagnostics", "Lab Results & Reporting","HC021","Receive, validate, and report laboratory results with critical value alerting"),
    ("Laboratory & Diagnostics", "Radiology & Imaging Management","HC022","Order imaging studies, schedule modalities, and distribute reports and images"),
    ("Pharmacy & Medication Management", "Medication Ordering & Reconciliation","HC030","Order medications, perform drug-drug interaction checks, and reconcile across transitions"),
    ("Pharmacy & Medication Management", "Pharmacy Dispensing & Verification","HC031","Dispense medications, perform verification checks, and manage formularies"),
    ("Pharmacy & Medication Management", "Medication Administration (MAR)","HC032","Document medication administration, barcode scanning, and dosage tracking"),
    ("Billing & Revenue Cycle", "Charge Capture & Coding","HC040","Capture charges, apply ICD-10/CPT/HCPCS coding, and validate claim readiness"),
    ("Billing & Revenue Cycle", "Claims Submission & Adjudication","HC041","Submit claims to payers, manage electronic clearinghouse exchanges, and track status"),
    ("Billing & Revenue Cycle", "Payment Posting & Denial Management","HC042","Post payments, manage denials, process appeals, and reconcile accounts"),
    ("Scheduling & Access", "Appointment Scheduling & Check-in","HC050","Schedule patient appointments, manage waitlists, and process check-in/check-out"),
    ("Scheduling & Access", "Referral Management & Authorizations","HC051","Manage referrals, obtain prior authorizations, and coordinate specialist access"),
    ("Care Coordination & Population Health", "Care Plan Development & Management","HC060","Develop, share, and track interdisciplinary care plans across the care continuum"),
    ("Care Coordination & Population Health", "Transition of Care & Discharge","HC061","Manage care transitions, discharge planning, and post-acute follow-up coordination"),
    ("Care Coordination & Population Health", "Population Health Risk Stratification","HC062","Stratify patient populations by risk, manage outreach, and track quality gaps"),
    ("Health Information Exchange", "HIE Document Sharing & Query","HC070","Query and share clinical documents across organizational boundaries via HIE"),
    ("Health Information Exchange", "Public Health Reporting & Immunization","HC071", "Report immunizations, communicable diseases, and vital records to public health agencies"),
    ("Supply Chain & Inventory", "Medical Supply Procurement","HC080","Manage procurement, vendor contracts, and purchase orders for medical supplies"),
    ("Supply Chain & Inventory", "Inventory & Asset Management","HC081","Track medical inventory levels, manage par levels, and locate medical equipment"),
    ("Regulatory Compliance & Quality", "Quality Measure Reporting (HEDIS/MIPS)","HC090","Calculate and report quality measures for HEDIS, MIPS, and value-based programs"),
    ("Regulatory Compliance & Quality", "Regulatory Audit & Compliance","HC091","Manage regulatory audits, accreditation surveys, and compliance documentation"),
    ("Regulatory Compliance & Quality", "Incident & Patient Safety Reporting","HC092","Report and track patient safety incidents, adverse events, and root cause analyses"),
]

SECTION_CAPABILITY_MAP = {
    "Patient Administration":              ["HC001","HC002","HC003","HC004","HC005"],
    "Clinical Documentation & EHR":        ["HC010","HC011","HC012"],
    "Laboratory & Diagnostics":            ["HC020","HC021","HC022"],
    "Pharmacy & Medication Management":    ["HC030","HC031","HC032"],
    "Billing & Revenue Cycle Management":  ["HC040","HC041","HC042"],
    "Appointment Scheduling & Access":     ["HC050","HC051"],
    "Care Coordination & Population Health":["HC060","HC061","HC062"],
    "Health Information Exchange":         ["HC070","HC071"],
    "Supply Chain & Inventory Management": ["HC080","HC081"],
    "Regulatory Compliance & Quality":     ["HC090","HC091","HC092"],
}

def build_hc_section():
    lines = []
    lines.append("## HIMSS Healthcare Capability Model Reference")
    lines.append("")
    lines.append("The HIMSS Healthcare Capability Model **v1.0** defines the standard business capabilities for healthcare delivery organizations. The table below lists all Level 2 capabilities grouped by Level 1 domain. Each process flow in this document is mapped to its relevant HIMSS capability codes.")
    lines.append("")

    groups = {}
    for l1, l2, code, desc in HC_CAPABILITIES:
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

    # 2. Inject HC section
    hc_text = build_hc_section()
    hc_lines = hc_text.split("\n")
    new_lines = lines[:meta_end_idx+1] + [""] + hc_lines + lines[meta_end_idx+1:toc_idx] + lines[toc_idx:]
    print(f"Inserted HC section ({len(hc_lines)} lines) after metadata")

    # 3. Add capability codes to domain headings
    for i, line in enumerate(new_lines):
        stripped = line.strip()
        for section_name, codes in SECTION_CAPABILITY_MAP.items():
            if stripped.startswith("# ") and not stripped.startswith("##") and section_name in stripped:
                new_lines[i] = add_capability_to_heading(line, codes)
            elif stripped.startswith("## ") and not stripped.startswith("###") and section_name in stripped:
                if "HC" not in stripped:
                    new_lines[i] = add_capability_to_heading(line, codes)

    # 4. Update TOC entries
    toc_cap_map = {
        "Patient Administration": "HC001, HC002, HC003, HC004, HC005",
        "Clinical Documentation & EHR": "HC010, HC011, HC012",
        "Laboratory & Diagnostics": "HC020, HC021, HC022",
        "Pharmacy & Medication Management": "HC030, HC031, HC032",
        "Billing & Revenue Cycle Management": "HC040, HC041, HC042",
        "Appointment Scheduling & Access": "HC050, HC051",
        "Care Coordination & Population Health": "HC060, HC061, HC062",
        "Health Information Exchange": "HC070, HC071",
        "Supply Chain & Inventory Management": "HC080, HC081",
        "Regulatory Compliance & Quality": "HC090, HC091, HC092",
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
    toc_updates = sum(1 for l in new_lines if " - HC" in l and l.strip().startswith("- [") and not l.strip().startswith("  "))
    heading_updates = sum(1 for l in new_lines if "`HC" in l and (l.strip().startswith("# ") or l.strip().startswith("## ")))
    print(f"TOC entries updated: {toc_updates}")
    print(f"Headings updated: {heading_updates}")

if __name__ == "__main__":
    process_readme()
