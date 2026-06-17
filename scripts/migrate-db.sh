#!/usr/bin/env bash
# Aplica as migrations SQL no PostgreSQL via kubectl exec (sem depender de
# psql no host).
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
NS=oracle-data
POD=oracle-postgres-postgresql-0
DB=oracle_professional_intelligence

for f in "$ROOT"/database/migrations/*.sql; do
  echo ">> aplicando $(basename "$f")"
  kubectl exec -i -n "$NS" "$POD" -- \
    psql -U oracle -d "$DB" -v ON_ERROR_STOP=1 < "$f"
done

echo ">> migrations aplicadas."
