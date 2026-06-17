# Oracle Professional Intelligence

## Guia Completo de Implementação Open Source com Kubernetes Local

---

# 1. Objetivo do Projeto

O **Oracle Professional Intelligence** é uma plataforma pessoal de inteligência artificial projetada para atuar como um **copiloto profissional permanente**.

O objetivo do projeto é centralizar conhecimento, experiências, oportunidades, conteúdo, currículo, networking, entrevistas e dados de carreira em um único ecossistema inteligente.

O Oracle não será apenas um assistente para LinkedIn e também não será apenas um buscador de vagas.

Ele será um **segundo cérebro profissional com IA**, capaz de transformar conhecimento, histórico profissional, documentação técnica, experiências reais, projetos, currículos, vagas e relacionamentos em ações concretas para acelerar a carreira.

---

# 2. Objetivos Principais

## 2.1 LinkedIn Intelligence

O Oracle deverá ajudar na evolução da presença profissional no LinkedIn.

Objetivos:

- Melhorar o Social Selling Index (SSI).
- Criar posts técnicos.
- Criar artigos.
- Criar comentários estratégicos.
- Gerar calendário editorial.
- Sugerir temas de conteúdo.
- Reaproveitar experiências profissionais como conteúdo.
- Ajudar no crescimento de autoridade técnica.
- Ajudar no networking com recrutadores, hiring managers e profissionais de tecnologia.

---

## 2.2 Career Intelligence

O Oracle deverá atuar como um assistente de carreira.

Objetivos:

- Buscar vagas aderentes ao perfil.
- Avaliar compatibilidade entre currículo e vaga.
- Gerenciar histórico de candidaturas.
- Organizar empresas-alvo.
- Organizar recrutadores.
- Criar plano de carreira.
- Recomendar certificações.
- Recomendar trilhas de estudo.
- Ajudar na estratégia para vagas internacionais.

---

## 2.3 Resume Intelligence

O Oracle deverá ajudar na criação e otimização de currículos.

Objetivos:

- Criar currículo base.
- Criar currículo em inglês.
- Adaptar currículo para cada vaga.
- Melhorar compatibilidade com ATS.
- Gerar bullet points técnicos.
- Gerar resumo profissional.
- Criar versões por cargo:
  - DevOps Engineer
  - SRE Engineer
  - DevSecOps Engineer
  - Cloud Architect
  - Platform Engineer
  - FinOps Engineer

---

## 2.4 Interview Intelligence

O Oracle deverá apoiar preparação para entrevistas.

Objetivos:

- Simular entrevistas técnicas.
- Simular entrevistas comportamentais.
- Criar respostas no formato STAR.
- Gerar perguntas por tecnologia.
- Gerar plano de estudo por vaga.
- Avaliar pontos fortes e gaps.
- Ajudar em entrevistas em português e inglês.

---

## 2.5 Knowledge Intelligence

O Oracle deverá utilizar uma base de conhecimento pessoal.

Objetivos:

- Usar Obsidian como memória principal.
- Ler documentação profissional.
- Organizar experiências.
- Transformar aprendizados em posts.
- Recuperar projetos antigos.
- Criar respostas usando histórico real.
- Criar memória semântica com pgvector.

---

# 3. Resultado Esperado

Ao final da implementação, o Oracle deverá ser capaz de:

- Rodar em Kubernetes local.
- Usar ferramentas open source de IA.
- Usar modelos locais com Ollama.
- Usar Open WebUI como interface de chat.
- Usar OpenClaw como assistente principal.
- Usar Skills especializadas.
- Usar MCPs para integrações.
- Usar Obsidian como memória humana.
- Usar PostgreSQL como memória estruturada.
- Usar pgvector como memória semântica.
- Usar Redis para cache e filas.
- Usar MinIO para arquivos.
- Usar n8n para automações.
- Usar Streamlit para dashboard.
- Usar Grafana para métricas.
- Gerar posts de LinkedIn.
- Gerar mensagens para recrutadores.
- Analisar vagas.
- Adaptar currículos.
- Preparar entrevistas.
- Gerar relatórios semanais de carreira.

---

# 4. Arquitetura Geral

```text
Oracle Professional Intelligence
│
├── Intelligence Layer
│   ├── OpenClaw
│   ├── Open WebUI
│   ├── Ollama
│   ├── LiteLLM
│   └── LocalAI opcional
│
├── Agent Layer
│   ├── CrewAI
│   ├── LangGraph
│   ├── PydanticAI
│   └── Skills
│
├── Memory Layer
│   ├── Obsidian
│   ├── PostgreSQL
│   ├── pgvector
│   ├── Redis
│   └── MinIO
│
├── Integration Layer
│   ├── GitHub MCP
│   ├── Obsidian MCP
│   ├── PostgreSQL MCP
│   ├── Filesystem MCP
│   ├── Playwright MCP
│   ├── Browser MCP
│   └── Git MCP
│
├── Automation Layer
│   ├── n8n
│   ├── Node-RED opcional
│   └── CronJobs Kubernetes
│
├── Application Layer
│   ├── FastAPI
│   ├── Streamlit
│   └── Workers Python
│
└── Platform Layer
    ├── Kubernetes Local
    ├── Helm
    ├── Argo CD
    ├── Prometheus
    ├── Grafana
    ├── Loki
    ├── Trivy
    └── Kyverno
```

---

# 5. Ferramentas Open Source Utilizadas

## 5.1 Kubernetes Local

Opções:

- k3d
- kind
- minikube
- k3s

Recomendação:

```text
k3d
```

Motivos:

- Leve.
- Simples.
- Rápido.
- Usa Docker.
- Fácil de recriar.
- Bom para laboratório local.

---

## 5.2 IA Local

Ferramentas:

- Ollama
- Open WebUI
- LiteLLM
- LocalAI
- vLLM

Recomendação inicial:

```text
Ollama + Open WebUI + LiteLLM
```

Função de cada ferramenta:

| Ferramenta | Função |
|---|---|
| Ollama | Rodar modelos locais |
| Open WebUI | Interface web para conversar com modelos |
| LiteLLM | Gateway para modelos locais e externos |
| LocalAI | Alternativa local compatível com OpenAI API |
| vLLM | Servir modelos grandes com performance |

Modelos sugeridos:

```text
qwen2.5-coder
qwen3
llama3.1
llama3.2
mistral
deepseek-r1
gemma
phi
```

Para começar:

```text
qwen2.5-coder
llama3.1
mistral
```

---

## 5.3 Assistente Principal

Ferramenta principal:

```text
OpenClaw
```

Uso no projeto:

- Atuar como assistente principal.
- Receber comandos.
- Acionar Skills.
- Acionar MCPs.
- Consultar memória.
- Orquestrar tarefas.
- Gerar respostas.
- Integrar com Telegram ou interface web.

---

## 5.4 Agentes

Ferramentas:

- CrewAI
- LangGraph
- PydanticAI
- AutoGen
- Semantic Kernel

Recomendação:

```text
CrewAI + LangGraph + PydanticAI
```

