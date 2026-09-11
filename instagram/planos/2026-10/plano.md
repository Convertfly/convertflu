# Plano de outubro 2026 · @convertfly.app

Gerado a partir do relatório de setembro (`baseline/2026-09.json`).
Escopo: carrossel e post único. Os Reels do Convert Talks seguem fora deste fluxo.

**Status: aguardando validação.** A grade da seção 6 é proposta. Nenhuma copy ou arte das publicações C02 em diante é produzida antes do aceite.

---

## 1 · Diagnóstico do funil

| Taxa | Setembro | Referência | Status |
|---|---|---|---|
| Shares sobre alcance | 1,07% | > 0,5% é forte | 🟢 2x acima |
| Saves sobre alcance | 0,10% | > 1% é forte | 🔴 10x abaixo |
| Novos seguidores sobre alcance | 0,20% | < 1,5% é crítico | 🔴 abaixo do piso |
| Crescimento da base | +7,7% (32 em 418) | | 🟡 saudável em %, pequeno em absoluto |

**Gargalo do mês: salvamento.** O perfil gera concordância e não gera referência. As pessoas compartilham porque se identificam e não guardam porque não há nada aplicável para voltar. Carrossel é o formato que corrige exatamente isso.

**Dois achados de estrutura**
1. Zero carrosséis em 90 dias. Outubro é o baseline do formato, não o teste dele.
2. As 29 publicações de setembro são Convert Talks, e o CTA é sempre "confira o link na BIO" apontando para o episódio. Nunca para a metodologia. O bloco de conversão do 40/30/30 não existe hoje.

**Meta de outubro:** saves sobre alcance de 0,10% para 0,40%. É 4x, e ainda fica abaixo da referência de 1%. Meta realista para o primeiro mês de um formato novo.

**Duas taxas do funil não são calculáveis.** `profile_views` e `website_clicks` estão depreciados na API no nível de conta, e `profile_links_taps` retornou zero nos 30 dias. O relatório de outubro vai reportar `media_profile_visits` por publicação, que existe em feed e carrossel, no lugar da taxa de cliques na bio.

---

## 2 · Auditoria do perfil

### BIO atual

> Tecnologia, metodologia e layouts de alta conversão.
> 🎙️Convert Talks: o podcast de conversão.
> Fale com a gente 👇🏻

| # | Dimensão | Status | Problema |
|---|---|---|---|
| 1 | Clareza da promessa | 🟡 | Diz o que a marca faz, mas "layouts de alta conversão" descreve entregável, não resultado |
| 2 | Público-alvo | 🔴 | Não diz para quem é. Não aparece lojista, e-commerce nem operação |
| 3 | Prova social | 🔴 | Nenhum número, selo ou diferencial |
| 4 | Benefício de seguir | 🔴 | O usuário não sabe o que ganha ao seguir |
| 5 | CTA | 🟡 | "Fale com a gente" é contato, não é oferta. Não diz o que tem do outro lado |
| 6 | Organização visual | 🟢 | Três linhas, dentro de 150 caracteres, emojis com lógica |
| 7 | Coerência com o conteúdo | 🟡 | A linha 1 promete método e os 29 posts do mês são podcast. A BIO promete uma coisa e o feed entrega outra |
| 8 | Link coerente com a BIO | ⬜ | Não auditável, ver abaixo |

**Leitura:** a BIO é o pitch de 2 segundos e hoje ela não nomeia o público nem entrega prova. Isso ataca direto a taxa de Visitas para Seguidores, que é a mais sensível do funil. Quem chega pelo Reels do podcast não descobre por que deveria seguir.

**Proposta de nova BIO**, na fórmula de 3 linhas (promessa, prova, benefício com CTA). Três versões para escolha:

| Tom | Texto |
|---|---|
| **Direta** | Páginas de produto que vendem sozinhas, para e-commerce.<br>Método Conversion Map™ aplicado em joalheria, moda e recovery.<br>🎙️ Convert Talks toda semana. Diagnóstico grátis 👇 |
| **Autoridade** | A conversão virou disciplina. A gente é dona dela.<br>Tech partner de conversão para e-commerce. 4 nichos, 1 método.<br>🎙️ Convert Talks. Pega o diagnóstico de PDP 👇 |
| **Transformação** | Seu tráfego já chega. A página é que precisa convencer.<br>Conversion Map™: método de PDP de alta conversão para e-commerce.<br>🎙️ Convert Talks toda semana. Diagnóstico grátis 👇 |

