"""Oracle Professional Intelligence — Dashboard (Streamlit).

Painel inicial do Oracle. Lê métricas da API quando disponível; cai para
zeros se a API ainda não estiver no ar.
"""
import os

import requests
import streamlit as st

API_BASE = os.getenv("ORACLE_API_BASE", "http://oracle-api.oracle-ai.svc.cluster.local:8000")

st.set_page_config(page_title="Oracle Professional Intelligence", layout="wide")
st.title("Oracle Professional Intelligence")
st.write(
    "Copiloto open source para LinkedIn, carreira, currículo, "
    "entrevistas e networking."
)


def fetch_stats():
    try:
        r = requests.get(f"{API_BASE}/stats", timeout=4)
        r.raise_for_status()
        return r.json(), None
    except Exception as exc:  # API/banco indisponível
        return {}, str(exc)


stats, err = fetch_stats()
if err:
    st.warning(f"API indisponível ({err}). Exibindo zeros.")

ssi = stats.get("ssi", "—")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("SSI atual", ssi)
    st.metric("Posts", stats.get("posts", 0))
with col2:
    st.metric("Vagas", stats.get("jobs", 0))
    st.metric("Recrutadores", stats.get("recruiters", 0))
with col3:
    st.metric("Currículos", stats.get("resumes", 0))
    st.metric("Entrevistas", stats.get("interviews", 0))

st.header("Gerar post de LinkedIn")
with st.form("gen_post"):
    topic = st.text_input("Tema", "Reduzir custo de EKS com Karpenter e Spot")
    language = st.selectbox("Idioma", ["pt-BR", "en"])
    submitted = st.form_submit_button("Gerar")
if submitted:
    with st.spinner("Gerando via LiteLLM (modelo local)..."):
        try:
            r = requests.post(
                f"{API_BASE}/generate/post",
                json={"topic": topic, "language": language},
                timeout=120,
            )
            r.raise_for_status()
            data = r.json()
            st.success(f"Rascunho salvo (post_id={data.get('post_id')})")
            st.write(data.get("content", ""))
        except Exception as exc:
            st.error(f"Falha ao gerar: {exc}")

st.header("Módulos")
st.markdown(
    """
- LinkedIn Intelligence
- Career Intelligence
- Resume Intelligence
- Interview Intelligence
- Recruiter Intelligence
- Knowledge Intelligence
"""
)

st.caption(f"API: {API_BASE}")
