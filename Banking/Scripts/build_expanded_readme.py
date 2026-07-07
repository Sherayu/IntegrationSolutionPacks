"""Build the expanded Banking README by combining existing content with new data."""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Append script dir to import expand_readme data
sys.path.insert(0, str(ROOT / "Scripts"))
import expand_readme as ED

README = ROOT / "README.md"
BAK = ROOT / "README.md.bak"


def read_current_readme():
    # Always read from backup if it exists (clean original state)
    source = BAK if BAK.exists() else README
    with open(source, "r", encoding="utf-8") as f:
        return f.read()


def write_readme(text):
    with open(README, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"  Written: {README} ({len(text.split(chr(10)))} lines)")


def extract_subflow_text(full_text, sf_name):
    """Extract the complete text of an existing sub-flow from the README,
    including its description, actors/systems, mermaid, integration table, AC table."""
    lines = full_text.split("\n")
    result = []
    in_sf = False
    sf_depth = 0

    for line in lines:
        stripped = line.strip()
        if stripped.startswith("### ") and not stripped.startswith("####"):
            if sf_name in stripped:
                in_sf = True
                sf_depth = 1
                result.append(line)
            elif in_sf:
                break  # next sub-flow or end
            continue

        if in_sf:
            if stripped.startswith("# ") and not stripped.startswith("## "):
                break
            result.append(line)

    return "\n".join(result)


def extract_section_text(full_text, section_title):
    """Extract the complete section text (H1 to next H1 or EOF)."""
    lines = full_text.split("\n")
    result = []
    found = False

    for line in lines:
        stripped = line.strip()
        if stripped.startswith("# ") and not stripped.startswith("## "):
            if found:
                break
            # Match section title (flexible match)
            norm = section_title.lower().replace("  ", " ")
            line_norm = stripped.lower().replace("  ", " ")
            if norm in line_norm:
                found = True
                result.append(line)
                continue

        if found:
            result.append(line)

    return "\n".join(result)


def strip_existing_subflow_section(section_text):
    """Remove all sub-flow content from a section text, keeping only the section
    header and any non-subflow lines."""
    lines = section_text.split("\n")
    result = []
    in_sf = False

    for line in lines:
        stripped = line.strip()
        if stripped.startswith("### ") and not stripped.startswith("####"):
            in_sf = True
        if in_sf:
            if stripped.startswith("### ") and not stripped.startswith("####"):
                pass  # skip sub-flow headers
            continue
        result.append(line)

    return "\n".join(result)


def subflow_heading(sf_id):
    return f"### {sf_id}"


def format_table_row(items):
    escaped = [str(c).replace("|", "\\|") for c in items]
    return "| " + " | ".join(escaped) + " |"


INT_TABLE_HEADER = "| Flow | Entity | Info Flow | Source | Target | Source Conn | Target Conn | Pattern | Complexity |"
INT_TABLE_SEP = "|------|--------|-----------|--------|--------|-------------|-------------|---------|------------|"
AC_TABLE_HEADER = "| Flow | Entity | Acceptance Criterion | Expected Outcome |"
AC_TABLE_SEP = "|------|--------|---------------------|------------------|"


def legacy_subflows():
    """Return ordered list of sub-flow IDs for sections 1-8."""
    return [
        "1.1 New Customer Onboarding & KYC",
        "1.2 Retail Account Opening",
        "1.3 Corporate Account Opening",
        "2.1 Domestic Payment (SEPA/ACH)",
        "2.2 Cross-Border Payment (SWIFT)",
        "2.3 Real-Time Payment (Faster Payments)",
        "3.1 Retail Loan Origination",
        "3.2 Mortgage Lending",
        "3.3 Credit Assessment & Scoring",
        "4.1 Card Issuance",
        "4.2 Card Transaction Processing",
        "4.3 Card Dispute Management",
        "5.1 Account Operations (Current/Savings)",
        "5.2 Term Deposits",
        "5.3 Sweep & Investment Products",
        "6.1 Fraud Detection & Prevention",
        "6.2 AML/Sanctions Screening",
        "6.3 Regulatory Reporting",
        "7.1 Internet Banking",
        "7.2 Mobile Banking",
        "7.3 Branch Banking (Teller)",
        "8.1 Nostro/Vostro Reconciliation",
        "8.2 Treasury & Liquidity Management",
        "8.3 End-of-Day Settlement",
    ]


