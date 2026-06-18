# Guia de Uso — Oracle Professional Intelligence

Este guia explica, passo a passo, como usar o Oracle no dia a dia de acordo com
o objetivo do projeto: ser um **copiloto profissional / segundo cérebro com IA**
para LinkedIn, carreira, currículo, entrevistas, networking e conhecimento.

---

## 0. Antes de começar — acesso

### 0.1 Liberar os hostnames (uma vez só)

Os serviços são expostos via Ingress em `*.oracle.local`. Adicione ao
`/etc/hosts` (precisa de sudo):

```bash
echo "172.18.255.200 dashboard.oracle.local api.oracle.local chat.oracle.local grafana.oracle.local n8n.oracle.local" | sudo tee -a /etc/hosts
```

Confira:

```bash
getent hosts dashboard.oracle.local   # deve mostrar 172.18.255.200
curl -I http://dashboard.oracle.local  # HTTP 200
```

### 0.2 Endereços

| O quê | URL | Login |
|---|---|---|
| **Dashboard** (painel principal) | http://dashboard.oracle.local | — |
| **Chat** (Open WebUI) | http://chat.oracle.local | criar no 1º acesso |
| **API** (Swagger) | http://api.oracle.local/docs | — |
| **Grafana** (métricas) | http://grafana.oracle.local | admin / oracle |
| **n8n** (automação) | http://n8n.oracle.local | oracle / oracle123 |

### 0.3 Modelos de IA disponíveis

O Oracle usa o LiteLLM como gateway. Modelos configurados:

| Alias | Quando usar |
|---|---|
| `claude-sonnet` | **padrão** — conteúdo, currículo, entrevistas (melhor custo/qualidade) |
| `claude-opus` | raciocínio mais pesado (estratégia de carreira, análises) |
| `qwen-local` | offline / privacidade (roda no Ollama, qualidade menor) |

No Open WebUI você escolhe o modelo no seletor do topo. Na API, o padrão é
`claude-sonnet`.

---

## 1. LinkedIn Intelligence — criar conteúdo e autoridade

### 1.1 Gerar um post (jeito mais rápido)

**Pelo Dashboard:** abra http://dashboard.oracle.local → seção *"Gerar post de
LinkedIn"* → escreva o tema → **Gerar**. O texto é criado e salvo como rascunho.

**Pela API** (ex.: para automatizar):

```bash
curl -X POST http://api.oracle.local/generate/post \
  -H 'Content-Type: application/json' \
  -d '{"topic":"Lições de um incidente de produção em EKS","language":"pt-BR"}'
```

### 1.2 Comentários e artigos