Uso:

- CrewAI para agentes especializados.
- LangGraph para fluxos controlados.
- PydanticAI para agentes tipados e validação de dados.

Agentes planejados:

```text
linkedin-writer-agent
personal-branding-agent
recruiter-outreach-agent
job-hunter-agent
resume-optimizer-agent
interview-coach-agent
career-strategist-agent
knowledge-agent
```

---

## 5.5 Banco de Dados e Memória

Ferramentas:

- PostgreSQL
- pgvector
- Redis
- MinIO
- Qdrant opcional
- ChromaDB opcional

Recomendação inicial:

```text
PostgreSQL + pgvector + Redis + MinIO
```

---

## 5.6 Automação

Ferramentas:

- n8n
- Node-RED
- Apache Airflow
- Temporal
- Kestra

Recomendação:

```text
n8n
```

Uso:

- Rotinas diárias.
- Rotinas semanais.
- Notificações.
- Relatórios.
- Integração com Telegram.
- Fluxos de aprovação humana.
- Pipeline de geração de conteúdo.

---

## 5.7 Dashboard

Ferramentas:

- Streamlit
- Gradio
- Grafana
- Metabase
- Apache Superset

Recomendação:

```text
Streamlit + Grafana
```

Uso:

- Streamlit para painel do Oracle.
- Grafana para observabilidade e métricas.

---

## 5.8 MCPs

MCPs recomendados:

```text
Filesystem MCP
GitHub MCP
Git MCP
PostgreSQL MCP
Obsidian MCP
Playwright MCP
Browser MCP
Fetch MCP
Memory MCP
```

Uso:

- Ler arquivos locais.
- Integrar com GitHub.
- Consultar banco.
- Ler Obsidian.
- Navegar na web.
- Buscar informações públicas.
- Salvar e recuperar memória.

---

## 5.9 Observabilidade

Ferramentas:

```text
Prometheus
Grafana
Loki
Promtail
OpenTelemetry
Jaeger
```

Recomendação:

```text
Prometheus + Grafana + Loki + Promtail
```

---

## 5.10 Segurança

Ferramentas:

```text
Trivy
Grype
Syft
Kyverno
OPA Gatekeeper
Sealed Secrets
External Secrets Operator
kube-bench
kube-score
kube-linter
```

Recomendação inicial:

```text
Trivy + Kyverno + Sealed Secrets
```

---

# 6. Arquitetura de Memória

A memória do Oracle será dividida em múltiplas camadas.

## 6.1 Camada 1 — Obsidian

O Obsidian será a **memória humana principal**.

Armazenará:

- Experiências profissionais.
- Projetos AWS.
- Projetos Kubernetes.
- Projetos Terraform.
- Casos FinOps.
- Casos DevSecOps.
- Incidentes SRE.
- Certificações.
- Estudos.
- Ideias de posts.
- Rascunhos de artigos.
- Currículos.
- Respostas de entrevistas.
- Estratégia de carreira.
- Histórico de aprendizados.

Estrutura sugerida:

```text
Oracle-Knowledge/
├── LinkedIn/
│   ├── Posts/
│   ├── Artigos/
│   ├── Comentarios/
│   ├── SSI/
│   └── Recrutadores/
├── Career/
│   ├── Curriculos/
│   ├── Vagas/
│   ├── Entrevistas/
│   ├── Empresas-Alvo/
│   └── Plano-de-Carreira/
├── Tech/
│   ├── AWS/
│   ├── Kubernetes/
│   ├── Terraform/
│   ├── DevOps/
│   ├── SRE/
│   ├── DevSecOps/
│   ├── FinOps/
│   ├── Observability/
│   └── Linux/
├── Projects/
│   ├── SmartFit/
│   ├── TIVIT/
│   ├── VERT/
│   └── Pessoais/
└── Templates/
    ├── Posts/
    ├── Curriculos/
    ├── Entrevistas/
    └── Recrutadores/
```

Integração:

```text
Obsidian MCP
```

---

## 6.2 Camada 2 — PostgreSQL

O PostgreSQL será a **memória estruturada**.

Armazenará:

- Vagas.
- Recrutadores.
- Empresas.
- Posts.
- Comentários.
- Currículos.
- Entrevistas.
- Métricas do LinkedIn.
- Calendário editorial.
- Histórico de candidaturas.
- Execuções dos agentes.

Tabelas principais:

```text
profiles
linkedin_metrics
posts
comments
recruiters
companies
jobs
resumes
interviews
connections
content_calendar
agent_runs
knowledge_documents
```

---

## 6.3 Camada 3 — pgvector

O pgvector será a **memória semântica**.

Armazenará embeddings de:

- Notas do Obsidian.
- Currículos.
- Vagas.
- Posts.
- Projetos GitHub.
- Documentação técnica.
- Respostas de entrevista.
- Experiências profissionais.

Permite:

- Busca contextual.
- Busca semântica.
- RAG.
- Recuperação de experiências.
- Geração de respostas com contexto.
- Criação de conteúdo baseado em histórico real.

Exemplo:

```text
Pergunta:
"Quais projetos eu fiz com ECS, RDS e FinOps?"

Fluxo:
Oracle → pgvector → Obsidian → GitHub → resposta contextual
```

---

## 6.4 Camada 4 — Redis

O Redis será usado para memória temporária.

Uso:

- Cache.
- Sessões.
- Filas.
- Estado temporário dos agentes.
- Controle de execução.
- Rate limit.

---

## 6.5 Camada 5 — MinIO

O MinIO será usado para arquivos.

Armazenará:

- Currículos em PDF.
- Currículos em DOCX.
- Exports.
- Relatórios.
- Anexos.
- Imagens de posts.
- Backups.

---

## 6.6 Fluxo de Memória

```text
Obsidian
   ↓
Obsidian MCP
   ↓
Ingestion Pipeline
   ↓
pgvector
   ↓
Oracle Agents
   ↓
Resposta com contexto

PostgreSQL
   ↓
PostgreSQL MCP
   ↓
Oracle Agents
   ↓
Dados estruturados

GitHub
   ↓
GitHub MCP
   ↓
Ingestion Pipeline
   ↓
pgvector
   ↓
Conteúdo e portfólio
```

---

# 7. Namespaces Kubernetes

Criar os seguintes namespaces:

```text
oracle-ai
oracle-data
oracle-mcp
oracle-automation
oracle-observability
oracle-security
argocd
```

Função:

| Namespace | Função |
|---|---|
| oracle-ai | IA, OpenClaw, Ollama, Open WebUI, LiteLLM |
| oracle-data | PostgreSQL, pgvector, Redis, MinIO |
| oracle-mcp | MCP servers |
| oracle-automation | n8n, jobs, workers |
| oracle-observability | Prometheus, Grafana, Loki |
| oracle-security | Trivy, Kyverno, secrets |
| argocd | GitOps |

---

# 8. Estrutura do Repositório