def build_all_sections():
    """Build the complete set of sections for the expanded README."""
    full_text = read_current_readme()

    # ── Section definitions (header name, BIAN codes) ──
    section_defs = [
        ("Customer Onboarding & Account Management", "BC032 BC033 BC031"),
        ("Payments & Transfers", "BC060 BC061"),
        ("Lending & Credit Management", "BC070"),
        ("Cards Management", "BC071"),
        ("Deposits & Savings Products", "BC072 BC073"),
        ("Risk & Compliance", "BC012 BC013"),
        ("Channels & Digital Banking", "BC001 BC003 BC002"),
        ("Finance, Treasury & Settlement", "BC010 BC014 BC061 BC062"),
    ]

    # Build each section
    all_sections = {}
    sf_order = legacy_subflows()

    for sec_idx, (sec_name, codes) in enumerate(section_defs):
        sec_num = sec_idx + 1
        header = f"# {sec_num}: {sec_name}  - `{'` `'.join(codes.split())}`"

        # Extract existing sub-flows for this section
        existing_sfs = []
        for sf_name in sf_order:
            if sf_name.startswith(f"{sec_num}."):
                existing_sfs.append(sf_name)

        # Build section content
        section_lines = [header, ""]

        for sf_name in existing_sfs:
            sf_text = extract_subflow_text(full_text, sf_name)
            if not sf_text:
                print(f"  WARNING: Could not extract sub-flow: {sf_name}")
                continue

            # Parse the sub-flow into components
            sf_lines = sf_text.split("\n")
            processed = process_subflow_lines(sf_name, sf_lines)
            section_lines.extend(processed)

            # Add separator
            section_lines.append("")
            section_lines.append("---")
            section_lines.append("")

        # Add new sub-flow if applicable
        new_sf = get_new_subflow(sec_num)
        if new_sf:
            section_lines.extend(new_sf)
            section_lines.append("")
            section_lines.append("---")
            section_lines.append("")

        # Remove trailing separators
        while section_lines and section_lines[-1] in ("", "---"):
            section_lines.pop()

        all_sections[sec_num] = "\n".join(section_lines)

    return all_sections


def process_subflow_lines(sf_name, lines):
    """Process sub-flow lines, inserting extra integration and AC rows."""
    result = []
    i = 0
    state = "HEADER"  # HEADER, MERMAID, INT_HEADER, INT_TABLE, INT_DONE, AC_HEADER, AC_TABLE, AC_DONE, DONE

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        result.append(line)

        if stripped == "#### Integration Details":
            state = "INT_HEADER"
            i += 1
            # Copy blank lines and table header/separator
            while i < len(lines):
                result.append(lines[i])
                if lines[i].strip() == INT_TABLE_SEP:
                    i += 1
                    break
                i += 1

            # Copy existing table rows
            while i < len(lines):
                stripped_i = lines[i].strip()
                if stripped_i.startswith("|"):
                    result.append(lines[i])
                    i += 1
                else:
                    break

            # Insert extra integration rows
            extra = ED.EXTRA_INTEGRATIONS.get(sf_name, [])
            if extra:
                for row in extra:
                    result.append(format_table_row(row))
                state = "INT_DONE"

        elif stripped == "#### Acceptance Criteria":
            state = "AC_HEADER"
            i += 1
            # Copy blank lines and table header/separator
            while i < len(lines):
                result.append(lines[i])
                if lines[i].strip() == AC_TABLE_SEP:
                    i += 1
                    break
                i += 1

            # Copy existing table rows
            while i < len(lines):
                stripped_i = lines[i].strip()
                if stripped_i.startswith("|"):
                    result.append(lines[i])
                    i += 1
                else:
                    break

            # Insert extra AC rows
            extra = ED.EXTRA_ACCEPTANCE.get(sf_name, [])
            if extra:
                for row in extra:
                    result.append(format_table_row(row))
                state = "AC_DONE"

        i += 1

    return result


