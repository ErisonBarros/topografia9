# Servidor MCP `openbot`

Conecta o Claude (Desktop/Cowork) a este repositório: o Claude passa a ler e
atualizar `pendencias.md`, `semanas/` e `notas/` por meio de ferramentas
específicas e a sincronizar tudo com o GitHub.

- Linguagem: Python ≥ 3.10, SDK oficial `mcp` (1.x, `FastMCP`)
- Transporte: stdio (processo local, sem porta aberta)
- Dependências: declaradas no próprio script (PEP 723); o `uv` instala no cache
  local, fora do Google Drive — nenhum `.venv` é criado na pasta sincronizada.

## Ferramentas

| Grupo | Ferramenta | O que faz |
|---|---|---|
| Consulta | `visao_geral` | Estado do git, pendências e lista de arquivos |
| | `listar_arquivos(pasta)` | Lista `.md`/`.txt` |
| | `ler_arquivo(caminho)` | Lê um arquivo do repositório |
| | `listar_pendencias(prioridade)` | Pendências por seção |
| | `ler_semana(data)` | Plano da semana que contém a data |
| Pendências | `adicionar_pendencia(o_que, prioridade, prazo, proximo_passo)` | `urgente` \| `importante` \| `pode_esperar` |
| | `concluir_pendencia(trecho)` | Move para ✅ Concluído com a data |
| | `mudar_prioridade(trecho, nova_prioridade)` | Reclassifica |
| Semanas | `criar_semana(data)` | Cria `semanas/AAAA-MM-DD.md` (segunda-feira) |
| | `adicionar_tarefa_semana(tarefa, dia)` | Inclui `- [ ] tarefa` no dia (cria a semana se faltar) |
| | `marcar_tarefa_semana(trecho, data, feita)` | Marca/desmarca `[x]` |
| Notas | `criar_nota(assunto, conteudo, data)` | Cria `notas/AAAA-MM-DD-assunto.md` |
| | `escrever_arquivo(caminho, conteudo, sobrescrever)` | Escrita livre (somente `.md`/`.txt`) |
| Git | `git_status`, `git_diff` | Estado e alterações locais |
| | `git_sincronizar` | `git pull --rebase --autostash` |
| | `git_publicar(mensagem)` | `add -A` → `commit` → `pull --rebase` → `push` |

Datas aceitas: `AAAA-MM-DD`, `DD/MM/AAAA` ou `DD/MM` (ano corrente); vazio = hoje.

## Segurança

- Todo caminho é resolvido e confinado à raiz do repositório (bloqueia `../`).
- `.git/`, `.venv/` e similares são inacessíveis; escrita só em `.md`/`.txt`.
- Não há ferramenta de exclusão; nada é sobrescrito sem `sobrescrever=True`.
- O `git push` usa as credenciais já salvas no Git Credential Manager.
- Quebras de linha (CRLF/LF) e codificação UTF-8 dos arquivos são preservadas.

## Instalação (Windows)

Pré-requisitos: Git for Windows e `uv` (`winget install astral-sh.uv`).

```powershell
cd "G:\Meu Drive\OpenBot"
git pull
powershell -ExecutionPolicy Bypass -File .\mcp_server\instalar.ps1
```

O script pré-instala as dependências e acrescenta a entrada `openbot` ao
`claude_desktop_config.json` (faz backup `.bak` antes). Em seguida, **saia** do
Claude Desktop pela bandeja do sistema e abra de novo.

Configuração equivalente, se preferir editar à mão:

```json
{
  "mcpServers": {
    "openbot": {
      "command": "C:\\Users\\USUARIO\\.local\\bin\\uv.exe",
      "args": ["run", "--script", "G:\\Meu Drive\\OpenBot\\mcp_server\\openbot_mcp.py"],
      "env": { "OPENBOT_REPO": "G:\\Meu Drive\\OpenBot", "PYTHONIOENCODING": "utf-8" }
    }
  }
}
```

## Teste manual

```powershell
# inspetor web oficial do MCP (requer Node.js)
npx @modelcontextprotocol/inspector uv run --script .\mcp_server\openbot_mcp.py
```

## Variáveis de ambiente

| Variável | Padrão | Uso |
|---|---|---|
| `OPENBOT_REPO` | `G:\Meu Drive\OpenBot` | Caminho do clone local |
| `OPENBOT_GIT_TIMEOUT` | `120` | Timeout (s) dos comandos git |

## Exemplos de pedidos ao Claude

- "Sincronize o OpenBot e me mostre as pendências urgentes."
- "Adicione como urgente: enviar parecer do TCC, prazo 21/11, próximo passo revisar o cap. 3."
- "Coloque 'Campo GNSS no Campus' na terça 24/11 e publique."
- "Crie uma nota da reunião do colegiado com estes pontos: …"
