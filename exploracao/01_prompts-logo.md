# Téra — 20 prompts para o wordmark

> Trabalho nosso, não é briefing. Base factual: `../briefing/`.
> Objetivo: chegar ao **logo vetorial**. Estes prompts servem à fase de ideação e à geração de SVG.

---

## Antes de rodar: três avisos que economizam horas

**1. IA erra texto — e "téra" tem acento.** Nenhum gerador escreve a palavra certa de forma confiável, e o acento agudo some ou vira mancha. Use os resultados como **estudo de forma e sistema**, não como letra final. Recraft V3/V4 é o menos ruim com texto curto; Midjourney é o pior. O desenho definitivo se fecha no vetor, à mão.

**2. Tool por etapa.**
- **Recraft V3/V4** → SVG nativo, é onde o logo vetorial nasce de verdade. Prompts A a F abaixo funcionam direto lá.
- **Midjourney** → exploração de território e atmosfera (bom para famílias C e D). MCP disponível nesta máquina: `mcp__midjourney__imagine`.
- **Vectorizer.ai** → só se o conceito vencedor nascer em raster.

**3. Referência de imagem melhora tudo.** Onde o prompt pedir, suba junto:
- `../briefing/midia/logo-cliente_wordmark.png` (o wordmark que o cliente já tem)
- `../briefing/midia/sala_grades-trama.png` (a chapa gradeada)
- `../briefing/midia/entrada_pilares-de-terra.png` (os pilares escavados)
- `../briefing/midia/sala_medidas-telas.png` (o cubo de 4 telas)

---

## Bloco de restrições — cole no fim de TODO prompt de vetor

```
Flat vector logo. Pure black on white, one single color only. No gradients, no shadows,
no textures, no glow, no bevel, no 3D, no photographic elements, no background scenery,
no mockup, no frame. Centered composition, generous margins, minimum anchor points,
must stay legible at 16 px.
```

Sem isso, sai logo com degradê e sombra — inútil para vetor.

---

## Fatos que ancoram os prompts

| Fato do cliente | Onde entra |
|---|---|
| Chapas gradeadas **1×1 m** revestindo concreto aparente | Família A |
| **4 telas**: fundo, 2 laterais, teto (sem piso). Fundo **15,36 × 8,16 m** = ratio **32:17** | Família B |
| **Pilares de terra** do Matarazzo, escavados à mão | Família C |
| **"Mais entretenimento"** (Ciao, 22.08) + programação: shows, festas, corporativo | Família D |
| Acento integrado ao desenho do wordmark do cliente | Família E |
| Wordmark existente: minúsculas geométricas por arcos | Família F |

---

# FAMÍLIA A — A GRADE (4 prompts)
*A chapa gradeada de 1×1 m como lógica de construção da letra.*

### A1 · Grade construtiva
```
Bold lowercase wordmark "téra". Typographic logo constructed strictly on a visible square
grid module: every stem, terminal and curve snaps to the grid. Stencil logic, strokes
separated by thin square gaps like a perforated metal plate. The acute accent is exactly
one grid module. Industrial, architectural, confident.
[+ bloco de restrições]
```

### A2 · A letra é o furo
```
Lowercase wordmark "téra" cut as negative space out of a solid black rectangular field.
The letters are the voids, the plate is the mark. Orthogonal geometry, square counters,
thick remaining material. Reads as a punched steel panel.
[+ bloco de restrições]
```

### A3 · Malha como contraforma
```
Lowercase logotype "téra" where the letters emerge from a dense uniform lattice of thin
square cells. Letterforms defined only by removing cells from the mesh, no outlines drawn.
High contrast, mechanical precision, no perspective.
[+ bloco de restrições]
```

### A4 · Módulo único
```
Monolinear lowercase wordmark "téra" built entirely from one repeated square module and
its quarter-circle variant. Visible modular seams. Rational, systematic, buildable.
Accent rendered as one rotated module.
[+ bloco de restrições]
```

---

# FAMÍLIA B — O CUBO DE QUATRO TELAS (4 prompts)
*A sala: fundo, duas laterais, teto. Ratio da tela de fundo = 32:17.*

### B5 · A sala como moldura
```
Minimal geometric logo mark: a one-point perspective interior formed by exactly four
planes — back wall, two side walls, ceiling — with an open floor and open front. Pure
line construction, all edges converging to a single vanishing point. Beneath it, a small
bold lowercase wordmark "téra".
[+ bloco de restrições]
```

### B6 · Proporção da tela
```
Lowercase wordmark "téra" locked inside a horizontal rectangle of ratio 32:17, letters
justified edge to edge, filling the full width and height of the frame. The rectangle is
part of the mark. Extremely bold, tight fit, architectural.
[+ bloco de restrições]
```

### B7 · Planificação
```
Abstract geometric logo: four rectangles unfolded flat into a cross-shaped net — one large
central rectangle with three rectangles attached on top, left and right, bottom edge open.
Clean flat construction, equal stroke weight, symmetrical. Paired with a small lowercase
wordmark "téra".
[+ bloco de restrições]
```

### B8 · Letra-interior
```
Lowercase logotype "téra" where the counters of the letters are drawn in one-point
perspective, as if each closed shape were a small room seen from inside. Outer silhouette
stays flat and orthogonal. Precise, uncanny, architectural.
[+ bloco de restrições]
```

---

# FAMÍLIA C — TERRA ESCAVADA (3 prompts)
*Os pilares originais do Matarazzo, escavados à mão. Matéria, não abstração.*

