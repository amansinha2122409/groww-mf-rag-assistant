import os
from pathlib import Path

DATA_DIR = Path("./data")
DATA_DIR.mkdir(parents=True, exist_ok=True)

DOCUMENTS = {
    # 1. Scheme Information Documents (SIDs)
    "hdfc_top_100_sid.txt": """HDFC Top 100 Fund - Scheme Information Document (SID)
Category: Large Cap Fund.
Investment Objective: To provide long-term capital appreciation by investing predominantly in large-cap stocks.
Asset Allocation: Minimum 80% of total assets invested in equity and equity-related instruments of large-cap companies (top 100 companies by market capitalization). Up to 20% in debt and money market instruments.
Benchmark: NIFTY 100 Total Return Index (TRI).
Exit Load: 1% if redeemed within 1 year from the date of allotment. Nil after 1 year.
Minimum Investment: Initial lump sum minimum is Rs 100; minimum additional purchase is Rs 100.""",

    "hdfc_flexi_cap_sid.txt": """HDFC Flexi Cap Fund - Scheme Information Document (SID)
Category: Flexi Cap Fund.
Investment Objective: To generate capital appreciation from a dynamically managed portfolio of equity & equity related securities across large, mid, and small cap market capitalizations.
Asset Allocation: Minimum 65% of total assets invested in equity and equity-related securities at all times. Remaining can be in debt, REITs, or InvITs.
Benchmark: NIFTY 500 TRI.
Exit Load: 1% if redeemed within 1 year. Nil after 1 year from the allotment date.
Fund Manager: Managed dynamically across market sectors without fixed cap limits.""",

    "hdfc_elss_taxsaver_sid.txt": """HDFC ELSS Tax saver - Scheme Information Document (SID)
Category: Equity Linked Savings Scheme (ELSS).
Investment Objective: To generate capital growth along with tax rebate under Section 80C of the Income Tax Act.
Mandatory Lock-in Period: 3 years statutory lock-in from the date of each allotment. Units cannot be redeemed, transferred, or pledged during this 3-year period. In SIPs, each individual instalment carries an independent 3-year lock-in.
Asset Allocation: Minimum 80% invested in equity and equity-related instruments.
Exit Load: Nil (post completion of the statutory 3-year lock-in period).
Benchmark: NIFTY 500 TRI.""",

    "hdfc_mid_cap_opp_sid.txt": """HDFC Mid-Cap Opportunities Fund - Scheme Information Document (SID)
Category: Mid Cap Fund.
Investment Objective: To provide capital appreciation by investing primarily in mid-cap companies.
Asset Allocation: Minimum 65% of total assets invested in equity and equity-related instruments of mid-cap companies (101st to 250th company by market cap).
Benchmark: NIFTY Midcap 150 TRI.
Exit Load: 1% if redeemed within 1 year from allotment date. Nil after 1 year.
Riskometer: Very High Risk.""",

    "hdfc_small_cap_sid.txt": """HDFC Small Cap Fund - Scheme Information Document (SID)
Category: Small Cap Fund.
Investment Objective: To generate long-term capital appreciation from an actively managed portfolio predominantly consisting of small-cap equity securities.
Asset Allocation: Minimum 65% of total assets in equity and equity-related instruments of small-cap companies (251st company onwards by market cap).
Benchmark: S&P BSE 250 SmallCap TRI.
Exit Load: 1% if redeemed/switched out within 1 year from date of allotment. Nil after 1 year.
Restrictions: Lump sum purchases may be capped or suspended by AMC based on capacity constraints.""",

    "hdfc_balanced_advantage_sid.txt": """HDFC Balanced Advantage Fund - Scheme Information Document (SID)
Category: Dynamic Asset Allocation or Balanced Advantage Fund.
Investment Objective: Capital appreciation and income distribution by investing dynamically in a mix of equity and debt instruments.
Asset Allocation: Equity allocation dynamically managed between 0% and 100%; debt allocation dynamically managed between 0% and 100%. Gross equity exposure is typically maintained above 65% for equity tax status.
Benchmark: NIFTY 50 Hybrid Composite Debt 50:50 Index.
Exit Load: In respect of each purchase, up to 15% of units may be redeemed without exit load within 1 year. For excess over 15%, 1% exit load applies if redeemed within 1 year. Nil after 1 year.""",

    "hdfc_liquid_fund_sid.txt": """HDFC Liquid Fund - Scheme Information Document (SID)
Category: Liquid Fund.
Investment Objective: To generate optimal returns with high liquidity and safety through investments in debt and money market instruments.
Maturity Profile: Invests strictly in securities with a residual maturity of up to 91 days only.
Exit Load: Graded exit load applies for redemptions within 7 days: Day 1: 0.0070%, Day 2: 0.0065%, Day 3: 0.0060%, Day 4: 0.0055%, Day 5: 0.0050%, Day 6: 0.0045%, Day 7 onwards: Nil.
Benchmark: CRISIL Liquid Debt A-I Index.""",

    "hdfc_corporate_bond_sid.txt": """HDFC Corporate Bond Fund - Scheme Information Document (SID)
Category: Corporate Bond Fund.
Investment Objective: To generate regular income and capital preservation by investing in corporate bonds.
Asset Allocation: Minimum 80% of total assets invested in highest rated corporate bonds (AA+ and above rated debt instruments).
Macaulay Duration: Macaulay duration is managed flexibly based on the interest rate environment.
Exit Load: Nil.
Benchmark: NIFTY Corporate Bond Index B-III.""",

    # 2. Factsheets & Disclosures
    "hdfc_equity_factsheet.txt": """HDFC AMC Equity Factsheet Disclosures
Portfolio Turnover Ratio: Calculated as the lesser of purchases or sales divided by average monthly net assets. For large-cap equity funds, typical turnover is between 15% and 35%.
AUM Disclosure: Scheme Average Assets Under Management (AAUM) are published on monthly basis on AMC portal and AMFI within 10 days of month-end.
Cash Allocation: Scheme equity cash levels are maintained below 10% under normal market conditions.
Fund Managers: Equity funds have designated chief and co-fund managers disclosed in monthly factsheets.""",

    "hdfc_debt_factsheet.txt": """HDFC AMC Debt & Hybrid Factsheet Disclosures
Modified Duration: Reflects scheme interest rate sensitivity. Lower duration indicates lower sensitivity to rate fluctuations.
Yield to Maturity (YTM): Indicates expected annual rate of return assuming all underlying debt holdings are held to maturity without default.
Credit Rating Composition: Factsheets categorize debt portfolio percentages into AAA, AA+, AA, sovereign treasury bills, and cash equivalents.""",

    # 3. Systematic Transaction FAQs
    "hdfc_sip_faq.txt": """HDFC Mutual Fund SIP FAQs & Rules
SIP Dates: Investors can choose any date between 1st and 28th of each month for auto-debit.
Minimum SIP Installment: Rs 100 per month for equity schemes, Rs 500 per month for specialized funds.
SIP Pause Facility: Investors can pause their SIP for up to 3 to 6 months by submitting a request 15 business days prior to next debit date.
SIP Modification: Modifying SIP mandate amount requires cancellation of old mandate and registering a fresh e-mandate.""",

    "hdfc_stp_swp_faq.txt": """HDFC Mutual Fund STP & SWP Guidelines
Systematic Transfer Plan (STP): Allows periodic transfer from a source scheme (usually liquid/debt) to a target scheme (equity). Minimum 6 installments required.
Systematic Withdrawal Plan (SWP): Enables fixed periodic redemptions from mutual fund units directly to registered investor bank account.
Taxation on SWP: Each SWP installment is treated as a partial redemption subject to capital gains tax as per scheme holding period rules.
Processing Timelines: SWP requests are processed on chosen cycle date, and proceeds are credited within T+1 to T+2 business days.""",

    "hdfc_cutoff_timings_faq.txt": """Mutual Fund Transaction Processing & Cut-off Timings
Liquid and Overnight Schemes: For purchase applications received up to 1:30 PM with funds credited before 1:30 PM, historical previous business day NAV applies. Applications after 1:30 PM receive same-day NAV.
Other Schemes (Equity, Hybrid, Debt): Cut-off time for purchases and redemptions is 3:00 PM.
Fund Realization Rule: NAV allocation across equity schemes is strictly subject to funds being credited to AMC collection account before cut-off time (3:00 PM), regardless of application submission time.""",

    # 4. Fee Structures & TER Schedules
    "hdfc_ter_schedule.txt": """HDFC Mutual Fund Total Expense Ratio (TER) Schedule
Direct Plan vs Regular Plan: Direct plans have lower expense ratios because no distributor commissions or brokerage are paid. Regular plans include distributor commissions.
Regulatory Caps: SEBI mandates maximum TER limits on equity schemes based on AUM slabs: up to Rs 500 cr is 2.25%, next 250 cr is 2.00%, next 1250 cr is 1.75%, tapering down as AUM grows.
Daily Calculation: TER is calculated and accrued on the daily net assets of the scheme and adjusted in the daily closing Net Asset Value (NAV).""",

    "stamp_duty_charges.txt": """Mutual Fund Stamp Duty & Transaction Charges
Stamp Duty: In accordance with Indian Stamp Act amendments, 0.005% stamp duty is levied on all mutual fund purchases (Lump sum, SIP, STP inflow, dividend reinvestment).
Deduction: Stamp duty is deducted directly from invested gross amount prior to allotment of units.
Transaction Charges: Distributors registered under AMFI can opt to receive Rs 100 transaction charge for existing investors and Rs 150 for first-time investors on transactions of Rs 10,000 and above.""",

    # 5. Regulatory Circulars, Riskometer & Taxation
    "sebi_categorization_circular.txt": """SEBI Circular on Categorization and Rationalization of Mutual Fund Schemes
SEBI Mandate: Only one scheme per category allowed per mutual fund company, with exceptions for Index Funds/ETFs, Sectoral/Thematic Funds, and Fund of Funds.
Large Cap Definition: 1st to 100th company in terms of full market capitalization.
Mid Cap Definition: 101st to 250th company in terms of full market capitalization.
Small Cap Definition: 251st company onwards in terms of full market capitalization.
Review: The list of market cap categorizations is published semi-annually by AMFI.""",

    "amfi_riskometer_guidelines.txt": """AMFI & SEBI Risk-o-meter Guidelines
Riskometer Levels: Mutual fund schemes are mapped into six standard risk categories: Low, Low to Moderate, Moderate, Moderately High, High, and Very High.
Monthly Evaluation: Risk-o-meter must be evaluated on a monthly basis based on the actual asset allocation and portfolio holdings at month-end.
Debt Scheme Risk Score: Evaluated based on Credit Risk Value, Interest Rate Risk Value, and Liquidity Risk Value.
Equity Scheme Risk Score: Evaluated based on Market Capitalization, Volatility, and Impact Cost of individual stock holdings.""",

    "amfi_taxation_guide.txt": """AMFI Capital Gains Taxation Guidelines for Mutual Funds
Equity Schemes (Holding period > 12 months): Long-term capital gains (LTCG) over Rs 1.25 lakh per financial year are taxed at 12.5% without indexation.
Equity Schemes (Holding period <= 12 months): Short-term capital gains (STCG) are taxed at 20%.
Specified Debt Schemes (Acquired on or after April 1, 2023): Gains are treated as short-term capital gains irrespective of holding period and taxed at applicable investor income tax slab rate.
Securities Transaction Tax (STT): 0.001% STT is deducted on redemption of equity mutual fund units.""",

    "hdfc_kyc_nomination_rules.txt": """KYC Compliance & Nomination Guidelines
KYC Compliance: Central KYC (CKYC) registration is mandatory for all mutual fund investors. Unregistered PANs or non-validated Aadhaar-PAN links restrict new financial investments.
Nomination Mandate: Individual investors must register up to three nominees for their mutual fund folios or submit an official nomination opt-out declaration.
Folio Freezing: Folios with non-compliant KYC or missing nomination instructions are subject to regulatory restrictions on fresh purchases and redemptions.""",

    "hdfc_statements_guide.txt": """HDFC Mutual Fund Capital Gains & Account Statement Guide
Consolidated Account Statement (CAS): Dispatched monthly across all AMCs via CAMS/KFintech showing all transactions and folio holdings across mutual funds.
Capital Gains Statement: Available for download from HDFC AMC online portal or investor desk at financial year end.
Realized vs Unrealized Gains: Capital gains statements reflect only realized gains on redeemed units. Unrealized portfolio gains do not attract taxation until redemption."""
}

for filename, content in DOCUMENTS.items():
    file_path = DATA_DIR / filename
    file_path.write_text(content.strip(), encoding="utf-8")

print(f"Success: Created {len(DOCUMENTS)} official regulatory/AMC documents in {DATA_DIR.resolve()}")