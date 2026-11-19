# /// script
# requires-python = ">=3.10"
# dependencies = ["mcp>=1.2,<2"]
# ///
"""
Servidor MCP "openbot" — conecta o Claude ao repositório Agent_Claude_UFPE
(pendências, planos semanais e notas), com sincronização via git.

Execução (stdio):
    uv run --script openbot_mcp.py

Variáveis de ambiente:
    OPENBOT_REPO   caminho do clone local (padrão: G:\\Meu Drive\\OpenBot)
    OPENBOT_GIT_TIMEOUT   timeout, em segundos, dos comandos git (padrão: 120)
"""

from __future__ import annotations

import os
import re
import subprocess
import sys
import unicodedata
from datetime import date, datetime, timedelta
from pathlib import Path

from mcp.server.fastmcp import FastMCP

# --------------------------------------------------------------------------
# Configuração
# --------------------------------------------------------------------------
REPO = Path(os.environ.get("OPENBOT_REPO", r"G:\Meu Drive\OpenBot")).resolve()
GIT_TIMEOUT = int(os.environ.get("OPENBOT_GIT_TIMEOUT", "120"))
EXTENSOES_PERMITIDAS = {".md", ".txt"}
PASTAS_IGNORADAS = {".git", ".venv", "__pycache__", "node_modules"}

ARQ_PENDENCIAS = "pendencias.md"
PASTA_SEMANAS = "semanas"
PASTA_NOTAS = "notas"

SECOES = {
    "urgente": "🔴 Urgente",
    "importante": "🟡 Importante",
    "pode_esperar": "🟢 Pode esperar",
    "concluido": "✅ Concluído",
}
DIAS_PT = ["Seg", "Ter", "Qua", "Qui", "Sex", "Sáb", "Dom"]
PLACEHOLDER = "- _(vazio)_"

mcp = FastMCP(
    "openbot",
    instructions=(
        "Ferramentas do repositório Agent_Claude_UFPE (central de pendências, "
        "planos semanais e notas do Prof. Erison/UFPE). Fluxo recomendado: "
        "git_sincronizar antes de alterar; usar as ferramentas específicas "
        "(adicionar_pendencia, adicionar_tarefa_semana, criar_nota); ao final, "
        "git_publicar com uma mensagem de commit em português."
    ),
)


# --------------------------------------------------------------------------
# Utilitários
# --------------------------------------------------------------------------
class ErroOpenBot(Exception):
    pass


def _caminho_seguro(relativo: str) -> Path:
    """Resolve um caminho relativo garantindo que ele fique dentro do repositório."""
    relativo = (relativo or "").strip().replace("\\", "/").lstrip("/")
    destino = (REPO / relativo).resolve()
    if destino != REPO and REPO not in destino.parents:
        raise ErroOpenBot(f"Caminho fora do repositório: {relativo}")
    if any(p in PASTAS_IGNORADAS for p in destino.relative_to(REPO).parts):
        raise ErroOpenBot(f"Acesso não permitido: {relativo}")
    return destino


def _rel(p: Path) -> str:
    return p.relative_to(REPO).as_posix()


def _ler(p: Path) -> tuple[str, str]:
    """Lê texto UTF-8 normalizando quebras de linha; devolve (texto, quebra_original)."""
    bruto = p.read_bytes().decode("utf-8-sig")
    nl = "\r\n" if "\r\n" in bruto else "\n"
    return bruto.replace("\r\n", "\n"), nl


def _gravar(p: Path, texto: str, nl: str = "\n") -> None:
    p.parent.mkdir(parents=True, exist_ok=True)
    if not texto.endswith("\n"):
        texto += "\n"
    p.write_bytes(texto.replace("\n", nl).encode("utf-8"))