```text
oracle-professional-intelligence/
├── README.md
├── docs/
│   ├── 01-objetivo.md
│   ├── 02-arquitetura.md
│   ├── 03-memoria.md
│   ├── 04-ferramentas-opensource.md
│   ├── 05-kubernetes.md
│   ├── 06-mcps.md
│   ├── 07-skills.md
│   ├── 08-agentes.md
│   ├── 09-roadmap.md
│   ├── 10-seguranca.md
│   └── 11-runbook.md
├── apps/
│   ├── api/
│   ├── dashboard/
│   ├── agents/
│   └── workers/
├── skills/
│   ├── linkedin-writer/
│   ├── personal-branding-advisor/
│   ├── recruiter-outreach/
│   ├── job-matcher/
│   ├── resume-optimizer/
│   ├── interview-coach/
│   └── career-strategist/
├── mcp/
│   ├── configs/
│   ├── claude/
│   ├── kiro/
│   └── openclaw/
├── kubernetes/
│   ├── namespaces/
│   ├── base/
│   ├── overlays/
│   └── helm-values/
├── charts/
│   ├── oracle-api/
│   ├── oracle-dashboard/
│   ├── oracle-agents/
│   └── oracle-mcp/
├── database/
│   ├── migrations/
│   └── seeds/
├── workflows/
│   └── n8n/
├── scripts/
│   ├── setup-k3d.sh
│   ├── install-argocd.sh
│   ├── install-observability.sh
│   ├── install-ai-stack.sh
│   └── bootstrap.sh
├── docker/
├── .env.example
├── .gitignore
├── Makefile
└── docker-compose.yml
```

---

# 9. Passo a Passo de Implementação

## Passo 1 — Instalar ferramentas locais

Ubuntu:

```bash
sudo apt update
sudo apt install -y curl wget git make jq unzip ca-certificates gnupg lsb-release
```

Instalar Docker:

```bash
curl -fsSL https://get.docker.com | sh
sudo usermod -aG docker $USER
```

Após isso, sair e entrar novamente na sessão.

Validar:

```bash
docker version
```

Instalar kubectl:

```bash
curl -LO "https://dl.k8s.io/release/stable.txt"
KUBECTL_VERSION=$(cat stable.txt)
curl -LO "https://dl.k8s.io/release/${KUBECTL_VERSION}/bin/linux/amd64/kubectl"
chmod +x kubectl
sudo mv kubectl /usr/local/bin/
kubectl version --client
```

Instalar Helm:

```bash
curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash
helm version
```

Instalar k3d:

```bash
curl -s https://raw.githubusercontent.com/k3d-io/k3d/main/install.sh | bash
k3d version
```

Instalar Argo CD CLI:

```bash
curl -sSL -o argocd https://github.com/argoproj/argo-cd/releases/latest/download/argocd-linux-amd64
chmod +x argocd
sudo mv argocd /usr/local/bin/
argocd version --client
```

---

## Passo 2 — Criar cluster Kubernetes local

```bash
k3d cluster create oracle \
  --servers 1 \
  --agents 2 \
  --api-port 6550 \
  -p "8080:80@loadbalancer" \
  -p "8443:443@loadbalancer"
```

Validar:

```bash
kubectl get nodes
```

Criar namespaces:

```bash
kubectl create namespace oracle-ai
kubectl create namespace oracle-data
kubectl create namespace oracle-mcp
kubectl create namespace oracle-automation
kubectl create namespace oracle-observability
kubectl create namespace oracle-security
kubectl create namespace argocd
```

---

## Passo 3 — Criar repositório local

```bash
mkdir oracle-professional-intelligence
cd oracle-professional-intelligence
git init
```

Criar estrutura:

```bash
mkdir -p docs
mkdir -p apps/api apps/dashboard apps/agents apps/workers
mkdir -p skills/linkedin-writer
mkdir -p skills/personal-branding-advisor
mkdir -p skills/recruiter-outreach
mkdir -p skills/job-matcher
mkdir -p skills/resume-optimizer
mkdir -p skills/interview-coach
mkdir -p skills/career-strategist
mkdir -p mcp/configs mcp/claude mcp/kiro mcp/openclaw
mkdir -p kubernetes/namespaces kubernetes/base kubernetes/overlays kubernetes/helm-values
mkdir -p charts database/migrations database/seeds workflows/n8n scripts docker
touch README.md .env.example .gitignore Makefile docker-compose.yml
```

---

## Passo 4 — Criar `.gitignore`

```bash
cat > .gitignore <<'EOF'
.venv/
.env
__pycache__/
*.pyc
*.pyo
*.log
.DS_Store
data/private/
data/exports/
obsidian/private/
*.sqlite
*.db
node_modules/
dist/
build/
EOF
```

---

## Passo 5 — Criar `.env.example`

```bash
cat > .env.example <<'EOF'
APP_NAME=Oracle Professional Intelligence
ENVIRONMENT=local

DATABASE_HOST=oracle-postgres-postgresql.oracle-data.svc.cluster.local
DATABASE_PORT=5432
DATABASE_NAME=oracle_professional_intelligence
DATABASE_USER=oracle
DATABASE_PASSWORD=oracle

REDIS_HOST=oracle-redis-master.oracle-data.svc.cluster.local
REDIS_PORT=6379

MINIO_ENDPOINT=oracle-minio.oracle-data.svc.cluster.local:9000
MINIO_ACCESS_KEY=oracle
MINIO_SECRET_KEY=oracle123456
MINIO_BUCKET=oracle-files

OLLAMA_BASE_URL=http://ollama.oracle-ai.svc.cluster.local:11434
LITELLM_BASE_URL=http://litellm.oracle-ai.svc.cluster.local:4000

OBSIDIAN_VAULT_PATH=/vaults/Oracle-Knowledge

TELEGRAM_BOT_TOKEN=
TELEGRAM_CHAT_ID=

LINKEDIN_PROFILE_URL=
GITHUB_PROFILE_URL=

DEFAULT_LANGUAGE=pt-BR
TARGET_MARKET=international
TARGET_ROLES=DevOps,SRE,DevSecOps,Cloud Architect,Platform Engineer,FinOps
EOF
```

---

# 10. Instalação da Camada de Dados

## Passo 6 — Instalar PostgreSQL com pgvector

Adicionar repositório Helm:

```bash
helm repo add bitnami https://charts.bitnami.com/bitnami
helm repo update
```

Criar values:

```bash
mkdir -p kubernetes/helm-values/postgresql

cat > kubernetes/helm-values/postgresql/values.yaml <<'EOF'
auth:
  username: oracle
  password: oracle
  database: oracle_professional_intelligence

image:
  registry: docker.io
  repository: pgvector/pgvector
  tag: pg16

primary:
  persistence:
    enabled: true
    size: 10Gi
EOF
```

Instalar:

```bash
helm install oracle-postgres bitnami/postgresql \
  -n oracle-data \
  -f kubernetes/helm-values/postgresql/values.yaml
```

Validar:

```bash
kubectl get pods -n oracle-data
```

---

## Passo 7 — Instalar Redis

