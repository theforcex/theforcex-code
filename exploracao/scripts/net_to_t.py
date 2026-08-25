# -*- coding: utf-8 -*-
"""
Téra — do net da sala ao monograma.

Geometria 100% derivada do briefing do cliente (21.08.2026):
  tela de fundo  15,36 x  8,16 m
  teto           15,36 x 10,08 m
  laterais       10,08 x  8,16 m   (profundidade x altura)
  4 telas, sem piso.

Módulo universal: 0,48 m — único divisor inteiro das tres medidas
(15,36/0,48=32 · 8,16/0,48=17 · 10,08/0,48=21). É tambem a altura do
gabinete de LED (640x480 mm) e 3 modulos de 160 mm.

Em unidades de 0,48 m:
  fundo   B = 32 x 17
  teto    C = 32 x 21
  lateral L = 17 x 21   (na planificação: altura vira largura)

Saidas: SVG vetorial (preto/branco) + board PNG de leitura.
"""
import os
from PIL import Image, ImageDraw

U = 0.48                      # metro por unidade
B_W, B_H = 32, 17             # fundo
C_W, C_H = 32, 21             # teto
S_W, S_H = 17, 21             # lateral na planificação

OUT = os.path.join(os.path.dirname(__file__), '..', 'vetor')
os.makedirs(OUT, exist_ok=True)

INK = '#111111'


# ---------------------------------------------------------------- helpers
def svg(w, h, body, pad=2):
    return (
        '<svg xmlns="http://www.w3.org/2000/svg" '
        'viewBox="{} {} {} {}" width="{}" height="{}">\n'
        '<rect x="{}" y="{}" width="{}" height="{}" fill="#ffffff"/>\n'
        '{}</svg>\n'
    ).format(-pad, -pad, w + 2 * pad, h + 2 * pad,
             (w + 2 * pad) * 10, (h + 2 * pad) * 10,
             -pad, -pad, w + 2 * pad, h + 2 * pad, body)


def rect(x, y, w, h, fill=INK):
    return '<rect x="{:.3f}" y="{:.3f}" width="{:.3f}" height="{:.3f}" fill="{}"/>\n'.format(
        x, y, w, h, fill)


def orect(x, y, w, h, sw=0.16):
    return ('<rect x="{:.3f}" y="{:.3f}" width="{:.3f}" height="{:.3f}" '
            'fill="none" stroke="{}" stroke-width="{}"/>\n').format(x, y, w, h, INK, sw)


def line(x1, y1, x2, y2, sw=0.04):
    return ('<line x1="{:.3f}" y1="{:.3f}" x2="{:.3f}" y2="{:.3f}" '
            'stroke="{}" stroke-width="{}"/>\n').format(x1, y1, x2, y2, INK, sw)


# ---------------------------------------------------------------- geometria
def net_T():
    """Planificação com o TETO no centro da travessa -> le como T."""
    faces = {}
    faces['L'] = (0,            0, S_W, S_H)
    faces['C'] = (S_W,          0, C_W, C_H)
    faces['R'] = (S_W + C_W,    0, S_W, S_H)
    faces['B'] = (S_W,        C_H, B_W, B_H)
    return faces, S_W * 2 + C_W, C_H + B_H          # 66 x 38


def net_perp():
    """Planificação com o FUNDO no centro -> le como ⊥ (comparativo)."""
    faces = {}
    faces['C'] = (S_H,          0, C_W, C_H)
    faces['L'] = (0,          C_H, S_H, B_H)
    faces['B'] = (S_H,        C_H, B_W, B_H)
    faces['R'] = (S_H + B_W,  C_H, S_H, B_H)
    return faces, S_H * 2 + B_W, C_H + B_H          # 74 x 38


def t_minusculo():
    """t minusculo no modulo de 0,48 m.

    ATENCAO: um t geometrico SIMETRICO le como crucifixo. A leitura de
    letra depende de tres assimetrias, todas aplicadas aqui:
      1. travessa desigual  - avanca mais a direita (5 un) que a esquerda (4)
      2. pe                 - degrau a direita na base (a curva do t)
      3. ascendente curta   - so 10 un acima da travessa, nao meia altura
    """
    W, H = 26, 38
    stem_x, stem_w = 9, 6
    bar_y, bar_h = 10, 6
    return [
        (stem_x,          0,      stem_w, H),          # haste
        (stem_x - 4,      bar_y,  4,      bar_h),      # travessa esquerda
        (stem_x + stem_w, bar_y,  9,      bar_h),      # travessa direita (maior)
        (stem_x + stem_w, H - 6,  7,      6),          # pe / degrau a direita
    ], W, H


