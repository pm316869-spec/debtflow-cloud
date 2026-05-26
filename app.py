import streamlit as st
import requests

API_URL = "https://debtflow-cloud.onrender.com/api"

st.set_page_config(page_title="DebtFlow", page_icon="💰", layout="wide")

st.title("💰 DebtFlow - Qarzlar")

try:
    r1 = requests.get(f"{API_URL}/qarzlar")
    r2 = requests.get(f"{API_URL}/jami")
    qarzlar = r1.json()
    jami = r2.json()
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Jami USD", f"${jami['jami_usd']:,.2f}")
    col2.metric("Jami SO'M", f"{jami['jami_uzs']:,.2f}")
    col3.metric("Mijozlar soni", jami['soni'])
    
    for q in qarzlar:
        st.markdown(f"""
        <div style="background:#1e1e2e; border-radius:15px; padding:15px; margin:10px 0; border-left:5px solid #4CAF50;">
            <b>{q['ism']}</b><br>
            💵 USD: {q['usd_qarz']:,.2f} | 💶 SO'M: {q['uzs_qarz']:,.2f}<br>
            📅 {q.get('beriladigan_sana', '-')}
        </div>
        """, unsafe_allow_html=True)
except:
    st.error("❌ Ulanish xatosi!")