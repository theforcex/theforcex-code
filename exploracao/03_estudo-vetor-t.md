# Estudo vetorial — do net da sala ao monograma

Vetor de verdade (SVG paramétrico, preto e branco), gerado por
`scripts/net_to_t.py`. Nada de IA aqui: é a geometria da sala desenhada em código.
Regenerar: `python exploracao/scripts/net_to_t.py`

---

## A régua: o módulo de 0,48 m

As três medidas que o cliente deu (21.08) têm **um único divisor inteiro comum**:

| Face | Metros | Em módulos de 0,48 m |
|---|---|---|
| Fundo | 15,36 × 8,16 | **32 × 17** |
| Teto | 15,36 × 10,08 | **32 × 21** |
| Lateral | 10,08 × 8,16 | **21 × 17** |

**0,48 m** não é escolha estética: é a altura do gabinete de LED (640 × 480 mm) e três módulos de 160 mm. A sala inteira é múltipla dela. O sistema herda essa régua em vez de inventar uma.

## A planificação

Com o **teto no centro** da travessa e o fundo pendurado abaixo, o net das 4 faces (sem piso) fecha em **66 × 38 módulos** e a silhueta é um **T**.

---

## Os seis estudos

| # | Arquivo | Leitura |
|---|---|---|
| 01 | `tera_01_net_exato.svg` | O net com a malha. **Documento**, não marca — serve para provar a origem |
| 02 | `tera_02_T_solido.svg` | O T literal, faces cheias e frestas. Honesto, mas **haste com 48% da travessa**: pesado, lê planta baixa |
| 03 | `tera_03_T_modulos.svg` | O T em módulos discretos. Ganha textura, mas fica **denso e lê QR code** |
| 04 | `tera_04_T_otico.svg` | Haste reduzida a 70% do teto por correção óptica. Equilibra — e **deixa de ser literal** |
| 05 | **`tera_05_t_minusculo.svg`** | **O mais forte.** t minúsculo no mesmo módulo: peso de venue, lê instantâneo, geometria honesta |
| 06 | `tera_06_t_modulos.svg` | O mesmo t em módulos discretos. Carrega a grade do cliente na letra |

Boards: `vetor/board_net_to_t.png` e `vetor/board_reducao.png`.

---

## O erro que apareceu no caminho (e a correção)

A primeira versão do t minúsculo era **simétrica** — haste central, travessa igual dos dois lados. Resultado: **crucifixo**. Não era sutil, era a leitura primária.

Três assimetrias resolveram, e viram regra do desenho:

1. **Travessa desigual** — avança mais à direita (9 un) do que à esquerda (4 un).
2. **Pé** — degrau à direita na base, a tradução geométrica da curva do t.
3. **Ascendente curta** — 10 un acima da travessa, nunca metade da altura.

Qualquer redesenho futuro que perca uma das três volta a ler cruz. Está no código.

## Redução

`board_reducao.png` — o t sobrevive a **16 px** em positivo e em negativo. Nenhum ajuste de peso necessário até lá.

Para o **T do net** (02/04) a regra é outra: abaixo de ~90 px as frestas fecham e ele vira mancha sólida. Se o T for usado, precisa de uma versão sem fresta para tamanhos pequenos.

---

## Onde isso ainda é aproximado

- As cotas de 15,36 / 10,08 / 8,16 vieram de um diagrama esquemático, e **qual cota é de qual face ainda não está confirmado** (ver `../briefing/02_respostas-cliente_21-08-2026.md`). Se a leitura mudar, o net muda de proporção — a lógica não.
- A **planta ainda não foi enviada**. Ela é o que fecha isso.

## Próximo

1. O **wordmark "téra"** completo — precisa de ferramenta que escreva texto (Recraft V4.1 em modo vetor, ou GPT Image 2). Depende do `higgsfield auth login`.
2. Testar o t contra o logo da Mata (teste da vizinhança) e em fachada.
3. Decidir entre **05 (t minúsculo)** e **02/04 (T do net)** — ou usar o T como símbolo institucional e o t como monograma de aplicação.