def _data(valor: str | None) -> date:
    """Aceita AAAA-MM-DD, DD/MM/AAAA ou DD/MM (ano corrente). Vazio = hoje."""
    if not valor:
        return date.today()
    valor = valor.strip()
    for fmt in ("%Y-%m-%d", "%d/%m/%Y", "%d/%m/%y"):
        try:
            return datetime.strptime(valor, fmt).date()
        except ValueError:
            pass
    m = re.fullmatch(r"(\d{1,2})/(\d{1,2})", valor)
    if m:
        return date(date.today().year, int(m.group(2)), int(m.group(1)))
    raise ErroOpenBot(f"Data inválida: {valor!r}. Use AAAA-MM-DD ou DD/MM/AAAA.")


def _segunda(d: date) -> date:
    return d - timedelta(days=d.weekday())


def _slug(texto: str) -> str:
    t = unicodedata.normalize("NFKD", texto).encode("ascii", "ignore").decode()
    t = re.sub(r"[^a-zA-Z0-9]+", "-", t).strip("-").lower()
    return t[:60] or "nota"


def _atualizar_carimbo(texto: str) -> str:
    hoje = date.today().strftime("%d/%m/%Y")
    return re.sub(r"(?m)^Atualizada em: .*$", f"Atualizada em: {hoje}", texto)


# --------------------------------------------------------------------------
# Pendências (parser por seções "## ")
# --------------------------------------------------------------------------
def _chave_secao(titulo: str) -> str | None:
    for chave, prefixo in SECOES.items():
        if titulo.strip().startswith(prefixo):
            return chave
    return None


def _localizar_secoes(linhas: list[str]) -> dict[str, tuple[int, int]]:
    """Mapeia chave -> (índice do título, índice final exclusivo) em pendencias.md."""
    titulos = [i for i, l in enumerate(linhas) if l.startswith("## ")]
    mapa: dict[str, tuple[int, int]] = {}
    for n, i in enumerate(titulos):
        fim = titulos[n + 1] if n + 1 < len(titulos) else len(linhas)
        chave = _chave_secao(linhas[i][3:])
        if chave:
            mapa[chave] = (i, fim)
    faltando = set(SECOES) - set(mapa)
    if faltando:
        raise ErroOpenBot(f"Seções ausentes em {ARQ_PENDENCIAS}: {', '.join(sorted(faltando))}")
    return mapa


def _itens(linhas: list[str], ini: int, fim: int) -> list[tuple[int, str]]:
    return [
        (i, linhas[i])
        for i in range(ini + 1, fim)
        if linhas[i].startswith("- ") and linhas[i].strip() != PLACEHOLDER
    ]


def _inserir_item(linhas: list[str], chave: str, item: str) -> list[str]:
    ini, fim = _localizar_secoes(linhas)[chave]
    # remove placeholder da seção
    for i in range(ini + 1, fim):
        if linhas[i].strip() == PLACEHOLDER:
            linhas[i] = item
            return linhas
    # insere após o último item da seção (ou logo após o título)
    existentes = _itens(linhas, ini, fim)
    pos = existentes[-1][0] + 1 if existentes else ini + 2
    linhas.insert(pos, item)
    return linhas


def _remover_item(linhas: list[str], chave: str, indice: int) -> list[str]:
    ini, fim = _localizar_secoes(linhas)[chave]
    del linhas[indice]
    if not _itens(linhas, ini, fim - 1):
        linhas.insert(ini + 2, PLACEHOLDER)
    return linhas


# --------------------------------------------------------------------------
# Git
# --------------------------------------------------------------------------
def _git(*args: str) -> str:
    kwargs = {}
    if sys.platform == "win32":
        kwargs["creationflags"] = 0x08000000  # CREATE_NO_WINDOW
    try:
        r = subprocess.run(
            ["git", "-C", str(REPO), *args],
            stdin=subprocess.DEVNULL,  # nunca herdar o stdin do protocolo MCP
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=GIT_TIMEOUT,
            **kwargs,
        )
    except FileNotFoundError as e:
        raise ErroOpenBot("git não encontrado no PATH.") from e
    except subprocess.TimeoutExpired as e:
        raise ErroOpenBot(f"git {' '.join(args)} excedeu {GIT_TIMEOUT}s.") from e
    saida = (r.stdout + r.stderr).strip()
    if r.returncode != 0:
        raise ErroOpenBot(f"git {' '.join(args)} falhou ({r.returncode}):\n{saida}")
    return saida


