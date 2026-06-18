#!/usr/bin/env bash
# Instala a camada de IA do Oracle (Ollama, Open WebUI, LiteLLM) no oracle-ai.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

echo ">> Ollama"
kubectl apply -f "$ROOT/kubernetes/base/ollama/deployment.yaml"
kubectl -n oracle-ai rollout status deploy/ollama --timeout=180s

echo ">> Baixando modelos (pode demorar)..."
# Modelos pequenos por padrão: host com ~15Gi de RAM compartilhada não comporta
# modelos 7B. Em máquina com mais RAM/GPU, troque por qwen2.5-coder / llama3.1.
kubectl -n oracle-ai exec deploy/ollama -- ollama pull qwen2.5-coder:1.5b || true
kubectl -n oracle-ai exec deploy/ollama -- ollama pull nomic-embed-text || true

echo ">> Open WebUI"
kubectl apply -f "$ROOT/kubernetes/base/open-webui/deployment.yaml"

echo ">> LiteLLM"
kubectl apply -f "$ROOT/kubernetes/base/litellm/deployment.yaml"

kubectl get pods -n oracle-ai
