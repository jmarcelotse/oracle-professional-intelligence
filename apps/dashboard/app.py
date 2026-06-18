"""Oracle Professional Intelligence — Dashboard (Streamlit).

Painel do Oracle com abas para visão geral, geração de conteúdo, recrutadores,
vagas e posts. Tudo via API (sem curl).
"""
import os

import pandas as pd
import requests
import streamlit as st

API_BASE = os.getenv("ORACLE_API_BASE", "http://oracle-api.oracle-ai.svc.cluster.local:8000")

st.set_page_config(page_title="Oracle Professional Intelligence", layout="wide")


def api_get(path, **params):
    r = requests.get(f"{API_BASE}{path}", params=params, timeout=10)
    r.raise_for_status()
    return r.json()


def api_post(path, payload, timeout=120):
    r = requests.post(f"{API_BASE}{path}", json=payload, timeout=timeout)
    r.raise_for_status()
    return r.json()


st.title("Oracle Professional Intelligence")
st.caption(f"API: {API_BASE}")

tab_home, tab_post, tab_rec, tab_jobs, tab_posts = st.tabs(
    ["📊 Visão geral", "✍️ Gerar post", "🤝 Recrutadores", "💼 Vagas", "📝 Posts"]
)

# --------------------------------------------------------------------------- #
# Visão geral
# --------------------------------------------------------------------------- #
with tab_home:
    try:
        s = api_get("/stats")
        c1, c2, c3 = st.columns(3)
        c1.metric("Posts", s.get("posts", 0))
        c1.metric("Currículos", s.get("resumes", 0))
        c2.metric("Vagas", s.get("jobs", 0))
        c2.metric("Entrevistas", s.get("interviews", 0))
        c3.metric("Recrutadores", s.get("recruiters", 0))
    except Exception as exc:
        st.error(f"API indisponível: {exc}")
    st.markdown(
        "**Módulos:** LinkedIn · Career · Resume · Interview · Recruiter · Knowledge Intelligence"
    )

# --------------------------------------------------------------------------- #
# Gerar post
# --------------------------------------------------------------------------- #
with tab_post:
    st.subheader("Gerar post de LinkedIn")
    with st.form("gen_post"):
        topic = st.text_input("Tema", "Lições de um incidente de produção em EKS")
        language = st.selectbox("Idioma", ["pt-BR", "en"], key="post_lang")
        ok = st.form_submit_button("Gerar")
    if ok:
        with st.spinner("Gerando..."):
            try:
                d = api_post("/generate/post", {"topic": topic, "language": language})
                st.success(f"Rascunho salvo (post_id={d.get('post_id')})")
                st.text_area("Conteúdo", d.get("content", ""), height=400)
            except Exception as exc:
                st.error(f"Falha: {exc}")

# --------------------------------------------------------------------------- #
# Recrutadores
# --------------------------------------------------------------------------- #
with tab_rec:
    st.subheader("Gerar mensagem para recrutador")
    with st.form("gen_outreach"):
        col1, col2 = st.columns(2)
        rname = col1.text_input("Nome do recrutador", "Maria")
        rcompany = col2.text_input("Empresa", "Datadog")
        rrole = col1.text_input("Cargo de interesse", "Senior SRE")
        rlang = col2.selectbox("Idioma", ["en", "pt-BR", "es"], key="out_lang")
        gen_ok = st.form_submit_button("Gerar mensagem")
    if gen_ok:
        with st.spinner("Gerando..."):
            try:
                d = api_post(
                    "/generate/outreach",
                    {"recruiter_name": rname, "company": rcompany,
                     "target_role": rrole, "language": rlang},
                )
                st.text_area("Mensagem", d.get("message", ""), height=180)
            except Exception as exc:
                st.error(f"Falha: {exc}")

    st.divider()
    st.subheader("Cadastrar recrutador")
    with st.form("add_rec"):
        col1, col2 = st.columns(2)
        n = col1.text_input("Nome")
        comp = col2.text_input("Empresa ", key="rec_comp")
        role = col1.text_input("Função (ex.: Tech Recruiter)")
        country = col2.text_input("País")
        add_ok = st.form_submit_button("Salvar")
    if add_ok and n:
        try:
            api_post("/recruiters", {"name": n, "company": comp, "role": role,
                                     "country": country, "status": "new"})
            st.success("Recrutador salvo.")
        except Exception as exc:
            st.error(f"Falha: {exc}")

    st.subheader("Recrutadores cadastrados")
    try:
        recs = api_get("/recruiters")
        if recs:
            st.dataframe(pd.DataFrame(recs), use_container_width=True, hide_index=True)
        else:
            st.info("Nenhum recrutador ainda.")
    except Exception as exc:
        st.error(f"Falha ao listar: {exc}")

# --------------------------------------------------------------------------- #
# Vagas
# --------------------------------------------------------------------------- #
with tab_jobs:
    st.subheader("Cadastrar vaga")
    with st.form("add_job"):
        col1, col2 = st.columns(2)
        title = col1.text_input("Título")
        company = col2.text_input("Empresa", key="job_comp")
        location = col1.text_input("Local")
        stack = col2.text_input("Stack (ex.: Kubernetes, AWS)")
        url = col1.text_input("URL da vaga")
        remote = col2.checkbox("Remota", value=True)
        job_ok = st.form_submit_button("Salvar")
    if job_ok and title:
        try:
            api_post("/jobs", {"title": title, "company": company, "location": location,
                               "stack": stack, "job_url": url, "remote": remote,
                               "status": "new"})
            st.success("Vaga salva.")
        except Exception as exc:
            st.error(f"Falha: {exc}")

    st.subheader("Vagas cadastradas")
    try:
        jobs = api_get("/jobs")
        if jobs:
            cols = ["id", "title", "company", "location", "remote", "stack", "status", "created_at"]
            df = pd.DataFrame(jobs)
            st.dataframe(df[[c for c in cols if c in df.columns]],
                         use_container_width=True, hide_index=True)
        else:
            st.info("Nenhuma vaga ainda.")
    except Exception as exc:
        st.error(f"Falha ao listar: {exc}")

# --------------------------------------------------------------------------- #
# Posts
# --------------------------------------------------------------------------- #
with tab_posts:
    st.subheader("Posts gerados (rascunhos)")
    st.caption("Revise e publique manualmente no LinkedIn.")
    try:
        posts = api_get("/posts")
        if posts:
            for p in posts:
                with st.expander(f"#{p['id']} — {p.get('topic') or p.get('title') or 'post'} ({p.get('status')})"):
                    st.write(p.get("content", ""))
        else:
            st.info("Nenhum post ainda. Gere um na aba 'Gerar post'.")
    except Exception as exc:
        st.error(f"Falha ao listar: {exc}")