def T_otico():
    """O T do net com a haste estreitada por correcao optica.

    O net literal tem haste = 48% da travessa, o que le pesado e fecha a
    contraforma. Aqui a haste cai para ~34% mantendo a altura real.
    """
    faces, W, H = net_T()
    _, _, _, bh = faces['B']
    new_w = C_W * 0.70
    cx = S_W + C_W / 2.0
    out = dict(faces)
    out['B'] = (cx - new_w / 2.0, C_H, new_w, bh)
    return out, W, H


def blocks(faces, step=4.0, gap=0.55):
    """Converte as faces em modulos discretos (quadrados soltos)."""
    out = []
    for (fx, fy, fw, fh) in faces.values():
        nx, ny = int(round(fw / step)), int(round(fh / step))
        cw, ch = fw / nx, fh / ny
        for i in range(nx):
            for j in range(ny):
                out.append((fx + i * cw + gap / 2, fy + j * ch + gap / 2,
                            cw - gap, ch - gap))
    return out


# ---------------------------------------------------------------- svgs
def build():
    made = []

    # 01 · net exato, com a malha do modulo
    faces, W, H = net_T()
    body = ''
    for (x, y, w, h) in faces.values():
        for i in range(1, int(w)):
            body += line(x + i, y, x + i, y + h)
        for j in range(1, int(h)):
            body += line(x, y + j, x + w, y + j)
    for (x, y, w, h) in faces.values():
        body += orect(x, y, w, h)
    p = os.path.join(OUT, 'tera_01_net_exato.svg')
    open(p, 'w', encoding='utf-8').write(svg(W, H, body))
    made.append(('01 · net exato + malha 0,48 m', p, W, H))

    # 02 · T solido, faces cheias separadas pela fresta
    f = 0.5
    body = ''
    for (x, y, w, h) in faces.values():
        body += rect(x + f / 2, y + f / 2, w - f, h - f)
    p = os.path.join(OUT, 'tera_02_T_solido.svg')
    open(p, 'w', encoding='utf-8').write(svg(W, H, body))
    made.append(('02 · T solido (planos + fresta)', p, W, H))

    # 03 · T em modulos discretos
    body = ''.join(rect(*b) for b in blocks(faces))
    p = os.path.join(OUT, 'tera_03_T_modulos.svg')
    open(p, 'w', encoding='utf-8').write(svg(W, H, body))
    made.append(('03 · T em modulos discretos', p, W, H))

    # 04 · T com haste corrigida opticamente
    faces_o, Wo, Ho = T_otico()
    body = ''
    for (x, y, w, h) in faces_o.values():
        body += rect(x + f / 2, y + f / 2, w - f, h - f)
    p = os.path.join(OUT, 'tera_04_T_otico.svg')
    open(p, 'w', encoding='utf-8').write(svg(Wo, Ho, body))
    made.append(('04 - T com haste corrigida (70% do teto)', p, Wo, Ho))

    # 05 · t minusculo solido
    parts, W3, H3 = t_minusculo()
    body = ''.join(rect(*r) for r in parts)
    p = os.path.join(OUT, 'tera_05_t_minusculo.svg')
    open(p, 'w', encoding='utf-8').write(svg(W3, H3, body))
    made.append(('05 · t minusculo no modulo', p, W3, H3))

    # 06 · t minusculo em modulos
    fake = {i: r for i, r in enumerate(parts)}
    body = ''.join(rect(*b) for b in blocks(fake, step=3.0, gap=0.5))
    p = os.path.join(OUT, 'tera_06_t_modulos.svg')
    open(p, 'w', encoding='utf-8').write(svg(W3, H3, body))
    made.append(('06 · t minusculo em modulos', p, W3, H3))

    return made