```bash
helm install oracle-redis bitnami/redis \
  -n oracle-data \
  --set auth.enabled=false
```

Validar:

```bash
kubectl get pods -n oracle-data
```

---

## Passo 8 — Instalar MinIO

```bash
helm install oracle-minio bitnami/minio \
  -n oracle-data \
  --set auth.rootUser=oracle \
  --set auth.rootPassword=oracle123456 \
  --set defaultBuckets=oracle-files
```

Validar:

```bash
kubectl get pods -n oracle-data
```

---

## Passo 9 — Criar schema inicial do banco

Criar arquivo SQL:

```bash
cat > database/migrations/001_initial_schema.sql <<'EOF'
CREATE EXTENSION IF NOT EXISTS vector;

CREATE TABLE IF NOT EXISTS profiles (
    id SERIAL PRIMARY KEY,
    full_name TEXT NOT NULL,
    headline TEXT,
    linkedin_url TEXT,
    github_url TEXT,
    target_roles TEXT,
    target_countries TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS linkedin_metrics (
    id SERIAL PRIMARY KEY,
    profile_id INTEGER REFERENCES profiles(id),
    ssi_score NUMERIC,
    professional_brand NUMERIC,
    find_right_people NUMERIC,
    engage_insights NUMERIC,
    build_relationships NUMERIC,
    collected_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS posts (
    id SERIAL PRIMARY KEY,
    title TEXT,
    content TEXT NOT NULL,
    topic TEXT,
    status TEXT DEFAULT 'draft',
    platform TEXT DEFAULT 'linkedin',
    published_at TIMESTAMP,
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS comments (
    id SERIAL PRIMARY KEY,
    post_url TEXT,
    content TEXT NOT NULL,
    topic TEXT,
    status TEXT DEFAULT 'draft',
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS recruiters (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    company TEXT,
    role TEXT,
    linkedin_url TEXT,
    country TEXT,
    status TEXT DEFAULT 'new',
    notes TEXT,
    next_follow_up DATE,
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS companies (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    website TEXT,
    linkedin_url TEXT,
    country TEXT,
    industry TEXT,
    notes TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS jobs (
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    company TEXT,
    location TEXT,
    remote BOOLEAN DEFAULT FALSE,
    salary_range TEXT,
    job_url TEXT,
    description TEXT,
    stack TEXT,
    match_score NUMERIC,
    status TEXT DEFAULT 'new',
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS resumes (
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    content TEXT,
    target_role TEXT,
    target_company TEXT,
    language TEXT DEFAULT 'en',
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS interviews (
    id SERIAL PRIMARY KEY,
    company TEXT,
    role TEXT,
    interview_type TEXT,
    questions TEXT,
    answers TEXT,
    feedback TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS content_calendar (
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    topic TEXT,
    planned_date DATE,
    status TEXT DEFAULT 'planned',
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS agent_runs (
    id SERIAL PRIMARY KEY,
    agent_name TEXT NOT NULL,
    input TEXT,
    output TEXT,
    status TEXT,
    started_at TIMESTAMP DEFAULT NOW(),
    finished_at TIMESTAMP
);

CREATE TABLE IF NOT EXISTS knowledge_documents (
    id SERIAL PRIMARY KEY,
    source TEXT,
    source_path TEXT,
    title TEXT,
    content TEXT,
    embedding vector(1536),
    created_at TIMESTAMP DEFAULT NOW()
);
EOF
```

Aplicar:

```bash
kubectl -n oracle-data port-forward svc/oracle-postgres-postgresql 5432:5432
```

Em outro terminal:

```bash
PGPASSWORD=oracle psql \
  -h localhost \
  -U oracle \
  -d oracle_professional_intelligence \
  -f database/migrations/001_initial_schema.sql
```

---

# 11. Instalação da Camada de IA

## Passo 10 — Instalar Ollama

Criar manifesto:

```bash
mkdir -p kubernetes/base/ollama

cat > kubernetes/base/ollama/deployment.yaml <<'EOF'
apiVersion: apps/v1
kind: Deployment
metadata:
  name: ollama
  namespace: oracle-ai
spec:
  replicas: 1
  selector:
    matchLabels:
      app: ollama
  template:
    metadata:
      labels:
        app: ollama
    spec:
      containers:
        - name: ollama
          image: ollama/ollama:latest
          ports:
            - containerPort: 11434
          resources:
            requests:
              cpu: "1"
              memory: "2Gi"
            limits:
              cpu: "4"
              memory: "8Gi"
          volumeMounts:
            - name: ollama-data
              mountPath: /root/.ollama
      volumes:
        - name: ollama-data
          emptyDir: {}
---
apiVersion: v1
kind: Service
metadata:
  name: ollama
  namespace: oracle-ai
spec:
  selector:
    app: ollama
  ports:
    - port: 11434
      targetPort: 11434
EOF
```

Aplicar:

```bash
kubectl apply -f kubernetes/base/ollama/deployment.yaml
```

Baixar modelos:

```bash
kubectl -n oracle-ai exec deploy/ollama -- ollama pull qwen2.5-coder
kubectl -n oracle-ai exec deploy/ollama -- ollama pull llama3.1
kubectl -n oracle-ai exec deploy/ollama -- ollama pull mistral
```

Validar:

```bash
kubectl -n oracle-ai exec deploy/ollama -- ollama list
```

---

## Passo 11 — Instalar Open WebUI

```bash
helm repo add open-webui https://helm.openwebui.com/
helm repo update
```

Instalar:

```bash
helm install open-webui open-webui/open-webui \
  -n oracle-ai \
  --set ollama.enabled=false \
  --set ollamaUrls[0]=http://ollama.oracle-ai.svc.cluster.local:11434
```

Acessar:

```bash
kubectl -n oracle-ai port-forward svc/open-webui 3000:80
```

URL:

```text
http://localhost:3000
```

---

## Passo 12 — Instalar LiteLLM

Criar manifesto:

```bash
mkdir -p kubernetes/base/litellm

cat > kubernetes/base/litellm/deployment.yaml <<'EOF'
apiVersion: apps/v1
kind: Deployment
metadata:
  name: litellm
  namespace: oracle-ai
spec:
  replicas: 1
  selector:
    matchLabels:
      app: litellm
  template:
    metadata:
      labels:
        app: litellm
    spec:
      containers:
        - name: litellm
          image: ghcr.io/berriai/litellm:main-latest
          args:
            - "--model"
            - "ollama/qwen2.5-coder"
            - "--api_base"
            - "http://ollama.oracle-ai.svc.cluster.local:11434"
          ports:
            - containerPort: 4000
---
apiVersion: v1
kind: Service
metadata:
  name: litellm
  namespace: oracle-ai
spec:
  selector:
    app: litellm
  ports:
    - port: 4000
      targetPort: 4000
EOF
```

Aplicar:

```bash
kubectl apply -f kubernetes/base/litellm/deployment.yaml
```

Validar:

```bash
kubectl get pods -n oracle-ai
```

---

