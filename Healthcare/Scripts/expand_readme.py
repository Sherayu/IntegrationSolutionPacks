"""Expansion data for Healthcare domain README.md.
Targets: 10 sections, 30+ sub-flows, 100+ integration rows, 30+ test entities.
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# ─── NEW TEST ENTITIES ─────────────────────────────────────────────

NEW_TEST_DATA = {
    "Encounter": [
        ("encounter_id", "ENC-2026-001"),
        ("type", "Inpatient"),
        ("start_date", "2026-06-15"),
        ("end_date", "2026-06-18"),
        ("patient_id", "PT-2026-001"),
        ("provider_id", "PROV-101"),
    ],
    "Order": [
        ("order_id", "ORD-2026-001"),
        ("type", "Lab"),
        ("status", "Active"),
        ("patient_id", "PT-2026-001"),
        ("ordering_provider", "PROV-101"),
    ],
    "Observation": [
        ("observation_id", "OBS-2026-001"),
        ("type", "Blood Glucose"),
        ("value", "98"),
        ("unit", "mg/dL"),
        ("status", "Final"),
        ("patient_id", "PT-2026-001"),
    ],
    "Medication": [
        ("med_id", "MED-2026-001"),
        ("name", "Metformin 500mg"),
        ("dose", "500mg"),
        ("route", "Oral"),
        ("frequency", "BID"),
        ("patient_id", "PT-2026-001"),
    ],
    "Claim": [
        ("claim_id", "CLM-2026-001"),
        ("type", "Professional"),
        ("amount", "1250.00"),
        ("status", "Submitted"),
        ("patient_id", "PT-2026-001"),
        ("payer_id", "PAYER-001"),
    ],
    "Appointment": [
        ("appt_id", "APT-2026-001"),
        ("type", "Office Visit"),
        ("date", "2026-07-10"),
        ("status", "Scheduled"),
        ("patient_id", "PT-2026-001"),
        ("provider_id", "PROV-101"),
    ],
    "CarePlan": [
        ("careplan_id", "CP-2026-001"),
        ("type", "Diabetes Management"),
       ("status", "Active"),
        ("patient_id", "PT-2026-001"),
        ("start_date", "2026-06-01"),
    ],
    "Location": [
        ("location_id", "LOC-001"),
        ("name", "Main Hospital - Floor 3"),
        ("type", "Inpatient Ward"),
        ("capacity", "30"),
    ],
    "Insurance": [
        ("insurance_id", "INS-001"),
        ("payer_name", "Blue Cross Blue Shield"),
        ("plan_type", "PPO"),
        ("member_id", "MBR-2026-001"),
        ("group_num", "GRP-7890"),
        ("patient_id", "PT-2026-001"),
    ],
    "LabResult": [
        ("lab_result_id", "LR-2026-001"),
        ("test_name", "CBC"),
        ("result", "Normal"),
        ("collected_date", "2026-06-15"),
        ("resulted_date", "2026-06-16"),
        ("order_id", "ORD-2026-001"),
    ],
    "ImagingStudy": [
        ("study_id", "IMG-2026-001"),
        ("modality", "X-Ray"),
        ("body_part", "Chest"),
        ("status", "Completed"),
        ("patient_id", "PT-2026-001"),
    ],
    "Immunization": [
        ("imm_id", "IMM-2026-001"),
        ("vaccine", "Influenza"),
        ("dose", "0.5mL"),
        ("admin_date", "2026-09-01"),
        ("patient_id", "PT-2026-001"),
    ],
    "Consent": [
        ("consent_id", "CON-2026-001"),
        ("type", "Treatment Consent"),
        ("status", "Signed"),
        ("signed_date", "2026-06-10"),
        ("patient_id", "PT-2026-001"),
    ],
    "Referral": [
        ("referral_id", "REF-2026-001"),
        ("type", "Specialist"),
        ("from_provider", "PROV-101"),
        ("to_specialty", "Cardiology"),
        ("status", "Pending"),
        ("patient_id", "PT-2026-001"),
    ],
    "SupplyItem": [
        ("item_id", "SUP-2026-001"),
        ("name", "Surgical Gloves - Box"),
        ("category", "PPE"),
        ("quantity", "500"),
        ("reorder_level", "100"),
    ],
    "Incident": [
        ("incident_id", "INC-2026-001"),
        ("type", "Medication Error"),
        ("severity", "Moderate"),
        ("status", "Investigating"),
        ("patient_id", "PT-2026-001"),
    ],
    "QualityMeasure": [
        ("measure_id", "QM-2026-001"),
        ("name", "Diabetes HbA1c Control"),
        ("type", "HEDIS"),
        ("score", "85.5"),
        ("reporting_period", "2026-Q2"),
    ],
    "Allergy": [
        ("allergy_id", "ALG-2026-001"),
        ("substance", "Penicillin"),
        ("reaction", "Rash"),
        ("severity", "Moderate"),
        ("patient_id", "PT-2026-001"),
    ],
    "Provider": [
        ("provider_id", "PROV-101"),
        ("name", "Dr. Sarah Williams"),
        ("specialty", "Internal Medicine"),
        ("npi", "1234567890"),
        ("department", "Medicine"),
    ],
    "Patient": [
        ("patient_id", "PT-2026-001"),
        ("name", "John Doe"),
        ("dob", "1985-04-12"),
        ("mrn", "MRN-2026-0001"),
        ("gender", "Male"),
        ("phone", "555-0100"),
    ],
}

# ─── SECTION CAPABILITY MAP ─────────────────────────────────────────

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

# ─── EXTRA INTEGRATIONS BY SUB-FLOW ─────────────────────────────────

EXTRA_INTEGRATIONS = {
    "1.1 Patient Registration & Demographics": [
        ("Patient Registration", "Guarantor", "AddGuarantor", "Admissions (Epic)", "Revenue Cycle (Epic)", "Epic REST API (FHIR)", "Epic REST API (FHIR)", "API-led (Real-time)", "Simple"),
        ("Patient Registration", "NextOfKin", "AddNextOfKin", "Admissions (Epic)", "Admissions (Epic)", "Epic REST API (FHIR)", "Epic REST API (FHIR)", "API-led (Real-time)", "Simple"),
    ],
    "1.2 Patient Identity & MPI Management": [
        ("Identity Management", "Patient", "MergeDuplicate", "Enterprise Master Patient Index (Rhapsody EMPI)", "EHR (Epic)", "EMPI SOAP API", "Epic REST API (FHIR)", "Event-driven", "High"),
        ("Identity Management", "Patient", "CrossReference", "Enterprise Master Patient Index (Rhapsody EMPI)", "External MPI (Community MPI)", "EMPI SOAP API", "Community MPI SOAP", "Batch (Scheduled)", "Medium"),
    ],
    "2.1 Clinical Notes & H&P Documentation": [
        ("Clinical Notes", "Encounter", "SignNote", "EHR (Epic)", "Clinical Data Repository (CDR)", "Epic REST API (FHIR)", "CDR JDBC", "Database Replication (CDC)", "Medium"),
        ("Clinical Notes", "Encounter", "Addendum", "EHR (Epic)", "EHR (Epic)", "Epic REST API (FHIR)", "Epic REST API (FHIR)", "API-led (Real-time)", "Simple"),
    ],
    "3.1 Lab Order & Specimen Collection": [
        ("Lab Order", "Specimen", "CollectSpecimen", "Phlebotomy (BD Pyxis)", "LIS (Cerner Lab)", "BD Pyxis API", "LIS HL7 v2.5.1", "Event-driven", "Medium"),
        ("Lab Order", "Order", "CancelOrder", "CPOE (Epic)", "LIS (Cerner Lab)", "Epic REST API (FHIR)", "LIS HL7 v2.5.1", "API-led (Real-time)", "Simple"),
    ],
    "4.1 Medication Ordering & Reconciliation": [
        ("Med Order", "Medication", "FormularyCheck", "CPOE (Epic)", "Pharmacy System (BD Pyxis)", "Epic REST API (FHIR)", "Pyxis REST API", "API-led (Real-time)", "Medium"),
        ("Med Order", "Medication", "Reconcile", "EHR (Epic)", "Pharmacy System (BD Pyxis)", "Epic REST API (FHIR)", "Pyxis REST API", "Batch (Scheduled)", "High"),
    ],
    "5.1 Charge Capture & Coding": [
        ("Charge Capture", "Encounter", "ValidateCoding", "Revenue Cycle (Epic)", "Coding Workflow (3M 360)", "Epic REST API", "3M REST API", "API-led (Real-time)", "Medium"),
        ("Charge Capture", "Claim", "AuditCharge", "Revenue Cycle (Epic)", "Compliance System (Cerner)", "Epic REST API", "Cerner SOAP", "Batch (Scheduled)", "Medium"),
    ],
    "6.1 Patient Scheduling & Check-in": [
        ("Scheduling", "Appointment", "WaitlistManage", "Scheduling (Epic Cadence)", "Scheduling (Epic Cadence)", "Epic REST API (FHIR)", "Epic REST API (FHIR)", "API-led (Real-time)", "Simple"),
        ("Scheduling", "Patient", "SelfCheckin", "Patient Portal (MyChart)", "Scheduling (Epic Cadence)", "MyChart REST API", "Epic REST API (FHIR)", "API-led (Real-time)", "Medium"),
    ],
    "7.1 Care Plan Development & Management": [
        ("Care Plan", "Goal", "UpdateGoal", "Care Management (Cerner)", "EHR (Epic)", "Cerner REST API", "Epic REST API (FHIR)", "API-led (Real-time)", "Medium"),
        ("Care Plan", "CarePlan", "SharePlan", "Care Management (Cerner)", "Patient Portal (MyChart)", "Cerner REST API", "MyChart REST API", "API-led (Real-time)", "Simple"),
    ],
    "8.1 HIE Document Sharing & Query": [
        ("HIE", "Document", "SubscribeToAlerts", "HIE (HealthShare)", "EHR (Epic)", "HealthShare REST API", "Epic REST API (FHIR)", "Event-driven", "Medium"),
        ("HIE", "Patient", "QueryExternal", "HIE (HealthShare)", "External HIE (State HIE)", "HealthShare REST API", "State HIE SOAP", "API-led (Real-time)", "High"),
    ],
    "9.1 Medical Supply Procurement": [
        ("Procurement", "PurchaseOrder", "ApprovePO", "Procurement (Workday)", "Finance ERP (Oracle EBS)", "Workday REST API", "Oracle EBS SOAP", "API-led (Real-time)", "Medium"),
    ],
    "10.1 Quality Measure Reporting (HEDIS/MIPS)": [
        ("Quality", "Measure", "ValidateMeasure", "Quality Analytics (Cerner HealtheIntent)", "Registry (NCQA)", "Cerner REST API", "NCQA SFTP", "Batch (Scheduled)", "High"),
        ("Quality", "Patient", "AttestMeasure", "EHR (Epic)", "Quality Analytics (Cerner HealtheIntent)", "Epic REST API (FHIR)", "Cerner REST API", "Batch (ETL)", "Medium"),
    ],
}

# ─── ACCEPTANCE CRITERIA BY SUB-FLOW ────────────────────────────────

ACCEPTANCE_CRITERIA = {
    "1.1 Patient Registration & Demographics": [
        ("AC-1.1-01", "Data integrity: Patient demographic data transferred from Admissions to MPI via RegisterPatient must be complete and consistent", "RegisterPatient", "Patient records in MPI match source; no data loss; reconciliation report confirms accuracy", "Critical"),
        ("AC-1.1-02", "Data integrity: Insurance data transferred from Admissions to Revenue Cycle via AddInsurance must be complete and consistent", "AddInsurance", "Insurance records in Revenue Cycle match source; no data loss; reconciliation report confirms accuracy", "High"),
        ("AC-1.1-03", "Data integrity: Consent data transferred from Patient Portal to EHR via CaptureConsent must be complete and consistent", "CaptureConsent", "Consent records in EHR match source; no data loss; reconciliation report confirms accuracy", "High"),
        ("AC-1.1-04", "Error handling: Failed transactions between Admissions and MPI are logged with error context and trigger automatic retry or alert", "RegisterPatient", "Errors logged with timestamp, HTTP status, request payload excerpt; retry up to 3 times; alert sent after consecutive failures", "Critical"),
        ("AC-1.1-05", "Security: All endpoints enforce authentication and encrypt data in transit via TLS 1.2+", "All flows", "Unauthenticated requests rejected with 401; tokens validated per call; invalid/expired tokens logged", "Critical"),
    ],
    "1.2 Patient Identity & MPI Management": [
        ("AC-1.2-01", "Data integrity: Patient identity data transferred from Admissions to EMPI via CreateOrMatchPatient must be complete and consistent", "CreateOrMatchPatient", "Patient records in EMPI match source; no data loss; reconciliation report confirms accuracy", "Critical"),
        ("AC-1.2-02", "Data integrity: Consolidated patient data transferred from EMPI to EHR via PushConsolidated must be complete and consistent", "PushConsolidated", "Patient records in EHR match EMPI source; no data loss; reconciliation report confirms accuracy", "Critical"),
        ("AC-1.2-03", "Error handling: Failed identity matching transactions are logged with error context and trigger manual review or alert", "CreateOrMatchPatient", "Errors logged with timestamp, match score, request payload; manual review queue populated", "Critical"),
    ],
    "2.1 Clinical Notes & H&P Documentation": [
        ("AC-2.1-01", "Data integrity: Clinical note data transferred from EHR to CDR via StoreNote must be complete and consistent", "StoreNote", "Clinical notes in CDR match source; no data loss; reconciliation report confirms accuracy", "Critical"),
        ("AC-2.1-02", "Data integrity: Signed note data transferred from EHR to CDR via SignNote must be complete and consistent", "SignNote", "Signed notes in CDR match source; no data loss; reconciliation report confirms accuracy", "High"),
        ("AC-2.1-03", "Error handling: Failed clinical note storage transactions are logged with error context and trigger automatic retry or alert", "StoreNote", "Errors logged with timestamp, HTTP status, request payload excerpt; retry up to 3 times; alert sent after consecutive failures", "Critical"),
    ],
    "3.1 Lab Order & Specimen Collection": [
        ("AC-3.1-01", "Data integrity: Lab order data transferred from CPOE to LIS via PlaceOrder must be complete and consistent", "PlaceOrder", "Lab orders in LIS match source; no data loss; reconciliation report confirms accuracy", "Critical"),
        ("AC-3.1-02", "Data integrity: Order status updates transferred from LIS to EHR via UpdateOrderStatus must be complete and consistent", "UpdateOrderStatus", "Order status in EHR matches LIS source; no data loss; reconciliation report confirms accuracy", "High"),
        ("AC-3.1-03", "Error handling: Failed lab order transactions are logged with error context and trigger automatic retry or alert", "PlaceOrder", "Errors logged with timestamp, HTTP status, request payload excerpt; retry up to 3 times; alert sent after consecutive failures", "Critical"),
    ],
    "4.1 Medication Ordering & Reconciliation": [
        ("AC-4.1-01", "Data integrity: Medication order data transferred from CPOE to Pharmacy via PlaceMedOrder must be complete and consistent", "PlaceMedOrder", "Medication orders in Pharmacy match source; no data loss; reconciliation report confirms accuracy", "Critical"),
        ("AC-4.1-02", "Data integrity: Interaction check results transferred from Pharmacy to CPOE via CheckInteractions must be complete and consistent", "CheckInteractions", "Interaction check results in CPOE match source; no data loss; reconciliation report confirms accuracy", "Critical"),
        ("AC-4.1-03", "Error handling: Failed medication order transactions are logged with error context and trigger automatic retry or alert", "PlaceMedOrder", "Errors logged with timestamp, HTTP status, request payload excerpt; retry up to 3 times; alert sent after consecutive failures", "Critical"),
    ],
    "5.1 Charge Capture & Coding": [
        ("AC-5.1-01", "Data integrity: Charge data transferred from EHR to Revenue Cycle via CaptureCharge must be complete and consistent", "CaptureCharge", "Charge records in Revenue Cycle match source; no data loss; reconciliation report confirms accuracy", "Critical"),
        ("AC-5.1-02", "Data integrity: Coding data transferred from Coding Workflow to Claim via SubmitCoding must be complete and consistent", "SubmitCoding", "Coding records in Claim match source; no data loss; reconciliation report confirms accuracy", "High"),
        ("AC-5.1-03", "Error handling: Failed charge capture transactions are logged with error context and trigger automatic retry or alert", "CaptureCharge", "Errors logged with timestamp, HTTP status, request payload excerpt; retry up to 3 times; alert sent after consecutive failures", "Critical"),
    ],
    "6.1 Patient Scheduling & Check-in": [
        ("AC-6.1-01", "Data integrity: Appointment data transferred from Scheduling to Patient Portal via ScheduleAppt must be complete and consistent", "ScheduleAppt", "Appointment records in Patient Portal match source; no data loss; reconciliation report confirms accuracy", "Medium"),
        ("AC-6.1-02", "Data integrity: Check-in data transferred from Patient Portal to EHR via CheckInPatient must be complete and consistent", "CheckInPatient", "Check-in records in EHR match source; no data loss; reconciliation report confirms accuracy", "High"),
        ("AC-6.1-03", "Error handling: Failed scheduling transactions are logged with error context and trigger automatic retry or alert", "ScheduleAppt", "Errors logged with timestamp, HTTP status, request payload excerpt; retry up to 3 times; alert sent after consecutive failures", "High"),
    ],
    "7.1 Care Plan Development & Management": [
        ("AC-7.1-01", "Data integrity: Care Plan data transferred from Care Management to EHR via CreateCarePlan must be complete and consistent", "CreateCarePlan", "Care Plan records in EHR match source; no data loss; reconciliation report confirms accuracy", "High"),
        ("AC-7.1-02", "Data integrity: Goal progress data transferred from EHR to Care Management via UpdateGoalProgress must be complete and consistent", "UpdateGoalProgress", "Goal progress records in Care Management match source; no data loss; reconciliation report confirms accuracy", "Medium"),
        ("AC-7.1-03", "Error handling: Failed care plan transactions are logged with error context and trigger automatic retry or alert", "CreateCarePlan", "Errors logged with timestamp, HTTP status, request payload excerpt; retry up to 3 times; alert sent after consecutive failures", "High"),
    ],
    "8.1 HIE Document Sharing & Query": [
        ("AC-8.1-01", "Data integrity: Document data transferred from EHR to HIE via PublishDocument must be complete and consistent", "PublishDocument", "Document records in HIE match source; no data loss; reconciliation report confirms accuracy", "Critical"),
        ("AC-8.1-02", "Data integrity: Query results transferred from HIE to EHR via QueryHIE must be complete and consistent", "QueryHIE", "Query results in EHR match source; no data loss; reconciliation report confirms accuracy", "High"),
        ("AC-8.1-03", "Security: All endpoints enforce authentication (HIE REST API (IHE XCA), Epic REST API (FHIR), ...) and encrypt data in transit via TLS 1.2+", "All flows", "Unauthenticated requests rejected with 401; tokens validated per call; invalid/expired tokens logged", "Critical"),
    ],
    "9.1 Medical Supply Procurement": [
        ("AC-9.1-01", "Data integrity: Purchase Order data transferred from Procurement to Finance via CreatePO must be complete and consistent", "CreatePO", "Purchase Order records in Finance match source; no data loss; reconciliation report confirms accuracy", "High"),
        ("AC-9.1-02", "Error handling: Failed procurement transactions are logged with error context and trigger automatic retry or alert", "CreatePO", "Errors logged with timestamp, HTTP status, request payload excerpt; retry up to 3 times; alert sent after consecutive failures", "High"),
    ],
    "10.1 Quality Measure Reporting (HEDIS/MIPS)": [
        ("AC-10.1-01", "Data integrity: Quality measure data transferred from EHR to Quality Analytics via SubmitMeasureData must be complete and consistent", "SubmitMeasureData", "Quality measure records in Quality Analytics match source; no data loss; reconciliation report confirms accuracy", "Critical"),
        ("AC-10.1-02", "Data integrity: Report data transferred from Quality Analytics to Registry via SubmitReport must be complete and consistent", "SubmitReport", "Report records in Registry match source; no data loss; reconciliation report confirms accuracy", "High"),
        ("AC-10.1-03", "Error handling: Failed quality measure reporting transactions are logged with error context and trigger automatic retry or alert", "SubmitMeasureData", "Errors logged with timestamp, HTTP status, request payload excerpt; retry up to 3 times; alert sent after consecutive failures", "Critical"),
    ],
}

# ─── NEW SECTIONS FOR FUTURE EXPANSION ──────────────────────────────

NEW_SECTIONS = {}
