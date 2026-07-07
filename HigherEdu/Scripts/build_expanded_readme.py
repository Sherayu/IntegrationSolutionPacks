"""Build expanded Higher Education README by combining existing content with new data."""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "Scripts"))
import expand_readme as ED

README = ROOT / "README.md"
BAK = ROOT / "README.md.bak"

INT_HEADER = "| Flow | Entity | Info Flow | Source | Target | Source Conn | Target Conn | Pattern | Complexity |"
INT_SEP    = "|------|--------|-----------|--------|--------|-------------|-------------|---------|------------|"

AC_HEADER  = "| AC ID | Description | Related Info Flow | Expected Outcome | Priority |"
AC_SEP     = "|-------|------------|-------------------|------------------|----------|"


def read_current():
    src = BAK if BAK.exists() else README
    return src.read_text(encoding="utf-8")


def write_readme(text):
    README.write_text(text, encoding="utf-8")
    lines = text.split("\n")
    print(f"  Written: {README} ({len(lines)} lines)")


def format_row(items):
    escaped = [str(c).replace("|", "\\|") for c in items]
    return "| " + " | ".join(escaped) + " |"


def extract_subflow_text(full_text, sf_name):
    """Extract complete sub-flow text from ### to next ### or H1."""
    lines = full_text.split("\n")
    result = []
    in_sf = False
    # Normalize for matching: remove arrows, non-ASCII
    def norm(t):
        return t.lower().replace(" ", "").replace("\u2192", "").encode("ascii", "ignore").decode()
    target = norm(sf_name)
    for line in lines:
        s = line.strip()
        if s.startswith("### ") and not s.startswith("####"):
            heading = s.lstrip("### ").strip()
            if target in norm(heading) or norm(heading) in target:
                in_sf = True
                result.append(line)
            elif in_sf:
                break
            continue
        if in_sf:
            if s.startswith("# ") and not s.startswith("## "):
                break
            result.append(line)
    return "\n".join(result)


def process_subflow_text(sf_name, sf_text):
    """Process sub-flow text: add extra integration rows after existing table."""
    lines = sf_text.split("\n")
    result = []
    i = 0
    in_int = False

    while i < len(lines):
        line = lines[i]
        s = line.strip()

        if s == "#### Integration Details":
            in_int = True
            result.append(line)
            i += 1
            # Copy blank lines
            while i < len(lines) and lines[i].strip() == "":
                result.append(lines[i])
                i += 1
            # Copy table header and separator
            while i < len(lines) and lines[i].strip().startswith("|"):
                result.append(lines[i])
                i += 1
                if lines[i-1].strip() == INT_SEP:
                    break
            # Copy existing data rows
            while i < len(lines):
                si = lines[i].strip()
                if si.startswith("|"):
                    result.append(lines[i])
                    i += 1
                elif si == "":
                    break
                else:
                    break
            # Insert extra rows
            extra = ED.EXTRA_INTEGRATIONS.get(sf_name, [])
            if extra:
                for row in extra:
                    result.append(format_row(row))
            # Add Acceptance Criteria table
            ac_rows = ED.ACCEPTANCE_CRITERIA.get(sf_name, [])
            if ac_rows:
                result.append("")
                result.append("#### Acceptance Criteria")
                result.append("")
                result.append(AC_HEADER)
                result.append(AC_SEP)
                for ac in ac_rows:
                    result.append(format_row(ac))
            # Ensure blank line after table
            if result and result[-1].strip().startswith("|"):
                result.append("")
            # Consume remaining blank lines in original
            while i < len(lines) and lines[i].strip() == "":
                i += 1
            # Continue copying rest of sub-flow content (after integration table)
            while i < len(lines):
                result.append(lines[i])
                i += 1
            in_int = False
            continue

        result.append(line)
        i += 1

    return result


