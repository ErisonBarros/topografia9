# Orientações para Contribuição no Repositório e Integração com Gitbook

Este documento serve como um guia para contribuir com o material deste repositório e explica como ele se integra ao Gitbook.

## Estrutura do Repositório

O conteúdo principal do curso está localizado na pasta `guitbook/`. A estrutura básica é a seguinte:

*   **`guitbook/`**: Pasta raiz do conteúdo do Gitbook.
    *   **`README.md`**: Página inicial do Gitbook (Introdução).
    *   **`SUMMARY.md`**: Índice lateral do Gitbook. Define a estrutura de navegação.
    *   **`introducao/`**: Pasta contendo arquivos relacionados à introdução (ex: Plano de Ensino).
    *   **`aulas/`**: Pasta contendo os arquivos das aulas.
    *   **`referencias-bibliograficas.md`**: Arquivo com as referências.

## Como Contribuir

Para adicionar ou modificar conteúdo, siga os passos abaixo:

### 1. Criar ou Editar Arquivos Markdown

Todo o conteúdo é escrito em **Markdown (.md)**.

*   **Para editar uma página existente**: Navegue até o arquivo desejado dentro da pasta `guitbook/` e faça as alterações.
*   **Para criar uma nova página**:
    1.  Crie um novo arquivo com a extensão `.md` na pasta apropriada (por exemplo, `guitbook/aulas/aula-4.md`).
    2.  Escreva o conteúdo utilizando a sintaxe Markdown.

### 2. Atualizar o Índice (SUMMARY.md)

Se você criou um novo arquivo, é **obrigatório** adicioná-lo ao `guitbook/SUMMARY.md` para que ele apareça na navegação do Gitbook.

Abra o arquivo `guitbook/SUMMARY.md` e adicione uma nova linha seguindo o padrão:

```markdown
* [Título da Página](caminho/para/o/arquivo.md)
```

Exemplo para adicionar uma nova aula:

```markdown
* [🚩 Aula 4](aulas/aula-4.md)
```

### 3. Commit e Push

Após realizar as alterações:

1.  Adicione os arquivos modificados ao Git:
    ```bash
    git add .
    ```
2.  Faça o commit com uma mensagem descritiva:
    ```bash
    git commit -m "Adiciona conteúdo da Aula 4"
    ```
3.  Envie as alterações para o repositório remoto:
    ```bash
    git push origin main
    ```

## Integração com Gitbook

Este repositório pode ser vinculado ao Gitbook para publicação automática.

### Como Vincular

1.  Acesse sua conta no [Gitbook](https://www.gitbook.com/).
2.  Crie um novo **Space** ou selecione um existente.
3.  Vá em **Integrations** (Integrações) > **GitHub**.
4.  Selecione este repositório (`topografia9`).
5.  Configure a sincronização:
    *   **Branch**: Escolha a branch principal (geralmente `main` ou `master`).
    *   **Content Directory**: Defina como `guitbook` (pois é onde o `SUMMARY.md` e o conteúdo estão).

### Sincronização Automática

Uma vez vinculado, qualquer `git push` para a branch configurada atualizará automaticamente o conteúdo no Gitbook.