As três nomeiam o público (e-commerce), carregam prova (4 nichos, nome do método) e trocam "fale com a gente" por uma oferta concreta.

### O que não consegui auditar

| Elemento | Motivo |
|---|---|
| **Link da bio** | `bio.convertfly.com.br` está bloqueado pelo proxy de saída deste ambiente. Preciso de um print da página ou da lista de botões |
| **Destaques** | A API do Instagram não expõe destaques. Preciso de um print da faixa |
| **Feed fixado** | A API não marca quais posts estão fixados. Preciso de um print da grade |

Os três impactam a mesma taxa que a BIO. Com os prints eu fecho a auditoria e a proposta de reordenação em uma passada.

---

## 3 · Quem de fato está seguindo

Dado de audiência do Windsor, não hipótese.

**Idade.** A faixa dominante é 35 a 44 anos (140 pessoas), seguida de 25 a 34 (111). Juntas são 65% da base.

**Gênero.** Praticamente equilibrado: 148 masculino, 139 feminino, 97 não declarado.

**Cidade.**

| Cidade | Seguidores |
|---|---|
| Rio de Janeiro | 88 |
| São Paulo | 48 |
| Niterói | 11 |
| Curitiba | 10 |
| Marília | 10 |
| Salvador | 8 |

**Um alerta para validar.** Rio tem quase o dobro de São Paulo. São Paulo é onde está a maior concentração de operação de e-commerce do país, então esperar-se-ia o inverso. Duas hipóteses: a base carrega bastante rede pessoal do time, ou a audiência dos convidados do podcast puxa para o Rio. Isso não muda a grade de outubro, mas muda a leitura do churn e a expectativa de conversão: se boa parte da base não é lojista, a taxa de cliques baixa não é só problema de bio.

A forma de checar é o `media_follows` por publicação, que existe em carrossel e post único. Em setembro só uma publicação gerou follows (2, no post de 31/08). Com 5 carrosséis em outubro esse campo passa a dizer que tema traz seguidor de verdade.

---

## 4 · As três personas

### 🎯 Avançado · o lojista que já tentou resolver com mídia

- **Quem é:** dono ou head de e-commerce, 35 a 44 anos, faturamento de R$ 200 mil a R$ 1 milhão por mês. Tem agência de tráfego ou gestor interno.
- **Dor:** aumentou verba, melhorou as métricas de campanha e não viu o faturamento subir na mesma proporção.
- **Desejo:** entender onde o dinheiro está vazando, com número, sem depender de achismo de fornecedor.
- **Objeção:** "já contratei quem prometeu isso e não mudou nada."
- **Estágio:** consciente do problema, avaliando solução.
- **Gatilho de compra:** ver o diagnóstico aplicado a um caso parecido com o dele, com o número antes e o número depois.
- **Tom que ressoa:** técnico e direto, com dado na frente. Zero hype.

### 💰 Econômico · quem olha CAC e margem antes de tudo

- **Quem é:** sócio ou financeiro da operação, 35 a 54 anos. Aprova ou barra investimento.
- **Dor:** o CAC sobe todo trimestre e a margem encolhe. Cada real novo em mídia rende menos que o anterior.
- **Desejo:** parar de comprar tráfego mais caro para o mesmo resultado.
- **Objeção:** "isso é mais um custo. Qual o retorno e em quanto tempo?"
- **Estágio:** consciente do problema, cético quanto à solução.
- **Gatilho de compra:** a conta feita na frente dele, mostrando o custo de não fazer nada.
- **Tom que ressoa:** matemático. Fórmula, comparação, payback.

### 🔍 Curioso · acompanha o método e ainda não contratou

- **Quem é:** profissional de marketing, designer ou gestor de e-commerce, 25 a 34 anos. Consome o Convert Talks.
- **Dor:** sabe que a página importa e não tem um processo para atacar isso.
- **Desejo:** um método que ele consiga aplicar ou defender internamente.
- **Objeção:** "isso é para operação grande, não para a minha."
- **Estágio:** consciente da solução, sem urgência.
- **Gatilho de compra:** material aplicável que ele usa sozinho e que funciona. O uso vira confiança e a confiança vira conversa.
- **Tom que ressoa:** didático e generoso. Mostra o processo por dentro.

> O Curioso é quem move o gargalo do mês. Save é o comportamento dele, não do Avançado. Por isso ele aparece em três das oito publicações e leva os CTAs de material.

---

