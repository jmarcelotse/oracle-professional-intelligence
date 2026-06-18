# Arquitetura (as-built)

Este documento descreve o que **foi de fato implantado**, que difere em alguns
pontos do spec original (`oracle-professional-intelligence-v2.md`). Os desvios
estão justificados ao final.

## Visão geral

```
Cluster kind: nxt-cluster-staging (K8s v1.35, 1 control-plane + 3 workers)

oracle-data            Postgres+pgvector · Redis · MinIO
oracle-ai              Ollama · LiteLLM · Open WebUI · API (FastAPI) · Dashboard (Streamlit)
oracle-automation      n8n
oracle-observability   Prometheus · Grafana
oracle-security        Kyverno · Trivy Operator
```

## Fluxo principal

```
n8n (agenda) → API /generate/post → LiteLLM → Ollama (qwen2.5-coder:1.5b)
            → grava rascunho no Postgres → revisão no Dashboard / Open WebUI
```

## Camada de dados (oracle-data)

- **PostgreSQL 16 + pgvector 0.8.2** — StatefulSet próprio (imagem oficial
  `pgvector/pgvector:pg16`), 12 tabelas, índice ivfflat para busca semântica.
- **Redis 7** — cache/filas (sem auth, lab local), PVC AOF.
- **MinIO** — objetos (bucket `oracle-files`), API 9000 + console 9001.

## Camada de IA (oracle-ai)

- **Ollama** — modelos locais, PVC 20Gi. Modelos: `qwen2.5-coder:1.5b`
  (chat/código) e `nomic-embed-text` (embeddings, dim 768).
- **LiteLLM** — gateway compatível com OpenAI; aponta para o Ollama. Ponto de
  troca para multi-LLM (Claude/maior) quando houver RAM/GPU ou chaves.
- **Open WebUI** — chat com os modelos; embeddings via Ollama (evita OOM).
- **API (FastAPI)** — `/health`, CRUD (jobs/recruiters/posts), `/stats`,
  `/generate/post`, `/generate/outreach`.
- **Dashboard (Streamlit)** — métricas + form de geração de post.

## Camada de automação (oracle-automation)

- **n8n** — workflows. Incluído `daily-linkedin-plan` (cron → /generate/post).

## Camada de observabilidade (oracle-observability)

- **Prometheus** (retenção 24h) raspando cAdvisor/kubelet via proxy do apiserver.
- **Grafana** com datasource Prometheus provisionado.

## Camada de segurança (oracle-security)

- **Kyverno** — `ClusterPolicy oracle-baseline` (6 regras) em modo **Audit**,
  escopada aos namespaces `oracle-*` (não impacta outros projetos).
- **Trivy Operator** — vulnerabilidades + config audit, escopado a `oracle-*`.

## Reuso da infraestrutura existente

O cluster já tinha **argocd**, **ingress-nginx** e **metallb** — reaproveitados
em vez de reinstalados.

## Desvios em relação ao spec (justificados)

1. **kind em vez de k3d** — o cluster já existia. Deploy via
   `kind load docker-image` (sem registry), `imagePullPolicy: IfNotPresent`.
2. **Manifestos próprios para os dados em vez dos charts Bitnami** — a imagem
   oficial `pgvector/pgvector` é incompatível com o chart Bitnami
   (`/var/run/postgresql` read-only). Mais confiável e sob controle.
3. **Embeddings dim 768** (`nomic-embed-text`) em vez de 1536 (OpenAI).
4. **Modelo 1.5b em vez de 7B** — host com ~15Gi de RAM compartilhada; um 7B
   causa OOM. Para qualidade de produção, apontar o LiteLLM para Claude/modelo
   maior (capítulo Multi-LLM do spec).
5. **Observabilidade enxuta** (Prometheus+Grafana) em vez do kube-prometheus-stack
   — restrição de RAM.
6. **Kyverno em Audit + Trivy escopado** — cluster compartilhado; evita impactar
   sacola/backstage.

## Restrição operacional

Host com RAM no limite (~1,6Gi livre, swap cheio). Componentes pesados
adicionais exigem liberar RAM. Ver [11-runbook.md](11-runbook.md).
