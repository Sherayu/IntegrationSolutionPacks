"""Data definitions for Utilities domain README generation."""
from pathlib import Path
from collections import OrderedDict

ROOT = Path(__file__).resolve().parent.parent

FRAMEWORK = {
    "business_domain": "Utilities",
    "framework_name": "Common Information Model (CIM) from EPRI with IEC 61970/IEC 61850/IEC 62351/IEC 61968, OpenADR 2.0b and Green Button (NAESB REQ.21 ESPI) for Smart Grid and Metering, EPRI Utility Business Capability Model (UCBM) and TM Forum eTOM for Multi-Utilities",
    "capability_prefix": "UT",
    "generated_date": "2026-07-07",
}

CAPABILITY_MODEL = {
    "Customer & Energy Services": [
        ("Customer Information Management", "UT-CIM", "Manage customer accounts, contacts, and relationship data across utility services"),
        ("Customer Service & Support", "UT-CSS", "Handle customer inquiries, service requests, complaints, and field service coordination"),
        ("Marketing & Sales", "UT-MKT", "Plan and execute marketing campaigns, lead management, and customer acquisition"),
        ("Credit & Collections", "UT-CCL", "Manage credit risk assessment, collections, and disconnection/reconnection processes"),
    ],
    "Metering & Smart Grid": [
        ("Advanced Metering Infrastructure", "UT-AMI", "Operate AMI head-end systems, meter communications, and smart meter network"),
        ("Meter Data Management", "UT-MDM", "Validate, estimate, and edit (VEE) meter data; manage data quality and storage"),
        ("Smart Grid Operations", "UT-SGO", "Monitor and control smart grid devices, DERMS integration, and grid-edge intelligence"),
        ("Green Button Data Access", "UT-GBD", "Provide customer energy usage data via Download My Data and Connect My Data standards"),
    ],
    "Billing & Revenue Management": [
        ("Rate & Tariff Management", "UT-RTM", "Define and manage rate structures, tariffs, riders, and pricing schedules"),
        ("Billing Calculation & Presentment", "UT-BIL", "Calculate charges, apply rates, generate bills, and manage presentment"),
        ("Payment Processing", "UT-PAY", "Process payments via multiple channels, manage payment plans and deposits"),
        ("Revenue Assurance", "UT-REV", "Detect revenue leakage, audit billing accuracy, and manage write-offs"),
    ],
    "Generation Operations": [
        ("Thermal Generation Control", "UT-TGC", "Monitor and control thermal power plant operations including boiler, turbine, and generator"),
        ("Renewable Generation Management", "UT-RGM", "Manage solar, wind, and hydro generation assets including variability and forecasting"),
        ("Generator Dispatch & AGC", "UT-GDA", "Coordinate generator dispatch, automatic generation control, and load following"),
        ("Fuel Management", "UT-FMG", "Manage fuel procurement, inventory, quality, and consumption for thermal plants"),
    ],
    "Transmission Operations": [
        ("EMS Real-time Operations", "UT-EMS", "Monitor and control transmission network via energy management system SCADA"),
        ("State Estimation & Contingency", "UT-SEC", "Perform network state estimation, contingency analysis, and security assessment"),
        ("Wide Area Monitoring", "UT-WAM", "Monitor grid stability using synchrophasors, PMUs, and wide-area situational awareness"),
        ("Transmission Switching & Clearance", "UT-TSC", "Manage transmission switching orders, clearance requests, and tagging procedures"),
    ],
    "Substation Automation": [
        ("RTU & SCADA Control", "UT-RTU", "Operate remote terminal units and substation SCADA for data acquisition and control"),
        ("Protection & IED Management", "UT-PIM", "Manage protection relays, intelligent electronic devices, and fault recording"),
        ("IEC 61850 Communications", "UT-IEC", "Implement IEC 61850 GOOSE, MMS, and sampled value communications for substation automation"),
        ("Substation Security & Access", "UT-SSA", "Manage substation physical security, cyber access, and electronic security perimeters"),
    ],
    "Distribution Grid": [
        ("Distribution SCADA / ADMS", "UT-DSC", "Monitor and control distribution network via ADMS, DMS, and distribution SCADA"),
        ("DERMS & Distributed Energy", "UT-DER", "Manage distributed energy resource interconnection, dispatch, and optimization"),
        ("Fault Location & Restoration", "UT-FLR", "Detect faults, locate via FLISR, and automatically restore distribution service"),
        ("Distribution Planning & Optimization", "UT-DPO", "Plan distribution network capacity, volt/VAR optimization, and loss reduction"),
    ],
    "Water Operations": [
        ("Water Treatment Control", "UT-WTC", "Monitor and control water treatment plant processes including chemical dosing and filtration"),
        ("Water Distribution Management", "UT-WDM", "Manage water distribution network pressure zones, flow, and reservoir levels"),
        ("Wastewater Treatment Control", "UT-WWC", "Monitor and control wastewater treatment processes and effluent quality"),
        ("Water Quality Management", "UT-WQM", "Monitor water quality parameters, regulatory compliance, and sampling programs"),
    ],
    "Outage & Workforce Management": [
        ("Outage Detection & IVR", "UT-ODI", "Detect outages via AMI, SCADA, and customer calls; manage IVR outage reporting"),
        ("Damage Assessment & Switching", "UT-DAS", "Assess storm damage, perform switching orders, and isolate faulted sections"),
        ("Crew Dispatch & Restoration", "UT-CDR", "Dispatch field crews, manage mobile workforce, and track restoration progress"),
        ("Outage Analytics & Reporting", "UT-OAR", "Analyze outage duration, frequency, SAIDI/SAIFI metrics, and regulatory reporting"),
    ],
    "Asset Management": [
        ("Asset Registry & Hierarchy", "UT-ARH", "Maintain asset register, hierarchy, criticality ratings, and lifecycle status"),
        ("GIS Network Model", "UT-GIS", "Manage geographic information system network model and asset geolocation"),
        ("Condition Monitoring & IoT", "UT-CMI", "Monitor asset condition via IoT sensors, online monitoring, and predictive analytics"),
        ("Predictive Maintenance & CBM", "UT-PMC", "Plan condition-based and predictive maintenance activities for critical assets"),
    ],
    "Enterprise Resources": [
        ("Financial Management", "UT-FIN", "Manage general ledger, accounts payable/receivable, budgeting, and financial reporting"),
        ("Human Resources & Payroll", "UT-HRP", "Manage workforce planning, recruitment, time tracking, payroll, and benefits"),
        ("Procurement & Supply Chain", "UT-PSC", "Manage procurement, vendor contracts, purchase orders, and logistics"),
        ("Inventory & Warehousing", "UT-INV", "Manage materials inventory, warehouse operations, and stock replenishment"),
    ],
    "Supply Chain & Materials": [
        ("Vendor & Supplier Management", "UT-VSM", "Manage vendor qualifications, performance, contracts, and compliance"),
        ("Materials & Equipment Management", "UT-MEM", "Manage materials catalog, equipment specifications, and standardization"),
        ("Contract Lifecycle Management", "UT-CLM", "Manage contract creation, negotiation, approval, and renewal processes"),
        ("Logistics & Warehousing", "UT-LGW", "Manage inbound/outbound logistics, warehouse operations, and fleet management"),
    ],
    "Cybersecurity & Compliance": [
        ("Identity & Access Management", "UT-IAM", "Manage user identities, role-based access control, and privileged access for OT/IT"),
        ("Security Monitoring & SIEM", "UT-SSM", "Monitor security events, analyze threats, and manage security incident response"),
        ("Vulnerability & Patch Management", "UT-VPM", "Manage vulnerability scanning, patch deployment, and configuration hardening"),
        ("NERC CIP Compliance", "UT-NCC", "Manage NERC Critical Infrastructure Protection compliance, audits, and evidence"),
    ],
    "Data & Analytics": [
        ("Operational Data Lake", "UT-ODL", "Ingest and store OT/IT data via PI System, data lake, and historian platforms"),
        ("Grid Analytics & Forecasting", "UT-GAF", "Analyze grid data for load forecasting, renewable integration, and optimization"),
        ("Customer Analytics", "UT-CAN", "Analyze customer usage patterns, segmentation, and energy efficiency program targeting"),
        ("Asset Health & Predictive Analytics", "UT-AHP", "Predict asset failures, calculate remaining useful life, and optimize maintenance"),
    ],
    "Regulatory & Market Operations": [
        ("Regulatory Reporting", "UT-RRP", "Prepare and submit regulatory reports to FERC, NERC, state PUCs, and environmental agencies"),
        ("ISO/RTO Market Operations", "UT-ISO", "Participate in wholesale electricity markets, bid management, and settlement"),
        ("Environmental Compliance & Emissions", "UT-ENV", "Monitor emissions, manage environmental permits, and report compliance data"),
        ("Environmental Health & Safety", "UT-EHS", "Manage safety programs, incident reporting, industrial hygiene, and OSHA compliance"),
    ],
    "Demand Response & Energy Efficiency": [
        ("Demand Response Program Management", "UT-DRP", "Design, market, and manage demand response programs across customer segments"),
        ("OpenADR VEN/VTN Operations", "UT-OAD", "Operate OpenADR 2.0b virtual top node for automated DR signaling and reporting"),
        ("Energy Efficiency Programs", "UT-EEP", "Manage energy efficiency audits, rebates, incentives, and measurement/verification"),
        ("DER Customer Enrollment", "UT-DCE", "Enroll customer-owned DER (solar, battery, EV) in utility programs and markets"),
    ],
    "Engineering & Planning": [
        ("T&D Planning & Studies", "UT-TDP", "Plan transmission and distribution capacity, reliability, and expansion projects"),
        ("Generation Planning", "UT-GNP", "Plan generation capacity, fuel mix, retirement, and new resource acquisition"),
        ("Standards & Specifications", "UT-STS", "Develop and maintain technical standards, specifications, and design criteria"),
        ("System Protection & Coordination", "UT-SPC", "Design and coordinate protection schemes, relay settings, and arc flash studies"),
    ],
}

