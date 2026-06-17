# Lógica da Ponderação — Avaliação Prática de Topografia

---

## 1. Princípio Geral

A nota final de cada aluno é composta pela **soma ponderada de 4 critérios**, cada um com peso proporcional à sua relevância técnica na atividade. A referência de excelência é o aluno **Referencia (ID 8)**, que obtém pontuação máxima em todos os critérios.

```
Nota Final = C1 + C2 + C3 + C4
```

Onde a soma máxima possível é **10,0 pts**.

---

## 2. Estrutura dos Critérios

| Código | Critério                        | Peso | Máx. (pts) |
|--------|---------------------------------|------|------------|
| C1     | Situação de Centragem           | 40%  | 4,80       |
| C2     | Tempo de Calagem/Centragem      | 35%  | 4,20       |
| C3     | Leitura Angular                 | 15%  | 1,80       |
| C4     | Tempo Geral                     | 10%  | 1,20       |

---

## 3. Fórmula de Cada Critério

---

### C1 — Situação de Centragem (40% → 4,80 pts)

Critério **binário**: avalia se o equipamento foi devidamente calado e centrado.

```
C1 = 4,80   se Situação = "OK"
C1 = 0,00   se Situação = "NÃO"
```

> **Justificativa:** a centragem correta é condição fundamental para qualquer medição topográfica válida. Peso máximo por ser critério eliminatório qualitativo.

---

### C2 — Tempo de Calagem/Centragem (35% → 4,20 pts)

Critério **contínuo decrescente**: quanto menor o tempo, maior a nota. A escala vai de 0 a 720 segundos (12 min) como limite máximo tolerável.

```
C2 = max(0,  (1 − t_cal / 720)  × 4,20)
```

Onde `t_cal` = tempo de calagem em segundos.

