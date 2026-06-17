#!/usr/bin/env bash
# Bootstrap do MVP do Oracle em um cluster kind JÁ existente.
# Ordem: namespaces -> dados -> migrations -> IA -> apps.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
export KIND_CLUSTER="${KIND_CLUSTER:-nxt-cluster-staging}"

echo "=================================================="
echo " Oracle MVP bootstrap — cluster kind: $KIND_CLUSTER"
echo "=================================================="

echo ">> [1/5] namespaces"
kubectl apply -f "$ROOT/kubernetes/namespaces/namespaces.yaml"

echo ">> [2/5] camada de dados (Postgres+pgvector, Redis, MinIO)"
bash "$ROOT/scripts/install-data-stack.sh"

echo ">> [3/5] migrations"
bash "$ROOT/scripts/migrate-db.sh"

echo ">> [4/5] camada de IA (Ollama, Open WebUI, LiteLLM)"
bash "$ROOT/scripts/install-ai-stack.sh"

echo ">> [5/5] apps (API + dashboard)"
bash "$ROOT/scripts/build-and-deploy-apps.sh"

echo
echo "MVP no ar. Use o Makefile (port-*) para acessar os serviços."
