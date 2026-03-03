## 1. Inicialização do projeto

```bash
uv init
```

## 2. Instalar pacotes

```Bash
uv add numpy
```

## 3. Remover pacotes desnecessários

```bash
uv remove tensorflow
```


Segue a organização dos comandos que você descreveu, com uma explicação clara de cada etapa 👇

---

## 🚀 Inicialização do Projeto

```bash
uv init
```

Esse comando:

* Cria um novo projeto Python
* Gera automaticamente:
  * `pyproject.toml`
  * Ambiente virtual
  * Estrutura básica do projeto

O `uv` já prepara o ambiente isolado (sem precisar usar `venv` manualmente).

---

## 📦 Instalar Pacotes

```bash
uv add numpy
```

Esse comando:

* Instala o pacote **numpy**
* Atualiza automaticamente o `pyproject.toml`
* Atualiza o arquivo de lock (`uv.lock`)
* Instala a dependência no ambiente virtual

Se quiser instalar múltiplos pacotes:

```bash
uv add pandas matplotlib
```

---

## 🗑️ Remover Pacotes Desnecessários

```bash
uv remove tensorflow
```

Esse comando:

* Remove o pacote do projeto
* Atualiza o `pyproject.toml`
* Atualiza o `uv.lock`
* Remove do ambiente virtual

---

## 📌 Fluxo Completo de Uso

```bash
uv init
uv add numpy
uv add pandas
uv remove tensorflow
```

---

Se você quiser, posso preparar um **guia completo em Markdown para GitHub** sobre uso do `uv` (instalação, ambientes, boas práticas e comparação com pip/poetry).