Use o **Chat** (http://chat.oracle.local) com o modelo `claude-sonnet`. Cole como
instrução o conteúdo de [`skills/linkedin-writer/SKILL.md`](../skills/linkedin-writer/SKILL.md)
e peça o que precisa (comentário estratégico, artigo longo, variações).

### 1.3 Onde os rascunhos ficam

Todos os posts gerados vão para a tabela `posts` (status `draft`). Veja:

```bash
kubectl exec -n oracle-data oracle-postgres-postgresql-0 -- \
  psql -U oracle -d oracle_professional_intelligence \
  -c "SELECT id, topic, status, created_at FROM posts ORDER BY id DESC;"
```

> **Regra de ouro:** o Oracle gera e guarda rascunhos. **Você revisa e publica
> manualmente** no LinkedIn. Nada é publicado automaticamente.

---

## 2. Recruiter Intelligence — networking com recrutadores

### 2.1 Gerar mensagem para recrutador

```bash
curl -X POST http://api.oracle.local/generate/outreach \
  -H 'Content-Type: application/json' \
  -d '{"recruiter_name":"Maria","company":"Datadog","target_role":"Senior SRE","language":"en"}'
```

### 2.2 Organizar recrutadores

```bash
# cadastrar
curl -X POST http://api.oracle.local/recruiters \
  -H 'Content-Type: application/json' \
  -d '{"name":"Maria","company":"Datadog","role":"Tech Recruiter","country":"US","status":"new"}'

# listar
curl http://api.oracle.local/recruiters
```

Campos úteis: `status` (new/contacted/interview/...) e `next_follow_up` (data)
para acompanhar relacionamento.

---

## 3. Career Intelligence — vagas e estratégia

### 3.1 Cadastrar e acompanhar vagas

```bash
# cadastrar uma vaga
curl -X POST http://api.oracle.local/jobs \
  -H 'Content-Type: application/json' \
  -d '{"title":"Platform Engineer","company":"Acme","location":"Remote EU","remote":true,"stack":"Kubernetes, AWS, Terraform","job_url":"https://...","status":"new"}'

# listar (ou filtrar por status)
curl "http://api.oracle.local/jobs?status=new"
```

### 3.2 Compatibilidade vaga × perfil (job match)

Hoje, via **Chat** com `claude-sonnet`: cole a descrição da vaga + seu currículo
e use a instrução de [`skills/job-matcher/SKILL.md`](../skills/job-matcher/SKILL.md).
A skill retorna match score, requisitos atendidos, gaps e recomendações.

### 3.3 Estratégia de carreira

No Chat com `claude-opus`, use [`skills/career-strategist/SKILL.md`](../skills/career-strategist/SKILL.md)
para plano de carreira, certificações e trilhas de estudo.

---

## 4. Resume Intelligence — currículos

Via **Chat** com `claude-sonnet`, usando [`skills/resume-optimizer/SKILL.md`](../skills/resume-optimizer/SKILL.md):

1. Cole seu currículo base.
2. Cole a descrição da vaga.
3. Peça a versão adaptada (PT/EN), otimizada para ATS, com bullets orientados a
   resultado.

Guarde as versões na tabela `resumes` (ou anexe PDFs no MinIO, bucket
`oracle-files`).

---

## 5. Interview Intelligence — entrevistas

Via **Chat**, usando [`skills/interview-coach/SKILL.md`](../skills/interview-coach/SKILL.md):

- Gerar perguntas técnicas por stack/cargo.
- Simular entrevista (o modelo faz as perguntas, você responde, ele dá feedback).
- Montar respostas no formato **STAR**.
- Treinar em inglês.

Registre o que praticou na tabela `interviews`.

---

## 6. Knowledge Intelligence — sua memória (Obsidian + pgvector)

Essa é a camada que torna o Oracle um "segundo cérebro": ele responde usando o
**seu histórico real** (projetos, experiências, notas).

**Estado atual:** a infraestrutura está pronta (tabela `knowledge_documents` com
coluna `embedding vector(768)`, modelo de embeddings `nomic-embed-text` no
Ollama, índice vetorial). O **pipeline de ingestão** (ler Obsidian/GitHub →
gerar embeddings → gravar no pgvector) é o próximo passo a implementar (ver
[09-roadmap] e os fluxos em [`workflows/n8n/README.md`](../workflows/n8n/README.md)).

Enquanto isso, você já pode:
- Usar os **MCPs** (ver [`mcp/README.md`](../mcp/README.md)) para dar ao Claude
  acesso direto ao seu vault Obsidian, ao GitHub e ao banco Postgres durante o chat.

---

## 7. Automação (n8n) — rotinas no piloto automático

Abra http://n8n.oracle.local e importe os fluxos de
[`workflows/n8n/`](../workflows/n8n/).

- **daily-linkedin-plan** (incluído): todo dia gera um rascunho de post via API.
- Sugeridos: relatório semanal de carreira, monitor de vagas, follow-up de
  recrutadores, ingestão do Obsidian.

Para aprovação humana, adicione um nó **Telegram** (precisa de
`TELEGRAM_BOT_TOKEN` / `TELEGRAM_CHAT_ID`).

---

## 8. Monitoramento (Grafana)

http://grafana.oracle.local (admin / oracle) → Explore → datasource Prometheus.
Exemplo (memória por pod):

```
topk(10, sum by (pod) (container_memory_working_set_bytes) / 1024 / 1024)
```

---

## 9. Fluxo recomendado da semana

1. **Seg** — gerar 2-3 rascunhos de post (Dashboard) e agendar no calendário.
2. **Durante a semana** — revisar e publicar 1 post/dia; comentar em posts
   técnicos (Chat + skill linkedin-writer).
3. **Vagas** — cadastrar vagas interessantes (`/jobs`); rodar job-match nas top 3.
4. **Currículo** — adaptar o CV para cada vaga forte (skill resume-optimizer).
5. **Recrutadores** — cadastrar e enviar outreach; marcar `next_follow_up`.
6. **Entrevistas** — simular com a skill interview-coach antes de cada processo.
7. **Sex** — revisar métricas no Dashboard/Grafana e planejar a próxima semana.

---

## 10. Resumo do que é automático vs. via chat

| Função | Como usar hoje |
|---|---|
| Gerar post LinkedIn | ✅ API / Dashboard (automático) |
| Mensagem p/ recrutador | ✅ API (automático) |
| Cadastro de vagas/recrutadores/posts | ✅ API (automático) |
| Job match, currículo, entrevista, estratégia | 💬 Chat (Open WebUI/Claude) + as SKILL.md |
| Memória semântica (RAG do Obsidian) | 🚧 infra pronta, pipeline a implementar |

Para transformar as funções "via chat" em endpoints automáticos da API, é só
pedir — o padrão já existe (ver `apps/api/src/main.py`, `/generate/*`).
