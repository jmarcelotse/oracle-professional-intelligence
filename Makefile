KIND_CLUSTER ?= nxt-cluster-staging

.PHONY: help namespaces data migrate ai apps automation observability security \
        bootstrap build-api build-dashboard deploy-api deploy-dashboard \
        port-api port-dashboard port-openwebui port-n8n port-postgres \
        port-grafana port-prometheus status

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
	  awk 'BEGIN{FS=":.*?## "}{printf "  \033[36m%-18s\033[0m %s\n", $$1, $$2}'

bootstrap: ## Sobe o MVP inteiro no cluster kind existente
	KIND_CLUSTER=$(KIND_CLUSTER) bash scripts/bootstrap.sh

namespaces: ## Cria os namespaces oracle-*
	kubectl apply -f kubernetes/namespaces/namespaces.yaml

data: ## Instala Postgres+pgvector, Redis, MinIO
	bash scripts/install-data-stack.sh

migrate: ## Aplica as migrations SQL
	bash scripts/migrate-db.sh

ai: ## Instala Ollama, Open WebUI, LiteLLM
	bash scripts/install-ai-stack.sh

apps: ## Builda e faz deploy de API + dashboard
	KIND_CLUSTER=$(KIND_CLUSTER) bash scripts/build-and-deploy-apps.sh

build-api: ## Builda e carrega a imagem da API no kind
	docker build -t oracle-api:local -f docker/api.Dockerfile .
	kind load docker-image oracle-api:local --name $(KIND_CLUSTER)

build-dashboard: ## Builda e carrega a imagem do dashboard no kind
	docker build -t oracle-dashboard:local -f docker/dashboard.Dockerfile .
	kind load docker-image oracle-dashboard:local --name $(KIND_CLUSTER)

deploy-api: ## Aplica o manifesto da API
	kubectl apply -f kubernetes/base/api/deployment.yaml

deploy-dashboard: ## Aplica o manifesto do dashboard
	kubectl apply -f kubernetes/base/dashboard/deployment.yaml

port-api: ## Expõe a API em localhost:8000
	kubectl -n oracle-ai port-forward svc/oracle-api 8000:8000

port-dashboard: ## Expõe o dashboard em localhost:8501
	kubectl -n oracle-ai port-forward svc/oracle-dashboard 8501:8501

port-openwebui: ## Expõe o Open WebUI em localhost:3000
	kubectl -n oracle-ai port-forward svc/open-webui 3000:80

automation: ## Instala o n8n (oracle-automation)
	kubectl apply -f kubernetes/base/n8n/deployment.yaml

observability: ## Instala Prometheus + Grafana enxutos (oracle-observability)
	bash scripts/install-observability.sh

security: ## Instala Kyverno (Audit) + Trivy Operator (oracle-security)
	bash scripts/install-security.sh

port-n8n: ## Expõe o n8n em localhost:5678
	kubectl -n oracle-automation port-forward svc/n8n 5678:5678

port-grafana: ## Expõe o Grafana em localhost:3001
	kubectl -n oracle-observability port-forward svc/grafana 3001:80

port-prometheus: ## Expõe o Prometheus em localhost:9090
	kubectl -n oracle-observability port-forward svc/prometheus 9090:9090

port-postgres: ## Expõe o Postgres em localhost:5432
	kubectl -n oracle-data port-forward svc/oracle-postgres-postgresql 5432:5432

status: ## Mostra pods dos namespaces do Oracle
	kubectl get pods -n oracle-ai -n oracle-data 2>/dev/null; \
	kubectl get pods -n oracle-data; kubectl get pods -n oracle-ai
