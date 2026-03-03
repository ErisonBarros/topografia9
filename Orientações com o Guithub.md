Para  **ver todas as branches no Git** , você pode usar os comandos abaixo 👇

---

# ✅ 1️⃣ Ver branches locais

```bash
git branch
```

✔ Mostra apenas as branches que existem no seu computador.
✔ A branch atual aparece com `*`

---

# 🌎 2️⃣ Ver branches remotas (do GitHub)

```bash
git branch -r
```

Mostra algo como:

```
origin/main
origin/dev
origin/aula-topografia
```

---

# 🌍 3️⃣ Ver TODAS (locais + remotas)

```bash
git branch -a
```

Esse é o comando mais completo.

---

# 🔄 Se não aparecer alguma branch remota

Atualize antes:

```bash
git fetch --all
```

Depois rode:

```bash
git branch -a
```

---

# 🎯 Dica extra (visual mais organizado)

```bash
git branch -vv
```

Mostra:

* Qual branch está ativa
* Qual branch remota está vinculada
* Último commit

---

# 🧠 Resumo rápido

```bash
git branch      # locais
git branch -r   # remotas
git branch -a   # todas
```

---