def build_subflow_content(sf_id, sf_data):
    """Build complete new sub-flow content (no AC tables)."""
    lines = []
    lines.append(f"### {sf_id}")
    lines.append("")
    lines.append(f"**Description:** {sf_data['description']}")
    lines.append("")
    lines.append(f"**Actors:** {sf_data['actors']}  ")
    lines.append(f"**Systems:** {sf_data['systems']}")
    lines.append("")
    lines.append("#### Sequence Diagram")
    lines.append("")
    lines.append("```mermaid")
    lines.append("sequenceDiagram")
    for step in sf_data["mermaid"]:
        lines.append(step)
    lines.append("```")
    lines.append("")
    lines.append("#### Integration Details")
    lines.append("")
    lines.append(INT_HEADER)
    lines.append(INT_SEP)
    for row in sf_data["integrations"]:
        lines.append(format_row(row))
    # Add Acceptance Criteria table
    ac_rows = ED.ACCEPTANCE_CRITERIA.get(sf_id, [])
    if ac_rows:
        lines.append("")
        lines.append("#### Acceptance Criteria")
        lines.append("")
        lines.append(AC_HEADER)
        lines.append(AC_SEP)
        for ac in ac_rows:
            lines.append(format_row(ac))
    lines.append("")
    return lines


def build_new_section(sec_key, sec_data):
    """Build complete new section from data."""
    lines = []
    lines.append(f"# {sec_key}")
    lines.append("")
    lines.append(sec_data["description"])
    lines.append("")
    first = True
    for sf_id, sf_data in sec_data["subflows"].items():
        if not first:
            lines.append("---")
            lines.append("")
        first = False
        lines.extend(build_subflow_content(sf_id, sf_data))
    lines.append("")
    lines.append("---")
    lines.append("")
    return lines


def generate_toc():
    return """## Table of Contents

- [Student Administration  - BC008, BC014, BC019, BC044, BC052, BC032](#student-administration)
  - [1.1 Student Onboarding (Prospect → Enrollment)](#11-student-onboarding-prospect--enrollment)
  - [1.2 Enrollment & Registration](#12-enrollment--registration)
  - [1.3 Academic Records Management](#13-academic-records-management)
  - [1.4 Graduation & Certification](#14-graduation--certification)
- [Learning & Teaching  - BC001, BC023, BC028](#learning-teaching)
  - [2.1 Curriculum Management](#21-curriculum-management)
  - [2.2 Course Delivery & Assessment](#22-course-delivery--assessment)
  - [2.3 Timetable & Scheduling](#23-timetable--scheduling)
  - [2.4 Academic Advising & Progression Management](#24-academic-advising--progression-management)
- [HR & Faculty Management  - BC171](#hr-faculty-management)
  - [3.1 Faculty Recruitment](#31-faculty-recruitment)
  - [3.2 Payroll & Benefits](#32-payroll--benefits)
  - [3.3 Faculty Performance & Development](#33-faculty-performance--development)
- [Finance & Resource Management  - BC184](#finance-resource-management)
  - [4.1 Fee Assessment & Billing](#41-fee-assessment--billing)
  - [4.2 Financial Aid Management](#42-financial-aid-management)
  - [4.3 Procurement & Vendor Management](#43-procurement--vendor-management)
- [Research Management  - BC065, BC071, BC074, BC086, BC093, BC245](#research-management)
  - [5.1 Grant Lifecycle Management](#51-grant-lifecycle-management)
  - [5.2 Research Outputs & Publishing](#52-research-outputs--publishing)
  - [5.3 Research Compliance & Ethics](#53-research-compliance--ethics)
- [Institutional Engagement  - BC107, BC232, BC238](#institutional-engagement)
  - [6.1 Marketing & Student Recruitment](#61-marketing--student-recruitment)
  - [6.2 Alumni Relations & Fundraising](#62-alumni-relations--fundraising)
  - [6.3 Community & Industry Partnerships](#63-community--industry-partnerships)
- [Library & Learning Support  - BC133, BC135](#library-learning-support)
  - [7.1 Library Resource Management](#71-library-resource-management)
  - [7.2 Digital Content Delivery & Course Reserves](#72-digital-content-delivery--course-reserves)
- [Enterprise Data & Analytics  - BC201, BC135](#enterprise-data-analytics)
  - [8.1 Data Integration & Warehousing](#81-data-integration--warehousing)
  - [8.2 Institutional Reporting & BI](#82-institutional-reporting--bi)
  - [8.3 Data Governance & Quality Management](#83-data-governance--quality-management)
- [Student Services & Wellbeing  - BC052, BC019](#student-services--wellbeing)
  - [9.1 Student Support & Counselling Services](#91-student-support--counselling-services)
  - [9.2 Career Services & Placement](#92-career-services--placement)
- [Facilities & Campus Operations  - BC125, BC114](#facilities--campus-operations)
  - [10.1 Facility Management & Space Allocation](#101-facility-management--space-allocation)
  - [10.2 Security & Access Control](#102-security--access-control)
  - [10.3 Ancillary Services Management](#103-ancillary-services-management)
- [Governance, Risk & Compliance  - BC160, BC155](#governance-risk--compliance)
  - [11.1 Policy Management & Accreditation](#111-policy-management--accreditation)
  - [11.2 Risk Management & Audit](#112-risk-management--audit)
"""


