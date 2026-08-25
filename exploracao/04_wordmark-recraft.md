# Wordmark "téra" — Recraft V4.1 vetor (23.08.2026)

16 SVGs nativos, preto e branco. Arquivos em `vetor/recraft/`, folha de contato em `vetor/recraft/board_recraft.png`.
Ao contrário do Midjourney, **a palavra sai escrita certa, com acento** — é a diferença entre uma ferramenta que entende tipografia e uma que desenha pixels.

---

## Custo — o que aprendi apanhando

| Config | Créditos por job (4 imagens) |
|---|---|
| `z_image` | **0,15** — raster, sem vetor |
| Recraft vetor 1k, batch 1 | 2,5 |
| Recraft standard 1k, batch 4 | 5 |
| `gpt_image_2` | 7 |
| **Recraft vetor 1k, batch 4** | **10** ← o certo |
| Recraft vetor 2k, batch 4 | 40 ← o que rodei por engano |

**Em modo vetor a saída é SVG escalável — `--resolution 2k` só encarece o preview e não melhora o vetor.** Rodei 4 jobs em 2k e gastei 160 créditos onde 40 resolviam. Daqui pra frente: **1k sempre** para vetor.

Com 1545 créditos restantes: ~154 levas de 4 vetores, ou ~10.000 imagens no z_image.
E o mais barato de todos continua sendo SVG escrito em código: **zero**.

---

## As quatro famílias

**A · grade modular** — letras travadas em módulo quadrado.
As mais interessantes. **A_grid_2** e **A_grid_4** têm peso, geometria e um acento anguloso próprio. Coerentes com a régua de 0,48 m do estudo do t.

**B · peso de venue** — grotesca pesada.
Competente e genérica: parecem Druk e derivados, qualquer marca poderia usar. Pior: em `B_venue_1` e `B_venue_4` o acento virou **macron** (`tēra`), não agudo. Descartáveis como estão.

**C · arcos monolineares** — o DNA do desenho do cliente.
Elegantes, mas **finas demais**. Lêem marca de beleza/moda, não casa de espetáculo — brigam frontalmente com o reposicionamento para entretenimento. `C_arcos_2` é a mais bonita e ainda assim leve demais.

**D · stencil modular** — letras em módulos soltos.
**D_stencil_3** e **D_stencil_4** são fortes: chunky, modulares, com o acento no mesmo módulo. É a família que mais conversa com a chapa gradeada de 1×1 m. Cuidado com `D_stencil_2`, que trocou o `a` por `ä`.

---

## Curadoria

Quatro para levar adiante: **A_grid_2 · A_grid_4 · D_stencil_3 · D_stencil_4**.

O que elas têm em comum, e que B e C não têm: **são construídas em módulo** — a mesma lógica do t que fechamos em `03_estudo-vetor-t.md` e a mesma lógica do lugar. Não é coincidência estética, é a régua do briefing aparecendo na letra.

## Ressalvas antes de qualquer entusiasmo

- **Nenhum destes é o logo final.** São referência de forma. O desenho definitivo se constrói em Bézier, com kerning óptico por par e o acento resolvido dentro do sistema — inclusive porque imagem gerada por IA não tem proteção autoral.
- **Conferir o acento em cada um**: vários saíram macron em vez de agudo. Em português isso não é detalhe.
- **A família C responde ao briefing antigo**, de instituição cultural. Se "entretenimento" se confirmar por escrito, ela sai.

## Próximo

1. Rodar mais variações de A e D **em 1k** (10 créditos a leva), agora que o território está achado.
2. Testar os quatro contra o logo da Mata e em redução.
3. Fechar o escolhido à mão, no módulo de 0,48 m, junto com o monograma t.