## 5 · As seis combinações do mês

| # | Pilar × Persona × Formato | Gancho esperado |
|---|---|---|
| 1 | Conceito × Avançado × Carrossel | A campanha melhorou e o faturamento não. A causa não está onde todo mundo procura |
| 2 | Ângulos econômico × Econômico × Carrossel | Quanto custa, por ano, uma página que não convence |
| 3 | Prova Social × Curioso × Post único | O que muda numa página entre o antes e o depois, lado a lado |
| 4 | Conceito × Avançado × Carrossel | As sete objeções que toda página de produto precisa responder |
| 5 | Bastidores × Curioso × Post único | Como nasce um Canvas PDP, por dentro da sessão com o cliente |
| 6 | DSB × Avançado × Carrossel | O diagnóstico de página que aplicamos antes de qualquer projeto |

As combinações 1, 4 e 6 carregam o tema PDP em três ângulos diferentes: diagnóstico, catálogo de objeções e processo. É repetição de território com execução distinta, que é o que constrói autoridade sem virar template.

---

## 6 · Grade de outubro

8 publicações. 5 carrosséis, 3 posts únicos.

| Bloco | Peso | Publicações |
|---|---|---|
| Alcance | 40% | 3 (2 carrosséis, 1 post único) |
| Relacionamento | 30% | 2 (1 carrossel, 1 post único) |
| Conversão | 30% | 3 (2 carrosséis, 1 post único) |

| # | Data | Formato | Pilar | Persona | Bloco | Tema | CTA |
|---|---|---|---|---|---|---|---|
| C01 | 06/10 | Carrossel | Conceito | Avançado | Alcance | Você aumentou a verba e a loja ficou mais pobre | Comenta MAPA |
| P01 | 09/10 | Post único | Prova Social | Curioso | Relacionamento | O que muda numa PDP entre o antes e o depois | Salva para a próxima revisão |
| C02 | 13/10 | Carrossel | Ângulos | Econômico | Conversão | Quanto custa por ano uma página que não convence | Comenta CONTA |
| P02 | 16/10 | Post único | Bastidores | Curioso | Relacionamento | Como nasce um Canvas PDP, por dentro da sessão | Pergunta na caixa |
| C03 | 20/10 | Carrossel | Conceito | Avançado | Alcance | As sete objeções que toda página de produto precisa responder | Comenta OBJEÇÃO |
| P03 | 23/10 | Post único | DSB | Econômico | Conversão | O cálculo que mostra se o problema é mídia ou página | Link na bio |
| C04 | 27/10 | Carrossel | Prova Social | Curioso | Relacionamento | O que o método encontrou em quatro nichos diferentes | Comenta MÉTODO |
| C05 | 30/10 | Carrossel | DSB | Avançado | Conversão | O diagnóstico de página que aplicamos em cliente novo | Comenta DIAGNÓSTICO |

**Regras verificadas**
- Nenhuma função repetida em dias consecutivos de publicação.
- Nenhuma persona em três posições seguidas.
- Cada publicação tem CTA próprio. Nenhum "confira o link na bio" genérico.
- Cinco dos oito CTAs são captação por palavra-chave, que converte leitura em conversa e é o comportamento que puxa save.

---

## 7 · Quick wins da semana

| # | Ação | Onde impacta | Tempo | Por que agora |
|---|---|---|---|---|
| 1 | Trocar a BIO por uma das três versões | Visitas para Seguidores | 5 min | A BIO não nomeia o público nem carrega prova, e é a métrica mais sensível do funil |
| 2 | Fixar no feed o post de 31/08 | Visitas para Seguidores | 2 min | É a única publicação de setembro que gerou follows (2) e teve 48 compartilhamentos |
| 3 | Mandar os prints de destaques, feed fixado e link da bio | Visitas para Link | 5 min | Destrava a metade da auditoria de perfil que a API não entrega |

---

## 8 · Pendências que travam ou condicionam

| Pendência | Efeito |
|---|---|
| **Volume de 8 publicações não confirmado** | É o número que a rotina mensal vai gerar |
| **Logo em arquivo** | O badge do carrossel usa o "C" em gradiente como provisório |
| **Prints de perfil** | Fecham a auditoria das seções que a API não expõe |
| **C02 depende de dado que não existe** | O custo anual de uma página que não converte precisa de número real de cliente. Sem isso o tema sai com a conta em aberto ou é substituído |
| **Plano Windsor em Trial** | Se expirar, a esteira para na coleta |
