"""Fix all pattern discrepancies in README.md: 16 pattern changes + 2 source/conn changes."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
README = ROOT / "README.md"

REPLACEMENTS = [
    # ============================================================
    # Category A (10 edits): Event-driven -> API-led (Real-time)
    # All show sync request-response in diagrams
    # ============================================================
    (
        "| Customer Onboarding | CIF | CreateCustomerRecord | CRM (Salesforce Financial Services) | Core Banking (Temenos Transact) | Salesforce REST API (OAuth2) | Temenos REST API (API Key) | Event-driven | Medium |",
        "| Customer Onboarding | CIF | CreateCustomerRecord | CRM (Salesforce Financial Services) | Core Banking (Temenos Transact) | Salesforce REST API (OAuth2) | Temenos REST API (API Key) | API-led (Real-time) | Medium |",
    ),
    (
        "| Account Opening | Card | OrderDebitCard | Onboarding Platform (Backbase) | Card Management (Fiserv) | Backbase REST API | Fiserv API (SOAP) | Event-driven | Medium |",
        "| Account Opening | Card | OrderDebitCard | Onboarding Platform (Backbase) | Card Management (Fiserv) | Backbase REST API | Fiserv API (SOAP) | API-led (Real-time) | Medium |",
    ),
    (
        "| Corporate Account | Account | OpenCorporateAccount | CRM (Salesforce Financial Services) | Core Banking (Temenos Transact) | Salesforce REST API (OAuth2) | Temenos REST API (API Key) | Event-driven | High |",
        "| Corporate Account | Account | OpenCorporateAccount | CRM (Salesforce Financial Services) | Core Banking (Temenos Transact) | Salesforce REST API (OAuth2) | Temenos REST API (API Key) | API-led (Real-time) | High |",
    ),
    (
        "| Domestic Payment | Ledger | PostTransaction | Payment Hub (Volante) | Core Banking (Temenos Transact) | Volante REST API | Temenos REST API (API Key) | Event-driven | Medium |",
        "| Domestic Payment | Ledger | PostTransaction | Payment Hub (Volante) | Core Banking (Temenos Transact) | Volante REST API | Temenos REST API (API Key) | API-led (Real-time) | Medium |",
    ),
    (
        "| Domestic Payment | Reconciliation | MatchTransaction | Payment Hub (Volante) | Reconciliation Engine (SmartStream) | Volante REST API | SmartStream API (REST) | Event-driven | Simple |",
        "| Domestic Payment | Reconciliation | MatchTransaction | Payment Hub (Volante) | Reconciliation Engine (SmartStream) | Volante REST API | SmartStream API (REST) | API-led (Real-time) | Simple |",
    ),
    (
        "| Real-Time Payment | Ledger | PostDebit | Payment Hub (Volante) | Core Banking (Temenos Transact) | Volante REST API | Temenos REST API (API Key) | Event-driven | Medium |",
        "| Real-Time Payment | Ledger | PostDebit | Payment Hub (Volante) | Core Banking (Temenos Transact) | Volante REST API | Temenos REST API (API Key) | API-led (Real-time) | Medium |",
    ),
    (
        "| Loan Origination | Disbursement | DisburseLoan | LOS (nCino) | Core Banking (Temenos Transact) | nCino REST API (OAuth2) | Temenos REST API (API Key) | Event-driven | Medium |",
        "| Loan Origination | Disbursement | DisburseLoan | LOS (nCino) | Core Banking (Temenos Transact) | nCino REST API (OAuth2) | Temenos REST API (API Key) | API-led (Real-time) | Medium |",
    ),
    (
        "| Card Transaction | Posting | PostCardTransaction | Card Management (Fiserv) | Core Banking (Temenos Transact) | Fiserv REST API | Temenos REST API (API Key) | Event-driven | Medium |",
        "| Card Transaction | Posting | PostCardTransaction | Card Management (Fiserv) | Core Banking (Temenos Transact) | Fiserv REST API | Temenos REST API (API Key) | API-led (Real-time) | Medium |",
    ),
    (
        "| Sweep Products | Investment | AutoInvestSurplus | Core Banking (Temenos Transact) | Treasury System (Murex) | Temenos REST API | Murex API (SOAP) | Event-driven | Medium |",
        "| Sweep Products | Investment | AutoInvestSurplus | Core Banking (Temenos Transact) | Treasury System (Murex) | Temenos REST API | Murex API (SOAP) | API-led (Real-time) | Medium |",
    ),
    (
        "| EOD Settlement | Posting | PostSettlementEntries | Payment Hub (Volante) | Core Banking (Temenos Transact) | Volante REST API | Temenos REST API (API Key) | Event-driven | Medium |",
        "| EOD Settlement | Posting | PostSettlementEntries | Payment Hub (Volante) | Core Banking (Temenos Transact) | Volante REST API | Temenos REST API (API Key) | API-led (Real-time) | Medium |",
    ),
    # ============================================================
    # Category B (3 edits): API-led (Real-time) -> Event-driven
    # Non-real-time business processes
    # ============================================================
    (
        "| Mortgage Lending | Valuation | OrderValuation | LOS (nCino) | Valuation Provider (Hometrack) | nCino REST API | Hometrack API (SOAP) | API-led (Real-time) | Medium |",
        "| Mortgage Lending | Valuation | OrderValuation | LOS (nCino) | Valuation Provider (Hometrack) | nCino REST API | Hometrack API (SOAP) | Event-driven | Medium |",
    ),
    (
        "| Mortgage Lending | Funds | ReleaseFunds | LOS (nCino) | Core Banking (Temenos Transact) | nCino REST API (OAuth2) | Temenos REST API (API Key) | API-led (Real-time) | High |",
        "| Mortgage Lending | Funds | ReleaseFunds | LOS (nCino) | Core Banking (Temenos Transact) | nCino REST API (OAuth2) | Temenos REST API (API Key) | Event-driven | High |",
    ),
    # ApproveUnderwriting: human workflow, change pattern + target + connector
    (
        "| Credit Assessment | Approval | ApproveUnderwriting | LOS (nCino) | Underwriter | nCino API | Workflow | API-led (Real-time) | Medium |",
        "| Credit Assessment | Approval | ApproveUnderwriting | LOS (nCino) | Workflow (Pega) | nCino REST API (OAuth2) | Pega Workflow API (REST) | Event-driven | Medium |",
    ),
    # ============================================================
    # Category C (2 edits): Batch (Scheduled) -> API-led (Real-time)
    # Diagrams show synchronous request-response, not batch
    # ============================================================
    (
        "| Account Operations | Standing Order | ExecuteStandingOrder | Core Banking (Temenos Transact) | Payment Hub (Volante) | Temenos REST API | Volante API (ISO 20022) | Batch (Scheduled) | Medium |",
        "| Account Operations | Standing Order | ExecuteStandingOrder | Core Banking (Temenos Transact) | Payment Hub (Volante) | Temenos REST API | Volante API (ISO 20022) | API-led (Real-time) | Medium |",
    ),
    (
        "| EOD Settlement | GL | PostGLJournal | Payment Hub (Volante) | General Ledger (SAP) | Volante REST API | SAP API (SOAP) | Batch (Scheduled) | Medium |",
        "| EOD Settlement | GL | PostGLJournal | Payment Hub (Volante) | General Ledger (SAP) | Volante REST API | SAP API (SOAP) | API-led (Real-time) | Medium |",
    ),
    # ============================================================
    # Category D (1 edit): Event-driven -> API-led (Real-time)
    # Fraud scoring must be sync (<100ms) to block before completion
    # ============================================================
    (
        "| Fraud Detection | Transaction | SendTransactionEvent | Core Banking (Temenos Transact) | Fraud Detection (FICO Falcon) | Temenos REST API | Falcon API (ISO 8583) | Event-driven | High |",
        "| Fraud Detection | Transaction | SendTransactionEvent | Core Banking (Temenos Transact) | Fraud Detection (FICO Falcon) | Temenos REST API | Falcon API (ISO 8583) | API-led (Real-time) | High |",
    ),
    # ============================================================
    # Source/Connector changes (2 edits)
    # Replace human actors with actual system names
    # ============================================================
    (
        "| Fraud Detection | Unblock | UnblockCard | Fraud Investigator | Core Banking (Temenos Transact) | Pega UI | Temenos REST API | API-led (Real-time) | Simple |",
        "| Fraud Detection | Unblock | UnblockCard | Case Management (Pega) | Core Banking (Temenos Transact) | Pega REST API (OAuth2) | Temenos REST API | API-led (Real-time) | Simple |",
    ),
    (
        "| AML Screening | Release | ReleasePayment | Compliance Officer | Core Banking (Temenos Transact) | Pega UI | Temenos REST API | API-led (Real-time) | Simple |",
        "| AML Screening | Release | ReleasePayment | Case Management (Pega) | Core Banking (Temenos Transact) | Pega REST API (OAuth2) | Temenos REST API | API-led (Real-time) | Simple |",
    ),
]


def main():
    text = README.read_text(encoding="utf-8")
    applied = 0
    not_found = []

    for old, new in REPLACEMENTS:
        if old in text:
            text = text.replace(old, new, 1)
            applied += 1
        else:
            not_found.append(old[:80])

    README.write_text(text, encoding="utf-8")
    print(f"Applied {applied}/{len(REPLACEMENTS)} replacements")
    if not_found:
        print(f"NOT FOUND ({len(not_found)}):")
        for nf in not_found:
            print(f"  - {nf}...")


if __name__ == "__main__":
    main()
