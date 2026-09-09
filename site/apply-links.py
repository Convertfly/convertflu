#!/usr/bin/env python3
"""Aplica as URLs de links.json em todos os links marcados com data-link.

Uso:  python3 site/apply-links.py

Cada link do site que ainda não tem destino carrega um data-link com o nome
da chave. Preencha links.json e rode — quem estiver vazio continua como
placeholder, então dá para ir preenchendo aos poucos.
"""
import json, pathlib, re, sys

BASE = pathlib.Path(__file__).parent
links = json.loads((BASE / 'links.json').read_text())
links = {k: v.strip() for k, v in links.items() if not k.startswith('_') and v.strip()}

if not links:
    print('Nada preenchido em links.json — nenhum link alterado.')
    sys.exit(0)

EXTERNO = ' target="_blank" rel="noopener"'
total, por_chave = 0, {}

for page in sorted(BASE.rglob('*.html')):
    html = page.read_text()
    original = html

    def troca(m):
        global total
        tag, chave = m.group(0), m.group('k')
        url = links.get(chave)
        if not url:
            return tag
        novo = tag.replace('href="#"', 'href="%s"' % url)
        if url.startswith('http') and 'target=' not in novo:
            novo = novo.replace('>', EXTERNO + '>', 1)
        total += 1
        por_chave[chave] = por_chave.get(chave, 0) + 1
        return novo

    html = re.sub(r'<a[^>]*href="#"[^>]*data-link="(?P<k>[a-z-]+)"[^>]*>', troca, html)
    html = re.sub(r'<a[^>]*data-link="(?P<k>[a-z-]+)"[^>]*href="#"[^>]*>', troca, html)
    if html != original:
        page.write_text(html)

for chave in sorted(por_chave):
    print('%-24s %d links' % (chave, por_chave[chave]))

# o que continua sem destino: data-link cujo href ainda é "#"
todo = ' '.join(p.read_text() for p in BASE.rglob('*.html'))
pendentes = sorted(set(
    re.findall(r'<a[^>]*href="#"[^>]*data-link="([a-z-]+)"', todo) +
    re.findall(r'<a[^>]*data-link="([a-z-]+)"[^>]*href="#"', todo)))
print('---')
print('%d links preenchidos.' % total)
print('Ainda sem destino: %s' % (', '.join(pendentes) if pendentes else 'nenhum — tudo apontando.'))
