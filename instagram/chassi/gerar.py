#!/usr/bin/env python3
"""
CONVERTFLY · gerador de carrossel 4:5 (1080 x 1350)

Fonte de verdade da arte. Recebe um spec JSON, escreve os HTML de trabalho
num temporario e renderiza os PNG finais. A pasta de entrega recebe somente PNG.

  python3 gerar.py spec.json --saida ../artes/2026-09/saves

Superficies: dark | light | grad. A alternancia e validada: nunca tres
slides seguidos da mesma superficie.
"""
from __future__ import annotations

import argparse
import html
import json
import pathlib
import shutil
import subprocess
import sys
import tempfile

RAIZ = pathlib.Path(__file__).resolve().parent
LARGURA, ALTURA = 1080, 1350


# ── marcacao inline ──────────────────────────────────────────────────
def rich(txt: str) -> str:
    """*palavra* vira accent (Times italico gradiente). **palavra** vira strong.
    <br> passa. O resto e escapado."""
    out = html.escape(txt, quote=False)
    out = out.replace("&lt;br&gt;", "<br>")
    for marca, tag, cls in (("**", "strong", ""), ("*", "span", "accent")):
        partes = out.split(marca)
        if len(partes) > 1:
            reconstruido = partes[0]
            for i, p in enumerate(partes[1:], start=1):
                if i % 2:
                    abre = f'<{tag} class="{cls}">' if cls else f"<{tag}>"
                    reconstruido += abre + p
                else:
                    reconstruido += f"</{tag}>" + p
            out = reconstruido
    return out


def checar_travessao(spec: dict) -> list[str]:
    """Travessao e proibido em qualquer copy de card. Regra inviolavel."""
    achados = []
    def varrer(no, caminho):
        if isinstance(no, str):
            if "—" in no or "–" in no:
                achados.append(f"{caminho}: {no[:70]}")
        elif isinstance(no, dict):
            for k, v in no.items():
                varrer(v, f"{caminho}.{k}")
        elif isinstance(no, list):
            for i, v in enumerate(no):
                varrer(v, f"{caminho}[{i}]")
    varrer(spec, "spec")
    return achados


def checar_alternancia(slides: list[dict]) -> list[str]:
    erros = []
    for i in range(2, len(slides)):
        trio = [s.get("superficie") for s in slides[i - 2 : i + 1]]
        if trio[0] == trio[1] == trio[2]:
            erros.append(f"slides {i-1}, {i} e {i+1} sao todos '{trio[0]}'")
    return erros


# ── blocos ───────────────────────────────────────────────────────────
def bloco(b: dict) -> str:
    t = b.get("tipo")
    if t == "texto":
        return f'<div class="body">{rich(b["txt"])}</div>'
    if t == "stat":
        rot = f'<div class="stat-label">{rich(b["rotulo"])}</div>' if b.get("rotulo") else ""
        return f'<div class="stat">{html.escape(b["valor"])}</div>{rot}'
    if t == "card":
        cor = "card-glass" if b.get("glass") else "card-light"
        tit = f'<div class="card-title">{rich(b["titulo"])}</div>' if b.get("titulo") else ""
        return f'<div class="{cor}">{tit}<div class="card-text">{rich(b["txt"])}</div></div>'
    if t == "linhas":
        itens = "".join(
            f'<div class="row"><div class="row-arrow">→</div>'
            f'<div class="row-text">{rich(x)}</div></div>'
            for x in b["itens"]
        )
        return f"<div>{itens}</div>"
    if t == "tabela":
        cab = "".join(f"<th>{html.escape(c)}</th>" for c in b["cabecalho"])
        corpo = ""
        for linha in b["linhas"]:
            rotulo, valor = linha["rotulo"], linha["valor"]
            cor = linha.get("cor", "")
            corpo += f'<tr><td>{rich(rotulo)}</td><td class="v {cor}">{rich(valor)}</td></tr>'
        return f'<table class="table"><tr>{cab}</tr>{corpo}</table>'
    if t == "tag":
        return f'<div class="tag {b.get("cor","violet")}">{rich(b["txt"])}</div>'
    if t == "capsule":
        ponto = f'<div class="capsule-dot {b.get("cor","coral")}"></div>' if b.get("cor") else ""
        return f'<div class="capsule">{ponto}{rich(b["txt"])}</div>'
    if t == "regua":
        return '<div class="regua"></div>'
    if t == "espaco":
        return f'<div style="height:{b.get("px",28)}px"></div>'
    raise ValueError(f"bloco desconhecido: {t}")


