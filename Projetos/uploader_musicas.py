# ============ LISTAS DE VALIDAÇÃO ============
generos_validos = ["Rock", "Pop", "Sertanejo", "Rap", "Eletronica", "MPB"]
tipos_permitidos = ["mp3", "wav", "flac", "m4a"]

# ---------- ARMAZENAMENTO ----------
musicas = []
proximo_id = [1]

# ============ CONSTANTES DE ÍNDICE ============
IND_ID = 0
IND_GENERO = 1
IND_ARTISTA = 2
IND_NOME = 3
IND_DURACAO_SEG = 4
IND_DIA = 5
IND_MES = 6
IND_ANO = 7
IND_HORA = 8
IND_MINUTO = 9
IND_AUTORES = 10
IND_CO_AUTORES = 11
IND_PRODUTORES = 12
IND_TIPO_ARQ = 13
IND_TAMANHO_MB = 14
IND_NOME_ARQ = 15
IND_STATUS = 16

# ---------- MENU PRINCIPAL ----------
while True:
    print("===== UPLOADER DE MÚSICAS ====")
    print("1 - Cadastrar música (upload)")
    print("2 - Listar músicas")
    print("3 - Buscar músicas")
    print("4 - Atualizar música")
    print("5 - Excluir música")
    print("6 - Sair ")
    print("=====================================")

    opcao = input("Escolha uma opção:\n")

    if not opcao.isdigit():
        print("Opção Invalida! Digite um numero de 1 a 6.")
    elif int(opcao) < 1 or int(opcao) > 6:
        print("Opção inválida! Digite um número de 1 a 6")
    elif int(opcao) == 1:
        # CADASTRAR MÚSICA
        print("----- NOVO UPLOAD -----")
        while True:
            generosNome = input(
                f"Generos disponíveis {generos_validos}\nDigite o gênero:\n"
            )
            if generosNome not in generos_validos:
                print("Gênero inválido! Escolha um da lista.")
            else:
                break
        # ---------- GÊNERO ----------
        while True:
            artistasNome = input("Artistas:\n")
            if artistasNome == "":
                print("O nome do artista não pod ficar vazio!")
            else:
                break
        # ---------- NOME DA MÚSICA ----------
        while True:
            musicaNome = input("Nome Musica:\n")
            if musicaNome == "":
                print("O nome da música não pode ficar vazio.")
            else:
                break
        # ---------- DURAÇÃO ----------
        while True:
            durocaoMusica = input("Duração em segundos:\n")
            if not durocaoMusica.isdigit():
                print("Digite apnes números. ")
            else:
                duracaoSeg = int(durocaoMusica)
                if duracaoSeg <= 0:
                    print("A duração deve ser maor que zero.")
                else:
                    break
        # ---------- DATA DE LANÇAMENTO ----------
        while True:
            diaLancamento = int(input("Dia de lançamento:\n"))
            mesLançamento = int(input("Mês de lançamento:\n"))
            anoLançamento = int(input("Ano de lançamento:\n"))
            if (
                diaLancamento < 1
                or diaLancamento > 31
                or mesLançamento < 1
                or mesLançamento > 31
                or anoLançamento < 1900
            ):
                print(
                    "Data invalida! Verifique o dia (1-31), o mês (1-12) e o ano (<1900)"
                )
            else:
                break
        # ---------- HORA DE LANÇAMENTO ----------
        while True:
            horaLancamento = int(input("Hora de lançamento:\n"))
            minutoLancamento = int(input("Minuto de lançamento:\n"))
            segundosLancamento = int(input("Segundos de lançamento:\n"))
            if (
                horaLancamento < 0
                or horaLancamento > 23
                or minutoLancamento < 0
                or minutoLancamento > 59
                or segundosLancamento < 0
                or segundosLancamento > 59
            ):
                print(
                    "Hora inválida! Verifique a hora (0 a 23), os minutos (0 a 59) e os segundos (0 a 59) "
                )
            else:
                break
        # ---------- AUTORES ----------
        autores = []
        while True:
            autoresMusic = input("Digite Autor/a ('ou fim' para encerrar):\n")
            if autoresMusic != "fim" and autoresMusic != "":
                autores.append(autoresMusic)

            if autoresMusic == "fim":
                break
        # ---------- PRODUTORES ----------
        produtores = []
        while True:
            prodMusic = input("Digite Produtor/a ('ou fim para encerrar'):\n")
            if autoresMusic != "fim" or autoresMusic != "":
                produtores.append(prodMusic)

            if autoresMusic == "fim":
                break
        # ---------- TIPO DE ARQUIVO ----------
        while True:
            arquivoTipo = input(f"Tipos aceitos:{tipos_permitidos}\nTipo de arquivo:")
            arquivoTipo = arquivoTipo.lower()
            if arquivoTipo not in tipos_permitidos:
                print("Tipo inválido! Use um da lista.")
                arquivoTipo = input("Tipo de arquivo:\n").lower()
            else:
                break
        # ---------- NOME DO ARQUIVO ---------
        nomeArquivo = input("Digiite o nome do arquivo (ex:santforxo.mp3):\n")
        if nomeArquivo == "":
            print("O nome do arquivo não pode estar vazio")
        else:
            break
        # ---------- REGRA DE APROVAÇÃO DO UPLOAD ----------
        tamanhoMB = float
        if tamanhoMB <= 50:
            status = "enviado"
        else:
            status = "falhou"
            print("Arquivo muito grande! Limite de 50 MB.")
        # ---------- MONTA A MÚSICA E GUARDA ----------
        novasMusicas = [
            proximo_id,
            generosNome,
            artistasNome,
            musicaNome,
            duracaoSeg,
            diaLancamento,
            mesLançamento,
            anoLançamento,
            horaLancamento,
            minutoLancamento,
            autoresMusic,
            prodMusic,
            arquivoTipo,
            tamanhoMB,
            nomeArquivo,
            status,
        ]
        musicas.append(novasMusicas)
        print("Upload registrado! ID da musica: ", proximo_id)
        if status == "enviado":
            print("Status: ENVIADO com sucesso")
        else:
            print("Status: FALHOU (arquivo acima do limite).")
        proximo_id == proximo_id + 1

    elif int(opcao) == 2:
        # Listar Músicas
        if len(musicas) == 0:
            print("Nenhuma música cadastrada ainda")
        else:
            print("===== LISTA DE MÚSICAS =====")
            contador = 0
            for musica_atual in musicas:
                minutos = musica_atual[IND_DURACAO_SEG] // 60
                segundos = musica_atual[IND_DURACAO_SEG] % 60
                duracao_texto = f"{minutos}:{segundos:02d}"
                print(
                    contador,
                    "| ID",
                    musica_atual[IND_ID],
                    " | ",
                    musica_atual[IND_NOME],
                    " | Artistas: ",
                    musica_atual[IND_ARTISTA],
                    " | Gênero: ",
                    musica_atual[IND_GENERO],
                    " | Duração: ",
                    duracao_texto,
                    " | Status: ",
                    musica_atual[IND_STATUS],
                )
            contador = contador + 1
            print(f"Total: {len(musicas)} música(s).")
            print()
    elif int(opcao) == 3:
        # Buscar Música
        if len(musicas) == 0:
            print("Nenhuma música cadastrada ainda.")
        else:
            print("---- BUSCA ----")
            print("1 - Buscar por ID")
            print("2 - Buscar por Artista")
            print("3 - Buscar por Nome")
            print("4 - Buscar por Gênero")
            print("5 - Buscar Combinada (gênero e duração mínima)")
            tipo_busca = input
            if tipo_busca == 1:
                # ---------- Busca por ID  ----------
                id_busca = input("Digite o ID:\n")
                posicao_encontrada = -1
                for i in range(0, len(musicas)):
                    if musicas[i][IND_ID] == id_busca:
                        posicao_encontrada = i
                    break
                if posicao_encontrada == -1:
                    print("Nenhuma música foi encontrada com ID", id_busca, ":")
                else:
                    print("Encontrada na posição", posicao_encontrada, ":")
                    print(
                        musicas[posicao_encontrada][IND_NOME],
                        "-",
                        musicas[posicao_encontrada][IND_ARTISTA],
                        "-",
                        musicas[posicao_encontrada][IND_STATUS],
                    )
            elif tipo_busca == 2 or tipo_busca == 3 or tipo_busca == 4:
                # ---------- Busca por texto ----------
                if tipo_busca == 2:
                    input("Digite parte do artista:\n")
                    indice_campo = IND_ARTISTA
                elif tipo_busca == 3:
                    input("Digite parte do nome:\n")
                    indice_campo = IND_NOME
                else:
                    input("Digite o gênero:\n")
                    indice_campo = IND_GENERO
                termo_busca = input
                termo_busca = termo_busca.lower()

                resultados = []

                for musica_atual in musicas:
                    campo = musica_atual[indice_campo].lower()
                    if campo in termo_busca:
                        resultados.append(musica_atual)
                    if len(resultados) == 0:
                        print("Nenhum resultado para '", termo_busca, "'.")
                    else:
                        print(f"{resultados}, resultado(s): ")
                        for musica_achada in resultados:
                            print(
                                "ID: ",
                                musica_achada[IND_ID],
                                " | ",
                                musica_achada[IND_NOME],
                                " | ",
                                musica_achada[IND_ARTISTA],
                                " | ",
                                musica_achada[IND_GENERO],
                            )
                        break
            elif tipo_busca == 5:
                # ---------- Busca combinada ----------
                genero_busca = input("Digite o gênero:\n")
                genero_busca = genero_busca.lower()

                duracao_mini = "Duração minima em segundos"

                resultados = []
                for musica_atual in musicas:
                    if (
                        musica_atual["IND_GENERO"].lower() == genero_busca
                        and musica_atual["IND_DURACAO_SEG"] >= duracao_mini
                    ):
                        resultados.append(musica_atual)
                    if resultados == 0:
                        print("Nenhuma musica combina com os 2 criterios")
                    else:
                        for musica_achada in resultados:
                            print(
                                musica_achada[IND_NOME],
                                "-",
                                musica_achada[IND_DURACAO_SEG],
                                " Segundos",
                            )
                else:
                    print("Tipo de Busca invalida ")
    elif int(opcao) == 4:
        #Atualizar  Musicas
        if musicas == 0:
            print("Nenhuma música cadastrada.")
        else:
            # ---------- Busca por ID ----------
            id_busca = input("Digite o ID da música que você esta procurando:\n")
            posicao_encontrada = -1
            for i in range(0, musicas - 1):
                if musicas[i][IND_ID] == id_busca:
                    posicao_encontrada = -1
                break
            if posicao_encontrada == -1:
                print("Nenhuma música com ID ", id_busca, ".")
            else:
                # ---------- Mostrar a música atual ----------
                musica_atual = musicas[posicao_encontrada]
                print("Música encontrada:\n")
                print(
                    "Gênero:",
                    musica_atual[IND_GENERO],
                    "| Artista:",
                    musica_atual[IND_ARTISTA],
                    "| Nome:",
                    musica_atual[IND_NOME],
                    "| Duração(seg):",
                    musica_atual[IND_DURACAO_SEG],
                    "| Data:",
                    musica_atual[IND_DIA],
                    "/",
                    musica_atual[IND_MES],
                    "/",
                    musica_atual[IND_ANO],
                    "| Hora:",
                    musica_atual[IND_HORA],
                    ":",
                    musica_atual[IND_MINUTO],
                    "| Autores:",
                    musica_atual[IND_AUTORES],
                    "| Produtores:",
                    musica_atual[IND_PRODUTORES],
                    "| Tipo/Tamanho:",
                    musica_atual[IND_TIPO_ARQ],
                    "-",
                    musica_atual[IND_TAMANHO_MB],
                    "MB",
                    "| Arquivo:",
                    musica_atual[IND_NOME_ARQ],
                )
                # ---------- Submenu: qual campo alterar ----------
                campo_escolhido = input("Qual campo deseja alterar? 0 para cancelar")
                if campo_escolhido == 0:
                    print("Atualização cancelada.")

                elif campo_escolhido == 1:
                    while True:
                        genero_atlz = input("Gênero disponíveis: ", generos_validos)
                        if genero_atlz not in generos_validos:
                            print("Gênero inválido! Escolha um da lista.")

                        while genero_atlz not in generos_validos:
                            musicas[posicao_encontrada][IND_GENERO] = genero_atlz

                elif campo_escolhido == 2:
                    while True:
                        artista_atlz = input("Novo artista:\n")
                        while artista_atlz == "":
                            musicas[posicao_encontrada][IND_ARTISTA] = artista_atlz

                elif campo_escolhido == 3:
                    nomeMusica_atlz = input("Novo nome da música:\n")
                    while nomeMusica_atlz == "":
                        musicas[posicao_encontrada][IND_NOME] = nomeMusica_atlz

                elif campo_escolhido == 4:
                    duracao_atlz = input("Nova duração em segundos:\n")
                    if not duracao_atlz.isdigit():
                        print("Digite apenas números.")
                    else:
                        atlz_duracaoSeg = int(duracao_atlz)
                        if atlz_duracaoSeg <= 0:
                            print("A duração deve ser maior que zero.")
                            while not duracao_atlz.isdigit() or atlz_duracaoSeg <= 0:
                                musicas[posicao_encontrada][IND_DURACAO_SEG] = atlz_duracaoSeg

                elif campo_escolhido == 5:
                    dia_atlz, mes_atlz, ano_atlz = input ("Novo dia / mês / ano : ").split()
                    if dia_atlz < 1 or dia_atlz > 31 or mes_atlz < 1 or mes_atlz > 31 or ano_atlz < 1900:
                        print("Data inválida!")
                        while dia_atlz < 1 or dia_atlz > 31 or mes_atlz < 1 or mes_atlz > 31 or ano_atlz < 1900:
                            musicas[posicao_encontrada][IND_DIA] = dia_atlz
                            musicas[posicao_encontrada][IND_MES] = mes_atlz
                            musicas[posicao_encontrada][IND_ANO] = ano_atlz

                elif campo_escolhido == 6:
    elif int(opcao) == 5:
        print("Excluir")
    else:
        print("Encerrando o programa. Até uma proximma!")
    break