def generate_test_data():
    existing = {
        "Student": [("id", "STU-2026-001"), ("name", "John Doe"), ("email", "john.doe@university.edu"),
                    ("program", "B.Sc. Computer Science"), ("semester", "Fall 2026"), ("gpa", "3.75")],
        "Prospect": [("id", "PRO-2026-042"), ("name", "Jane Smith"), ("email", "jane.smith@prospect.com"),
                     ("program", "M.Sc. Data Science"), ("source", "Open Day")],
        "Course": [("id", "CS501"), ("title", "Artificial Intelligence & ML"), ("credits", "4"),
                   ("instructor", "Dr. Sarah Smith"), ("capacity", "120"), ("enrolled", "98")],
        "Faculty": [("id", "FAC-101"), ("name", "Dr. Sarah Smith"), ("dept", "Computer Science"),
                    ("email", "sarah.smith@university.edu"), ("hire_date", "2024-08-15"), ("salary", "95000")],
        "Finance": [("fee_amount", "12500.0"), ("scholarship", "2500.0"), ("grant_amount", "5000.0"),
                    ("invoice_no", "INV-2026-8901"), ("payment_ref", "PAY-7X3K2")],
        "Research": [("grant_id", "GR-2026-045"), ("title", "AI-Driven Personalized Learning"),
                     ("amount", "250000.0"), ("sponsor", "NSF"), ("pi", "Dr. Sarah Smith"), ("status", "Active")],
        "Alumni": [("id", "ALUM-2019-088"), ("name", "Emily Johnson"), ("grad_year", "2019"),
                   ("degree", "B.Sc. Computer Science"), ("email", "emily.j@corp.com")],
    }
    all_entities = dict(existing)
    for name, fields in ED.NEW_TEST_DATA.items():
        if name not in all_entities:
            all_entities[name] = fields

    lines = ["## Test Data", "",
             "The following test data is used consistently across all sequence diagrams:", "",
             "| Entity | Field | Value |", "|--------|-------|-------|"]
    for name in sorted(all_entities.keys()):
        fields = all_entities[name]
        first = True
        for key, val in fields:
            prefix = f"**{name}**" if first else ""
            lines.append(f"| {prefix} | {key} | {val} |")
            first = False
    lines.append("")
    return "\n".join(lines)


def get_section_header_simple(full_text, sec_name_part):
    """Find a section H1 matching the given name."""
    for l in full_text.split("\n"):
        s = l.strip()
        if s.startswith("# ") and not s.startswith("## ") and sec_name_part.lower() in s.lower().replace(":", ""):
            return s
    return None


def get_section_preamble(full_text, sec_h1):
    """Get the description paragraph(s) between a section H1 and the first sub-flow."""
    lines = full_text.split("\n")
    result = []
    after_h1 = False
    for l in lines:
        s = l.strip()
        if s == sec_h1.strip():
            after_h1 = True
            continue
        if after_h1:
            if s.startswith("### ") and not s.startswith("####"):
                break
            result.append(l)
    return result


def build_section(full_text, sec_h1, sf_names, preamble_lines):
    """Build a section with processed sub-flows + new sub-flows + description."""
    lines = [sec_h1, ""]
    lines.extend(preamble_lines)

    sep_needed = False
    for sf_name in sf_names:
        sf_text = extract_subflow_text(full_text, sf_name)
        if not sf_text:
            safe = sf_name.encode("ascii", "replace").decode()
            print(f"  WARNING: Could not extract: {safe}")
            continue
        processed = process_subflow_text(sf_name, sf_text)
        if sep_needed:
            lines.append("")
            lines.append("---")
            lines.append("")
        lines.extend(processed)
        sep_needed = True

    # Add new sub-flows assigned to this section
    new_sfs = {nid: ndata for nid, ndata in ED.NEW_SUBFLOWS.items() if ndata["section"].lower() == section_name_from_h1(sec_h1).lower()}
    for nid, ndata in new_sfs.items():
        if sep_needed:
            lines.append("")
            lines.append("---")
            lines.append("")
        lines.extend(build_subflow_content(nid, ndata))
        sep_needed = True

    return lines


