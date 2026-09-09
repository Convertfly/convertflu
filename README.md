# Convertfly

Site institucional e comercial da Convertfly, mais os materiais de apresentação
e a documentação do método.

```
site/          o site — HTML estático, sem build obrigatório
docs/          documentos internos (NÃO publicar junto com o site)
design-system/ tokens de marca usados nas apresentações
materiais/     apresentações e propostas em HTML
slides/        motor de deck usado pelos materiais
```

## O site

Quatorze páginas em HTML estático. Sem framework, sem passo de build: o que
está no repositório é o que vai pro ar.

| Rota | O que faz |
|---|---|
| `/` | Tese da categoria, benchmark de conversão e roteamento para as duas rotas |
| `/app` | Hub do produto: os três níveis de autonomia e os cinco módulos |
| `/app/editor` `/app/elementos` `/app/paginas` `/app/metricas` `/app/teste-ab` | Uma LP por módulo |
| `/implementacao` | O serviço sob o Conversion Map™ |
| `/cases` · `/cases/neurofood` | Resultados medidos, com a janela sempre declarada |
| `/conversao` | Ferramenta de conversão média por segmento |
| `/quem-somos` · `/convert-talks` · `/contato` | Marca, conteúdo e contato |

### Ver localmente

```bash
cd site && python3 -m http.server 8000
```

### Empacotar num arquivo só

Para mandar o site inteiro navegável por um link (preview, aprovação):

```bash
python3 site/build-bundle.py     # gera site-completo.html
```

## Preencher os links que faltam

Todo link ainda sem destino carrega um `data-link` com o nome da chave.
Preencha `site/links.json` e rode:

```bash
python3 site/apply-links.py
```

O script só toca no que estiver preenchido, adiciona `target="_blank"` e
`rel="noopener"` em URL externa, e no fim lista o que continua sem destino.
Dá para ir preenchendo aos poucos.

## Imagens

As páginas trazem placeholders listrados onde entram prints reais.
`site/assets/img/MANIFESTO.md` diz o nome exato de cada arquivo, o que precisa
aparecer nele e qual página consome — basta salvar com aquele nome.

## Regras que valem para qualquer alteração

- **Nenhum dado fictício.** Número sem fonte não entra. Case sem autorização
  não entra.
- **Resultado sempre com a janela declarada** — "em 55 dias", nunca "D+90"
  enquanto nenhum ciclo de noventa dias tiver fechado.
- **Limitação técnica se diz na própria página.** O teste A/B é por UTM e não
  split automático; a métrica de carrinho depende do NubeSDK. As duas coisas
  estão escritas onde o recurso é apresentado, e é assim que devem ficar.
- **`docs/` não vai pro ar.** São documentos de estratégia com dado de cliente,
  preço não decidido e avaliação franca do que ainda não se sustenta.
