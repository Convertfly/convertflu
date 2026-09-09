# -*- coding: utf-8 -*-
"""Empacota o site inteiro num único HTML navegável, com roteamento por hash."""
import pathlib, re, posixpath

BASE = pathlib.Path('/home/user/convertflu/site')
PAGES = [  # (arquivo relativo, rota)
    ('index.html', '/'),
    ('app/index.html', '/app'),
    ('app/editor/index.html', '/app/editor'),
    ('app/elementos/index.html', '/app/elementos'),
    ('app/paginas/index.html', '/app/paginas'),
    ('app/metricas/index.html', '/app/metricas'),
    ('app/teste-ab/index.html', '/app/teste-ab'),
    ('implementacao/index.html', '/implementacao'),
    ('cases/index.html', '/cases'),
    ('cases/neurofood/index.html', '/cases/neurofood'),
    ('conversao/index.html', '/conversao'),
    ('quem-somos/index.html', '/quem-somos'),
    ('convert-talks/index.html', '/convert-talks'),
    ('contato/index.html', '/contato'),
]
DIR2ROUTE = {posixpath.dirname(f) or '.': r for f, r in PAGES}

def to_route(page_file, href):
    """Converte um href relativo do site em rota de hash."""
    if href.startswith(('mailto:', 'http://', 'https://', 'tel:')) or href == '#':
        return None
    if href.startswith('#'):                      # âncora na própria página
        return None
    frag = ''
    if '#' in href:
        href, frag = href.split('#', 1)
    pagedir = posixpath.dirname(page_file) or '.'
    target = posixpath.normpath(posixpath.join(pagedir, href or '.'))
    target = '.' if target in ('', '.') else target
    route = DIR2ROUTE.get(target)
    if route is None:
        return None
    return '#' + route + ('!' + frag if frag else '')

out = []
for f, route in PAGES:
    html = (BASE / f).read_text()
    body = html.split('<body>', 1)[1].rsplit('</body>', 1)[0]
    body = re.sub(r'<script src="[^"]*cf-web\.js"></script>', '', body)

    def fix(m):
        href = m.group(1)
        r = to_route(f, href)
        return 'href="%s"' % r if r else m.group(0)
    body = re.sub(r'href="([^"]+)"', fix, body)

    # âncoras internas viram rota!fragmento, para o roteador conseguir rolar
    body = re.sub(r'href="#([a-z0-9-]+)"',
                  lambda m: 'href="#%s!%s"' % (route, m.group(1)), body)
    out.append('<div class="rt" data-route="%s">\n%s\n</div>' % (route, body))

css = (BASE / 'assets/cf-web.css').read_text()
font = "@import url('https://fonts.googleapis.com/css2?family=Mulish:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;1,700&display=swap');"

doc = f'''<title>Convertfly · site completo</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Mulish:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;1,700&display=swap">
<style>
{css.replace(font, '')}
.rt {{ display: none; }}
.rt.is-on {{ display: block; }}
</style>

{chr(10).join(out)}

<script>
(function () {{
  var routes = {{}};
  document.querySelectorAll('.rt').forEach(function (el) {{ routes[el.dataset.route] = el; }});

  function show(hash) {{
    var raw = (hash || '').replace(/^#/, '') || '/';
    var parts = raw.split('!'), route = parts[0] || '/', anchor = parts[1];
    if (!routes[route]) route = '/';
    Object.keys(routes).forEach(function (r) {{ routes[r].classList.toggle('is-on', r === route); }});
    document.title = (routes[route].querySelector('h1') || {{}}).textContent
      ? routes[route].querySelector('h1').textContent.trim() + ' · Convertfly'
      : 'Convertfly';
    if (anchor) {{
      var t = routes[route].querySelector('#' + anchor);
      if (t) {{ t.scrollIntoView(); syncNavs(); return; }}
    }}
    window.scrollTo(0, 0);
    syncNavs();
  }}

  // Nav em pílula: aplica em todas as páginas do pacote
  function syncNavs() {{
    var stuck = window.scrollY > 32;
    document.querySelectorAll('.nav').forEach(function (n) {{ n.classList.toggle('is-stuck', stuck); }});
  }}
  window.addEventListener('scroll', syncNavs, {{ passive: true }});
  window.addEventListener('hashchange', function () {{ show(location.hash); }});
  show(location.hash);
}})();
</script>
'''
pathlib.Path('site-completo.html').write_text(doc)
print('site-completo.html', round(len(doc)/1024), 'KB ·', len(PAGES), 'páginas')
