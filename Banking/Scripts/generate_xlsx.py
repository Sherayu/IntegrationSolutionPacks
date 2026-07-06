from pathlib import Path
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side

ROOT = Path(__file__).resolve().parent.parent
out_path = ROOT / "Catalogue" / "integration-details.xlsx"

sections_data = {
    "1-Customer Onboarding": [
        ("Customer Onboarding", "Customer", "CheckExistingCustomer", "Onboarding Platform (Backbase)", "CRM (Salesforce Financial Services)", "Backbase REST API", "Salesforce REST API (OAuth2)", "API-led (Real-time)", "Simple"),
        ("Customer Onboarding", "Identity", "VerifyDocuments", "Onboarding Platform (Backbase)", "Identity Verification (Onfido)", "Backbase REST API", "Onfido API (API Key)", "API-led (Real-time)", "Medium"),
        ("Customer Onboarding", "Sanctions", "ScreenCustomer", "Onboarding Platform (Backbase)", "Screening (WorldCheck)", "Backbase REST API", "WorldCheck API (SOAP)", "API-led (Real-time)", "Medium"),
        ("Customer Onboarding", "CIF", "CreateCustomerRecord", "CRM (Salesforce Financial Services)", "Core Banking (Temenos Transact)", "Salesforce REST API (OAuth2)", "Temenos REST API (API Key)", "API-led (Real-time)", "Medium"),
        ("Account Opening", "Account", "CreateAccount", "Onboarding Platform (Backbase)", "Core Banking (Temenos Transact)", "Backbase REST API", "Temenos REST API (API Key)", "API-led (Real-time)", "Medium"),
        ("Account Opening", "Card", "OrderDebitCard", "Onboarding Platform (Backbase)", "Card Management (Fiserv)", "Backbase REST API", "Fiserv API (SOAP)", "API-led (Real-time)", "Medium"),
        ("Corporate Account", "Compliance", "ApproveCompliance", "CRM (Salesforce Financial Services)", "Compliance Case Mgmt (Pega)", "Salesforce REST API (OAuth2)", "Pega API (REST)", "API-led (Real-time)", "Medium"),
        ("Corporate Account", "Account", "OpenCorporateAccount", "CRM (Salesforce Financial Services)", "Core Banking (Temenos Transact)", "Salesforce REST API (OAuth2)", "Temenos REST API (API Key)", "API-led (Real-time)", "High"),
    ],
    "2-Payments": [
        ("Domestic Payment", "Payment Instruction", "SubmitPayment", "Digital Banking (Backbase)", "Payment Hub (Volante)", "Backbase REST API", "Volante API (ISO 20022)", "API-led (Real-time)", "Medium"),
        ("Domestic Payment", "Clearing", "SubmitToClearing", "Payment Hub (Volante)", "SEPA Clearing (EBA Clearing)", "Volante API (ISO 20022)", "EBA Clearing API (ISO 20022)", "API-led (Real-time)", "High"),
        ("Domestic Payment", "Ledger", "PostTransaction", "Payment Hub (Volante)", "Core Banking (Temenos Transact)", "Volante REST API", "Temenos REST API (API Key)", "API-led (Real-time)", "Medium"),
        ("Domestic Payment", "Reconciliation", "MatchTransaction", "Payment Hub (Volante)", "Reconciliation Engine (SmartStream)", "Volante REST API", "SmartStream API (REST)", "API-led (Real-time)", "Simple"),
        ("Cross-Border Payment", "SWIFT Message", "SendMT103", "Payment Hub (Volante)", "SWIFT Alliance Gateway", "Volante ISO 20022", "SWIFT Alliance (MT)", "API-led (Real-time)", "High"),
        ("Cross-Border Payment", "Cover Payment", "ProcessCover", "SWIFT Alliance Gateway", "Correspondent Bank (Deutsche Bank)", "SWIFT Alliance (MT)", "SWIFT MT202", "Batch (Scheduled)", "High"),
        ("Real-Time Payment", "FPS Message", "SubmitToFPS", "Payment Hub (Volante)", "Faster Payments Service (FPS)", "Volante API (ISO 20022)", "FPS API (ISO 20022)", "API-led (Real-time)", "High"),
        ("Real-Time Payment", "Ledger", "PostDebit", "Payment Hub (Volante)", "Core Banking (Temenos Transact)", "Volante REST API", "Temenos REST API (API Key)", "API-led (Real-time)", "Medium"),
    ],
    "3-Lending": [
        ("Loan Origination", "Application", "SubmitLoanApp", "Digital Banking (Backbase)", "LOS (nCino)", "Backbase REST API", "nCino REST API (OAuth2)", "API-led (Real-time)", "Medium"),
        ("Loan Origination", "Credit Check", "CreditBureauCheck", "LOS (nCino)", "Credit Bureau (Experian)", "nCino API", "Experian API (SOAP)", "API-led (Real-time)", "High"),
        ("Loan Origination", "Decision", "CalculateAffordability", "LOS (nCino)", "Decision Engine (FICO)", "nCino REST API", "FICO Blaze API (REST)", "API-led (Real-time)", "Medium"),
        ("Loan Origination", "Disbursement", "DisburseLoan", "LOS (nCino)", "Core Banking (Temenos Transact)", "nCino REST API (OAuth2)", "Temenos REST API (API Key)", "API-led (Real-time)", "Medium"),
        ("Mortgage Lending", "Valuation", "OrderValuation", "LOS (nCino)", "Valuation Provider (Hometrack)", "nCino REST API", "Hometrack API (SOAP)", "Event-driven", "Medium"),
        ("Mortgage Lending", "Funds", "ReleaseFunds", "LOS (nCino)", "Core Banking (Temenos Transact)", "nCino REST API (OAuth2)", "Temenos REST API (API Key)", "Event-driven", "High"),
        ("Credit Assessment", "Approval", "ApproveUnderwriting", "LOS (nCino)", "Workflow (Pega)", "nCino REST API (OAuth2)", "Pega Workflow API (REST)", "Event-driven", "Medium"),
        ("Credit Assessment", "Credit Report", "GetCreditReport", "Decision Engine (FICO)", "Credit Bureau (Experian)", "FICO Blaze API", "Experian API (SOAP)", "API-led (Real-time)", "High"),
        ("Credit Assessment", "Bank Statements", "GetTransactionData", "Decision Engine (FICO)", "Open Banking (Token.io)", "FICO API", "Token.io API (OAuth2)", "API-led (Real-time)", "High"),
    ],
    "4-Cards": [
        ("Card Issuance", "Card Request", "CreateCardRequest", "Digital Banking (Backbase)", "Card Management (Fiserv)", "Backbase REST API", "Fiserv API (SOAP)", "API-led (Real-time)", "Medium"),
        ("Card Issuance", "Production", "OrderProduction", "Card Management (Fiserv)", "Card Bureau (CPI)", "Fiserv API (ISO 8583)", "CPI API (SFTP)", "Batch (Scheduled)", "High"),
        ("Card Issuance", "Tokenization", "TokenizeCard", "Digital Wallet (Apple Pay)", "Card Management (Fiserv)", "Apple Pay API", "Fiserv Token API", "API-led (Real-time)", "High"),
        ("Card Transaction", "Authorization", "AuthorizeTransaction", "POS Terminal", "Merchant Acquirer (Worldpay)", "POS Protocol (ISO 8583)", "Worldpay Gateway API", "API-led (Real-time)", "High"),
        ("Card Transaction", "Issuer Auth", "AuthDecision", "Payment Network (Mastercard)", "Card Management (Fiserv)", "Mastercard Interface", "Fiserv API (ISO 8583)", "API-led (Real-time)", "Medium"),
        ("Card Transaction", "Settlement", "SubmitSettlement", "Merchant Acquirer (Worldpay)", "Payment Network (Mastercard)", "Worldpay Settlement API", "Mastercard Settlement (ISO 20022)", "Batch (Scheduled)", "High"),
        ("Card Dispute", "Chargeback", "IssueChargeback", "Dispute System (Fiserv)", "Payment Network (Mastercard)", "Fiserv API", "Mastercard Chargeback API", "API-led (Real-time)", "High"),
        ("Card Dispute", "Reversal", "ReverseFunds", "Dispute System (Fiserv)", "Core Banking (Temenos Transact)", "Fiserv REST API", "Temenos REST API (API Key)", "Event-driven", "Medium"),
    ],
    "5-Deposits": [
        ("Account Operations", "Cash Deposit", "PostCashDeposit", "Branch Teller (Fiserv DNA)", "Core Banking (Temenos Transact)", "Fiserv Teller API", "Temenos REST API (API Key)", "API-led (Real-time)", "Simple"),
        ("Account Operations", "Standing Order", "ExecuteStandingOrder", "Core Banking (Temenos Transact)", "Payment Hub (Volante)", "Temenos REST API", "Volante API (ISO 20022)", "API-led (Real-time)", "Medium"),
        ("Account Operations", "Direct Debit", "ProcessDirectDebit", "Direct Debit Scheme (Bacs)", "Core Banking (Temenos Transact)", "Bacs API (ISO 20022)", "Temenos REST API", "Batch (Scheduled)", "Medium"),
        ("Term Deposit", "Placement", "CreateTermDeposit", "Core Banking (Temenos Transact)", "Core Banking (Temenos Transact)", "Internal", "Internal", "API-led (Real-time)", "Medium"),
        ("Term Deposit", "Maturity", "ProcessMaturity", "Core Banking (Temenos Transact)", "Core Banking (Temenos Transact)", "Internal", "Internal", "Batch (Scheduled)", "Simple"),
        ("Sweep Products", "Sweep", "ExecuteSweep", "Core Banking (Temenos Transact)", "Core Banking (Temenos Transact)", "Internal", "Internal", "Batch (Scheduled)", "Medium"),
        ("Sweep Products", "Investment", "AutoInvestSurplus", "Core Banking (Temenos Transact)", "Treasury System (Murex)", "Temenos REST API", "Murex API (SOAP)", "API-led (Real-time)", "Medium"),
    ],
    "6-Risk-Compliance": [
        ("Fraud Detection", "Transaction", "SendTransactionEvent", "Core Banking (Temenos Transact)", "Fraud Detection (FICO Falcon)", "Temenos REST API", "Falcon API (ISO 8583)", "API-led (Real-time)", "High"),
        ("Fraud Detection", "Alert", "CreateFraudAlert", "Core Banking (Temenos Transact)", "Case Management (Pega)", "Temenos REST API", "Pega REST API (OAuth2)", "Event-driven", "Medium"),
        ("Fraud Detection", "Unblock", "UnblockCard", "Case Management (Pega)", "Core Banking (Temenos Transact)", "Pega REST API (OAuth2)", "Temenos REST API", "API-led (Real-time)", "Simple"),
        ("AML Screening", "Payment", "ScreenPayment", "Core Banking (Temenos Transact)", "AML System (Oracle FCCM)", "Temenos REST API", "Oracle FCCM API (SOAP)", "API-led (Real-time)", "High"),
        ("AML Screening", "Sanctions", "CheckSanctionsLists", "AML System (Oracle FCCM)", "Sanctions Screening (WorldCheck)", "Oracle FCCM API", "WorldCheck API (SOAP)", "API-led (Real-time)", "High"),
        ("AML Screening", "Alert", "CreateAMLAlert", "AML System (Oracle FCCM)", "Case Management (Pega)", "Oracle FCCM API", "Pega REST API (OAuth2)", "Event-driven", "Medium"),
        ("AML Screening", "Release", "ReleasePayment", "Case Management (Pega)", "Core Banking (Temenos Transact)", "Pega REST API (OAuth2)", "Temenos REST API", "API-led (Real-time)", "Simple"),
        ("Regulatory Reporting", "Balance Sheet", "ExtractBalanceSheet", "Core Banking (Temenos Transact)", "Regulatory Reporting (AxiomSL)", "Temenos ODBC", "AxiomSL JDBC", "Batch (ETL)", "Medium"),
        ("Regulatory Reporting", "Lending Data", "ExtractLendingPortfolio", "Lending System (nCino)", "Regulatory Reporting (AxiomSL)", "nCino REST API", "AxiomSL REST API", "Batch (ETL)", "Medium"),
        ("Regulatory Reporting", "Submission", "SubmitToRegulator", "Regulatory Reporting (AxiomSL)", "Regulator Portal (PRA)", "AxiomSL XBRL", "PRA Gateway (SFTP)", "Batch (Scheduled)", "High"),
    ],
    "7-Channels": [
        ("Internet Banking", "Balances", "FetchAccountBalances", "Internet Banking (Backbase)", "Core Banking (Temenos Transact)", "Backbase REST API", "Temenos REST API (API Key)", "API-led (Real-time)", "Medium"),
        ("Internet Banking", "Profile", "GetCustomerProfile", "Internet Banking (Backbase)", "CRM (Salesforce Financial Services)", "Backbase REST API", "Salesforce REST API (OAuth2)", "API-led (Real-time)", "Simple"),
        ("Mobile Banking", "Payment", "AuthorizePayment", "Mobile Banking App (Backbase)", "Core Banking (Temenos Transact)", "Backbase REST API", "Temenos REST API (API Key)", "API-led (Real-time)", "Medium"),
        ("Mobile Banking", "Cheque Deposit", "ProcessChequeImage", "Mobile Banking App (Backbase)", "Cheque Processing", "Backbase REST API", "Cheque API (Image)", "API-led (Real-time)", "Medium"),
        ("Branch Banking", "Transaction", "PostCashDeposit", "Branch Teller (Fiserv DNA)", "Core Banking (Temenos Transact)", "Fiserv Teller API", "Temenos REST API (API Key)", "API-led (Real-time)", "Simple"),
        ("Branch Banking", "Cross-Sell", "GetCrossSellOffer", "Branch Teller (Fiserv DNA)", "CRM (Salesforce Financial Services)", "Fiserv REST API", "Salesforce REST API (OAuth2)", "API-led (Real-time)", "Medium"),
    ],
    "8-Treasury-Settlement": [
        ("Nostro Reconciliation", "Statement", "ReceiveMT950", "SWIFT Alliance (Correspondent)", "Reconciliation Engine (SmartStream)", "SWIFT MT950", "SmartStream API (REST)", "Batch (Scheduled)", "High"),
        ("Nostro Reconciliation", "Transactions", "LoadInternalTxns", "Core Banking (Temenos Transact)", "Reconciliation Engine (SmartStream)", "Temenos ODBC", "SmartStream JDBC", "Batch (ETL)", "Medium"),
        ("Nostro Reconciliation", "Adjustments", "PostAdjustments", "Reconciliation Engine (SmartStream)", "General Ledger (SAP)", "SmartStream REST API", "SAP API (SOAP)", "Event-driven", "Medium"),
        ("Treasury Management", "FX Trade", "ExecuteFXOrder", "Treasury System (Murex)", "FX Matching (FXall)", "Murex API", "FXall API (FIX)", "API-led (Real-time)", "High"),
        ("Treasury Management", "Confirmation", "SendMT300", "Treasury System (Murex)", "SWIFT Alliance", "Murex API (MT300)", "SWIFT Alliance", "API-led (Real-time)", "Medium"),
        ("EOD Settlement", "Net Position", "SubmitNetSettlement", "Payment Hub (Volante)", "RTGS System (TARGET2)", "Volante API (ISO 20022)", "TARGET2 API (ISO 20022)", "Batch (Scheduled)", "High"),
        ("EOD Settlement", "Posting", "PostSettlementEntries", "Payment Hub (Volante)", "Core Banking (Temenos Transact)", "Volante REST API", "Temenos REST API (API Key)", "API-led (Real-time)", "Medium"),
        ("EOD Settlement", "GL", "PostGLJournal", "Payment Hub (Volante)", "General Ledger (SAP)", "Volante REST API", "SAP API (SOAP)", "API-led (Real-time)", "Medium"),
    ],
}