# 12. Instalação da Camada de Aplicação

## Passo 13 — Criar Backend FastAPI

Criar aplicação:

```bash
mkdir -p apps/api/src

cat > apps/api/src/main.py <<'EOF'
from fastapi import FastAPI

app = FastAPI(title="Oracle Professional Intelligence")

@app.get("/health")
def health():
    return {"status": "ok", "service": "oracle-api"}

@app.get("/")
def root():
    return {
        "project": "Oracle Professional Intelligence",
        "objective": "AI-powered professional intelligence platform",
        "modules": [
            "LinkedIn Intelligence",
            "Career Intelligence",
            "Resume Intelligence",
            "Interview Intelligence",
            "Recruiter Intelligence",
            "Knowledge Intelligence"
        ]
    }
EOF
```

Criar Dockerfile:

```bash
cat > docker/api.Dockerfile <<'EOF'
FROM python:3.12-slim

WORKDIR /app

RUN pip install fastapi uvicorn psycopg[binary] sqlalchemy pydantic python-dotenv requests

COPY apps/api/src /app/src

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
EOF
```

Build:

```bash
docker build -t oracle-api:local -f docker/api.Dockerfile .
k3d image import oracle-api:local -c oracle
```

Manifesto:

```bash
mkdir -p kubernetes/base/api

cat > kubernetes/base/api/deployment.yaml <<'EOF'
apiVersion: apps/v1
kind: Deployment
metadata:
  name: oracle-api
  namespace: oracle-ai
spec:
  replicas: 1
  selector:
    matchLabels:
      app: oracle-api
  template:
    metadata:
      labels:
        app: oracle-api
    spec:
      containers:
        - name: oracle-api
          image: oracle-api:local
          imagePullPolicy: Never
          ports:
            - containerPort: 8000
---
apiVersion: v1
kind: Service
metadata:
  name: oracle-api
  namespace: oracle-ai
spec:
  selector:
    app: oracle-api
  ports:
    - port: 8000
      targetPort: 8000
EOF
```

Deploy:

```bash
kubectl apply -f kubernetes/base/api/deployment.yaml
```

Testar:

```bash
kubectl -n oracle-ai port-forward svc/oracle-api 8000:8000
curl http://localhost:8000/health
```

---

## Passo 14 — Criar Dashboard Streamlit

Criar app:

```bash
mkdir -p apps/dashboard

cat > apps/dashboard/app.py <<'EOF'
import streamlit as st

st.set_page_config(page_title="Oracle Professional Intelligence", layout="wide")

st.title("Oracle Professional Intelligence")

st.write("Copiloto open source para LinkedIn, carreira, currículo, entrevistas e networking.")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("SSI Atual", "51")
    st.metric("Posts na semana", "0")

with col2:
    st.metric("Vagas analisadas", "0")
    st.metric("Recrutadores", "0")

with col3:
    st.metric("Currículos gerados", "0")
    st.metric("Entrevistas simuladas", "0")

st.header("Módulos")

st.markdown("""
- LinkedIn Intelligence
- Career Intelligence
- Resume Intelligence
- Interview Intelligence
- Recruiter Intelligence
- Knowledge Intelligence
""")
EOF
```

Criar Dockerfile:

```bash
cat > docker/dashboard.Dockerfile <<'EOF'
FROM python:3.12-slim

WORKDIR /app

RUN pip install streamlit requests pandas psycopg[binary]

COPY apps/dashboard /app

CMD ["streamlit", "run", "app.py", "--server.address=0.0.0.0", "--server.port=8501"]
EOF
```

Build:

```bash
docker build -t oracle-dashboard:local -f docker/dashboard.Dockerfile .
k3d image import oracle-dashboard:local -c oracle
```

Manifesto:

```bash
mkdir -p kubernetes/base/dashboard

cat > kubernetes/base/dashboard/deployment.yaml <<'EOF'
apiVersion: apps/v1
kind: Deployment
metadata:
  name: oracle-dashboard
  namespace: oracle-ai
spec:
  replicas: 1
  selector:
    matchLabels:
      app: oracle-dashboard
  template:
    metadata:
      labels:
        app: oracle-dashboard
    spec:
      containers:
        - name: oracle-dashboard
          image: oracle-dashboard:local
          imagePullPolicy: Never
          ports:
            - containerPort: 8501
---
apiVersion: v1
kind: Service
metadata:
  name: oracle-dashboard
  namespace: oracle-ai
spec:
  selector:
    app: oracle-dashboard
  ports:
    - port: 8501
      targetPort: 8501
EOF
```

Deploy:

```bash
kubectl apply -f kubernetes/base/dashboard/deployment.yaml
```

Acessar:

```bash
kubectl -n oracle-ai port-forward svc/oracle-dashboard 8501:8501
```

URL:

```text
http://localhost:8501
```

---

# 13. Instalação da Camada de Automação

## Passo 15 — Instalar n8n

Criar manifesto:

```bash
mkdir -p kubernetes/base/n8n

cat > kubernetes/base/n8n/deployment.yaml <<'EOF'
apiVersion: apps/v1
kind: Deployment
metadata:
  name: n8n
  namespace: oracle-automation
spec:
  replicas: 1
  selector:
    matchLabels:
      app: n8n
  template:
    metadata:
      labels:
        app: n8n
    spec:
      containers:
        - name: n8n
          image: n8nio/n8n:latest
          ports:
            - containerPort: 5678
          env:
            - name: N8N_BASIC_AUTH_ACTIVE
              value: "true"
            - name: N8N_BASIC_AUTH_USER
              value: "oracle"
            - name: N8N_BASIC_AUTH_PASSWORD
              value: "oracle123"
---
apiVersion: v1
kind: Service
metadata:
  name: n8n
  namespace: oracle-automation
spec:
  selector:
    app: n8n
  ports:
    - port: 5678
      targetPort: 5678
EOF
```

Deploy:

```bash
kubectl apply -f kubernetes/base/n8n/deployment.yaml
```

Acessar:

```bash
kubectl -n oracle-automation port-forward svc/n8n 5678:5678
```

URL:

```text
http://localhost:5678
```

---

## Passo 16 — Criar fluxos n8n

Fluxos planejados:

```text
daily-linkedin-plan
weekly-career-report
job-monitor
recruiter-follow-up
content-calendar
interview-preparation
obsidian-ingestion
github-ingestion
```

### daily-linkedin-plan

Fluxo:

```text
Cron diário
↓
Buscar calendário de conteúdo
↓
Gerar sugestão de post
↓
Gerar 3 comentários técnicos
↓
Salvar no PostgreSQL
↓
Enviar Telegram para aprovação
```

### weekly-career-report

Fluxo:

```text
Cron semanal
↓
Buscar métricas
↓
Buscar vagas
↓
Buscar recrutadores
↓
Buscar posts criados
↓
Gerar relatório
↓
Enviar Telegram
```

### obsidian-ingestion

Fluxo:

```text
Cron diário
↓
Ler notas novas do Obsidian
↓
Quebrar em chunks
↓
Gerar embeddings
↓
Salvar no pgvector
```

