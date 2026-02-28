# 🚩 Aula 1

---

# Topografia 9 - Revisão de Trigonometria

**Disciplina:** Topografia 9  
**Curso:** Engenharia Civil  
**Aula:** 1  
**Departamento:** Engenharia Cartográfica - UFPE  
**Professora:** Erison Rosa de O. Barros  
**Contato:** erison.barros@ufpe.br

---

## Objetivos da Aula

### Planejamento Didático

1. **Fundamentos Trigonométricos**
   - Revisar os princípios matemáticos da trigonometria essenciais e aplicados diretamente à prática topográfica.

2. **Medidas Lineares**
   - Relembrar conceitos de mensuração e a evolução histórica da definição padrão do metro (1791–1983).

3. **Sistemas Angulares**
   - Compreender as definições, diferenças e aplicações de Grau (sexagesimal), Grado (gon) e Radiano.

4. **Conversão de Unidades**
   - Dominar os métodos de conversão precisa entre os diferentes sistemas de medidas angulares utilizados em engenharia.

5. **Aplicações Práticas**
   - Aplicar funções trigonométricas na resolução de problemas reais de planimetria e altimetria.

---

## Medida Linear — O Metro

### Histórico e Definições

#### **1791 - Academia de Ciências de Paris**
- **Definição:** 1 metro = 1/10.000.000 do arco do meridiano terrestre (do Equador ao Polo Norte)
- Primeira tentativa de criar um padrão universal de comprimento baseado em medições geodésicas

#### **Séculos XIX–XX - Padrões Materiais**
- Utilização de barras-metro físicas (protótipos metálicos)
- Armazenamento em condições controladas para preservação do padrão

#### **1983 - Conferência Geral de Pesos e Medidas (CGPM)**
- **Definição atual:** 1 metro = distância percorrida pela luz no vácuo durante o intervalo de tempo de **1/299.792.458 segundos**
- Definição baseada em constantes físicas universais

#### **Implicações na Topografia**
- Calibração precisa de trenas e equipamentos EDM (Medidor Eletrônico de Distância)
- Estações totais e instrumentos de medição
- Correções necessárias: temperatura, pressão atmosférica
- Controle rigoroso de escala em levantamentos

---

## Medidas Angulares — Grau

### Sistema Sexagesimal

**Características principais:**

- **Volta completa:** 360°
- **Subdivisões:**
  - 1° (grau) = 60' (minutos)
  - 1' (minuto) = 60" (segundos)
- **Exemplo de notação:** 27° 15' 30"

**Aplicações:**
- Sistema de uso geral em navegação
- Cartografia tradicional
- Astronomia
- Engenharia civil

**Observação importante:**
- Sistema não decimal - requer atenção especial nas conversões entre minutos/segundos ↔ decimais

---

## Medidas Angulares — Grado

### Sistema Centesimal (gon)

**Características principais:**

- **Volta completa:** 400 gon (ou 400g)
- **Subdivisões decimais:**
  - 1g (grado) = 100c (centigrade)
  - 1c = 100cc (centi-centigrade)

**Conversão básica:**
- 1° = 10/9 gon ≈ 1,111 gon
- 1 gon = 0,9° = 54'

**Aplicações:**
- **Principal uso:** Topografia e instrumentação
- Teodolitos
- Estações totais
- Levantamentos geodésicos

**Vantagem:**
- Sistema totalmente decimal facilita cálculos de azimutes e deflexões
- Reduz erros em operações matemáticas

---

## Medidas Angulares — Radiano

### Unidade Padrão do Sistema Internacional (SI)

**Definição geométrica:**

```
θ (rad) = comprimento do arco / raio
```

- **1 radiano:** ângulo cujo arco tem comprimento igual ao raio

**Valores importantes:**
- **Volta completa:** 2π rad ≈ 6,2832 rad
- **Meia-volta:** π rad ≈ 3,1416 rad
- **Ângulo reto:** π/2 rad ≈ 1,5708 rad

**Conversões fundamentais:**
- 1° = π/180 rad ≈ 0,01745 rad
- 1 gon = π/200 rad ≈ 0,01571 rad
- 1 rad ≈ 57,2958° ≈ 63,662 gon

**Aplicações:**
- Fórmulas trigonométricas
- Cálculo numérico e análise matemática
- Programação e software de engenharia
- Modelagem computacional

---

## Comparativo de Sistemas Angulares

### Grau × Grado × Radiano

#### **Equivalências da Volta Completa**

| Sistema | Volta Completa |
|---------|----------------|
| Grau | 360° |
| Grado | 400 gon (g) |
| Radiano | 2π rad |

#### **Fatores de Conversão**

**Grado ↔ Grau:**
- g = (10/9) × °
- ° = 0,9 × g

**Radiano ↔ Grau:**
- rad = (π/180) × °
- ° = (180/π) × rad

**Radiano ↔ Grado:**
- rad = (π/200) × g
- g = (200/π) × rad

#### **Subdivisões**

| Sistema | Subdivisões |
|---------|-------------|
| Grau | °, ' (minutos), " (segundos) |
| Grado | g, c (centigrade), cc (centi-centigrade) |
| Radiano | Sistema decimal |

#### **Aplicações Práticas**

- **Campo:** Predominantemente gon (grado)
- **Relatórios:** ° (graus) ou gon, conforme convenção
- **Modelagem e Software:** rad (radianos)

#### **⚠️ Atenção**

- Sempre **padronizar a unidade** antes de realizar cálculos
- **Documentar conversões** em relatórios técnicos
- Verificar configuração de instrumentos antes de levantamentos

---

## Revisão Trigonométrica

### Fundamentos e Aplicações Topográficas

#### **Funções no Triângulo Retângulo**

```
sen θ = cateto oposto / hipotenusa

cos θ = cateto adjacente / hipotenusa

tan θ = cateto oposto / cateto adjacente = sen θ / cos θ
```

#### **Identidades Trigonométricas Fundamentais**

```
sen²θ + cos²θ = 1

tan θ = sen θ / cos θ

1 + tan²θ = sec²θ
```

#### **Círculo Trigonométrico**

- Ângulos expressos em radianos
- Análise dos 4 quadrantes
- Sinais das funções por quadrante:
  - **1º Quadrante:** sen(+), cos(+), tan(+)
  - **2º Quadrante:** sen(+), cos(-), tan(-)
  - **3º Quadrante:** sen(-), cos(-), tan(+)
  - **4º Quadrante:** sen(-), cos(+), tan(-)

#### **Aplicações Topográficas**

**Cálculo de Componentes de Coordenadas:**

```
ΔE = d × sen(A)    (Componente Este)

ΔN = d × cos(A)    (Componente Norte)
```

Onde:
- **d** = distância horizontal medida
- **A** = azimute medido a partir do Norte, sentido horário
- **ΔE** = variação na coordenada Este
- **ΔN** = variação na coordenada Norte

**Importante:**
- Garantir conversões angulares coerentes antes de computar
- Verificar sistema de referência (azimute vs. rumo)
- Atenção ao quadrante para sinais corretos

---

## Encerramento

### Obrigado pela Atenção!

Finalizamos aqui a introdução aos conceitos fundamentais de trigonometria aplicados à topografia.

**Próximos passos:**
- Revisaremos conversões práticas e exemplos aplicados na próxima aula
- Exercícios de fixação serão disponibilizados

**Dúvidas?**



**Documento gerado a partir da apresentação:** Topografia 9 - Aula 1  
**Data:** Fevereiro/2026  
**Formato:** Markdown

---