# ---------------------------------------------------------------- preview
def preview(made):
    """Board PNG: 3 colunas x 2 linhas, preto e branco."""
    CW, CH, PAD, TOP = 1040, 760, 60, 66
    cols, rows = 3, 2
    Wpx = cols * CW + PAD * (cols + 1)
    Hpx = rows * (CH + TOP) + PAD * (rows + 1)
    img = Image.new('RGB', (Wpx, Hpx), 'white')
    d = ImageDraw.Draw(img)

    faces, W, H = net_T()
    faces2, W2, H2 = T_otico()
    parts, W3, H3 = t_minusculo()
    f = 0.5

    def draw_cell(idx, kind):
        c, r = idx % cols, idx // cols
        ox = PAD + c * (CW + PAD)
        oy = PAD + r * (CH + TOP) + TOP
        d.rectangle([ox - 1, oy - 1, ox + CW, oy + CH], outline='#dddddd')
        d.text((ox, oy - 34), made[idx][0], fill='#111111')

        if kind in ('net', 'solid', 'mods'):
            gw, gh, fs = W, H, faces
        elif kind == 'perp':
            gw, gh, fs = W2, H2, faces2
        else:
            gw, gh, fs = W3, H3, None

        s = min((CW - 120) / gw, (CH - 120) / gh)
        bx = ox + (CW - gw * s) / 2
        by = oy + (CH - gh * s) / 2

        def R(x, y, w, h):
            d.rectangle([bx + x * s, by + y * s,
                         bx + (x + w) * s, by + (y + h) * s], fill='#111111')

        if kind == 'net':
            for (x, y, w, h) in fs.values():
                for i in range(int(w) + 1):
                    d.line([bx + (x + i) * s, by + y * s,
                            bx + (x + i) * s, by + (y + h) * s], fill='#c9c9c9')
                for j in range(int(h) + 1):
                    d.line([bx + x * s, by + (y + j) * s,
                            bx + (x + w) * s, by + (y + j) * s], fill='#c9c9c9')
            for (x, y, w, h) in fs.values():
                d.rectangle([bx + x * s, by + y * s,
                             bx + (x + w) * s, by + (y + h) * s],
                            outline='#111111', width=3)
        elif kind in ('solid', 'perp'):
            for (x, y, w, h) in fs.values():
                R(x + f / 2, y + f / 2, w - f, h - f)
        elif kind == 'mods':
            for b in blocks(fs):
                R(*b)
        elif kind == 'tsolid':
            for rr in parts:
                R(*rr)
        elif kind == 'tmods':
            for b in blocks({i: rr for i, rr in enumerate(parts)}, step=3.0, gap=0.5):
                R(*b)

    for i, k in enumerate(['net', 'solid', 'mods', 'perp', 'tsolid', 'tmods']):
        draw_cell(i, k)

    p = os.path.join(OUT, 'board_net_to_t.png')
    img.save(p)
    return p


# ---------------------------------------------------------------- reducao
def reduction():
    """Reducao critica do t minusculo (altura em px) + inversao."""
    parts, W, H = t_minusculo()
    sizes = [16, 24, 32, 64, 160]
    gap, top = 56, 70
    Wpx = int(sum(s * W / H for s in sizes) + gap * (len(sizes) + 1))
    Hpx = max(sizes) * 2 + top * 2 + gap
    img = Image.new('RGB', (Wpx, Hpx), 'white')
    d = ImageDraw.Draw(img)

    # faixa escura embaixo, para checar a versao invertida
    y_dark = top + max(sizes) + gap // 2
    d.rectangle([0, y_dark - 20, Wpx, Hpx], fill='#111111')

    x = gap
    for px in sizes:
        s = px / float(H)
        for (ink, oy) in [('#111111', top + (max(sizes) - H * s)),
                          ('#ffffff', y_dark + 30 + (max(sizes) - H * s))]:
            for (rx, ry, rw, rh) in parts:
                d.rectangle([x + rx * s, oy + ry * s,
                             x + (rx + rw) * s, oy + (ry + rh) * s], fill=ink)
        d.text((x, 28), '%d px' % px, fill='#111111')
        x += int(px * W / H) + gap

    p = os.path.join(OUT, 'board_reducao.png')
    img.save(p)
    return p


if __name__ == '__main__':
    made = build()
    for name, path, w, h in made:
        print('%-44s %s  (%dx%d un)' % (name, os.path.basename(path), w, h))
    print('board  ->', preview(made))
    print('reducao->', reduction())
