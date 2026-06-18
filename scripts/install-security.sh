#!/usr/bin/env bash
# Instala a camada de segurança do Oracle no namespace oracle-security:
# Kyverno (políticas de baseline em modo Audit) + Trivy Operator (scans de
# vulnerabilidade e config audit), escopado aos namespaces oracle-*.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

helm repo add kyverno https://kyverno.github.io/kyverno/ >/dev/null 2>&1 || true
helm repo add aqua https://aquasecurity.github.io/helm-charts/ >/dev/null 2>&1 || true
helm repo update kyverno aqua >/dev/null

echo ">> Kyverno (réplicas únicas — sem HA, adequado a lab local)"
helm upgrade --install kyverno kyverno/kyverno -n oracle-security --create-namespace \
  --set admissionController.replicas=1 \
  --set backgroundController.replicas=1 \
  --set cleanupController.replicas=1 \
  --set reportsController.replicas=1 \
  --wait --timeout=180s

echo ">> Políticas de baseline (Audit, escopo oracle-*)"
kubectl apply -f "$ROOT/kubernetes/base/security/kyverno-policies.yaml"

echo ">> Trivy Operator (escopo oracle-*, 1 scan por vez)"
helm upgrade --install trivy-operator aqua/trivy-operator -n oracle-security \
  --set="targetNamespaces=oracle-ai\,oracle-data\,oracle-automation\,oracle-observability" \
  --set="operator.scanJobsConcurrentLimit=1" \
  --set="trivy.ignoreUnfixed=true" \
  --set="trivy.resources.requests.memory=100Mi" \
  --set="trivy.resources.limits.memory=500Mi" \
  --wait --timeout=180s

kubectl get pods -n oracle-security
echo
echo "Relatórios:"
echo "  kubectl get policyreport -A          # Kyverno (audit)"
echo "  kubectl get vulnerabilityreports -A  # Trivy (CVEs)"
echo "  kubectl get configauditreports -A    # Trivy (config)"
