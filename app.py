import streamlit as st
from rag_engine import get_answer

st.set_page_config(
    page_title="Groww Facts-Only MF Assistant",
    page_icon="📈",
    layout="centered"
)

# Header & Branding
st.markdown("<h2 style='text-align: center;'>📈 Groww Facts-Only Mutual Fund Assistant</h2>", unsafe_allow_html=True)
st.info("📌 **Notice:** Facts-only. No investment advice. Answers derived strictly from official AMC, AMFI, and SEBI filings.")

# Quick Evaluation Prompt Buttons
st.markdown("##### Example Questions:")
col1, col2, col3 = st.columns(3)

clicked_prompt = None
with col1:
    if st.button("🔒 HDFC ELSS Lock-in", use_container_width=True):
        clicked_prompt = "What is the lock-in period for HDFC ELSS Tax saver?"
with col2:
    if st.button("📉 Exit Load Rules", use_container_width=True):
        clicked_prompt = "What is the exit load structure for HDFC Liquid Fund within 7 days?"
with col3:
    if st.button("📄 Capital Gains Guide", use_container_width=True):
        clicked_prompt = "What is the capital gains tax rate on equity mutual funds held for more than 12 months?"

# Session State for Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User Input Handling
user_query = st.chat_input("Ask a factual question about HDFC Mutual Fund schemes...")
active_query = clicked_prompt if clicked_prompt else user_query

if active_query:
    st.session_state.messages.append({"role": "user", "content": active_query})
    with st.chat_message("user"):
        st.markdown(active_query)

    with st.chat_message("assistant"):
        with st.spinner("Retrieving verified facts..."):
            response_text = get_answer(active_query)
            st.markdown(response_text)
            st.session_state.messages.append({"role": "assistant", "content": response_text})

st.markdown("---")
st.caption("⚠️ **Disclaimer:** Facts-only, no advice. This assistant does not calculate returns, compare portfolios, or provide recommendations. Do not submit personal identification or account credentials.")