---

# 14. Skills do Oracle

## Passo 17 — Criar Skill LinkedIn Writer

```bash
cat > skills/linkedin-writer/SKILL.md <<'EOF'
# LinkedIn Writer Skill

## Objetivo

Criar conteúdos técnicos para LinkedIn com foco em DevOps, SRE, DevSecOps, AWS, Kubernetes, Terraform, FinOps e carreira internacional.

## Responsabilidades

- Criar posts curtos.
- Criar posts técnicos.
- Criar artigos.
- Criar comentários estratégicos.
- Transformar experiências profissionais em conteúdo.
- Adaptar conteúdo para português e inglês.
- Sugerir hashtags.
- Sugerir CTA.

## Entrada esperada

- Tema.
- Público-alvo.
- Tom desejado.
- Objetivo do post.
- Experiência ou contexto técnico.

## Saída esperada

- Texto pronto para LinkedIn.
- Sugestões de hashtags.
- Sugestão de imagem ou diagrama.
- CTA final.
EOF
```

---

## Passo 18 — Criar Skill Personal Branding Advisor

```bash
cat > skills/personal-branding-advisor/SKILL.md <<'EOF'
# Personal Branding Advisor Skill

## Objetivo

Melhorar o posicionamento profissional no LinkedIn e em canais públicos.

## Responsabilidades

- Melhorar headline.
- Melhorar seção About.
- Melhorar experiências.
- Sugerir palavras-chave.
- Fortalecer autoridade técnica.
- Ajustar posicionamento para mercado internacional.

## Entrada esperada

- Perfil atual.
- Objetivo de carreira.
- Cargos alvo.
- Mercado alvo.

## Saída esperada

- Headline otimizada.
- About otimizado.
- Sugestões de melhoria.
- Palavras-chave recomendadas.
EOF
```

---

## Passo 19 — Criar Skill Recruiter Outreach

```bash
cat > skills/recruiter-outreach/SKILL.md <<'EOF'
# Recruiter Outreach Skill

## Objetivo

Criar mensagens profissionais para conexão, follow-up e relacionamento com recrutadores.

## Responsabilidades

- Criar mensagem de conexão.
- Criar mensagem de apresentação.
- Criar follow-up.
- Criar resposta para recrutadores.
- Adaptar mensagem para português, inglês e espanhol.

## Entrada esperada

- Nome do recrutador.
- Empresa.
- Cargo alvo.
- Contexto da oportunidade.
- Idioma.

## Saída esperada

- Mensagem curta.
- Mensagem profissional.
- Follow-up.
- Versão em inglês quando necessário.
EOF
```

---

## Passo 20 — Criar Skill Job Matcher

```bash
cat > skills/job-matcher/SKILL.md <<'EOF'
# Job Matcher Skill

## Objetivo

Comparar vagas com o perfil profissional e calcular aderência.

## Responsabilidades

- Analisar descrição da vaga.
- Comparar com currículo.
- Identificar requisitos atendidos.
- Identificar gaps.
- Gerar match score.
- Recomendar próximos passos.

## Entrada esperada

- Descrição da vaga.
- Currículo.
- Cargo alvo.
- País ou mercado.

## Saída esperada

- Match score.
- Requisitos atendidos.
- Gaps.
- Recomendações.
- Palavras-chave importantes.
EOF
```

---

## Passo 21 — Criar Skill Resume Optimizer

```bash
cat > skills/resume-optimizer/SKILL.md <<'EOF'
# Resume Optimizer Skill

## Objetivo

Otimizar currículos para vagas de DevOps, SRE, DevSecOps, Cloud Architect, Platform Engineer e FinOps.

## Responsabilidades

- Adaptar currículo para vagas específicas.
- Melhorar compatibilidade ATS.
- Criar versão em inglês.
- Melhorar resumo profissional.
- Criar bullet points orientados a resultado.
- Identificar gaps entre currículo e vaga.

## Entrada esperada

- Currículo base.
- Descrição da vaga.
- Cargo alvo.
- Idioma desejado.

## Saída esperada

- Currículo ajustado.
- Resumo profissional.
- Lista de melhorias.
- Palavras-chave recomendadas.
EOF
```

---

## Passo 22 — Criar Skill Interview Coach

```bash
cat > skills/interview-coach/SKILL.md <<'EOF'
# Interview Coach Skill

## Objetivo

Preparar o usuário para entrevistas técnicas, comportamentais e internacionais.

## Responsabilidades

- Criar perguntas técnicas.
- Criar respostas STAR.
- Simular entrevistas.
- Avaliar respostas.
- Criar plano de estudo.
- Preparar respostas em inglês.

## Entrada esperada

- Cargo alvo.
- Descrição da vaga.
- Idioma.
- Nível da entrevista.
- Stack técnica.

## Saída esperada

- Lista de perguntas.
- Respostas sugeridas.
- Feedback.
- Plano de estudo.
EOF
```

---

## Passo 23 — Criar Skill Career Strategist

```bash
cat > skills/career-strategist/SKILL.md <<'EOF'
# Career Strategist Skill

## Objetivo

Criar estratégia de crescimento profissional e evolução de carreira.

## Responsabilidades

- Criar plano de carreira.
- Recomendar certificações.
- Recomendar trilhas de estudo.
- Mapear empresas-alvo.
- Mapear cargos-alvo.
- Sugerir posicionamento de mercado.

## Entrada esperada

- Perfil atual.
- Objetivo profissional.
- Mercado alvo.
- Prazo desejado.
- Tecnologias de interesse.

## Saída esperada

- Plano de carreira.
- Roadmap de estudos.
- Certificações recomendadas.
- Ações práticas.
EOF
```

---

# 15. Agentes

## Passo 24 — Criar agentes com CrewAI

Criar arquivo:

```bash
cat > apps/agents/crew.py <<'EOF'
from crewai import Agent, Task, Crew

linkedin_writer = Agent(
    role="LinkedIn Writer",
    goal="Criar conteúdo técnico para fortalecer autoridade profissional.",
    backstory="Especialista em DevOps, SRE, AWS, Kubernetes, Terraform, DevSecOps e FinOps."
)

resume_optimizer = Agent(
    role="Resume Optimizer",
    goal="Adaptar currículos para vagas internacionais de tecnologia.",
    backstory="Especialista em ATS, recrutamento internacional e currículos técnicos."
)

career_strategist = Agent(
    role="Career Strategist",
    goal="Criar planos de carreira e posicionamento profissional.",
    backstory="Especialista em carreira internacional para profissionais de tecnologia."
)

task = Task(
    description="Criar um post para LinkedIn sobre otimização de custos AWS usando FinOps.",
    agent=linkedin_writer,
    expected_output="Post pronto para LinkedIn em português."
)

crew = Crew(
    agents=[linkedin_writer, resume_optimizer, career_strategist],
    tasks=[task]
)

result = crew.kickoff()
print(result)
EOF
```

---

## Passo 25 — Fluxos com LangGraph

