import streamlit as st
import math

def poisson(mu, k):
    return (math.exp(-mu) * (mu**k)) / math.factorial(k)

st.set_page_config(page_title="Dica Certa", layout="centered")
st.title("⚽ Dica Certa Predictor")

# Entrada de Dados
p1 = st.text_input("Nome do Player 1", "Casa")
p2 = st.text_input("Nome do Player 2", "Visitante")
m1 = st.number_input(f"Média de Gols Marcados ({p1})", value=2.0)
m2 = st.number_input(f"Média de Gols Sofridos ({p2})", value=1.5)

if st.button("CALCULAR GREEN"):
    exp = (m1 + m2) / 2
    p15 = (1 - sum(poisson(exp, i) for i in range(2))) * 100
    p25 = (1 - sum(poisson(exp, i) for i in range(3))) * 100
    
    st.subheader(f"📊 Análise: {p1} vs {p2}")
    st.write(f"**Probabilidade Over 1.5:** {p15:.2f}%")
    st.write(f"**Probabilidade Over 2.5:** {p25:.2f}%")
    
    if p25 > 70:
        st.success("🔥 DICA: ENTRADA FORTE NO OVER 2.5")
    else:
        st.warning("⚠️ Jogo para análise cautelosa.")