# --------------------------------------------------------------------------
# Ferramentas MCP — consulta
# --------------------------------------------------------------------------
@mcp.tool()
def visao_geral() -> str:
    """Resumo do repositório: caminho, branch, estado do git, contagem de pendências e arquivos."""
    partes = [f"Repositório: {REPO}"]
    try:
        partes.append("Git:\n" + _git("status", "-sb"))
        partes.append("Último commit: " + _git("log", "-1", "--format=%h %s (%cr, %an)"))
    except ErroOpenBot as e:
        partes.append(f"Git indisponível: {e}")
    try:
        pend = listar_pendencias()
        partes.append("Pendências:\n" + pend)
    except Exception as e:  # noqa: BLE001
        partes.append(f"Pendências: erro ao ler ({e})")
    partes.append("Arquivos:\n" + listar_arquivos())
    return "\n\n".join(partes)


@mcp.tool()
def listar_arquivos(pasta: str = "") -> str:
    """Lista os arquivos .md/.txt do repositório (ou de uma subpasta, ex.: 'semanas')."""
    base = _caminho_seguro(pasta)
    if not base.is_dir():
        raise ErroOpenBot(f"Pasta não encontrada: {pasta}")
    arquivos = []
    for p in sorted(base.rglob("*")):
        if p.is_file() and p.suffix.lower() in EXTENSOES_PERMITIDAS:
            if not any(x in PASTAS_IGNORADAS for x in p.relative_to(REPO).parts):
                arquivos.append(f"{_rel(p)}  ({p.stat().st_size} B)")
    return "\n".join(arquivos) or "(nenhum arquivo)"


@mcp.tool()
def ler_arquivo(caminho: str) -> str:
    """Lê um arquivo do repositório pelo caminho relativo (ex.: 'notas/README.md')."""
    p = _caminho_seguro(caminho)
    if not p.is_file():
        raise ErroOpenBot(f"Arquivo não encontrado: {caminho}")
    return _ler(p)[0]


@mcp.tool()
def listar_pendencias(prioridade: str = "") -> str:
    """Lista as pendências por seção. prioridade opcional: urgente | importante | pode_esperar | concluido."""
    p = _caminho_seguro(ARQ_PENDENCIAS)
    linhas = _ler(p)[0].split("\n")
    mapa = _localizar_secoes(linhas)
    chaves = [prioridade] if prioridade else list(SECOES)
    saida = []
    for ch in chaves:
        if ch not in SECOES:
            raise ErroOpenBot(f"Prioridade inválida: {ch}. Use: {', '.join(SECOES)}")
        ini, fim = mapa[ch]
        itens = [l for _, l in _itens(linhas, ini, fim)]
        saida.append(f"{SECOES[ch]} ({len(itens)})")
        saida.extend(f"  {l}" for l in itens)
    return "\n".join(saida)


@mcp.tool()
def ler_semana(data: str = "") -> str:
    """Lê o plano da semana que contém a data (AAAA-MM-DD ou DD/MM/AAAA; vazio = semana atual)."""
    seg = _segunda(_data(data))
    p = _caminho_seguro(f"{PASTA_SEMANAS}/{seg.isoformat()}.md")
    if not p.is_file():
        return f"Não existe plano para a semana de {seg:%d/%m/%Y} ({_rel(p)}). Use criar_semana."
    return _ler(p)[0]


