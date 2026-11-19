# Agent_Claude_UFPE

Central de pendências, tarefas e planejamento semanal das atividades na UFPE.

## Estrutura de pastas

```
Agent_Claude_UFPE/
├── README.md              # este arquivo: visão geral e estrutura
├── LICENSE                # licença MIT
├── pendencias.md          # lista mestra de pendências por prioridade
├── semanas/               # um plano por semana
│   └── 2026-11-16.md      # semana de 16/11 a 22/11/2026
└── notas/                 # notas soltas (reuniões, avisos, ideias)
    └── README.md          # como nomear e usar as notas
```

## Como usar cada parte

| Caminho | Para que serve | Padrão de nome |
|---|---|---|
| `pendencias.md` | Todas as pendências em aberto, separadas em 🔴 urgente, 🟡 importante, 🟢 pode esperar e ✅ concluído | arquivo único |
| `semanas/` | Plano da semana: compromissos fixos, prazos e checklist por dia | `AAAA-MM-DD.md` (data da segunda-feira) |
| `notas/` | Registros soltos; o que virar tarefa vai para `pendencias.md` | `AAAA-MM-DD-assunto.md` |

## Fluxo

1. Anotar tudo o que surgir em `notas/` ou direto em `pendencias.md`.
2. Classificar cada pendência por prioridade, com prazo e próximo passo.
3. No início da semana, criar o arquivo em `semanas/` e distribuir as tarefas pelos dias.
4. Ao concluir, mover o item para ✅ Concluído em `pendencias.md`.
