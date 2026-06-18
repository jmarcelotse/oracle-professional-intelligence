#!/usr/bin/env bash
# Instala a camada de dados do Oracle (PostgreSQL+pgvector, Redis, MinIO)
# via manifestos próprios (imagens oficiais) no namespace oracle-data.
#
# Nota: optamos por manifestos próprios em vez do chart Bitnami porque a imagem
# oficial pgvector/pgvector é incompatível com o chart Bitnami (entrypoint/layout
# e /var/run/postgresql read-only).
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

kubectl apply -f "$ROOT/kubernetes/namespaces/namespaces.yaml"

echo ">> PostgreSQL + pgvector"
kubectl apply -f "$ROOT/kubernetes/base/postgres/statefulset.yaml"

echo ">> Redis"
kubectl apply -f "$ROOT/kubernetes/base/redis/deployment.yaml"

echo ">> MinIO"
kubectl apply -f "$ROOT/kubernetes/base/minio/deployment.yaml"

echo ">> Aguardando pods..."
kubectl -n oracle-data rollout status statefulset/oracle-postgres-postgresql --timeout=180s || true
kubectl -n oracle-data rollout status deploy/oracle-redis --timeout=120s || true
kubectl -n oracle-data rollout status deploy/oracle-minio --timeout=180s || true

echo ">> Criando bucket oracle-files no MinIO"
kubectl -n oracle-data exec deploy/oracle-minio -- sh -c '
  mc alias set local http://localhost:9000 "$MINIO_ROOT_USER" "$MINIO_ROOT_PASSWORD" >/dev/null 2>&1 &&
  mc mb -p local/oracle-files >/dev/null 2>&1 || true
' || echo "(crie o bucket manualmente se necessário)"

kubectl get pods -n oracle-data
