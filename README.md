# UpSpot

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=flat&logo=python&logoColor=white)
![Interface](https://img.shields.io/badge/Interface-CLI-222222)
![Persistência](https://img.shields.io/badge/Persistência-JSON-orange)

## Sobre o projeto

O **UpSpot** é um sistema de gerenciamento de músicas desenvolvido em Python, executado diretamente no terminal. Seu propósito é simular o processo de envio de músicas para uma plataforma digital, permitindo cadastrar, consultar, atualizar e excluir registros musicais, além de gerar relatórios sobre o catálogo.

O projeto aplica os conceitos de CRUD (_Create, Read, Update, Delete_), modularização por funções, estruturas de dados, validação de entradas e persistência local em JSON, sem dependências externas.

## Funcionalidades

| Opção | Funcionalidade   | Descrição                                                 |
| ----- | ---------------- | --------------------------------------------------------- |
| 1     | Cadastrar música | Registra metadados, simula o upload e salva o catálogo.   |
| 2     | Listar músicas   | Exibe IDs, títulos, artistas, gêneros, durações e status. |
| 3     | Buscar músicas   | Localiza registros por diferentes critérios.              |
| 4     | Atualizar música | Altera dados de um registro localizado pelo ID.           |
| 5     | Excluir música   | Remove um registro mediante confirmação.                  |
| 6     | Sair             | Encerra o programa.                                       |
| 7     | Relatórios       | Apresenta estatísticas sobre o catálogo.                  |

### Métodos de busca

- Por ID único;
- Por artista;
- Por título da música;
- Por gênero musical;
- Busca combinada por gênero e duração mínima em segundos.

As buscas textuais aceitam correspondências parciais e ignoram diferenças entre maiúsculas e minúsculas. Na busca combinada, o gênero deve corresponder integralmente ao informado.

### Relatórios

- **Resumo geral:** quantidade de músicas, duração total e média, tamanho total e médio dos arquivos informados;
- **Duração:** identificação da música mais longa e da mais curta;
- **Gêneros:** quantidade de músicas por gênero, incluindo gêneros sem registros;
- **Uploads:** quantidade de registros enviados, falhas e percentual de sucesso.

## Regras de negócio

- Cada música recebe um ID incremental, independente da posição na lista. IDs não são reutilizados após exclusões enquanto o catálogo for preservado.
- Gêneros aceitos: Rock, Pop, Sertanejo, Rap, Eletronica e MPB.
- Formatos aceitos: MP3, WAV, FLAC e M4A.
- Artista, título e nome do arquivo não podem estar vazios ou conter apenas espaços.
- A duração deve ser um número inteiro positivo, em segundos.
- A data de lançamento deve existir no calendário, considerando os dias de cada mês e anos bissextos, com ano a partir de 1900.
- A hora deve estar entre 0 e 23 e os minutos entre 0 e 59.
- O tamanho informado deve ser positivo e finito, aceitando ponto ou vírgula como separador decimal.
- É possível cadastrar zero ou mais autores e produtores, utilizando `fim` para encerrar cada entrada.
- O limite de aprovação do upload é de 50 MB. Registros de até 50 MB recebem status `enviado`; acima desse limite, recebem `falhou` e também são armazenados.
- A atualização do formato e tamanho recalcula o status do upload.
- A exclusão exige confirmação do usuário (`s` ou `n`).

## Estrutura de dados

O catálogo utiliza uma lista de dicionários. Cada música possui 16 campos identificados por chaves descritivas, substituindo o modelo anterior baseado em índices fixos.

| Chave          | Descrição                    | Tipo    |
| -------------- | ---------------------------- | ------- |
| `id`           | Identificador único          | `int`   |
| `genero`       | Gênero musical               | `str`   |
| `artista`      | Nome do artista              | `str`   |
| `titulo`       | Título da música             | `str`   |
| `duracao_seg`  | Duração em segundos          | `int`   |
| `dia`          | Dia de lançamento            | `int`   |
| `mes`          | Mês de lançamento            | `int`   |
| `ano`          | Ano de lançamento            | `int`   |
| `hora`         | Hora de lançamento           | `int`   |
| `minuto`       | Minuto de lançamento         | `int`   |
| `autores`      | Lista de autores             | `list`  |
| `produtores`   | Lista de produtores          | `list`  |
| `formato`      | Formato do arquivo           | `str`   |
| `tamanho_mb`   | Tamanho informado em MB      | `float` |
| `nome_arquivo` | Nome do arquivo              | `str`   |
| `status`       | Resultado do upload simulado | `str`   |

## Persistência de dados

O arquivo `musicas.json` é criado automaticamente na pasta do script após o primeiro cadastro salvo com sucesso. Ele armazena a lista de músicas e o próximo ID disponível. Na inicialização, o programa recupera essas informações; caso o arquivo ainda não exista, inicia com um catálogo vazio e ID 1.

Exemplo de catálogo (dados fictícios):

```json
{
  "musicas": [
    {
      "id": 1,
      "genero": "Rap",
      "artista": "Artista Exemplo",
      "titulo": "Minha Música",
      "duracao_seg": 210,
      "dia": 24,
      "mes": 11,
      "ano": 2026,
      "hora": 12,
      "minuto": 0,
      "autores": ["Autor Exemplo"],
      "produtores": ["Produtor Exemplo"],
      "formato": "mp3",
      "tamanho_mb": 8.5,
      "nome_arquivo": "minha_musica.mp3",
      "status": "enviado"
    }
  ],
  "proximo_id": 2
}
```

As operações de cadastro, atualização e exclusão salvam o catálogo antes de alterar os registros em memória. A gravação utiliza um arquivo temporário e posterior substituição do arquivo definitivo, reduzindo o risco de gravações incompletas. O sistema também trata erros de leitura e escrita e verifica parte da estrutura do catálogo carregado.

## Modularização e organização do código

O código permanece em um único arquivo Python, organizado em funções com responsabilidades específicas.

| Funções                                                     | Responsabilidade                                    |
| ----------------------------------------------------------- | --------------------------------------------------- |
| `main()`                                                    | Inicialização, menu principal e controle do fluxo.  |
| `carregar_catalogo()`, `salvar_catalogo()`                  | Leitura e gravação do catálogo JSON.                |
| `ler_texto()`, `ler_opcao()`, `ler_inteiro()`               | Validações reutilizáveis de entradas.               |
| `ler_genero()`, `ler_duracao()`, `ler_data()`, `ler_hora()` | Validação de metadados musicais.                    |
| `ler_nomes()`, `ler_tamanho()`, `ler_dados_upload()`        | Leitura de listas de nomes e informações do upload. |
| `cadastrar_musica()`, `listar_musicas()`                    | Cadastro e listagem de registros.                   |
| `buscar_posicao()`, `buscar_musicas()`                      | Busca sequencial por ID e filtros de consulta.      |
| `exibir_detalhes()`, `atualizar_musica()`                   | Exibição de detalhes e edição dos registros.        |
| `excluir_musica()`                                          | Exclusão mediante confirmação.                      |
| `gerar_relatorio()`                                         | Cálculo e apresentação das estatísticas.            |

O ponto de entrada utiliza `if __name__ == "__main__"`, permitindo importar as funções sem iniciar automaticamente o menu.

## Tecnologias e conceitos aplicados

- Python 3 e interface de linha de comando (CLI);
- Funções, parâmetros, retornos e reutilização de código;
- Listas, dicionários, tuplas e compreensão de listas;
- Estruturas condicionais e de repetição;
- Busca sequencial, IDs incrementais e operações CRUD;
- Tratamento de exceções com `try`, `except` e `finally`;
- Manipulação de arquivos e serialização JSON;
- Funções auxiliares como `enumerate()`, `divmod()`, `sum()`, `min()` e `max()` com expressões `lambda`.

### Biblioteca padrão

| Módulo        | Utilização                                       |
| ------------- | ------------------------------------------------ |
| `json`        | Serialização e desserialização do catálogo.      |
| `calendar`    | Validação de datas com `monthrange()`.           |
| `collections` | Contagem de gêneros e status com `Counter`.      |
| `math`        | Verificação de valores finitos com `isfinite()`. |
| `pathlib`     | Manipulação de caminhos e arquivos.              |
| `tempfile`    | Criação de arquivos temporários para gravação.   |

## Principais melhorias da refatoração

| Versão anterior                                   | Versão refatorada                                     |
| ------------------------------------------------- | ----------------------------------------------------- |
| Código concentrado no menu principal              | Funções com responsabilidades específicas             |
| Listas com índices fixos                          | Dicionários com chaves descritivas                    |
| Dados perdidos ao encerrar                        | Persistência local em JSON                            |
| IDs restritos à sessão                            | Próximo ID preservado no catálogo                     |
| Validações repetidas                              | Funções de validação reutilizáveis                    |
| Validação parcial de datas                        | Validação dos dias reais de cada mês                  |
| Tamanho decimal apenas com ponto                  | Ponto ou vírgula como separador decimal               |
| Relatórios com cálculos e exibição inconsistentes | Agregações corrigidas com funções nativas e `Counter` |

## Estrutura do projeto

```text
UpSpot/
├── uploader_musicas.py   # Código principal
├── musicas.json         # Gerado automaticamente após o primeiro cadastro
└── README.md            # Documentação
```

## Como executar

### Pré-requisitos

- Python 3.8 ou superior;
- Permissão de escrita na pasta do script para salvar o catálogo.

Não é necessário instalar bibliotecas externas.

### Execução

Abra o terminal na pasta do projeto e execute:

```bash
python uploader_musicas.py
```

Caso o interpretador seja identificado como `python3`, utilize:

```bash
python3 uploader_musicas.py
```

Os comandos pressupõem que o arquivo principal foi salvo como `uploader_musicas.py`.

### Menu principal

```text
===== UPLOADER DE MÚSICAS =====
1 - Cadastrar música (upload)
2 - Listar músicas
3 - Buscar músicas
4 - Atualizar música
5 - Excluir música
6 - Sair
7 - Relatórios
=====================================
```

Digite o número correspondente à operação desejada e siga as instruções apresentadas no terminal.

## Limitações e melhorias futuras

O UpSpot simula uploads com base nos metadados informados pelo usuário. Não realiza transferência real de arquivos de áudio, verificação do conteúdo ou tamanho físico dos arquivos nem integração com plataformas de streaming. A persistência é local e não utiliza banco de dados.

Possíveis evoluções:

- Implementar testes automatizados;
- Ampliar a validação da integridade dos registros carregados do JSON;
- Implementar armazenamento em banco de dados;
- Desenvolver uma interface gráfica ou web;
- Implementar upload real e validação de arquivos de áudio.

## Objetivo de aprendizagem

Consolidar conhecimentos de programação em Python por meio da construção e refatoração de um sistema CRUD, aplicando modularização, estruturas de dados, algoritmos de busca, validações, tratamento de exceções, persistência e processamento de informações em um contexto de distribuição musical.