Fluxos planejados:

```text
content_graph
resume_graph
job_match_graph
interview_graph
recruiter_graph
knowledge_ingestion_graph
```

### content_graph

```text
Receber tema
↓
Buscar contexto no Obsidian
↓
Buscar histórico no PostgreSQL
↓
Gerar rascunho
↓
Revisar tom
↓
Gerar versão final
↓
Salvar no banco
↓
Enviar para revisão humana
```

### resume_graph

```text
Receber vaga
↓
Buscar currículo base
↓
Extrair requisitos
↓
Comparar perfil
↓
Gerar versão adaptada
↓
Salvar versão
↓
Gerar relatório de aderência
```

---

# 16. MCPs

## Passo 26 — Configurar MCPs

Criar diretórios:

```bash
mkdir -p mcp/configs
mkdir -p mcp/openclaw
mkdir -p mcp/claude
mkdir -p mcp/kiro
```

MCPs recomendados:

```text
filesystem
github
git
postgresql
obsidian
playwright
browser
fetch
memory
```

Uso por ferramenta:

| MCP | Uso |
|---|---|
| Filesystem MCP | Ler e escrever arquivos do projeto |
| GitHub MCP | Consultar portfólio e repositórios |
| Git MCP | Histórico de commits |
| PostgreSQL MCP | Consultar dados estruturados |
| Obsidian MCP | Ler base de conhecimento |
| Playwright MCP | Navegação web controlada |
| Browser MCP | Pesquisa e análise de páginas |
| Fetch MCP | Buscar conteúdo HTTP |
| Memory MCP | Memória persistente adicional |

---

# 17. OpenClaw

## Passo 27 — Usar OpenClaw como assistente principal

O OpenClaw será usado como:

- Interface principal de agente.
- Orquestrador de Skills.
- Orquestrador de MCPs.
- Assistente conectado à memória.
- Assistente de carreira.
- Assistente de LinkedIn.
- Assistente de currículo.
- Assistente de entrevistas.

Funções principais:

```text
/oracle post linkedin sobre terraform
/oracle analisar vaga
/oracle adaptar curriculo
/oracle preparar entrevista
/oracle listar recrutadores
/oracle gerar relatorio semanal
/oracle buscar memoria obsidian sobre ecs
```

---

# 18. Observabilidade

## Passo 28 — Instalar Prometheus e Grafana

```bash
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo add grafana https://grafana.github.io/helm-charts
helm repo update
```

Instalar:

```bash
helm install kube-prometheus-stack prometheus-community/kube-prometheus-stack \
  -n oracle-observability
```

Acessar Grafana:

```bash
kubectl -n oracle-observability port-forward svc/kube-prometheus-stack-grafana 3001:80
```

---

## Passo 29 — Instalar Loki

```bash
helm install loki grafana/loki-stack \
  -n oracle-observability
```

---

# 19. Segurança

## Passo 30 — Instalar Trivy Operator

```bash
helm repo add aqua https://aquasecurity.github.io/helm-charts/
helm repo update

helm install trivy-operator aqua/trivy-operator \
  -n oracle-security
```

Verificar relatórios:

```bash
kubectl get vulnerabilityreports -A
```

---

## Passo 31 — Instalar Kyverno

```bash
helm repo add kyverno https://kyverno.github.io/kyverno/
helm repo update

helm install kyverno kyverno/kyverno \
  -n oracle-security
```

Políticas recomendadas:

- Bloquear containers privilegiados.
- Exigir resources limits.
- Exigir probes.
- Bloquear imagens `latest` em produção.
- Exigir execução como non-root.
- Bloquear secrets em manifests públicos.

---

# 20. GitOps

## Passo 32 — Instalar Argo CD

```bash
kubectl apply -n argocd \
  -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
```

Acessar:

```bash
kubectl -n argocd port-forward svc/argocd-server 8081:443
```

Senha inicial:

```bash
kubectl -n argocd get secret argocd-initial-admin-secret \
  -o jsonpath="{.data.password}" | base64 -d
```

---

# 21. Telegram Bot

## Passo 33 — Criar integração com Telegram

Objetivo:

- Receber notificações.
- Aprovar posts.
- Receber resumo diário.
- Receber resumo semanal.
- Receber alertas de vagas.
- Receber lembretes de follow-up.

Variáveis:

```env
TELEGRAM_BOT_TOKEN=
TELEGRAM_CHAT_ID=
```

Fluxo ideal:

```text
Oracle gera post
↓
Envia para Telegram
↓
Usuário aprova ou edita
↓
Oracle salva status
↓
Usuário publica manualmente no LinkedIn
```

---

# 22. LinkedIn — Regras de Uso Seguro

O Oracle deve ajudar no LinkedIn, mas não deve operar de forma agressiva.

Evitar:

- Spam.
- Envio automático em massa.
- Scraping pesado.
- Publicação automática sem revisão.
- Comentários automáticos sem revisão.
- Login automatizado inseguro.
- Armazenar senha do LinkedIn.

Usar para:

- Gerar posts.
- Gerar comentários.
- Gerar mensagens.
- Organizar recrutadores.
- Organizar ideias.
- Medir evolução.
- Sugerir ações.

Regra principal:

```text
Toda ação pública no LinkedIn deve ter revisão humana.
```

---

# 23. Makefile

Criar Makefile:

```bash
cat > Makefile <<'EOF'
cluster-create:
	k3d cluster create oracle --servers 1 --agents 2 --api-port 6550 -p "8080:80@loadbalancer" -p "8443:443@loadbalancer"

namespaces:
	kubectl create namespace oracle-ai --dry-run=client -o yaml | kubectl apply -f -
	kubectl create namespace oracle-data --dry-run=client -o yaml | kubectl apply -f -
	kubectl create namespace oracle-mcp --dry-run=client -o yaml | kubectl apply -f -
	kubectl create namespace oracle-automation --dry-run=client -o yaml | kubectl apply -f -
	kubectl create namespace oracle-observability --dry-run=client -o yaml | kubectl apply -f -
	kubectl create namespace oracle-security --dry-run=client -o yaml | kubectl apply -f -
	kubectl create namespace argocd --dry-run=client -o yaml | kubectl apply -f -

build-api:
	docker build -t oracle-api:local -f docker/api.Dockerfile .
	k3d image import oracle-api:local -c oracle

build-dashboard:
	docker build -t oracle-dashboard:local -f docker/dashboard.Dockerfile .
	k3d image import oracle-dashboard:local -c oracle

deploy-api:
	kubectl apply -f kubernetes/base/api/deployment.yaml

deploy-dashboard:
	kubectl apply -f kubernetes/base/dashboard/deployment.yaml

port-api:
	kubectl -n oracle-ai port-forward svc/oracle-api 8000:8000

port-dashboard:
	kubectl -n oracle-ai port-forward svc/oracle-dashboard 8501:8501

port-openwebui:
	kubectl -n oracle-ai port-forward svc/open-webui 3000:80

port-n8n:
	kubectl -n oracle-automation port-forward svc/n8n 5678:5678

port-grafana:
	kubectl -n oracle-observability port-forward svc/kube-prometheus-stack-grafana 3001:80
EOF
```

