# Assets do site — o que falta e onde cada um entra

Os prints enviados no chat foram **lidos**, mas não viram arquivo: para
aparecerem nas páginas precisam ser anexados como imagem. Salve cada um com
o nome exato abaixo nesta pasta e eu ligo sem precisar perguntar de novo.

## Já resolvido

| Arquivo | Origem |
|---|---|
| `logo-convertfly-claro.png` | extraído da Apresentação Master (600 dpi, fundo escuro) |
| `logo-convertfly-escuro.png` | idem, versão para fundo claro |

Ambos são raster. O SVG oficial continua sendo melhor — se aparecer, troca.

## Prioridade 1 — destrava as páginas principais

| Arquivo | O que precisa aparecer | Onde entra |
|---|---|---|
| `editor-canvas.png` | Editor aberto com PDP de cliente real montada: árvore de camadas à esquerda com seções nomeadas, topbar roxa, canvas preenchido. Desktop, tela cheia. | hero de `/app` e `/app/editor` |
| `pdp-aevi.png` | PDP do Anel Clássico no ar, desktop, rolada até um trecho com trabalho da Convertfly | `/cases` e `/implementacao` |
| `pdp-neurofood.png` | PDP da Banheira de Gelo no ar, mesmo critério | `/cases` e Home |
| `ops-exemplo.png` | Uma página do OPS versão cliente, dados sensíveis borrados | `/implementacao` |

## Prioridade 2 — completa os módulos

| Arquivo | O que precisa aparecer | Onde entra |
|---|---|---|
| `metricas-real.png` | Página de cliente com curva de visualizações preenchida, funil de rolagem nas quatro faixas e tempo médio com valor | `/app/metricas` |
| `teste-ab-real.png` | Teste com visualizações acumuladas nas duas variantes | `/app/teste-ab` |
| `showroom.png` | O LP Showroom **renderizado**, rolado num trecho com vários elementos juntos | `/app/elementos` |
| `galeria-completa.png` | A galeria inteira num print só, ou dois sem sobreposição | `/app/elementos` + conferir a contagem real |

## Prioridade 3 — prova e marca

| Arquivo | O que precisa aparecer | Onde entra |
|---|---|---|
| `loja-*.png` | Print de cada loja da vitrine: `loja-lustres-genesis`, `loja-neurofood`, `loja-winona`, `loja-adel`, `loja-cactario`, `loja-nutricao-total` | vitrine da Home |
| `neurofood-*.png` | As nove features autorais da Neurofood, uma imagem cada | rota `/cases/neurofood` (v4) |
| `fonte-statista.png`, `fonte-nuvem-commerce.png`, `fonte-prax.png` | Os recortes das fontes do benchmark | painel "Sobre os números" na Home |
| `socio-breno.jpg`, `socio-bruno.jpg`, `socio-bia.jpg`, `socio-mauro.jpg` | As quatro fotos circulares em alta | `/quem-somos` |
| `canvas-pdp-board.png` | Board do Miro ou foto de uma sessão real | `/implementacao` |

## Formato

PNG para tela, JPG para foto. Largura mínima de 1600px nos prints de tela —
eles aparecem dentro de mockups e cortam nas bordas. Não precisa recortar
nem tratar: eu enquadro.
