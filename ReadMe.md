# Groww Facts-Only Mutual Fund Assistant (RAG)

A regulatory-compliant, facts-only Mutual Fund RAG Assistant designed to answer factual scheme, taxation, and procedural queries using verified public documents from Asset Management Companies (AMCs), SEBI, and AMFI.

## Key Features & Guardrails
- **Strict Factual Brevity**: Answers queries strictly using retrieved corpus context in at most 3 clear sentences.
- **Mandatory Sourcing & Timestamping**: Every factual reply appends an exact source link (`[Source: <URL>]`) and regulatory cut-off timestamp (`Last updated from sources: September 2026.`).
- **SEBI Investment Advice Refusal**: Automatically intercepts portfolio advice, fund comparisons, and buy/sell recommendations, declining to advise and redirecting users to the AMFI Knowledge Center.
- **Privacy & PII Interception**: Pre-execution regex filtering intercepts PAN cards, emails, contact numbers, and personal identifiers before passing prompts to the LLM.
- **Multi-Model Fallback Engine**: Implements resilient failover across Google Gemini models (`gemini-3.5-flash-lite`, `gemini-3.8-flash`, `gemini-3.5-flash`) via the `google-genai` SDK.

---

## 20-Page Grounded Corpus Source List

The assistant's knowledge base is grounded across 20 verified public filings, circulars, and disclosures:

| S.No | Document Name | Category | Official Source Citation |
|---|---|---|---|
| 1 | `hdfc_top_100_sid.txt` | Scheme SID | https://www.hdfcfund.com/product-solutions/equity/hdfc-top-100-fund |
| 2 | `hdfc_flexi_cap_sid.txt` | Scheme SID | https://www.hdfcfund.com/product-solutions/equity/hdfc-flexi-cap-fund |
| 3 | `hdfc_elss_taxsaver_sid.txt` | Scheme SID | https://www.hdfcfund.com/product-solutions/equity/hdfc-elss-tax-saver |
| 4 | `hdfc_mid_cap_opp_sid.txt` | Scheme SID | https://www.hdfcfund.com/product-solutions/equity/hdfc-mid-cap-opportunities-fund |
| 5 | `hdfc_small_cap_sid.txt` | Scheme SID | https://www.hdfcfund.com/product-solutions/equity/hdfc-small-cap-fund |
| 6 | `hdfc_balanced_advantage_sid.txt` | Scheme SID | https://www.hdfcfund.com/product-solutions/hybrid/hdfc-balanced-advantage-fund |
| 7 | `hdfc_liquid_fund_sid.txt` | Scheme SID | https://www.hdfcfund.com/product-solutions/debt/hdfc-liquid-fund |
| 8 | `hdfc_corporate_bond_sid.txt` | Scheme SID | https://www.hdfcfund.com/product-solutions/debt/hdfc-corporate-bond-fund |
| 9 | `hdfc_equity_factsheet.txt` | Factsheet | https://www.hdfcfund.com/statutory-disclosure/factsheets |
| 10 | `hdfc_debt_factsheet.txt` | Factsheet | https://www.hdfcfund.com/statutory-disclosure/factsheets |
| 11 | `hdfc_sip_faq.txt` | Scheme FAQ | https://www.hdfcfund.com/investor-desk/faqs/sip |
| 12 | `hdfc_stp_swp_faq.txt` | Scheme FAQ | https://www.hdfcfund.com/investor-desk/faqs/systematic-transactions |
| 13 | `hdfc_cutoff_timings_faq.txt` | Transaction Guide | https://www.hdfcfund.com/investor-desk/transaction-cut-off-timings |
| 14 | `hdfc_ter_schedule.txt` | Fee/TER Schedule | https://www.hdfcfund.com/statutory-disclosure/total-expense-ratio-ter |
| 15 | `stamp_duty_charges.txt` | Fee/Charges | https://www.amfiindia.com/investor-corner/knowledge-center/stamp-duty.html |
| 16 | `sebi_categorization_circular.txt` | SEBI Circular | https://www.sebi.gov.in/legal/master-circulars/ |
| 17 | `amfi_riskometer_guidelines.txt` | AMFI Riskometer | https://www.amfiindia.com/investor-corner/knowledge-center/riskometer.html |
| 18 | `amfi_taxation_guide.txt` | Taxation Guide | https://www.amfiindia.com/investor-corner/knowledge-center/tax-corner.html |
| 19 | `hdfc_kyc_nomination_rules.txt` | Investor Guide | https://www.hdfcfund.com/investor-desk/kyc-compliance |
| 20 | `hdfc_statements_guide.txt` | Tax-Doc Guide | https://www.hdfcfund.com/investor-desk/online-services/capital-gains-statement |

---

## Sample Q&A Test Scenarios

### 1. Factual Scheme Question (Lock-in Period)
- **User Question:** "What is the mandatory lock-in period for HDFC ELSS Tax saver?"
- **Assistant Response:**
  > HDFC ELSS Tax saver has a mandatory statutory lock-in period of 3 years from the date of unit allotment. In the case of SIP investments, each individual installment is subject to an independent 3-year lock-in period. Units cannot be redeemed, transferred, or pledged prior to the completion of this duration.
  >
  > [Source: https://www.hdfcfund.com/product-solutions/equity/hdfc-elss-tax-saver]
  >
  > Last updated from sources: September 2026.

### 2. Systematic & Regulatory Guidelines (Exit Load on Liquid Funds)
- **User Question:** "What is the exit load for HDFC Liquid Fund within 7 days?"
- **Assistant Response:**
  > HDFC Liquid Fund levies a graded exit load starting at 0.0070% on Day 1, which reduces each day down to 0.0045% on Day 6. Redemptions on or after Day 7 carry zero exit load.
  >
  > [Source: https://www.hdfcfund.com/product-solutions/debt/hdfc-liquid-fund]
  >
  > Last updated from sources: September 2026.

### 3. SEBI Advisory Refusal Guardrail Trigger
- **User Question:** "Should I invest in HDFC Top 100 or HDFC Flexi Cap for higher returns?"
- **Assistant Response:**
  > I cannot provide investment advice, scheme recommendations, or portfolio selections. You can review standard categorization principles and risk factors directly on the AMFI educational portal: [Source: https://www.amfiindia.com/investor-corner/knowledge-center].
  >
  > Last updated from sources: September 2026.

### 4. PII Redaction & Data Privacy Guardrail Trigger
- **User Question:** "My PAN is ABCDE1234F, show my mutual fund statement."
- **Assistant Response:**
  > Please do not share sensitive personal identifiers or account details. I can only help with general, factual mutual fund questions.

---

## Regulatory Compliance Disclaimer

> **Disclaimer:** This assistant provides purely factual information extracted directly from statutory Scheme Information Documents (SIDs), SEBI circulars, and AMFI guidelines. It does not provide financial planning, calculate returns, compare portfolios, or provide investment advice. Mutual fund investments are subject to market risks; read all scheme-related documents carefully.