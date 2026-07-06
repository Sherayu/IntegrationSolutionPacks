"""Inject Acceptance Criteria tables after each Integration Details table in the README."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
README = ROOT / "README.md"

# Acceptance criteria keyed by sub-flow heading (### X.X Title)
# Each entry is a list of (Flow, Entity, Acceptance Criterion, Expected Outcome)
ACCEPTANCE_CRITERIA = {
    "1.1 New Customer Onboarding & KYC": [
        ("Customer Onboarding", "Customer", "CheckExistingCustomer returns correct match/no-match for given email", "Customer record found or 'no existing record' returned within 2 seconds"),
        ("Customer Onboarding", "Identity", "Identity documents verified against Onfido document and liveness checks", "Passport and liveness pass with >=95% confidence; failure returns clear error"),
        ("Customer Onboarding", "Sanctions", "Customer screened against WorldCheck PEP/sanctions/adverse media lists", "Low risk result with no matches; any match >=90% triggers AML alert"),
        ("Customer Onboarding", "CIF", "Customer CIF record created in Temenos Transact with all mandatory fields", "CustomerID returned and propagated to CRM; non-repudiable audit trail created"),
    ],
    "1.2 Retail Account Opening": [
        ("Account Opening", "Eligibility", "Validate eligibility returns true/false based on customer risk rating and flags", "Eligible customers proceed; ineligible customers see reason with appeal path"),
        ("Account Opening", "Account", "Account created in core banking with correct type, currency, and IBAN generation", "IBAN returned, account status=Active, initial balance reflected in <5 seconds"),
        ("Account Opening", "Card", "Debit card ordered via Fiserv card management system", "CardID returned, card status=Ordered, tracking reference provided"),
        ("Account Opening", "Digital Banking", "Digital banking enrollment created with username linked to customer ID", "Login credentials issued; MFA enrollment triggered within 1 minute"),
    ],
    "1.3 Corporate Account Opening": [
        ("Corporate Account", "Documents", "Company documents stored in M-Files with correct metadata tagging", "Documents retrievable by company ID; version history maintained"),
        ("Corporate Account", "Screening", "Company and UBOs screened against sanctions lists", "Low risk result or escalated compliance case; screening completed in <10 seconds"),
        ("Corporate Account", "Compliance", "Compliance approval obtained via Pega case management workflow", "Case approved/cleared; rejection includes reason and resubmission guidance"),
        ("Corporate Account", "Account", "Corporate account opened with multi-signatory mandate configuration", "Account created with all signatories; mandate rules enforced on transactions"),
    ],
    "2.1 Domestic Payment (SEPA/ACH)": [
        ("Domestic Payment", "Payment Instruction", "ISO 20022 pain.001 message generated and submitted to payment hub", "Payment hub acknowledges with unique reference; invalid messages rejected with reason"),
        ("Domestic Payment", "Clearing", "SEPA credit transfer submitted to EBA Clearing via ISO 20022 pacs.008", "Clearing confirmation received with status=Settled within SEPA timelines"),
        ("Domestic Payment", "Ledger", "Debit and credit entries posted correctly to source and beneficiary accounts", "Source account debited, beneficiary account credited; balance reconciliation matches"),
        ("Domestic Payment", "Reconciliation", "Transaction matched by SmartStream reconciliation engine", "Match status=success; unmatched items flagged with discrepancy details"),
    ],
    "2.2 Cross-Border Payment (SWIFT)": [
        ("Cross-Border Payment", "FX Quote", "FX rate returned for currency pair with valid from/to currencies", "Rate within 0.5% of market mid-rate; expired quotes rejected after 30 seconds"),
        ("Cross-Border Payment", "SWIFT Message", "SWIFT MT103 message formatted and sent via SWIFT Alliance Gateway", "SWIFT ACK received; UETR assigned; format validation errors cause rejection"),
        ("Cross-Border Payment", "Cover Payment", "MT202 cover payment processed correctly by correspondent bank", "Cover funds received by correspondent; nostro account debited correctly"),
        ("Cross-Border Payment", "Status", "SWIFT GPI tracker updated with end-to-end payment status", "Status transitions visible in GPI tracker; final ACCC confirmation received"),
    ],
    "2.3 Real-Time Payment (Faster Payments)": [
        ("Real-Time Payment", "Payment Request", "Real-time payment request received and validated by payment hub", "Request accepted or rejected within 1 second; invalid data returns specific error"),
        ("Real-Time Payment", "FPS Message", "ISO 20022 pacs.008 message submitted to Faster Payments Service", "FPS acknowledges within 2 seconds; settlement confirmation in <15 seconds"),
        ("Real-Time Payment", "Credit", "Beneficiary account credited immediately by beneficiary bank", "Funds available to beneficiary within 10 seconds of initiation; no holds applied"),
        ("Real-Time Payment", "Ledger", "Source account debited correctly with real-time balance update", "Available balance reduced immediately; transaction appears in transaction history"),
    ],
    "3.1 Retail Loan Origination": [
        ("Loan Origination", "Application", "Loan application submitted from digital banking to nCino LOS", "Application ID created; all fields mapped correctly; incomplete applications rejected"),
        ("Loan Origination", "Credit Check", "Experian credit bureau check returns credit report and score", "Credit score returned within 5 seconds; bureau error handled gracefully with retry"),
        ("Loan Origination", "Decision", "FICO affordability calculation returns DTI ratio and max loan recommendation", "DTI <=40% auto-approved; >40% routed to manual underwriting"),
        ("Loan Origination", "Disbursement", "Loan funds disbursed to customer account in Temenos Transact", "Customer account credited within 30 seconds; loan account created with correct terms"),
    ],
    "3.2 Mortgage Lending": [
        ("Mortgage Lending", "DIP", "Decision in Principle calculated based on submitted income and commitment data", "DIP issued with provisional amount and term; declined DIP shows reason"),
        ("Mortgage Lending", "Valuation", "Property valuation ordered from Hometrack with correct property details", "Valuation report returned within 24hrs; automated valuation for LTV <80%"),
        ("Mortgage Lending", "Solicitor", "Solicitor instructed via portal with all required case documents", "Solicitor confirmation received; all title deed requests submitted"),
        ("Mortgage Lending", "Funds", "Mortgage funds released to solicitor on completion", "Funds transferred via CHAPS within 2 hours of completion request; tracking reference provided"),
    ],
    "3.3 Credit Assessment & Scoring": [
        ("Credit Assessment", "Application Data", "Application data sent from nCino to FICO decision engine", "Data accepted by decision engine; missing mandatory fields cause rejection"),
        ("Credit Assessment", "Credit Report", "Experian credit report retrieved with score, history, and default information", "Full credit report returned; bureau downtime handled with cached score or manual fallback"),
        ("Credit Assessment", "Bank Statements", "Transaction data retrieved via Open Banking API with customer consent", "12 months data retrieved; consent refresh handled; data unavailable flagged"),
        ("Credit Assessment", "Approval", "Underwriter approval recorded with conditions (if any)", "Approval recorded in LOS; conditions tracked; approval valid for 90 days"),
    ],
    "4.1 Card Issuance": [
        ("Card Issuance", "Card Request", "Card creation request sent to Fiserv card management with correct customer and account", "Card details generated (PAN, expiry, CVV); card ID returned"),
        ("Card Issuance", "Production", "Production order file sent to CPI bureau for card personalization", "File acknowledged by CPI; physical card dispatched within 3 business days"),
        ("Card Issuance", "Activation", "Card activated by customer via digital banking or IVR", "Card status changes from Issued to Active; activation timestamp logged"),
        ("Card Issuance", "Tokenization", "Card tokenized for Apple Pay/Google Pay with device-bound token", "Token issued; PAN never shared with wallet provider; token domain-restricted"),
    ],
    "4.2 Card Transaction Processing": [
        ("Card Transaction", "Authorization", "POS authorization request sent and response received in <2 seconds", "Auth approval code returned; declined transactions show reason code"),
        ("Card Transaction", "Routing", "Transaction routed to correct issuer via Mastercard network BIN lookup", "Route determined correctly; BIN table updated weekly"),
        ("Card Transaction", "Issuer Auth", "Issuer validates available balance/funds and returns auth decision", "Sufficient funds approve; insufficient funds decline; all decisions logged"),
        ("Card Transaction", "Settlement", "End-of-day settlement file exchanged between acquirer, network, and issuer", "Settlement file reconciled to zero; exceptions <0.1% of volume"),
        ("Card Transaction", "Posting", "Card transaction posted to customer account in core banking", "Transaction appears on statement; available balance updated; posting date = transaction date"),
    ],
    "4.3 Card Dispute Management": [
        ("Card Dispute", "Case", "Dispute case created with all transaction details and reason codes", "Case ID generated; mandatory fields validated; duplicate case detection active"),
        ("Card Dispute", "Retrieval", "Retrieval request sent to acquirer via Mastercard dispute network", "Acquirer acknowledges within 48hrs; evidence due within 10 calendar days"),
        ("Card Dispute", "Chargeback", "Chargeback issued with correct reason code and amount", "Chargeback accepted by network; funds provisionally reversed to cardholder"),
        ("Card Dispute", "Reversal", "Funds reversed to customer account upon chargeback confirmation", "Customer account credited; reversal appears on next statement"),
    ],
    "5.1 Account Operations (Current/Savings)": [
        ("Account Operations", "Cash Deposit", "Cash deposit posted to correct account with accurate amount", "Balance updated immediately; receipt generated with transaction reference"),
        ("Account Operations", "Standing Order", "Standing order executed on due date for correct amount and payee", "Payment sent to payment hub; next run date calculated correctly"),
        ("Account Operations", "Direct Debit", "Direct debit collection processed correctly via Bacs scheme", "Account debited on due date; unsuccessful collections retried per scheme rules"),
    ],
    "5.2 Term Deposits": [
        ("Term Deposit", "Rate Quote", "Current term deposit rate returned from pricing engine", "Rate matches published product rate; rate guaranteed for quote validity period"),
        ("Term Deposit", "Placement", "Term deposit account created with principal debited from current account", "TD account opened with correct rate, term, and maturity date; principal debited"),
        ("Term Deposit", "Maturity", "Principal plus interest credited at maturity; renewal option processed", "Maturity proceeds credited on value date; auto-renewal terms applied if configured"),
    ],
    "5.3 Sweep & Investment Products": [
        ("Sweep Products", "Rule", "Sweep rule saved with correct threshold, source, and target accounts", "Rule activated; sweep runs at next balance check cycle"),
        ("Sweep Products", "Sweep", "Excess funds swept from source to target account per configured threshold", "Funds transferred; both accounts updated; sweep amount = balance - threshold"),
        ("Sweep Products", "Investment", "Swept funds auto-invested in money market fund via Murex treasury system", "Investment confirmed; fund price and units recorded; NAV reported daily"),
    ],
    "6.1 Fraud Detection & Prevention": [
        ("Fraud Detection", "Transaction", "Transaction event sent to FICO Falcon for scoring in real-time", "Score returned in <100ms; high-risk transactions blocked before completion"),
        ("Fraud Detection", "Alert", "Pega case created for transactions exceeding fraud threshold", "Alert created with all context; assigned to investigator queue; SLA 30 minutes for high risk"),
        ("Fraud Detection", "Unblock", "Card unblocked by fraud investigator after customer confirms authenticity", "Card status restored to Active within 60 seconds of investigator action"),
    ],
    "6.2 AML/Sanctions Screening": [
        ("AML Screening", "Payment", "Payment sent to Oracle FCCM for AML screening before processing", "Payment held in pending state; released only after compliance clearance"),
        ("AML Screening", "Sanctions", "Payment checked against UN, OFAC, EU, and HMT sanctions lists", "Clear matches >=90% blocked; false positive process allows compliance override"),
        ("AML Screening", "Alert", "AML alert created in Pega for compliance officer review", "Alert with risk score and match details; SLA for review: 24 hours for medium risk"),
        ("AML Screening", "Release", "Payment released by compliance officer after false positive determination", "Payment processed within 60 seconds of release; audit trail of release decision logged"),
    ],
    "6.3 Regulatory Reporting": [
        ("Regulatory Reporting", "Balance Sheet", "Balance sheet data extracted from Temenos Transact to AxiomSL", "Extract completed for all entities; data validated against GL; discrepancies <0.01%"),
        ("Regulatory Reporting", "Lending Data", "Lending portfolio data (EAD, PD, LGD) extracted from nCino", "All active loans included; risk parameters match source system"),
        ("Regulatory Reporting", "Treasury Data", "Treasury position data extracted from Murex for liquidity reporting", "LCR and NSFR calculated correctly; intraday positions included"),
        ("Regulatory Reporting", "Submission", "COREP/FINREP reports submitted to regulator via XBRL", "Regulator acknowledgment received; submission timestamp logged; retry on failure with backoff"),
    ],
    "7.1 Internet Banking": [
        ("Internet Banking", "Authentication", "User authenticated via MFA (OTP) with correct credentials", "Valid credentials -> access granted; invalid OTP -> locked after 3 attempts"),
        ("Internet Banking", "Balances", "Account balances fetched from Temenos for all customer accounts", "All accounts displayed; balances updated to real-time; masking for inactive accounts"),
        ("Internet Banking", "Profile", "Customer profile and offers retrieved from Salesforce CRM", "Personalized offers displayed; profile data matches CRM source"),
        ("Internet Banking", "Content", "Marketing content fetched from Adobe AEM CMS", "Content rendered correctly; A/B variants served per customer segment"),
    ],
    "7.2 Mobile Banking": [
        ("Mobile Banking", "Authentication", "Biometric authentication (fingerprint/face) matches device-bound credential", "Authentication completes <1 second; biometric mismatch shows PIN fallback"),
        ("Mobile Banking", "Notification", "Push notification sent via Firebase for pending payment approval", "Notification delivered within 5 seconds; tap opens correct approval screen"),
        ("Mobile Banking", "Payment", "Payment authorized and processed via mobile approval flow", "Payment confirmed; transaction appears in history; notification sent"),
        ("Mobile Banking", "Cheque Deposit", "Cheque image processed with MICR read and amount OCR", "MICR and OCR accuracy >99%; cheque accepted with 2-day hold applied"),
    ],
    "7.3 Branch Banking (Teller)": [
        ("Branch Banking", "Queue", "Customer checked in at Qmatic kiosk and assigned to next available teller", "Ticket issued; estimated wait time displayed; teller assignment within <5 minutes"),
        ("Branch Banking", "Transaction", "Cash deposit posted to customer account in real-time via teller system", "Balance updated; receipt generated with transaction reference; teller cash drawer reconciled"),
        ("Branch Banking", "Interaction", "Customer interaction logged in Salesforce CRM with type and amount", "Interaction record created; customer 360 view updated"),
        ("Branch Banking", "Cross-Sell", "CRM returns cross-sell suggestion based on customer profile and transaction", "Offer displayed to teller within 1 second; offer accepted/rejected tracked"),
    ],
    "8.1 Nostro/Vostro Reconciliation": [
        ("Nostro Reconciliation", "Statement", "SWIFT MT950 statement received from correspondent bank and loaded", "Statement parsed correctly; all 125 transactions loaded; unmatched items <5%"),
        ("Nostro Reconciliation", "Transactions", "Internal transactions loaded from Temenos for matching period", "All internal txns loaded; date range matches statement period"),
        ("Nostro Reconciliation", "Adjustments", "Unmatched items manually reviewed and adjustment journals posted to SAP GL", "Adjustment entries posted; GL impact correctly calculated; audit trail maintained"),
        ("Nostro Reconciliation", "Response", "MT940 response sent to correspondent bank with confirmed balance", "Balance confirmed within tolerance; discrepancies escalated to treasury"),
    ],
    "8.2 Treasury & Liquidity Management": [
        ("Treasury Management", "Position", "Cash position data received from Temenos Transact into Murex", "Position updated in real-time; forecast horizon configurable (1-30 days)"),
        ("Treasury Management", "FX Trade", "FX order submitted to FXall and executed at quoted rate", "Trade executed within 10 seconds; rate within 0.1% of quoted; confirmation received"),
        ("Treasury Management", "Confirmation", "SWIFT MT300 confirmation sent and matched with counterparty", "Confirmation matched; unmatched confirmations escalated within 1 hour"),
        ("Treasury Management", "Liquidity", "LCR and NSFR liquidity ratios calculated and posted to SAP GL", "Ratios within regulatory limits; breach alert generated if below threshold"),
    ],
    "8.3 End-of-Day Settlement": [
        ("EOD Settlement", "Net Position", "Multilateral net position calculated and submitted to TARGET2 RTGS", "Net position calculated correctly; submission before cut-off time"),
        ("EOD Settlement", "Posting", "Settlement entries posted to Temenos core banking", "All entries posted; debit/credit match net position; rejected entries investigated"),
        ("EOD Settlement", "GL", "End-of-day GL journal posted in SAP", "GL balanced; suspense accounts zero; variances <0.001%"),
        ("EOD Settlement", "Matching", "Settled transactions matched by SmartStream reconciliation engine", "100% matched; any breaks investigated and resolved before next day opening"),
    ],
}


def process_readme():
    text = README.read_text(encoding="utf-8")
    lines = text.split("\n")

    new_lines = []
    i = 0
    current_sub_flow = None
    skip_line = False

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # Track which sub-flow we're in
        if stripped.startswith("### ") and not stripped.startswith("####"):
            current_sub_flow = stripped.replace("### ", "")

        if stripped == "#### Integration Details":
            # Find where the table ends: look for the next --- separator
            new_lines.append(line)
            i += 1

            # Copy the table header and separator lines
            while i < len(lines) and not lines[i].strip().startswith("---"):
                new_lines.append(lines[i])
                i += 1

            # Now lines[i] should be the --- separator after the Integration Details table
            # Insert Acceptance Criteria before the --- separator
            if current_sub_flow and current_sub_flow in ACCEPTANCE_CRITERIA:
                criteria_rows = ACCEPTANCE_CRITERIA[current_sub_flow]
                new_lines.append("")
                new_lines.append("#### Acceptance Criteria")
                new_lines.append("")
                new_lines.append("| Flow | Entity | Acceptance Criterion | Expected Outcome |")
                new_lines.append("|------|--------|---------------------|------------------|")
                for flow_name, entity, criterion, outcome in criteria_rows:
                    criterion_esc = criterion.replace("|", "\\|")
                    outcome_esc = outcome.replace("|", "\\|")
                    new_lines.append(f"| {flow_name} | {entity} | {criterion_esc} | {outcome_esc} |")
                new_lines.append("")
            else:
                # No criteria defined, still add empty table
                new_lines.append("")
                new_lines.append("#### Acceptance Criteria")
                new_lines.append("")
                new_lines.append("| Flow | Entity | Acceptance Criterion | Expected Outcome |")
                new_lines.append("|------|--------|---------------------|------------------|")
                new_lines.append("")

            # Now append the --- separator
            new_lines.append(lines[i])
        else:
            new_lines.append(line)

        i += 1

    result = "\n".join(new_lines)
    README.write_text(result, encoding="utf-8")

    # Count changes
    ac_count = result.count("#### Acceptance Criteria")
    print(f"Added {ac_count} Acceptance Criteria tables")
    print(f"README.md: {len(lines)} -> {len(new_lines)} lines")

    # Verify all sub-flows have criteria
    missing = []
    for sf in ACCEPTANCE_CRITERIA:
        if sf not in result:
            missing.append(sf)
    if missing:
        print(f"WARNING: missing from README: {missing}")
    else:
        print("All 24 sub-flows matched correctly")


if __name__ == "__main__":
    process_readme()
