#!/usr/bin/env bash
# Builda as imagens da API e do dashboard, carrega no cluster kind e aplica
# os manifestos. Usa a variável KIND_CLUSTER (default: nxt-cluster-staging).
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
KIND_CLUSTER="${KIND_CLUSTER:-nxt-cluster-staging}"

echo ">> build oracle-api:local"
docker build -t oracle-api:local -f "$ROOT/docker/api.Dockerfile" "$ROOT"
kind load docker-image oracle-api:local --name "$KIND_CLUSTER"

echo ">> build oracle-dashboard:local"
docker build -t oracle-dashboard:local -f "$ROOT/docker/dashboard.Dockerfile" "$ROOT"
kind load docker-image oracle-dashboard:local --name "$KIND_CLUSTER"

echo ">> deploy"
kubectl apply -f "$ROOT/kubernetes/base/api/deployment.yaml"
kubectl apply -f "$ROOT/kubernetes/base/dashboard/deployment.yaml"

kubectl -n oracle-ai rollout status deploy/oracle-api --timeout=120s
kubectl -n oracle-ai rollout status deploy/oracle-dashboard --timeout=120s
kubectl get pods -n oracle-ai