---

# 24. MVP Recomendado

O MVP inicial deve conter:

```text
k3d
PostgreSQL + pgvector
Redis
MinIO
Ollama
Open WebUI
LiteLLM
FastAPI
Streamlit
n8n
Skills básicas
MCP configs
Prometheus
Grafana
Loki
Trivy
Kyverno
```

O MVP deve entregar:

- Dashboard inicial.
- API funcionando.
- IA local funcionando.
- Banco funcionando.
- Memória estruturada criada.
- Obsidian planejado como memória humana.
- Geração de posts.
- Geração de mensagens.
- Cadastro de vagas.
- Cadastro de recrutadores.
- Geração de currículo adaptado.
- Relatório semanal.

---

# 25. Roadmap de 90 Dias

## Primeiros 15 dias

- Criar repositório.
- Criar documentação.
- Criar cluster local.
- Subir PostgreSQL.
- Subir Redis.
- Subir MinIO.
- Subir Ollama.
- Subir Open WebUI.
- Subir FastAPI.
- Subir Streamlit.

## Dias 16 a 30

- Criar schema do banco.
- Criar Skills.
- Criar agentes básicos.
- Criar dashboard com dados reais.
- Criar fluxo n8n diário.
- Criar integração Telegram.

## Dias 31 a 45

- Integrar Obsidian.
- Criar pipeline de ingestão.
- Criar pgvector com embeddings.
- Criar busca semântica.
- Criar Job Matcher.
- Criar Resume Optimizer.

## Dias 46 a 60

- Configurar MCPs.
- Integrar GitHub.
- Criar fluxo de posts.
- Criar fluxo de recrutadores.
- Criar relatórios semanais.
- Criar Interview Coach.

## Dias 61 a 75

- Melhorar observabilidade.
- Adicionar Trivy.
- Adicionar Kyverno.
- Adicionar Argo CD.
- Criar GitOps.
- Criar Helm charts.

## Dias 76 a 90

- Refinar arquitetura.
- Melhorar segurança.
- Melhorar prompts.
- Melhorar dashboard.
- Criar documentação final.
- Preparar versão v1.0.

---

# 26. Ordem Recomendada de Subida

```text
1. k3d
2. Namespaces
3. PostgreSQL + pgvector
4. Redis
5. MinIO
6. Ollama
7. Open WebUI
8. LiteLLM
9. FastAPI
10. Streamlit
11. n8n
12. Skills
13. Agentes
14. MCPs
15. OpenClaw
16. Telegram
17. Prometheus
18. Grafana
19. Loki
20. Trivy
21. Kyverno
22. Argo CD
```

---

# 27. Comandos de Validação

Ver pods:

```bash
kubectl get pods -A
```

Ver services:

```bash
kubectl get svc -A
```

Ver logs da API:

```bash
kubectl logs -n oracle-ai deploy/oracle-api
```

Ver logs do dashboard:

```bash
kubectl logs -n oracle-ai deploy/oracle-dashboard
```

Ver logs do Ollama:

```bash
kubectl logs -n oracle-ai deploy/ollama
```

Ver banco:

```bash
kubectl get pods -n oracle-data
```

Testar API:

```bash
curl http://localhost:8000/health
```

---

# 28. Critérios de Sucesso

O projeto será considerado funcional quando:

- O Kubernetes local estiver rodando.
- O Open WebUI estiver acessível.
- O Ollama estiver servindo modelos.
- O PostgreSQL estiver funcionando.
- O pgvector estiver habilitado.
- O Redis estiver funcionando.
- O MinIO estiver funcionando.
- A API estiver respondendo.
- O dashboard estiver acessível.
- O n8n estiver acessível.
- As Skills estiverem criadas.
- O primeiro post de LinkedIn for gerado.
- A primeira vaga for analisada.
- O primeiro currículo for adaptado.
- O primeiro relatório semanal for gerado.

---

# 29. Conclusão

O **Oracle Professional Intelligence** será um segundo cérebro profissional baseado em IA, construído com ferramentas open source e executado em Kubernetes local.

Ele terá como missão transformar conhecimento profissional, experiências técnicas, documentação pessoal, histórico de carreira, LinkedIn, vagas, currículos e entrevistas em inteligência prática para evolução profissional.

A arquitetura recomendada usa:

```text
OpenClaw
Ollama
Open WebUI
LiteLLM
CrewAI
LangGraph
PostgreSQL
pgvector
Redis
MinIO
Obsidian
MCPs
n8n
FastAPI
Streamlit
Kubernetes
Argo CD
Prometheus
Grafana
Loki
Trivy
Kyverno
```

A implementação deve começar simples, com um MVP local, e evoluir gradualmente para um ecossistema completo de inteligência profissional.


---

# 30. Arquitetura Multi-LLM (Recomendado)

O Oracle não deve depender de um único modelo.

A arquitetura recomendada é Multi-LLM, permitindo escolher o melhor modelo para cada tarefa.

## Objetivos

- Reduzir dependência de fornecedor.
- Utilizar modelos locais e externos.
- Reduzir custos.
- Melhorar qualidade das respostas.
- Escolher o melhor modelo para cada cenário.

## Arquitetura

```text
Open WebUI
      │
      ▼
    LiteLLM
      │
      ├── Claude
      ├── Ollama
      ├── OpenAI
      ├── Gemini
      └── DeepSeek
```

## Modelos Recomendados

### Claude

Uso:

- LinkedIn
- Currículos
- Entrevistas
- Carreira
- Storytelling
- Escrita profissional

### Ollama

Uso:

- Execução local
- Privacidade
- Desenvolvimento offline
- Laboratório pessoal

### Qwen 3

Uso:

- DevOps
- AWS
- Kubernetes
- Terraform
- Linux
- Automação

### Qwen Coder

Uso:

- Programação
- Refatoração
- Scripts
- Python
- Golang
- Kubernetes YAML

### DeepSeek

Uso:

- Pesquisa
- Comparações
- Análises técnicas

## Perfis de Agentes

```text
Oracle Career
→ Claude

Oracle LinkedIn
→ Claude

Oracle Interview Coach
→ Claude

Oracle Resume Optimizer
→ Claude

Oracle DevOps
→ Qwen

Oracle Kubernetes
→ Qwen

Oracle Terraform
→ Qwen

Oracle AWS
→ Claude + Qwen

Oracle Research
→ DeepSeek

Oracle Local
→ Ollama
```

## Configuração Recomendada

```text
Open WebUI
LiteLLM
Claude Sonnet
Ollama
Qwen3 32B
Qwen Coder
PostgreSQL
pgvector
Redis
MinIO
OpenClaw
CrewAI
LangGraph
Obsidian
```

## Resultado

O usuário poderá selecionar manualmente o modelo desejado ou permitir que o Oracle escolha automaticamente o melhor modelo para cada tarefa.
