"""Insurance Analytics Dashboard Definitions — ACORD Capability Model Reference.

Each dashboard maps to one or more ACORD INxxx capability codes.
KPIs carry inline references to Solvency II, NAIC, IFRS 17, and APRA standards.
"""

DASHBOARDS = [
    # ──────────────────────────────────────────────────────────────
    # 1. PRODUCT LIFECYCLE PERFORMANCE   (IN001–IN004)
    # ──────────────────────────────────────────────────────────────
    {
        "id": 1,
        "title": "Product Lifecycle Performance Dashboard",
        "acord_codes": ["IN001", "IN002", "IN003", "IN004"],
        "business_question": "Which products are underperforming and why?",
        "owner": "Head of Product Management",
        "description": (
            "Tracks product pipeline from concept through filing, launch, and in-force "
            "performance. Enables product managers to compare loss/expense/combined ratios "
            "across products, monitor rate filing progress, and identify underperforming "
            "coverages before they erode margin."
        ),
        "kpis": [
            ("Products in Pipeline", "Count of products in concept/design/filing", "Count", "Duck Creek PLM", "Weekly", "NAIC Product Filing"),
            ("Time to Market", "Avg days from concept to launch", "Bar (trend)", "Duck Creek PLM", "Monthly", "\u2014"),
            ("In-Force Policies", "Total active policies by product", "Count", "Guidewire PolicyCenter", "Daily", "\u2014"),
            ("Premium Written (GWP)", "Gross premium written by product line", "Bar (stacked)", "Duck Creek Rating", "Monthly", "IFRS 17.55(a)"),
            ("Loss Ratio (LR)", "Incurred Claims / Earned Premium", "Line + Gauge", "Guidewire ClaimCenter", "Monthly", "NAIC SSAP 53; IFRS 17.55(c)"),
            ("Expense Ratio (ER)", "Acquisition + Admin Expenses / EP", "Line + Gauge", "SAP GL", "Monthly", "NAIC SSAP 61"),
            ("Combined Ratio", "LR + ER", "Gauge", "BI (Tableau)", "Monthly", "NAIC IRIS 4a"),
            ("Product Profitability", "Underwriting result by product", "Bar (waterfall)", "Snowflake DW", "Monthly", "IFRS 17.55(d)"),
            ("Rate Filing Approval %", "Filed rates approved vs pending", "Donut", "Duck Creek Rating", "Monthly", "NAIC SERFF"),
            ("Coverage Utilization", "% of policies with optional coverages attached", "Bar", "Guidewire PolicyCenter", "Quarterly", "\u2014"),
            ("Retention by Product", "% of renewable policies retained", "Line", "Guidewire PolicyCenter", "Monthly", "\u2014"),
            ("Benchmark Comparison", "LR/ER vs industry benchmark by product line", "Table (heatmap)", "BI (Tableau)", "Quarterly", "NAIC IRIS"),
        ],
        "filters": ["Product Line", "Region", "Distribution Channel", "Time Period"],
        "drill_down": "Product > Coverage > Policy > Claim",
        "mermaid": [
            "sequenceDiagram",
            "    participant PLM as Product Lifecycle<br/>(Duck Creek)",
            "    participant RATE as Rating Engine<br/>(Duck Creek Rating)",
            "    participant PAS as Policy Admin<br/>(Guidewire PolicyCenter)",
            "    participant CC as ClaimCenter<br/>(Guidewire ClaimCenter)",
            "    participant DW as Data Warehouse<br/>(Snowflake)",
            "    participant BI as BI Platform<br/>(Tableau)",
            "    participant PM as Product Manager",
            "    PLM->>DW: Product master, filing status",
            "    RATE->>DW: Rate tables, filed premiums",
            "    PAS->>DW: In-force policies, retention",
            "    CC->>DW: Incurred claims, loss triangles",
            "    DW->>BI: Aggregated KPI dataset",
            "    BI->>BI: LR/ER/Combined ratio calc",
            "    PM->>BI: View product dashboard",
            "    BI-->>PM: Dashboard loaded (12 KPIs)",
        ],
    },
    # ──────────────────────────────────────────────────────────────
    # 2. DISTRIBUTION & CHANNEL ANALYTICS   (IN005\u2013IN008)
    # ──────────────────────────────────────────────────────────────
    {
        "id": 2,
        "title": "Distribution & Channel Analytics Dashboard",
        "acord_codes": ["IN005", "IN006", "IN007", "IN008"],
        "business_question": "Which channels and producers deliver the best ROI?",
        "owner": "Head of Distribution",
        "description": (
            "Monitors channel performance (agents, brokers, direct, bancassurance, aggregators) "
            "on premium volume, acquisition cost, conversion, retention, and cross-sell. "
            "Includes producer scorecards with traffic-light indicators and peer percentile ranking."
        ),
        "kpis": [
            ("Premium by Channel", "GWP split by channel", "Pie + Bar", "Guidewire PolicyCenter", "Monthly", "\u2014"),
            ("Customer Acquisition Cost", "Total channel cost / new policies", "Bar (by channel)", "SAP GL", "Monthly", "\u2014"),
            ("Conversion Rate", "Quotes accepted / quotes issued by channel", "Line + Gauge", "Duck Creek Rating", "Monthly", "\u2014"),
            ("Retention Rate", "Policies renewed / policies expiring by channel", "Line", "Guidewire PolicyCenter", "Monthly", "\u2014"),
            ("Active Producer Count", "Producers with >=1 policy in period", "Count", "Guidewire PolicyCenter", "Monthly", "NAIC Producer Licensing"),
            ("Commission Ratio", "Commission paid / premium written by channel", "Bar", "Duck Creek Billing", "Monthly", "\u2014"),
            ("Cross-Sell Ratio", "% of multi-policy households by channel", "Bar", "CRM (Salesforce)", "Monthly", "\u2014"),
            ("Cost-to-Serve", "Service cost per policy by channel", "Bar", "SAP GL", "Monthly", "\u2014"),
            ("Producer Scorecard", "KPI vs target with traffic-light per producer", "Table (heatmap)", "BI (Tableau)", "Monthly", "\u2014"),
            ("Channel Profitability", "Channel P&L: premium - commissions - expenses", "Waterfall", "Snowflake DW", "Monthly", "IFRS 17.55(d)"),
            ("Lead Conversion Funnel", "Lead > quote > bind by source", "Funnel", "Marketo + CRM", "Weekly", "\u2014"),
            ("Agency Contingent Pay", "Profit-sharing % vs loss-ratio threshold", "Gauge", "Duck Creek Billing", "Annual", "NAIC SSAP 54"),
        ],
        "filters": ["Channel Type", "Region", "Producer Tier", "Time Period"],
        "drill_down": "Channel > Producer > Policy > Commission",
        "mermaid": [
            "sequenceDiagram",
            "    participant PAS as Policy Admin<br/>(Guidewire PolicyCenter)",
            "    participant CRM as CRM<br/>(Salesforce Financial Svcs)",
            "    participant BILL as Billing<br/>(Duck Creek Billing)",
            "    participant GL as Finance GL<br/>(SAP)",
            "    participant MKT as Marketing<br/>(Marketo)",
            "    participant DW as Data Warehouse<br/>(Snowflake)",
            "    participant BI as BI Platform<br/>(Tableau)",
            "    participant DIST as Distribution Manager",
            "    PAS->>DW: Premium, producer, channel",
            "    CRM->>DW: Lead sources, cross-sell",
            "    BILL->>DW: Commissions paid",
            "    GL->>DW: Channel expenses",
            "    MKT->>DW: Campaign attribution",
            "    DW->>BI: Channel analytics model",
            "    DIST->>BI: View distribution dashboard",
            "    BI-->>DIST: KPIs by channel",
        ],
    },
    # ──────────────────────────────────────────────────────────────
    # 3. UNDERWRITING DASHBOARD   (IN009\u2013IN012)
    # ──────────────────────────────────────────────────────────────
    {
        "id": 3,
        "title": "Underwriting Dashboard",
        "acord_codes": ["IN009", "IN010", "IN011", "IN012"],
        "business_question": "Is underwriting risk selection improving or deteriorating?",
        "owner": "Chief Underwriting Officer",
        "description": (
            "Provides real-time visibility into new business pipeline, risk selection quality, "
            "quote-to-bind conversion, referral bottlenecks, and portfolio risk concentration. "
            "Helps underwriters balance growth against risk appetite."
        ),
        "kpis": [
            ("Submission Volume", "New business submissions received", "Count (trend)", "Origami Risk UW", "Daily", "\u2014"),
            ("Quote-to-Bind Ratio", "Policies bound / quotes issued", "Gauge", "Duck Creek Rating", "Daily", "\u2014"),
            ("Average Premium", "Mean premium per bound policy", "Line", "Duck Creek Rating", "Monthly", "\u2014"),
            ("Risk Score Distribution", "Count of risks by score decile", "Histogram", "Origami Risk UW", "Monthly", "Solvency II UW Risk 1.2"),
            ("Referral Rate", "% of submissions requiring UW referral", "Line", "Origami Risk UW", "Monthly", "\u2014"),
            ("TAT (Submission > Quote)", "Avg hours from submission to quote issued", "Bar", "Origami Risk UW", "Weekly", "\u2014"),
            ("TAT (Quote > Bind)", "Avg days from quote to policy bound", "Bar", "Guidewire PolicyCenter", "Weekly", "\u2014"),
            ("Portfolio Concentration", "% of premium in top 3 risk categories", "Donut", "BI (Tableau)", "Monthly", "Solvency II Risk Concentration"),
            ("Declination Rate", "Quotes declined / submissions", "Line", "Origami Risk UW", "Monthly", "\u2014"),
            ("UW Authority Utilization", "% decided within UW authority limit", "Gauge", "Origami Risk UW", "Monthly", "\u2014"),
            ("Reinsurance Impact", "Premium ceded vs retained by risk band", "Bar (stacked)", "Sapiens Re", "Monthly", "Solvency II RI Risk"),
            ("New Business LR", "Incurred loss ratio on policies <=12 months", "Line", "Guidewire ClaimCenter", "Quarterly", "NAIC IRIS 7"),
        ],
        "filters": ["Product Line", "Region", "UW Team", "Risk Band"],
        "drill_down": "Submission > Quote > Policy > Claims Experience",
        "mermaid": [
            "sequenceDiagram",
            "    participant UW as UW Workbench<br/>(Origami Risk)",
            "    participant RATE as Rating Engine<br/>(Duck Creek Rating)",
            "    participant PAS as Policy Admin<br/>(Guidewire PolicyCenter)",
            "    participant CRM as CRM<br/>(Salesforce Financial Svcs)",
            "    participant DW as Data Warehouse<br/>(Snowflake)",
            "    participant BI as BI Platform<br/>(Tableau)",
            "    participant CUO as Chief UW Officer",
            "    UW->>DW: Submission, risk score, referral",
            "    RATE->>DW: Quotes issued, premium",
            "    PAS->>DW: Bound policies, effective date",
            "    CRM->>DW: Producer attribution",
            "    DW->>BI: UW pipeline model",
            "    BI->>BI: Calc funnel metrics",
            "    CUO->>BI: View UW dashboard",
            "    BI-->>CUO: Pipeline and risk selection KPIs",
        ],
    },
    # ──────────────────────────────────────────────────────────────
    # 4. POLICY ADMINISTRATION DASHBOARD   (IN013\u2013IN015)
    # ──────────────────────────────────────────────────────────────
    {
        "id": 4,
        "title": "Policy Administration Dashboard",
        "acord_codes": ["IN013", "IN014", "IN015"],
        "business_question": "How healthy is the in-force book and policy servicing?",
        "owner": "Head of Policy Services",
        "description": (
            "Provides a complete view of the policy lifecycle: new business, in-force book, "
            "renewals, mid-term adjustments, cancellations, and endorsements. "
            "Tracks service levels including TAT for endorsements and policy inquiry response."
        ),
        "kpis": [
            ("In-Force Policies", "Total active policies", "Count (trend)", "Guidewire PolicyCenter", "Daily", "\u2014"),
            ("New Business Count", "Policies issued (first-time) this period", "Bar", "Guidewire PolicyCenter", "Daily", "\u2014"),
            ("Renewal Rate", "Policies renewed / renewals offered", "Gauge + Line", "Guidewire PolicyCenter", "Monthly", "\u2014"),
            ("Mid-Term Adjustments", "Endorsements processed this period", "Bar", "Guidewire PolicyCenter", "Monthly", "\u2014"),
            ("Cancellation Rate", "Policies cancelled / in-force count", "Line", "Guidewire PolicyCenter", "Monthly", "\u2014"),
            ("Cancellation Reason Mix", "% by reason (non-pay, UW, fraud, request)", "Pie", "Guidewire PolicyCenter", "Monthly", "\u2014"),
            ("Endorsement TAT", "Avg hours from request to endorsement issued", "Bar", "Guidewire PolicyCenter", "Weekly", "\u2014"),
            ("Policy Inquiry Volume", "Customer/producer inquiries received", "Count (trend)", "CRM (Salesforce)", "Weekly", "\u2014"),
            ("Average Policy Tenure", "Mean days policy has been in-force", "Line", "Guidewire PolicyCenter", "Monthly", "\u2014"),
            ("NPS (Policy Servicing)", "Net promoter score from servicing survey", "Gauge", "CRM (Salesforce)", "Quarterly", "\u2014"),
            ("Auto-Issue %", "Policies issued without manual intervention", "Gauge", "Guidewire PolicyCenter", "Monthly", "\u2014"),
            ("Document Generation", "Policy documents generated (schedules, COIs)", "Count", "M-Files", "Monthly", "\u2014"),
        ],
        "filters": ["Product Line", "Region", "Coverage Type", "Time Period"],
        "drill_down": "Policy > Endorsement > Document > Inquiry",
        "mermaid": [
            "sequenceDiagram",
            "    participant PAS as Policy Admin<br/>(Guidewire PolicyCenter)",
            "    participant CRM as CRM<br/>(Salesforce Financial Svcs)",
            "    participant DOC as Document Mgmt<br/>(M-Files)",
            "    participant DW as Data Warehouse<br/>(Snowflake)",
            "    participant BI as BI Platform<br/>(Tableau)",
            "    participant MGR as Policy Services Manager",
            "    PAS->>DW: Policy events (issue, endorse, cancel, renew)",
            "    CRM->>DW: Inquiry, NPS, servicing data",
            "    DOC->>DW: Document generation count",
            "    DW->>BI: Policy lifecycle model",
            "    MGR->>BI: View policy dashboard",
            "    BI-->>MGR: Book health and servicing KPIs",
        ],
    },
    # ──────────────────────────────────────────────────────────────
    # 5. CLAIMS OPERATIONS DASHBOARD   (IN016\u2013IN019)
    # ──────────────────────────────────────────────────────────────
    {
        "id": 5,
        "title": "Claims Operations Dashboard",
        "acord_codes": ["IN016", "IN017", "IN018", "IN019"],
        "business_question": "Are claims being handled efficiently, fairly, and within reserve?",
        "owner": "Chief Claims Officer",
        "description": (
            "End-to-end claims analytics covering FNOL intake, investigation, adjudication, "
            "payment, litigation, and subrogation. Monitors leakage, cycle times, adjuster "
            "workload, and reserve adequacy. Alerts when claims exceed authority or "
            "outlier severity thresholds."
        ),
        "kpis": [
            ("FNOL Volume", "First notices of loss received", "Count (trend)", "Guidewire ClaimCenter", "Daily", "NAIC Claims Handling"),
            ("Open Claims Count", "Claims currently open (by status)", "Count", "Guidewire ClaimCenter", "Daily", "\u2014"),
            ("Average Severity", "Total paid / closed claims", "Line + Bar", "Guidewire ClaimCenter", "Monthly", "\u2014"),
            ("Claims Frequency", "Claim count / in-force policies", "Line", "Guidewire ClaimCenter", "Monthly", "Solvency II Premium Risk"),
            ("Leakage Rate", "Indemnity paid / expected reserve (deviation)", "Gauge", "Guidewire ClaimCenter", "Monthly", "\u2014"),
            ("Cycle Time (FNOL > Payment)", "Avg days from FNOL to first payment", "Bar", "Guidewire ClaimCenter", "Weekly", "NAIC Timely Claims Handling"),
            ("Cycle Time (FNOL > Close)", "Avg days from FNOL to claim closure", "Bar", "Guidewire ClaimCenter", "Weekly", "\u2014"),
            ("Reserve Adequacy", "Case reserve adequacy ratio", "Line", "SAS Actuarial", "Monthly", "Solvency II TP 2.2; NAIC SSAP 55"),
            ("Subrogation Recovery Rate", "Amount recovered / amount recoverable", "Gauge", "Guidewire ClaimCenter", "Monthly", "\u2014"),
            ("Litigation Rate", "% of claims with active litigation", "Line", "Guidewire ClaimCenter", "Monthly", "\u2014"),
            ("Adjuster Workload", "Open claims per adjuster", "Bar", "Guidewire ClaimCenter", "Weekly", "\u2014"),
            ("Claims NPS", "Customer satisfaction survey post-settlement", "Gauge", "CRM (Salesforce)", "Quarterly", "NAIC Fair Claims Practices"),
        ],
        "filters": ["Line of Business", "Claim Status", "Adjuster Team", "Time Period"],
        "drill_down": "Claim > Coverage > Payment > Litigation > Recovery",
        "mermaid": [
            "sequenceDiagram",
            "    participant CC as ClaimCenter<br/>(Guidewire ClaimCenter)",
            "    participant CRM as CRM<br/>(Salesforce Financial Svcs)",
            "    participant SAS as Actuarial System<br/>(SAS)",
            "    participant PAY as Payment Gateway<br/>(Stripe)",
            "    participant DW as Data Warehouse<br/>(Snowflake)",
            "    participant BI as BI Platform<br/>(Tableau)",
            "    participant CCO as Chief Claims Officer",
            "    CC->>DW: FNOL, reserve, payment, status",
            "    CRM->>DW: Survey, NPS, interaction",
            "    SAS->>DW: Reserve adequacy, IBNR",
            "    PAY->>DW: Payment transactions",
            "    DW->>BI: Claims analytics model",
            "    CCO->>BI: View claims dashboard",
            "    BI-->>CCO: Operations and leakage KPIs",
        ],
    },
    # ──────────────────────────────────────────────────────────────
    # 6. REINSURANCE DASHBOARD   (IN020\u2013IN022)
    # ──────────────────────────────────────────────────────────────
    {
        "id": 6,
        "title": "Reinsurance Dashboard",
        "acord_codes": ["IN020", "IN021", "IN022"],
        "business_question": "Are our reinsurance programmes adequately covering our risk exposure?",
        "owner": "Head of Reinsurance",
        "description": (
            "Monitors treaty and facultative placements, premium ceded, recoveries, "
            "bordereaux accuracy and timeliness, counterparty credit risk, and retrocession "
            "coverage. Provides early warning if treaty capacity is approaching exhaustion."
        ),
        "kpis": [
            ("Treaty Capacity Utilisation", "% of treaty limit consumed by claims", "Gauge + Bar", "Sapiens Re", "Monthly", "Solvency II RI Risk 2.1"),
            ("Premium Ceded Ratio", "Ceded premium / gross written premium", "Line", "Sapiens Re + PAS", "Quarterly", "IFRS 17.62; NAIC SSAP 61"),
            ("Recoveries Received", "Reinsurance recoveries collected this period", "Bar", "Sapiens Re", "Monthly", "\u2014"),
            ("Recovery Cycle Time", "Avg days from cession notification to cash received", "Bar", "Sapiens Re", "Monthly", "\u2014"),
            ("Bordereaux Accuracy", "% of bordereaux records error-free on submission", "Gauge", "Sapiens Re", "Monthly", "\u2014"),
            ("Bordereaux Timeliness", "% submitted within contractual deadline", "Gauge", "Sapiens Re", "Monthly", "\u2014"),
            ("RI Credit Risk", "Exposure weighted by reinsurer credit rating", "Bar", "Sapiens Re + Moody's", "Quarterly", "Solvency II Counterparty Risk 3.1"),
            ("Facultative Placement", "Number of facultative placements requested/placed", "Count (bar)", "Sapiens Re", "Monthly", "\u2014"),
            ("Retrocession Coverage", "% of ceded risk covered by retrocession", "Gauge", "Sapiens Re", "Quarterly", "Solvency II RI Risk 2.3"),
            ("Catastrophe RI Cover", "Per-occurrence limit vs modelled PML", "Gauge", "Moody's RMS", "Annual", "Solvency II Cat Risk"),
            ("Treaty Expiry Calendar", "Upcoming treaty renewals in next 6 months", "Timeline table", "Sapiens Re", "Monthly", "\u2014"),
            ("RI Programme ROE", "Return on equity of RI programme", "Line", "Snowflake DW", "Annual", "\u2014"),
        ],
        "filters": ["Treaty Type", "Reinsurer", "Line of Business", "Year"],
        "drill_down": "Treaty > Cession > Claim Recovery > Reinsurer",
        "mermaid": [
            "sequenceDiagram",
            "    participant RE as Reinsurance System<br/>(Sapiens Re)",
            "    participant PAS as Policy Admin<br/>(Guidewire PolicyCenter)",
            "    participant CC as ClaimCenter<br/>(Guidewire ClaimCenter)",
            "    participant RMS as Cat Modelling<br/>(Moody's RMS)",
            "    participant DW as Data Warehouse<br/>(Snowflake)",
            "    participant BI as BI Platform<br/>(Tableau)",
            "    participant RE_MGR as Reinsurance Manager",
            "    RE->>DW: Treaty, cession, bordereaux",
            "    PAS->>DW: Premium by treaty",
            "    CC->>DW: Ceded claim recoveries",
            "    RMS->>DW: PML by peril vs treaty cover",
            "    DW->>BI: RI analytics model",
            "    RE_MGR->>BI: View RI dashboard",
            "    BI-->>RE_MGR: Treaty and recovery KPIs",
        ],
    },
    # ──────────────────────────────────────────────────────────────
    # 7. ACTUARIAL & PRICING DASHBOARD   (IN023\u2013IN025)
    # ──────────────────────────────────────────────────────────────
    {
        "id": 7,
        "title": "Actuarial & Pricing Dashboard",
        "acord_codes": ["IN023", "IN024", "IN025"],
        "business_question": "Are our rates adequate and reserves sufficient?",
        "owner": "Chief Actuary",
        "description": (
            "Aggregates pricing, rate monitoring, reserving, and catastrophe modelling analytics. "
            "Enables the actuarial team to assess rate adequacy, track IBNR emergence, validate "
            "reserve assumptions, and understand catastrophe exposure. Links pricing decisions "
            "to actual loss experience."
        ),
        "kpis": [
            ("Rate Adequacy", "Indicated rate change vs filed (by product)", "Gauge + Table", "Duck Creek Rating", "Monthly", "NAIC SERFF; Solvency II Pricing"),
            ("Actual vs Expected LR", "Incurred LR vs pricing assumption LR", "Line (pair)", "SAS + DW", "Monthly", "Solvency II TP 2.2"),
            ("IBNR Ratio", "IBNR reserve / total reserve", "Line", "SAS Actuarial", "Monthly", "IFRS 17.37; NAIC SSAP 55"),
            ("Reserve Adequacy Ratio", "Best estimate vs central estimate", "Gauge", "SAS Actuarial", "Quarterly", "Solvency II TP 2.3"),
            ("Chain-Ladder IBNR", "IBNR via chain-ladder method", "Line (development)", "SAS Actuarial", "Quarterly", "\u2014"),
            ("Bornhuetter-Ferguson IBNR", "IBNR via BF method for immature periods", "Line (development)", "SAS Actuarial", "Quarterly", "\u2014"),
            ("Probable Maximum Loss", "OEP 100yr / AEP 100yr / AAL", "Bar (by peril)", "Moody's RMS", "Quarterly", "Solvency II Cat Risk"),
            ("PML vs Treaty Cover", "PML as % of per-occurrence treaty limit", "Gauge", "Moody's RMS", "Annual", "Solvency II Cat Risk 4.1"),
            ("Credibility-Weighted LR", "LR weighted by credibility factor", "Line", "SAS Actuarial", "Monthly", "\u2014"),
            ("Loss Development Pattern", "Paid + incurred loss triangles", "Line (multi-series)", "SAS Actuarial", "Quarterly", "IFRS 17.37; NAIC SSAP 55"),
            ("Expense Load", "Expense provision as % of gross premium", "Bar", "SAP GL", "Monthly", "\u2014"),
            ("Model Stability", "Variance of reserve estimates across quarterly runs", "Bar (variance)", "SAS Actuarial", "Quarterly", "Solvency II TP 2.5"),
        ],
        "filters": ["Product Line", "Accident Year", "Development Period", "Peril"],
        "drill_down": "Product > Accident Year > Reserve Method > Model Run",
        "mermaid": [
            "sequenceDiagram",
            "    participant SAS as Actuarial System<br/>(SAS)",
            "    participant RATE as Rating Engine<br/>(Duck Creek Rating)",
            "    participant RMS as Cat Modelling<br/>(Moody's RMS)",
            "    participant CC as ClaimCenter<br/>(Guidewire ClaimCenter)",
            "    participant DW as Data Warehouse<br/>(Snowflake)",
            "    participant BI as BI Platform<br/>(Tableau)",
            "    participant ACT as Chief Actuary",
            "    SAS->>DW: Reserve estimates, IBNR",
            "    RATE->>DW: Rate adequacy, premiums",
            "    RMS->>DW: PML, AAL, exceedance curves",
            "    CC->>DW: Paid + incurred loss triangles",
            "    DW->>BI: Actuarial analytics model",
            "    ACT->>BI: View actuarial dashboard",
            "    BI-->>ACT: Pricing and reserving KPIs",
        ],
    },
    # ──────────────────────────────────────────────────────────────
    # 8. BILLING & COLLECTIONS DASHBOARD   (IN031)
    # ──────────────────────────────────────────────────────────────
    {
        "id": 8,
        "title": "Billing & Collections Dashboard",
        "acord_codes": ["IN031"],
        "business_question": "Are premiums being collected efficiently and on time?",
        "owner": "Head of Finance Operations",
        "description": (
            "Monitors premium billing, payment processing, accounts receivable aging, "
            "collection effectiveness, refunds, and commission disbursement. Flags overdue "
            "accounts and tracks DSO improvements."
        ),
        "kpis": [
            ("Premium Billed", "Total premium billed this period", "Bar", "Duck Creek Billing", "Monthly", "\u2014"),
            ("Premium Collected", "Cash received against billed premium", "Bar", "Duck Creek Billing", "Monthly", "\u2014"),
            ("Collection Rate", "Collected / billed (%)", "Gauge", "Duck Creek Billing", "Monthly", "\u2014"),
            ("Aging (0-30 days)", "Receivables 0-30 days overdue", "Bar (stacked)", "Duck Creek Billing", "Weekly", "\u2014"),
            ("Aging (31-60 days)", "Receivables 31-60 days overdue", "Bar (stacked)", "Duck Creek Billing", "Weekly", "\u2014"),
            ("Aging (61-90 days)", "Receivables 61-90 days overdue", "Bar (stacked)", "Duck Creek Billing", "Weekly", "\u2014"),
            ("Aging (90+ days)", "Receivables >90 days overdue", "Bar (stacked)", "Duck Creek Billing", "Weekly", "\u2014"),
            ("DSO", "Days sales outstanding to collect premium", "Line", "BI (Tableau)", "Monthly", "\u2014"),
            ("Payment Method Mix", "% by method (CC, bank transfer, direct debit, cheque)", "Pie", "Stripe + Billing", "Monthly", "\u2014"),
            ("Failed Payment Rate", "Auto-pay attempts failed / total attempts", "Line", "Stripe", "Monthly", "\u2014"),
            ("Refund Volume", "Premium refunds processed this period", "Count (bar)", "Duck Creek Billing", "Monthly", "\u2014"),
            ("Commission Payable", "Commission due to producers this period", "Bar", "Duck Creek Billing", "Monthly", "\u2014"),
        ],
        "filters": ["Product Line", "Payment Method", "Aging Bucket", "Time Period"],
        "drill_down": "Billing Account > Policy > Payment > Refund",
        "mermaid": [
            "sequenceDiagram",
            "    participant BILL as Billing<br/>(Duck Creek Billing)",
            "    participant PAS as Policy Admin<br/>(Guidewire PolicyCenter)",
            "    participant PAY as Payment Gateway<br/>(Stripe)",
            "    participant GL as Finance GL<br/>(SAP)",
            "    participant DW as Data Warehouse<br/>(Snowflake)",
            "    participant BI as BI Platform<br/>(Tableau)",
            "    participant FIN as Finance Manager",
            "    BILL->>DW: Invoices, payments, aging",
            "    PAS->>DW: Premium adjustments, cancellations",
            "    PAY->>DW: Transaction success/failure",
            "    GL->>DW: GL postings, commission",
            "    DW->>BI: Billing analytics model",
            "    FIN->>BI: View billing dashboard",
            "    BI-->>FIN: Collection and aging KPIs",
        ],
    },
    # ──────────────────────────────────────────────────────────────
    # 9. CUSTOMER ANALYTICS DASHBOARD   (IN026\u2013IN027)
    # ──────────────────────────────────────────────────────────────
    {
        "id": 9,
        "title": "Customer Analytics Dashboard",
        "acord_codes": ["IN026", "IN027"],
        "business_question": "How satisfied are our customers and what drives loyalty?",
        "owner": "Chief Customer Officer",
        "description": (
            "360-degree view of customer health including NPS, CSAT, customer lifetime value, "
            "retention and loyalty programme effectiveness, cross-sell penetration, complaints "
            "trends, and service experience metrics. Segments customers by behaviour, "
            "value, and risk profile."
        ),
        "kpis": [
            ("Net Promoter Score", "Promoters - Detractors (scale -100 to +100)", "Gauge + Line", "CRM (Salesforce)", "Quarterly", "\u2014"),
            ("Customer Satisfaction", "Avg satisfaction score (1-5) post-interaction", "Gauge", "CRM (Salesforce)", "Monthly", "NAIC Fair Treatment"),
            ("Customer Lifetime Value", "Present value of future profit from customer", "Bar (segment)", "BI (Tableau)", "Monthly", "\u2014"),
            ("Retention Rate", "Customers retained / customers at risk", "Gauge + Line", "Guidewire PolicyCenter", "Monthly", "\u2014"),
            ("Cross-Sell Penetration", "% customers with >1 policy", "Bar (trend)", "CRM (Salesforce)", "Monthly", "\u2014"),
            ("Complaint Volume", "Complaints received by category", "Count (bar)", "CRM (Salesforce)", "Monthly", "NAIC Consumer Complaints"),
            ("First-Contact Resolution", "Issues resolved in first interaction", "Gauge", "CRM (Salesforce)", "Monthly", "\u2014"),
            ("Average Response Time", "Avg hours to respond to customer enquiry", "Line", "CRM (Salesforce)", "Weekly", "\u2014"),
            ("Customer Segment Mix", "% by value tier (platinum/gold/silver/bronze)", "Pie", "BI (Tableau)", "Monthly", "\u2014"),
            ("Loyalty Programme Engagement", "Active members / eligible customers", "Gauge", "CRM (Salesforce)", "Monthly", "\u2014"),
            ("Cost-to-Serve per Customer", "Service cost / customer count by segment", "Bar", "SAP GL", "Monthly", "\u2014"),
            ("Churn Prediction Score", "Avg churn probability for at-risk population", "Gauge", "H2O.ai ML Model", "Monthly", "\u2014"),
        ],
        "filters": ["Customer Segment", "Product Line", "Channel", "Time Period"],
        "drill_down": "Segment > Customer > Policy > Interaction",
        "mermaid": [
            "sequenceDiagram",
            "    participant CRM as CRM<br/>(Salesforce Financial Svcs)",
            "    participant PAS as Policy Admin<br/>(Guidewire PolicyCenter)",
            "    participant ML as ML Platform<br/>(H2O.ai)",
            "    participant MKT as Marketing<br/>(Marketo)",
            "    participant DW as Data Warehouse<br/>(Snowflake)",
            "    participant BI as BI Platform<br/>(Tableau)",
            "    participant CCO as Chief Customer Officer",
            "    CRM->>DW: NPS, CSAT, complaints, CLV",
            "    PAS->>DW: Retention, cross-sell",
            "    ML->>DW: Churn probability scores",
            "    MKT->>DW: Campaign engagement",
            "    DW->>BI: Customer 360 model",
            "    CCO->>BI: View customer dashboard",
            "    BI-->>CCO: Satisfaction and loyalty KPIs",
        ],
    },
    # ──────────────────────────────────────────────────────────────
    # 10. RISK & COMPLIANCE DASHBOARD   (IN028\u2013IN030)
    # ──────────────────────────────────────────────────────────────
    {
        "id": 10,
        "title": "Risk & Compliance Dashboard",
        "acord_codes": ["IN028", "IN029", "IN030"],
        "business_question": "Are we operating within risk appetite and meeting regulatory obligations?",
        "owner": "Chief Risk Officer",
        "description": (
            "Consolidates enterprise risk management, capital adequacy (SCR/MCR), "
            "operational risk incidents, compliance monitoring, internal audit findings, "
            "and conduct risk metrics. Provides a single pane of glass for the CRO "
            "and board risk committee."
        ),
        "kpis": [
            ("SCR Coverage Ratio", "Eligible own funds / SCR", "Gauge + Line", "Moody's Capital", "Quarterly", "Solvency II SCR 3.1"),
            ("MCR Coverage Ratio", "Eligible own funds / MCR", "Gauge", "Moody's Capital", "Quarterly", "Solvency II MCR 4.1"),
            ("KRI Dashboard", "15 green, 3 amber, 2 red indicators", "Traffic-light heatmap", "Moody's Risk", "Monthly", "Solvency II ORSA 5.1"),
            ("Risk Appetite Utilisation", "Risk exposure / risk appetite limit", "Bullet chart", "Moody's Risk", "Monthly", "Solvency II ORSA 5.2"),
            ("Operational Risk Incidents", "Operational loss events by category", "Bar", "ServiceNow GRC", "Monthly", "Solvency II OpRisk 6.1"),
            ("Compliance Breaches", "Regulatory or internal policy breaches", "Count (trend)", "ServiceNow GRC", "Monthly", "\u2014"),
            ("Internal Audit Findings", "Open findings by severity", "Bar (stacked)", "ServiceNow GRC", "Monthly", "IAIS ICPs"),
            ("Open Regulatory Queries", "Outstanding regulatory information requests", "Count", "AxiomSL", "Weekly", "\u2014"),
            ("RCSA Completion", "Risk and control self-assessment completion by BU", "Gauge", "ServiceNow GRC", "Quarterly", "\u2014"),
            ("Conduct Risk Score", "Fair value assessment score by product", "Bar", "Compliance System", "Monthly", "NAIC Market Conduct"),
            ("Capital Allocation", "Capital allocated by risk type", "Waterfall", "Moody's Capital", "Quarterly", "Solvency II SCR 3.2"),
            ("Board Risk Summary", "CRO summary for board risk committee", "Table (executive)", "BI (Tableau)", "Quarterly", "Solvency II ORSA 5.3"),
        ],
        "filters": ["Risk Category", "Business Unit", "KRI Status", "Time Period"],
        "drill_down": "Risk Category > KRI > Incident > Remediation",
        "mermaid": [
            "sequenceDiagram",
            "    participant RISK as Risk System<br/>(Moody's Risk)",
            "    participant CAP as Capital Model<br/>(Moody's Capital)",
            "    participant REG as Reg Reporting<br/>(AxiomSL)",
            "    participant GRC as GRC Platform<br/>(ServiceNow GRC)",
            "    participant AUDIT as Internal Audit<br/>(ServiceNow Audit)",
            "    participant DW as Data Warehouse<br/>(Snowflake)",
            "    participant BI as BI Platform<br/>(Tableau)",
            "    participant CRO as Chief Risk Officer",
            "    RISK->>DW: KRIs, risk appetite, incidents",
            "    CAP->>DW: SCR/MCR ratios, capital allocation",
            "    REG->>DW: Regulatory queries, filings",
            "    GRC->>DW: RCSA, compliance breaches",
            "    AUDIT->>DW: Audit findings",
            "    DW->>BI: Enterprise risk model",
            "    CRO->>BI: View risk dashboard",
            "    BI-->>CRO: Capital and compliance KPIs",
        ],
    },
    # ──────────────────────────────────────────────────────────────
    # 11. IFRS 17 DASHBOARD   (IN032)
    # ──────────────────────────────────────────────────────────────
    {
        "id": 11,
        "title": "IFRS 17 Accounting Dashboard",
        "acord_codes": ["IN032"],
        "business_question": "What is the IFRS 17 profit profile and CSM emergence pattern?",
        "owner": "CFO / IFRS 17 Programme Director",
        "description": (
            "Provides full visibility into IFRS 17 financial metrics: CSM balance and "
            "amortisation, risk adjustment, insurance revenue recognition by PAA/GMM/VFA, "
            "insurance service result, and reinsurance impact. Essential for internal and "
            "external financial reporting."
        ),
        "kpis": [
            ("CSM Balance", "CSM opening + movement - amortised", "Waterfall", "SAP IFRS17", "Quarterly", "IFRS 17.43-46"),
            ("CSM Amortisation", "CSM released to P&L this period", "Bar", "SAP IFRS17", "Quarterly", "IFRS 17.44(b)"),
            ("Risk Adjustment (RA)", "Non-financial risk adjustment movement", "Bar", "SAP IFRS17", "Quarterly", "IFRS 17.37, 17.84"),
            ("Insurance Revenue", "Revenue recognised (PAA/GMM/VFA by group)", "Line + Bar", "SAP IFRS17", "Quarterly", "IFRS 17.83-86"),
            ("Insurance Service Expenses", "Incurred claims + expenses recognised", "Bar", "SAP IFRS17", "Quarterly", "IFRS 17.87-88"),
            ("Net Insurance Result", "Insurance revenue - service expenses", "Line", "SAP IFRS17", "Quarterly", "IFRS 17.80"),
            ("GWP vs NEP", "Gross written vs net earned premium", "Bar (paired)", "SAP IFRS17", "Quarterly", "IFRS 17.55(a)"),
            ("PAA Eligibility", "% of groups qualifying for PAA", "Pie", "SAP IFRS17", "Annual", "IFRS 17.53-54"),
            ("Group Aggregation", "Groups by profitability (onerous/other)", "Bar (stacked)", "SAP IFRS17", "Quarterly", "IFRS 17.16-24"),
            ("Reinsurance Impact", "Reinsurance share of CSM, RA, revenue", "Bar (stacked)", "SAP + Sapiens", "Quarterly", "IFRS 17.62-65"),
            ("Discount Rate Sensitivity", "CSM sensitivity to -50bp/+50bp yield curve", "Table", "SAP IFRS17", "Quarterly", "IFRS 17.56-58"),
            ("Transition Balances", "Opening IFRS 17 equity adjustment by method", "Waterfall", "SAP IFRS17", "Annual", "IFRS 17.C1-C8"),
        ],
        "filters": ["IFRS 17 Group", "Measurement Approach", "Transition Method", "Reporting Period"],
        "drill_down": "Group > Measurement Approach > Movement Component > Journal",
        "mermaid": [
            "sequenceDiagram",
            "    participant IFRS as IFRS17 Engine<br/>(SAP IFRS17)",
            "    participant PAS as Policy Admin<br/>(Guidewire PolicyCenter)",
            "    participant CC as ClaimCenter<br/>(Guidewire ClaimCenter)",
            "    participant GL as Finance GL<br/>(SAP)",
            "    participant RE as Reinsurance<br/>(Sapiens Re)",
            "    participant DW as Data Warehouse<br/>(Snowflake)",
            "    participant BI as BI Platform<br/>(Tableau)",
            "    participant CFO as CFO / Reporting",
            "    IFRS->>DW: CSM, RA, revenue, result",
            "    PAS->>DW: Premium by group",
            "    CC->>DW: Claims by accident period",
            "    RE->>DW: RI share of CSM",
            "    GL->>DW: Journal postings",
            "    DW->>BI: IFRS17 analytics model",
            "    CFO->>BI: View IFRS17 dashboard",
            "    BI-->>CFO: CSM and revenue KPIs",
        ],
    },
    # ──────────────────────────────────────────────────────────────
    # 12. REGULATORY REPORTING DASHBOARD   (IN029)
    # ──────────────────────────────────────────────────────────────
    {
        "id": 12,
        "title": "Regulatory Reporting Dashboard",
        "acord_codes": ["IN029"],
        "business_question": "Are all regulatory filings accurate and on time?",
        "owner": "Head of Regulatory Reporting",
        "description": (
            "Tracks the end-to-end regulatory reporting lifecycle across Solvency II QRTs, "
            "NAIC statutory statements, APRA GPS/LRS filings, and tax returns. Monitors "
            "filing calendar, submission status, data quality scores, and regulator queries."
        ),
        "kpis": [
            ("Filings Due", "Number of regulatory returns due this period", "Count", "AxiomSL", "Monthly", "\u2014"),
            ("Filings Submitted", "Returns submitted on time", "Count", "AxiomSL", "Monthly", "\u2014"),
            ("On-Time Filing Rate", "Submitted on time / due (%)", "Gauge", "AxiomSL", "Monthly", "Solvency II, NAIC, APRA"),
            ("Data Quality Score", "DQ pass rate across all regulatory data", "Gauge + Line", "AxiomSL + Informatica", "Monthly", "\u2014"),
            ("QRT Completion %", "Solvency II QRT completeness (0-100%)", "Gauge", "AxiomSL", "Quarterly", "Solvency II QRT"),
            ("NAIC Filing Status", "Annual/quarterly statement status by state", "Table (traffic-light)", "AxiomSL", "Quarterly", "NAIC SSAP"),
            ("APRA Filing Status", "GPS 001 / LRS 750.0 / other status", "Table (traffic-light)", "AxiomSL", "Quarterly", "APRA GPS 001"),
            ("Regulatory Queries", "Open queries from regulators", "Count (trend)", "AxiomSL", "Monthly", "\u2014"),
            ("Query Resolution TAT", "Avg days to respond to regulator query", "Line", "AxiomSL", "Monthly", "\u2014"),
            ("Tax Filing Status", "GST / premium tax / income tax filing status", "Table", "AxiomSL + SAP", "Quarterly", "ATO / IRS / HMRC"),
            ("Filing Calendar Adherence", "Days ahead of deadline for each filing", "Bar", "AxiomSL", "Monthly", "\u2014"),
            ("Regulatory Change Impact", "Number of regulatory changes affecting reporting", "Count", "AxiomSL", "Quarterly", "\u2014"),
        ],
        "filters": ["Regulator", "Filing Type", "Jurisdiction", "Status"],
        "drill_down": "Regulator > Filing Type > Submission > Query",
        "mermaid": [
            "sequenceDiagram",
            "    participant REG as Reg Reporting<br/>(AxiomSL)",
            "    participant PAS as Policy Admin<br/>(Guidewire PolicyCenter)",
            "    participant GL as Finance GL<br/>(SAP)",
            "    participant DQ as Data Quality<br/>(Informatica)",
            "    participant DW as Data Warehouse<br/>(Snowflake)",
            "    participant BI as BI Platform<br/>(Tableau)",
            "    participant REP as Reporting Manager",
            "    REG->>DW: Filing status, data quality",
            "    PAS->>DW: Premium, policy data",
            "    GL->>DW: Financial data for filings",
            "    DQ->>DW: DQ score by data domain",
            "    DW->>BI: Regulatory dashboard model",
            "    REP->>BI: View regulatory dashboard",
            "    BI-->>REP: Filing and compliance KPIs",
        ],
    },
    # ──────────────────────────────────────────────────────────────
    # 13. DATA & ANALYTICS GOVERNANCE DASHBOARD   (IN033)
    # ──────────────────────────────────────────────────────────────
    {
        "id": 13,
        "title": "Data & Analytics Governance Dashboard",
        "acord_codes": ["IN033"],
        "business_question": "Can we trust our data for decision-making and reporting?",
        "owner": "Chief Data Officer",
        "description": (
            "Monitors data quality across all insurance data domains (policy, claims, "
            "customer, finance, risk), data cataloguing coverage, data lineage completeness, "
            "master data management health, and ML model performance. Drives the "
            "data governance operating model."
        ),
        "kpis": [
            ("Overall DQ Score", "Weighted avg of completeness, timeliness, accuracy, consistency", "Gauge + Line", "Informatica DQ", "Weekly", "BCBS 239; Solvency II Data"),
            ("Completeness %", "Mandatory fields populated correctly", "Gauge", "Informatica DQ", "Weekly", "\u2014"),
            ("Timeliness %", "Data available within SLA", "Gauge", "Informatica DQ", "Weekly", "\u2014"),
            ("Accuracy %", "Data values match authoritative source", "Gauge", "Informatica DQ", "Weekly", "\u2014"),
            ("Consistency %", "Data consistent across source systems", "Gauge", "Informatica DQ", "Weekly", "\u2014"),
            ("DQ Domain Coverage", "% of data domains with active DQ rules", "Donut", "Informatica DQ", "Monthly", "\u2014"),
            ("Data Catalog Coverage", "Data assets catalogued in Collibra", "Gauge", "Collibra", "Monthly", "\u2014"),
            ("Data Lineage Coverage", "Critical data elements with documented lineage", "Gauge", "Collibra + Informatica", "Monthly", "BCBS 239"),
            ("Open DQ Issues", "Data quality issues by severity", "Bar (stacked)", "Informatica DQ", "Weekly", "\u2014"),
            ("MDM Match Rate", "Customer/policy master match rate", "Gauge", "Informatica MDM", "Monthly", "\u2014"),
            ("ML Model Performance", "Avg MAE / R2 across deployed models", "Gauge + Table", "H2O.ai ML Ops", "Monthly", "\u2014"),
            ("DG Adoption", "Business units with active data governance representation", "Gauge", "Collibra", "Quarterly", "\u2014"),
        ],
        "filters": ["Data Domain", "Business Unit", "DQ Dimension", "Time Period"],
        "drill_down": "Data Domain > DQ Rule > Issue > Remediation",
        "mermaid": [
            "sequenceDiagram",
            "    participant DQ as Data Quality<br/>(Informatica DQ)",
            "    participant CAT as Data Catalog<br/>(Collibra)",
            "    participant MDM as MDM<br/>(Informatica MDM)",
            "    participant ML as ML Platform<br/>(H2O.ai)",
            "    participant DW as Data Warehouse<br/>(Snowflake)",
            "    participant BI as BI Platform<br/>(Tableau)",
            "    participant CDO as Chief Data Officer",
            "    DQ->>DW: DQ scores, issue count",
            "    CAT->>DW: Catalog coverage, lineage",
            "    MDM->>DW: Match rates, golden records",
            "    ML->>DW: Model performance metrics",
            "    DW->>BI: Data governance model",
            "    CDO->>BI: View governance dashboard",
            "    BI-->>CDO: Data quality and governance KPIs",
        ],
    },
    # ──────────────────────────────────────────────────────────────
    # 14. INFORMATION SECURITY DASHBOARD   (IN034)
    # ──────────────────────────────────────────────────────────────
    {
        "id": 14,
        "title": "Information Security Dashboard",
        "acord_codes": ["IN034"],
        "business_question": "Are we effectively protecting company and customer data?",
        "owner": "Chief Information Security Officer",
        "description": (
            "Provides a comprehensive view of the security posture including security "
            "incidents, vulnerability management, identity and access management, "
            "business continuity readiness, and third-party risk. Essential for board "
            "risk reporting and regulatory compliance (GDPR, CCPA, DORA)."
        ),
        "kpis": [
            ("Security Incidents", "Incidents by type (phishing, malware, DDoS, insider)", "Bar (stacked)", "SIEM (Azure Sentinel)", "Daily", "GDPR Art 33; NIST 800-61"),
            ("MTTR (Incidents)", "Mean time to resolve security incidents (hours)", "Line", "SIEM (Azure Sentinel)", "Monthly", "\u2014"),
            ("Critical Vulnerabilities", "CVSS >=9.0 unpatched", "Count (trend)", "Qualys / Tenable", "Daily", "NIST 800-53; CIS Controls"),
            ("High Vulnerabilities", "CVSS 7.0-8.9 unpatched", "Count (trend)", "Qualys / Tenable", "Daily", "\u2014"),
            ("Patch Compliance %", "Systems patched within SLA", "Gauge", "Qualys + ServiceNow", "Weekly", "NIST 800-53 SI-2"),
            ("Privileged Access Reviews", "Reviews completed / due (%)", "Gauge", "CyberArk + ServiceNow", "Monthly", "SOX; NIST AC-6"),
            ("Phishing Simulation Click Rate", "Click-through rate on simulated phishing", "Gauge", "KnowBe4", "Monthly", "\u2014"),
            ("BCP Tests Completed", "Tests passed / scheduled (%)", "Gauge", "ServiceNow BCM", "Quarterly", "Solvency II BCM; DORA"),
            ("RPO/RTO Adherence", "Systems meeting recovery point/time objectives", "Gauge", "ServiceNow BCM", "Quarterly", "Solvency II BCM"),
            ("Third-Party Risk", "Vendors with active security assessments", "Count (bar)", "ServiceNow VRM", "Monthly", "DORA; NIST SP 800-53"),
            ("Data Breach Notifications", "Breaches reported to regulator / affected parties", "Count", "SIEM + DPO Tracker", "Monthly", "GDPR Art 33-34"),
            ("Security Awareness Training", "Employees with up-to-date training", "Gauge", "KnowBe4", "Monthly", "NIST AT-2"),
        ],
        "filters": ["Incident Type", "Severity", "System", "Time Period"],
        "drill_down": "Incident > System > Vulnerability > Remediation",
        "mermaid": [
            "sequenceDiagram",
            "    participant SIEM as SIEM<br/>(Azure Sentinel)",
            "    participant VULN as Vuln Scanner<br/>(Qualys)",
            "    participant IAM as IAM<br/>(CyberArk + Azure AD)",
            "    participant BCM as BCM Platform<br/>(ServiceNow BCM)",
            "    participant VRM as Vendor Risk<br/>(ServiceNow VRM)",
            "    participant DW as Data Warehouse<br/>(Snowflake)",
            "    participant BI as BI Platform<br/>(Tableau)",
            "    participant CISO as Chief Info Security Officer",
            "    SIEM->>DW: Incidents, MTTR",
            "    VULN->>DW: Vuln scans, patch status",
            "    IAM->>DW: Access reviews, MFA coverage",
            "    BCM->>DW: BCP test results, RTO/RPO",
            "    VRM->>DW: Vendor assessments",
            "    DW->>BI: Security dashboard model",
            "    CISO->>BI: View security dashboard",
            "    BI-->>CISO: Security posture KPIs",
        ],
    },
    # ──────────────────────────────────────────────────────────────
    # 15. ENTERPRISE SERVICES DASHBOARD   (IN035)
    # ──────────────────────────────────────────────────────────────
    {
        "id": 15,
        "title": "Enterprise Services Dashboard",
        "acord_codes": ["IN035"],
        "business_question": "Are enterprise operations running efficiently?",
        "owner": "Chief Operating Officer",
        "description": (
            "Covers corporate functions: HR and payroll, financial accounting, "
            "procurement and vendor management, legal and contract management, and "
            "facilities. Provides a cost-centre view of enterprise operations with "
            "headcount trends, attrition, vendor performance, open legal cases, "
            "and facilities utilisation."
        ),
        "kpis": [
            ("Headcount (FTE)", "Total active employees", "Count (trend)", "Workday", "Monthly", "\u2014"),
            ("Attrition Rate", "Departures / avg headcount", "Line + Gauge", "Workday", "Monthly", "\u2014"),
            ("Open Positions", "Unfilled requisitions by department", "Bar", "Workday", "Monthly", "\u2014"),
            ("Time-to-Hire", "Avg days from req open to offer accepted", "Line", "Workday", "Monthly", "\u2014"),
            ("Active Vendors", "Vendors with active PO or contract", "Count", "SAP Procurement", "Monthly", "\u2014"),
            ("PO Value (YTD)", "Total purchase order value placed YTD", "Bar", "SAP Procurement", "Monthly", "\u2014"),
            ("Vendor Scorecard", "Avg vendor rating (quality, delivery, cost)", "Gauge + Table", "SAP Procurement", "Quarterly", "\u2014"),
            ("Legal Cases Open", "Active litigation and regulatory matters", "Count", "ServiceNow Legal", "Monthly", "\u2014"),
            ("Contract Expiry Calendar", "Contracts expiring within 6 months", "Timeline table", "ServiceNow Contracts", "Monthly", "\u2014"),
            ("Facilities Utilisation", "% of office space occupied", "Gauge", "Facilities Mgmt System", "Monthly", "\u2014"),
            ("HR Cost per FTE", "Total HR cost / headcount", "Line", "SAP GL", "Quarterly", "\u2014"),
            ("Finance Close TAT", "Days to complete month-end close", "Line", "SAP GL", "Monthly", "\u2014"),
        ],
        "filters": ["Department", "Cost Centre", "Vendor Category", "Time Period"],
        "drill_down": "Function > Cost Centre > Vendor/Employee > Transaction",
        "mermaid": [
            "sequenceDiagram",
            "    participant HR as HR System<br/>(Workday)",
            "    participant PROC as Procurement<br/>(SAP Procurement)",
            "    participant LEGAL as Legal Mgmt<br/>(ServiceNow Legal)",
            "    participant FM as Facilities Mgmt",
            "    participant GL as Finance GL<br/>(SAP)",
            "    participant DW as Data Warehouse<br/>(Snowflake)",
            "    participant BI as BI Platform<br/>(Tableau)",
            "    participant COO as Chief Operating Officer",
            "    HR->>DW: Headcount, attrition, hiring",
            "    PROC->>DW: POs, vendors, contracts",
            "    LEGAL->>DW: Legal cases, matters",
            "    FM->>DW: Space utilisation, costs",
            "    GL->>DW: Cost centre GL data",
            "    DW->>BI: Enterprise services model",
            "    COO->>BI: View enterprise dashboard",
            "    BI-->>COO: Operational efficiency KPIs",
        ],
    },
    # ──────────────────────────────────────────────────────────────
    # 16. IT & DIGITAL PLATFORMS DASHBOARD   (IN036)
    # ──────────────────────────────────────────────────────────────
    {
        "id": 16,
        "title": "IT & Digital Platform Operations Dashboard",
        "acord_codes": ["IN036"],
        "business_question": "Are our digital platforms reliable, performant, and cost-effective?",
        "owner": "Chief Information Officer",
        "description": (
            "Monitors IT operations across cloud infrastructure, API gateway performance, "
            "CI/CD pipeline health, testing coverage, service desk, and cloud cost "
            "management. Provides real-time and trend visibility into platform reliability, "
            "developer productivity, and IT financial management."
        ),
        "kpis": [
            ("API Uptime", "% of time API gateway is available", "Gauge", "Azure API Mgmt", "Real-time", "\u2014"),
            ("API Call Volume", "API requests per minute by endpoint", "Line (multi-series)", "Azure API Mgmt", "Real-time", "\u2014"),
            ("API Latency (P50/P95/P99)", "Response time in ms at percentiles", "Line", "Azure API Mgmt", "Real-time", "\u2014"),
            ("Deployment Frequency", "Production deployments per week", "Bar", "Azure DevOps", "Weekly", "\u2014"),
            ("Deployment Success Rate", "% of deployments without rollback", "Gauge", "Azure DevOps", "Weekly", "\u2014"),
            ("MTTR (Incidents)", "Mean time to resolve P1/P2 incidents", "Line", "ServiceNow ITSM", "Monthly", "\u2014"),
            ("Service Desk Tickets", "Tickets opened by category", "Bar (stacked)", "ServiceNow ITSM", "Weekly", "\u2014"),
            ("Ticket FCR Rate", "First-contact resolution rate", "Gauge", "ServiceNow ITSM", "Monthly", "\u2014"),
            ("Cloud Cost (Monthly)", "Monthly cloud infrastructure spend by provider", "Bar (stacked)", "Azure Cost Mgmt", "Monthly", "\u2014"),
            ("Cloud Cost per Transaction", "Cloud cost / API transactions", "Line", "Azure Cost Mgmt", "Monthly", "\u2014"),
            ("Test Coverage", "Code coverage % by criticality", "Gauge", "SonarQube + ADO", "Monthly", "\u2014"),
            ("SLA Adherence", "IT services meeting published SLAs", "Gauge", "ServiceNow ITSM", "Monthly", "\u2014"),
        ],
        "filters": ["Service", "Environment", "Cloud Provider", "Time Period"],
        "drill_down": "Service > API > Deployment > Incident > Ticket",
        "mermaid": [
            "sequenceDiagram",
            "    participant API as API Gateway<br/>(Azure API Mgmt)",
            "    participant DEVOPS as DevOps<br/>(Azure DevOps)",
            "    participant CLOUD as Cloud Infra<br/>(Azure / AWS)",
            "    participant ITSM as Service Desk<br/>(ServiceNow ITSM)",
            "    participant COST as Cloud Cost Mgmt<br/>(Azure Cost Mgmt)",
            "    participant DW as Data Warehouse<br/>(Snowflake)",
            "    participant BI as BI Platform<br/>(Tableau)",
            "    participant CIO as Chief Information Officer",
            "    API->>DW: Uptime, latency, call volume",
            "    DEVOPS->>DW: Deploy frequency, success",
            "    CLOUD->>DW: Resource utilisation",
            "    ITSM->>DW: Incidents, tickets",
            "    COST->>DW: Cloud spend by service",
            "    DW->>BI: IT operations model",
            "    CIO->>BI: View IT dashboard",
            "    BI-->>CIO: Platform reliability and cost KPIs",
        ],
    },
]