def get_new_subflow(sec_num):
    """Get new sub-flow content for a section, or None."""
    mapping = {
        2: "2.4 Batch Payment Processing",
        3: "3.4 Loan Servicing & Collections",
        4: "4.4 Card Rewards & Loyalty",
        5: "5.4 Overdraft Management",
    }

    sf_id = mapping.get(sec_num)
    if not sf_id:
        return None

    sf_data = ED.NEW_SUBFLOWS.get(sf_id)
    if not sf_data:
        return None

    return build_subflow_content(sf_id, sf_data)


def build_subflow_content(sf_id, sf_data):
    """Build complete sub-flow content from data."""
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
        sf_content = build_subflow_content(sf_id, sf_data)
        lines.extend(sf_content)
    return lines


def generate_toc(section_defs, all_sections, new_sections, new_subflow_ids):
    """Generate Table of Contents."""
    lines = []
    lines.append("## Table of Contents")
    lines.append("")

    for sec_num, (sec_name, _) in enumerate(section_defs, 1):
        anchor = f"{sec_num}: {sec_name}".lower().replace(":", "").replace("  ", " ").replace(" ", "-")
        anchor = re.sub(r"[`'\"!@#$%^&*()+=,./?;:{}[\]|\\~]", "", anchor)
        lines.append(f"- [{sec_num}: {sec_name}](#{anchor})")

        # Sub-flows
        for sf_name in legacy_subflows():
            if sf_name.startswith(f"{sec_num}."):
                sf_anchor = sf_name.lower().replace(" ", "-")
                sf_anchor = re.sub(r"[`'\"!@#$%^&*()+=,./?;:{}[\]|\\~]", "", sf_anchor)
                lines.append(f"  - [{sf_name}](#{sf_anchor})")

        # New sub-flow
        new_id = {2: "2.4 Batch Payment Processing", 3: "3.4 Loan Servicing & Collections",
                  4: "4.4 Card Rewards & Loyalty", 5: "5.4 Overdraft Management"}.get(sec_num)
        if new_id:
            sf_anchor = new_id.lower().replace(" ", "-")
            sf_anchor = re.sub(r"[`'\"!@#$%^&*()+=,./?;:{}[\]|\\~]", "", sf_anchor)
            lines.append(f"  - [{new_id}](#{sf_anchor})")

    # New sections (9-12)
    for sec_key in ED.NEW_SECTIONS:
        sec_data = ED.NEW_SECTIONS[sec_key]
        # Parse section number from key
        sec_num = sec_key.split(":")[0].strip()
        sec_name_full = sec_key.split(":")[1].strip() if ":" in sec_key else sec_key
        # Remove codes from sec_name
        clean_name = re.sub(r"- `[A-Z0-9 `]+`", "", sec_name_full).strip()
        # Remove trailing codes
        clean_name = re.sub(r"`[A-Z0-9]+`", "", clean_name).strip().rstrip("-").strip()

        display = f"{sec_num}: {clean_name}"
        anchor = display.lower().replace(":", "").replace("  ", " ").replace(" ", "-").replace("--", "-")
        anchor = re.sub(r"[`'\"!@#$%^&*()+=,./?;:{}[\]|\\~]", "", anchor)
        lines.append(f"- [{display}](#{anchor})")

        for sf_id in sec_data["subflows"]:
            sf_anchor = sf_id.lower().replace(" ", "-")
            sf_anchor = re.sub(r"[`'\"!@#$%^&*()+=,./?;:{}[\]|\\~]", "", sf_anchor)
            lines.append(f"  - [{sf_id}](#{sf_anchor})")

    lines.append("")
    return "\n".join(lines)


