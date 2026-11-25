# 📓 LOGBOOK AFP — Algoritmos e Programação (2026.2)

> **Como usar este arquivo:** copie-o para a raiz do **seu** repositório (ou para `logbook/LOGBOOK.md`) e preencha **direto no GitHub** (botão ✏️ *Edit this file*) ou no VS Code. Ele reúne todos os instrumentos do Protocolo AFP 2026.2 (Logbook Individual — Campos 01 a 04, 06 e 07; Registro de Revisão por Pares — Campo 05; Checkpoint Conceitual; Rubrica de Defesa Técnica).
>
> **Organização:** o Logbook está dividido em **3 grupos de entrega**, cada um com seu prazo. Dentro de cada grupo, os **ciclos de entrega (01 a 12)** continuam os mesmos, com as orientações de preenchimento. Siga a ordem: **Grupo 1 → Grupo 2 → Grupo 3 → Defesa Técnica**.
>
> O `Diario.md` do checklist passa a ser **este arquivo**: o registro de cada ciclo está na seção do ciclo correspondente.

## 📍 Navegação rápida

| Seção | Prazo |
|---|---|
| [👨‍🎓 Identificação](#-identificação) | Hoje |
| [🟢 Grupo 1](#-grupo-1--prazo-segunda-1611-às-23h59) · Registros 01–04, Campos 01 e 02 | **Segunda 16/11, 23h59** |
| [🟠 Grupo 2](#-grupo-2--prazo-sábado-2111-às-23h59) · Registros 05–08, Checkpoint, Campos 03 e 04 | **Sábado 21/11, 23h59** |
| [🔵 Grupo 3](#-grupo-3--prazo-quinta-2611-às-23h59) · Registros 09–12, Campos 05, 06 e 07 | **Quinta 26/11, 23h59** |
| [🏁 Defesa Técnica](#-defesa-técnica--quarta-1811) | **Quarta 18/11** |
| [🆘 Estou atrasado](#-estou-atrasado-no-logbook-e-agora) | — |

---

## 👨‍🎓 Identificação

| Campo | Preencha |
|---|---|
| **Nome do estudante** | Marcos Oliveira Ferreira|
| **Curso / Módulo** | ADS · 2º período_ |
| **Unidade curricular** | Algoritmos e Programação — UnDB 2026.2 |
| **Professor** | Rondineli Seba Salomão |
| **App-base do meu CRUD** | Spotify |
| **Link do meu repositório** | https://github.com/SantX0/AlgoritimosUNDB |
| **Dupla de revisão (Campo 05)** | Davi Gael Lopes |
| **Função neste ciclo** | Marcos Oliveira Ferreira · Davi Gael Lopes |

---

## 🧭 Regras de ouro (leia antes de preencher)

1. **Processo, não resultado.** O Logbook mostra *como você pensou*, não só o que funcionou. Registre erros, desvios e dúvidas reais.
2. **Vocabulário técnico.** Use os termos da área (ex.: "laço de repetição", "validação de entrada", "estrutura de dados"). Respostas genéricas ("aprendi Python") não são aceitas.
3. **Todo registro relevante tem 3 âncoras:** o **objeto de conhecimento** mobilizado + a **justificativa técnica** + a **referência/fonte**. *Decisão sem objeto de conhecimento e sem referência é considerada não rastreável e não conta para a avaliação formativa.*
4. **Coerência entre campos.** O Campo 02 deve ser coerente com o Campo 01. *Incoerência é evidência de autoria externa.* O Campo 07 retoma o Campo 01.
5. **IA é permitida e avaliada (Campo 04).** *Print sem análise crítica = devolução imediata. Reproduzir a IA sem questionamento = reprovado.* Você precisa mostrar o que aceitou **e** o que questionou/descartou, com argumento técnico.
6. **O histórico do Git é a sua evidência.** Faça commits pequenos e frequentes. Nunca reescreva o histórico (`force push`) do arquivo do Logbook.
7. **Campo 01 e Checkpoint são "sem consulta".** Preencha em um bloco contínuo, sem internet, sem material e sem colegas, no tempo indicado (Campo 01: durante o laboratório; Checkpoint: 20 min). Depois **não edite** esses campos — se perceber um erro, corrija em um campo posterior (Campo 03 ou 07), explicando.
8. **Os prazos dos grupos (16/11, 21/11 e 26/11, às 23h59)** valem para o commit no GitHub. O horário do commit é o registro oficial.

### ✅ Padrão de commit do Logbook

```text
docs(logbook): campo 01 — ciclo 02
docs(logbook): registro do ciclo 05
docs(logbook): campo 05 — revisão do CRUD de <colega>
```

---

## 🗓️ Calendário de entregas e Defesa

Os grupos têm **5 dias entre um prazo e outro**. O horário do commit no GitHub é o registro oficial.

| Grupo | Janela de preenchimento | **Prazo** | O que entregar |
|:--:|---|---|---|
| **1** | Qua 11/11 → seg 16/11 | **Segunda 16/11, 23h59** | Identificação · Registros dos Ciclos 01 a 04 · Campo 01 · Campo 02 |
| **2** | Seg 16/11 → sáb 21/11 | **Sábado 21/11, 23h59** | Registros dos Ciclos 05 a 08 · Checkpoint Conceitual · Campo 03 · Campo 04 |
| **3** | Sáb 21/11 → qui 26/11 | **Quinta 26/11, 23h59** | Registros dos Ciclos 09 a 12 · Campo 05 (2 revisões) · Campo 06 · Campo 07 |
| 🏁 | — | **Quarta 18/11** | **Defesa Técnica individual** (Rubrica) |

### Linha do tempo

| Data | Evento |
|---|---|
| Qua 11/11 | **Hoje:** começa o Grupo 1 |
| Seg 16/11 | ✅ Prazo do **Grupo 1** |
| **Qua 18/11** | 🏁 **Defesa Técnica** |
| Sáb 21/11 | ✅ Prazo do **Grupo 2** |
| Qua 25/11 | Avaliação P2 |
| Qui 26/11 | ✅ Prazo do **Grupo 3** |
| Qua 02/12 | Avaliação Substitutiva |
| Qua 09/12 | Avaliação Final |

> ⚠️ **Atenção:** a Defesa Técnica (18/11) acontece **antes** dos prazos dos Grupos 2 e 3. Na defesa você será arguido sobre **o que já estiver registrado e commitado**. Veja a seção [Defesa Técnica](#-defesa-técnica--quarta-1811) para saber o que priorizar até 18/11.

### Ciclos de entrega por grupo

| Ciclo | Data da aula | Tema do ciclo | Grupo | O que preencher |
|:--:|:--:|---|:--:|---|
| 01 | 12/08 | Preparação do laboratório e escolha do projeto | **1** | Registro do Ciclo |
| 02 | 19/08 | Variáveis, tipos de dados, entrada/saída | **1** | Registro + **Campo 01** + **Campo 02** |
| 03 | 26/08 | Operadores, fluxogramas, paradigmas | **1** (registro) · **2** (campos) | Registro (G1) · **Checkpoint**, **Campo 03**, **Campo 04** (G2) |
| 04 | 02/09 | Condicionais: `if`, `elif`, `else` | **1** | Registro do Ciclo |
| 05 | 09/09 | Condicionais aninhadas e operadores lógicos | **2** | Registro do Ciclo |
| 06 | 30/09 | Repetição: `for`, `while`, `break`, `continue` | **2** | Registro do Ciclo (inclui devolutiva da P1) |
| 07 | 07/10 | Listas: armazenamento e iteração | **2** | Registro do Ciclo |
| 08 | 14/10 | Busca e introdução a dicionários/matrizes | **2** | Registro do Ciclo |
| 09 | 21/10 | Atualização e exclusão: CRUD completo | **3** | Registro + **Campo 05** (revisão nº 1) |
| 10 | 28/10 | Modularização: funções | **3** | Registro do Ciclo |
| 11 | 04/11 | Recursividade | **3** | Registro + **Campo 06** |
| 12 | 11/11 | Refatoração e qualidade de código | **3** | Registro + **Campo 05** (revisão nº 2) + **Campo 07** |

---

## 📊 Painel de acompanhamento

Atualize a cada commit (troque ⬜ por ✅).

| Grupo | Item | Prazo | Preenchido | Commit |
|:--:|---|---|:--:|:--:|
| 1 | Identificação | 16/11 | ✅ | ✅ |
| 1 | Registros dos Ciclos 01, 02, 03 e 04 | 16/11 | ✅ | ✅ |
| 1 | Campo 01 — Instrumento de entrada | 16/11 | ✅ | ✅ |
| 1 | Campo 02 — Aprofundamento | 16/11 | ✅ | ✅ |
| 2 | Registros dos Ciclos 05, 06, 07 e 08 | 21/11 | ✅ | ✅ |
| 2 | Checkpoint Conceitual | 21/11 | ⬜ | ⬜ |
| 2 | Campo 03 — Execução e desvios | 21/11 | ✅ | ✅ |
| 2 | Campo 04 — Interação com IA | 21/11 | ✅ | ✅ |
| 3 | Registros dos Ciclos 09, 10, 11 e 12 | 26/11 | ✅ | ✅ |
| 3 | Campo 05 — Revisão por pares nº 1 e nº 2 | 26/11 | ✅ | ✅ |
| 3 | Campo 06 — Próximos passos | 26/11 | ⬜ | ⬜ |
| 3 | Campo 07 — Evolução conceitual | 26/11 | ⬜ | ⬜ |
| 🏁 | Defesa Técnica | 18/11 | ⬜ | — |

---

## ❓ A questão-problema da AFP

**Título:** *O sistema em produção: diagnosticando as falhas do CRUD que você mesmo construiu.*

> **Enunciado completo (Apêndice A):** _professor(a): cole aqui o enunciado e os anexos liberados conforme o cronograma._

A questão-problema é **a mesma durante todo o semestre**: ela se aplica ao **seu** CRUD, que cresce a cada ciclo. Os **dados com defeito** do seu app chegam em um **lote cumulativo único** e vão expondo problemas diferentes conforme sua estrutura evolui. Seu trabalho é diagnosticar, ajustar o CRUD para tratar cada falha e **registrar o raciocínio** neste Logbook.

---

# 🔁 REGISTRO DO CICLO — modelo (copie em cada ciclo)

Cada ciclo tem sua própria seção abaixo, já com o modelo. Se precisar de espaço extra, acrescente linhas.

```markdown
### Registro do Ciclo NN — DD/MM
1. **Desafio do ciclo (em 1 frase):**
2. **O que implementei (commits / arquivos / links):**
3. **Objeto(s) de conhecimento mobilizado(s) (vocabulário técnico):**
4. **Desvio ou erro encontrado + causa técnica:**
5. **Decisão de ajuste + fonte (livro, doc, vídeo, colega, IA):**
6. **Feedback recebido (professor/colega) e o que mudei por causa dele:**
7. **Próximo passo:**
```

**Como preencher bem:** escreva como se explicasse a um colega que não esteve na aula. O item 3 e o item 5 são os mais importantes: eles ligam o que você fez ao **conteúdo** e à **fonte**.

| ❌ Fraco | ✅ Forte |
|---|---|
| "Aprendi a usar `if`." | "Usei estrutura condicional aninhada para validar a idade antes de cadastrar. Meu erro foi comparar `str` com `int` (resultado de `input()`); corrigi com `int()` (Pense em Python, cap. 2)." |
| "Deu erro e consertei." | "O programa quebrou com `ZeroDivisionError` ao calcular a média de um item sem avaliações. Causa: divisão por `len(lista)` com lista vazia. Ajuste: testar `if len(lista) > 0`." |

---

# 🟢 GRUPO 1 — prazo segunda 16/11 às 23h59

> **Janela:** quarta 11/11 → segunda 16/11. **O que entregar:** Identificação · Registros dos Ciclos 01, 02, 03 e 04 · Campo 01 · Campo 02.
>
> **Sugestão de ordem:** (1) Identificação → (2) **Campo 01 primeiro, sem consulta** → (3) Registros dos Ciclos 01 a 04 → (4) Campo 02, com pesquisa.

**Checklist do Grupo 1**
- [x] Identificação preenchida (app-base, link do repositório, dupla de revisão)
- [x] Campo 01: 3 objetos de conhecimento, 3 lacunas, hipótese de até 5 linhas
- [x] Registros dos Ciclos 01, 02, 03 e 04 com os 7 itens
- [x] Campo 02: 2 referências com contribuição, hipótese revisada, 3 recursos
- [x] Commits no GitHub e painel atualizado

## 🟢 CICLO 01 — 12/08 — Preparação do laboratório e escolha do projeto

<details>
<summary>📘 Orientações do Ciclo 01</summary>

- **Hoje não há Campo do Protocolo.** O foco é preparar o ambiente: criar o repositório, configurar o VS Code e escolher o **app-base** do seu CRUD (e, portanto, o *schema* dos seus dados).
- Preencha a **Identificação** (no início deste arquivo) e o **Registro do Ciclo 01**.
- No item 3, registre **o que você já sabia** e o que era novo (Git, GitHub, VS Code). Isso será útil para o Campo 07.
- No item 4, registre qualquer problema de instalação ou configuração e como o resolveu — isso conta como desvio.
- Faça o primeiro commit: `docs(logbook): registro do ciclo 01`.
</details>

#### Registro do Ciclo 01 — 12/08
1. **Desafio do ciclo (em 1 frase):** Preparar o ambiente de desenvolvimento com Git, GitHub e VS Code para a construção de um CRUD inspirado no sistema de upload de músicas ds.o Spotify, definindo as entidades e a estrutura inicial dos dados

2. **O que implementei (commits / arquivos / links):** Iniciei a preparação do meu ambiente de desenvolvimento utilizando Git, GitHub e VS Code, tendo como objetivo construir um CRUD inspirado no sistema de upload de músicas do Spotify. Utilizei o repositório AlgoritimosUNDB para armazenar as atividades da disciplina e comecei a estruturar o projeto com arquivos Python (.py) e documentação em README.md. O histórico do GitHub apresenta o commit Add initial README with CRUD title, realizado em 06/08, que serve como evidência da documentação inicial. Configurei minha identidade no Git utilizando git config --global user.name e git config --global user.email e utilizei git remote add origin para estabelecer a conexão com o repositório remoto. Também preparei o VS Code com extensões para Python, Code Runner, tradução para português e o tema AMOLED Black Theme. A organização posterior das pastas e a implementação do cadastro de músicas fazem parte da continuidade do desenvolvimento, não sendo consideradas entregas concluídas neste ciclo.
Repositório: https://github.com/SantX0/AlgoritimosUNDB

3. **Objeto(s) de conhecimento mobilizado(s):** Conhecimentos prévios: Já conhecia o Git por utilizá-lo para clonar repositórios, principalmente quando instalava o Powercord no Discord Canary. Entendia o GitHub como uma plataforma de armazenamento de projetos, semelhante a um Google Drive mais avançado. Também conhecia o VS Code como editor de código, principalmente pelo terminal integrado, pelas extensões e pelas ferramentas de inteligência artificial. 
Conhecimentos novos: Ampliei meus conhecimentos sobre controle de versões, utilizando comandos como git init, responsável por inicializar um repositório; git add ., que adiciona alterações à área de preparação; git status, que permite verificar o estado dos arquivos; e git commit, utilizado para registrar versões das alterações. Também conheci os comandos git log, que permite visualizar o histórico de commits do repositório, incluindo informações como autor, data e mensagem de cada commit, e git revert, que permite desfazer as alterações de um commit anterior por meio da criação de um novo commit, preservando o histórico do projeto. Na modelagem inicial do CRUD, comecei a planejar a organização dos dados, separando as informações em Música (nome, autores, produtores, duração e gênero), Arquivo (identificador, nome, formato e status) e Data/Hora de Lançamento (dia, mês, ano, hora e minuto).

4. **Desvio ou erro encontrado + causa técnica:** Não encontrei erros significativos durante a instalação ou configuração das ferramentas. Minha principal dificuldade foi lembrar de executar git init ao criar uma nova pasta destinada a um projeto independente. Esse comando inicializa um repositório Git local, criando a estrutura necessária para o controle de versões. Sem essa inicialização, caso a pasta não esteja dentro de outro repositório, comandos como git status e git commit não conseguem operar normalmente sobre ela. Essa dificuldade me ajudou a compreender a importância de diferenciar a criação de uma pasta comum da inicialização de um repositório Git.

5. **Decisão de ajuste + fonte:** Decidi organizar o projeto em uma pasta específica dentro do meu repositório AlgoritimosUNDB, separando os arquivos do CRUD das atividades da disciplina para facilitar a organização e a localização dos arquivos. Também escolhi desenvolver um CRUD inspirado no sistema de upload de músicas do Spotify, planejando inicialmente três entidades: Música, Arquivo e Data/Hora de Lançamento. Essa separação foi importante para identificar quais informações o sistema precisaria armazenar e ter uma base para o desenvolvimento nas próximas aulas. Além disso, optei por utilizar Git e GitHub para controlar as versões do projeto, acompanhar as alterações realizadas e possibilitar a recuperação de versões anteriores, caso alguma modificação apresentasse problemas.
Fonte: Orientações do professor Rondineli nas aulas de Algoritmos e Programação, que incentivou a utilização do GitHub para armazenar as atividades, do VS Code para desenvolver os projetos e do terminal para praticar comandos de versionamento do git.

6. **Feedback recebido e o que mudei:** Não recebi feedback individual específico sobre o CRUD neste ciclo. Entretanto, segui as orientações gerais do professor Rondineli, que destacou a importância da familiarização com Git, GitHub, VS Code e Python desde as primeiras aulas. Com base nessas orientações, organizei os arquivos em uma pasta específica, configurei as ferramentas necessárias e passei a utilizar o terminal para gerenciar o versionamento e o envio dos arquivos ao repositório.

7. **Próximo passo:** Avançar na implementação do CRUD de upload de músicas, utilizando as entidades definidas neste ciclo para estruturar os dados e desenvolver as operações de cadastro, consulta, atualização e exclusão. Também pretendo aprofundar meus conhecimentos sobre comandos do Git, principalmente o gerenciamento de branches e a realização de commits pequenos e frequentes, mantendo um histórico organizado e rastreável das alterações do projeto.

## 🟢 CICLO 02 — 19/08 — Variáveis, tipos de dados e entrada/saída

<details>
<summary>📘 Orientações do Ciclo 02 — Campo 01 (sem consulta) e Campo 02 (pesquisa)</summary>

**Campo 01 — Instrumento de entrada** · *sem consulta · faça primeiro*
- Preencha **antes de tudo**, em um bloco contínuo de cerca de 15 minutos, sem internet, sem material, sem IA e sem colegas, depois de conhecer a questão-problema e a primeira amostra de dados do seu app. Depois do Campo 01 você pode consultar o que quiser.
- **1a.** Liste pelo menos **3 objetos de conhecimento** que você acha que precisa dominar para resolver o problema. Use o vocabulário técnico da área. *Não precisa acertar tudo — o Campo 07 vai mostrar o quanto você evoluiu.*
- **1b.** Liste pelo menos **3 lacunas**: o que você **não sabe** e precisa descobrir, com precisão (ruim: "não sei programar"; bom: "não sei como validar a entrada para impedir que o usuário digite texto onde espero número").
- **1c.** Escreva sua **hipótese inicial** em até 5 linhas: o que você acha que está causando as falhas do CRUD e por quê.
- Faça o commit **logo ao terminar**. Depois, **não edite** o Campo 01.

**Campo 02 — Aprofundamento** · *AV Qualis · segunda 16/11, 23h59*
- Preencha **depois do Campo 01, com pesquisa real**, e seja coerente com ele.
- **2a.** Pelo menos **2 referências** (livro, documentação, vídeo, artigo), cada uma com a **contribuição** concreta para a sua solução. Não basta listar o título.
- **2b.** **Hipótese revisada:** o que mudou em relação ao Campo 01 e **por quê**. Se não mudou nada, explique por que a pesquisa confirmou a hipótese.
- **2c.** **Dimensionamento inicial de recursos** (mínimo 3 itens), com quantidade estimada e justificativa técnica. Exemplos de recursos no seu contexto: horas de estudo, número de casos de teste, módulos/arquivos do projeto, dados de teste, bibliotecas.
</details>

### 🧩 CAMPO 01 — Instrumento de entrada
*Grupo 1 | Prazo segunda 16/11, 23h59 | SEM CONSULTA*

**1a. Objetos de conhecimento identificados (mínimo 3, com vocabulário técnico):**
1. Entendia que as variáveis era um espaço na memoria aonde conseguíamos armazenar os dados exemplo: oi = 'ola mundo.
2. Domínio conceitual sobre representações de cadeias de caracteres (str), inteiros (int), números de ponto flutuante (float) e valores lógicos (bool).
3. Utilização da função input() para leitura de fluxo de entrada padrão (stdin) e print() para escrita na saída padrão (stdout).
4. Mapeamento estrutural de entidades de domínio e definição de seus respectivos tipos de dados.

**1b. Lacunas — o que não sei e preciso descobrir (mínimo 3, com precisão técnica):**
1. Implementação de blocos de controle de exceção (try-except) ou métodos de verificação de string para mitigar falhas de tempo de execução (ValueError) na conversão explícita de str para int.
2. Compreensão dos tipos e bibliotecas nativas (como o módulo datetime) para armazenamento e formatação de datas e horas, corrigindo o equívoco conceitual de tipar strings formatadas (DD/MM/AAAA e HH:MM) como inteiros.
3.Transposição da abstração teórica e do mapeamento de dados para a escrita, depuração e execução de código-fonte funcional em Python.

**1c. Hipótese inicial em até 5 linhas — com lógica da área de formação:**

> Ainda preciso aprender a armazenar varias músicas, validar entradas incorretas e controlar as opções escolhidas pelo o usuários, mas usando os conhecimento de receber, armazenar e apresentar os valores utilizando variáveis através do input() e print()

### 🧩 CAMPO 02 — Aprofundamento pós-aula
*AV Qualis — Grupo 1 | Segunda 16/11, 23h59*

> **Preenchido depois do Campo 01, com pesquisa real. Deve ser coerente com o Campo 01. Incoerência = evidência de autoria externa.**

**2a. Aprofundamento dos objetos de conhecimento (mínimo 2 referências com síntese da contribuição para a solução):**

- **Referência 1:** Pense em Python: Seção 3.1 e Apêndice A.2 - **Contribuição:** A leitura me ajudou a compreender melhor a diferença entre ValueError e TypeError. Entendi que o ValueError ocorre quando uma operação recebe um argumento do tipo esperado, mas com um valor inadequado, como tentar converter "abc" para inteiro utilizando int().
Já o TypeError ocorre quando uma operação recebe um tipo de dado incompatível com o esperado, como tentar somar uma string diretamente a um número inteiro.
- **Referência 2:** CS50x — Harvard, Módulo 6: Python — **Contribuição:** O curso me ajudou a compreender a utilização de f-strings (f"..."), que permitem inserir valores de variáveis diretamente em textos utilizando chaves.

**2b. Hipótese revisada — o que mudou em relação ao Campo 01 e por quê:**

> Mantive minha hipótese inicial de utilizar variáveis, input() e print() para começar o desenvolvimento do CRUD de músicas. Entretanto, após estudar as diferenças entre ValueError e TypeError, compreendi melhor a importância de validar as entradas fornecidas pelo usuário. Também aprendi a utilizar f-strings para apresentar informações de forma mais organizada. Ainda preciso aprofundar meus conhecimentos sobre como armazenar várias músicas e controlar as opções escolhidas pelo usuário.

**2c. Dimensionamento inicial de recursos (recurso, quantidade estimada, justificativa técnica — mínimo 3 itens):**

| RECURSO / MATERIAL / INSUMO | QUANTIDADE ESTIMADA | JUSTIFICATIVA TÉCNICA |
|---|---|---|
| Livro Pense em Python | 1 livro | Consultar conceitos de programação para compreender e desenvolver as funcionalidades do CRUD. |
| Arquivo Python (.py) | 1 arquivo | Centralizar inicialmente as operações de cadastro, consulta, atualização e exclusão, facilitando a organização e o acompanhamento do código. |
| Registros de músicas para teste | 5 registros | Utilizar dados de exemplo para verificar o funcionamento das operações de cadastro, consulta, atualização e exclusão. |
| Casos de teste | 8 testes | Verificar entradas válidas, inválidas e possíveis erros durante a execução das funcionalidades. |

#### Registro do Ciclo 02 — 19/08
1. **Desafio do ciclo (em 1 frase):** Compreender a utilização de variáveis, tipos de dados e funções de entrada e saída em Python, para começar a aplicar esses conhecimentos na organização e no funcionamento do CRUD de upload de músicas inspirado no Spotify.

2. **O que implementei (commits / arquivos / links):** Durante a aula, pratiquei conceitos relacionados à declaração de variáveis, atribuição de valores e utilização de strings. Também tivemos contato com o operador lógico or, buscando compreender seu funcionamento em expressões Python. O professor Rondineli explicou como combinar atribuições de variáveis com entradas dinâmicas por meio de input(), além da conversão de tipos de dados. Como atividade de casa, desenvolvi e executei uma calculadora simples para praticar esses conhecimentos. O arquivo Calculadora1908PA.py está registrado no meu repositório GitHub. O histórico apresentado contém uma alteração descrita como a retirada de uma função e a mudança dos nomes das variáveis a, b e c, relacionada à organização e à legibilidade do código. Essa atividade me permitiu praticar os conceitos trabalhados na aula e perceber a importância de utilizar nomes de variáveis que facilitem a compreensão do programa.
Repositório: https://github.com/SantX0/AlgoritimosUNDB

3. **Objeto(s) de conhecimento mobilizado(s):** Os principais objetos de conhecimento foram variáveis, atribuição de valores, tipos de dados, entrada e saída de dados e conversão de tipos. Aprendi a utilizar str para representar textos, int para números inteiros, float para números decimais e bool para valores lógicos. Também aprofundei meus conhecimentos sobre input(), utilizado para receber informações do usuário, e print(), responsável por apresentar informações na saída do programa. Outro conceito trabalhado foi a conversão de tipos, principalmente com float(), necessária quando uma entrada recebida como string precisa ser utilizada em operações aritméticas.

4. **Desvio ou erro encontrado + causa técnica:** Encontrei duas dificuldades relacionadas à entrada e à conversão de dados.
A primeira foi o TypeError, que acontecia quando eu esquecia de converter o valor recebido pelo input() antes de realizar uma operação com números. Como o input() retorna uma string, tentar somar diretamente esse valor a um inteiro provocava um erro de incompatibilidade entre tipos. A segunda dificuldade foi o ValueError, que ocorria quando o programa tentava converter uma entrada textual, como "ola", para um tipo numérico utilizando int() ou float(). Essas situações demonstraram que receber um dado não significa que ele esteja automaticamente no tipo adequado para a operação desejada.

5. **Decisão de ajuste + fonte:** Para resolver o TypeError, passei a utilizar a conversão explícita com float(input()) nas entradas destinadas a operações numéricas. Essa decisão permite transformar uma entrada textual válida em um valor numérico que pode ser utilizado em cálculos. Em relação ao ValueError, identifiquei que a conversão com float() ou int() depende de o usuário fornecer um valor compatível com o tipo esperado. Por isso, percebi que ainda precisava aprofundar meus conhecimentos sobre validação de entradas para evitar problemas durante a execução do programa. Essas decisões estão relacionadas aos conceitos de conversão de tipos e compatibilidade entre valores utilizados em operações aritméticas.

Fonte: Pense em Python, seção 3.1 e Apêndice A.2, conforme as referências que utilizei para estudar os conceitos apresentados, além das orientações do professor Rondineli durante a aula.

6. **Feedback recebido e o que mudei:** Durante a aula, o professor Rondineli explicou a utilização dos tipos de dados e das funções input() e print(), demonstrando como receber informações e trabalhar com elas no programa. Essas orientações contribuíram para minha compreensão da necessidade de converter os valores recebidos antes de utilizá-los em operações numéricas. Também passei a prestar mais atenção à escolha dos nomes das variáveis, buscando melhorar a legibilidade do código. Não recebi feedback individual específico sobre o CRUD neste ciclo.

7. **Próximo passo:** Aprofundar meus conhecimentos sobre operadores de comparação e estruturas condicionais, para compreender como controlar o fluxo de execução do programa de acordo com diferentes situações e escolhas do usuário. Pretendo utilizar esses conhecimentos futuramente no CRUD, principalmente para permitir a seleção de operações e verificar condições relacionadas às informações cadastradas.

## 🟢 CICLO 03 — 26/08 — Operadores, fluxogramas e paradigmas

<details>
<summary>📘 Orientações do Ciclo 03 — Registro (Grupo 1)</summary>

- Neste grupo você preenche **apenas o Registro do Ciclo 03**. O **Checkpoint Conceitual** e os **Campos 03 e 04** deste ciclo estão no **Grupo 2**.
- Item 3: nomeie os **operadores** (aritméticos, relacionais, lógicos) e os **tipos** que usou. Se montou fluxogramas, cite o que o fluxograma ajudou a perceber.
- Item 4: registre erros de precedência de operadores, divisão por zero ou confusão entre `=` e `==`, com a causa técnica.
</details>

#### Registro do Ciclo 03 — 26/08
1. **Desafio do ciclo (em 1 frase):** Compreender a utilização dos operadores aritméticos, de comparação e lógicos em Python, além de aprender a representar o fluxo de execução de um programa por meio de fluxogramas, visando aplicar esses conhecimentos no desenvolvimento do CRUD de músicas.

2. **O que implementei (commits / arquivos / links):** Durante a aula, o professor Rondineli propôs uma atividade de cálculo de médias utilizando operadores e comparações entre valores, que consegui desenvolver e executar. O programa está identificado no arquivo CalcularMedias2608.py, presente no meu repositório GitHub. Também solicitou a elaboração de um fluxograma no caderno para representar como o nosso sistema CRUD funcionaria. Comecei a desenvolver esse fluxograma, utilizando os símbolos apresentados durante a aula, mas não consegui concluí-lo naquele momento. Na construção do fluxograma, utilizei o oval para indicar o início e o fim do fluxo, o retângulo para representar ações ou processamentos, as setas para indicar a direção e a conexão entre as etapas e o losango para representar pontos de decisão. Além disso, pratiquei a construção de fluxogramas em casa, refazendo representações e criando outros exemplos relacionados a situações do cotidiano, buscando compreender melhor como organizar as etapas de um algoritmo.
Neste ciclo, concluí a atividade de cálculo de médias, enquanto o fluxograma do CRUD permaneceu em desenvolvimento.
Repositório: https://github.com/SantX0/AlgoritimosUNDB

3. **Objeto(s) de conhecimento mobilizado(s):** Os principais objetos de conhecimento foram operadores aritméticos, operadores de comparação, operadores lógicos e representação de algoritmos por fluxogramas. Utilizei operadores aritméticos como +, * e /, responsáveis por realizar operações matemáticas. Também trabalhei com os operadores de comparação > e <, utilizados para verificar relações entre valores. Outro conhecimento mobilizado foi a representação do fluxo de execução por meio de símbolos gráficos. Aprendi a identificar início e fim, processos, conexões e pontos de decisão, compreendendo como essas representações ajudam a visualizar a sequência de execução de um algoritmo antes de implementá-lo em código.

4. **Desvio ou erro encontrado + causa técnica:** Encontrei duas dificuldades durante o aprendizado. A primeira foi compreender como utilizar corretamente o losango nos fluxogramas. Eu ainda tinha dúvidas sobre onde posicionar os pontos de decisão e como organizar as diferentes possibilidades de continuidade do fluxo, o que contribuiu para que eu não concluísse o fluxograma do CRUD durante a atividade. A segunda dificuldade foi diferenciar os operadores = e == em Python. Inicialmente, confundia suas finalidades, pois os dois utilizam o mesmo símbolo básico. Entretanto, = é utilizado para atribuir valores a variáveis, enquanto == verifica se dois valores são iguais. Essas dificuldades estavam relacionadas à compreensão da lógica de decisão e à diferenciação entre atribuição e comparação.

5. **Decisão de ajuste + fonte:** Para compreender melhor a utilização do losango, decidi praticar em casa, refazendo fluxogramas e criando outros exemplos relacionados a problemas do cotidiano. Essa prática me ajudou a compreender melhor onde representar as decisões e como conectar os diferentes caminhos do fluxo. Para diferenciar = de ==, utilizei a explicação do professor Rondineli e criei uma associação mental: o sinal = serve para atribuir um valor, enquanto == é utilizado para comparar dois valores. Essas decisões estão relacionadas aos conceitos de representação de algoritmos, fluxo de execução, atribuição e operadores de comparação, pois compreender a função de cada símbolo e operador é necessário para estruturar corretamente a lógica do programa.
Fonte: Orientações e explicações do professor Rondineli durante a aula de Algoritmos e Programação, além dos exercícios de fluxogramas que pratiquei em casa.

6. **Feedback recebido e o que mudei:** Não recebi feedback individual específico sobre o CRUD neste ciclo, mas o professor Rondineli apresentou orientações gerais sobre operadores e representação de algoritmos.
Durante a aula, explicou o operador aritmético %, utilizado para obter o resto de uma divisão, e a exponenciação com **. Também comentou sobre o paralelogramo nos fluxogramas, utilizado para representar operações de entrada e saída de dados. Essas explicações ampliaram meu conhecimento sobre os operadores disponíveis em Python e sobre os símbolos utilizados na construção de fluxogramas. A partir das orientações e da prática individual, passei a prestar mais atenção à diferença entre atribuição e comparação e à organização dos pontos de decisão nos fluxogramas.

7. **Próximo passo:** Aprofundar meus conhecimentos sobre estruturas condicionais, buscando compreender o que são, como funcionam e de que maneira podem ser utilizadas junto aos operadores lógicos e de comparação. Pretendo aplicar esses conhecimentos futuramente no CRUD de upload de músicas para controlar diferentes situações, verificar condições e permitir que o programa execute operações de acordo com as escolhas do usuário.

## 🟢 CICLO 04 — 02/09 — Estruturas condicionais: `if`, `elif`, `else`

<details>
<summary>📘 Orientações do Ciclo 04</summary>

- **Sem Campo do Protocolo hoje.** Preencha o Registro do Ciclo 04.
- Conecte **cada condicional** do seu CRUD a uma **regra de negócio** (ex.: "preço não pode ser negativo").
- Se já recebeu o lote de dados com defeito, procure **qual registro quebra qual condição** e registre o item 4 com a **causa técnica** (ex.: valor `None`, texto vazio, número negativo, divisão por zero).
- No item 5, cite a fonte da decisão: livro (*Pense em Python*), documentação ou exercício que você resolveu.
- Compare com o **Campo 02**: o desvio de hoje já estava previsto no seu dimensionamento?
</details>

#### Registro do Ciclo 04 — 02/09
1. **Desafio do ciclo (em 1 frase):** Compreender o funcionamento das estruturas condicionais if, elif e else em Python, aprendendo a combiná-las com operadores de comparação para controlar diferentes situações durante a execução de um programa.

2. **O que implementei (commits / arquivos / links):** Durante as atividades relacionadas ao ciclo, reutilizei o arquivo Identificador2608.py, desenvolvido anteriormente, realizando modificações para aplicar os conhecimentos sobre estruturas condicionais if, elif e else. Utilizei essas estruturas junto ao operador de comparação == para verificar determinadas condições e apresentar resultados de acordo com os valores analisados. Após as modificações, consegui executar o programa. Essa atividade me permitiu praticar a lógica de decisão em Python e compreender melhor como as estruturas condicionais controlam o fluxo de execução de um programa. O arquivo já existia antes deste ciclo, sendo utilizado novamente para aprofundar meus conhecimentos. Essas alterações ainda não representavam a implementação das estruturas condicionais no CRUD de upload de músicas.
Repositório: https://github.com/SantX0/AlgoritimosUNDB

3. **Objeto(s) de conhecimento mobilizado(s):** Os principais objetos de conhecimento foram estruturas condicionais, operadores de comparação, expressões booleanas e indentação de blocos de código. Aprendi que if executa um bloco quando uma condição é verdadeira, elif permite verificar condições alternativas e else executa um bloco quando nenhuma das condições anteriores é atendida. Também compreendi como combinar operadores de comparação, como == e !=, com estruturas condicionais para construir expressões que resultam em True ou False. Outro conhecimento importante foi a indentação, responsável por delimitar os blocos de código em Python e indicar quais instruções pertencem a cada estrutura condicional.

4. **Desvio ou erro encontrado + causa técnica:** Minha principal dificuldade foi organizar corretamente a indentação dos blocos condicionais. Em algumas situações, acabava deixando o print() sem o recuo necessário após uma estrutura if, provocando um IndentationError. Esse erro acontecia porque Python utiliza a indentação para identificar quais instruções pertencem a um bloco. Quando um if termina com dois-pontos, o interpretador espera que o corpo da estrutura esteja corretamente indentado. Essa dificuldade mostrou que a organização dos blocos não é apenas uma questão visual, mas também uma exigência da sintaxe da linguagem.
5. **Decisão de ajuste + fonte:** Para corrigir os problemas de indentação, decidi praticar a construção de estruturas if, elif e else, criando o hábito de utilizar a tecla Tab após iniciar um bloco condicional e verificar se as instruções estavam alinhadas corretamente. Essa prática me ajudou a compreender melhor a organização dos blocos e a evitar erros causados pela ausência de recuo. A decisão está relacionada aos conceitos de indentação, sintaxe e controle de fluxo, pois a estrutura correta do código é necessária para que o interpretador consiga identificar e executar as instruções pertencentes a cada condição.
Fonte: Orientações do professor Rondineli durante as aulas de Algoritmos e Programação, principalmente sobre a importância da indentação, da organização dos blocos e das boas práticas na escrita de estruturas condicionais.

6. **Feedback recebido e o que mudei:** Não relatei feedback individual específico sobre meu código neste ciclo, mas o professor Rondineli apresentou orientações gerais sobre a importância de manter os blocos condicionais organizados e corretamente indentados. A partir dessas explicações, passei a prestar mais atenção ao alinhamento das instruções dentro de if, elif e else, buscando evitar erros de sintaxe e melhorar a organização do código.

7. **Próximo passo:** Pensar em maneiras de aplicar as estruturas condicionais no CRUD de upload de músicas, combinando if, elif e else com operadores de comparação para controlar diferentes situações e escolhas do usuário. Naquele momento, ainda não imaginava utilizar condicionais aninhadas no projeto, pois meu foco estava em compreender e aplicar corretamente a lógica condicional básica.

---

# 🟠 GRUPO 2 — prazo sábado 21/11 às 23h59

> **Janela:** segunda 16/11 → sábado 21/11. **O que entregar:** Registros dos Ciclos 05, 06, 07 e 08 · Checkpoint Conceitual · Campo 03 · Campo 04.
>
> ⚠️ O prazo cai num **sábado**: planeje terminar na sexta. Os campos do Ciclo 03 (Checkpoint, 03 e 04) aparecem **primeiro**, porque são a base da investigação.

**Checklist do Grupo 2**
- [ ] Checkpoint Conceitual feito conforme orientação do professor (20 min, sem consulta)
- [x] Campo 03: 2 achados com objeto, 1 desvio com causa técnica, 1 decisão com fonte
- [x] Campo 04: ferramenta, pergunta íntegra, resumo, o que aceitei e o que questionei
- [x] Registros dos Ciclos 05, 06, 07 e 08 com os 7 itens (devolutiva da P1 no ciclo 06)
- [x] Commits no GitHub e painel atualizado

## 🟠 CICLO 03 (campos) — 26/08 — Checkpoint, Campo 03 e Campo 04

<details>
<summary>📘 Orientações — Checkpoint, Campo 03 e Campo 04 (referentes ao Ciclo 03)</summary>

**Checkpoint Conceitual** · *20 min · sem consulta · conforme orientação do professor*
- Verifica o **seu domínio individual** do conteúdo — não avalia a sua solução. São **3 questões dissertativas**. Quem investiu por conta própria responde com segurança.
- Respostas **genéricas, sem ancoragem técnica, não são aceitas**. Defina o objeto **e** relacione-o ao problema do seu CRUD, explicitando as implicações.
- Critérios: *precisão conceitual*, *relação conteúdo-problema*, *qualidade do raciocínio*.
- Se for insatisfatório, você recebe **feedback escrito em até 48h** e deve ajustar a investigação antes da avaliação somativa.
- Se o professor aplicar o Checkpoint via GitHub, use o arquivo abaixo **só durante os 20 minutos**, com um único commit ao final.

**Campo 03 — Execução e desvios** · *sábado 21/11, 23h59*
- **3a.** Pelo menos **2 achados** que mudaram sua compreensão do problema, cada um com o **objeto de conhecimento** associado.
- **3b.** Pelo menos **1 desvio** em relação ao Campo 02 (o que você planejou e não aconteceu) e a **causa técnica** — não vale "falta de tempo".
- **3c.** Pelo menos **1 decisão de ajuste**, com justificativa e **fonte**, e o objeto de conhecimento mobilizado.

**Campo 04 — Interação com IA** · *sábado 21/11, 23h59 · obrigatório e avaliado*
- Registre **pelo menos uma** interação real com uma IA sobre o seu CRUD.
- **4b.** Transcreva a pergunta **na íntegra** (copie e cole).
- **4c.** Resuma a resposta em **um parágrafo** com as suas palavras.
- **4d.** O que você **aceitou**, ligando ao objeto de conhecimento.
- **4e.** O que você **questionou ou descartou**, com **argumento técnico ou fonte** (teste, documentação, livro). Dica: **rode o código** que a IA sugeriu antes de decidir.
- **Print sem análise crítica = devolução imediata.** Se você aceitou tudo, volte e procure o que verificar.
</details>

### 🧩 CHECKPOINT CONCEITUAL INDIVIDUAL
*20 minutos · sem consulta a qualquer fonte, material ou colega · conforme orientação do professor.*

| | |
|---|---|
| **Nome do estudante** | _…_ |
| **Data de realização** | _…_ |
| **Unidade curricular** | Algoritmos e Programação |
| **Professor(a)** | Rondineli Seba Salomão |

> **INSTRUÇÕES:** Responda individualmente, sem consulta. Você tem 20 minutos. As questões avaliam seu domínio dos objetos de conhecimento do componente — não sua solução para o problema. Respostas genéricas sem ancoragem técnica não são aceitas.

**QUESTÃO 1** — Objeto de conhecimento: _…_
> _(Questão elaborada pelo professor na Proposta — Apêndice A, item 6)_

**RESPOSTA:**

> _…_

**QUESTÃO 2** — Objeto de conhecimento: _…_
> _(Questão elaborada pelo professor na Proposta — Apêndice A, item 6)_

**RESPOSTA:**

> _…_

**QUESTÃO 3** — Objeto de conhecimento: _…_
> _(Questão elaborada pelo professor na Proposta — Apêndice A, item 6)_

**RESPOSTA:**

> _…_

<details>
<summary>🔒 Uso do professor — critérios de avaliação do Checkpoint</summary>

| CRITÉRIO | SATISFATÓRIO | INSATISFATÓRIO |
|---|---|---|
| **Precisão conceitual** | Domínio do objeto de conhecimento, com vocabulário técnico adequado e sem erros conceituais relevantes. | Resposta vaga, com erros conceituais ou sem ancoragem nos objetos de conhecimento do componente. |
| **Relação conteúdo-problema** | Conecta o objeto de conhecimento ao problema trabalhado na AFP. | Responde o objeto de forma isolada, sem relação com o problema do ciclo. |
| **Qualidade do raciocínio** | Raciocínio técnico articulado: relaciona o objeto ao problema e explicita implicações para a investigação. | Apenas define o objeto, sem articular raciocínio ou relação com o problema investigado. |

**RESULTADO:** ☐ Satisfatório ☐ Insatisfatório
**AÇÃO DO PROFESSOR:** Checkpoint insatisfatório gera feedback escrito individualizado até 48h — o aluno ajusta a investigação antes da avaliação somativa.
</details>

### 🧩 CAMPO 03 — Execução e desvios
*AV Qualis — Grupo 2 | Sábado 21/11, 23h59*

**3a. O que descobri que mudou minha compreensão do problema (mínimo 2 achados, com objeto de conhecimento associado):**
1. Compreendi que as listas permitem armazenar vários elementos de maneira ordenada e dinâmica, possibilitando adicionar, acessar e remover registros. Esse conhecimento contribuiu para organizar as músicas cadastradas e trabalhar com múltiplos registros dentro do CRUD. — *Objeto de conhecimento:* Listas em Python
2. Aprendi que os dicionários permitem associar chaves a valores, facilitando a organização e o acesso às informações de cada música. Esse conhecimento contribuiu para compreender como identificar e consultar atributos dos registros, como nome, autores, produtores e gênero. — *Objeto de conhecimento:* Dicionários em Python
3. _…_ *(opcional)*

**3b. Desvio em relação ao Campo 02 (ao menos 1 — causa técnica):**
- **Desvio:** No Campo 02, planejei utilizar cinco registros de músicas e realizar oito testes para verificar o funcionamento do CRUD. Entretanto, durante a execução, decidi não criar os cinco registros inicialmente previstos, pois considerei essa quantidade desnecessária para as verificações que estava realizando. Mantive os oito testes, executados manualmente no VS Code.
- **Causa técnica:** O desvio ocorreu porque considerei desnecessário cadastrar cinco músicas para verificar as funcionalidades do CRUD. Minha avaliação inicial foi de que poderia testar as operações utilizando uma quantidade menor de registros, sem considerar que isso reduziria a variedade de situações verificadas, principalmente nas operações de busca, atualização e exclusão com múltiplas músicas cadastradas.

**3c. Decisão de ajuste (ao menos 1) com justificativa e fonte:**
- **Decisão:** Uma das principais dificuldades que encontrei foi utilizar corretamente o comando break dentro dos laços while. Inicialmente, colocava o break em várias partes do programa, fazendo com que o menu fosse encerrado imediatamente após o cadastro de uma música. Para corrigir esse problema, ajustei a utilização do break, compreendendo que esse comando interrompe o laço em que está inserido e não deve ser utilizado indiscriminadamente após cada operação. Após essa correção, consegui manter o menu funcionando depois do cadastro, permitindo que o usuário continuasse utilizando o CRUD. Também compreendi que o break pode ser utilizado para interromper um laço de busca quando o resultado desejado é encontrado ou para encerrar o menu quando o usuário seleciona a opção de saída.
Justificativa técnica: Ajustei o uso do comando break para evitar o encerramento antecipado do laço responsável pelo menu principal. Essa correção permitiu que o usuário continuasse executando diferentes operações do CRUD sem precisar reiniciar o programa após cada cadastro.
- **Fonte:** Orientações do professor Rondineli durante a aula sobre laços de repetição e o livro Pense em Python, capítulo 7, seção 7.4, utilizados para aprofundar meus conhecimentos sobre o funcionamento dos laços de repetição e do comando break.

**Objeto de conhecimento mobilizado nesta decisão:** Laços de repetição while, comando break e controle do fluxo de execução.

### 🧩 CAMPO 04 — Interação com IA
*AV Qualis — Grupo 2 | Sábado 21/11, 23h59 | OBRIGATÓRIO*

> **Obrigatório e avaliado. Print sem análise crítica = devolução imediata. Reproduzir a IA sem questionamento = reprovado.**

**4a. Ferramenta:** Verdent, utilizando o modelo de inteligência artificial GPT, da OpenAI.  **Data:** 13/09/2026.

**4b. Pergunta formulada (transcrita integralmente):**

> O meu programa após completar alguma terminar alguma ação dos menus simplesmente fechava, como posso utilizar o break de forma correta para resolver este problema ? Responda sem codigo

**4c. Resposta da IA (resumida em parágrafo):**

> A IA orientou que, para impedir que o programa encerrasse após cada operação, seria necessário manter o menu principal dentro de um laço contínuo (while) e utilizar o comando break exclusivamente quando o usuário selecionasse a opção de sair.
A orientação buscava permitir que o programa retornasse ao menu principal após a conclusão das operações, sem precisar ser executado novamente.

**4d. O que aceitei — com referência ao objeto de conhecimento do componente:**

> Aceitei a orientação de manter o menu principal dentro de um laço de repetição contínuo, pois compreendi que essa estrutura permitiria ao usuário realizar diferentes operações sem precisar reiniciar o programa.
Também compreendi melhor que o comando break interrompe a execução do laço em que está inserido. Por isso, seu posicionamento precisa considerar qual repetição deve ser encerrada e em qual momento.
Essa orientação contribuiu para minha compreensão dos conceitos de laços de repetição e controle do fluxo de execução.

**4e. O que questionei ou descartei — com argumento técnico ou fonte:**

> Questionei a orientação de utilizar o comando break exclusivamente na opção de sair.
Entendi que essa afirmação era muito restritiva, pois o break também pode ser utilizado para interromper outros laços quando uma condição específica é atingida, como encerrar uma repetição de busca depois que o resultado desejado foi encontrado.
O ponto técnico é que o break interrompe somente o laço mais interno em que está inserido. Portanto, sua utilização depende da organização dos laços e do comportamento esperado do programa.
Assim, considerei adequada a recomendação para o menu principal, mas não a interpretação de que o comando deveria ser utilizado exclusivamente para encerrar o programa.
Objeto de conhecimento: Laços de repetição while, estruturas condicionais e comando break. Fundamentação: Compreensão do funcionamento do comando break e de sua relação com o laço em que está inserido. Não consultei uma fonte externa adicional para verificar a resposta da IA nessa interação.

## 🟠 CICLO 05 — 09/09 — Condicionais aninhadas e operadores lógicos

<details>
<summary>📘 Orientações do Ciclo 05</summary>

- **Sem Campo do Protocolo hoje.** Preencha o Registro do Ciclo 05.
- Registre **qual combinação de condições** (`and`, `or`, `not`) você precisou e **por que** uma condicional aninhada ou um operador lógico foi a melhor escolha.
- Descreva **pelo menos um caso de teste** que você usou para provar a lógica (entrada → resultado esperado → resultado obtido).
- **Atenção à P1 (23/09):** reveja o Logbook até aqui. Complete itens em branco e confirme se os commits estão em dia.
- Na semana de 16/09 (Nivelamento / Peer Instruction), reserve 10 minutos para atualizar este arquivo.
</details>

#### Registro do Ciclo 05 — 09/09
1. **Desafio do ciclo (em 1 frase):** Compreender como utilizar estruturas condicionais aninhadas em Python, aplicando um if dentro de outro if para realizar verificações mais específicas e utilizar essa lógica no desenvolvimento do CRUD de músicas.

2. **O que implementei (commits / arquivos / links):** Durante este ciclo, trabalhei com estruturas condicionais aninhadas na funcionalidade de busca por ID do meu CRUD de upload de músicas inspirado no Spotify.
Na implementação, utilizei condições para verificar a opção de busca selecionada pelo usuário e analisar o identificador informado, buscando localizar uma música entre os registros cadastrados.
Na versão atual do código, essa funcionalidade utiliza isdigit() para verificar a entrada antes de convertê-la para int, além da variável posicao_encontrada, inicializada com -1, para controlar a localização do registro.
Essa atividade me permitiu relacionar o conteúdo sobre condicionais aninhadas com uma funcionalidade do projeto.
Repositório: https://github.com/SantX0/AlgoritimosUNDB

3. **Objeto(s) de conhecimento mobilizado(s):** Os principais objetos de conhecimento foram estruturas condicionais aninhadas, operadores de comparação, operadores lógicos, validação de entradas e controle de fluxo.
Compreendi que as condicionais aninhadas permitem realizar uma segunda verificação dentro de uma condição anterior, funcionando como uma sequência de verificações.
Na busca por ID, esse conhecimento se relaciona à necessidade de verificar a opção escolhida pelo usuário e analisar se o identificador informado possui um formato adequado antes de realizar a busca.
Também aprofundei minha compreensão sobre como a ordem das condições influencia o comportamento do programa. Os operadores lógicos and, or e not já eram conhecimentos com os quais eu tinha maior familiaridade, enquanto meu foco principal estava na organização das condicionais aninhadas.

4. **Desvio ou erro encontrado + causa técnica:** Minha principal dificuldade foi organizar corretamente as estruturas condicionais aninhadas na funcionalidade de busca por ID do CRUD.
Durante a implementação, o programa informava que a música não existia, mesmo quando ela já estava cadastrada. Esse comportamento demonstrava que a lógica de busca não estava identificando corretamente o registro procurado.
A dificuldade estava relacionada à organização das verificações condicionais e ao controle de fluxo. Entretanto, não consegui identificar com precisão qual condição específica provocava o resultado incorreto na versão anterior do código.

5. **Decisão de ajuste + fonte:** ara reduzir problemas nas condições aninhadas da busca por ID, procurei aplicar práticas de programação defensiva, utilizando verificações para tratar entradas inválidas e organizar melhor o fluxo de execução.
Na versão atual do código, utilizei isdigit() para verificar se o identificador informado contém apenas dígitos antes de convertê-lo para int. Também defini o valor inicial de posicao_encontrada como -1 e utilizei um bloco else para continuar a operação quando a entrada atendesse à validação.
Essa organização permite separar o tratamento de uma entrada inválida do caminho normal da busca. Entretanto, não consigo afirmar qual alteração específica corrigiu o problema de resultados incorretos que ocorreu anteriormente.
Fonte: MCCONNELL, Steve. Code Complete. 2ª edição. Capítulo 8 — Defensive Programming, p. 196; capítulo 15 — Using Conditionals, p. 356.

6. **Feedback recebido e o que mudei:** Não recebi feedback individual específico sobre o CRUD neste ciclo.
Durante a aula, o professor Rondineli apresentou explicações gerais sobre estruturas condicionais aninhadas e lógica, contribuindo para minha compreensão de como organizar diferentes verificações dentro de um programa.
A partir dessas explicações e da prática no projeto, passei a prestar mais atenção à organização das condições e à importância de verificar os valores recebidos antes de utilizá-los nas operações de busca.

7. **Próximo passo:** Continuar praticando a utilização das estruturas condicionais aninhadas no CRUD, buscando compreender melhor como organizar as verificações necessárias para o funcionamento das buscas.
Também pretendia aprofundar meus conhecimentos sobre laços de repetição while e for, para permitir a execução de diferentes operações no CRUD sem precisar reiniciar o programa após cada ação.

## 🟠 CICLO 06 — 30/09 — Devolutiva da P1 + repetição: `for`, `while`, `break`, `continue`

<details>
<summary>📘 Orientações do Ciclo 06</summary>

- **Sem Campo do Protocolo hoje.** Preencha o Registro do Ciclo 06.
- Use o item 6 para registrar a **devolutiva da P1**: o que errou e **qual conceito** estava faltando. Esses erros alimentam o **Campo 07c** (conceitos corrigidos). *Anote já, para não esquecer.*
- Registre **por que escolheu `for` ou `while`** em cada laço do seu CRUD (cadastro em lote, listagem, menu).
- Item 4: se um laço ficou infinito ou pulou itens, descreva a **causa técnica** (condição de parada, incremento, `break` fora de lugar).
</details>

#### Registro do Ciclo 06 — 30/09
1. **Desafio do ciclo (em 1 frase):** Compreender o funcionamento dos laços de repetição while e for em Python, aprendendo a controlar repetições com o comando break para aplicar esses conhecimentos no desenvolvimento do CRUD de músicas.

2. **O que implementei (commits / arquivos / links):** Durante as atividades relacionadas ao ciclo, trabalhei com laços de repetição no meu CRUD de upload de músicas inspirado no Spotify.
Utilizei o while para solicitar novamente informações quando o usuário fornecia uma entrada inválida, permitindo que ele corrigisse os dados sem precisar reiniciar o programa.
Também utilizei o for para percorrer as músicas cadastradas, possibilitando acessar os registros armazenados e trabalhar com suas informações.
Essas aplicações contribuíram para compreender melhor como controlar a repetição de instruções e percorrer os dados do sistema.
Repositório: https://github.com/SantX0/AlgoritimosUNDB

3. **Objeto(s) de conhecimento mobilizado(s):** Os principais objetos de conhecimento foram laços de repetição while e for, comando break, condições de parada e controle de fluxo.
Compreendi que o while executa repetidamente um bloco de código enquanto uma condição permanece verdadeira. Esse conhecimento foi importante para entender como solicitar novamente uma informação quando o usuário fornece uma entrada inválida.
Também aprendi que o for permite percorrer os elementos de uma sequência, como uma lista de músicas cadastradas, executando instruções para cada elemento.
Outro conhecimento mobilizado foi o comando break, utilizado para interromper um laço quando uma condição específica é atingida.

4. **Desvio ou erro encontrado + causa técnica:** Minha principal dificuldade foi controlar corretamente os laços de repetição while durante a validação das entradas do usuário no CRUD.
Em algumas situações, mesmo depois de digitar uma informação válida, o programa continuava repetindo a mesma pergunta, impedindo que a execução avançasse para a próxima etapa.

Causa técnica: O problema estava relacionado ao controle da condição de parada do while True, pois esse laço continua executando até encontrar uma instrução que interrompa sua repetição. 

5. **Decisão de ajuste + fonte:** Para lidar com os laços infinitos, aprofundei meus conhecimentos sobre o comando break e sua utilização dentro das estruturas while.
Passei a utilizar o break quando a entrada fornecida pelo usuário atendia aos critérios esperados, permitindo que o programa encerrasse a repetição e avançasse para a próxima etapa.
Essa decisão ajudou a controlar melhor os laços de validação, evitando que a mesma pergunta continuasse sendo apresentada mesmo após o usuário informar um valor válido.

Fonte: Orientações do professor Rondineli durante a aula sobre laços de repetição e o livro Pense em Python, capítulo 7, seção 7.4, conforme a referência que consultei para aprofundar meus conhecimentos sobre repetição.

6. **Feedback recebido (inclui devolutiva da P1) e o que mudei:** Neste ciclo, o professor Rondineli ainda não havia realizado a devolutiva formal da avaliação P1.
Entretanto, durante as aulas, acompanhei as dúvidas apresentadas pelos colegas e as explicações fornecidas pelo professor, utilizando essas orientações gerais para compreender melhor os conteúdos trabalhados.
Não recebi feedback individual específico sobre meu CRUD neste ciclo.

7. **Próximo passo:** Continuar aplicando os laços while e for no CRUD, principalmente para solicitar novamente entradas inválidas e percorrer as músicas cadastradas.
Também pretendia aprofundar meus conhecimentos sobre listas, pois já imaginava utilizá-las para armazenar várias músicas e acessar seus registros por meio de laços for.

## 🟠 CICLO 07 — 07/10 — Listas: armazenamento e iteração

<details>
<summary>📘 Orientações do Ciclo 07</summary>

- **Sem Campo do Protocolo hoje.** Preencha o Registro do Ciclo 07.
- Justifique **por que seus dados cabem em uma lista** e como você os percorre (iteração).
- Item 4: erros típicos — índice fora do intervalo, alterar a lista enquanto percorre, confundir cópia com referência. Registre qual deles aconteceu e a causa técnica.
- Item 3: nomeie as **operações de lista** que usou (adicionar, remover, ordenar, fatiar…).
</details>

#### Registro do Ciclo 07 — 07/10
1. **Desafio do ciclo (em 1 frase):** Aprender a criar listas em Python, armazenar várias músicas e acessar seus elementos por meio de índices, aplicando esses conhecimentos no desenvolvimento do CRUD de músicas.

2. **O que implementei (commits / arquivos / links):** Durante este ciclo, trabalhei com a utilização de listas no meu CRUD de upload de músicas inspirado no Spotify, principalmente na funcionalidade de listagem das músicas cadastradas.
Implementei a listagem dos registros armazenados, utilizando estruturas de repetição para percorrer as músicas e apresentar suas informações.
Para isso, utilizei o for musica in musicas para acessar diretamente cada música cadastrada e o for i in range(len(musicas)) quando precisava trabalhar com os índices da lista.
Essa implementação me ajudou a compreender como armazenar e acessar vários registros dentro de uma mesma estrutura, dando continuidade ao que havia estudado sobre laços de repetição no Ciclo 06.

Repositório: https://github.com/SantX0/AlgoritimosUNDB

3. **Objeto(s) de conhecimento mobilizado(s):** Os principais objetos de conhecimento foram listas, índices, método append(), função len(), função range() e iteração com for.
Compreendi que uma lista permite armazenar vários elementos em uma mesma estrutura e que seus índices representam as posições desses elementos, começando em 0.
Também aprendi que o método append() adiciona um novo elemento ao final da lista e que a função len() retorna a quantidade de elementos armazenados.
Outro conhecimento importante foi entender duas maneiras de percorrer uma lista: diretamente pelos elementos, utilizando for musica in musicas, ou pelas posições, utilizando for i in range(len(musicas)).

4. **Desvio ou erro encontrado + causa técnica:** Minha principal dificuldade foi tentar acessar uma posição inexistente na lista de músicas, provocando o erro IndexError.
Esse problema aconteceu porque eu tentava acessar um índice que ultrapassava os limites da lista.
Compreendi que os índices começam em 0 e que, quando uma lista possui elementos, sua última posição válida corresponde a len(lista) - 1. Portanto, tentar acessar uma posição fora desse intervalo provoca um IndexError.
Essa dificuldade mostrou que eu precisava compreender melhor a relação entre o tamanho da lista e os índices utilizados para acessar seus elementos.

5. **Decisão de ajuste + fonte:** Para resolver minha dificuldade com o erro IndexError, aprofundei meus conhecimentos sobre os limites dos índices das listas em Python.
A partir do estudo, passei a utilizar duas formas de percorrer as músicas cadastradas: for musica in musicas, para acessar diretamente cada registro, e for i in range(len(musicas)), quando precisava trabalhar com as posições da lista.
Compreendi que os índices começam em 0 e terminam em len(lista) - 1. Por isso, percorrer diretamente os elementos ou utilizar range(len(musicas)) ajuda a evitar tentativas de acessar posições inexistentes.

Fonte: DOWNEY, Allen B. Pense em Python: Pense como um cientista da computação. Capítulo 10 Seção 10.1, 10.2 e 10.13 — Listas.

6. **Feedback recebido e o que mudei:** Neste ciclo, não recebi feedback individual específico sobre meu CRUD.
Durante a aula, o professor Rondineli apresentou explicações gerais sobre listas e iteração, contribuindo para minha compreensão de como armazenar vários elementos e acessar suas posições.
Com o conteúdo estudado e a prática no CRUD, passei a prestar mais atenção aos limites dos índices para evitar erros ao percorrer as músicas cadastradas.

7. **Próximo passo:** Continuar desenvolvendo o CRUD utilizando listas e identificadores para organizar e localizar as músicas cadastradas.
Meu objetivo era aplicar os conhecimentos sobre índices e iteração nas funcionalidades de busca, relacionando cada música ao seu ID.
Naquele momento, não considerava necessário utilizar dicionários ou matrizes, pois pretendia continuar trabalhando com listas para organizar os registros do projeto.

## 🟠 CICLO 08 — 14/10 — Busca/consulta e introdução a dicionários e matrizes

<details>
<summary>📘 Orientações do Ciclo 08</summary>

- **Sem Campo do Protocolo hoje.** Preencha o Registro do Ciclo 08.
- Explique **por que cada item do seu catálogo virou um dicionário** (chave → valor) em vez de uma lista de valores soltos.
- Item 4: registre **qual busca falhou** (item inexistente, tipo diferente — `"2"` ≠ `2`, chave com maiúscula errada) e a causa técnica.
- Se usou o lote de dados defeituoso, registre **qual registro** quebrou a busca.
- Item 5: cite a fonte (*Pense em Python*, cap. 11, ou outra).
</details>

#### Registro do Ciclo 08 — 14/10
1. **Desafio do ciclo (em 1 frase):** Aprender a realizar buscas em listas utilizando índices e identificadores, compreender o funcionamento dos dicionários e conhecer os conceitos iniciais de matrizes para continuar desenvolvendo o CRUD de músicas.

2. **O que implementei (commits / arquivos / links):** Durante este ciclo, trabalhei no desenvolvimento das funcionalidades de busca do meu CRUD de upload de músicas inspirado no Spotify.
Utilizei listas, índices e identificadores para localizar os registros cadastrados, aplicando laços de repetição e estruturas condicionais para verificar se uma música correspondia ao critério procurado.
Essa atividade deu continuidade ao Ciclo 07, no qual havia trabalhado com a listagem das músicas. Agora, meu objetivo era não apenas percorrer os registros, mas também localizar uma música específica.
Repositório: https://github.com/SantX0/AlgoritimosUNDB

3. **Objeto(s) de conhecimento mobilizado(s):** Os principais objetos de conhecimento foram listas, índices, identificadores (IDs), busca sequencial, laços for e estruturas condicionais if, elif e else.
Compreendi que posso utilizar o for para percorrer os elementos de uma lista e aplicar condições para verificar se determinado registro corresponde à informação procurada.
Também comecei a compreender melhor a diferença entre índices e identificadores. O índice representa a posição de um elemento na lista, enquanto o ID funciona como um código utilizado para identificar uma música cadastrada.
Durante a aula, também estudei o funcionamento dos dicionários e tive uma introdução às matrizes. Entretanto, optei por continuar utilizando listas na implementação do CRUD.

4. **Desvio ou erro encontrado + causa técnica:** Minha principal dificuldade foi diferenciar o ID de uma música da posição que ela ocupava na lista durante a implementação da funcionalidade de busca do CRUD.
Ao tentar buscar uma música cadastrada, o programa acessava uma música diferente daquela que eu procurava. Isso aconteceu porque eu confundia o identificador do registro com o índice utilizado para acessar os elementos da lista.
Causa técnica: O índice representa a posição de um elemento na lista, começando em 0, enquanto o ID é um identificador associado à música cadastrada. Como esses valores não representam necessariamente a mesma informação, utilizar o ID diretamente como índice pode levar ao acesso de um registro diferente do desejado.
Essa dificuldade me ajudou a compreender que, para localizar uma música corretamente, precisava percorrer os registros e comparar o ID informado com o identificador armazenado em cada música, em vez de considerar que o ID correspondia à sua posição na lista.

5. **Decisão de ajuste + fonte:** Para superar essa dificuldade, procurei compreender melhor a diferença entre os índices das listas e os identificadores das músicas cadastradas.
Decidi continuar utilizando listas no CRUD, pois precisava de uma estrutura dinâmica, que permitisse adicionar registros e percorrê-los durante as operações do sistema.
Também compreendi que a posição de uma música na lista não deve ser confundida com seu ID. Por isso, nas operações de busca, passei a percorrer os registros e comparar o identificador informado com o ID armazenado em cada música, sem depender exclusivamente de sua posição na lista.
Mesmo tendo estudado dicionários, considerei que as listas eram suficientes para a estrutura que estava desenvolvendo naquele momento.

Fonte: DOWNEY, Allen B. Pense em Python: Pense como um cientista da computação. Capítulo 10 — Listas; explicações do professor Rondineli durante a aula sobre buscas e estruturas de dados.

6. **Feedback recebido e o que mudei:** Neste ciclo, não recebi feedback individual específico sobre meu CRUD.
Durante a aula, o professor Rondineli apresentou explicações gerais sobre listas, buscas e dicionários, contribuindo para minha compreensão das diferentes formas de organizar e localizar dados.
A partir do conteúdo estudado, passei a prestar mais atenção à diferença entre os índices e os IDs, principalmente ao desenvolver as funcionalidades de busca do CRUD.

7. **Próximo passo:** Continuar aplicando listas e identificadores no CRUD, aprimorando a organização e a localização das músicas cadastradas.
Também pretendia desenvolver as funcionalidades de atualização e exclusão, permitindo editar ou remover registros existentes.
Para isso, precisava aprofundar meu entendimento sobre como localizar corretamente uma música pelo seu ID e acessar sua posição na lista antes de realizar alguma alteração.

---

# 🔵 GRUPO 3 — prazo quinta 26/11 às 23h59

> **Janela:** sábado 21/11 → quinta 26/11. **O que entregar:** Registros dos Ciclos 09, 10, 11 e 12 · Campo 05 (duas revisões por pares) · Campo 06 · Campo 07.
>
> ⚠️ O prazo vem **um dia depois da P2 (25/11)**. Os Campos 06 e 07 dependem de todo o Logbook: deixe-os para o final, mas **adiante o rascunho do 6c e do 7a/7b antes da Defesa (18/11)**.

**Checklist do Grupo 3**
- [x] Registros dos Ciclos 09, 10, 11 e 12 com os 7 itens
- [x] Campo 05: duas revisões (Ciclos 09 e 12), blocos 5a a 5e
- [x] Campo 06: decisão autônoma, lacuna com plano, pergunta da banca com 5 linhas ou mais
- [ ] Campo 07: 7a a 7e, com 3 objetos, 2 equívocos corrigidos e transferência
- [ ] Coerência entre Campo 01 e Campo 07
- [ ] Painel de acompanhamento completo

## 🔵 CICLO 09 — 21/10 — Atualização e exclusão: CRUD completo

<details>
<summary>📘 Orientações do Ciclo 09 — Registro + Campo 05 (revisão por pares nº 1)</summary>

- Neste ciclo seu CRUD ficou **completo** (Create, Read, Update, Delete). Preencha o Registro do Ciclo 09.
- **Item 4:** *atualizar* ou *excluir* item inexistente, e excluir durante um laço (a lista muda de tamanho e itens são pulados) são erros comuns.
- **Campo 05 — Registro de Revisão por Pares.** Você passa a ser **revisor** do CRUD de um colega.
  - Cada revisão tem **um registro** (copie a seção do Campo 05) com o nome e o link do repositório revisado.
  - **Revise o processo, não só o código:** o que foi decidido, em que objeto de conhecimento se apoia, com que fonte.
  - **5a:** liste as etapas da revisão (ex.: rodar o CRUD, testar com o lote de dados com defeito, ler o código, registrar achados, devolver feedback).
  - **5b:** liste os insumos que usou (lote de dados, casos de teste, `requisitos.md`) com quantidade planejada, utilizada e variação.
  - **5c:** diga se a solução do colega atende ao critério (Sim/Parcialmente/Não) e **qual critério** usou (ex.: requisito do `requisitos.md`).
  - **5d:** riscos da revisão (ex.: não conseguir rodar o código do colega) e como mitigou.
  - **5e:** registre **cada decisão técnica** da revisão com **data, responsável, objeto de conhecimento e fundamentação/referência**. *Sem objeto e sem referência, não é rastreável.*
  - Feedback ao colega: **específico e respeitoso** (o que está bom, o que quebrou, como reproduzir, sugestão).
</details>

#### Registro do Ciclo 09 — 21/10
1. **Desafio do ciclo (em 1 frase):** Aprender a atualizar as informações das músicas já cadastradas e excluir registros da lista, aplicando os conhecimentos sobre índices, identificadores e busca no CRUD.

2. **O que implementei (commits / arquivos / links):** Durante este ciclo, implementei as funcionalidades de atualização e exclusão de músicas no meu CRUD.
Na atualização, desenvolvi a possibilidade de o usuário escolher quais atributos de uma música cadastrada deseja modificar, sem precisar alterar todo o registro.
Nas duas funcionalidades, utilizei a busca pelo ID para localizar a música antes de realizar qualquer alteração.
Para a exclusão, utilizei o método pop() para remover o registro da lista, juntamente com uma confirmação do usuário para evitar exclusões acidentais.

Repositório: https://github.com/SantX0/AlgoritimosUNDB

3. **Objeto(s) de conhecimento mobilizado(s):** Os principais objetos de conhecimento foram listas, índices, atribuição de valores, método pop(), busca por ID e estruturas condicionais if e else.
Compreendi que é possível atualizar um atributo de uma música acessando sua posição na lista e atribuindo um novo valor, sem precisar substituir todo o registro.
Também aprendi que o método pop() remove um elemento de uma lista e retorna o valor removido, modificando a estrutura original.
Utilizei a busca por ID para localizar corretamente a música cadastrada, evitando que o usuário modificasse ou excluísse um registro diferente do desejado.
Além disso, utilizei as estruturas condicionais if e else para controlar a confirmação da exclusão, funcionando como uma medida de segurança para evitar que uma música fosse apagada acidentalmente.

4. **Desvio ou erro encontrado + causa técnica:** Minha principal dificuldade foi utilizar corretamente o método pop() durante a implementação da funcionalidade de exclusão de músicas no CRUD.
Durante a implementação, utilizei o método pop() em uma lista diferente daquela que deveria ser modificada, removendo um dado da estrutura incorreta.
Causa técnica: O método pop() modifica diretamente a lista sobre a qual é chamado. Ao utilizar a variável correspondente a outra lista, a remoção ocorreu na estrutura errada, em vez de acontecer na lista que armazenava o registro que eu desejava excluir.
Essa dificuldade me ajudou a compreender a importância de identificar corretamente a lista e o índice antes de realizar uma operação de exclusão.

5. **Decisão de ajuste + fonte:** Para corrigir o problema na funcionalidade de exclusão do CRUD, ajustei a variável da lista na qual o método pop() estava sendo chamado, permitindo que a remoção acontecesse na estrutura que armazenava as músicas cadastradas.
Compreendi que o método pop() modifica diretamente a lista sobre a qual é chamado. Por isso, é necessário identificar corretamente tanto a lista quanto o índice do elemento que será removido.

Fonte: Explicações do professor Rondineli durante a aula sobre os recursos e métodos disponíveis em Python para facilitar a manipulação de listas.

6. **Feedback recebido e o que mudei:** Neste ciclo, não recebi feedback individual específico sobre meu CRUD, apenas acompanhei as explicações gerais do professor Rondineli durante a aula.
Essas explicações contribuíram para minha compreensão dos métodos disponíveis em Python para manipular listas, principalmente a utilização do pop().
A partir desse conhecimento, corrigi a variável da lista na qual estava utilizando o método de exclusão, evitando remover dados de uma estrutura incorreta.

7. **Próximo passo:** Pretendia aprofundar meus conhecimentos sobre funções em Python, aprendendo a utilizar a palavra-chave def para definir funções e reduzir a repetição de código no CRUD.
Apesar de considerar meu código relativamente bem organizado naquele momento, acreditava que a utilização de funções poderia contribuir para reduzir a duplicação de instruções, facilitar a manutenção e permitir a reutilização de trechos de código em diferentes operações do sistema.

### 🧩 CAMPO 05 — Registro de Revisão por Pares
*Adaptação do **Logbook do Time** (Apêndice C) para o CRUD individual. Documento atualizado pelo **revisor**. Cada decisão técnica relevante deve ter associado o objeto de conhecimento correspondente.*

> ⚠️ **Nota de adaptação:** o Apêndice C original prevê Gestor, Responsável Técnico, Analista de Qualidade e Comunicador. Como o CRUD é **individual** e os alunos atuam como **revisores**, mantive os blocos 5a a 5e e troquei os papéis por **Autor** (dono do CRUD) e **Revisor** (você). *Pendente de validação do professor/NDE.*

> **O Logbook de revisão é um registro de conhecimento em ação.** Cada decisão técnica relevante deve estar associada ao objeto de conhecimento que a fundamenta, à justificativa técnica e à referência utilizada. Registros sem esse vínculo não são aceitos.

#### Revisão nº 1

| | |
|---|---|
| **Autor do CRUD revisado** | Davi Gael Lopes |
| **Repositório revisado** | https://github.com/deuspato/PriVer |
| **Revisor** | Marcos Oliveira Ferreira |
| **Unidade curricular / Semestre** | Algoritmos e Programação · 2026.2 |
| **Ciclo / data** | _Ciclo 09 · 24/10_ |

**5a. AVANÇO DO PROCESSO DE REVISÃO — análise técnica de cada etapa:**

| ETAPA DO PROCESSO | RESPONSÁVEL | PRAZO | STATUS | DESVIO / JUSTIFICATIVA |
|---|---|---|---|---|
| 1. Acessar o repositório e verificar a documentação | Revisor | _24/11_ | ☑ Concluída ☐ Em andamento ☐ Com desvio | README vazio e ausência do arquivo requisitos.md na raiz do repositório. |
| 2. Analisar o código-fonte main.py | Revisor | _24/11_ | ☑ Concluída ☐ Em andamento ☐ Com desvio | Nenhuma dificuldade encontrada durante a leitura do código. |
| 3. Executar o CRUD e realizar os casos de teste | Revisor | _24/11_ | ☑ Concluída ☐ Em andamento ☐ Com desvio | Foram avaliados 11 casos de teste, sendo 8 aprovados, 1 aprovado com ressalvas e 2 reprovados. Foram identificadas quatro falhas distintas. |
| 4. Registrar as falhas e elaborar sugestões de melhoria | Revisor | _24/11_ | ☑ Concluída ☐ Em andamento ☐ Com desvio | Foram identificadas as causas técnicas das falhas e propostas sugestões de melhoria. |
| 5. Apresentar o feedback ao autor | Revisor | _25/11_ | ☑ Concluída ☐ Em andamento ☐ Com desvio | Feedback enviado em 24/11, antes do prazo planejado. O autor respondeu na mesma data, mas ainda não apresentou um posicionamento técnico sobre as sugestões de melhoria. |

**5b. ANÁLISE DE INSUMOS E CRITÉRIOS DE QUALIDADE:**

| RECURSO | QTDE PLANEJADA | QTDE UTILIZADA | VARIAÇÃO | JUSTIFICATIVA TÉCNICA |
|---|---|---|---|---|
| Código-fonte (main.py) | 1 | 1 | 0 | Utilizado para analisar as estruturas de dados, o controle de fluxo e identificar as causas técnicas dos erros encontrados durante a execução do CRUD. |
| Casos de teste | 11 | 11 | 0 | Utilizados para verificar as funcionalidades do CRUD, a validação de entradas e o comportamento do programa diante de situações inválidas. |
| Arquivo de documentação do projeto | 1 | 0 | -1 | O arquivo README.md estava vazio, impossibilitando a comparação das funcionalidades implementadas com os requisitos documentados. Por isso, utilizei as funcionalidades apresentadas pelo próprio programa como critérios de revisão. |

**5c. CONTROLE DE QUALIDADE:**
- **Critério ou norma técnica:** Funcionamento das quatro operações do CRUD (Create, Read, Update e Delete), validação das entradas, tratamento de erros e compatibilidade com o sistema operacional utilizado durante os testes.
- **A solução atende?** ☐ Sim ☑ Parcialmente ☐ Não

**5d. GESTÃO DE RISCOS:**
- **Risco:** A ausência de documentação dos requisitos poderia dificultar a avaliação das funcionalidades do CRUD. Além disso, os problemas de compatibilidade com o Windows e a falta de tratamento de exceções poderiam interromper a execução do programa e comprometer a continuidade dos testes.
- **Estratégia de mitigação:** Utilizei as funcionalidades apresentadas pelo próprio programa e a análise do código-fonte como critérios de revisão. Durante os testes, utilizei um arquivo de teste existente e adaptei o formato do caminho, substituindo as barras invertidas por barras normais. Também reiniciei o programa após os erros de execução, permitindo continuar os testes sem modificar o código original do colega.

**5e. RASTREABILIDADE DAS DECISÕES TÉCNICAS — COM VÍNCULO AO CONTEÚDO:**

| DATA | DECISÃO TÉCNICA | RESP. | OBJETO DE CONHECIMENTO MOBILIZADO | FUNDAMENTAÇÃO / REFERÊNCIA |
|---|---|---|---|---|
| 24/11/26 | Sugerir a utilização de os.name para selecionar o comando de limpeza do terminal conforme o sistema operacional. | Revisor | Módulo os e estruturas condicionais. | A utilização de os.name permite identificar o ambiente do sistema operacional e selecionar o comando adequado. [Documentação oficial do Python — os.](https://docs.python.org/pt-br/3/library/os.html#os.name) |
| 24/11/26 | Sugerir a utilização de try/except para tratar arquivos inexistentes. | Revisor | Tratamento de exceções e manipulação de arquivos. | O tratamento de exceções permite lidar com o FileNotFoundError sem interromper inesperadamente a execução do programa. [Documentação oficial do Python — Erros e exceções.](https://docs.python.org/pt-br/3/tutorial/errors.html) |
| 24/11/26 | Sugerir a utilização de os.path.basename() e os.path.splitext() para extrair o nome e a extensão do arquivo. | Revisor | Strings, manipulação de caminhos e métodos do módulo os. | Essas funções permitem manipular caminhos de acordo com as convenções do sistema operacional, evitando a extração incorreta do nome do arquivo. [Documentação oficial do Python — os.path.](https://docs.python.org/pt-br/3/library/os.path.html) |
| 24/11/26 | Sugerir a reorganização da lógica de cadastro para preservar o nome base atualizado. | Revisor | Dicionários, atribuição de valores e controle de fluxo. | A atribuição de um novo valor a uma chave existente substitui seu valor anterior. Por isso, é necessário controlar quando o nome base deve ser alterado. [Documentação oficial do Python — Dicionários.](https://docs.python.org/pt-br/3/tutorial/datastructures.html#dictionaries) |
| 24/11/26 | Utilizar as funcionalidades apresentadas pelo próprio programa como critérios de avaliação. | Revisor | Operações CRUD, validação de entradas e testes funcionais. | A ausência de documentação preenchida impossibilitou a comparação com os requisitos originais. Utilizei a análise do código-fonte e os 11 casos de teste para avaliar as funcionalidades. Referência: orientações do Logbook AFP 2026.2 sobre revisão por pares. |

> **IMPORTANTE:** Decisão registrada sem objeto de conhecimento associado e sem referência é considerada **não rastreável** e não conta para a avaliação formativa. O vínculo entre processo e conteúdo é obrigatório em todas as decisões relevantes.

## 🔵 CICLO 10 — 28/10 — Modularização: funções

<details>
<summary>📘 Orientações do Ciclo 10</summary>

- **Sem Campo do Protocolo hoje.** Preencha o Registro do Ciclo 10.
- Explique **como dividiu** o CRUD em funções (`cadastrar()`, `buscar()`, `alterar()`, `excluir()`, `listar()`, `menu()`) e **por que** cada função tem aquela responsabilidade.
- Item 4: erros típicos — variável fora de escopo, função sem `return`, parâmetro na ordem errada.
- Compare o código **antes e depois** da refatoração: o que ficou mais claro? Registre no item 6 o feedback do colega que fez a *peer review*.
</details>

#### Registro do Ciclo 10 — 28/10
1. **Desafio do ciclo (em 1 frase):** Aprender a definir funções utilizando def, compreender a diferença entre parâmetros e argumentos e utilizar o return para retornar um valor específico ou um conjunto de dados.

2. **O que implementei (commits / arquivos / links):** Durante este ciclo, estudei o funcionamento das funções em Python separadamente do desenvolvimento do meu CRUD de upload de músicas, o UpSpot.
Ainda não implementei funções próprias no projeto, pois decidi manter a estrutura existente do código enquanto aprofundava meus conhecimentos sobre esse conteúdo.
Apesar de considerar meu código relativamente bem organizado, reconheci que a modularização poderia contribuir para reduzir a repetição de instruções e facilitar sua manutenção.

Repositório: https://github.com/SantX0/AlgoritimosUNDB

3. **Objeto(s) de conhecimento mobilizado(s):** Os principais objetos de conhecimento foram funções, definição com def, parâmetros, argumentos, retorno de valores e modularização.
Compreendi que a palavra-chave def permite definir uma função, reunindo instruções que podem ser executadas quando ela é chamada.
Também aprendi que os parâmetros são definidos na declaração da função e recebem os valores fornecidos durante sua chamada, enquanto os argumentos são os valores passados para esses parâmetros.
Outro conhecimento mobilizado foi o comando return, que permite retornar um resultado e encerrar a execução da função.

4. **Desvio ou erro encontrado + causa técnica:** MMinha principal dificuldade foi diferenciar parâmetros de argumentos e compreender corretamente o funcionamento do return.
Inicialmente, confundia os nomes definidos na declaração de uma função com os valores fornecidos durante sua chamada. Também apresentava dificuldades para compreender como retornar um resultado e utilizá-lo em outra parte do programa.

Causa técnica: Minha dificuldade estava relacionada à compreensão da passagem de valores entre a chamada e a definição de uma função, assim como ao fluxo de execução e retorno dos dados.
Como ainda não havia implementado funções próprias no CRUD, essa dificuldade ocorreu durante o estudo do conteúdo, e não durante a execução do projeto.

5. **Decisão de ajuste + fonte:** Decidi não modularizar meu CRUD naquele momento, pois ainda não compreendia completamente o funcionamento das funções e não havia desenvolvido o hábito de organizar minhas instruções utilizando def.
Optei por manter a estrutura existente enquanto aprofundava meus conhecimentos sobre parâmetros, argumentos e retorno de valores, para posteriormente aplicar esses conceitos de maneira adequada no projeto.

Fonte: Documentação oficial do Python — seção Definindo funções.

6. **Feedback recebido e o que mudei:** Ele identificou alguns problemas, como a opção 7 do menu não estar habilitada e inconsistências relacionadas à diferenciação entre letras maiúsculas e minúsculas (case-sensitivity).
A partir desse feedback, identifiquei pontos que precisam ser aprimorados no projeto. Pretendo corrigir esses problemas e tentar modularizar o código utilizando funções, buscando melhorar sua organização e reduzir a repetição de instruções.
Até a data de preenchimento deste registro (24/11/2026), essas alterações permanecem planejadas.

7. **Próximo passo:** Aprofundar meus conhecimentos sobre a definição e utilização de funções com def, buscando aplicá-las futuramente nas funcionalidades do meu CRUD.
Também pretendo compreender melhor a passagem de parâmetros, o retorno de valores e a reutilização de código, além de iniciar meus estudos sobre recursividade e entender como uma função pode chamar a si mesma.

## 🔵 CICLO 11 — 04/11 — Recursividade

<details>
<summary>📘 Orientações do Ciclo 11 — Registro + Campo 06 (Grupo 3)</summary>

- Preencha o Registro do Ciclo 11 (caso base, chamada recursiva, pilha de execução).
- **Campo 06 — Próximos passos para a defesa** · *individual · quinta 26/11, 23h59*. Prepare-se para a **Defesa Técnica de quarta 18/11**: como o prazo é posterior à defesa, **adiante pelo menos o 6c** (pergunta da banca e resposta) e leve-o para a arguição.
  - **6a.** Uma **decisão técnica que você defende com plena autonomia**: algo que aprendeu e **é exclusivamente seu**, que nenhum colega consegue explicar por você.
  - **6b.** Uma **lacuna técnica real** e um **plano de ação** com passos e datas para saná-la antes da defesa.
  - **6c.** Uma **pergunta que a banca pode fazer** (nível de Avaliação ou Criação) e a sua **resposta fundamentada em, no mínimo, 5 linhas**, com o objeto de conhecimento e a fonte.
  - Dica: leia a **Rubrica de Defesa Técnica** (no Encerramento) e escolha uma pergunta que teste *aplicação*, *evolução* ou *transferência*.
</details>

#### Registro do Ciclo 11 — 04/11
1. **Desafio do ciclo (em 1 frase):** Compreender o funcionamento da recursividade, entender como uma função pode chamar a si mesma, identificar suas condições de parada e diferenciá-la dos laços de repetição.

2. **O que implementei (commits / arquivos / links):** Durante este ciclo, estudei apenas a parte teórica sobre recursividade, buscando compreender seu funcionamento e sua relação com as funções em Python.
Não implementei funções recursivas no meu CRUD de upload de músicas, o UpSpot, pois ainda estava aprofundando meus conhecimentos sobre funções e modularização.
Mantive a estrutura existente do projeto, utilizando os laços de repetição while e for nas funcionalidades que necessitam de repetição e iteração.

Repositório: https://github.com/SantX0/AlgoritimosUNDB

3. **Objeto(s) de conhecimento mobilizado(s):** Os principais objetos de conhecimento foram recursividade, funções, caso base, caso recursivo, retorno de valores e iteração.
Compreendi que a recursividade ocorre quando uma função chama a si mesma para resolver determinado problema.
Também aprendi os seguintes conceitos:
Caso base: condição que permite encerrar as chamadas recursivas.
Caso recursivo: etapa em que a função chama a si mesma para continuar a resolução do problema.
Iteração: execução repetida de instruções por meio de estruturas como while e for, sem a necessidade de chamadas recursivas.

Esses conhecimentos contribuíram para ampliar minha compreensão sobre as diferentes formas de realizar repetições em Python.

4. **Desvio ou erro encontrado + causa técnica:** Minha principal dificuldade foi compreender como funciona o retorno de valores nas chamadas recursivas e diferenciar a recursividade dos laços de repetição.
Apesar de compreender que uma função recursiva chama a si mesma, ainda apresentava dificuldades para entender como os valores retornados por cada chamada contribuíam para o resultado final.

Causa técnica: Minha dificuldade estava relacionada à compreensão do fluxo de execução das chamadas recursivas e do retorno de valores entre essas chamadas, diferentemente dos laços while e for, com os quais já possuía maior familiaridade.
Como estudei apenas a parte teórica neste ciclo, não identifiquei erros de execução relacionados à recursividade no meu CRUD.

5. **Decisão de ajuste + fonte:** Decidi não implementar recursividade no meu CRUD naquele momento, pois ainda não dominava suficientemente o conteúdo, principalmente o funcionamento das chamadas recursivas e o retorno dos valores.
Optei por manter os laços while e for que já utilizava no projeto, enquanto aprofundava meus conhecimentos sobre funções e recursividade.

Fonte: Documentação oficial do Python — Programação Funcional.

6. **Feedback recebido e o que mudei:** Neste ciclo, não recebi feedback individual específico sobre meu CRUD.
Entretanto, as explicações apresentadas durante a aula contribuíram para ampliar minha compreensão sobre funções, recursividade e estruturas de repetição.
Ainda não realizei alterações no código relacionadas a esse conteúdo, mas passei a compreender melhor que existem diferentes formas de realizar operações repetitivas em Python.

7. **Próximo passo:** Pretendia melhorar meu CRUD, corrigindo os erros identificados e começando a modularizar suas funcionalidades por meio de funções.
Também pretendia continuar aprofundando meus conhecimentos sobre funções e retorno de valores, buscando reduzir a repetição de código e melhorar a organização e a qualidade do projeto.

### 🧩 CAMPO 06 — Próximos passos para a defesa
*AV Qualis — Grupo 3 | Individual | Quinta 26/11, 23h59*

**6a. Decisão técnica que defendo com plena autonomia — o que aprendi que é exclusivamente meu e não consigo transferir para nenhum colega:**

> Uma decisão técnica que consigo defender com autonomia é a utilização de IDs para identificar as músicas cadastradas, independentemente de suas posições na lista. Escolhi essa abordagem porque ela facilita a busca das músicas sem que eu precise me preocupar com a posição que cada registro ocupa. Mesmo quando uma música é excluída e os índices dos elementos seguintes mudam, os IDs das demais músicas permanecem os mesmos.

**6b. Lacuna técnica e plano de ação para saná-la:**

- **Lacuna:** Ainda não domino completamente a utilização de funções em Python, principalmente a definição com def, a passagem de parâmetros e argumentos e o uso do return para modularizar meu CRUD.
- **Plano de ação (passos e datas):** 
24/11/2026: Revisar a documentação do Python sobre definição de funções.
25/11/2026: Identificar trechos repetitivos e iniciar a modularização das funcionalidades do CRUD.
26/11/2026: Testar as funcionalidades modificadas e corrigir possíveis erros antes da entrega.

**6c. Pergunta que a banca pode fazer — com resposta fundamentada (mínimo 5 linhas):**

- **Pergunta:** Por que você decidiu utilizar identificadores (IDs) independentes dos índices da lista no seu CRUD e quais problemas poderiam ocorrer nas operações de busca, atualização e exclusão caso utilizasse somente os índices?
- **Resposta:**

> Decidi utilizar IDs independentes dos índices para evitar problemas relacionados à posição dos dados na lista pois o índice representa a posição de uma música, enquanto o ID funciona como um identificador próprio de cada registro e quando uma música é excluída, os índices dos elementos seguintes podem mudar, enquanto seus IDs permanecem os mesmos.

A utilização dos IDs facilita a localização das músicas, pois não preciso me preocupar com a posição que cada registro ocupa na lista. Para realizar a busca, utilizo o laço for e estruturas condicionais para comparar o ID informado pelo usuário com os identificadores das músicas cadastradas. Essa decisão também facilita as operações de atualização e exclusão, reduzindo o risco de modificar ou remover uma música diferente da desejada.

**Objeto de conhecimento mobilizado:** Listas, índices, identificadores, busca sequencial, laços de repetição e estruturas condicionais.
**Fonte:** DOWNEY, Allen B. Pense em Python: Pense como um cientista da computação. Capítulo 10 — Listas; explicações do professor Rondineli durante a aula sobre buscas.

## 🔵 CICLO 12 — 11/11 — Refatoração e qualidade de código

<details>
<summary>📘 Orientações do Ciclo 12 — Registro + Campo 05 (revisão nº 2) + início do Campo 07</summary>

- Preencha o Registro do Ciclo 12. Registre o que revisou: código duplicado, nomes ruins, funções grandes, comentários desnecessários, lógica confusa.
- **Campo 05 — Revisão por pares nº 2.** Foque em **qualidade**: o CRUD do colega resiste aos casos de teste (mínimos, máximos, inválidos, entradas vazias) e ao **lote de dados com defeito**? Use a seção abaixo (copie o bloco *Revisão nº 1* do Ciclo 09 e preencha novamente).
- **Campo 07 — Evolução conceitual** · *individual · quinta 26/11, 23h59.* Comece agora, enquanto a memória do semestre está fresca; leve o rascunho de 7a e 7b para a Defesa de 18/11. Dicas por item:
  - **7a.** Releia o **Campo 01** e resuma o que você *pensava* e *achava que sabia*. Seja honesto, mesmo se o Campo 01 estiver "errado".
  - **7b.** Pelo menos **3 objetos de conhecimento** na tabela: o que você *não dominava*, o que *aprendeu e consegue demonstrar* e a **evidência** (em qual Campo ou ciclo do Logbook aparece).
  - **7c.** Pelo menos **2 equívocos corrigidos**, dizendo **o que os corrigiu** (Fechamento Teórico, pesquisa, *Peer Review*, arguição, devolutiva da P1).
  - **7d.** **Transferência:** um exemplo concreto de aplicar o que aprendeu em um **contexto diferente** do CRUD (outra área do seu curso ou outro tipo de sistema).
  - **7e.** Avaliação honesta do que **ainda não domina** e vai aprofundar.
</details>

#### Registro do Ciclo 12 — 11/11
1. **Desafio do ciclo (em 1 frase):** Melhorar a organização do código, corrigir erros, reduzir instruções duplicadas, aprimorar as validações e modularizar as funcionalidades do CRUD.
2. **O que implementei (commits / arquivos / links):** Realizei a refatoração do meu CRUD, o UpSpot, organizando o código em 21 funções com responsabilidades específicas, buscando reduzir a repetição de instruções e facilitar sua manutenção. Substituí a estrutura de listas de listas por uma lista de dicionários, permitindo identificar os atributos das músicas por meio de chaves descritivas.Utilizei os seguintes módulos da biblioteca padrão do Python:
json: persistência dos dados cadastrados.
calendar: validação de datas.
collections: contagem de elementos nos relatórios.
math: verificação de valores numéricos finitos.
pathlib: manipulação dos caminhos de arquivos.
tempfile: criação de arquivos temporários durante o salvamento dos dados.

Também implementei o tratamento de exceções com try/except, funcionando como uma rede de proteção para capturar determinadas exceções e apresentar mensagens ao usuário. Além disso, aprimorei as validações de entrada com strip() e casefold() e corrigi a estrutura dos relatórios disponibilizados na opção 7 do menu.

3. **Objeto(s) de conhecimento mobilizado(s):** 
Refatoração: melhorar a estrutura interna do código sem alterar seu comportamento esperado.
Legibilidade: facilitar a leitura e a compreensão do código.
Reutilização de código: evitar a duplicação de instruções por meio de funções.
Manutenibilidade: facilitar futuras correções e alterações no sistema.
Validação de dados: impedir que entradas inválidas comprometam o funcionamento do programa.
Modularização: dividir o código em funções com responsabilidades específicas.
Tratamento de exceções: utilizar try/except para tratar determinadas exceções durante a execução.
Persistência de dados: utilizar arquivos JSON para preservar os registros entre diferentes execuções do programa.
Dicionários: organizar os atributos das músicas por meio de pares de chave e valor.

4. **Desvio ou erro encontrado + causa técnica:** Os principais problemas que identifiquei foram a repetição de instruções e a dificuldade de manutenção do código.
A estrutura anterior concentrava as funcionalidades do CRUD no fluxo principal do programa, dificultando a localização de determinadas instruções e a realização de alterações.
Causa técnica: A ausência de modularização e a repetição de trechos de código dificultavam sua reutilização e manutenção. Dessa forma, determinadas alterações exigiam a revisão de diferentes partes do código, tornando o processo mais trabalhoso.

5. **Decisão de ajuste + fonte:** Decidi criar funções com nomes descritivos que representassem tarefas específicas, centralizando a lógica de cada funcionalidade em um único ponto do código.
Também busquei seguir padrões de estilo, nomenclatura clara e organização estrutural, priorizando a simplicidade e a legibilidade em vez de soluções desnecessariamente complexas.

Fontes consultadas:
Tutorial Oficial do Python — Definindo Funções: auxiliou na definição e utilização de funções para modularizar o código.
PEP 8 — Style Guide for Python Code: serviu como referência para a padronização, nomenclatura e organização do código.
PEP 20 — The Zen of Python: orientou a priorização da simplicidade, clareza e legibilidade do código.

6. **Feedback recebido e o que mudei:** No dia 24/11/2026, recebi um feedback do meu colega Davi Gael Lopes, que identificou problemas relacionados ao funcionamento da opção 7 do menu e à diferenciação entre letras maiúsculas e minúsculas em determinadas entradas. A partir desse feedback, corrigi os problemas apontados, além de outras inconsistências relatadas durante a revisão. 

Para corrigir os problemas de diferenciação entre letras maiúsculas e minúsculas, utilizei o método casefold(), permitindo realizar comparações independentemente da capitalização das entradas. Também reorganizei a lógica dos relatórios, implementando a função gerar_relatorio() e integrando-a à opção 7 do menu principal.

Essas orientações contribuíram para melhorar as validações, a organização e o funcionamento do meu CRUD.

7. **Próximo passo:** Considero que as alterações realizadas no último commit do projeto são suficientes para a entrega final do CRUD. Como próximo passo, pretendo realizar uma verificação final das funcionalidades e concluir a documentação do Logbook, registrando minha evolução conceitual e as decisões técnicas tomadas ao longo do semestre.

### 🧩 CAMPO 05 — Registro de Revisão por Pares (revisão nº 2)

| | |
|---|---|
| **Autor do CRUD revisado** | Davi Gael Lopes |
| **Repositório revisado** | https://github.com/deuspato/PriVer |
| **Revisor** | Marcos Oliveira Ferreira |
| **Ciclo / data** | _Ciclo 12 · 24/11_ |

**5a. AVANÇO DO PROCESSO DE REVISÃO:**

| ETAPA DO PROCESSO | RESPONSÁVEL | PRAZO | STATUS | DESVIO / JUSTIFICATIVA |
|---|---|---|---|---|
| 1. Receber a versão atualizada do CRUD. | Autor / Revisor | 24/11 | ☑ Concluída ☐ Em andamento ☐ Com desvio | O autor disponibilizou o código atualizado após a primeira revisão. |
| 2. Comparar as alterações com a versão anterior. | Revisor | 24/11 | ☑ Concluída ☐ Em andamento ☐ Com desvio | Utilizei o ChatGPT como ferramenta de apoio para identificar as correções implementadas. |
| 3. Analisar os casos de teste e as validações. | Revisor | 24/11 | ☑ Concluída ☐ Em andamento ☐ Com desvio | Revisão realizada com auxílio da IA, sem execução pessoal dos testes. |
| 4. Registrar os problemas encontrados e as sugestões de melhoria. | Revisor | 24/11 | ☑ Concluída ☐ Em andamento ☐ Com desvio | Foram identificados problemas relacionados à manipulação de arquivos, tratamento de exceções e controle de versões. |
| 5. Apresentar o feedback ao autor. | Revisor | 25/11 | ☑ Concluída ☐ Em andamento ☐ Com desvio | O feedback foi encaminhado antecipadamente, no dia 24/11. |

**5b. ANÁLISE DE INSUMOS E CRITÉRIOS DE QUALIDADE:**

| RECURSO | QTDE PLANEJADA | QTDE UTILIZADA | VARIAÇÃO | JUSTIFICATIVA TÉCNICA |
|---|---|---|---|---|
| Código-fonte atualizado (main.py) | 1 | 1 | 0 | Utilizado para identificar as correções implementadas e os problemas que permaneceram. |
| ChatGPT | 1 | 1 | 0 | Utilizado como ferramenta de apoio à análise do código, identificação de falhas e elaboração do feedback técnico. |
| Feedback da primeira revisão | 1 | 1 | 0 | Utilizado como referência para verificar se o autor aplicou as recomendações anteriores. |

**5c. CONTROLE DE QUALIDADE:**
- **Critério ou norma técnica:** Funcionamento das operações do CRUD, validação de entradas, tratamento de exceções, integridade dos arquivos, consistência do controle de versões e atendimento às recomendações da primeira revisão.
- **A solução atende?** ☐ Sim ☑ Parcialmente ☐ Não

**5d. GESTÃO DE RISCOS:**
- **Risco:** Encerramento inesperado do programa ao receber caminhos inválidos, falhas durante a renomeação ou gravação de arquivos e sobrescrita de versões anteriores após o reset dos registros.
- **Estratégia de mitigação:** Recomendei ao autor aprimorar a validação dos caminhos e nomes dos arquivos, ampliar o tratamento de exceções com try/except, verificar a existência dos arquivos de destino antes da gravação e atualizar os contadores de versões somente após a confirmação do salvamento.

**5e. RASTREABILIDADE DAS DECISÕES TÉCNICAS — COM VÍNCULO AO CONTEÚDO:**

| DATA | DECISÃO TÉCNICA | RESP. | OBJETO DE CONHECIMENTO MOBILIZADO | FUNDAMENTAÇÃO / REFERÊNCIA |
|---|---|---|---|---|
| 24/11/26 | Recomendar a validação dos caminhos antes da abertura dos arquivos. | Revisor | Condicionais e validação de dados. | [Documentação Python — os.path.isfile().](https://docs.python.org/pt-br/3/library/os.path.html#os.path.isfile) |
| 24/11/26 | Recomendar a validação dos nomes e o tratamento de exceções durante a renomeação dos arquivos. | Revisor | Validação de strings e tratamento de exceções. | [Documentação Python — os.rename().](https://docs.python.org/pt-br/3/library/os.html#os.rename) |
| 24/11/26 | Recomendar a atualização dos contadores somente após o salvamento bem-sucedido.| Revisor | Operadores de atribuição, controle de fluxo e manipulação de arquivos. | [Documentação Python — Leitura e escrita de arquivos.](https://docs.python.org/pt-br/3/tutorial/inputoutput.html#reading-and-writing-files) |
| 24/11/26 | Recomendar a verificação da existência do arquivo de destino para evitar a sobrescrita de versões anteriores. | Revisor | Estruturas condicionais e integridade de dados. | [Documentação Python — os.path.exists().](https://docs.python.org/pt-br/3/library/os.path.html#os.path.exists) |
| 24/11/26 | Recomendar a continuidade da modularização das funcionalidades do CRUD. | Revisor | Funções, modularização, reutilização e manutenibilidade.| [Documentação Python — Definindo funções.](https://docs.python.org/pt-br/3/tutorial/controlflow.html#defining-functions) |

### 🧩 CAMPO 07 — Evolução conceitual
*AV Qualis — Grupo 3 | Individual | Quinta 26/11, 23h59*

*Evidência rastreável de aprendizagem entre o início e o encerramento do ciclo AFP.*

**7a. O que eu pensava no início do ciclo (com base no Campo 01 — registrar a hipótese inicial e os objetos de conhecimento que achava conhecer):**

> _…_

**7b. O que aprendi — conceitos, princípios ou relações técnicas que não dominava no início e que agora consigo explicar com precisão (mínimo 3 objetos de conhecimento):**

| OBJETO DE CONHECIMENTO | O QUE EU NÃO DOMINAVA | O QUE APRENDI E CONSIGO DEMONSTRAR | EVIDÊNCIA (campo do Logbook onde aparece) |
|---|---|---|---|
| _…_ | _…_ | _…_ | _…_ |
| _…_ | _…_ | _…_ | _…_ |
| _…_ | _…_ | _…_ | _…_ |

**7c. Conceitos que precisei corrigir ao longo do ciclo — onde eu estava equivocado e o que o corrigiu (Fechamento Teórico, pesquisa, Peer Review, arguição):**

1. **Equívoco:** _…_ — **Correção:** _…_
   **O que corrigiu:** _…_
2. **Equívoco:** _…_ — **Correção:** _…_
   **O que corrigiu:** _…_

**7d. Transferência — como este aprendizado se aplica a um contexto diferente do problema trabalhado (ao menos 1 exemplo concreto da área de formação):**

> _…_

**7e. Avaliação honesta do próprio percurso — o que ainda não domino e preciso aprofundar após este ciclo:**

> _…_

---

# 🏁 DEFESA TÉCNICA — quarta 18/11

<details>
<summary>📘 Orientações para a Defesa Técnica e preparação</summary>

**A Defesa é antes dos prazos dos Grupos 2 e 3.** Você será arguido sobre o que já estiver registrado e commitado. Priorize, até **terça 17/11**:
- [ ] **Grupo 1 entregue** (prazo 16/11): Identificação, Registros 01 a 04, Campos 01 e 02.
- [ ] **Campo 04 (IA)** e **Campo 03** ao menos em rascunho, para sustentar as perguntas sobre decisões (critérios 2 e 5).
- [ ] **Campo 06c** (pergunta da banca e resposta) e **rascunho de 7a e 7b**, para sustentar a evolução conceitual (critério 3).
- [ ] Registros dos Ciclos já feitos, mesmo que ainda não "entregues" no prazo do grupo.
- [ ] `README.md`, `docs/` e CRUD rodando.
- [ ] Você consegue explicar **cada linha** do seu código e **cada decisão** registrada.
- Os demais itens seguem com os prazos dos grupos (21/11 e 26/11). A banca pode consultar o histórico do Git.

**A Defesa Técnica é individual.** Você será arguido sobre o que registrou. Cada aluno recebe pelo menos **1 questão** nos níveis de **Avaliação** ou **Criação** (taxonomia de Bloom).

**Como a Rubrica se liga ao seu Logbook:**

| Critério da Rubrica | Onde você prepara a evidência |
|---|---|
| 1. Domínio dos objetos de conhecimento | Campos 01, 02 e 07b |
| 2. Aplicação do conteúdo à solução ⚠️ *inegociável* | Registros dos ciclos (itens 3 e 5), Campo 03c e Campo 05e |
| 3. Evolução conceitual ⚠️ *inegociável* | Campo 01 → Campo 07 (7a, 7b e 7c; leve o rascunho) |
| 4. Capacidade de transferência | Campo 07d |
| 5. Argumentação sob pressão | Campo 06c e Campo 04e |
| 6. Autonomia intelectual e coerência com o Logbook | Todo o Logbook (principalmente Campos 04 e 06a) |

**Treino:** peça a um colega que faça 3 perguntas "imprevistas" sobre o seu CRUD e responda **sem consultar** o Logbook. Se não conseguir, volte ao Campo 06b.
</details>

## 🧩 RUBRICA DE DEFESA TÉCNICA (revisada)
*Avaliação individual de cada membro na Semana 16. Cada membro recebe ao menos 1 questão nos níveis de Avaliação ou Criação da Taxonomia de Bloom. Critérios revisados para medir aprendizagem, aplicação, evolução e transferência do conteúdo.*

| | |
|---|---|
| **Nome** | _…_ |
| **Curso / Time / Função** | _…_ |

<details>
<summary>🔒 Uso do professor — rubrica completa</summary>

| CRITÉRIO | EXCELENTE (4,0) | SATISFATÓRIO (3,0) | INSATISFATÓRIO (2,0) | AUSENTE (0) |
|---|---|---|---|---|
| **1. DOMÍNIO DOS OBJETOS DE CONHECIMENTO** — Responde com precisão técnica, sem apoio dos colegas, demonstrando aprendizagem do conteúdo. | Responde com precisão e profundidade, nomeando os objetos de conhecimento mobilizados sem hesitação. | Responde com precisão, com imprecisões pontuais que não comprometem o raciocínio. | Responde de forma vaga, com erros conceituais relevantes ou dependendo dos colegas. | Não responde ou demonstra desconhecimento total. |
| **2. APLICAÇÃO DO CONTEÚDO À SOLUÇÃO** — Demonstra como os objetos de conhecimento fundamentaram as decisões do processo. | Explicita com precisão qual objeto de conhecimento fundamentou cada decisão relevante do processo investigativo, citando referência e demonstrando por que aquele conhecimento era o mais adequado. | Estabelece a relação conteúdo-decisão na maioria das perguntas, com alguma imprecisão pontual. | Não consegue explicitar a relação entre o conteúdo e as decisões do processo investigativo com clareza. | Não demonstra nenhuma relação entre os objetos de conhecimento e as decisões tomadas. |
| **3. EVOLUÇÃO CONCEITUAL** — Demonstra aprendizagem em relação ao que sabia no início do ciclo. | Identifica com precisão o que aprendeu, o que corrigiu e como o conhecimento evoluiu ao longo do ciclo. | Demonstra evolução em parte dos conceitos trabalhados, com alguma dificuldade de articular a trajetória. | Dificuldade em identificar diferenças entre o que sabia no início e o que domina agora. | Não demonstra nenhuma percepção de evolução conceitual ao longo do ciclo. |
| **4. CAPACIDADE DE TRANSFERÊNCIA** — Aplica o conhecimento a um contexto diferente do problema trabalhado. | Consegue transferir o aprendizado para um contexto novo com fundamentação técnica precisa. | Realiza a transferência com imprecisões que não comprometem a lógica do raciocínio. | Demonstra dificuldade em aplicar o conhecimento a contextos diferentes do problema original. | Não consegue realizar nenhuma transferência do conhecimento para contexto diferente. |
| **5. ARGUMENTAÇÃO SOB PRESSÃO** — Mantém coerência técnica diante de questionamentos imprevistos. | Mantém raciocínio coerente, reconhece limites com honestidade e reformula com fundamentação. | Mantém coerência na maior parte, com hesitações pontuais sem perda do fio técnico. | Fragilidade técnica diante de questionamentos imprevistos. | Não sustenta argumentação técnica diante de nenhum questionamento. |
| **6. AUTONOMIA INTELECTUAL E COERÊNCIA COM O LOGBOOK** — Defende o que registrou com consciência e sem depender do grupo. | Defende com precisão as decisões do Logbook, demonstrando autoria plena e independência intelectual. | Defende a maioria das decisões com coerência, com alguma imprecisão ou apoio pontual. | Depende dos colegas ou demonstra desconhecimento de parte do que registrou no próprio Logbook. | Não reconhece o que registrou ou não demonstra autonomia intelectual durante a arguição. |

**PONTUAÇÃO:** _____ / 24,0 **CONCEITO:** _____________

**Conversão:** 20–24 = Excelente (4,0) | 14–19 = Satisfatório (3,0) | 8–13 = Insatisfatório (2,0) | < 8 = Ausente (0)

> ⚠️ **Critérios 2 (Aplicação) e 3 (Evolução Conceitual) são inegociáveis — AUSENTE em qualquer um deles implica nota máxima de 2,0 na Defesa, independentemente do desempenho nos demais.**

**OBSERVAÇÕES:** _…_

**Professor(a):** _________________  **Data:** ___________
</details>

### Registro do Encerramento — 18/11
1. **O que apresentei/defendi (em 1 frase):** _…_
2. **Objeto(s) de conhecimento que a banca mais explorou:** _…_
3. **Pergunta que mais me desafiou e como respondi:** _…_
4. **O que levo deste semestre para o próximo módulo:** _…_

---

# 🆘 Estou atrasado no Logbook. E agora?

1. **Não apague nem "retroescreva" o passado.** Preencha agora e **escreva a data real** do preenchimento (ex.: *"preenchido com atraso em 12/11"*).
2. **Campo 01 e Checkpoint (sem consulta):** se perdeu a janela, registre **o que sabe hoje, sem consultar nada**, marcando-o como *preenchimento tardio*. Combine o tratamento com o professor.
3. **Priorize a ordem dos grupos:** Grupo 1 (16/11) → Defesa (18/11) → Grupo 2 (21/11) → Grupo 3 (26/11). Dentro de cada grupo, os Campos vêm antes dos Registros.
4. **Use o histórico do Git** (`git log --oneline`) para reconstruir o que fez em cada ciclo — ele é uma evidência melhor que a memória.
5. **Fale com o professor** antes do prazo, não depois.