# --------------------------------------------------------------------------
# Ferramentas MCP — escrita
# --------------------------------------------------------------------------
@mcp.tool()
def adicionar_pendencia(
    o_que: str, prioridade: str = "importante", prazo: str = "", proximo_passo: str = ""
) -> str:
    """Adiciona uma pendência em pendencias.md.

    prioridade: urgente | importante | pode_esperar
    prazo: texto livre ou data (ex.: '25/11/2026')
    proximo_passo: ação concreta seguinte
    """
    if prioridade not in ("urgente", "importante", "pode_esperar"):
        raise ErroOpenBot("prioridade deve ser: urgente, importante ou pode_esperar")
    o_que = o_que.strip()
    if not o_que:
        raise ErroOpenBot("Descreva a pendência em 'o_que'.")
    item = f"- **{o_que}** — {prazo.strip() or 'sem prazo'} — {proximo_passo.strip() or 'definir próximo passo'}"
    p = _caminho_seguro(ARQ_PENDENCIAS)
    texto, nl = _ler(p)
    linhas = _inserir_item(texto.split("\n"), prioridade, item)
    _gravar(p, _atualizar_carimbo("\n".join(linhas)), nl)
    return f"Adicionado em {SECOES[prioridade]}:\n{item}"


def _buscar_aberta(linhas: list[str], trecho: str) -> tuple[str, int, str]:
    mapa = _localizar_secoes(linhas)
    achados = []
    for ch in ("urgente", "importante", "pode_esperar"):
        ini, fim = mapa[ch]
        for i, l in _itens(linhas, ini, fim):
            if trecho.lower() in l.lower():
                achados.append((ch, i, l))
    if not achados:
        raise ErroOpenBot(f"Nenhuma pendência em aberto contém: {trecho!r}")
    if len(achados) > 1:
        lista = "\n".join(f"  [{c}] {l}" for c, _, l in achados)
        raise ErroOpenBot(f"Trecho ambíguo ({len(achados)} itens). Seja mais específico:\n{lista}")
    return achados[0]


@mcp.tool()
def concluir_pendencia(trecho: str) -> str:
    """Move para ✅ Concluído a pendência em aberto cujo texto contém 'trecho' (deve ser único)."""
    p = _caminho_seguro(ARQ_PENDENCIAS)
    texto, nl = _ler(p)
    linhas = texto.split("\n")
    ch, i, item = _buscar_aberta(linhas, trecho)
    linhas = _remover_item(linhas, ch, i)
    concluido = f"{item} _(concluído em {date.today():%d/%m/%Y})_"
    linhas = _inserir_item(linhas, "concluido", concluido)
    _gravar(p, _atualizar_carimbo("\n".join(linhas)), nl)
    return f"Concluído (veio de {SECOES[ch]}):\n{concluido}"


@mcp.tool()
def mudar_prioridade(trecho: str, nova_prioridade: str) -> str:
    """Move uma pendência em aberto (identificada por 'trecho') para outra prioridade."""
    if nova_prioridade not in ("urgente", "importante", "pode_esperar"):
        raise ErroOpenBot("nova_prioridade deve ser: urgente, importante ou pode_esperar")
    p = _caminho_seguro(ARQ_PENDENCIAS)
    texto, nl = _ler(p)
    linhas = texto.split("\n")
    ch, i, item = _buscar_aberta(linhas, trecho)
    if ch == nova_prioridade:
        return f"A pendência já está em {SECOES[ch]}."
    linhas = _remover_item(linhas, ch, i)
    linhas = _inserir_item(linhas, nova_prioridade, item)
    _gravar(p, _atualizar_carimbo("\n".join(linhas)), nl)
    return f"Movido de {SECOES[ch]} para {SECOES[nova_prioridade]}:\n{item}"