def generate_test_data():
    """Generate expanded Test Data section with existing + new entities."""
    lines = []
    lines.append("## Test Data")
    lines.append("")

    # Combined test data: existing known entities + new ones
    existing_entities = {
        "Customer": [("customer_id", "CUST-2026-001"), ("name", "Alice Johnson"), ("dob", "1990-03-15"),
                     ("email", "alice.johnson@email.com"), ("phone", "+44 7700 900001"),
                     ("address", "123 Main Street, London")],
        "Account": [("account_id", "ACCT-4001-2026"), ("type", "Current Account"), ("balance", "44,490.50"),
                    ("currency", "GBP"), ("status", "Active"), ("customer_id", "CUST-2026-001")],
        "Beneficiary": [("beneficiary_id", "BEN-2026-001"), ("name", "John Smith"),
                        ("account_number", "GB29NWBK60161331926819"), ("sort_code", "60-13-31")],
        "Loan": [("loan_id", "LN-2026-042"), ("type", "Personal Loan"), ("amount", "25,000.00"),
                 ("term_months", "60"), ("interest_rate", "6.9% APR"), ("status", "Active"),
                 ("customer_id", "CUST-2026-001")],
        "CreditCard": [("card_id", "CARD-2026-001"), ("card_number", "****-****-****-1234"), ("type", "Visa Platinum"),
                       ("limit", "10,000.00"), ("balance", "2,350.00"), ("customer_id", "CUST-2026-001")],
        "Merchant": [("merchant_id", "MER-2026-042"), ("name", "Harrods London"), ("mcc_code", "5311"),
                     ("acquirer", "Worldpay")],
        "Transaction": [("txn_id", "TXN-2026-8901"), ("amount", "1,250.00"), ("currency", "GBP"),
                        ("type", "International Transfer"), ("timestamp", "2026-07-06T10:30:00Z"),
                        ("status", "Completed"), ("account_id", "ACCT-4001-2026")],
        "Employee": [("employee_id", "EMP-2026-011"), ("name", "Sarah Williams"), ("role", "Relationship Manager"),
                     ("branch_id", "BR-001-LDN")],
        "Branch": [("branch_id", "BR-001-LDN"), ("name", "London City Branch"), ("sort_code", "60-13-31"),
                   ("region", "London")],
        "Collateral": [("collateral_id", "COL-2026-001"), ("type", "Residential Property"),
                       ("value", "355,000.00"), ("lien_position", "First"), ("loan_id", "LN-2026-042")],
        "SavingsAccount": [("account_id", "SAV-2026-001"), ("balance", "15,750.25"), ("interest_rate", "2.75% p.a."),
                           ("customer_id", "CUST-2026-001")],
        "TermDeposit": [("deposit_id", "TD-2026-001"), ("amount", "50,000.00"), ("term_months", "12"),
                        ("interest_rate", "4.5% p.a."), ("maturity_date", "2027-07-06"),
                        ("customer_id", "CUST-2026-002")],
        "ComplianceCase": [("case_id", "AML-2026-088"), ("type", "Sanctions Screening"),
                           ("status", "Under Review"), ("severity", "High"),
                           ("related_entity", "CUST-2026-002")],
    }

    # Add all new test data
    all_entities = dict(existing_entities)
    for name, fields in ED.NEW_TEST_DATA.items():
        # Only add if not already present
        if name not in all_entities:
            all_entities[name] = fields

    # Write table
    lines.append("| Entity | Field | Value |")
    lines.append("|--------|-------|-------|")

    for name in sorted(all_entities.keys()):
        fields = all_entities[name]
        first = True
        for key, val in fields:
            if first:
                lines.append(f"| **{name}** | {key} | {val} |")
                first = False
            else:
                lines.append(f"| | {key} | {val} |")

    lines.append("")
    return "\n".join(lines)


