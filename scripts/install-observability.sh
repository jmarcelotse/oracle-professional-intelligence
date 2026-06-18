#!/usr/bin/env bash
# Instala uma observabilidade enxuta (Prometheus + Grafana) no namespace
# oracle-observability. Versão leve (sem node-exporter/alertmanager) adequada
# a hosts com pouca RAM; o Prometheus raspa cAdvisor/kubelet via apiserver.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

kubectl apply -f "$ROOT/kubernetes/base/observability/prometheus.yaml"
kubectl apply -f "$ROOT/kubernetes/base/observability/grafana.yaml"

kubectl -n oracle-observability rollout status deploy/prometheus --timeout=120s || true
kubectl -n oracle-observability rollout status deploy/grafana --timeout=120s || true

kubectl get pods -n oracle-observability
echo
echo "Grafana: make port-grafana  -> http://localhost:3001 (admin / oracle)"
echo "Prometheus: make port-prometheus -> http://localhost:9090"
