# 📚 Aula: Gerenciador de Pacotes **uv** para Projetos Python

---

## 🎯 Objetivos da Aula

Ao final desta aula, você será capaz de:

* Entender o que é o **uv**
* Criar um projeto Python moderno
* Gerenciar dependências
* Trabalhar com ambientes virtuais
* Comparar `uv` com `pip` e `poetry`
* Aplicar boas práticas em projetos acadêmicos e técnicos

---

# 🚀 1. O que é o uv?

O **uv** é um gerenciador de pacotes e ambientes para Python, extremamente rápido, escrito em Rust, criado pela empresa Astral.

Ele substitui:

* `pip`
* `venv`
* `pip-tools`
* `poetry` (em muitos casos)

Com foco em:

* ⚡ Alta performance
* 🔒 Reprodutibilidade
* 🧩 Simplicidade
* 📦 Controle de dependências moderno

---

# 🏗️ 2. Estrutura de um Projeto com uv

## 📌 Inicializando um Projeto

```bash
uv init
```

Esse comando cria:

```
meu_projeto/
│
├── pyproject.toml
├── uv.lock
└── .venv/
```

### 🔎 Arquivos importantes

| Arquivo            | Função                       |
| ------------------ | ------------------------------ |
| `pyproject.toml` | Configuração e dependências |
| `uv.lock`        | Travamento das versões        |
| `.venv/`         | Ambiente virtual               |

---

# 📦 3. Instalando Dependências

## Instalar um pacote

```bash
uv add numpy
```

### O que acontece internamente?

* Atualiza `pyproject.toml`
* Atualiza `uv.lock`
* Instala no ambiente virtual

---

## Instalar múltiplos pacotes

```bash
uv add pandas matplotlib
```

---

## Instalar dependência de desenvolvimento

```bash
uv add pytest --dev
```

Ideal para:

* Testes
* Linters
* Ferramentas auxiliares

---

# 🗑️ 4. Removendo Pacotes

```bash
uv remove tensorflow
```

Remove:

* Do ambiente virtual
* Do `pyproject.toml`
* Do `uv.lock`

---

# 🔄 5. Executando Código

## Rodar script Python

```bash
uv run main.py
```

Não precisa ativar o ambiente manualmente.

---

# 🔒 6. Reprodutibilidade Científica

Para você que trabalha com:

* Geoprocessamento
* GNSS
* Topografia
* Modelagem Matemática

O `uv.lock` garante que:

* Todos usem as mesmas versões
* Resultados sejam reproduzíveis
* Projetos acadêmicos tenham rastreabilidade

Isso é essencial para:

* Trabalhos científicos
* Projetos institucionais
* Pesquisas em Engenharia Cartográfica

---

# ⚖️ 7. Comparação: uv vs pip vs poetry

| Recurso           | pip         | poetry      | uv          |
| ----------------- | ----------- | ----------- | ----------- |
| Ambiente virtual  | Manual      | Automático | Automático |
| Lock file         | Não nativo | Sim         | Sim         |
| Performance       | Média      | Boa         | Muito Alta  |
| Simplicidade      | Alta        | Média      | Alta        |
| Reprodutibilidade | Baixa       | Alta        | Alta        |

---

# 🧠 8. Exemplo Prático (Aplicação em Geoprocessamento)

Suponha um projeto de:

📍 Ajustamento de Observações
📍 Processamento GNSS
📍 Análise de Nuvem de Pontos

```bash
uv init
uv add numpy pandas matplotlib scipy
```

Depois:

```bash
uv run processamento.py
```

---

# 📂 9. Boas Práticas

✔ Sempre versionar `pyproject.toml`
✔ Sempre versionar `uv.lock`
✔ Nunca versionar `.venv/`
✔ Usar dependências `--dev` para testes
✔ Criar README explicando o ambiente

---

# 🏫 10. Atividade Proposta

1. Criar um projeto chamado `aula_uv`
2. Instalar:
   * numpy
   * pandas
3. Criar um script que:
   * Gere uma matriz 3x3
   * Calcule determinante
4. Executar com:

```bash
uv run script.py
```

---

---
