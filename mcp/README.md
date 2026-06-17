# MCPs do Oracle

Os MCP servers rodam **no lado do cliente** (Claude Code/Desktop, OpenClaw,
Kiro) como subprocessos — não consomem RAM do cluster. Eles dão ao assistente
acesso a arquivos, Git/GitHub, banco, Obsidian e web.

## MCPs configurados

| MCP | Uso | Runtime |
|---|---|---|
| filesystem | Ler/escrever arquivos do projeto | `npx @modelcontextprotocol/server-filesystem` |
| git | Histórico/commits do repo local | `uvx mcp-server-git` |
| github | Portfólio e repositórios | `npx @modelcontextprotocol/server-github` |
| postgres | Consultar a memória estruturada | `npx @modelcontextprotocol/server-postgres` |
| obsidian | Ler a base de conhecimento | `npx mcp-obsidian` |
| fetch | Buscar conteúdo HTTP | `uvx mcp-server-fetch` |
| memory | Memória persistente adicional | `npx @modelcontextprotocol/server-memory` |

## Variáveis a definir

Antes de usar, exporte (ou substitua nos arquivos):

```bash
export ORACLE_REPO_PATH="$(pwd)"                       # raiz deste repositório
export OBSIDIAN_VAULT_PATH="$HOME/Obsidian/Oracle-Knowledge"
export GITHUB_TOKEN="ghp_..."                          # PAT com escopo de leitura
```

## Conectar o Postgres MCP ao banco no cluster

O banco roda no Kubernetes. Abra um túnel antes de usar o MCP:

```bash
make port-postgres   # expõe oracle-postgres-postgresql em localhost:5432
```

A connection string já aponta para `localhost:5432` nos configs.

## Onde colocar cada config

| Cliente | Arquivo | Caminho típico |
|---|---|---|
| Claude Code | `claude/.mcp.json` | raiz do projeto (`.mcp.json`) |
| Claude Desktop | `claude/claude_desktop_config.json` | `~/Library/Application Support/Claude/` (macOS) / `%APPDATA%/Claude/` (Win) |
| OpenClaw | `openclaw/mcp.json` | conforme docs do OpenClaw |
| Kiro | `kiro/mcp.json` | `.kiro/settings/mcp.json` |

O conteúdo é o mesmo formato `mcpServers`; veja também `configs/mcp.json` como
referência canônica.
