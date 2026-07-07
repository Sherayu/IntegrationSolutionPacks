"""Expansion script for Banking domain README.md - defines complete data structures.

This script is a PLANNED expansion definition. It does NOT execute changes.
Run: python Scripts/expand_readme.py
It will print a summary of what would be added without modifying the README.

Target: 12 sections, 40+ sub-flows, 180+ integration rows, 30+ test entities.
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
README = ROOT / "README.md"

# ─── NEW TEST DATA ENTITIES (adds to existing 13) ────────────────────────────────

NEW_TEST_DATA = {
    "LoanProduct": [
        ("loan_product_id", "LP-HOL-001"),
        ("name", "Homeowner Loan"),
        ("min_amount", "5,000.00"),
        ("max_amount", "100,000.00"),
        ("interest_rate", "6.9% APR"),
        ("term_min_months", "12"),
        ("term_max_months", "120"),
    ],
    "Merchant": [
        ("merchant_id", "MER-2026-042"),
        ("name", "Harrods London"),
        ("mcc_code", "5311"),
        ("acquirer", "Worldpay"),
    ],
    "Branch": [
        ("branch_id", "BR-001-LDN"),
        ("name", "London City Branch"),
        ("sort_code", "60-13-31"),
        ("region", "London"),
    ],
    "Employee": [
        ("employee_id", "EMP-2026-011"),
        ("name", "Sarah Williams"),
        ("role", "Relationship Manager"),
        ("branch_id", "BR-001-LDN"),
    ],
    "FXRate": [
        ("pair", "GBP/EUR"),
        ("rate", "1.1500"),
        ("bid", "1.1498"),
        ("ask", "1.1502"),
        ("timestamp", "2026-07-06T09:00:00Z"),
    ],
    "InterestRate": [
        ("rate_id", "IRT-2026-001"),
        ("product", "Savings Account"),
        ("rate", "2.75% p.a."),
        ("effective_date", "2026-07-01"),
    ],
    "ValuationReport": [
        ("report_id", "VAL-2026-042"),
        ("property", "123 Main Street, London"),
        ("market_value", "355,000.00"),
        ("valuation_date", "2026-07-04"),
        ("provider", "Hometrack"),
    ],
    "Collateral": [
        ("collateral_id", "COL-2026-001"),
        ("type", "Residential Property"),
        ("value", "355,000.00"),
        ("lien_position", "First"),
        ("loan_id", "LN-2026-042"),
    ],
    "Trade": [
        ("trade_id", "TRD-2026-088"),
        ("type", "FX Spot"),
        ("currency_pair", "GBP/USD"),
        ("amount", "5,000,000.00"),
        ("rate", "1.1500"),
        ("value_date", "2026-07-08"),
        ("counterparty", "Deutsche Bank"),
    ],
    "Portfolio": [
        ("portfolio_id", "PF-2026-001"),
        ("name", "Growth Balanced Fund"),
        ("risk_profile", "Moderate"),
        ("total_value", "1,250,000.00"),
        ("currency", "GBP"),
    ],
    "Security": [
        ("security_id", "SEC-2026-001"),
        ("isin", "GB000BH4RFK5"),
        ("name", "UK Government Bond 2.5% 2030"),
        ("asset_class", "Fixed Income"),
        ("market_price", "98.50"),
        ("currency", "GBP"),
    ],
    "InvestmentFund": [
        ("fund_id", "FND-2026-001"),
        ("name", "BlackRock Global Equity Fund"),
        ("nav", "245.80"),
        ("currency", "GBP"),
        ("fund_type", "OEIC"),
    ],
    "CollectionCase": [
        ("case_id", "COL-2026-077"),
        ("customer_id", "CUST-2026-002"),
        ("debt_amount", "3,450.00"),
        ("days_past_due", "45"),
        ("status", "Active"),
        ("collector", "EMP-2026-015"),
    ],
    "RestructuringPlan": [
        ("plan_id", "RSP-2026-001"),
        ("customer_id", "CUST-2026-003"),
        ("original_amount", "25,000.00"),
        ("revised_term", "96"),
        ("revised_rate", "4.5%"),
        ("status", "Approved"),
    ],
    "ServiceRequest": [
        ("sr_id", "SR-2026-042"),
        ("customer_id", "CUST-2026-001"),
        ("type", "Statement Request"),
        ("channel", "Email"),
        ("status", "Open"),
        ("priority", "Medium"),
    ],
    "LetterOfCredit": [
        ("lc_id", "LC-2026-001"),
        ("applicant", "Acme Corp Ltd"),
        ("beneficiary", "Global Exports GmbH"),
        ("amount", "500,000.00"),
        ("currency", "USD"),
        ("type", "Irrevocable Sight LC"),
        ("expiry", "2026-12-31"),
        ("status", "Issued"),
    ],
    "Guarantee": [
        ("guarantee_id", "GUA-2026-001"),
        ("type", "Bid Bond"),
        ("applicant", "Acme Corp Ltd"),
        ("beneficiary", "Govt Procurement"),
        ("amount", "50,000.00"),
        ("expiry", "2026-10-15"),
    ],
    "BeneficiaryBank": [
        ("bank_id", "BB-2026-001"),
        ("name", "Deutsche Bank AG"),
        ("swift", "DEUTDEFF"),
        ("country", "Germany"),
    ],
    "Invoice": [
        ("invoice_id", "INV-2026-001"),
        ("issuer", "Global Exports GmbH"),
        ("amount", "150,000.00"),
        ("currency", "EUR"),
        ("due_date", "2026-09-30"),
        ("status", "Unpaid"),
    ],
    "PaymentSchedule": [
        ("schedule_id", "SCH-2026-001"),
        ("loan_id", "LN-2026-042"),
        ("installment", "1 of 60"),
        ("due_date", "2026-08-01"),
        ("amount", "493.75"),
        ("status", "Pending"),
    ],
    "OverdraftLimit": [
        ("limit_id", "ODL-2026-001"),
        ("account_id", "ACCT-4001-2026"),
        ("limit_amount", "2,000.00"),
        ("used_amount", "500.00"),
        ("interest_rate", "19.9% APR"),
    ],
    "SweepRule": [
        ("rule_id", "SWP-2026-001"),
        ("source_account", "ACCT-4001-2026"),
        ("target_account", "SAV-2026-001"),
        ("threshold", "500.00"),
        ("frequency", "Daily"),
    ],
    "RiskModel": [
        ("model_id", "RM-2026-001"),
        ("name", "Credit Risk PD Model v3"),
        ("type", "Probability of Default"),
        ("version", "3.2"),
        ("last_calibrated", "2026-06-01"),
    ],
    "ComplianceAlert": [
        ("alert_id", "ALT-2026-042"),
        ("case_id", "AML-2026-088"),
        ("rule", "STR-001"),
        ("severity", "Medium"),
        ("status", "Investigating"),
    ],
    "AuditTrail": [
        ("audit_id", "AUD-2026-001"),
        ("action", "Payment Released"),
        ("performed_by", "CO-2026-001"),
        ("timestamp", "2026-07-06T11:45:00Z"),
        ("ip_address", "10.0.1.50"),
    ],
    "Campaign": [
        ("campaign_id", "CMP-2026-001"),
        ("name", "Summer Loan Promotion"),
        ("channel", "Email"),
        ("target_segment", "Existing Customers"),
        ("status", "Active"),
    ],
    "Offer": [
        ("offer_id", "OFF-2026-001"),
        ("customer_id", "CUST-2026-001"),
        ("product", "Personal Loan"),
        ("amount", "30,000.00"),
        ("rate", "5.9% APR"),
        ("expiry", "2026-08-06"),
    ],
    "Channel": [
        ("channel_id", "CH-2026-001"),
        ("name", "Internet Banking"),
        ("type", "Digital"),
        ("is_active", "True"),
    ],
    "Session": [
        ("session_id", "SES-2026-001"),
        ("customer_id", "CUST-2026-001"),
        ("channel", "Mobile App"),
        ("start_time", "2026-07-06T10:00:00Z"),
        ("ip_address", "192.168.1.100"),
    ],
    "Consent": [
        ("consent_id", "CON-2026-001"),
        ("customer_id", "CUST-2026-001"),
        ("type", "Open Banking Data Share"),
        ("granted_date", "2026-07-01"),
        ("expiry_date", "2027-07-01"),
    ],
    "PaymentInitiation": [
        ("pi_id", "PI-2026-001"),
        ("customer_id", "CUST-2026-001"),
        ("amount", "1,250.00"),
        ("currency", "GBP"),
        ("status", "Initiated"),
    ],
}

# ─── ADDITIONAL INTEGRATION ROWS FOR EXISTING SUB-FLOWS ──────────────────────────
# Each entry: (Flow, Entity, InfoFlow, Source, Target, SourceConn, TargetConn, Pattern, Complexity)

EXTRA_INTEGRATIONS = {
    "1.1 New Customer Onboarding & KYC": [
        ("Customer Onboarding", "Customer", "SendWelcomeEmail", "CRM (Salesforce Financial Services)", "Email Service (SendGrid)", "Salesforce REST API (OAuth2)", "SendGrid SMTP API", "Event-driven", "Simple"),
        ("Customer Onboarding", "Consent", "CaptureRegulatoryConsent", "Onboarding Platform (Backbase)", "Consent Repository (SealSign)", "Backbase REST API", "SealSign API (REST)", "API-led (Real-time)", "Medium"),
    ],
    "1.2 Retail Account Opening": [
        ("Account Opening", "Mandate", "SetupStandingOrderMandate", "Onboarding Platform (Backbase)", "Payment Hub (Volante)", "Backbase REST API", "Volante API (ISO 20022)", "Event-driven", "Medium"),
        ("Account Opening", "Terms", "CaptureSignedTerms", "Onboarding Platform (Backbase)", "Document Mgmt (M-Files)", "Backbase REST API", "M-Files REST API (API Key)", "API-led (Real-time)", "Simple"),
    ],
    "1.3 Corporate Account Opening": [
        ("Corporate Account", "Signatory", "VerifySignatoryIdentity", "CRM (Salesforce Financial Services)", "Identity Verification (Onfido)", "Salesforce REST API (OAuth2)", "Onfido API (API Key)", "API-led (Real-time)", "Medium"),
        ("Corporate Account", "Fee", "SetupAccountFeeSchedule", "CRM (Salesforce Financial Services)", "Core Banking (Temenos Transact)", "Salesforce REST API (OAuth2)", "Temenos REST API (API Key)", "API-led (Real-time)", "Simple"),
    ],
    "2.1 Domestic Payment (SEPA/ACH)": [
        ("Domestic Payment", "Notification", "SendPaymentConfirmation", "Payment Hub (Volante)", "Notification Service (Firebase)", "Volante REST API", "Firebase FCM API", "Event-driven", "Simple"),
        ("Domestic Payment", "FX", "ApplyFXConversion", "Payment Hub (Volante)", "Core Banking (Temenos Transact)", "Volante REST API", "Temenos REST API (API Key)", "API-led (Real-time)", "Medium"),
    ],
    "2.2 Cross-Border Payment (SWIFT)": [
        ("Cross-Border Payment", "Compliance", "ScreenCrossBorderPayment", "Payment Hub (Volante)", "AML System (Oracle FCCM)", "Volante REST API", "Oracle FCCM API (SOAP)", "API-led (Real-time)", "High"),
        ("Cross-Border Payment", "Fee", "DeductTransactionFee", "Payment Hub (Volante)", "Core Banking (Temenos Transact)", "Volante REST API", "Temenos REST API (API Key)", "API-led (Real-time)", "Simple"),
    ],
    "2.3 Real-Time Payment (Faster Payments)": [
        ("Real-Time Payment", "Fraud", "RealTimeFraudCheck", "Payment Hub (Volante)", "Fraud Detection (FICO Falcon)", "Volante REST API", "Falcon API (ISO 8583)", "API-led (Real-time)", "High"),
        ("Real-Time Payment", "Confirmation", "SendInstantConfirmation", "Payment Hub (Volante)", "Digital Banking (Backbase)", "Volante REST API", "Backbase REST API (JWT)", "Event-driven", "Simple"),
    ],
    "3.1 Retail Loan Origination": [
        ("Loan Origination", "Document", "UploadLoanDocuments", "LOS (nCino)", "Document Mgmt (M-Files)", "nCino REST API", "M-Files REST API (API Key)", "API-led (Real-time)", "Simple"),
        ("Loan Origination", "Pricing", "GetRiskBasedPricing", "LOS (nCino)", "Pricing Engine", "nCino REST API", "Pricing API (REST)", "API-led (Real-time)", "Medium"),
    ],
    "3.2 Mortgage Lending": [
        ("Mortgage Lending", "Insurance", "RequestInsuranceQuote", "LOS (nCino)", "Insurance Provider (Aviva)", "nCino REST API", "Aviva API (SOAP)", "Event-driven", "Medium"),
        ("Mortgage Lending", "Title", "VerifyTitleDeeds", "Solicitor Portal", "Land Registry (UK LR)", "Solicitor API (REST)", "Land Registry API (SOAP)", "API-led (Real-time)", "High"),
    ],
    "3.3 Credit Assessment & Scoring": [
        ("Credit Assessment", "Fraud", "IdentityFraudCheck", "Decision Engine (FICO)", "Fraud Detection (FICO Falcon)", "FICO Blaze API", "Falcon API (ISO 8583)", "API-led (Real-time)", "Medium"),
        ("Credit Assessment", "Decision", "GenerateOfferLetter", "LOS (nCino)", "Document Generation (Adobe Sign)", "nCino REST API", "Adobe Sign API (REST)", "Event-driven", "Simple"),
    ],
    "4.1 Card Issuance": [
        ("Card Issuance", "PIN", "SendPINMailer", "Card Management (Fiserv)", "Card Bureau (CPI)", "Fiserv API (ISO 8583)", "CPI API (SFTP)", "Batch (Scheduled)", "Medium"),
        ("Card Issuance", "Notification", "NotifyCardDispatched", "Card Management (Fiserv)", "Notification Service (Firebase)", "Fiserv REST API", "Firebase FCM API", "Event-driven", "Simple"),
    ],
    "4.2 Card Transaction Processing": [
        ("Card Transaction", "FX", "ConvertTransactionCurrency", "Card Management (Fiserv)", "FX Rate Service (Reuters)", "Fiserv REST API", "Reuters API (REST)", "API-led (Real-time)", "Medium"),
        ("Card Transaction", "Reward", "CalculateRewardPoints", "Card Management (Fiserv)", "Rewards Engine (LoyaltyPlus)", "Fiserv REST API", "LoyaltyPlus API (REST)", "Event-driven", "Medium"),
    ],
    "4.3 Card Dispute Management": [
        ("Card Dispute", "Evidence", "UploadDisputeEvidence", "Digital Banking (Backbase)", "Dispute System (Fiserv)", "Backbase REST API", "Fiserv Dispute API (SOAP)", "API-led (Real-time)", "Simple"),
        ("Card Dispute", "Notification", "NotifyDisputeOutcome", "Dispute System (Fiserv)", "Notification Service (Firebase)", "Fiserv REST API", "Firebase FCM API", "Event-driven", "Simple"),
    ],
    "5.1 Account Operations (Current/Savings)": [
        ("Account Operations", "Fee", "ApplyMonthlyFee", "Core Banking (Temenos Transact)", "Core Banking (Temenos Transact)", "Internal", "Internal", "Batch (Scheduled)", "Simple"),
        ("Account Operations", "Statement", "GenerateMonthlyStatement", "Core Banking (Temenos Transact)", "Document Generation (Adobe Sign)", "Temenos REST API", "Adobe Sign API (REST)", "Batch (Scheduled)", "Medium"),
    ],
    "5.2 Term Deposits": [
        ("Term Deposit", "Break", "ProcessEarlyBreakFee", "Core Banking (Temenos Transact)", "Core Banking (Temenos Transact)", "Internal", "Internal", "API-led (Real-time)", "Simple"),
        ("Term Deposit", "Renewal", "ProcessAutoRenewal", "Core Banking (Temenos Transact)", "Notification Service (Firebase)", "Temenos REST API", "Firebase FCM API", "Batch (Scheduled)", "Simple"),
    ],
    "5.3 Sweep & Investment Products": [
        ("Sweep Products", "Reporting", "GenerateSweepReport", "Core Banking (Temenos Transact)", "Treasury System (Murex)", "Temenos REST API", "Murex API (SOAP)", "Batch (Scheduled)", "Simple"),
        ("Sweep Products", "Tax", "CalculateTaxOnInterest", "Core Banking (Temenos Transact)", "Tax Engine (Vertex)", "Temenos REST API", "Vertex API (SOAP)", "Event-driven", "Medium"),
    ],
    "6.1 Fraud Detection & Prevention": [
        ("Fraud Detection", "Rule", "UpdateFraudRuleSet", "Fraud Detection (FICO Falcon)", "Fraud Detection (FICO Falcon)", "Internal", "Internal", "Batch (Scheduled)", "Medium"),
        ("Fraud Detection", "Report", "GenerateFraudDashboard", "Case Management (Pega)", "BI Platform (Tableau)", "Pega REST API (OAuth2)", "Tableau REST API", "Batch (Scheduled)", "Simple"),
    ],
    "6.2 AML/Sanctions Screening": [
        ("AML Screening", "List", "UpdateSanctionsLists", "Sanctions Screening (WorldCheck)", "AML System (Oracle FCCM)", "WorldCheck API (SOAP)", "Oracle FCCM API (SOAP)", "Batch (Scheduled)", "Medium"),
        ("AML Screening", "SAR", "SubmitSuspiciousActivityReport", "Case Management (Pega)", "Regulator Portal (NCA)", "Pega REST API (OAuth2)", "NCA Gateway (SFTP)", "Batch (Scheduled)", "High"),
    ],
    "6.3 Regulatory Reporting": [
        ("Regulatory Reporting", "Validation", "ValidateReportData", "Regulatory Reporting (AxiomSL)", "Data Quality Tool (Informatica)", "AxiomSL REST API", "Informatica API (REST)", "Batch (ETL)", "Medium"),
        ("Regulatory Reporting", "SignOff", "DigitalSignReport", "Regulatory Reporting (AxiomSL)", "Digital Signature (DocuSign)", "AxiomSL REST API", "DocuSign API (REST)", "API-led (Real-time)", "Simple"),
    ],
    "7.1 Internet Banking": [
        ("Internet Banking", "Analytics", "TrackUserBehavior", "Internet Banking (Backbase)", "Analytics (Google Analytics)", "Backbase REST API", "GA4 API (REST)", "Event-driven", "Simple"),
        ("Internet Banking", "Search", "IndexSearchResults", "Internet Banking (Backbase)", "Search Engine (Elasticsearch)", "Backbase REST API", "Elasticsearch REST API", "Event-driven", "Medium"),
    ],
    "7.2 Mobile Banking": [
        ("Mobile Banking", "Location", "GetNearbyBranches", "Mobile Banking App (Backbase)", "Location Service (Google Maps)", "Backbase Mobile SDK", "Google Maps API (REST)", "API-led (Real-time)", "Simple"),
        ("Mobile Banking", "Feedback", "SubmitAppFeedback", "Mobile Banking App (Backbase)", "CRM (Salesforce Financial Services)", "Backbase REST API", "Salesforce REST API (OAuth2)", "API-led (Real-time)", "Simple"),
    ],
    "7.3 Branch Banking (Teller)": [
        ("Branch Banking", "Appointment", "BookAppointment", "Queue Management (Qmatic)", "CRM (Salesforce Financial Services)", "Qmatic API", "Salesforce REST API (OAuth2)", "Event-driven", "Simple"),
        ("Branch Banking", "Cash", "ReconcileTellerCash", "Branch Teller (Fiserv DNA)", "Core Banking (Temenos Transact)", "Fiserv Teller API", "Temenos REST API (API Key)", "Batch (Scheduled)", "Medium"),
    ],
    "8.1 Nostro/Vostro Reconciliation": [
        ("Nostro Reconciliation", "Reporting", "GenerateAgedBreakReport", "Reconciliation Engine (SmartStream)", "General Ledger (SAP)", "SmartStream REST API", "SAP API (SOAP)", "Batch (Scheduled)", "Medium"),
        ("Nostro Reconciliation", "Alert", "SendBreakAlert", "Reconciliation Engine (SmartStream)", "Notification Service (Firebase)", "SmartStream REST API", "Firebase FCM API", "Event-driven", "Simple"),
    ],
    "8.2 Treasury & Liquidity Management": [
        ("Treasury Management", "Forecast", "GenerateLiquidityForecast", "Treasury System (Murex)", "Core Banking (Temenos Transact)", "Murex API (REST)", "Temenos REST API (API Key)", "API-led (Real-time)", "Medium"),
        ("Treasury Management", "Hedge", "ExecuteFXHedge", "Treasury System (Murex)", "FX Matching (FXall)", "Murex API", "FXall API (FIX)", "API-led (Real-time)", "High"),
    ],
    "8.3 End-of-Day Settlement": [
        ("EOD Settlement", "Reporting", "GenerateSettlementReport", "Payment Hub (Volante)", "Regulatory Reporting (AxiomSL)", "Volante REST API", "AxiomSL REST API", "Batch (Scheduled)", "Medium"),
        ("EOD Settlement", "Audit", "LogSettlementAudit", "Payment Hub (Volante)", "Audit System (LogRhythm)", "Volante REST API", "LogRhythm API (SIEM)", "Event-driven", "Simple"),
    ],
}

# ─── ADDITIONAL ACCEPTANCE CRITERIA FOR EXISTING SUB-FLOWS ───────────────────────

EXTRA_ACCEPTANCE = {
    "1.1 New Customer Onboarding & KYC": [
        ("Customer Onboarding", "Customer", "Welcome email sent to new customer post-registration", "Email delivered within 60 seconds; tracking pixel confirms open"),
        ("Customer Onboarding", "Consent", "Regulatory consent captured and stored for GDPR/FCA compliance", "Consent record created with timestamp; audit trail of consent captured"),
    ],
    "1.2 Retail Account Opening": [
        ("Account Opening", "Mandate", "Standing order mandate setup triggered for new account", "Mandate reference created; first payment scheduled correctly"),
        ("Account Opening", "Terms", "Signed terms and conditions stored in document management", "Document retrievable; signature verification completes; terms version tracked"),
    ],
    "1.3 Corporate Account Opening": [
        ("Corporate Account", "Signatory", "All signatories' identities verified through Onfido", "Each signatory verified with >=95% confidence; failed verification blocks account"),
        ("Corporate Account", "Fee", "Account fee schedule configured correctly in core banking", "Fee schedule applied; monthly fees calculated correctly from start date"),
    ],
    "2.1 Domestic Payment (SEPA/ACH)": [
        ("Domestic Payment", "Notification", "Payment confirmation notification sent to customer", "Push/email notification delivered within 30 seconds; reference included"),
        ("Domestic Payment", "FX", "FX conversion applied correctly for payments in non-base currency", "Rate from FX feed applied; conversion amount verified; rounding rules followed"),
    ],
    "2.2 Cross-Border Payment (SWIFT)": [
        ("Cross-Border Payment", "Compliance", "Cross-border payment screened for AML before SWIFT submission", "Payment held until compliance clearance; held payments flagged to operations"),
        ("Cross-Border Payment", "Fee", "Transaction fees deducted correctly and transparently", "Fee amount disclosed before confirmation; fees posted to income GL"),
    ],
    "2.3 Real-Time Payment (Faster Payments)": [
        ("Real-Time Payment", "Fraud", "Real-time fraud check completed before FPS submission", "Fraud check response in <200ms; high-risk scores block payment before transmission"),
        ("Real-Time Payment", "Confirmation", "Instant confirmation sent to customer after FPS settlement", "Confirmation visible in digital banking within 5 seconds of settlement"),
    ],
    "3.1 Retail Loan Origination": [
        ("Loan Origination", "Document", "Loan application documents uploaded and stored in M-Files", "All documents linked to application ID; automated document classification applied"),
        ("Loan Origination", "Pricing", "Risk-based pricing returned from pricing engine", "Rate within defined band for risk score; manual override requires approval"),
    ],
    "3.2 Mortgage Lending": [
        ("Mortgage Lending", "Insurance", "Buildings insurance quote requested and received", "Quote returned within 30 seconds; multiple quotes compared; waiver available for self-sourced"),
        ("Mortgage Lending", "Title", "Title deeds verified with Land Registry", "Title registered; charges confirmed; any existing mortgages noted"),
    ],
    "3.3 Credit Assessment & Scoring": [
        ("Credit Assessment", "Fraud", "Identity fraud check completed as part of credit assessment", "Fraud check integrated into composite score; high fraud flags trigger manual review"),
        ("Credit Assessment", "Decision", "Offer letter generated and digitally signed", "Offer letter generated with correct terms; digital signature applied; valid for 90 days"),
    ],
    "4.1 Card Issuance": [
        ("Card Issuance", "PIN", "PIN mailer dispatched separately from card", "PIN generated securely; mailer dispatched within 24 hours; PIN never in same envelope as card"),
        ("Card Issuance", "Notification", "Customer notified when card is dispatched", "Notification sent with tracking reference; estimated delivery date provided"),
    ],
    "4.2 Card Transaction Processing": [
        ("Card Transaction", "FX", "Dynamic currency conversion applied for foreign transactions", "Exchange rate displayed at POS; conversion rate within 1% of wholesale rate"),
        ("Card Transaction", "Reward", "Reward points calculated and credited for qualifying transactions", "Points calculated per card programme rules; points balance updated immediately"),
    ],
    "4.3 Card Dispute Management": [
        ("Card Dispute", "Evidence", "Customer can upload evidence directly via digital banking", "Evidence attached to dispute case; max file size 10MB; accepted formats PDF/JPEG/PNG"),
        ("Card Dispute", "Notification", "Customer notified of dispute outcome at each lifecycle stage", "Notification sent on case creation, chargeback issuance, and final resolution"),
    ],
    "5.1 Account Operations (Current/Savings)": [
        ("Account Operations", "Fee", "Monthly account fee applied on correct schedule", "Fee applied on last day of month; fee waiver rules checked; zero-fee accounts not charged"),
        ("Account Operations", "Statement", "Monthly statement generated and made available digitally", "Statement PDF generated; available in digital banking; notification sent"),
    ],
    "5.2 Term Deposits": [
        ("Term Deposit", "Break", "Early break fee calculated and applied correctly", "Break fee = interest penalty per T&Cs; remaining interest recalculated; net amount credited"),
        ("Term Deposit", "Renewal", "Auto-renewal processed at maturity with current rate", "Principal + interest reinvested; new rate applied; renewal confirmation sent"),
    ],
    "5.3 Sweep & Investment Products": [
        ("Sweep Products", "Reporting", "Sweep activity report generated for treasury", "Report includes all sweeps, amounts, timestamps; daily summary sent to treasury team"),
        ("Sweep Products", "Tax", "Tax on interest calculated at correct rate", "Tax calculated per account tax status; tax voucher generated; HMRC reporting filed"),
    ],
    "6.1 Fraud Detection & Prevention": [
        ("Fraud Detection", "Rule", "Fraud detection rules updated from central rule repository", "New rules active within 5 minutes; version history maintained; rollback capability exists"),
        ("Fraud Detection", "Report", "Fraud dashboard updated with real-time metrics", "Dashboard refreshes every 60 seconds; alert counts, score distribution, false positive rate visible"),
    ],
    "6.2 AML/Sanctions Screening": [
        ("AML Screening", "List", "Sanctions lists updated within 24 hours of regulatory release", "List version tracked; update applied without system restart; audit of list changes maintained"),
        ("AML Screening", "SAR", "SAR report submitted to NCA within required timeframe", "SAR submitted within 24 hours of determination; reference number received; archive copy retained"),
    ],
    "6.3 Regulatory Reporting": [
        ("Regulatory Reporting", "Validation", "Report data validated against data quality rules", "All data quality rules passed; failure rate <1%; invalid data flagged and quarantined"),
        ("Regulatory Reporting", "SignOff", "Report digitally signed by authorized signatory", "Digital signature applied; signatory verified; signing chain auditable"),
    ],
    "7.1 Internet Banking": [
        ("Internet Banking", "Analytics", "User behavior tracked and sent to analytics platform", "Page views, clicks, and session duration recorded; privacy-compliant data anonymization applied"),
        ("Internet Banking", "Search", "Search results indexed by Elasticsearch with fuzzy matching", "Search returns results within 500ms; typos corrected; most relevant results ranked first"),
    ],
    "7.2 Mobile Banking": [
        ("Mobile Banking", "Location", "Nearby branches retrieved based on device GPS location", "Branches sorted by distance; opening hours displayed; directions link provided"),
        ("Mobile Banking", "Feedback", "App feedback submitted and stored in CRM", "Feedback linked to customer record; rating captured; feedback routed to product team"),
    ],
    "7.3 Branch Banking (Teller)": [
        ("Branch Banking", "Appointment", "Customer appointment booked and synced with teller schedule", "Appointment slot confirmed; reminder sent 24 hours before; wait time minimized"),
        ("Branch Banking", "Cash", "Teller cash position reconciled at end of shift", "Cash difference <0.01% of total; discrepancies flagged; supervisor sign-off required"),
    ],
    "8.1 Nostro/Vostro Reconciliation": [
        ("Nostro Reconciliation", "Reporting", "Aged break report generated with items >30 days highlighted", "Report generated daily; aged items tracked and escalated; break aging trend visible"),
        ("Nostro Reconciliation", "Alert", "Alert sent to operations team when break exceeds threshold", "Alert sent within 5 minutes of break detection; threshold configurable per currency"),
    ],
    "8.2 Treasury & Liquidity Management": [
        ("Treasury Management", "Forecast", "Liquidity forecast generated with 30-day forward view", "Forecast accuracy within 95%; cash flow waterfall visible; what-if scenarios supported"),
        ("Treasury Management", "Hedge", "FX hedge executed to mitigate open currency exposure", "Hedge covers 100% of projected exposure; hedge effectiveness tested monthly"),
    ],
    "8.3 End-of-Day Settlement": [
        ("EOD Settlement", "Reporting", "Settlement report generated with full audit trail", "Report includes all transactions; settlement status for each; exception summary provided"),
        ("EOD Settlement", "Audit", "Settlement audit log sent to SIEM system for compliance", "All EOD events logged; tamper-proof audit trail maintained; retention period 7 years"),
    ],
}

# ─── NEW SUB-FLOWS FOR EXISTING SECTIONS (2.4, 3.4, 4.4, 5.4) ──────────────────

NEW_SUBFLOWS = {
    # ── Section 2: Payments & Transfers ──────────────────────────────────────
    "2.4 Batch Payment Processing": {
        "after": "2.3 Real-Time Payment (Faster Payments)",
        "section": "Payments & Transfers",
        "description": "Corporate customer submits batch payment file. Payment hub validates, processes bulk payments through clearing, generates reconciliation report.",
        "actors": "Customer (Corporate), Payment Operations",
        "systems": "Digital Banking (Backbase), Payment Hub (Volante), SEPA Clearing (EBA Clearing), Reconciliation Engine (SmartStream), Core Banking (Temenos Transact)",
        "mermaid": [
            "    participant C as Customer (Corporate)",
            "    participant DB as Digital Banking<br/>(Backbase)",
            "    participant PH as Payment Hub<br/>(Volante)",
            "    participant SEPA as SEPA Clearing<br/>(EBA Clearing)",
            "    participant CBS as Core Banking<br/>(Temenos Transact)",
            "    participant REC as Reconciliation<br/>(SmartStream)",
            "    C->>DB: Upload batch payment file<br/>CSV, 250 payments, total=125,000.00 GBP",
            "    DB->>PH: Submit batch file<br/>ISO 20022 pain.002",
            "    PH->>PH: Validate file format<br/>check headers, row count, balance",
            "    PH->>PH: Individual validation<br/>250 items validated, 2 warnings",
            "    PH-->>DB: Validation report<br/>248 valid, 2 warnings",
            "    DB-->>C: Confirm batch submission?<br/>248 payments, total=124,500.00 GBP",
            "    C->>DB: Approve batch",
            "    DB->>PH: Execute batch",
            "    PH->>PH: Group by payment type<br/>SEPA Credit Transfers",
            "    PH->>SEPA: Submit batch<br/>ISO 20022 pacs.008 bulk",
            "    SEPA->>SEPA: Process batch<br/>net position calculated",
            "    SEPA-->>PH: Settlement confirmation<br/>total=124,500.00 GBP, timestamp=14:30:00Z",
            "    PH->>CBS: Post individual credits<br/>batch ref=BAT-2026-042",
            "    CBS-->>PH: 248 entries posted",
            "    PH->>REC: Submit batch for reconciliation",
            "    REC->>REC: Auto-match 248 items<br/>248 matched, 0 unmatched",
            "    REC-->>PH: Reconciliation complete",
            "    PH-->>DB: Batch summary<br/>248 processed, 0 failed",
            "    DB-->>C: Batch completed<br/>reference=BAT-2026-042, status=Completed",
        ],
        "integrations": [
            ("Batch Payment", "File Upload", "UploadBatchFile", "Digital Banking (Backbase)", "Payment Hub (Volante)", "Backbase REST API", "Volante API (ISO 20022)", "API-led (Real-time)", "Medium"),
            ("Batch Payment", "Validation", "ValidateBatchFile", "Payment Hub (Volante)", "Payment Hub (Volante)", "Internal", "Internal", "Batch (Scheduled)", "Medium"),
            ("Batch Payment", "Clearing", "SubmitBatchToClearing", "Payment Hub (Volante)", "SEPA Clearing (EBA Clearing)", "Volante API (ISO 20022)", "EBA Clearing API (ISO 20022)", "Batch (Scheduled)", "High"),
            ("Batch Payment", "Posting", "PostBatchEntries", "Payment Hub (Volante)", "Core Banking (Temenos Transact)", "Volante REST API", "Temenos REST API (API Key)", "Batch (Scheduled)", "High"),
            ("Batch Payment", "Reconciliation", "ReconcileBatch", "Payment Hub (Volante)", "Reconciliation Engine (SmartStream)", "Volante REST API", "SmartStream API (REST)", "Event-driven", "Simple"),
        ],
        "acceptance": [
            ("Batch Payment", "File Upload", "Batch payment file uploaded in supported format (CSV/ISO 20022 XML)", "File parsed successfully; row count and total amount validated"),
            ("Batch Payment", "Validation", "Each payment validated individually; warnings non-blocking", "Invalid rows rejected with reason; valid rows processed; partial acceptance supported"),
            ("Batch Payment", "Clearing", "Batch submitted to SEPA Clearing as ISO 20022 bulk pacs.008", "Clearing confirmation received; settlement timestamp recorded; exceptions reported"),
            ("Batch Payment", "Posting", "All valid payments posted to individual accounts", "248 entries posted; total debited matches batch total; posting report generated"),
            ("Batch Payment", "Reconciliation", "Batch fully reconciled with zero unmatched items", "Reconciliation report generated; any breaks investigated before next batch"),
        ],
    },
    # ── Section 3: Lending & Credit Management ────────────────────────────────
    "3.4 Loan Servicing & Collections": {
        "after": "3.3 Credit Assessment & Scoring",
        "section": "Lending & Credit Management",
        "description": "Loan servicing team manages ongoing loan accounts - payment collection, arrears management, statement generation, and early-stage collections.",
        "actors": "Customer, Loan Servicing Officer, Collections Officer",
        "systems": "LOS (nCino), Core Banking (Temenos Transact), Collections System (FICO Debt Manager), Document Mgmt (M-Files), Notification Service (Firebase)",
        "mermaid": [
            "    participant CBS as Core Banking<br/>(Temenos Transact)",
            "    participant LOS as Loan Servicing<br/>(nCino)",
            "    participant COL as Collections<br/>(FICO Debt Manager)",
            "    participant DOC as Document Mgmt<br/>(M-Files)",
            "    participant NOT as Notification<br/>(Firebase)",
            "    participant C as Customer",
            "    CBS->>CBS: Monthly payment due<br/>LN-2026-042, amount=493.75 GBP",
            "    CBS->>CBS: Attempt direct debit<br/>ACCT-4001-2026, balance=44,490.50",
            "    CBS->>CBS: Payment successful<br/>debit 493.75, new balance=43,996.75",
            "    CBS->>LOS: Update loan status<br/>payment_received, next_due=2026-08-01",
            "    LOS-->>LOS: Record payment<br/>installment 1 of 60",
            "    CBS->>NOT: Send payment confirmation",
            "    NOT-->>C: Payment confirmed<br/>LN-2026-042, 493.75 GBP",
            "    LOS->>DOC: Generate statement<br/>loan_id=LN-2026-042, period=monthly",
            "    DOC-->>C: Statement available",
            "    CBS->>CBS: Arrears check<br/>all loans, DPD report",
            "    CBS->>COL: Delinquent account<br/>LN-2026-043, DPD=15, amount=550.00",
            "    COL->>COL: Score account<br/>collection_score=720, risk=Medium",
            "    COL->>COL: Assign collector<br/>strategy=Early_Collection",
            "    COL->>NOT: Send reminder SMS",
            "    NOT-->>C: Payment reminder<br/>LN-2026-043, 550.00 GBP, due=3 days",
            "    C->>CBS: Make payment<br/>550.00 GBP, reference=LN-2026-043",
            "    CBS->>COL: Payment received<br/>account cured",
            "    COL->>COL: Close collection case",
        ],
        "integrations": [
            ("Loan Servicing", "Payment", "ProcessMonthlyPayment", "Core Banking (Temenos Transact)", "Core Banking (Temenos Transact)", "Internal", "Internal", "Batch (Scheduled)", "Medium"),
            ("Loan Servicing", "Notification", "SendPaymentConfirmation", "Core Banking (Temenos Transact)", "Notification Service (Firebase)", "Temenos REST API", "Firebase FCM API", "Event-driven", "Simple"),
            ("Loan Servicing", "Arrears", "FlagDelinquentAccount", "Core Banking (Temenos Transact)", "Collections (FICO Debt Manager)", "Temenos REST API", "FICO API (SOAP)", "Event-driven", "Medium"),
            ("Loan Servicing", "Collections", "AssignCollectionStrategy", "Collections (FICO Debt Manager)", "Collections (FICO Debt Manager)", "Internal", "Internal", "API-led (Real-time)", "Medium"),
            ("Loan Servicing", "Statement", "GenerateLoanStatement", "LOS (nCino)", "Document Mgmt (M-Files)", "nCino REST API", "M-Files REST API (API Key)", "Batch (Scheduled)", "Simple"),
        ],
        "acceptance": [
            ("Loan Servicing", "Payment", "Monthly direct debit payment processed on due date", "Payment debited on due date; loan balance reduced; next due date calculated"),
            ("Loan Servicing", "Notification", "Payment confirmation sent to customer immediately", "Confirmation includes amount, loan ID, remaining balance; delivered within 60 seconds"),
            ("Loan Servicing", "Arrears", "Delinquent accounts flagged correctly based on DPD threshold", "Accounts with DPD >0 flagged; severity assigned based on DPD bands; escalation triggered at 30 DPD"),
            ("Loan Servicing", "Collections", "Collection strategy assigned based on risk score and DPD", "Strategy determined by collection score; treatment plan customized; contact schedule set"),
            ("Loan Servicing", "Statement", "Monthly loan statement generated and made available", "Statement shows payments, interest, outstanding balance; available in digital banking and document mgmt"),
        ],
    },
    # ── Section 4: Cards Management ───────────────────────────────────────────
    "4.4 Card Rewards & Loyalty": {
        "after": "4.3 Card Dispute Management",
        "section": "Cards Management",
        "description": "Cardholder earns rewards on qualifying transactions. Rewards engine calculates points, manages redemption, and integrates with partner systems.",
        "actors": "Customer, Card Operations, Marketing Manager",
        "systems": "Card Management (Fiserv), Rewards Engine (LoyaltyPlus), Digital Banking (Backbase), Partner Portal (Avios), Notification Service (Firebase)",
        "mermaid": [
            "    participant CMS as Card Management<br/>(Fiserv)",
            "    participant REW as Rewards Engine<br/>(LoyaltyPlus)",
            "    participant DB as Digital Banking<br/>(Backbase)",
            "    participant PART as Partner Portal<br/>(Avios)",
            "    participant NOT as Notification<br/>(Firebase)",
            "    participant C as Customer",
            "    CMS->>REW: Transaction posted<br/>card=CARD-2026-001, amount=85.50 GBP, mcc=5311",
            "    REW->>REW: Calculate points<br/>2 points per GBP, mcc multiplier=1x",
            "    REW-->>CMS: Points awarded<br/>171 points, balance=2,450",
            "    C->>DB: View rewards dashboard<br/>points balance, tier status",
            "    DB->>REW: Fetch rewards data",
            "    REW-->>DB: Points=2,450, tier=Silver<br/>next tier=Gold at 5,000 points",
            "    DB-->>C: Rewards dashboard",
            "    C->>DB: Browse reward catalogue<br/>travel, gift cards, cashback",
            "    DB->>REW: Get catalogue<br/>available rewards, points required",
            "    REW-->>DB: Catalogue returned<br/>50 items across 4 categories",
            "    C->>DB: Select reward<br/>100 GBP gift card, points=4,000",
            "    DB->>REW: Request redemption<br/>customerId=CUST-2026-001, reward=GC-042",
            "    REW->>REW: Validate points balance<br/>balance=2,450, required=4,000",
            "    REW-->>DB: Insufficient points<br/>shortfall=1,550 points",
            "    DB-->>C: Insufficient balance<br/>4,000 needed, 2,450 available",
            "    C->>DB: Choose alternative<br/>50 GBP gift card, points=2,000",
            "    DB->>REW: Request redemption<br/>customerId=CUST-2026-001, reward=GC-021",
            "    REW->>REW: Deduct points<br/>2,450 - 2,000 = 450 remaining",
            "    REW->>PART: Issue gift card<br/>partner=Tesco, amount=50.00 GBP",
            "    PART-->>REW: Gift card issued<br/>code=TESC-2026-042, expires=2027-07",
            "    REW-->>DB: Redemption confirmed<br/>gift_card=XXXX-042, expiry=2027-07-06",
            "    DB->>NOT: Send redemption confirmation",
            "    NOT-->>C: Reward redeemed<br/>50 GBP Tesco gift card, code in app",
        ],
        "integrations": [
            ("Card Rewards", "Earning", "award_points", "Card Management (Fiserv)", "Rewards Engine (LoyaltyPlus)", "Fiserv REST API", "LoyaltyPlus API (REST)", "Event-driven", "Medium"),
            ("Card Rewards", "Dashboard", "GetRewardsDashboard", "Digital Banking (Backbase)", "Rewards Engine (LoyaltyPlus)", "Backbase REST API", "LoyaltyPlus API (REST)", "API-led (Real-time)", "Simple"),
            ("Card Rewards", "Catalogue", "GetRewardCatalogue", "Digital Banking (Backbase)", "Rewards Engine (LoyaltyPlus)", "Backbase REST API", "LoyaltyPlus API (REST)", "API-led (Real-time)", "Simple"),
            ("Card Rewards", "Redemption", "RedeemReward", "Digital Banking (Backbase)", "Rewards Engine (LoyaltyPlus)", "Backbase REST API", "LoyaltyPlus API (REST)", "API-led (Real-time)", "Medium"),
            ("Card Rewards", "Partner", "IssuePartnerReward", "Rewards Engine (LoyaltyPlus)", "Partner Portal (Avios)", "LoyaltyPlus API", "Avios API (SOAP)", "API-led (Real-time)", "High"),
            ("Card Rewards", "Notification", "SendRedemptionConfirm", "Digital Banking (Backbase)", "Notification Service (Firebase)", "Backbase REST API", "Firebase FCM API", "Event-driven", "Simple"),
        ],
        "acceptance": [
            ("Card Rewards", "Earning", "Reward points calculated and awarded on qualifying transaction posting", "Points calculated per card programme rules; points awarded within 60 seconds of posting"),
            ("Card Rewards", "Dashboard", "Customer views rewards dashboard with points balance and tier", "Dashboard loads within 2 seconds; points balance accurate; tier progress shown"),
            ("Card Rewards", "Catalogue", "Reward catalogue returned with available items and points required", "Catalogue filtered by eligibility; out-of-stock items hidden; regional availability enforced"),
            ("Card Rewards", "Redemption", "Points redeemed for selected reward; sufficient balance validated", "Sufficient points: redemption confirmed; insufficient points: clear shortfall message shown"),
            ("Card Rewards", "Partner", "Partner reward issued via partner API for third-party fulfilment", "Partner confirms fulfilment; gift card code returned; expiry date provided"),
            ("Card Rewards", "Notification", "Redemption confirmation sent to customer", "Notification includes reward details, delivery method, and expected timeline"),
        ],
    },
    # ── Section 5: Deposits & Savings Products ────────────────────────────────
    "5.4 Overdraft Management": {
        "after": "5.3 Sweep & Investment Products",
        "section": "Deposits & Savings Products",
        "description": "Customer manages overdraft facility. System monitors usage, applies interest, sends alerts, handles limit increase requests and fee processing.",
        "actors": "Customer, Product Manager, Risk Analyst",
        "systems": "Core Banking (Temenos Transact), Digital Banking (Backbase), Decision Engine (FICO), Notification Service (Firebase), CRM (Salesforce Financial Services)",
        "mermaid": [
            "    participant C as Customer",
            "    participant DB as Digital Banking<br/>(Backbase)",
            "    participant CBS as Core Banking<br/>(Temenos Transact)",
            "    participant DE as Decision Engine<br/>(FICO)",
            "    participant CRM as CRM<br/>(Salesforce Financial Svcs)",
            "    participant NOT as Notification<br/>(Firebase)",
            "    C->>DB: Request overdraft<br/>limit=2,000.00 GBP, account=ACCT-4001-2026",
            "    DB->>CBS: Check eligibility<br/>risk_rating=Low, account_age=6 months",
            "    CBS->>DE: Score overdraft request<br/>customerId=CUST-2026-001, amount=2,000.00",
            "    DE-->>CBS: Approve<br/>limit=2,000.00, rate=19.9% APR",
            "    CBS->>CBS: Setup overdraft<br/>limit_id=ODL-2026-001, limit=2,000.00",
            "    CBS-->>DB: Overdraft approved",
            "    DB-->>C: Overdraft approved<br/>2,000.00 GBP at 19.9% APR",
            "    CBS->>CBS: Daily position check<br/>balance=-500.00, limit=2,000.00",
            "    CBS->>CBS: Calculate interest<br/>500.00 * 19.9% / 365 = 0.27 GBP",
            "    CBS->>NOT: Threshold alert<br/>usage=25% of limit",
            "    NOT-->>C: Overdraft usage alert<br/>500.00 of 2,000.00 used",
            "    C->>DB: Request limit increase<br/>new_limit=5,000.00 GBP",
            "    DB->>CBS: Evaluate increase<br/>current_usage=500.00, requested=5,000.00",
            "    CBS->>DE: Credit check for increase",
            "    DE-->>CBS: Approved<br/>new_limit=5,000.00, rate=18.5% APR",
            "    CBS->>CBS: Update limit<br/>ODL-2026-001, limit=5,000.00",
            "    CBS-->>DB: Limit increased",
            "    DB-->>C: Limit increased to 5,000.00 GBP",
            "    CBS->>CBS: Monthly fee cycle<br/>overdraft fee=5.00 GBP",
            "    CBS->>CBS: Apply fee<br/>debit ACCT-4001-2026, -5.00 GBP",
            "    CBS->>CRM: Log overdraft activity<br/>fee_applied, limit=5,000.00",
            "    CRM-->>CBS: Cross-sell suggestion<br/>personal loan consolidation",
        ],
        "integrations": [
            ("Overdraft", "Setup", "SetupOverdraftLimit", "Digital Banking (Backbase)", "Core Banking (Temenos Transact)", "Backbase REST API", "Temenos REST API (API Key)", "API-led (Real-time)", "Medium"),
            ("Overdraft", "Scoring", "ScoreOverdraftRequest", "Core Banking (Temenos Transact)", "Decision Engine (FICO)", "Temenos REST API", "FICO Blaze API (REST)", "API-led (Real-time)", "Medium"),
            ("Overdraft", "Alert", "SendUsageAlert", "Core Banking (Temenos Transact)", "Notification Service (Firebase)", "Temenos REST API", "Firebase FCM API", "Event-driven", "Simple"),
            ("Overdraft", "Increase", "ProcessLimitIncrease", "Digital Banking (Backbase)", "Core Banking (Temenos Transact)", "Backbase REST API", "Temenos REST API (API Key)", "API-led (Real-time)", "Medium"),
            ("Overdraft", "Fee", "ApplyOverdraftFee", "Core Banking (Temenos Transact)", "Core Banking (Temenos Transact)", "Internal", "Internal", "Batch (Scheduled)", "Simple"),
            ("Overdraft", "CrossSell", "GetCrossSellOffer", "Core Banking (Temenos Transact)", "CRM (Salesforce Financial Services)", "Temenos REST API", "Salesforce REST API (OAuth2)", "API-led (Real-time)", "Medium"),
        ],
        "acceptance": [
            ("Overdraft", "Setup", "Customer requests overdraft; eligibility checked and limit set", "Eligibility verified; limit <= risk-based max; overdraft activated immediately"),
            ("Overdraft", "Scoring", "Credit score-based decision for overdraft approval", "Score threshold determines approval; auto-approved for scores >680; manual review <680"),
            ("Overdraft", "Alert", "Customer notified when overdraft usage crosses thresholds (25%, 50%, 75%, 90%)", "Alert sent within 5 minutes of crossing threshold; contains usage details and interest info"),
            ("Overdraft", "Increase", "Limit increase processed after re-scoring", "Increase approved within customer risk profile; new limit effective immediately"),
            ("Overdraft", "Fee", "Monthly overdraft fee applied on correct schedule", "Fee applied; fee waived if balance positive for 80% of month; fee amount per published schedule"),
            ("Overdraft", "CrossSell", "Cross-sell offer generated based on overdraft usage patterns", "Relevant offer displayed; consolidation loan offered for persistent overdraft >60 days"),
        ],
    },
}

# ─── NEW SECTIONS 9-12 ──────────────────────────────────────────────────────────

NEW_SECTIONS = {
    # ── Section 9: Trade Finance ──────────────────────────────────────────────
    "9: Trade Finance  - `BC063`": {
        "description": "Trade finance operations covering letter of credit issuance, bank guarantees, and invoice financing. Supports international trade with documentary credit instruments.",
        "subflows": {
            "9.1 Letter of Credit Issuance": {
                "description": "Importer applies for LC. Bank issues LC via SWIFT MT700 to advising bank. Exporter ships goods, presents documents, bank checks compliance and pays.",
                "actors": "Customer (Importer), Trade Operations Officer, Compliance Officer",
                "systems": "Trade Finance System (Finacle Trade), SWIFT Alliance Gateway, Core Banking (Temenos Transact), Compliance (WorldCheck), Document Mgmt (M-Files)",
                "mermaid": [
                    "    participant IMP as Importer<br/>(Acme Corp Ltd)",
                    "    participant TFS as Trade Finance<br/>(Finacle Trade)",
                    "    participant SW as SWIFT Alliance",
                    "    participant ADV as Advising Bank<br/>(Deutsche Bank)",
                    "    participant EXP as Exporter<br/>(Global Exports GmbH)",
                    "    participant CBS as Core Banking<br/>(Temenos Transact)",
                    "    participant COMP as Compliance<br/>(WorldCheck)",
                    "    IMP->>TFS: Submit LC application<br/>beneficiary=Global Exports GmbH, amount=500,000 USD",
                    "    TFS->>CBS: Check collateral/limit<br/>applicant=Acme Corp Ltd, limit=2,000,000 USD",
                    "    CBS-->>TFS: Limit available<br/>used=750,000, available=1,250,000 USD",
                    "    TFS->>COMP: Screen parties<br/>applicant, beneficiary, goods description",
                    "    COMP-->>TFS: No sanctions matches<br/>risk=Low",
                    "    TFS->>TFS: Generate LC terms<br/>Irrevocable Sight LC, exp=2026-12-31",
                    "    TFS->>SW: Issue LC via MT700<br/>LC-2026-001, amount=500,000 USD",
                    "    SW->>ADV: Forward MT700",
                    "    ADV->>ADV: Authenticate & advise<br/>verify SWIFT keys",
                    "    ADV-->>EXP: LC advised<br/>LC-2026-001, terms confirmed",
                    "    EXP->>EXP: Ship goods<br/>per LC terms, bill of lading issued",
                    "    EXP->>ADV: Present documents<br/>invoice, B/L, packing list, COO",
                    "    ADV->>ADV: Check documents<br/>against LC terms, discrepancy check",
                    "    ADV-->>SW: Forward docs + MT730",
                    "    SW->>TFS: Documents received",
                    "    TFS->>TFS: Verify documents<br/>compliant, no discrepancies",
                    "    TFS->>CBS: Debit applicant<br/>500,000 USD, fee=1,500 USD",
                    "    CBS-->>TFS: Payment ready",
                    "    TFS->>SW: Issue MT202 cover<br/>payment to advising bank",
                    "    SW->>ADV: Cover received",
                    "    ADV-->>EXP: Payment credited<br/>500,000 USD less charges",
                    "    TFS->>TFS: Archive LC record<br/>closure, audit trail",
                ],
                "integrations": [
                    ("LC Issuance", "Application", "SubmitLCApplication", "Importer Portal (Finacle Trade)", "Trade Finance System (Finacle Trade)", "Finacle Web Portal", "Finacle Trade API", "API-led (Real-time)", "Medium"),
                    ("LC Issuance", "Limit", "CheckCustomerLimit", "Trade Finance System (Finacle Trade)", "Core Banking (Temenos Transact)", "Finacle REST API", "Temenos REST API (API Key)", "API-led (Real-time)", "Medium"),
                    ("LC Issuance", "Compliance", "ScreenTradeParties", "Trade Finance System (Finacle Trade)", "Compliance (WorldCheck)", "Finacle REST API", "WorldCheck API (SOAP)", "API-led (Real-time)", "High"),
                    ("LC Issuance", "SWIFT", "IssueMT700", "Trade Finance System (Finacle Trade)", "SWIFT Alliance Gateway", "Finacle Trade API (MT)", "SWIFT Alliance (MT700)", "API-led (Real-time)", "High"),
                    ("LC Issuance", "Payment", "ProcessLCPayment", "Trade Finance System (Finacle Trade)", "Core Banking (Temenos Transact)", "Finacle REST API", "Temenos REST API (API Key)", "API-led (Real-time)", "Medium"),
                    ("LC Issuance", "Archive", "ArchiveLC", "Trade Finance System (Finacle Trade)", "Document Mgmt (M-Files)", "Finacle REST API", "M-Files REST API (API Key)", "Event-driven", "Simple"),
                ],
                "acceptance": [
                    ("LC Issuance", "Application", "LC application submitted with all required fields and supporting documents", "Application validated; limit checked; incomplete applications rejected with clear errors"),
                    ("LC Issuance", "Limit", "Customer limit checked and sufficient for LC face value plus margin", "Limit reserved; available limit reduced; margin requirement of 10-30% verified"),
                    ("LC Issuance", "Compliance", "All trade parties screened against sanctions and PEP lists", "Parties screened; high-risk jurisdictions flagged; enhanced due diligence triggered if required"),
                    ("LC Issuance", "SWIFT", "SWIFT MT700 message issued and sent to advising bank", "MT700 authenticated by SWIFT; UETR assigned; advising bank acknowledges within 24hrs"),
                    ("LC Issuance", "Payment", "Payment processed on compliant document presentation", "Documents verified compliant; payment made within agreed tenor; discrepancies handled per UCP600"),
                    ("LC Issuance", "Archive", "LC record archived with full document set and audit trail", "All documents indexed; audit trail complete; retention period 7 years post-expiry"),
                ],
            },
            "9.2 Bank Guarantee Issuance": {
                "description": "Customer requests bank guarantee for a contract bid. Bank issues guarantee to beneficiary, manages margin/collateral, handles claim and expiry.",
                "actors": "Customer (Corporate), Trade Operations, Risk Analyst",
                "systems": "Trade Finance System (Finacle Trade), SWIFT Alliance Gateway, Core Banking (Temenos Transact), Risk System (Moody's), Document Mgmt (M-Files)",
                "mermaid": [
                    "    participant C as Customer<br/>(Acme Corp Ltd)",
                    "    participant TFS as Trade Finance<br/>(Finacle Trade)",
                    "    participant CBS as Core Banking<br/>(Temenos Transact)",
                    "    participant RISK as Risk System<br/>(Moody's)",
                    "    participant SW as SWIFT Alliance",
                    "    participant BEN as Beneficiary<br/>(Govt Procurement)",
                    "    C->>TFS: Request bid bond<br/>project=Infra Tender, amount=50,000 GBP expiry=2026-10-15",
                    "    TFS->>CBS: Block margin<br/>margin=100% cash, hold=50,000 GBP",
                    "    CBS-->>TFS: Margin held<br/>available_balance reduced",
                    "    TFS->>RISK: Assess counterparty risk<br/>applicant=Acme Corp Ltd",
                    "    RISK-->>TFS: Risk rating=A<br/>low risk, standard terms",
                    "    TFS->>TFS: Generate guarantee text<br/>bid bond template, jurisdiction=English",
                    "    TFS->>SW: Issue guarantee via MT760<br/>GUA-2026-001, amount=50,000 GBP",
                    "    SW-->>TFS: Guarantee issued",
                    "    TFS-->>C: Guarantee issued<br/>ref=GUA-2026-001, sent to beneficiary",
                    "    BEN->>BEN: Submit winning bid",
                    "    BEN-->>TFS: Claim on guarantee<br/>demand letter, certified default",
                    "    TFS->>TFS: Validate claim<br/>check terms, expiry, demand format",
                    "    TFS->>C: Notify customer<br/>claim received, 5 days to respond",
                    "    C->>TFS: Accept claim<br/>authorize payment",
                    "    TFS->>CBS: Release margin & pay<br/>debit margin, pay 50,000 GBP to beneficiary",
                    "    CBS-->>TFS: Payment completed",
                    "    TFS->>SW: Claim paid confirmation",
                    "    BEN-->>BEN: Funds received",
                ],
                "integrations": [
                    ("Guarantee", "Request", "RequestGuarantee", "Customer Portal (Finacle Trade)", "Trade Finance System (Finacle Trade)", "Finacle Web Portal", "Finacle Trade API", "API-led (Real-time)", "Simple"),
                    ("Guarantee", "Margin", "BlockCashMargin", "Trade Finance System (Finacle Trade)", "Core Banking (Temenos Transact)", "Finacle REST API", "Temenos REST API (API Key)", "API-led (Real-time)", "Medium"),
                    ("Guarantee", "Risk", "AssessCounterpartyRisk", "Trade Finance System (Finacle Trade)", "Risk System (Moody's)", "Finacle REST API", "Moody's Risk Analyst API (SOAP)", "API-led (Real-time)", "Medium"),
                    ("Guarantee", "SWIFT", "IssueMT760", "Trade Finance System (Finacle Trade)", "SWIFT Alliance Gateway", "Finacle Trade API (MT)", "SWIFT Alliance (MT760)", "API-led (Real-time)", "High"),
                    ("Guarantee", "Claim", "ProcessGuaranteeClaim", "Trade Finance System (Finacle Trade)", "Core Banking (Temenos Transact)", "Finacle REST API", "Temenos REST API (API Key)", "Event-driven", "High"),
                ],
                "acceptance": [
                    ("Guarantee", "Request", "Guarantee request submitted with all required details", "Application validated; guarantee type and template selected; terms confirmed"),
                    ("Guarantee", "Margin", "Cash margin blocked in customer account for guarantee value", "Margin successfully held; funds ear-marked; margin release triggered on expiry"),
                    ("Guarantee", "Risk", "Counterparty risk assessed and risk rating determined", "Risk rating assigned; rated A-E; rating determines margin % and pricing"),
                    ("Guarantee", "SWIFT", "SWIFT MT760 message issued to beneficiary bank", "MT760 authenticated; beneficiary bank notified; guarantee registered"),
                    ("Guarantee", "Claim", "Claim processed correctly per guarantee terms", "Claim validated against terms; payment made only if demand compliant; customer notified"),
                ],
            },
            "9.3 Invoice Financing": {
                "description": "Exporter requests financing against unpaid invoices. Bank evaluates invoices, advances funds, manages collection from buyer.",
                "actors": "Customer (Exporter), Trade Operations Officer, Risk Analyst",
                "systems": "Trade Finance System (Finacle Trade), Core Banking (Temenos Transact), Risk System (Moody's), Receivables Platform (TradeIX), Credit Insurance (Euler Hermes)",
                "mermaid": [
                    "    participant EXP as Exporter<br/>(Global Exports GmbH)",
                    "    participant TFS as Trade Finance<br/>(Finacle Trade)",
                    "    participant CBS as Core Banking<br/>(Temenos Transact)",
                    "    participant RISK as Risk System<br/>(Moody's)",
                    "    participant INS as Credit Insurance<br/>(Euler Hermes)",
                    "    participant BUY as Buyer<br/>(Acme Corp Ltd)",
                    "    EXP->>TFS: Submit invoice for financing<br/>INV-2026-001, amount=150,000 EUR, buyer=Acme Corp",
                    "    TFS->>RISK: Assess buyer credit<br/>Acme Corp Ltd, country=UK",
                    "    RISK-->>TFS: Buyer rating=A-<br/>credit_limit=200,000 EUR",
                    "    TFS->>INS: Check credit insurance<br/>buyer covered, limit=200,000 EUR",
                    "    INS-->>TFS: Coverage confirmed<br/>90% indemnity, premium=0.5%",
                    "    TFS->>TFS: Calculate advance<br/>invoice=150,000 EUR, advance_rate=85%",
                    "    TFS-->>EXP: Offer financing<br/>127,500 EUR advance, fee=1.5%, rate=SOFR+3%",
                    "    EXP->>TFS: Accept financing",
                    "    TFS->>CBS: Disburse advance<br/>127,500 EUR to exporter account",
                    "    CBS-->>TFS: Disbursed",
                    "    TFS->>BUY: Notify assignment<br/>pay TFS directly, invoice due=2026-09-30",
                    "    BUY->>CBS: Pay invoice at maturity<br/>150,000 EUR",
                    "    CBS->>TFS: Payment received<br/>buyer paid 150,000 EUR",
                    "    TFS->>TFS: Calculate final<br/>advance=127,500, fees=1,912.50, reserve=20,587.50",
                    "    TFS->>CBS: Release reserve<br/>20,587.50 EUR to exporter",
                    "    CBS-->>EXP: Reserve released<br/>financing closed",
                ],
                "integrations": [
                    ("Invoice Financing", "Submission", "SubmitInvoiceForFinancing", "Exporter Portal (Finacle Trade)", "Trade Finance System (Finacle Trade)", "Finacle Web Portal", "Finacle Trade API", "API-led (Real-time)", "Simple"),
                    ("Invoice Financing", "Credit Assessment", "AssessBuyerCredit", "Trade Finance System (Finacle Trade)", "Risk System (Moody's)", "Finacle REST API", "Moody's Risk Analyst API (SOAP)", "API-led (Real-time)", "Medium"),
                    ("Invoice Financing", "Insurance", "CheckCreditInsurance", "Trade Finance System (Finacle Trade)", "Credit Insurance (Euler Hermes)", "Finacle REST API", "Euler Hermes API (SOAP)", "API-led (Real-time)", "Medium"),
                    ("Invoice Financing", "Advance", "DisburseAdvance", "Trade Finance System (Finacle Trade)", "Core Banking (Temenos Transact)", "Finacle REST API", "Temenos REST API (API Key)", "API-led (Real-time)", "Medium"),
                    ("Invoice Financing", "Collection", "ProcessCollection", "Core Banking (Temenos Transact)", "Trade Finance System (Finacle Trade)", "Temenos REST API", "Finacle REST API", "Event-driven", "Medium"),
                ],
                "acceptance": [
                    ("Invoice Financing", "Submission", "Valid invoice submitted with proof of delivery and assignment clause", "Invoice validated against buyer; duplicate checks performed; fraud checks passed"),
                    ("Invoice Financing", "Credit Assessment", "Buyer credit assessed and facility limit checked", "Buyer within insured limit; credit rating determines advance rate; excess requires approval"),
                    ("Invoice Financing", "Insurance", "Credit insurance policy checked and coverage confirmed for buyer", "Coverage in force; indemnity % confirmed; premium calculated and quoted"),
                    ("Invoice Financing", "Advance", "Advance disbursed to exporter account per agreed terms", "Funds credited within 2 hours; advance rate applied correctly; fees deducted upfront"),
                    ("Invoice Financing", "Collection", "Maturity proceeds collected and reserve remitted to exporter", "Payment from buyer received; reserve calculated correctly; all fees accounted"),
                ],
            },
        },
    },

    # ── Section 10: Wealth Management ──────────────────────────────────────────
    "10: Wealth Management  - `BC074` `BC075`": {
        "description": "Wealth management services covering portfolio management, financial advisory, and asset allocation. Integration with market data, custody, and reporting systems.",
        "subflows": {
            "10.1 Portfolio Management & Rebalancing": {
                "description": "Wealth manager reviews portfolio performance against benchmarks. System executes rebalancing trades, generates performance reports, monitors risk.",
                "actors": "Portfolio Manager, Wealth Advisor, Client",
                "systems": "Portfolio Management (Bloomberg AIM), Custody System (BNY Mellon), Market Data (Reuters), Execution Mgmt (FlexTrade), Core Banking (Temenos Transact)",
                "mermaid": [
                    "    participant PM as Portfolio Manager",
                    "    participant PMS as Portfolio Mgmt<br/>(Bloomberg AIM)",
                    "    participant CUST as Custody<br/>(BNY Mellon)",
                    "    participant MKT as Market Data<br/>(Reuters)",
                    "    participant EXEC as Execution<br/>(FlexTrade)",
                    "    participant CBS as Core Banking<br/>(Temenos Transact)",
                    "    PMS->>CUST: Download holdings<br/>portfolio=PF-2026-001, date=2026-07-05",
                    "    CUST-->>PMS: Holdings report<br/>10 positions, total=1,250,000.00 GBP",
                    "    PMS->>MKT: Get current prices<br/>GBP bonds, equities, funds",
                    "    MKT-->>PMS: Prices updated<br/>FTSE 100, Gilt yields, FX rates",
                    "    PMS->>PMS: Calculate allocation<br/>actual vs target allocation",
                    "    PMS->>PMS: Identify drift<br/>equity=70% vs target=65%, drift=+5%",
                    "    PM->>PMS: Review rebalancing proposal<br/>sell equities, buy bonds",
                    "    PM->>PMS: Approve rebalancing",
                    "    PMS->>EXEC: Submit orders<br/>sell 100,000 GBP equities, buy bonds",
                    "    EXEC->>MKT: Execute trades<br/>market orders, TWAP schedule",
                    "    MKT-->>EXEC: Trades filled<br/>sells at avg 98.20, buys at 97.80",
                    "    EXEC-->>PMS: Execution report<br/>fills, avg prices, commissions",
                    "    PMS->>PMS: Rebalance complete<br/>allocation within tolerance",
                    "    PMS->>CUST: Settlement instructions<br/>trade settlement T+2",
                    "    PMS->>PMS: Generate report<br/>pre/post rebalancing comparison",
                    "    PMS-->>PM: Rebalancing summary<br/>tracking error reduced to 0.5%",
                ],
                "integrations": [
                    ("Portfolio Mgmt", "Holdings", "DownloadHoldings", "Portfolio Mgmt (Bloomberg AIM)", "Custody (BNY Mellon)", "Bloomberg AIM API", "BNY Mellon API (SFTP)", "Batch (Scheduled)", "High"),
                    ("Portfolio Mgmt", "Pricing", "GetMarketPrices", "Portfolio Mgmt (Bloomberg AIM)", "Market Data (Reuters)", "Bloomberg AIM API", "Reuters API (REST)", "API-led (Real-time)", "Medium"),
                    ("Portfolio Mgmt", "Rebalancing", "ExecuteRebalancing", "Portfolio Mgmt (Bloomberg AIM)", "Execution Mgmt (FlexTrade)", "Bloomberg AIM FIX", "FlexTrade FIX", "API-led (Real-time)", "High"),
                    ("Portfolio Mgmt", "Settlement", "SendSettlementInstructions", "Portfolio Mgmt (Bloomberg AIM)", "Custody (BNY Mellon)", "Bloomberg AIM API", "BNY Mellon API (SFTP)", "Batch (Scheduled)", "Medium"),
                ],
                "acceptance": [
                    ("Portfolio Mgmt", "Holdings", "Daily holdings downloaded from custody and reconciled", "All positions reconciled; price variances >0.5% flagged; failed downloads retried"),
                    ("Portfolio Mgmt", "Pricing", "Market prices retrieved for all instruments in portfolio", "Prices within 30 minutes of market open; stale prices flagged; estimated prices used as fallback"),
                    ("Portfolio Mgmt", "Rebalancing", "Portfolio rebalanced to target allocation within tolerance bands", "Drift >3% triggers rebalancing; execution within 1% of target; tracking error <=0.5%"),
                    ("Portfolio Mgmt", "Settlement", "Settlement instructions sent to custodian for executed trades", "Instructions match execution; T+2 settlement; failed trades investigated within 1 hour"),
                ],
            },
            "10.2 Financial Advisory & Planning": {
                "description": "Wealth advisor meets client, reviews financial goals, builds financial plan. System runs projections, tax optimization, retirement modeling.",
                "actors": "Wealth Advisor, Client",
                "systems": "Financial Planning (MoneyGuidePro/Advisor360), CRM (Salesforce Financial Services), Portfolio Mgmt (Bloomberg AIM), Document Mgmt (M-Files), Tax Engine (Vertex)",
                "mermaid": [
                    "    participant AD as Wealth Advisor",
                    "    participant CRM as CRM<br/>(Salesforce Financial Svcs)",
                    "    participant FP as Financial Planning<br/>(MoneyGuidePro)",
                    "    participant PMS as Portfolio Mgmt<br/>(Bloomberg AIM)",
                    "    participant TAX as Tax Engine<br/>(Vertex)",
                    "    participant C as Client<br/>(Alice Johnson)",
                    "    AD->>CRM: Schedule review<br/>client=CUST-2026-001, review=Annual",
                    "    CRM-->>AD: Profile loaded<br/>risk=Low, net_worth=450,000 GBP",
                    "    C->>AD: Attend review meeting",
                    "    AD->>FP: Initiate financial plan<br/>clientAge=36, retirementAge=65",
                    "    FP->>PMS: Fetch current holdings<br/>PF-2026-001, total=1,250,000 GBP",
                    "    PMS-->>FP: Holdings data",
                    "    FP->>FP: Run projections<br/>retirement=1,500,000 GBP target",
                    "    FP->>FP: Monte Carlo simulation<br/>5,000 scenarios, success_rate=82%",
                    "    FP-->>AD: Projection results<br/>deficit=250,000 GBP, inc savings 500/m",
                    "    FP->>TAX: Tax optimization calc<br/>ISA allowance, CGT threshold",
                    "    TAX-->>FP: Tax-efficient strategy<br/>use ISA, bed & ISA, harvest losses",
                    "    AD->>C: Present plan<br/>increase savings, rebalance, tax strategy",
                    "    C->>AD: Approve recommendations",
                    "    AD->>FP: Implement plan<br/>increase standing order to 2,000/m",
                    "    FP->>CRM: Log plan acceptance<br/>recommendations, review_date=annual",
                    "    CRM-->>AD: Next review scheduled<br/>2027-07-06",
                    "    AD-->>C: Plan summary sent<br/>digital copy in secure portal",
                ],
                "integrations": [
                    ("Financial Advisory", "Planning", "InitiateFinancialPlan", "Wealth Advisor Portal (Advisor360)", "Financial Planning (MoneyGuidePro)", "Advisor360 API", "MoneyGuidePro API (SOAP)", "API-led (Real-time)", "Medium"),
                    ("Financial Advisory", "Holdings", "FetchCurrentHoldings", "Financial Planning (MoneyGuidePro)", "Portfolio Mgmt (Bloomberg AIM)", "MoneyGuidePro API", "Bloomberg AIM API (REST)", "API-led (Real-time)", "Medium"),
                    ("Financial Advisory", "Tax Calc", "CalculateTaxStrategy", "Financial Planning (MoneyGuidePro)", "Tax Engine (Vertex)", "MoneyGuidePro API", "Vertex API (SOAP)", "API-led (Real-time)", "High"),
                    ("Financial Advisory", "CRM", "LogPlanAcceptance", "Financial Planning (MoneyGuidePro)", "CRM (Salesforce Financial Services)", "MoneyGuidePro API", "Salesforce REST API (OAuth2)", "Event-driven", "Simple"),
                ],
                "acceptance": [
                    ("Financial Advisory", "Planning", "Financial plan created with client goals, risk profile, and time horizon", "Plan includes retirement projection, education funding, and cash flow analysis"),
                    ("Financial Advisory", "Holdings", "Current holdings fetched from portfolio management and included in plan", "Holdings accurately reflected; unrealized gains calculated; asset allocation shown"),
                    ("Financial Advisory", "Tax Calc", "Tax optimization recommendations generated based on client tax position", "ISA allowance utilization; CGT harvesting; bed & ISA; pension contribution calc"),
                    ("Financial Advisory", "CRM", "Plan acceptance recorded and next review scheduled in CRM", "Plan status=Accepted; next review date set; recommendations tracked for follow-up"),
                ],
            },
            "10.3 Asset Allocation & Rebalancing Automation": {
                "description": "Automated model portfolio management. System monitors allocation drift, executes threshold-based rebalancing, handles cash flows and dividend reinvestment.",
                "actors": "Investment Committee, Portfolio Manager, Client",
                "systems": "Portfolio Mgmt (Bloomberg AIM), Risk Analytics (MSCI Barra), Execution Mgmt (FlexTrade), OMS (Charles River), Custody (BNY Mellon)",
                "mermaid": [
                    "    participant IC as Investment Committee",
                    "    participant PMS as Portfolio Mgmt<br/>(Bloomberg AIM)",
                    "    participant RISK as Risk Analytics<br/>(MSCI Barra)",
                    "    participant OMS as OMS<br/>(Charles River)",
                    "    participant EXEC as Execution<br/>(FlexTrade)",
                    "    participant CUST as Custody<br/>(BNY Mellon)",
                    "    IC->>PMS: Set strategic allocation<br/>equity=60%, bonds=30%, cash=10%",
                    "    PMS->>RISK: Validate allocation<br/>risk budget=12%, VaR=8.5%",
                    "    RISK-->>PMS: Within risk budget<br/>expected tracking error=1.2%",
                    "    PMS->>PMS: Model portfolios updated<br/>5 risk profiles, 3 models each",
                    "    PMS->>CUST: Reconcile all accounts<br/>client holdings vs model",
                    "    CUST-->>PMS: 150 accounts, 12 drifted<br/>drift >3% threshold",
                    "    PMS->>PMS: Auto-rebalance candidates<br/>12 accounts, total=480,000 GBP",
                    "    PMS->>OMS: Generate trade list<br/>offsetting trades across accounts",
                    "    OMS->>OMS: Net orders<br/>buy=600,000, sell=120,000, net=480,000",
                    "    OMS->>EXEC: Execute net trades",
                    "    EXEC-->>OMS: Fills reported",
                    "    OMS->>PMS: Allocation restored<br/>all accounts within 0.5% of model",
                    "    PMS->>PMS: Generate report<br/>rebalance summary, cost=1,200 GBP",
                    "    PMS-->>IC: Monthly rebalance report<br/>12 accounts rebalanced, total cost=0.10%",
                ],
                "integrations": [
                    ("Asset Allocation", "SAA", "SetStrategicAllocation", "Investment Committee Portal", "Portfolio Mgmt (Bloomberg AIM)", "Bloomberg AIM API", "Bloomberg AIM API", "API-led (Real-time)", "Simple"),
                    ("Asset Allocation", "Risk Validation", "ValidateRiskBudget", "Portfolio Mgmt (Bloomberg AIM)", "Risk Analytics (MSCI Barra)", "Bloomberg AIM API", "MSCI Barra API (SOAP)", "Batch (Scheduled)", "High"),
                    ("Asset Allocation", "Rebalancing", "AutoRebalancePortfolios", "Portfolio Mgmt (Bloomberg AIM)", "OMS (Charles River)", "Bloomberg AIM FIX", "Charles River FIX", "Batch (Scheduled)", "High"),
                    ("Asset Allocation", "Execution", "ExecuteNetTrades", "OMS (Charles River)", "Execution Mgmt (FlexTrade)", "Charles River FIX", "FlexTrade FIX", "API-led (Real-time)", "High"),
                ],
                "acceptance": [
                    ("Asset Allocation", "SAA", "Strategic asset allocation set by investment committee per risk profile", "SAA recorded; bands around each asset class; rebalancing thresholds defined"),
                    ("Asset Allocation", "Risk Validation", "Proposed allocation validated against risk budget", "VaR within limit; tracking error vs benchmark below threshold; stress tests passed"),
                    ("Asset Allocation", "Rebalancing", "Accounts with drift >threshold identified and auto-rebalanced", "Drift calculated daily; auto-rebalance within 1% of model; full or threshold rebalance selectable"),
                    ("Asset Allocation", "Execution", "Net trades executed efficiently across all rebalancing accounts", "Netting optimized; execution cost <15bps; T+2 settlement confirmed"),
                ],
            },
        },
    },

    # ── Section 11: Contact Center ─────────────────────────────────────────────
    "11: Contact Center  - `BC002` `BC034`": {
        "description": "Omnichannel contact center operations. Voice, email, chat, and social media interactions managed through IVR, CTI, and CRM integration with knowledge management.",
        "subflows": {
            "11.1 Omnichannel Customer Service": {
                "description": "Customer contacts via phone. IVR authenticates, routes to agent. Agent handles query with CRM context, knowledge articles, and follow-up actions.",
                "actors": "Customer, Contact Center Agent, Supervisor",
                "systems": "Contact Center (Genesys Cloud CX), CRM (Salesforce Service Cloud), IVR System (Avaya), Knowledge Mgmt (ServiceNow), Voice Biometrics (Nuance)",
                "mermaid": [
                    "    participant C as Customer<br/>(Alice Johnson)",
                    "    participant IVR as IVR<br/>(Avaya)",
                    "    participant CC as Contact Center<br/>(Genesys Cloud CX)",
                    "    participant CRM as CRM<br/>(Salesforce Service Cloud)",
                    "    participant KB as Knowledge Mgmt<br/>(ServiceNow)",
                    "    participant AG as Agent",
                    "    C->>IVR: Call inbound<br/>+44 7700 900001",
                    "    IVR->>IVR: Play welcome menu<br/>press 1 for banking, 2 for cards",
                    "    C->>IVR: Press 1<br/>account services",
                    "    IVR->>IVR: Authenticate caller<br/>ANR matched to customer record",
                    "    IVR->>CRM: Lookup customer<br/>phone=+44 7700 900001",
                    "    CRM-->>IVR: Customer found<br/>CUST-2026-001, Alice Johnson",
                    "    IVR->>CC: Route to agent<br/>skill=GeneralBanking, priority=Normal",
                    "    CC->>CRM: Screen pop<br/>customer context, last interaction",
                    "    CRM-->>CC: Context: 7 days ago<br/>missed payment inquiry",
                    "    CC->>AG: Call delivered<br/>customer=CUST-2026-001, context",
                    "    AG-->>C: Greeting<br/>Hello Alice, how can I help?",
                    "    C->>AG: Query about<br/>recent international payment fee",
                    "    AG->>CRM: Review payment history<br/>TXN-2026-8901, 1,250.00 GBP",
                    "    AG->>KB: Search fee schedule<br/>international transfer fee=15 GBP",
                    "    KB-->>AG: Fee explained<br/>15 GBP + 0.5% FX fee = 21.25 GBP",
                    "    AG-->>C: Explanation provided",
                    "    C->>AG: Request fee waiver<br/>one-time goodwill",
                    "    AG->>CRM: Submit waiver request<br/>amount=21.25 GBP, reason=Goodwill",
                    "    CRM->>CRM: Approval workflow<br/>supervisor approval required",
                    "    CRM-->>AG: Approved<br/>waiver reference=GW-2026-042",
                    "    AG-->>C: Fee waived<br/>credited to account, 3-5 days",
                    "    AG->>CC: End call<br/>wrap-up code=Inquiry Resolved",
                ],
                "integrations": [
                    ("Omnichannel", "IVR", "AuthenticateCaller", "IVR (Avaya)", "CRM (Salesforce Service Cloud)", "Avaya CTI API", "Salesforce CTI (Open CTI)", "API-led (Real-time)", "Medium"),
                    ("Omnichannel", "Routing", "RouteToAgent", "IVR (Avaya)", "Contact Center (Genesys Cloud CX)", "Avaya API", "Genesys API (REST)", "API-led (Real-time)", "High"),
                    ("Omnichannel", "Screen Pop", "DeliverCustomerContext", "Contact Center (Genesys Cloud CX)", "CRM (Salesforce Service Cloud)", "Genesys Cloud CX API", "Salesforce REST API (OAuth2)", "Event-driven", "Medium"),
                    ("Omnichannel", "Knowledge", "SearchKnowledgeBase", "Contact Center (Genesys Cloud CX)", "Knowledge Mgmt (ServiceNow)", "Genesys API", "ServiceNow API (REST)", "API-led (Real-time)", "Simple"),
                    ("Omnichannel", "Waiver", "ProcessFeeWaiver", "CRM (Salesforce Service Cloud)", "Core Banking (Temenos Transact)", "Salesforce REST API (OAuth2)", "Temenos REST API (API Key)", "Event-driven", "Medium"),
                ],
                "acceptance": [
                    ("Omnichannel", "IVR", "Caller authenticated via ANR matching to customer record in CRM", "Authenticated within 3 seconds; unrecognized callers routed to verification flow"),
                    ("Omnichannel", "Routing", "Call routed to agent with appropriate skill set and availability", "Routed within 5 seconds; skill-based routing honors priority; queue position displayed"),
                    ("Omnichannel", "Screen Pop", "Agent receives screen pop with customer context before answer", "Customer name, account, last interaction, risk flag displayed; context loads in <1 second"),
                    ("Omnichannel", "Knowledge", "Agent retrieves relevant knowledge articles during call", "Search returns top 5 articles; articles relevance >80%; outdated articles flagged"),
                    ("Omnichannel", "Waiver", "Fee waiver processed and approved through supervisor workflow", "Waiver approved/declined within workflow SLA; credited to account; notification sent to customer"),
                ],
            },
            "11.2 IVR Self-Service & Automation": {
                "description": "Customer interacts with automated IVR to perform transactions - balance inquiry, card activation, payment, password reset - without agent intervention.",
                "actors": "Customer, IVR Administrator",
                "systems": "IVR System (Avaya/Genesys), Core Banking (Temenos Transact), Card Management (Fiserv), Authentication (Nuance Voice Biometrics), Speech Analytics (CallMiner)",
                "mermaid": [
                    "    participant C as Customer",
                    "    participant IVR as IVR System<br/>(Avaya)",
                    "    participant VB as Voice Biometrics<br/>(Nuance)",
                    "    participant CBS as Core Banking<br/>(Temenos Transact)",
                    "    participant CMS as Card Mgmt<br/>(Fiserv)",
                    "    C->>IVR: Call IVR<br/>+44 7700 900001",
                    "    IVR->>IVR: Welcome & menu<br/>speech enabled",
                    "    C->>IVR: Say 'Check my balance'",
                    "    IVR->>VB: Voiceprint match<br/>utterance compared to enrolled",
                    "    VB-->>IVR: Authenticated<br/>confidence=92%, Alice Johnson",
                    "    IVR->>CBS: Fetch balance<br/>customerId=CUST-2026-001",
                    "    CBS-->>IVR: Balance=43,996.75 GBP<br/>ACCT-4001-2026",
                    "    IVR-->>C: Your balance is<br/>43,996 pounds and 75 pence",
                    "    C->>IVR: Say 'Make payment'<br/>50 GBP to Bob Smith",
                    "    IVR->>CBS: Lookup beneficiary<br/>BEN-2026-301, Bob Smith",
                    "    CBS-->>IVR: Beneficiary found",
                    "    IVR->>IVR: Confirm payment<br/>50 GBP to Bob Smith?",
                    "    C->>IVR: Say 'Yes'",
                    "    IVR->>CBS: Execute payment<br/>50.00 GBP, BEN-2026-301",
                    "    CBS-->>IVR: Payment confirmed<br/>ref=TXN-2026-8903",
                    "    IVR-->>C: Payment of 50 GBP<br/>to Bob Smith confirmed",
                    "    C->>IVR: Say 'Activate card'<br/>CARD-2026-001",
                    "    IVR->>CMS: Activate card<br/>cardId=CARD-2026-001",
                    "    CMS-->>IVR: Card activated",
                    "    IVR-->>C: Card activated<br/>you can now use it",
                    "    C->>IVR: End call",
                ],
                "integrations": [
                    ("IVR Self-Service", "Auth", "VoiceBiometricAuth", "IVR System (Avaya)", "Voice Biometrics (Nuance)", "Avaya VXML", "Nuance API (SOAP)", "API-led (Real-time)", "High"),
                    ("IVR Self-Service", "Balance", "CheckAccountBalance", "IVR System (Avaya)", "Core Banking (Temenos Transact)", "Avaya REST API", "Temenos REST API (API Key)", "API-led (Real-time)", "Medium"),
                    ("IVR Self-Service", "Payment", "ExecuteIVRPayment", "IVR System (Avaya)", "Core Banking (Temenos Transact)", "Avaya REST API", "Temenos REST API (API Key)", "API-led (Real-time)", "Medium"),
                    ("IVR Self-Service", "Card Activation", "ActivateCardIVR", "IVR System (Avaya)", "Card Management (Fiserv)", "Avaya REST API", "Fiserv API (SOAP)", "API-led (Real-time)", "Medium"),
                ],
                "acceptance": [
                    ("IVR Self-Service", "Auth", "Voice biometrics authenticates customer with >=90% confidence", "Enrolled customers authenticated in <5 seconds; low confidence fallback to PIN; impostor detection active"),
                    ("IVR Self-Service", "Balance", "Account balance read out accurately via text-to-speech", "Balance matches core system; multiple accounts offered for selection; masking for security"),
                    ("IVR Self-Service", "Payment", "Payment executed via IVR with verbal confirmation and 2FA", "Payment confirmed with amount and payee; SMS confirmation sent; same-day cut-off enforced"),
                    ("IVR Self-Service", "Card Activation", "Card activated via IVR with activation code verification", "Card status changes to Active within 5 seconds; SMS confirmation sent; activation logged"),
                ],
            },
            "11.3 Complaints & Case Management": {
                "description": "Customer submits complaint via digital channel. System creates case, routes to team, tracks resolution SLA, manages escalation, captures feedback.",
                "actors": "Customer, Complaints Officer, Supervisor, Ombudsman",
                "systems": "CRM (Salesforce Service Cloud), Case Management (Pega), Workflow (ServiceNow), Digital Banking (Backbase), Quality Mgmt (CallMiner)",
                "mermaid": [
                    "    participant C as Customer<br/>(Alice Johnson)",
                    "    participant DB as Digital Banking<br/>(Backbase)",
                    "    participant CRM as CRM<br/>(Salesforce Service Cloud)",
                    "    participant CM as Case Mgmt<br/>(Pega)",
                    "    participant WF as Workflow<br/>(ServiceNow)",
                    "    participant CO as Complaints Officer",
                    "    C->>DB: Submit complaint<br/>type=Unauthorized Transaction, ref=TXN-2026-8901",
                    "    DB->>CRM: Create case<br/>customer=CUST-2026-001, category=Dispute",
                    "    CRM->>CM: Initiate complaint workflow<br/>caseID=COMP-2026-042, severity=Medium",
                    "    CM->>WF: Assign case<br/>team=CardDisputes, SLA=48 hours",
                    "    WF-->>CO: Case assigned<br/>COMP-2026-042, priority=Medium",
                    "    CO->>CM: Review complaint<br/>txn details, customer history",
                    "    CO->>CBS: Investigate txn<br/>TXN-2026-8901, amount=1,250.00 GBP",
                    "    CBS-->>CO: Transaction found<br/>IP=192.168.1.1, device=Unknown",
                    "    CO->>CM: Interim response<br/>investigating, 24hr update expected",
                    "    CRM-->>C: Update received<br/>we are looking into this",
                    "    CO->>CBS: Reverse transaction<br/>goodwill reversal",
                    "    CBS-->>CO: Reversal completed<br/>TXN-2026-8901 reversed",
                    "    CO->>CM: Resolve complaint<br/>outcome=Resolved, compensation=21.25 GBP",
                    "    CM->>WF: Close case<br/>resolution documented",
                    "    WF-->>CO: Case closed<br/>reference=COMP-2026-042, SLA met",
                    "    CRM-->>C: Final resolution<br/>transaction reversed, fee waived",
                    "    C->>DB: Provide feedback<br/>satisfaction=5/5, resolved quickly",
                    "    DB->>CRM: Log satisfaction<br/>CSAT=5, NPS=9, comment=Excellent",
                ],
                "integrations": [
                    ("Complaints", "Case Creation", "CreateComplaintCase", "Digital Banking (Backbase)", "CRM (Salesforce Service Cloud)", "Backbase REST API", "Salesforce REST API (OAuth2)", "API-led (Real-time)", "Medium"),
                    ("Complaints", "Workflow", "AssignComplaintWorkflow", "CRM (Salesforce Service Cloud)", "Case Management (Pega)", "Salesforce REST API (OAuth2)", "Pega REST API (OAuth2)", "Event-driven", "Medium"),
                    ("Complaints", "Resolution", "ProcessComplaintResolution", "Case Management (Pega)", "Core Banking (Temenos Transact)", "Pega REST API (OAuth2)", "Temenos REST API (API Key)", "Event-driven", "Medium"),
                    ("Complaints", "Satisfaction", "CaptureCustomerFeedback", "Digital Banking (Backbase)", "CRM (Salesforce Service Cloud)", "Backbase REST API", "Salesforce REST API (OAuth2)", "API-led (Real-time)", "Simple"),
                ],
                "acceptance": [
                    ("Complaints", "Case Creation", "Complaint case created with correct category, severity, and customer context", "Case ID generated; category mapped to internal workflow; duplicate detection run"),
                    ("Complaints", "Workflow", "Case assigned to correct team with SLA tracking", "Team assignment based on category; SLA timer started; escalation path defined"),
                    ("Complaints", "Resolution", "Resolution action completed within SLA; customer updated at each milestone", "Resolution within SLA; customer communication sent at each stage; compensation logged"),
                    ("Complaints", "Satisfaction", "Customer satisfaction feedback captured post-resolution", "CSAT and NPS captured; feedback routed to quality team; trends tracked monthly"),
                ],
            },
        },
    },

    # ── Section 12: Collections & Recovery ─────────────────────────────────────
    "12: Collections & Recovery  - `BC077`": {
        "description": "End-to-end collections and recovery lifecycle. Early-stage collection campaigns, late-stage recovery, restructuring and forbearance, and charged-off account management.",
        "subflows": {
            "12.1 Early Collections & Delinquency Management": {
                "description": "Accounts become past due. Collections system applies treatment strategies, automated outreach via SMS/email, payment arrangement offers, and self-service cure.",
                "actors": "Collections Officer, Customer, Risk Analyst",
                "systems": "Collections System (FICO Debt Manager), Core Banking (Temenos Transact), Communication Engine (Twilio), CRM (Salesforce Financial Services), Decision Engine (FICO)",
                "mermaid": [
                    "    participant CBS as Core Banking<br/>(Temenos Transact)",
                    "    participant COL as Collections<br/>(FICO Debt Manager)",
                    "    participant DE as Decision Engine<br/>(FICO)",
                    "    participant COMM as Communication<br/>(Twilio)",
                    "    participant CRM as CRM<br/>(Salesforce Financial Svcs)",
                    "    participant C as Customer",
                    "    CBS->>COL: Delinquency feed<br/>LN-2026-043, DPD=5, amount=550.00 GBP",
                    "    COL->>COL: Score account<br/>propensity_to_pay=78%, risk=Low",
                    "    COL->>DE: Determine treatment<br/>segment=Early, product=Consumer Loan",
                    "    DE-->>COL: Strategy=Gentle_Reminder<br/>channel=SMS, frequency=7 days",
                    "    COL->>COMM: Send SMS reminder<br/>+44 7700 900001, amount=550.00 GBP",
                    "    COMM-->>C: Payment reminder<br/>Your payment of 550.00 GBP is due",
                    "    C->>CBS: Make payment<br/>550.00 GBP, reference=LN-2026-043",
                    "    CBS->>COL: Payment received<br/>account cured, DPD=0",
                    "    COL->>COL: Close collection<br/>case_status=Cured",
                    "    COL->>CRM: Log collection<br/>case=COL-2026-077, status=Cured",
                    "    CBS->>COL: New delinquency feed<br/>LN-2026-044, DPD=15, amount=1,200.00 GBP",
                    "    COL->>COL: Score account<br/>propensity_to_pay=45%, risk=Medium",
                    "    COL->>DE: Determine treatment<br/>segment=Mid, product=Personal Loan",
                    "    DE-->>COL: Strategy=Payment_Arrangement<br/>channel=Email+Phone",
                    "    COL->>COMM: Send email offer<br/>payment plan, hardship options",
                    "    C->>COL: Accept arrangement<br/>6 months, 200 GBP/month",
                    "    COL->>CBS: Setup arrangement<br/>payment_schedule=SCH-2026-001",
                    "    CBS-->>COL: Arrangement active",
                    "    COL->>COMM: Confirmation SMS<br/>arrangement confirmed, 200 GBP/m",
                ],
                "integrations": [
                    ("Early Collections", "Delinquency", "ReceiveDelinquencyFeed", "Core Banking (Temenos Transact)", "Collections (FICO Debt Manager)", "Temenos REST API", "FICO API (SOAP)", "Batch (Scheduled)", "Medium"),
                    ("Early Collections", "Treatment", "DetermineTreatmentStrategy", "Collections (FICO Debt Manager)", "Decision Engine (FICO)", "FICO API", "FICO Blaze API (REST)", "API-led (Real-time)", "Medium"),
                    ("Early Collections", "Outreach", "SendPaymentReminder", "Collections (FICO Debt Manager)", "Communication (Twilio)", "FICO REST API", "Twilio SMS/Email API", "Batch (Scheduled)", "Simple"),
                    ("Early Collections", "Arrangement", "SetupPaymentArrangement", "Collections (FICO Debt Manager)", "Core Banking (Temenos Transact)", "FICO REST API", "Temenos REST API (API Key)", "API-led (Real-time)", "Medium"),
                    ("Early Collections", "Logging", "LogCollectionActivity", "Collections (FICO Debt Manager)", "CRM (Salesforce Financial Services)", "FICO REST API", "Salesforce REST API (OAuth2)", "Event-driven", "Simple"),
                ],
                "acceptance": [
                    ("Early Collections", "Delinquency", "Delinquent accounts scored and segmented by risk and propensity", "Accounts scored within 1 hour of delinquency detection; segment determines strategy"),
                    ("Early Collections", "Treatment", "Treatment strategy assigned based on risk score and product type", "Strategy applied; channel and frequency set; strategy effectiveness tracked by cohort"),
                    ("Early Collections", "Outreach", "Automated outreach sent via appropriate channel (SMS/email/phone)", "Message delivered; open/read rate tracked; opt-out honored; regulatory compliance maintained"),
                    ("Early Collections", "Arrangement", "Payment arrangement setup correctly with schedule and amount", "Arrangement recorded in core banking; payments deducted automatically; cure tracked"),
                    ("Early Collections", "Logging", "Collection activity logged to CRM for customer 360 view", "Activity visible to all teams; contact history maintained; Do Not Contact list checked"),
                ],
            },
            "12.2 Late-Stage Recovery & Legal": {
                "description": "Accounts in advanced delinquency. Collections system escalates to recovery team, manages litigation, agency placement, asset repossession, and charged-off account management.",
                "actors": "Recovery Officer, Collections Manager, Legal Counsel, External Agency",
                "systems": "Collections System (FICO Debt Manager), Legal Case Mgmt (Pega), Agency Portal (Experian Collections), Core Banking (Temenos Transact), Document Mgmt (M-Files)",
                "mermaid": [
                    "    participant COL as Collections<br/>(FICO Debt Manager)",
                    "    participant CBS as Core Banking<br/>(Temenos Transact)",
                    "    participant LEG as Legal Case Mgmt<br/>(Pega)",
                    "    participant AG as External Agency<br/>(Experian Collections)",
                    "    participant DOC as Document Mgmt<br/>(M-Files)",
                    "    participant RO as Recovery Officer",
                    "    COL->>COL: Escalate to recovery<br/>LN-2026-045, DPD=90, amount=15,000 GBP",
                    "    COL->>RO: Case assigned<br/>priority=High, segment=Late_Stage",
                    "    RO->>COL: Review case<br/>borrower=CUST-2026-003, history=6 months",
                    "    COL->>CBS: Restrict account<br/>freeze further drawdowns",
                    "    CBS-->>COL: Account restricted",
                    "    RO->>CBS: Send demand letter<br/>formal demand, 14 days to pay",
                    "    CBS-->>C: Demand letter sent<br/>recorded delivery",
                    "    RO->>LEG: Instruct legal action<br/>caseID=LEG-2026-042, claim=15,000 GBP",
                    "    LEG->>DOC: File documents<br/>claim form, statement of debt",
                    "    RO->>COL: Update status<br/>legal_proceedings_initiated",
                    "    COL->>AG: Place with agency<br/>agency=FIRSTGROUP, commission=15%",
                    "    AG-->>COL: Account accepted<br/>collection strategy=Legal",
                    "    C->>AG: Make partial payment<br/>5,000.00 GBP",
                    "    AG-->>COL: Payment received<br/>5,000.00, net_after_commission=4,250.00",
                    "    COL->>CBS: Post recovery payment<br/>credit LN-2026-045, -5,000.00 GBP",
                    "    CBS-->>COL: Posted, balance=10,000.00 GBP",
                    "    COL->>COL: Recalculate position<br/>outstanding=10,000, status=With_Agency",
                ],
                "integrations": [
                    ("Late Recovery", "Escalation", "EscalateToRecovery", "Collections (FICO Debt Manager)", "Collections (FICO Debt Manager)", "Internal", "Internal", "Event-driven", "Medium"),
                    ("Late Recovery", "Legal", "InstructLegalProceedings", "Collections (FICO Debt Manager)", "Legal Case Mgmt (Pega)", "FICO REST API", "Pega REST API (OAuth2)", "Event-driven", "High"),
                    ("Late Recovery", "Agency", "PlaceWithExternalAgency", "Collections (FICO Debt Manager)", "Agency Portal (Experian Collections)", "FICO API", "Experian API (SOAP)", "API-led (Real-time)", "High"),
                    ("Late Recovery", "Payment", "PostRecoveryPayment", "Collections (FICO Debt Manager)", "Core Banking (Temenos Transact)", "FICO REST API", "Temenos REST API (API Key)", "Event-driven", "Medium"),
                ],
                "acceptance": [
                    ("Late Recovery", "Escalation", "Account escalated to recovery team at correct DPD threshold with full history", "Escalation triggered at DPD>=90; full payment/contact history included; priority assigned"),
                    ("Late Recovery", "Legal", "Legal proceedings initiated with proper documentation and court filing", "Claim filed within 5 working days of instruction; all evidence attached; court fee accounted"),
                    ("Late Recovery", "Agency", "Account placed with external agency with correct commission structure", "Agency accepts within 24hrs; data shared securely; regulatory compliance maintained"),
                    ("Late Recovery", "Payment", "Recovery payment posted correctly net of agency commission/fees", "Payment allocated correctly; commission deducted per agreement; balance updated"),
                ],
            },
            "12.3 Restructuring & Forbearance": {
                "description": "Customer facing financial difficulty requests forbearance. Bank assesses eligibility, offers restructuring options (payment holiday, term extension, rate reduction), monitors cure.",
                "actors": "Customer, Collections Officer, Credit Risk Analyst, Underwriter",
                "systems": "Collections System (FICO Debt Manager), Decision Engine (FICO), Core Banking (Temenos Transact), CRM (Salesforce Financial Services), Document Mgmt (M-Files)",
                "mermaid": [
                    "    participant C as Customer<br/>(Alice Johnson)",
                    "    participant COL as Collections<br/>(FICO Debt Manager)",
                    "    participant DE as Decision Engine<br/>(FICO)",
                    "    participant CBS as Core Banking<br/>(Temenos Transact)",
                    "    participant CRM as CRM<br/>(Salesforce Financial Svcs)",
                    "    participant DOC as Document Mgmt<br/>(M-Files)",
                    "    C->>COL: Request forbearance<br/>hardship=Loss of income, account=LN-2026-042",
                    "    COL->>CBS: Verify hardship<br/>review transaction history, income profile",
                    "    CBS-->>COL: Income reduced 40%<br/>employed part-time",
                    "    COL->>DE: Assess restructuring<br/>customer=CUST-2026-001, loan=LN-2026-042",
                    "    DE->>DE: Affordability model<br/>DTI=55%, reduced_income=2,500 GBP/m",
                    "    DE-->>COL: Options available<br/>1: holiday 3m, 2: extend to 96m, 3: reduce rate",
                    "    COL->>C: Present options<br/>payment holiday, extend term, mix",
                    "    C->>COL: Select option 2<br/>extend term to 96 months, rate=4.5%",
                    "    COL->>CBS: Modify loan terms<br/>LN-2026-042, new_term=96, new_rate=4.5%",
                    "    CBS-->>COL: Terms modified<br/>new_payment=295.00 GBP/month",
                    "    COL->>DOC: Store forbearance agreement<br/>signed digital document",
                    "    DOC-->>COL: Agreement stored",
                    "    COL->>CRM: Log forbearance<br/>type=Term Extension, status=Active",
                    "    COL->>C: Confirmation<br/>new terms effective, payment=295.00 GBP",
                    "    COL->>COL: Set monitoring<br/>next_review=90 days, cure triggers",
                    "    CBS->>COL: Payment received<br/>295.00 GBP, on time, month 1 of 96",
                    "    COL->>COL: Update status<br/>forbearance_active, compliant",
                ],
                "integrations": [
                    ("Restructuring", "Request", "RequestForbearance", "Customer Portal (Digital Banking)", "Collections (FICO Debt Manager)", "Backbase REST API", "FICO API (SOAP)", "API-led (Real-time)", "Medium"),
                    ("Restructuring", "Assessment", "AssessRestructuringOptions", "Collections (FICO Debt Manager)", "Decision Engine (FICO)", "FICO API", "FICO Blaze API (REST)", "API-led (Real-time)", "High"),
                    ("Restructuring", "Modification", "ModifyLoanTerms", "Collections (FICO Debt Manager)", "Core Banking (Temenos Transact)", "FICO REST API", "Temenos REST API (API Key)", "API-led (Real-time)", "High"),
                    ("Restructuring", "Documentation", "StoreForbearanceAgreement", "Collections (FICO Debt Manager)", "Document Mgmt (M-Files)", "FICO REST API", "M-Files REST API (API Key)", "Event-driven", "Simple"),
                    ("Restructuring", "Monitoring", "MonitorForbearanceCompliance", "Collections (FICO Debt Manager)", "Collections (FICO Debt Manager)", "Internal", "Internal", "Batch (Scheduled)", "Medium"),
                ],
                "acceptance": [
                    ("Restructuring", "Request", "Customer submits forbearance request with hardship details via digital channel", "Request acknowledged within 24hrs; hardship evidence submitted; income/expense collected"),
                    ("Restructuring", "Assessment", "Restructuring options assessed based on affordability and risk model", "Options generated: payment holiday, term extension, rate reduction; DTI model accurate"),
                    ("Restructuring", "Modification", "Loan terms modified in core banking with correct repayment schedule", "All terms updated; new schedule generated; system prevents overlapping forbearance"),
                    ("Restructuring", "Documentation", "Forbearance agreement stored with digital signature", "Document signed and stored; terms visible to customer; regulatory disclosure provided"),
                    ("Restructuring", "Monitoring", "Forbearance compliance monitored monthly; cure triggers defined", "Payments tracked; missed payment triggers re-evaluation; cure resets loan to original terms"),
                ],
            },
        },
    },
}

# ─── ADDITIONAL BIAN CAPABILITIES ────────────────────────────────────────────────

NEW_BIAN_CAPABILITIES = [
    ("Products", "Wealth Management", "BC074", "Manage client investment portfolios, financial planning, and advisory services"),
    ("Products", "Asset Management", "BC075", "Manage institutional assets, fund management, and investment strategies"),
    ("Operations", "Collections & Recovery", "BC077", "Manage debt collection, recovery, forbearance, and charged-off accounts"),
]

NEW_SECTION_CAPABILITIES = {
    "Trade Finance": ["BC063"],
    "Wealth Management": ["BC074", "BC075"],
    "Contact Center": ["BC002", "BC034"],
    "Collections & Recovery": ["BC077"],
}


def count_section(section_name, current_lines):
    """Count existing section occurrences in README."""
    count = 0
    for line in current_lines:
        if line.strip().startswith("# ") and not line.strip().startswith("##"):
            if section_name.lower().replace(" & ", " & ") in line.lower():
                count += 1
    return count


def print_summary():
    """Print a detailed summary of what the expansion would add."""
    print("=" * 70)
    print("  BANKING DOMAIN README EXPANSION - PLAN SUMMARY")
    print("=" * 70)

    # Count existing content
    current_text = README.read_text(encoding="utf-8") if README.exists() else ""
    current_lines = current_text.split("\n")

    # Sections
    current_sections = sum(1 for l in current_lines if l.strip().startswith("# ") and not l.strip().startswith("##"))
    current_subflows = sum(1 for l in current_lines if l.strip().startswith("### ") and not l.strip().startswith("####"))
    current_integration_rows = current_text.count("|------|--------|-----------|--------|--------|-------------|-------------|---------|------------|")
    current_ac_rows = current_text.count("|------|--------|---------------------|------------------|")
    current_test_entities = len(set(
        line.split("|")[1].strip().strip("**") 
        for line in current_lines 
        if "**" in line and "|" in line and not line.strip().startswith("|") 
        and current_text.index(line) < current_text.index("## Table of Contents") 
        if "## Table of Contents" in current_text
    )) if current_text else 0
    # Simpler count: current defined entities
    current_test_ent_count = 13  # known from analysis

    # ── Count what we add ──
    new_test_entities = len(NEW_TEST_DATA)
    total_test_entities = current_test_ent_count + new_test_entities

    # Extra integration rows for existing sub-flows
    extra_int_count = sum(len(v) for v in EXTRA_INTEGRATIONS.values())
    # Extra acceptance criteria rows for existing sub-flows
    extra_ac_count = sum(len(v) for v in EXTRA_ACCEPTANCE.values())

    # New sub-flows in existing sections
    new_subflows_existing = len(NEW_SUBFLOWS)
    new_int_existing = sum(len(v["integrations"]) for v in NEW_SUBFLOWS.values())
    new_ac_existing = sum(len(v["acceptance"]) for v in NEW_SUBFLOWS.values())

    # New sections
    new_sections_count = len(NEW_SECTIONS)
    new_section_subflows = sum(len(v["subflows"]) for v in NEW_SECTIONS.values())
    new_section_int = sum(
        sum(len(sf["integrations"]) for sf in sec["subflows"].values())
        for sec in NEW_SECTIONS.values()
    )
    new_section_ac = sum(
        sum(len(sf["acceptance"]) for sf in sec["subflows"].values())
        for sec in NEW_SECTIONS.values()
    )

    # Totals
    total_new_subflows = new_subflows_existing + new_section_subflows
    total_new_int = extra_int_count + new_int_existing + new_section_int
    total_new_ac = extra_ac_count + new_ac_existing + new_section_ac

    current_int_count = current_integration_rows  # each Integration Details table header
    current_ac_count = current_ac_rows

    # We need actual row counts for integration and acceptance from existing
    # Integration rows per table (from the data): let's count from the README
    existing_int_rows = 93  # known from analysis
    existing_ac_rows = current_subflows  # each subflow has AC rows, but not all subflows have AC
    # Actually, we know from add_acceptance_criteria.py that there are 24 sub-flows with AC
    existing_ac_row_count = sum(len(v) for v in [  # from add_acceptance_criteria.py
        [1]*4,[1]*4,[1]*4,[1]*4,[1]*4,[1]*4,[1]*4,[1]*4,[1]*4,[1]*5,[1]*4,[1]*3,[1]*3,[1]*3,
        [1]*3,[1]*4,[1]*4,[1]*4,[1]*4,[1]*4,[1]*4,[1]*4,[1]*4,[1]*4,
    ])
    # Actually let me count properly:
    # 4 rows each: 20 sub-flows = 80
    # 5 rows: 4.2 = 5
    # 3 rows: 5.1, 5.2, 5.3, 6.1 = 12
    # Total = 80 + 5 + 12 = 97
    existing_ac_row_count = 97

    print(f"\n  CURRENT STATE:")
    print(f"    Sections:            {current_sections}")
    print(f"    Sub-flows:           {current_subflows}")
    print(f"    Integration rows:    {existing_int_rows}")
    print(f"    Acceptance criteria: {existing_ac_row_count}")
    print(f"    Test data entities:  {current_test_ent_count}")
    print(f"    BIAN codes:          26")

    print(f"\n  ADDITIONS:")
    print(f"    New test entities:     +{new_test_entities}  ({current_test_ent_count} -> {total_test_entities})")
    print(f"    Extra int. rows:       +{extra_int_count}  (to existing sub-flows)")
    print(f"    Extra AC rows:         +{extra_ac_count}  (to existing sub-flows)")
    print(f"    New sub-flows (exist):  +{new_subflows_existing}  (2.4, 3.4, 4.4, 5.4)")
    print(f"    New sections:           +{new_sections_count}  (9-12)")
    print(f"    New sub-flows (new):    +{new_section_subflows}")
    print(f"    New BIAN capabilities:  +{len(NEW_BIAN_CAPABILITIES)}")

    print(f"\n  SUBFLOW DETAIL:")
    total_subflows = current_subflows + total_new_subflows
    print(f"    Total sub-flows:       {total_subflows}  (target: 40+)")

    total_int = existing_int_rows + total_new_int
    print(f"    Total integration:     {total_int}  (target: 180+)")

    total_ac = existing_ac_row_count + total_new_ac
    print(f"    Total acceptance:      {total_ac}  (target: 180+)")

    print(f"    Total test entities:   {total_test_entities}  (target: 30+)")
    print(f"    Total sections:        {current_sections + new_sections_count}  (target: 12)")

    print(f"\n  NEW TEST DATA ENTITIES:")
    for i, name in enumerate(sorted(NEW_TEST_DATA.keys()), 1):
        fields = len(NEW_TEST_DATA[name])
        print(f"    {i:2d}. {name}  ({fields} fields)")

    print(f"\n  NEW SUB-FLOWS IN EXISTING SECTIONS:")
    for sf_id, data in NEW_SUBFLOWS.items():
        sec = data["section"]
        ints = len(data["integrations"])
        acs = len(data["acceptance"])
        mermaid_steps = len(data["mermaid"])
        print(f"    {sf_id}  [{sec}]  ({ints} ints, {acs} AC, {mermaid_steps} diagram steps)")

    print(f"\n  NEW SECTIONS & SUB-FLOWS:")
    for sec_key, sec_data in NEW_SECTIONS.items():
        sf_count = len(sec_data["subflows"])
        print(f"    {sec_key} - {sf_count} sub-flows")
        for sf_id, sf_data in sec_data["subflows"].items():
            ints = len(sf_data["integrations"])
            acs = len(sf_data["acceptance"])
            mermaid_steps = len(sf_data["mermaid"])
            print(f"      +- {sf_id}  ({ints} ints, {acs} AC, {mermaid_steps} diagram steps)")

    print(f"\n  SUMMARY TABLE:")
    print(f"    {'Metric':<35} {'Current':>8} {'Added':>8} {'Total':>8} {'Target':>8}")
    print(f"    {'-'*35} {'-'*8} {'-'*8} {'-'*8} {'-'*8}")
    print(f"    {'Sections':<35} {current_sections:>8} {new_sections_count:>8} {current_sections + new_sections_count:>8} {'12':>8}")
    print(f"    {'Sub-flows':<35} {current_subflows:>8} {total_new_subflows:>8} {total_subflows:>8} {'40+':>8}")
    print(f"    {'Integration rows':<35} {existing_int_rows:>8} {total_new_int:>8} {total_int:>8} {'180+':>8}")
    print(f"    {'Acceptance criteria':<35} {existing_ac_row_count:>8} {total_new_ac:>8} {total_ac:>8} {'180+':>8}")
    print(f"    {'Test data entities':<35} {current_test_ent_count:>8} {new_test_entities:>8} {total_test_entities:>8} {'30+':>8}")
    print(f"    {'BIAN capability codes':<35} {'26':>8} {len(NEW_BIAN_CAPABILITIES):>8} {26 + len(NEW_BIAN_CAPABILITIES):>8} {'-':>8}")

    print(f"\n  STATUS: This script defines all expansion data structures.")
    print(f"  It does NOT modify README.md. Review data above, then execute.")
    print("=" * 70)


def build_bian_section(bian_caps, section_cap_map):
    """Build the BIAN capability model reference section."""
    lines = []
    lines.append("## BIAN Capability Model Reference")
    lines.append("")
    lines.append("The BIAN (Banking Industry Architecture Network) Capability Model defines the standard business capabilities for banking institutions. The table below lists all relevant capabilities grouped by domain. Each process flow in this document is mapped to its relevant BIAN capability codes.")
    lines.append("")

    groups = {}
    for l1, l2, code, desc in bian_caps:
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


def format_integration_table(rows):
    """Format integration details as markdown table."""
    lines = []
    lines.append("#### Integration Details")
    lines.append("")
    lines.append("| Flow | Entity | Info Flow | Source | Target | Source Conn | Target Conn | Pattern | Complexity |")
    lines.append("|------|--------|-----------|--------|--------|-------------|-------------|---------|------------|")
    for row in rows:
        escaped = [str(c).replace("|", "\\|") for c in row]
        lines.append(f"| {' | '.join(escaped)} |")
    lines.append("")
    return "\n".join(lines)


def format_acceptance_table(rows):
    """Format acceptance criteria as markdown table."""
    lines = []
    lines.append("#### Acceptance Criteria")
    lines.append("")
    lines.append("| Flow | Entity | Acceptance Criterion | Expected Outcome |")
    lines.append("|------|--------|---------------------|------------------|")
    for flow_name, entity, criterion, outcome in rows:
        criterion_esc = criterion.replace("|", "\\|")
        outcome_esc = outcome.replace("|", "\\|")
        lines.append(f"| {flow_name} | {entity} | {criterion_esc} | {outcome_esc} |")
    lines.append("")
    return "\n".join(lines)


def format_mermaid(steps):
    """Format mermaid sequence diagram."""
    lines = []
    lines.append("```mermaid")
    lines.append("sequenceDiagram")
    for step in steps:
        lines.append(step)
    lines.append("```")
    return "\n".join(lines)


def format_subflow(sf_id, sf_data):
    """Format a complete sub-flow section."""
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
    lines.append(format_mermaid(sf_data["mermaid"]))
    lines.append("")
    lines.append(format_integration_table(sf_data["integrations"]))
    lines.append("")
    lines.append(format_acceptance_table(sf_data["acceptance"]))
    return "\n".join(lines)


def format_new_section(sec_key, sec_data):
    """Format a complete new section with all sub-flows."""
    lines = []
    lines.append(f"# {sec_key}")
    lines.append("")
    lines.append(sec_data["description"])
    lines.append("")
    for sf_id, sf_data in sec_data["subflows"].items():
        lines.append(format_subflow(sf_id, sf_data))
        lines.append("")
        lines.append("---")
        lines.append("")
    return "\n".join(lines)


if __name__ == "__main__":
    print_summary()
