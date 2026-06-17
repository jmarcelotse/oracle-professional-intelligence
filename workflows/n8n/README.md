# Fluxos n8n do Oracle

O n8n roda no namespace `oracle-automation`. Acesse com `make port-n8n`
(http://localhost:5678) e importe os workflows deste diretório
(menu **⋮ → Import from File**).

URLs internas úteis (dentro do cluster):

| Serviço | URL |
|---|---|
| Oracle API | `http://oracle-api.oracle-ai.svc.cluster.local:8000` |
| LiteLLM | `http://litellm.oracle-ai.svc.cluster.local:4000` |
| Postgres | `oracle-postgres-postgresql.oracle-data.svc.cluster.local:5432` |

## Workflows

### daily-linkedin-plan.json (incluído)

```
Cron diário (08:00)
  → POST /generate/post (Oracle API)   # gera e salva rascunho no Postgres
```

Extensões sugeridas: adicionar um nó **Telegram** após a geração para enviar o
rascunho para aprovação manual (defina `TELEGRAM_BOT_TOKEN`/`TELEGRAM_CHAT_ID`).

### Fluxos planejados (a montar no n8n)

- **weekly-career-report** — cron semanal → busca métricas/vagas/recrutadores
  via Oracle API → gera relatório → envia Telegram.
- **job-monitor** — coleta vagas → `POST /jobs` → calcula match.
- **recruiter-follow-up** — verifica `next_follow_up` em recruiters → lembrete.
- **obsidian-ingestion** — lê notas novas → chunk → embeddings (nomic-embed-text
  via Ollama) → grava em `knowledge_documents` (pgvector).
- **github-ingestion** — lê repositórios → embeddings → pgvector.

## Regra de ouro

Toda ação pública (post, comentário, mensagem) passa por **revisão humana**
antes de publicar. Os fluxos geram e armazenam rascunhos; a publicação é manual.
