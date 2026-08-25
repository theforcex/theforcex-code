# Leitura da primeira rodada — Midjourney (22.08.2026)

12 grades geradas (8 da primeira leva + 2 upscales + 2 da segunda leva corrigida).
Imagens em `midjourney/`. Todos os prompts em `01_prompts-logo.md`.

---

## O achado estrutural

Rodando a família B (o cubo de 4 telas), apareceu uma coisa que não veio de referência nenhuma — veio da **spec do cliente**:

> A sala tem **4 telas: fundo, duas laterais e teto. Não tem piso.**
> Desdobre essa caixa num plano e a planificação é um **T**.
> **T é a inicial de Téra.** E as paredes são revestidas por módulos quadrados de **1×1 m** — então esse T se constrói em módulos quadrados.

**O monograma da Téra é a planta da sala desdobrada, construída no módulo de um metro.**

Não é metáfora e não é referência: é a geometria literal do lugar, e sai direto de dois fatos que o cliente respondeu por escrito em 21.08. Nenhum concorrente pode ter isso, porque depende dessa sala.

A prova visual está em `midjourney/N4_t-modular.png` — os quadros inferiores mostram o T em módulos quadrados lendo instantaneamente como letra, com vãos entre os módulos. Vetoriza trivialmente (são retângulos).

---

## Curadoria — o que prestou

| # | Direção | Veredicto |
|---|---|---|
| **N4** | **t modular em grade** | **Vencedor.** Quadros inferiores: T em módulos quadrados com vãos. Lê como letra, é industrial, é a grade do cliente, e é vetor puro |
| **C11** | Monólito de terra | **Forte.** O quadro inferior-esquerdo (upscale em `UP_C11_monolito-sala.png`) tem o pilar escavado no centro de uma sala de concreto em perspectiva de um ponto — matéria + cubo no mesmo quadro. Serve de imagem-chave, não de logo |
| **A** | Grade modular abstrata | **Promissor com ressalva.** Marcas modulares reais, mas lêem QR code / escritório de arquitetura. A correção veio no N4: virar letra resolve |

## O que não prestou (e por quê — isso vale tanto quanto)

| # | Direção | O que aconteceu |
|---|---|---|
| **E18** | Acento isolado | A barra oblíqua sozinha vira **ícone de editar/lápis**. Genérica demais. **Achado negativo útil: o acento não carrega a marca sozinho** — ele é detalhe do wordmark, não símbolo |
| **C9** | Letra escavada | Vira *grunge* na hora — lê banda de metal, não casa de espetáculo. E textura rachada não vetoriza |
| **B5** | Sala em perspectiva | Limpo, mas lê túnel/caixa e beira ícone de monitor. É símbolo, não wordmark |
| **B7 / N3** | Planificação | MJ leu "cross shaped net" como **ornamento têxtil andino**; na segunda tentativa foi para desenho isométrico. A ideia estava certa (ver achado acima), a execução não sai no MJ |
| **D12** | Marquise | MJ produziu fotos de **marquises americanas nostálgicas**. Aviso de registro: "marquise" puxa cinema retrô — exatamente o lugar errado |
| **D15** | Letreiro na fachada | Derivou para **restaurante/hotel industrial**. Atmosfera aproveitável, estudo de logo não |

---

## O que isso ensina sobre a ferramenta

Confirmado o que estava previsto em `01_prompts-logo.md`: **Midjourney não faz wordmark.** Errou o texto em 100% dos casos e ignorou "flat vector logo" sempre que o prompt tinha substantivo fotográfico (marquise, fachada, letreiro).

Onde ele serve: **matéria, atmosfera e marca abstrata modular** — C11 e N4 provam isso.
Onde não serve: qualquer coisa que precise da palavra "téra" legível.

Correções de prompt que funcionaram:
- Tirar todo substantivo fotográfico do prompt de logo.
- Pedir **uma letra só** em vez da palavra (o "t" saiu limpo; "téra" nunca sai).
- Usar `--no` com os desvios observados (`ornament pattern symmetry cross`, `serif`, `photo`).

---

## Próximo passo

1. **Fechar o t modular no vetor**, à mão, a partir da geometria real: 4 faces da sala desdobradas, módulo de 1 m, vãos entre painéis. Não é traçar por cima do MJ — é redesenhar a partir da planta.
2. **Testar a régua**: o t modular funciona a 16 px? E em fachada? E ao lado do logo da Mata?
3. **O wordmark "téra"** precisa de ferramenta que escreva texto — Recraft V3/V4 ou GPT Image 2. Midjourney está descartado para essa etapa.
4. **Pedir a planta ao cliente** (já está na lista do `LEIA-ME.md`): sem ela, o módulo de 1 m e a proporção das 4 faces continuam aproximados.
