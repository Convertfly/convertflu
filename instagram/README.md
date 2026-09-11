# Instagram · @convertfly.app

Esteira de publicação para carrossel e post único. Reels e Stories ficam fora.

```
baseline/AAAA-MM.json   snapshot mensal. A API do Instagram so guarda 30 dias
                        de seguidores, entao este arquivo e o unico historico.
planos/AAAA-MM/         plano.md + uma pasta por publicacao (briefing + spec)
artes/AAAA-MM/          PNG 1080x1350. Somente PNG, nunca HTML.
chassi/                 fontes em base64, CSS e gerador. Fonte de verdade da arte.
```

## Gerar a arte de uma publicação

```bash
cd instagram/chassi
python3 gerar.py ../planos/2026-10/c01-verba-pagina/spec.json \
                 --saida ../artes/2026-10/c01-verba-pagina
```

O gerador reprova antes de renderizar quando encontra travessão em qualquer
campo ou três slides seguidos da mesma superfície. O HTML vai para um
temporário e nunca é entregável. Os PNG saem do elemento `.slide`, não do
viewport, o que garante 1080 x 1350 exatos.

## Pele

Tokens espelhados de `design-system/`. Cinco âncoras mais o gradiente de
quatro cores. A assinatura é a palavra-chave em serifa itálica com o
gradiente no texto, e ela só aparece em palavra-chave e em número-herói.
O gradiente nunca vira parede de fundo: ele é barra, régua, texto clipado,
preenchimento de progresso e aura desfocada.

Fontes embutidas em base64 porque Mulish não está instalada no runner. Sem
isso o PNG sai em fonte de fallback.
