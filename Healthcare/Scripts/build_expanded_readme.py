"""Build expanded Healthcare README by combining existing content with new data."""

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
            while i < len(lines) and lines[i].strip() == "":
                result.append(lines[i])
                i += 1
            while i < len(lines) and lines[i].strip().startswith("|"):
                result.append(lines[i])
                i += 1
                if lines[i-1].strip() == INT_SEP:
                    break
            while i < len(lines):
                si = lines[i].strip()
                if si.startswith("|"):
                    result.append(lines[i])
                    i += 1
                elif si == "":
                    break
                else:
                    break
            extra = ED.EXTRA_INTEGRATIONS.get(sf_name, [])
            if extra:
                for row in extra:
                    result.append(format_row(row))
                print(f"  Added {len(extra)} integration rows to {sf_name}")
            result.append("")
            continue

        if s == "#### Acceptance Criteria":
            result.append(line)
            i += 1
            while i < len(lines) and lines[i].strip() == "":
                result.append(lines[i])
                i += 1
            while i < len(lines):
                si = lines[i].strip()
                if si.startswith("|"):
                    result.append(lines[i])
                    i += 1
                elif si == "":
                    break
                else:
                    break
            extra_ac = ED.ACCEPTANCE_CRITERIA.get(sf_name, [])
            if extra_ac:
                for row in extra_ac:
                    result.append(format_row(row))
                print(f"  Added {len(extra_ac)} acceptance criteria to {sf_name}")
            result.append("")
            continue

        result.append(line)
        i += 1

    return "\n".join(result)


def add_new_sections(text):
    """Add new sections defined in expand_readme.py that don't exist yet."""
    lines = text.split("\n")
    # Check which sections already exist
    existing_sections = set()
    for line in lines:
        m = re.match(r"^# (.*?)\s*-", line.strip())
        if m:
            existing_sections.add(m.group(1).strip())

    new_sections = []
    for section_name, section_data in ED.NEW_SECTIONS.items():
        if section_name not in existing_sections:
            new_sections.append((section_name, section_data))
            print(f"  New section to add: {section_name}")

    if not new_sections:
        return text

    # Find insertion point - after all existing sections (after last # heading)
    last_section_idx = 0
    for i, line in enumerate(lines):
        if line.strip().startswith("# ") and not line.strip().startswith("## "):
            if "Healthcare Process" not in line:
                last_section_idx = i

    # Add after last section's --- separator
    while last_section_idx < len(lines) and not lines[last_section_idx].strip().startswith("---"):
        last_section_idx += 1
    if last_section_idx < len(lines):
        last_section_idx += 1  # skip the ---

    insert_lines = []
    for section_name, section_data in new_sections:
        insert_lines.append(f"\n# {section_name}  - {' '.join(f'`{c}`' for c in ED.SECTION_CAPABILITY_MAP.get(section_name, []))}\n")
        insert_lines.append(f"{section_data.get('description', '')}\n")
        for sf_id, sf_data in section_data.get("subflows", []):
            insert_lines.append(f"### {sf_id} {sf_data['title']}\n")
            insert_lines.append(f"**Description:** {sf_data['description']}\n")
            insert_lines.append(f"**Actors:** {sf_data['actors']}\n")
            insert_lines.append(f"**Systems:** {sf_data['systems']}\n")
            insert_lines.append("\n#### Sequence Diagram\n\n```mermaid\n")
            insert_lines.append(f"{sf_data['mermaid']}\n")
            insert_lines.append("```\n\n#### Integration Details\n\n")
            insert_lines.append(f"{INT_HEADER}\n{INT_SEP}\n")
            for row in sf_data.get("integrations", []):
                insert_lines.append(f"{format_row(row)}\n")
            insert_lines.append("\n#### Acceptance Criteria\n\n")
            insert_lines.append(f"{AC_HEADER}\n{AC_SEP}\n")
            for row in sf_data.get("acceptance_criteria", []):
                insert_lines.append(f"{format_row(row)}\n")
            insert_lines.append("\n")
        insert_lines.append("---\n")

    result = lines[:last_section_idx] + insert_lines + lines[last_section_idx:]
    return "\n".join(result)


def add_new_test_data(text):
    """Append new test data entities."""
    lines = text.split("\n")
    td_end = None
    for i, line in enumerate(lines):
        if line.strip() == "## Test Data":
            td_end = i
        if td_end and line.strip().startswith("## ") and line.strip() != "## Test Data":
            # Found end of test data section
            break

    if td_end is None:
        print("ERROR: Could not find Test Data section")
        return text

    existing_entities = set()
    for line in lines:
        m = re.match(r"\|\s*\*\*(\w+)\*\*\s*\|", line)
        if m:
            existing_entities.add(m.group(1))

    new_entities = []
    for entity_name, fields in ED.NEW_TEST_DATA.items():
        if entity_name not in existing_entities:
            for field_name, field_value in fields:
                new_entities.append((entity_name, field_name, field_value))

    if not new_entities:
        print("  No new test data entities to add")
        return text

    # Insert after last test data row
    insert_idx = td_end
    for i in range(td_end, len(lines)):
        if lines[i].strip().startswith("|") and i > insert_idx:
            insert_idx = i

    # Build new rows
    new_rows = []
    for entity_name, field_name, field_value in new_entities:
        new_rows.append(f"| **{entity_name}** | {field_name} | {field_value} |")
    # Only keep entity name on first occurrence
    output_rows = []
    prev_entity = None
    for row in new_rows:
        m = re.match(r"\|\s*\*\*(\w+)\*\*\s*\|", row)
        if m:
            curr_entity = m.group(1)
            if curr_entity == prev_entity:
                # Replace entity with empty
                parts = row.split("|")
                parts[1] = " "
                row = "|".join(parts)
            else:
                prev_entity = curr_entity
        output_rows.append(row)

    result = lines[:insert_idx+1] + ["", ""] + output_rows + lines[insert_idx+1:]
    print(f"  Added {len(new_entities)} new test data rows")
    return "\n".join(result)


def main():
    print("Building expanded Healthcare README...")
    text = read_current()

    # Add new test data
    print("\n1. Adding new test data...")
    text = add_new_test_data(text)

    # Add new sections
    print("\n2. Adding new sections...")
    text = add_new_sections(text)

    # Process each sub-flow to add extra integrations and acceptance criteria
    print("\n3. Processing sub-flow enhancements...")
    lines = text.split("\n")
    result_lines = []
    i = 0
    while i < len(lines):
        line = lines[i]
        s = line.strip()
        if s.startswith("### ") and not s.startswith("####"):
            heading = s.lstrip("### ").strip()
            sf_text_lines = [lines[i]]
            i += 1
            while i < len(lines):
                si = lines[i].strip()
                if si.startswith("### ") and not si.startswith("####"):
                    break
                if si.startswith("# ") and not si.startswith("## "):
                    break
                sf_text_lines.append(lines[i])
                i += 1
            sf_text = "\n".join(sf_text_lines)
            sf_text = process_subflow_text(heading, sf_text)
            result_lines.append(sf_text)
            # Don't increment i again - already at next section
            continue
        result_lines.append(line)
        i += 1

    text = "\n".join(result_lines)

    write_readme(text)
    print("\nDone!")


if __name__ == "__main__":
    main()
