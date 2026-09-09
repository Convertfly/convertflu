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

## 7 · Arquitetura real do site hoje

Nav: **Home · Quem somos · Cases · Contato**, mais o CTA único
`Testar grátis (7 dias)`. Rodapé aponta ainda para **Convert Talks** e
**Portfólio** — duas rotas que não estão na nav.

- **Home** — hero com mockup de PDP real, stat cards, diagnóstico com
  scroll-reveal, painel 60–70%, acordeão dos 4 pilares, bloco de tecnologia
  com print do dashboard do app.
- **Quem somos** — hero escuro, A origem (stat cards claros), A missão,
  Sociedade (4 sócios com foto circular), acordeão "Como a gente trabalha".
- **Cases** — hero, e um case por banda alternando o lado do mockup:
  Neurofood Shop, AEVI Galeria, Sobral — Noite Estrelada.
- **Contato** — hero escuro + formulário em banda clara, com cards de
  contato à direita.

### Dados reais de contato (do print)
WhatsApp +55 11 93618-5493 · contato@convertfly.com.br · Instagram
@convertfly.app · redes: Instagram, YouTube, TikTok, LinkedIn.
Assinatura de rodapé: "BM Web Marketing + Dr. Growth".

### Formulário de contato — campos reais
Nome · Nome da loja · E-mail · WhatsApp · URL da loja (opcional) ·
Plataforma da loja (select) · Como nos conheceu? (select) · Faturamento
mensal da loja (select) · O que você quer resolver? (textarea).
CTA: **Enviar e continuar no WhatsApp**.
O campo de faturamento é qualificação de lead embutida no formulário.

## 8 · Componentes confirmados nesta leva

- **Acordeão de método** (banda clara): linha branca, número `01`, título,
  **tag lilás** com o gancho à direita (`O TRIPÉ DE PESQUISA`,
  `60 MIN QUE MUDAM A PÁGINA`, `ARSENAL DE 40 SEÇÕES`, `RELATÓRIO D+90`),
  toggle `+` / `×`, borda violeta no item aberto.
- **Banda de CTA em gradiente cheio** (laranja → magenta → violeta) ocupando
  a seção inteira, com botão branco sólido + botão outline translúcido.
  É o CTA final padrão do site — não um card escuro.
- **Card de case**: mockup de tablet com sombra, tag lilás de nicho, três
  stats inline, citação em card lavanda com barra violeta à esquerda.
- **Card de sócio**: foto circular, nome, função em cinza.
- **Card de contato**: ícone em quadrado arredondado, rótulo, valor.
- **Eyebrow em duas variantes**: `— TEXTO` e `•— TEXTO` (dot colorido).

## 9 · Fatos que o site já decidiu

- **40 seções** é o número oficial do arsenal (`ARSENAL DE 40 SEÇÕES`).
  Encerra o conflito com o "+15 módulos" da proposta LF8.
- **Beatriz Helena** e **Mauro Rodon** — grafia e funções curtas do site
  ("Estratégia & Vendas", "CTO & Arquitetura do App", "Design & Gestão de
  Projetos", "Analytics & Tracking").
- **Não existe preço em lugar nenhum do site.** O único CTA é o teste de 7
  dias do app. Os pacotes de implementação (R$ 3.500 / 6.500 / 10.500) não
  têm porta de entrada própria hoje.

## 10 · O que ainda falta ver

Home abaixo do bloco de tecnologia · rotas Portfólio e Convert Talks ·
qualquer tela em mobile · estados de hover e foco. Este documento é
cumulativo — cada print novo entra aqui antes de virar CSS.
