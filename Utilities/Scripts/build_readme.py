"""Build Utilities domain README.md from definitions and section data files."""

import sys
from pathlib import Path
from collections import OrderedDict

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "Scripts"))

from definitions import FRAMEWORK, CAPABILITY_MODEL, TEST_DATA

SECTION_FILES = ["defs_s1", "defs_s2", "defs_s3", "defs_s4"]

INT_HEADER = "| Flow | Entity | Info Flow | Source | Target | Source Conn | Target Conn | Pattern | Complexity |"
INT_SEP    = "|------|--------|-----------|--------|--------|-------------|-------------|---------|------------|"
AC_HEADER  = "| AC ID | Description | Related Info Flow | Expected Outcome | Priority |"
AC_SEP     = "|-------|------------|-------------------|------------------|----------|"

README = ROOT / "README.md"


def fmt(items):
    return "| " + " | ".join(str(c).replace("|", "\\|") for c in items) + " |"


def generate_capability_model():
    lines = [
        "## EPRI Utility Business Capability Model Reference",
        "",
        "The EPRI Utility Business Capability Model (UCBM) defines standard business capabilities for electric, gas, and water utilities. The table below lists all Level 2 capabilities grouped by Level 1 domain. Each process flow in this document is mapped to its relevant UCBM capability codes.",
        "",
        "![EPRI Utility Business Capability Model overview - Customer, Grid Operations, Generation, Water, Enterprise, and Technology domains](./Document/utilities-brm-overview.png)",
        "",
        "*Source: EPRI Utility Business Capability Model (2024) — used under EPRI public version license*",
        "",
    ]
    for domain, caps in CAPABILITY_MODEL.items():
        lines.append(f"### {domain}")
        lines.append("")
        lines.append("| Capability | Code | Description |")
        lines.append("|-----------|------|-------------|")
        for name, code, desc in caps:
            lines.append(f"| **{name}** | `{code}` | {desc} |")
        lines.append("")
    return "\n".join(lines)


def generate_toc():
    lines = ["## Table of Contents", ""]
    section_num = 1
    for sf_path in SECTION_FILES:
        mod = __import__(sf_path.replace(".py", ""))
        for sec_key, sec_data in mod.SECTION_DATA.items():
            caps = ", ".join(sec_data["capabilities"])
            anchor = sec_data["title"].split("  -")[0].strip().lower().replace(" ", "-").replace("&", "and").replace(",", "").replace("--", "-")
            lines.append(f"- [{sec_data['title']}](#{anchor})")
            for sf_id, sf in sec_data["subflows"].items():
                sf_anchor = sf_id + " " + sf["title"]
                sf_anchor_clean = sf_anchor.lower().replace(" ", "-").replace("&", "and").replace(",", "").replace("---", "-").replace("--", "-").replace("(", "").replace(")", "").replace("/", "-")
                lines.append(f"  - [{sf_id} {sf['title']}](#{sf_anchor_clean})")
        section_num += 1
    lines.append("")
    return "\n".join(lines)


def generate_test_data():
    lines = [
        "## Test Data",
        "",
        "The following test data is used consistently across all sequence diagrams:",
        "",
        "| Entity | Field | Value |",
        "|--------|-------|-------|",
    ]
    for name, fields in TEST_DATA.items():
        first = True
        for key, val in fields:
            prefix = f"**{name}**" if first else ""
            lines.append(f"| {prefix} | {key} | {val} |")
            first = False
    lines.append("")
    return "\n".join(lines)


def build_subflow(sf_id, sf):
    lines = []
    lines.append(f"### {sf_id} {sf['title']}")
    lines.append("")
    lines.append(f"**Description:** {sf['description']}")
    lines.append("")
    actors_str = ", ".join(sf["actors"])
    systems_str = ", ".join(sf["systems"])
    lines.append(f"**Actors:** {actors_str}  ")
    lines.append(f"**Systems:** {systems_str}")
    lines.append("")
    lines.append("#### Sequence Diagram")
    lines.append("")
    lines.append("```mermaid")
    lines.append("sequenceDiagram")
    for step in sf["mermaid"]:
        lines.append(step.replace("\n", "<br/>"))
    lines.append("```")
    lines.append("")
    lines.append("#### Integration Details")
    lines.append("")
    lines.append(INT_HEADER)
    lines.append(INT_SEP)
    for row in sf["integrations"]:
        lines.append(fmt(row))
    if sf.get("acceptance_criteria"):
        lines.append("")
        lines.append("#### Acceptance Criteria")
        lines.append("")
        lines.append(AC_HEADER)
        lines.append(AC_SEP)
        for ac in sf["acceptance_criteria"]:
            lines.append(fmt(ac))
    lines.append("")
    return lines


def build_section(sec_data):
    lines = []
    lines.append(f"# {sec_data['title']}")
    lines.append("")
    lines.append(sec_data["description"])
    lines.append("")
    first = True
    for sf_id, sf in sec_data["subflows"].items():
        if not first:
            lines.append("---")
            lines.append("")
        first = False
        lines.extend(build_subflow(sf_id, sf))
    lines.append("---")
    lines.append("")
    return lines


def count_tables(readme_text):
    return readme_text.count(INT_SEP), readme_text.count(AC_SEP)


def main():
    all_sections = []
    for sf_path in SECTION_FILES:
        mod = __import__(sf_path.replace(".py", ""))
        for sec_key, sec_data in mod.SECTION_DATA.items():
            all_sections.append(build_section(sec_data))

    parts = [
        f"# {FRAMEWORK['business_domain']} Process Flows \u2014 {FRAMEWORK['framework_name']}",
        "",
        f"> Generated on {FRAMEWORK['generated_date']} | Domain: {FRAMEWORK['business_domain']} | Framework: {FRAMEWORK['framework_name']}",
        "",
        generate_capability_model(),
        "---",
        "",
        generate_toc(),
        "",
        generate_test_data(),
        "",
    ]

    for sec in all_sections:
        parts.append("\n".join(sec))

    result = "\n".join(parts)
    README.write_text(result, encoding="utf-8")

    lines = result.split("\n")
    h1_count = sum(1 for l in lines if l.strip().startswith("# ") and not l.strip().startswith("## ") and "Process Flows" not in l)
    h3_count = sum(1 for l in lines if l.strip().startswith("### ") and not l.strip().startswith("#### "))
    int_tables, ac_tables = count_tables(result)
    int_rows = int_tables
    test_ents = set()
    for l in lines:
        if l.strip().startswith("| **") and "|" in l[3:]:
            ent = l.strip().split("|")[1].strip().strip("**")
            if ent:
                test_ents.add(ent)

    print(f"README generated: {README} ({len(lines)} lines)")
    print(f"  Sections:     {h1_count} (target: 16)")
    print(f"  Sub-flows:    {h3_count}")
    print(f"  Int tables:   {int_rows}")
    print(f"  AC tables:    {ac_tables}")
    print(f"  Test entities: {len(test_ents)}")


if __name__ == "__main__":
    main()