| Tempo             | Cálculo                      | Nota C2  |
|-------------------|------------------------------|----------|
| 0 seg (instantâneo) | (1 − 0/720) × 4,20         | **4,20** |
| 360 seg (6 min — ref.) | (1 − 360/720) × 4,20   | **2,10** |
| 520 seg (8'40")   | (1 − 520/720) × 4,20         | **1,17** |
| 720 seg (12 min)  | (1 − 720/720) × 4,20         | **0,00** |

> **Justificativa:** agilidade na calagem e centragem reflete domínio do equipamento. Acima de 12 min considera-se desempenho insuficiente.

---

### C3 — Leitura Angular (15% → 1,80 pts)

Critério **contínuo decrescente**: penaliza o desvio angular em segundos de arco em relação à referência `52°50'51"`. Tolerância máxima: **1.200 segundos de arco (20')**.

**Passo 1 — Converter leitura para segundos de arco totais:**

```
seg_arco = graus × 3600 + minutos × 60 + segundos
```

**Passo 2 — Calcular desvio absoluto:**

```
desvio = |seg_arco_aluno − seg_arco_referencia|
```

**Passo 3 — Calcular nota:**

```
C3 = max(0,  (1 − desvio / 1200)  × 1,80)
```

| Desvio        | Situação                   | Nota C3  |
|---------------|----------------------------|----------|
| 0"            | Leitura idêntica à ref.    | **1,80** |
| 600" (10')    | Desvio moderado            | **0,90** |
| 1.200" (20')  | Limite tolerável           | **0,00** |
| > 1.200"      | Erro grosseiro             | **0,00** |

> **Justificativa:** peso reduzido (15%) pois a turma apresentou erro sistemático coletivo (~900"–1000"), sugerindo condição operacional comum a todos. Erros grosseiros (> 20') são zerados.

---

### C4 — Tempo Geral (10% → 1,20 pts)

Critério **contínuo de proximidade**: avalia quão próximo o aluno ficou do tempo de referência de **12:00:00 (43.200 seg)**. Penaliza desvios para cima ou para baixo.

```
C4 = max(0,  (1 − |t_geral − 43200| / 43200)  × 1,20)
```

Onde `t_geral` = tempo geral em segundos.

| Tempo Geral  | Desvio (seg) | Nota C4  |
|--------------|--------------|----------|
| 12:00:00     | 0            | **1,20** |
| 09:00:00     | 10.800       | **0,90** |
| 06:00:00     | 21.600       | **0,60** |
| 00:05:51     | 42.849       | **0,01** |
| 00:00:00     | 43.200       | **0,00** |

> **Justificativa:** peso mínimo (10%) pois o tempo geral depende de fatores externos à execução técnica individual. A referência de 12h representa o tempo padrão da atividade.

---

## 4. Fluxo de Cálculo

```
┌─────────────────────────────────────────────────┐
│              DADOS DE ENTRADA                   │
│  Situação │ T. Calagem │ Leitura │ T. Geral     │
└────────────────────┬────────────────────────────┘
                     │
         ┌───────────▼───────────┐
         │   C1: Centragem OK?   │
         │   OK  → 4,80 pts      │
         │   NÃO → 0,00 pts      │
         └───────────┬───────────┘
                     │
         ┌───────────▼───────────┐
         │   C2: Tempo Calagem   │
         │  (1 − t/720) × 4,20  │
         └───────────┬───────────┘
                     │
         ┌───────────▼───────────┐
         │   C3: Leitura Angular │
         │ (1 − dev/1200) × 1,80 │
         └───────────┬───────────┘
                     │
         ┌───────────▼───────────┐
         │   C4: Tempo Geral     │
         │ (1−|t−43200|/43200)   │
         │        × 1,20         │
         └───────────┬───────────┘
                     │
         ┌───────────▼───────────┐
         │   NOTA FINAL          │
         │  C1 + C2 + C3 + C4   │
         │   (máx. = 10,0 pts)   │
         └───────────────────────┘
```

---

## 5. Casos Especiais

| Situação                         | Tratamento                                                              |
|----------------------------------|-------------------------------------------------------------------------|
| Centragem "NÃO"                  | C1 = 0,00 — zerando 40% da nota                                         |
| Desvio angular > 1.200"          | C3 = 0,00 — erro grosseiro                                              |
| Tempo calagem > 720 seg          | C2 = 0,00 — limite máximo excedido                                      |
| Reclassificação docente          | Permitida via decisão justificada (ex.: Romeu ID 7)                     |

---

## 6. Exemplo Aplicado — Bianca

```
C1 = OK  → 4,80 pts

C2 = (1 − 345/720) × 4,20
   = (1 − 0,479) × 4,20
   = 0,521 × 4,20
   = 2,19 pts

C3 = (1 − 902/1200) × 1,80
   = (1 − 0,752) × 1,80
   = 0,248 × 1,80
   = 0,45 pts

C4 = (1 − |28800 − 43200|/43200) × 1,20
   = (1 − 14400/43200) × 1,20
   = (1 − 0,333) × 1,20
   = 0,667 × 1,20
   = 0,80 pts

NOTA FINAL = 4,80 + 2,19 + 0,45 + 0,80 = 8,24 ≈ 8,2
```

---

## 7. Resumo das Fórmulas

| Critério       | Fórmula                                              | Máx.   |
|----------------|------------------------------------------------------|--------|
| C1 Centragem   | OK → 4,80 \| NÃO → 0,00                             | 4,80   |
| C2 T. Calagem  | max(0, (1 − t_cal / 720) × 4,20)                    | 4,20   |
| C3 Angular     | max(0, (1 − desvio / 1200) × 1,80)                  | 1,80   |
| C4 T. Geral    | max(0, (1 − \|t_geral − 43200\| / 43200) × 1,20)    | 1,20   |
| **Nota Final** | **C1 + C2 + C3 + C4**                               | **10,0** |

---

*Documento gerado — Avaliação Prática de Topografia — Junho/2026*
