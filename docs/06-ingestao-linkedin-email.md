# Ingestão de vagas do LinkedIn por e-mail (sem scraping)

Em vez de varrer o LinkedIn (proibido pelos ToS e pelo próprio spec, seção 22),
o Oracle usa o **recurso oficial de alertas do LinkedIn**: ele te manda as vagas
por e-mail, o n8n lê esses e-mails e grava na tabela `jobs`. Seguro e legítimo.

```
LinkedIn (alerta de vaga) → e-mail (Hotmail) → n8n (IMAP) → POST /jobs/ingest → tabela jobs → Dashboard
```

## Passo 1 — Criar o alerta de vaga no LinkedIn

1. LinkedIn → **Vagas** → busque por cargo (ex.: "SRE", "DevOps", "Platform Engineer").
2. Aplique filtros (localização, remoto, nível).
3. Ative **"Criar alerta de vaga"** e escolha frequência **diária** e canal **e-mail**.
4. Repita para cada cargo-alvo. Os e-mails virão de `jobs-noreply@linkedin.com`
   / `jobalerts-noreply@linkedin.com`.

## Passo 2 — App password do Hotmail (para o IMAP)

O Outlook/Hotmail exige **autenticação em duas etapas + app password** para IMAP:

1. Acesse https://account.microsoft.com/security
2. Ative a **verificação em duas etapas** (se ainda não estiver).
3. Em **Opções de segurança avançadas → Senhas de aplicativo → Criar nova**.
4. Copie a senha gerada (use no n8n, não a sua senha normal).

Dados IMAP do Outlook/Hotmail:

| Campo | Valor |
|---|---|
| Host | `outlook.office365.com` |
| Porta | `993` |
| SSL/TLS | sim |
| Usuário | `jmarcelotse@hotmail.com` |
| Senha | a **app password** do passo acima |

> Se a Microsoft tiver desativado o IMAP/basic-auth na sua conta, use o nó
> **Microsoft Outlook** do n8n (OAuth2 via Azure App Registration) em vez do IMAP.

## Passo 3 — Credencial IMAP no n8n

1. Abra o n8n → **Credentials → New → IMAP**.
2. Preencha com os dados acima. Salve como "Hotmail IMAP".

## Passo 4 — Importar e ativar o workflow

1. n8n → **Import from File** → `workflows/n8n/linkedin-jobs-ingestion.json`.
2. No nó **"IMAP: e-mails do LinkedIn"**, selecione a credencial "Hotmail IMAP".
3. Rode uma vez manualmente (**Execute Workflow**) para testar.
4. Confira no Dashboard (aba **Vagas**) ou:
   ```bash
   curl -H "Host: api.oracle.local" http://172.18.255.200/jobs
   ```
5. Se vier certo, **Active** o workflow (passa a rodar sozinho a cada novo e-mail).

## Passo 5 — Ajustar o parser (provável, uma vez)

O layout dos e-mails do LinkedIn muda com o tempo. Se as vagas vierem com título
errado ou faltando:

1. No nó **"Parsear vagas"**, veja a saída do nó IMAP (campo `textHtml`).
2. Ajuste o regex no código conforme a estrutura real do e-mail.

O endpoint `/jobs/ingest` é **idempotente** (deduplica por `job_url`), então pode
rodar quantas vezes quiser sem criar vagas repetidas.

## Recrutadores

Mesma ideia: quando um recrutador te contata, o LinkedIn manda **notificação por
e-mail**. Dá para criar um segundo workflow filtrando essas notificações e
postando em `/recruiters/ingest` (também idempotente). A *descoberta* ativa de
recrutadores (prospecção) continua manual — scraping de LinkedIn está fora por
segurança da sua conta.