### C9 · Escavado
```
Lowercase wordmark "téra" whose letterforms look excavated rather than drawn: rough
chiselled contours, irregular hand-dug edges, slight erosion, but a rigorous geometric
skeleton underneath. Solid black, high contrast, no outline.
[+ bloco de restrições]
```

### C10 · Estratos
```
Lowercase logotype "téra" constructed from stacked horizontal strata of varying thickness,
like geological layers or rammed earth. The layers build the letters; gaps between strata
read as sediment lines. Flat, single color.
[+ bloco de restrições]
```

### C11 · Monólito (Midjourney)
```
A single monolithic earth column standing in a dark underground foyer, raw excavated
texture, hand-dug surface, warm low grazing light, exposed concrete beyond, no people,
no text, documentary photography, medium format --ar 32:17 --style raw --stylize 150
```
*Referência de matéria para a família C. Suba `entrada_pilares-de-terra.png` como `--sref`.*

---

# FAMÍLIA D — VENUE / ENTRETENIMENTO (4 prompts)
*O eixo novo: casa de espetáculo, não museu. Precisa de presença de fachada e cartaz.*

### D12 · Marquise
```
Ultra-bold lowercase wordmark "téra" with the presence of a theatre marquee sign: heavy
weight, tight spacing, strong horizontal lock-up, designed to be read across a street.
Confident and loud without being novelty. Flat single color.
[+ bloco de restrições]
```

### D13 · Carimbo de ingresso
```
Compact lowercase wordmark "téra" designed as a stamp: enclosed in a simple geometric
container, very high contrast, thick strokes, survives ink bleed and small reproduction.
Reads perfectly at 12 px and at 12 meters.
[+ bloco de restrições]
```

### D14 · Cartaz compartilhado
```
Bold lowercase wordmark "téra" designed to sit above an artist name on a concert poster:
strong enough to own the top of the composition, neutral enough not to fight a headliner.
Wide horizontal proportion, generous side bearings, no ornament.
[+ bloco de restrições]
```

### D15 · Letreiro dimensional (Midjourney)
```
Large physical sign spelling a short lowercase word, mounted on raw exposed concrete wall
clad with 1x1 meter industrial grating panels, underground venue entrance, warm amber
grazing light from below, night, no people, architectural photography --ar 32:17
--style raw --stylize 200
```
*Estudo de aplicação em fachada. Suba `sala_grades-trama.png` como `--sref`.*

---

# FAMÍLIA E — O ACENTO COMO ATIVO (3 prompts)
*O acento é o único elemento que só a Téra tem. Vale testar se ele carrega a marca sozinho.*

### E16 · Acento monumental
```
Lowercase wordmark "téra" where the acute accent over the é is deliberately oversized —
the largest element of the composition, dominating the letters below it. The accent is a
solid geometric bar, the wordmark is comparatively small and quiet. Bold, asymmetric,
memorable.
[+ bloco de restrições]
```

### E17 · Acento como plano
```
Lowercase wordmark "téra" where the acute accent is not a stroke but a small rectangle
seen in oblique perspective — a tilted plane floating above the é. Everything else is
strictly flat and orthogonal. The single perspective element is the signature.
[+ bloco de restrições]
```

### E18 · O acento isolado
```
Minimal abstract logo symbol: a single bold oblique bar, geometrically precise, designed
to work as a standalone brand mark, app icon and stamp — derived from an acute accent.
No letters. Balanced in a square, strong silhouette, instantly recognizable.
[+ bloco de restrições]
```

---

# FAMÍLIA F — EVOLUÇÃO DO DESENHO DO CLIENTE (2 prompts)
*Suba `logo-cliente_wordmark.png` como referência junto com estes.*

### F19 · Refino dos arcos
```
Refine this lowercase geometric wordmark "téra": keep the arc-based construction and the
lowercase posture, but unify the stroke weight, regularize every arc to a consistent
radius, tighten optical spacing, and resolve the acute accent as part of the same
geometric system. Cleaner, more inevitable, same personality.
[+ bloco de restrições]
```

### F20 · Arcos com peso de venue
```
Take this arc-based lowercase wordmark "téra" and rebuild it much heavier: same circular
geometry and same lowercase logic, but thick confident strokes with tight counters, built
for signage and posters rather than for stationery. Bold, grounded, contemporary.
[+ bloco de restrições]
```

---

## Do raster ao vetor — o caminho

1. **Rodar** as 20 famílias, 4–8 gerações cada. Arquivar prompt + seed de tudo que prestar.
2. **Curar** para 3–5 direções. Critério: sobrevive em 16 px? divide cartaz com nome de artista? não parece logo de tech?
3. **Vetorizar** — Recraft já entrega SVG; se a direção vencedora vier do Midjourney, upscale com modelo **Digital Art** (nunca fotográfico, senão entra granulado) e passar no Vectorizer.ai.
4. **Redesenhar à mão.** Aqui o output da IA vira referência e nada mais: a letra final é construída em Bézier, com o mínimo de pontos de ancoragem, kerning óptico por par e o acento resolvido no mesmo sistema.
5. **Testar** em 16 px, em 90 px, em fachada, ao lado de um nome de artista e sobre a chapa gradeada.

> Nota de IP: imagem 100% gerada por IA não tem proteção autoral. O redesenho vetorial humano da etapa 4 não é só qualidade — é o que torna a marca protegível.
