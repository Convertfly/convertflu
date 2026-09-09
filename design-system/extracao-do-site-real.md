# Extração do design system — site real convertfly.com.br

Fonte: prints do site em produção, fornecidos pelo facilitador (setembro 2026).
A rede da sessão bloqueia o domínio, então o print é a fonte primária.

Prioridade de fonte, conforme a skill `design-system-voz-marca`:
**site real > apresentações > transcrições.** Logo, quando este documento
diverge de `colors_and_type.css` (extraído das apresentações), **este vence.**

---

## 1 · Terreno

- Fundo escuro é **indigo/plum saturado**, mais azul que o `#0d0919` extraído do deck.
- Banda clara não é papel quente: é um **branco levemente lavanda** (~`#f5f4fb`).
- **Watermark tipográfico**: a palavra `convertfly` em outline, gigante, sangrando
  atrás do hero. Não é textura genérica — é a própria marca como marca d'água.
- Glow violeta forte no canto superior direito do hero.

## 2 · Navegação

- No topo: transparente sobre o escuro.
- Ao rolar: vira **pílula branca flutuante** com raio grande e sombra, destacada
  das bordas. Não é uma barra reta colada no topo.
- Item ativo sublinhado com o gradiente-assinatura.
- CTA da nav é pílula escura sobre a pílula branca.

## 3 · Botões

- Primário: **gradiente coral → violeta**, formato pílula, com **glow** por baixo.
  (O coral chapado do deck é o secundário, não o primário.)
- Secundário: pílula outline com ícone à esquerda.
- Ambos com ícone antes do label.

## 4 · Tipografia

- Display Mulish ExtraBold, igual ao deck.
- **Keyword serifada em gradiente NÃO usa caixa hairline no site.** A caixa é
  device de slide. Na web, o gradiente sozinho já marca.
- Eyebrow no site vem com **traço antes**: `— O DIAGNÓSTICO`, não `O DIAGNÓSTICO`.
- **Numerais grandes recebem o gradiente** (`37M`, `60-70%`) — no deck eram brancos.

## 5 · Componentes que só existem no site

- **Badge pill do hero** — `✦ TECH PARTNER DE CONVERSÃO · NUVEMSHOP`, outline,
  com ícone dourado.
- **Linha de chips** sob o subtítulo — `ESTRATÉGIA · DESIGN · TECNOLOGIA · DADOS`.
- **Stat card com ícone colorido** — ícone em quadrado arredondado no topo,
  numeral grande abaixo, label em cinza. Um dot violeta decorativo no primeiro.
- **Mockup de browser** — chrome com três dots, contendo screenshot real de PDP
  de cliente (Neurofood). É a prova visual central do hero.
- **Painel de estatística em destaque** — bloco arredondado com fundo violeta
  translúcido, numeral em gradiente enorme à esquerda e texto de apoio à direita.
- **Acordeão de cards-imagem verticais** — 5 cards altos lado a lado, o ativo
  expande e mostra tag + título + texto; os inativos mostram o label **rotacionado
  na vertical**. Usado para os 4 pilares + base científica.
- **Scroll-reveal palavra a palavra** — parágrafo grande que acende conforme rola.

## 6 · Divergência de taxonomia a resolver

Três listas diferentes de tipos de página circulam nos materiais:

| Fonte | Contagem | Lista |
|---|---|---|
| Onboarding B3 | 6 | PDP · Categoria · Global de Produto · Global de Categoria · Home · Landing Page |
| Apresentação Master / proposta LF8 | 6 | PDP · Categoria · Produto global · Categoria global · Landing page · Home e institucional |
| Site real (print) | 6 | produto global · produto específico · categoria global · categoria específica · institucional · blocos de home |
| Facilitador (set/2026) | 7 | as acima **+ vitrine /produtos** |

O site vende "Seis tipos de página" enquanto o facilitador conta sete.
**Fixar uma lista canônica antes do go-live** — ela aparece nas duas rotas,
no app e na proposta comercial.

## 7 · O que ainda falta ver

Prints pendentes: cases, quem somos, contato, rodapé, mobile, e os estados de
hover/foco. Este documento é cumulativo — cada print novo entra aqui antes de
virar CSS.
