# Oracle Professional Intelligence

Copiloto profissional pessoal baseado em IA open source, rodando em Kubernetes
local. Centraliza LinkedIn, carreira, currículos, entrevistas, networking e
conhecimento em um único ecossistema — um "segundo cérebro profissional".

> Especificação completa (30 capítulos): [`oracle-professional-intelligence-v2.md`](oracle-professional-intelligence-v2.md).

## Status

MVP scaffold — camada de dados, IA local, API e dashboard prontos para deploy
no cluster **kind** já existente (`nxt-cluster-staging`). Demais camadas
(observabilidade, segurança, GitOps, MCPs, Telegram) documentadas no roadmap.

## Arquitetura (MVP)

```
oracle-ai     → Ollama, Open WebUI, LiteLLM, API (FastAPI), Dashboard (Streamlit)
oracle-data   → PostgreSQL + pgvector, Redis, MinIO
oracle-*      → mcp / automation / observability / security (planejados)
```

## Pré-requisitos

- Um cluster Kubernetes rodando (aqui: kind `nxt-cluster-staging`).
- `kubectl`, `helm`, `docker`, `kind`, `psql` no host.

> Nota kind: se `kube-proxy` cair com `too many open files`, eleve os limites de
> inotify do host (`fs.inotify.max_user_instances`). Ver [`docs/11-runbook.md`](docs/11-runbook.md).

## Subindo o MVP

```bash
cp .env.example .env          # ajuste se necessário
make bootstrap                # namespaces -> dados -> migrations -> IA -> apps
```

Ou passo a passo:

```bash
make namespaces
make data        # Postgres+pgvector, Redis, MinIO
make migrate     # cria o schema
make ai          # Ollama, Open WebUI, LiteLLM
make apps        # build + deploy da API e do dashboard
```

## Acesso

```bash
make port-api         # http://localhost:8000  (API, /health, /docs)
make port-dashboard   # http://localhost:8501  (Streamlit)
make port-openwebui   # http://localhost:3000  (chat com modelos)
make status
```

## Estrutura

```
apps/        API (FastAPI), dashboard (Streamlit), agents (CrewAI), workers
database/    migrations SQL (schema + pgvector)
kubernetes/  namespaces, manifestos base, helm-values
skills/      7 skills do Oracle (SKILL.md)
mcp/         configs de MCP
scripts/     bootstrap e instaladores por camada
docs/        documentação por capítulo
```

## Segurança / uso do LinkedIn

Toda ação pública no LinkedIn deve ter **revisão humana**. O Oracle gera
conteúdo e organiza dados; não automatiza publicação nem faz scraping agressivo.