def generate_bian_section():
    """Generate BIAN Capability Model Reference section."""
    # All existing BIAN capabilities
    bian_caps = [
        # Channels
        ("Channels", "Channel Activity Analysis", "BC001", "Analyze customer channel usage and preferences"),
        ("Channels", "Contact Center", "BC002", "Manage omnichannel customer interactions including voice, email, chat"),
        ("Channels", "Channel Management", "BC003", "Manage all customer interaction channels consistently"),
        ("Channels", "Internet Banking", "BC004", "Deliver banking services through internet channel"),
        ("Channels", "Mobile Banking", "BC005", "Deliver banking services through mobile devices"),
        # Finance & Risk
        ("Finance & Risk Management", "Regulatory Reporting", "BC012", "Generate and submit regulatory reports to authorities"),
        ("Finance & Risk Management", "AML & Sanctions", "BC013", "Screen against AML and sanctions lists"),
        ("Finance & Risk Management", "Treasury Management", "BC014", "Manage liquidity, funding, and treasury operations"),
        # Customers
        ("Customers", "Customer Onboarding", "BC032", "Manage end-to-end customer onboarding and KYC processes"),
        ("Customers", "Customer Access Entitlement", "BC031", "Manage customer authentication, authorization, and entitlements"),
        ("Customers", "Customer Relationship Management", "BC033", "Manage customer data, interactions, and relationships"),
        # Operations
        ("Operations", "Collections & Recovery", "BC077", "Manage debt collection, recovery, forbearance, and charged-off accounts"),
        # Products
        ("Products", "Payments", "BC060", "Process domestic and cross-border payments across all schemes"),
        ("Products", "Payment Execution", "BC061", "Execute payment instructions including validation and settlement"),
        ("Products", "Correspondent Banking", "BC062", "Manage correspondent banking relationships and nostro/vostro accounts"),
        ("Products", "Trade Finance", "BC063", "Manage letters of credit, guarantees, and trade finance instruments"),
        ("Products", "Lending", "BC070", "Originate, underwrite, and service loan products"),
        ("Products", "Cards", "BC071", "Manage card lifecycle from issuance to transaction processing to disputes"),
        ("Products", "Deposits", "BC072", "Manage current and savings deposit accounts"),
        ("Products", "Savings", "BC073", "Manage term deposits and savings products including sweep accounts"),
        ("Products", "Wealth Management", "BC074", "Manage client investment portfolios, financial planning, and advisory services"),
        ("Products", "Asset Management", "BC075", "Manage institutional assets, fund management, and investment strategies"),
        # Business Management
        ("Business Management", "Fraud Monitoring", "BC023", "Monitor and detect fraudulent transactions and activities"),
        ("Business Management", "Fraud Management", "BC024", "Manage fraud cases, investigations, and resolutions"),
        ("Business Management", "Channel Activity Analysis", "BC034", "Analyze contact center performance and customer behavior patterns"),
        # Resource Management
        ("Resource Management", "Reconciliation", "BC049", "Reconcile transactions and positions across internal and external systems"),
        ("Resource Management", "Settlement", "BC010", "Manage settlement of financial transactions across clearing systems"),
    ]

    lines = []
    lines.append("## BIAN Capability Model Reference")
    lines.append("")
    lines.append("The BIAN (Banking Industry Architecture Network) Capability Model defines the standard business capabilities for banking institutions. The table below lists all relevant capabilities grouped by domain. Each process flow in this document is mapped to its relevant BIAN capability codes.")
    lines.append("")

    groups = {}
    for l1, l2, code, desc in bian_caps:
        groups.setdefault(l1, []).append((l2, code, desc))

    for domain in ["Channels", "Customers", "Products", "Operations", "Finance & Risk Management", "Business Management", "Resource Management"]:
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
    return "\n".join(lines)


def format_new_section_header(sec_key):
    """Extract clean section number and name from key."""
    # Key format: "9: Trade Finance  - `BC063`"
    sec_num = sec_key.split(":")[0].strip()
    rest = sec_key.split(":", 1)[1].strip() if ":" in sec_key else sec_key
    # Keep the format as-is
    return f"# {sec_key}"


