"""Build the complete Insurance README.md from expand_readme.py data."""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

import sys
sys.path.insert(0, str(ROOT / "Scripts"))
import expand_readme as ED

README = ROOT / "README.md"

INT_TABLE_HEADER = "| Flow | Entity | Info Flow | Source | Target | Source Conn | Target Conn | Pattern | Complexity |"
INT_TABLE_SEP = "|------|--------|-----------|--------|--------|-------------|-------------|---------|------------|"
AC_TABLE_HEADER = "| Flow | Entity | Acceptance Criterion | Expected Outcome |"
AC_TABLE_SEP = "|------|--------|---------------------|------------------|"


def format_table_row(items):
    escaped = [str(c).replace("|", "\\|") for c in items]
    return "| " + " | ".join(escaped) + " |"


def build_acord_section():
    from add_acord_model import ACORD_CAPABILITIES
    lines = []
    lines.append("## ACORD Business Capability Model Reference")
    lines.append("")
    lines.append("The ACORD (Association for Cooperative Operations Research and Development) Capability Model defines the standard business capabilities for insurance institutions. The table below lists all relevant capabilities across 10 Level-1 domains. Each process flow in this document is mapped to its relevant ACORD capability codes.")
    lines.append("")

    groups = {}
    for l1, l2, code, desc in ACORD_CAPABILITIES:
        groups.setdefault(l1, []).append((l2, code, desc))

    for domain in ["Product", "Distribution", "Underwriting", "Policy", "Claims",
                   "Reinsurance", "Financial & Actuarial", "Customer",
                   "Risk & Compliance", "Enterprise & IT"]:
        caps = groups.get(domain, [])
        if not caps:
            continue
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


def build_subflow(sf_id, sf_data):
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
    lines.append(INT_TABLE_HEADER)
    lines.append(INT_TABLE_SEP)
    for row in sf_data["integrations"]:
        lines.append(format_table_row(row))
    lines.append("")
    lines.append("#### Acceptance Criteria")
    lines.append("")
    lines.append(AC_TABLE_HEADER)
    lines.append(AC_TABLE_SEP)
    for flow, entity, criterion, outcome in sf_data["acceptance"]:
        criterion_esc = criterion.replace("|", "\\|")
        outcome_esc = outcome.replace("|", "\\|")
        lines.append(f"| {flow} | {entity} | {criterion_esc} | {outcome_esc} |")
    lines.append("")
    return "\n".join(lines)


def build_toc():
    lines = []
    lines.append("## Table of Contents")
    lines.append("")

    for sec_num, sec_name, codes, subflows in ED.SECTION_DEFS:
        display = f"{sec_num}: {sec_name}"
        anchor = display.lower().replace(":", "").replace(" ", "-")
        anchor = re.sub(r"[`'\"!@#$%^&*()+=,./?;:{}[\]|\\~]", "", anchor)
        lines.append(f"- [{display}](#{anchor})")
        for sf_id in subflows:
            sf_anchor = sf_id.lower().replace(" ", "-")
            sf_anchor = re.sub(r"[`'\"!@#$%^&*()+=,./?;:{}[\]|\\~]", "", sf_anchor)
            lines.append(f"  - [{sf_id}](#{sf_anchor})")

    lines.append("")
    return "\n".join(lines)


def build_test_data():
    lines = []
    lines.append("## Test Data")
    lines.append("")
    lines.append("| Entity | Field | Value |")
    lines.append("|--------|-------|-------|")

    for name in sorted(ED.NEW_TEST_DATA.keys()):
        fields = ED.NEW_TEST_DATA[name]
        first = True
        for key, val in fields:
            if first:
                lines.append(f"| **{name}** | {key} | {val} |")
                first = False
            else:
                lines.append(f"| | {key} | {val} |")

    lines.append("")
    return "\n".join(lines)


def main():
    print("=" * 60)
    print("  BUILDING INSURANCE README")
    print("=" * 60)

    result_parts = []

    # Title
    result_parts.append("# Insurance Domain Process Flows — ACORD Capability Model Reference")
    result_parts.append("")
    result_parts.append("> Generated on 2026-07-09 | Domain: Insurance | Framework: ACORD (Association for Cooperative Operations Research and Development)")
    result_parts.append("")
    result_parts.append("")

    # ACORD section
    result_parts.append(build_acord_section())
    result_parts.append("")

    # TOC
    result_parts.append(build_toc())
    result_parts.append("")

    # Test Data
    result_parts.append(build_test_data())
    result_parts.append("")

    # Domain sections
    for sec_num, sec_name, codes, subflows in ED.SECTION_DEFS:
        badges = " ".join(f"`{c}`" for c in codes)
        section_lines = [f"# {sec_num}: {sec_name}  — {badges}", ""]

        for sf_id in subflows:
            sf_data = ED.ALL_SUBFLOWS.get(sf_id)
            if not sf_data:
                print(f"  WARNING: Missing sub-flow data: {sf_id}")
                continue
            section_lines.append(build_subflow(sf_id, sf_data))
            section_lines.append("---")
            section_lines.append("")

        result_parts.append("\n".join(section_lines))

    # Final
    result = "\n".join(result_parts)

    # Write
    README.write_text(result, encoding="utf-8")

    # Stats
    final_lines = result.split("\n")
    h1_count = sum(1 for l in final_lines if l.strip().startswith("# ") and not l.strip().startswith("## "))
    h3_count = sum(1 for l in final_lines if l.strip().startswith("### ") and not l.strip().startswith("#### "))
    int_tables = result.count(INT_TABLE_SEP)
    ac_tables = result.count(AC_TABLE_SEP)

    print()
    print(f"  Sections:     {h1_count} (target: 16)")
    print(f"  Sub-flows:    {h3_count}")
    print(f"  Int tables:   {int_tables}")
    print(f"  AC tables:    {ac_tables}")
    print(f"  Total lines:  {len(final_lines)}")
    print()
    print(f"  Written: {README}")
    print()


if __name__ == "__main__":
    main()