def montar_slide(s: dict, n: int, total: int, marca: dict) -> str:
    sup = s["superficie"]
    classes = f"slide {sup}" + (" virada" if s.get("virada") else "")
    pct = round(n / total * 100)

    fixos = (
        f'<div class="accent-bar"></div>'
        f'<div class="brand-bar"><span>{html.escape(marca["handle"])}</span>'
        f'<span>{html.escape(marca.get("selo", ""))}</span></div>'
        f'<div class="prog"><div class="prog-track">'
        f'<div class="prog-fill" style="width:{pct}%"></div></div>'
        f'<div class="prog-num">{n:02d} / {total:02d}</div></div>'
    )

    if s.get("capa"):
        inicial = marca["handle"].lstrip("@")[:1].upper()
        return (
            f'<div class="{classes}">{fixos}'
            f'<div class="capa-area">'
            f'<div class="capsule capa-badge"><div class="badge-dot">{inicial}</div>'
            f'{html.escape(marca["handle"])}</div>'
            f'<div class="h-capa">{rich(s["headline"])}</div>'
            f"</div></div>"
        )

    partes = []
    if s.get("eyebrow"):
        cor = s.get("eyebrow_cor", "")
        partes.append(f'<div class="eyebrow {cor}">{html.escape(s["eyebrow"])}</div>')
    if s.get("headline"):
        if sup == "grad":
            partes.append('<div class="regua"></div>')
        h = {"dark": "h-dark", "light": "h-light", "grad": "h-grad"}[sup]
        partes.append(f'<div class="{h}">{rich(s["headline"])}</div>')
    for b in s.get("blocos", []):
        partes.append(bloco(b))

    return f'<div class="{classes}">{fixos}<div class="content">{"".join(partes)}</div></div>'


def montar_cta(s: dict, n: int, total: int, marca: dict) -> str:
    fixos = (
        f'<div class="accent-bar"></div>'
        f'<div class="brand-bar"><span>{html.escape(marca["handle"])}</span>'
        f'<span>{html.escape(marca.get("selo", ""))}</span></div>'
        f'<div class="prog"><div class="prog-track">'
        f'<div class="prog-fill" style="width:100%"></div></div>'
        f'<div class="prog-num">{n:02d} / {total:02d}</div></div>'
    )
    inicial = marca["handle"].lstrip("@")[:1].upper()
    return (
        f'<div class="slide light">{fixos}<div class="content">'
        f'<div class="cta-bridge">{rich(s["ponte"])}</div>'
        f'<div class="h-light">{rich(s["headline"])}</div>'
        f'<div class="cta-box">'
        f'<div class="cta-instr">{html.escape(s["instrucao"])}</div>'
        f'<div class="cta-word">{html.escape(s["palavra"])}</div>'
        f'<div class="cta-benefit">{rich(s["beneficio"])}</div></div>'
        f'<div class="cta-footer"><div class="badge-dot">{inicial}</div>'
        f'<span>{html.escape(marca["handle"])} · {html.escape(s.get("rodape",""))}</span></div>'
        f"</div></div>"
    )


def pagina(corpo: str, preview: bool) -> str:
    css = (RAIZ / "fontes.css").read_text(encoding="utf-8")
    css += (RAIZ / "chassi.css").read_text(encoding="utf-8")
    cls = "preview" if preview else ""
    envolve = f'<div class="wrap">{corpo}</div>' if preview else corpo
    return (
        f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">'
        f"<style>{css}</style></head><body class=\"{cls}\">{envolve}</body></html>"
    )


def renderizar(pasta_html: pathlib.Path, pasta_png: pathlib.Path) -> None:
    """Delega ao render.js. Screenshot do elemento .slide, nao do viewport:
    o Chrome cru captura num viewport menor que o --window-size e deixa faixa
    de fundo sobrando no rodape."""
    r = subprocess.run(
        ["node", str(RAIZ / "render.js"), str(pasta_html), str(pasta_png)],
        capture_output=True, text=True,
    )
    print(r.stdout, end="")
    if r.returncode != 0:
        raise RuntimeError(f"render.js falhou: {r.stderr.strip()}")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("spec")
    ap.add_argument("--saida", required=True, help="pasta dos PNG finais")
    args = ap.parse_args()

    spec = json.loads(pathlib.Path(args.spec).read_text(encoding="utf-8"))
    slides, marca = spec["slides"], spec["marca"]

    if (achados := checar_travessao(spec)):
        print("REPROVADO · travessao encontrado (regra inviolavel):", file=sys.stderr)
        for a in achados:
            print("  " + a, file=sys.stderr)
        return 1
    if (erros := checar_alternancia(slides)):
        print("REPROVADO · alternancia de superficie:", file=sys.stderr)
        for e in erros:
            print("  " + e, file=sys.stderr)
        return 1

    total = len(slides)
    marcacoes = [
        montar_cta(s, i, total, marca) if s.get("cta") else montar_slide(s, i, total, marca)
        for i, s in enumerate(slides, start=1)
    ]

    saida = pathlib.Path(args.saida).resolve()
    saida.mkdir(parents=True, exist_ok=True)
    tmp = pathlib.Path(tempfile.mkdtemp(prefix="cf-carrossel-"))

    for i, m in enumerate(marcacoes, start=1):
        (tmp / f"card-{i:02d}.html").write_text(pagina(m, preview=False), encoding="utf-8")
    renderizar(tmp, saida)

    prev = tmp / "preview.html"
    prev.write_text(pagina("".join(marcacoes), preview=True), encoding="utf-8")
    shutil.copy(prev, saida / "_preview.html")

    print(f"\n{total} PNG em {saida}")
    print(f"HTML de trabalho em {tmp} (temporario, nao e entregavel)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
