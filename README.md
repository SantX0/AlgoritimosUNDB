# UpSpot

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat&logo=python&logoColor=white)
![Interface](https://img.shields.io/badge/Interface-CLI-222222)
![Status](https://img.shields.io/badge/Status-Em%20desenvolvimento-yellow)

## Sobre o projeto

O **UpSpot** é um sistema de gerenciamento de músicas desenvolvido em Python, executado diretamente no terminal. Seu propósito é simular o processo de envio de músicas para uma plataforma digital, permitindo cadastrar, consultar, atualizar e excluir registros musicais, além de consultar relatórios sobre o catálogo.

O projeto aplica os conceitos de CRUD (*Create, Read, Update, Delete*), lógica de programação, estruturas de dados e validação de entradas, sem dependências externas.

## Funcionalidades

| Opção | Funcionalidade | Descrição |
| --- | --- | --- |
| 1 | Cadastrar música | Registra os metadados e simula a aprovação do upload. |
| 2 | Listar músicas | Exibe os registros, IDs, artistas, gêneros, durações e status. |
| 3 | Buscar músicas | Localiza registros por diferentes critérios. |
| 4 | Atualizar música | Altera os dados de um registro localizado pelo ID. |
| 5 | Excluir música | Remove um registro mediante confirmação. |
| 6 | Sair | Encerra o programa. |
| 7 | Relatórios | Disponibiliza consultas estatísticas sobre o catálogo. |

### Métodos de busca

- Por ID único;
- Por nome do artista;
- Por nome da música;
- Por gênero musical;
- Busca combinada por gênero e duração mínima.

As buscas textuais aceitam correspondências parciais e não diferenciam letras maiúsculas de minúsculas. Na busca combinada, o gênero deve corresponder integralmente ao informado.

### Relatórios

O módulo de relatórios contempla:

- Resumo geral do catálogo: quantidade, duração total e média, espaço total e médio;
- Identificação da música mais longa e mais curta;
- Quantidade de músicas por gênero;
- Quantidade de envios aprovados, falhas e percentual de sucesso.

## Regras de negócio

- Cada música recebe um ID incremental, que não é reutilizado durante a execução, mesmo após uma exclusão.
- Os gêneros aceitos são Rock, Pop, Sertanejo, Rap, Eletronica e MPB.
- Os formatos aceitos são MP3, WAV, FLAC e M4A.
- A duração e o tamanho do arquivo devem ser maiores que zero.
- O limite de aprovação do upload é de 50 MB. Registros acima desse limite são armazenados com status `falhou`; os demais recebem status `enviado`.
- O dia deve estar entre 1 e 31, o mês entre 1 e 12 e o ano deve ser igual ou posterior a 1900.
- A hora deve estar entre 0 e 23 e os minutos entre 0 e 59.
- É possível cadastrar múltiplos autores e produtores, utilizando `fim` para encerrar cada entrada.
- A exclusão exige confirmação do usuário.
- A atualização do tipo e tamanho do arquivo recalcula o status do upload.

## Estrutura de dados

Os registros são armazenados em uma lista principal chamada `musicas`. Cada música é representada por uma lista de 16 campos, acessados por constantes de índice.

| Índice | Campo | Tipo |
| --- | --- | --- |
| 0 | ID | `int` |
| 1 | Gênero | `str` |
| 2 | Artista | `str` |
| 3 | Nome da música | `str` |
| 4 | Duração em segundos | `int` |
| 5 | Dia de lançamento | `int` |
| 6 | Mês de lançamento | `int` |
| 7 | Ano de lançamento | `int` |
| 8 | Hora de lançamento | `int` |
| 9 | Minuto de lançamento | `int` |
| 10 | Autores | `list` |
| 11 | Produtores | `list` |
| 12 | Tipo de arquivo | `str` |
| 13 | Tamanho em MB | `float` |
| 14 | Nome do arquivo | `str` |
| 15 | Status | `str` |

O ID identifica o registro, enquanto o índice representa sua posição na lista. Essa distinção permite localizar corretamente uma música mesmo quando a posição dos registros muda após exclusões.

## Tecnologias e conceitos aplicados

- Python 3;
- Interface de linha de comando (CLI);
- Listas e listas aninhadas;
- Estruturas condicionais (`if`, `elif`, `else`);
- Estruturas de repetição (`for`, `while`);
- Busca sequencial, contadores e acumuladores;
- Constantes de índice e validação de dados;
- Operações CRUD.

## Estrutura do projeto

```text
UpSpot/
├── uploader_musicas.py
└── README.md
```

## Como executar

### Pré-requisitos

Ter o Python 3 instalado no computador. Não é necessário instalar bibliotecas adicionais.

### Execução

Abra o terminal na pasta do projeto e execute:

```bash
python uploader_musicas.py
```

Em sistemas nos quais o interpretador é identificado como `python3`, utilize:

```bash
python3 uploader_musicas.py
```

### Menu principal

```text
===== UPLOADER DE MÚSICAS =====
1 - Cadastrar música (upload)
2 - Listar músicas
3 - Buscar músicas
4 - Atualizar música
5 - Excluir música
6 - Sair
7 - Relatorio
=====================================
```

Digite o número correspondente à operação desejada e siga as instruções apresentadas no terminal.

## Limitações e melhorias futuras

O UpSpot simula uploads a partir dos metadados informados pelo usuário. Não realiza transferência real de arquivos de áudio nem integração com plataformas de streaming. Os dados são mantidos em memória e perdidos ao encerrar o programa.

Possíveis evoluções:

- Revisar o tratamento de entradas e os cálculos e a exibição dos relatórios;
- Implementar validação completa de datas;
- Implementar persistência de dados em JSON ou banco de dados;
- Modularizar o código em funções;
- Implementar testes automatizados;
- Desenvolver uma interface gráfica ou web;
- Implementar upload real de arquivos de áudio.

## Objetivo de aprendizagem

Consolidar conhecimentos de programação em Python por meio da construção de um sistema de gerenciamento de registros, aplicando estruturas de dados, algoritmos de busca, validações e processamento de informações em um contexto de distribuição musical.