def section_name_from_h1(h1):
    """Extract clean section name from H1 line."""
    # e.g. "# Student Administration  - `BC008` `BC014` ..."
    m = re.match(r"#\s+(.+?)\s*-", h1)
    if m:
        return m.group(1).strip()
    return h1.lstrip("# ").strip()


def main():
    import shutil
    full = read_current()

    if not BAK.exists():
        shutil.copy2(README, BAK)
        print(f"  Backup: {BAK}")

    # Extract prologue (everything before first section H1)
    lines = full.split("\n")
    h1_positions = [i for i, l in enumerate(lines) 
                    if l.strip().startswith("# ") and not l.strip().startswith("## ")]
    
    if len(h1_positions) < 2:
        print("ERROR: Could not find section H1 headings")
        return

    prologue = "\n".join(lines[:h1_positions[1]])

    # Build sections
    section_defs = [
        ("Student Administration", ["1.1 Student Onboarding (Prospect → Enrollment)",
                                     "1.2 Enrollment & Registration",
                                     "1.3 Academic Records Management",
                                     "1.4 Graduation & Certification"]),
        ("Learning & Teaching", ["2.1 Curriculum Management",
                                  "2.2 Course Delivery & Assessment",
                                  "2.3 Timetable & Scheduling",
                                  # 2.4 will be added as new
                                 ]),
        ("HR & Faculty Management", ["3.1 Faculty Recruitment",
                                       "3.2 Payroll & Benefits",
                                       "3.3 Faculty Performance & Development"]),
        ("Finance & Resource Management", ["4.1 Fee Assessment & Billing",
                                            "4.2 Financial Aid Management",
                                            "4.3 Procurement & Vendor Management"]),
        ("Research Management", ["5.1 Grant Lifecycle Management",
                                  "5.2 Research Outputs & Publishing"]),
        ("Institutional Engagement", ["6.1 Marketing & Student Recruitment",
                                       "6.2 Alumni Relations & Fundraising"]),
        ("Library & Learning Support", ["7.1 Library Resource Management"]),
        ("Enterprise Data & Analytics", ["8.1 Data Integration & Warehousing",
                                          "8.2 Institutional Reporting & BI"]),
    ]

    built_sections = []
    for sec_name, sf_names in section_defs:
        h1 = get_section_header_simple(full, sec_name)
        if not h1:
            print(f"  WARNING: Could not find H1 for section: {sec_name}")
            continue
        preamble = get_section_preamble(full, h1)
        sec_lines = build_section(full, h1, sf_names, preamble)
        # Trim trailing separators/blanks
        while sec_lines and sec_lines[-1] in ("", "---"):
            sec_lines.pop()
        sec_lines.append("")
        built_sections.append("\n".join(sec_lines))
        print(f"  Built section: {sec_name}")

    # Build new sections 9-11
    new_sections = []
    for sec_key, sec_data in ED.NEW_SECTIONS.items():
        ns = "\n".join(build_new_section(sec_key, sec_data))
        new_sections.append(ns)
        print(f"  Built new section: {sec_key.split('  -')[0].strip()}")

    # ── Assemble ──
    parts = [prologue.strip(), ""]
    parts.append(generate_toc())
    parts.append("")
    parts.append(generate_test_data())
    parts.append("")
    parts.append("---")
    parts.append("")

    for bs in built_sections:
        parts.append(bs)

    for ns in new_sections:
        parts.append(ns)

    result = "\n".join(parts)

    write_readme(result)

    # Stats
    fl = result.split("\n")
    h1_count = sum(1 for l in fl if l.strip().startswith("# ") and not l.strip().startswith("## ") and "Higher Education Process" not in l)
    h3_count = sum(1 for l in fl if l.strip().startswith("### ") and not l.strip().startswith("#### "))
    int_rows = result.count(INT_SEP)
    test_entities = set()
    for l in fl:
        m = re.match(r"\|\s*\*\*(\w+)\*\*\s*\|", l)
        if m:
            test_entities.add(m.group(1))

    print(f"\n  Sections:     {h1_count} (target: 11)")
    print(f"  Sub-flows:    {h3_count}")
    print(f"  Int tables:   {int_rows}")
    print(f"  Test entities: {len(test_entities)}")
    print(f"  Total lines:  {len(fl)}")


if __name__ == "__main__":
    main()