def _modelo_semana(seg: date) -> str:
    dom = seg + timedelta(days=6)
    dias = "\n\n".join(
        f"### {DIAS_PT[k]} {(seg + timedelta(days=k)):%d/%m}\n- [ ] " for k in range(7)
    )
    return (
        f"# Semana de {seg:%d/%m} a {dom:%d/%m/%Y}\n\n"
        "## Compromissos fixos\n\n| Dia | Horário | O quê |\n|---|---|---|\n| | | |\n\n"
        f"## Prazos da semana\n\n{PLACEHOLDER}\n\n"
        f"## Plano por dia\n\n{dias}\n\n"
        f"## Fica para a próxima semana\n\n{PLACEHOLDER}\n"
    )


@mcp.tool()
def criar_semana(data: str = "") -> str:
    """Cria semanas/AAAA-MM-DD.md (segunda-feira) para a semana da data informada (vazio = atual)."""
    seg = _segunda(_data(data))
    p = _caminho_seguro(f"{PASTA_SEMANAS}/{seg.isoformat()}.md")
    if p.exists():
        return f"Já existe: {_rel(p)}"
    _gravar(p, _modelo_semana(seg))
    return f"Criado: {_rel(p)}"


@mcp.tool()
def adicionar_tarefa_semana(tarefa: str, dia: str = "") -> str:
    """Adiciona '- [ ] tarefa' no dia indicado (AAAA-MM-DD ou DD/MM[/AAAA]; vazio = hoje).

    Cria o arquivo da semana se ainda não existir.
    """
    d = _data(dia)
    seg = _segunda(d)
    p = _caminho_seguro(f"{PASTA_SEMANAS}/{seg.isoformat()}.md")
    if not p.exists():
        _gravar(p, _modelo_semana(seg))
    texto, nl = _ler(p)
    linhas = texto.split("\n")
    alvo = f"{d:%d/%m}"
    idx = next(
        (i for i, l in enumerate(linhas) if l.startswith("### ") and alvo in l), None
    )
    if idx is None:
        # dia ausente (ex.: arquivo criado no meio da semana): cria o cabeçalho
        # em ordem cronológica dentro de "## Plano por dia"
        plano = next((i for i, l in enumerate(linhas) if l.startswith("## Plano por dia")), None)
        if plano is None:
            raise ErroOpenBot(f"{_rel(p)} não tem a seção '## Plano por dia'.")
        prox = next(
            (i for i in range(plano + 1, len(linhas)) if linhas[i].startswith("## ")), len(linhas)
        )
        pos = prox
        for i in range(plano + 1, prox):
            m = re.match(r"### \S+ (\d{2})/(\d{2})", linhas[i])
            if m and (int(m.group(2)), int(m.group(1))) > (d.month, d.day):
                pos = i
                break
        novo = [f"### {DIAS_PT[d.weekday()]} {alvo}", f"- [ ] {tarefa.strip()}", ""]
        linhas[pos:pos] = novo
    else:
        fim = next(
            (i for i in range(idx + 1, len(linhas)) if linhas[i].startswith("#")), len(linhas)
        )
        vazio = next((i for i in range(idx + 1, fim) if linhas[i].strip() == "- [ ]"), None)
        if vazio is not None:
            linhas[vazio] = f"- [ ] {tarefa.strip()}"
        else:
            ultimo = max(
                (i for i in range(idx + 1, fim) if linhas[i].startswith("- ")), default=idx
            )
            linhas.insert(ultimo + 1, f"- [ ] {tarefa.strip()}")
    _gravar(p, "\n".join(linhas), nl)
    return f"Tarefa adicionada em {_rel(p)} ({DIAS_PT[d.weekday()]} {alvo}): {tarefa.strip()}"