headers = ["Flow Name", "Entity", "Info Flow Name", "Source System", "Target System", "Source Connector", "Target Connector", "Integration Pattern", "Complexity"]

wb = Workbook()
wb.remove(wb.active)

header_font = Font(name="Calibri", bold=True, color="FFFFFF", size=10)
header_fill = PatternFill(start_color="1a3c6e", end_color="1a3c6e", fill_type="solid")
header_align = Alignment(horizontal="center", vertical="center", wrap_text=True)
thin_border = Border(
    left=Side(style="thin"),
    right=Side(style="thin"),
    top=Side(style="thin"),
    bottom=Side(style="thin"),
)

for sheet_name, rows in sections_data.items():
    ws = wb.create_sheet(title=sheet_name[:31])
    for col_idx, header in enumerate(headers, 1):
        cell = ws.cell(row=1, column=col_idx, value=header)
        cell.font = header_font
        cell.fill = header_fill
        cell.alignment = header_align
        cell.border = thin_border

    for row_idx, row_data in enumerate(rows, 2):
        for col_idx, value in enumerate(row_data, 1):
            cell = ws.cell(row=row_idx, column=col_idx, value=value)
            cell.border = thin_border
            cell.alignment = Alignment(wrap_text=True, vertical="top")
            cell.font = Font(name="Calibri", size=9)

    ws.column_dimensions["A"].width = 22
    ws.column_dimensions["B"].width = 16
    ws.column_dimensions["C"].width = 22
    ws.column_dimensions["D"].width = 30
    ws.column_dimensions["E"].width = 30
    ws.column_dimensions["F"].width = 22
    ws.column_dimensions["G"].width = 22
    ws.column_dimensions["H"].width = 22
    ws.column_dimensions["I"].width = 14

    ws.auto_filter.ref = f"A1:I{len(rows)+1}"
    ws.freeze_panes = "A2"

wb.save(str(out_path))
print(f"XLSX written: {out_path}")
print(f"Sheets: {len(sections_data)}, total rows: {sum(len(r) for r in sections_data.values())}")
