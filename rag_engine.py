import os
import re
from pathlib import Path
from dotenv import load_dotenv
from google import genai

load_dotenv()

DATA_DIR = Path("./data")

SOURCE_MAP = {
    # 1. Scheme Information Documents (SIDs)
    "hdfc_top_100_sid.txt": "https://www.hdfcfund.com/product-solutions/equity/hdfc-top-100-fund",
    "hdfc_flexi_cap_sid.txt": "https://www.hdfcfund.com/product-solutions/equity/hdfc-flexi-cap-fund",
    "hdfc_elss_taxsaver_sid.txt": "https://www.hdfcfund.com/product-solutions/equity/hdfc-elss-tax-saver",
    "hdfc_mid_cap_opp_sid.txt": "https://www.hdfcfund.com/product-solutions/equity/hdfc-mid-cap-opportunities-fund",
    "hdfc_small_cap_sid.txt": "https://www.hdfcfund.com/product-solutions/equity/hdfc-small-cap-fund",
    "hdfc_balanced_advantage_sid.txt": "https://www.hdfcfund.com/product-solutions/hybrid/hdfc-balanced-advantage-fund",
    "hdfc_liquid_fund_sid.txt": "https://www.hdfcfund.com/product-solutions/debt/hdfc-liquid-fund",
    "hdfc_corporate_bond_sid.txt": "https://www.hdfcfund.com/product-solutions/debt/hdfc-corporate-bond-fund",

    # 2. Factsheets & Disclosures
    "hdfc_equity_factsheet.txt": "https://www.hdfcfund.com/statutory-disclosure/factsheets",
    "hdfc_debt_factsheet.txt": "https://www.hdfcfund.com/statutory-disclosure/factsheets",

    # 3. Systematic Transaction FAQs
    "hdfc_sip_faq.txt": "https://www.hdfcfund.com/investor-desk/faqs/sip",
    "hdfc_stp_swp_faq.txt": "https://www.hdfcfund.com/investor-desk/faqs/systematic-transactions",
    "hdfc_cutoff_timings_faq.txt": "https://www.hdfcfund.com/investor-desk/transaction-cut-off-timings",

    # 4. Fee & Expense Disclosures
    "hdfc_ter_schedule.txt": "https://www.hdfcfund.com/statutory-disclosure/total-expense-ratio-ter",
    "stamp_duty_charges.txt": "https://www.amfiindia.com/investor-corner/knowledge-center/stamp-duty.html",

    # 5. Regulatory Circulars, Riskometer & Taxation
    "sebi_categorization_circular.txt": "https://www.sebi.gov.in/legal/master-circulars/",
    "amfi_riskometer_guidelines.txt": "https://www.amfiindia.com/investor-corner/knowledge-center/riskometer.html",
    "amfi_taxation_guide.txt": "https://www.amfiindia.com/investor-corner/knowledge-center/tax-corner.html",
    "hdfc_kyc_nomination_rules.txt": "https://www.hdfcfund.com/investor-desk/kyc-compliance",
    "hdfc_statements_guide.txt": "https://www.hdfcfund.com/investor-desk/online-services/capital-gains-statement"
}

def load_corpus():
    docs = []
    if DATA_DIR.exists():
        for file in DATA_DIR.glob("*.txt"):
            text = file.read_text(encoding="utf-8")
            url = SOURCE_MAP.get(file.name, "https://www.hdfcfund.com")
            docs.append({"content": text, "source_url": url, "filename": file.name})
    return docs

CORPUS = load_corpus()

api_key = os.getenv("GOOGLE_API_KEY")
client = genai.Client(api_key=api_key)

SYSTEM_PROMPT = """You are the Groww Facts-Only Mutual Fund Assistant.
Answer the user query strictly using the facts provided in the context below.

Mandatory Constraints:
1. Brevity: Deliver the factual answer in at most 3 clear sentences.
2. Citation: Append exactly one official citation link at the end using: [Source: <URL>].
3. Timestamp: Add the exact string: "Last updated from sources: September 2026." at the end.
4. If the provided context does not contain the answer, state that the specific fact is unavailable in official filings and cite: [Source: https://www.hdfcfund.com].
"""

def detect_pii(text: str) -> bool:
    """Detects phone numbers, emails, PAN cards, or generic government ID formats."""
    pan_pattern = r'[A-Z]{5}[0-9]{4}[A-Z]{1}'
    email_pattern = r'[\w\.-]+@[\w\.-]+'
    phone_pattern = r'\b[6-9]\d{9}\b'
    generic_id = r'\b\d{4}\s?\d{4}\s?\d{4}\b'
    return bool(
        re.search(pan_pattern, text, re.I)
        or re.search(email_pattern, text)
        or re.search(phone_pattern, text)
        or re.search(generic_id, text)
    )

def is_advice_query(text: str) -> bool:
    """Flags subjective recommendation or comparison prompts."""
    keywords = [
        "should i", "recommend", "best fund", "buy or sell",
        "which is better", "where should i invest", "good to buy"
    ]
    return any(kw in text.lower() for kw in keywords)

def get_answer(query: str) -> str:
    # 1. PII Safety Guardrail
    if detect_pii(query):
        return (
            "Please do not share sensitive personal identifiers or account details. "
            "I can only help with general, factual mutual fund questions."
        )

    # 2. Advisory Refusal Guardrail
    if is_advice_query(query):
        return (
            "I cannot provide investment advice, scheme recommendations, or portfolio selections. "
            "You can review standard categorization principles and risk factors directly on the AMFI educational portal: "
            "[Source: https://www.amfiindia.com/investor-corner/knowledge-center].\n\n"
            "Last updated from sources: September 2026."
        )

    if not CORPUS:
        return "Corpus data not found in ./data directory. Please run generate_corpus.py first."

    # 3. Keyword-Relevance Retrieval
    query_tokens = set(re.findall(r'\w+', query.lower()))
    ranked = []
    for doc in CORPUS:
        score = sum(1 for token in query_tokens if token in doc["content"].lower())
        ranked.append((score, doc))

    ranked.sort(key=lambda x: x[0], reverse=True)
    best_doc = ranked[0][1] if ranked and ranked[0][0] > 0 else CORPUS[0]

    context_text = best_doc["content"]
    source_url = best_doc["source_url"]

    prompt = f"""{SYSTEM_PROMPT}

Context:
{context_text}

Official Citation Source: {source_url}
User Question: {query}
"""

    # 4. LLM Generation via Chat interface with active model fallbacks
    candidate_models = [
        "gemini-3.5-flash-lite",
        "gemini-3.8-flash",
        "gemini-3.5-flash"
    ]

    last_error = ""
    for model_name in candidate_models:
        try:
            chat = client.chats.create(model=model_name)
            response = chat.send_message(prompt)
            if response.text:
                return response.text
        except Exception as e:
            last_error = str(e)
            continue

    return f"Service temporarily busy across endpoints: {last_error}"