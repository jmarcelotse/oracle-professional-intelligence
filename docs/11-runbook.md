# Runbook Operacional

## Cluster alvo

kind `nxt-cluster-staging` (K8s v1.35, 1 control-plane + 3 workers), contexto
`kind-nxt-cluster-staging`. Já hospeda outros workloads (argocd, ingress-nginx,
metallb, backstage, sacola) — o Oracle vive nos namespaces `oracle-*`.

## Subir o MVP

```bash
make bootstrap     # ou: make namespaces data migrate ai apps
```

## Acessos rápidos

| Serviço     | Comando               | URL                     |
|-------------|-----------------------|-------------------------|
| API         | `make port-api`       | http://localhost:8000   |
| Dashboard   | `make port-dashboard` | http://localhost:8501   |
| Open WebUI  | `make port-openwebui` | http://localhost:3000   |
| Postgres    | `make port-postgres`  | localhost:5432          |

## Validação

```bash
kubectl get pods -n oracle-data
kubectl get pods -n oracle-ai
curl http://localhost:8000/health           # {"database":"up"}
curl http://localhost:8000/stats
```

## Problemas conhecidos

### kube-proxy em CrashLoopBackOff: "too many open files"

Em hosts rodando kind com vários nós, o limite de **inotify** do host
(`fs.inotify.max_user_instances`, default 128) se esgota e o `kube-proxy`
não inicia. Sem ele, o ClusterIP `10.96.0.1:443` deixa de rotear e cai em
cascata: coredns, local-path-provisioner, metallb e os apps.

**Diagnóstico:**

```bash
kubectl get pods -n kube-system -l k8s-app=kube-proxy
kubectl logs -n kube-system -l k8s-app=kube-proxy --tail=20 | grep "too many open files"
cat /proc/sys/fs/inotify/max_user_instances
```

**Correção (host, persistente):**

```bash
sudo tee /etc/sysctl.d/99-kind-inotify.conf >/dev/null <<'EOF'
fs.inotify.max_user_instances = 1024
fs.inotify.max_user_watches = 1048576
EOF
sudo sysctl --system
```

Depois, destrave os componentes:

```bash
kubectl rollout restart daemonset/kube-proxy -n kube-system
kubectl rollout restart deploy/coredns -n kube-system
kubectl rollout restart deploy/local-path-provisioner -n local-path-storage
```

### PVC fica Pending

Verifique o `local-path-provisioner` (provisionador da StorageClass `standard`):

```bash
kubectl get pods -n local-path-storage
kubectl logs -n local-path-storage deploy/local-path-provisioner --tail=20
```

Se ele estiver em crashloop reclamando de timeout em `10.96.0.1:443`, a causa
provável é o kube-proxy (ver acima).

## Imagens locais (kind)

As imagens da API/dashboard são buildadas localmente e carregadas com
`kind load docker-image <img> --name nxt-cluster-staging` (não há registry).
Por isso os deployments usam `imagePullPolicy: IfNotPresent`.