def main():
    print("=" * 60)
    print("  BUILDING EXPANDED BANKING README")
    print("=" * 60)

    # Read current README
    full_text = read_current_readme()

    # Build sections 1-8 from existing content + new subflows + extra rows
    section_defs = [
        ("Customer Onboarding & Account Management", "BC032 BC033 BC031"),
        ("Payments & Transfers", "BC060 BC061"),
        ("Lending & Credit Management", "BC070"),
        ("Cards Management", "BC071"),
        ("Deposits & Savings Products", "BC072 BC073"),
        ("Risk & Compliance", "BC012 BC013"),
        ("Channels & Digital Banking", "BC001 BC003 BC002"),
        ("Finance, Treasury & Settlement", "BC010 BC014 BC061 BC062"),
    ]

    # Build each section
    sections_1_to_8 = {}
    sf_order = legacy_subflows()

    for sec_idx, (sec_name, codes) in enumerate(section_defs):
        sec_num = sec_idx + 1
        header = f"# {sec_num}: {sec_name}  - `{'` `'.join(codes.split())}`"

        existing_sfs = [sf for sf in sf_order if sf.startswith(f"{sec_num}.")]

        section_lines = [header, ""]

        for sf_name in existing_sfs:
            sf_text = extract_subflow_text(full_text, sf_name)
            if not sf_text:
                print(f"  WARNING: Could not extract sub-flow: {sf_name}")
                continue

            sf_lines = sf_text.split("\n")
            processed = process_subflow_lines(sf_name, sf_lines)
            section_lines.extend(processed)

            # Separator between sub-flows
            section_lines.append("")
            section_lines.append("---")
            section_lines.append("")

        # Add new sub-flow for this section
        new_sf = get_new_subflow(sec_num)
        if new_sf:
            section_lines.extend(new_sf)
            section_lines.append("")
            section_lines.append("---")
            section_lines.append("")

        sections_1_to_8[sec_num] = "\n".join(section_lines)

    # Build new sections 9-12
    sections_9_12 = []
    for sec_key, sec_data in ED.NEW_SECTIONS.items():
        sec_content = build_new_section(sec_key, sec_data)
        sections_9_12.append("\n".join(sec_content))

    # ── Assemble the full README ──
    result_parts = []

    # Title
    result_parts.append("# Banking Process Flows — BIAN Capability Model Reference")
    result_parts.append("")
    result_parts.append("> Generated on 2026-07-06 | Domain: Banking | Framework: BIAN (Banking Industry Architecture Network)")
    result_parts.append("")
    result_parts.append("")

    # BIAN section
    result_parts.append(generate_bian_section())
    result_parts.append("")

    # TOC
    toc = generate_toc(section_defs, sections_1_to_8, ED.NEW_SECTIONS, {})
    result_parts.append(toc)

    # Test Data
    result_parts.append(generate_test_data())
    result_parts.append("")

    # Domain sections 1-8
    for sec_num in sorted(sections_1_to_8.keys()):
        # Check if last line is a separator
        sec_text = sections_1_to_8[sec_num]
        # Remove trailing separators
        while sec_text.rstrip().endswith("---"):
            sec_text = sec_text.rstrip()[:-3].rstrip()
        result_parts.append(sec_text)
        result_parts.append("")

    # New sections 9-12
    for sec_text in sections_9_12:
        result_parts.append(sec_text)
        result_parts.append("")

    # Final separator
    result_parts.append("---")
    result_parts.append("")

    # Combine
    result = "\n".join(result_parts)

    # Backup original
    import shutil
    if not BAK.exists():
        shutil.copy2(README, BAK)
        print(f"  Backup: {BAK}")

    # Write
    write_readme(result)

    # Stats
    final_lines = result.split("\n")
    h1_count = sum(1 for l in final_lines if l.strip().startswith("# ") and not l.strip().startswith("## "))
    h3_count = sum(1 for l in final_lines if l.strip().startswith("### ") and not l.strip().startswith("#### "))
    int_rows = result.count(INT_TABLE_SEP)
    ac_rows = result.count(AC_TABLE_SEP)

    print()
    print(f"  Sections:     {h1_count} (target: 12)")
    print(f"  Sub-flows:    {h3_count} (target: 40+)")
    print(f"  Int tables:   {int_rows}")
    print(f"  AC tables:    {ac_rows}")
    print(f"  Total lines:  {len(final_lines)}")
    print()
    print("  Done! Verify output and fix any issues.")


if __name__ == "__main__":
    main()