TEST_DATA = OrderedDict([
    ("Customer", [("customer_id", "CUST-2026-001"), ("name", "Jane Smith"), ("address", "123 Oak Street, Springfield"), ("service_type", "Electric + Water"), ("status", "Active")]),
    ("Account", [("account_id", "ACCT-2026-001"), ("customer_id", "CUST-2026-001"), ("billing_cycle", "Monthly"), ("balance", "$245.80"), ("payment_method", "Auto-Pay")]),
    ("Meter", [("meter_id", "MTR-2026-001"), ("type", "Smart Meter (Itron OpenWay)"), ("installation_date", "2024-03-15"), ("status", "Commissioned"), ("interval", "15-min")]),
    ("MeterReading", [("reading_id", "RDG-2026-001"), ("meter_id", "MTR-2026-001"), ("timestamp", "2026-07-07T10:00:00Z"), ("kwh", "12.45"), ("quality", "Validated")]),
    ("ServicePoint", [("sp_id", "SP-2026-001"), ("address", "123 Oak Street, Springfield"), ("transformer_id", "TX-2026-001"), ("feeder_id", "FDR-2026-001"), ("voltage", "240V")]),
    ("Transformer", [("transformer_id", "TX-2026-001"), ("type", "Padmount 75kVA"), ("location", "123 Oak St pad"), ("status", "In Service"), ("capacity", "75")]),
    ("Feeder", [("feeder_id", "FDR-2026-001"), ("substation_id", "SUB-MAIN-001"), ("voltage", "12.47kV"), ("rating", "600A"), ("length_km", "4.2")]),
    ("Substation", [("substation_id", "SUB-MAIN-001"), ("name", "Springfield Main Substation"), ("voltage", "138kV/12.47kV"), ("type", "Distribution"), ("status", "Operational")]),
    ("Breaker", [("breaker_id", "BRK-2026-001"), ("substation_id", "SUB-MAIN-001"), ("status", "Closed"), ("rating", "1200A"), ("type", "SF6")]),
    ("WorkOrder", [("wo_id", "WO-2026-001"), ("type", "Emergency Repair"), ("status", "Assigned"), ("priority", "High"), ("crew_id", "CREW-2026-001")]),
    ("Crew", [("crew_id", "CREW-2026-001"), ("name", "Line Crew Alpha"), ("members", "4"), ("location", "Springfield Depot"), ("status", "Available")]),
    ("Plant", [("plant_id", "PLT-GEN-001"), ("name", "Springfield Thermal Power Station"), ("type", "Combined Cycle Gas Turbine"), ("capacity_mw", "500"), ("status", "Operating")]),
    ("Generator", [("generator_id", "GEN-2026-001"), ("plant_id", "PLT-GEN-001"), ("type", "Gas Turbine"), ("capacity_mw", "250"), ("status", "Online")]),
    ("Boiler", [("boiler_id", "BLR-2026-001"), ("plant_id", "PLT-GEN-001"), ("type", "Heat Recovery Steam Generator"), ("steam_pressure", "1800 psi"), ("status", "Operating")]),
    ("Turbine", [("turbine_id", "TRB-2026-001"), ("plant_id", "PLT-GEN-001"), ("type", "Steam Turbine"), ("rating_mw", "250"), ("speed_rpm", "3600")]),
    ("WaterTreatmentPlant", [("wtp_id", "WTP-2026-001"), ("name", "Springfield Water Treatment Plant"), ("capacity_mgd", "50"), ("source", "Springfield Reservoir"), ("status", "Operating")]),
    ("WaterQualitySample", [("sample_id", "WQ-2026-001"), ("wtp_id", "WTP-2026-001"), ("ph", "7.2"), ("turbidity_ntu", "0.15"), ("chlorine_residual", "1.2 mg/L"), ("status", "Compliant")]),
    ("Pump", [("pump_id", "PUMP-2026-001"), ("station", "Springfield Booster Station"), ("type", "Centrifugal"), ("flow_gpm", "2500"), ("status", "Running")]),
    ("Valve", [("valve_id", "VALV-2026-001"), ("type", "Butterfly"), ("diameter_inches", "16"), ("position", "85% Open"), ("status", "Operational")]),
    ("Pipe", [("pipe_id", "PIPE-2026-001"), ("material", "Ductile Iron"), ("diameter_inches", "24"), ("length_ft", "3200"), ("zone", "Pressure Zone 3")]),
    ("LiftStation", [("ls_id", "LS-2026-001"), ("name", "Oak Street Lift Station"), ("type", "Wastewater"), ("pump_count", "3"), ("status", "Auto")]),
    ("SCADA_Point", [("point_id", "PT-2026-001"), ("description", "Turbine Speed"), ("value", "3600"), ("unit", "RPM"), ("quality", "Good")]),
    ("Alarm", [("alarm_id", "ALM-2026-001"), ("source", "Boiler BLR-2026-001"), ("type", "High Pressure"), ("severity", "Critical"), ("timestamp", "2026-07-07T09:45:00Z"), ("status", "Acknowledged")]),
    ("DER", [("der_id", "DER-2026-001"), ("customer_id", "CUST-2026-001"), ("type", "Solar PV"), ("capacity_kw", "10"), ("status", "Interconnected")]),
    ("Battery", [("battery_id", "BAT-2026-001"), ("customer_id", "CUST-2026-001"), ("capacity_kwh", "13.5"), ("type", "Lithium-Ion"), ("status", "Charging")]),
    ("EV_Charger", [("ev_id", "EV-2026-001"), ("customer_id", "CUST-2026-001"), ("type", "Level 2"), ("rating_kw", "7.2"), ("status", "Idle")]),
    ("DR_Event", [("event_id", "DR-2026-001"), ("program", "Peak Rewards"), ("status", "Active"), ("start_time", "2026-07-07T14:00:00Z"), ("end_time", "2026-07-07T18:00:00Z"), ("reduction_target_kw", "500")]),
    ("Invoice", [("invoice_id", "INV-2026-007"), ("account_id", "ACCT-2026-001"), ("amount", "$245.80"), ("due_date", "2026-07-25"), ("status", "Pending")]),
    ("Payment", [("payment_id", "PAY-2026-042"), ("invoice_id", "INV-2026-007"), ("amount", "$245.80"), ("method", "Credit Card"), ("reference", "CC-4242")]),
    ("Outage", [("outage_id", "OUT-2026-001"), ("feeder_id", "FDR-2026-001"), ("cause", "Tree Contact"), ("start_time", "2026-07-07T08:30:00Z"), ("customers_affected", "450"), ("status", "Active")]),
    ("Switchgear", [("switch_id", "SW-2026-001"), ("substation_id", "SUB-MAIN-001"), ("type", "Load Break Switch"), ("status", "Open"), ("location", "Pole #47")]),
    ("Relay", [("relay_id", "REL-2026-001"), ("substation_id", "SUB-MAIN-001"), ("type", "Distance Protection (SEL-421)"), ("setting_group", "1"), ("status", "Enabled")]),
    ("PMU", [("pmu_id", "PMU-2026-001"), ("substation_id", "SUB-MAIN-001"), ("phasor", "V1"), ("magnitude", "138.2 kV"), ("angle", "-2.4 deg"), ("frequency", "60.02 Hz")]),
    ("EnvironmentalReport", [("report_id", "ENV-2026-001"), ("plant_id", "PLT-GEN-001"), ("co2_tons", "1250"), ("nox_lbs", "320"), ("so2_lbs", "15"), ("reporting_period", "2026-Q2")]),
    ("Permit", [("permit_id", "PER-2026-001"), ("type", "NPDES Discharge"), ("facility", "WTP-2026-001"), ("issue_date", "2026-01-01"), ("expiry_date", "2030-12-31"), ("status", "Active")]),
    ("Contract", [("contract_id", "CON-2026-001"), ("vendor", "GE Vernova"), ("type", "Turbine Maintenance"), ("value", "$2.5M"), ("start_date", "2026-01-01"), ("end_date", "2028-12-31")]),
    ("Vendor", [("vendor_id", "VEN-2026-001"), ("name", "ACME Electrical Supply"), ("category", "Switchgear"), ("status", "Approved"), ("rating", "4.5/5")]),
    ("ComplianceReport", [("comp_id", "COMP-2026-001"), ("standard", "NERC CIP-005"), ("status", "Compliant"), ("audit_date", "2026-04-15"), ("findings", "0")]),
])