@mcp.tool()
def marcar_tarefa_semana(trecho: str, data: str = "", feita: bool = True) -> str:
    """Marca (ou desmarca) como feita a tarefa da semana que contém 'trecho'."""
    seg = _segunda(_data(data))
    p = _caminho_seguro(f"{PASTA_SEMANAS}/{seg.isoformat()}.md")
    if not p.is_file():
        raise ErroOpenBot(f"Não existe {_rel(p)}.")
    texto, nl = _ler(p)
    linhas = texto.split("\n")
    padrao = "- [ ] " if feita else "- [x] "
    achados = [
        i for i, l in enumerate(linhas)
        if l.lower().startswith(padrao) and trecho.lower() in l.lower()
    ]
    if len(achados) != 1:
        raise ErroOpenBot(f"Encontradas {len(achados)} tarefas com {trecho!r}; é preciso exatamente 1.")
    i = achados[0]
    linhas[i] = ("- [x] " if feita else "- [ ] ") + linhas[i][6:]
    _gravar(p, "\n".join(linhas), nl)
    return f"Atualizado: {linhas[i]}"


@mcp.tool()
def criar_nota(assunto: str, conteudo: str, data: str = "") -> str:
    """Cria notas/AAAA-MM-DD-assunto.md com título e conteúdo em Markdown."""
    d = _data(data)
    p = _caminho_seguro(f"{PASTA_NOTAS}/{d.isoformat()}-{_slug(assunto)}.md")
    if p.exists():
        raise ErroOpenBot(f"Já existe {_rel(p)}. Use escrever_arquivo com sobrescrever=True ou outro assunto.")
    _gravar(p, f"# {assunto.strip()} — {d:%d/%m/%Y}\n\n{conteudo.strip()}\n")
    return f"Nota criada: {_rel(p)}"


@mcp.tool()
def escrever_arquivo(caminho: str, conteudo: str, sobrescrever: bool = False) -> str:
    """Grava um arquivo .md/.txt dentro do repositório. Não sobrescreve sem sobrescrever=True."""
    p = _caminho_seguro(caminho)
    if p.suffix.lower() not in EXTENSOES_PERMITIDAS:
        raise ErroOpenBot(f"Somente {', '.join(sorted(EXTENSOES_PERMITIDAS))} são permitidos.")
    if p.exists() and not sobrescrever:
        raise ErroOpenBot(f"{_rel(p)} já existe. Passe sobrescrever=True para substituir.")
    nl = _ler(p)[1] if p.exists() else "\n"
    _gravar(p, conteudo.replace("\r\n", "\n"), nl)
    return f"Gravado: {_rel(p)} ({len(conteudo)} caracteres)"


# --------------------------------------------------------------------------
# Ferramentas MCP — git
# --------------------------------------------------------------------------
@mcp.tool()
def git_status() -> str:
    """Mostra o estado do git (branch, alterações locais e diferença em relação ao remoto)."""
    try:
        _git("fetch", "--quiet")
    except ErroOpenBot:
        pass  # offline: mostra o estado local mesmo assim
    return _git("status", "-sb")


@mcp.tool()
def git_diff() -> str:
    """Mostra as alterações locais ainda não publicadas (inclui arquivos novos)."""
    _git("add", "-A", "--intent-to-add")
    diff = _git("diff", "--stat") + "\n\n" + _git("diff")
    return diff[:20000] if diff.strip() else "Sem alterações locais."


@mcp.tool()
def git_sincronizar() -> str:
    """Baixa as alterações do GitHub (git pull --rebase --autostash)."""
    return _git("pull", "--rebase", "--autostash") or "Atualizado."


@mcp.tool()
def git_publicar(mensagem: str) -> str:
    """Faz commit de todas as alterações com a mensagem informada e envia ao GitHub (pull --rebase + push)."""
    if not mensagem.strip():
        raise ErroOpenBot("Informe a mensagem do commit.")
    _git("add", "-A")
    if not _git("status", "--porcelain"):
        return "Nada a publicar: sem alterações locais."
    _git("commit", "-m", mensagem.strip())
    _git("pull", "--rebase", "--autostash")
    _git("push")
    return "Publicado:\n" + _git("log", "-1", "--format=%h %s")


if __name__ == "__main__":
    if not REPO.is_dir():
        print(f"[openbot] Repositório não encontrado: {REPO}", file=sys.stderr)
        sys.exit(1)
    mcp.run()  # transporte stdio
