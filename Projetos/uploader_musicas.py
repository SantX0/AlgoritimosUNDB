# ============ UPLOADER DE MÚSICAS - CRUD ============

# ---------- LISTAS DE VALIDAÇÃO ----------
generos_validos = ["Rock", "Pop", "Sertanejo", "Rap", "Eletronica", "MPB"]
tipos_permitidos = ["mp3", "wav", "flac", "m4a"]

# ---------- ARMAZENAMENTO ----------
musicas = []
proximo_id = 1

# ============ CONSTANTES DE ÍNDICE (16 campos) ============
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
IND_PRODUTORES = 11
IND_TIPO_ARQ = 12
IND_TAMANHO_MB = 13
IND_NOME_ARQ = 14
IND_STATUS = 15

# ============ MENU PRINCIPAL ============
while True:
    print("===== UPLOADER DE MÚSICAS =====")
    print("1 - Cadastrar música (upload)")
    print("2 - Listar músicas")
    print("3 - Buscar músicas")
    print("4 - Atualizar música")
    print("5 - Excluir música")
    print("6 - Sair")
    print("7 - Relatorio")
    print("=====================================")

    opcao = input("Escolha uma opção:\n")

    if not opcao.isdigit():
        print("Opção inválida! Digite um número de 1 a 6.")
    elif int(opcao) < 1 or int(opcao) > 6:
        print("Opção inválida! Digite um número de 1 a 6.")
    elif opcao == "1":
        # ============ CADASTRAR MÚSICA ============
        print("----- NOVO UPLOAD -----")

        # ---------- GÊNERO ----------
        while True:
            generosNome = input(
                f"Generos disponíveis {generos_validos}\nDigite o gênero:\n"
            )
            if generosNome not in generos_validos:
                print("Gênero inválido! Escolha um da lista.")
            else:
                break

        # ---------- ARTISTA ----------
        while True:
            artistasNome = input("Artistas:\n")
            if artistasNome == "":
                print("O nome do artista não pode ficar vazio!")
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
            duracaoTexto = input("Duração em segundos:\n")
            if not duracaoTexto.isdigit():
                print("Digite apenas números.")
            else:
                duracaoSeg = int(duracaoTexto)
                if duracaoSeg <= 0:
                    print("A duração deve ser maior que zero.")
                else:
                    break

        # ---------- DATA DE LANÇAMENTO ----------
        while True:
            diaTexto = input("Dia de lançamento:\n")
            mesTexto = input("Mês de lançamento:\n")
            anoTexto = input("Ano de lançamento:\n")

            if (
                not diaTexto.isdigit()
                or not mesTexto.isdigit()
                or not anoTexto.isdigit()
            ):
                print("Digite apenas números na data.")
            else:
                diaLancamento = int(diaTexto)
                mesLancamento = int(mesTexto)
                anoLancamento = int(anoTexto)
                if (
                    diaLancamento < 1
                    or diaLancamento > 31
                    or mesLancamento < 1
                    or mesLancamento > 12
                    or anoLancamento < 1900
                ):
                    print(
                        "Data inválida! Verifique o dia (1-31), o mês (1-12) e o ano (<1900)"
                    )
                else:
                    break

        # ---------- HORA DE LANÇAMENTO ----------
        while True:
            horaTexto = input("Hora de lançamento:\n")
            minutoTexto = input("Minuto de lançamento:\n")

            if not horaTexto.isdigit() or not minutoTexto.isdigit():
                print("Digite apenas números na hora.")
            else:
                horaLancamento = int(horaTexto)
                minutoLancamento = int(minutoTexto)
                if (
                    horaLancamento < 0
                    or horaLancamento > 23
                    or minutoLancamento < 0
                    or minutoLancamento > 59
                ):
                    print(
                        "Hora inválida! Verifique a hora (0 a 23) e os minutos (0 a 59)."
                    )
                else:
                    break

        # ---------- AUTORES ----------
        autores = []
        while True:
            autoresTexto = input("Digite Autor/a (ou 'fim' para encerrar):\n")
            if autoresTexto != "fim" and autoresTexto != "":
                autores.append(autoresTexto)
            if autoresTexto == "fim":
                break

        # ---------- PRODUTORES ----------
        produtores = []
        while True:
            produtoresTexto = input("Digite Produtor/a (ou 'fim' para encerrar):\n")
            if produtoresTexto != "fim" and produtoresTexto != "":
                produtores.append(produtoresTexto)
            if produtoresTexto == "fim":
                break

        # ---------- TIPO DE ARQUIVO ----------
        while True:
            arquivoTipo = input(
                f"Tipos aceitos: {tipos_permitidos}\nTipo de arquivo:\n"
            )
            arquivoTipo = arquivoTipo.lower()
            if arquivoTipo not in tipos_permitidos:
                print("Tipo inválido! Use um da lista.")
            else:
                break

        # ---------- TAMANHO DO ARQUIVO (decimal) ----------
        while True:
            tamanhoTexto = input("Tamanho do arquivo em MB (ex: 8.5):\n")

            if not tamanhoTexto.replace(".", "", 1).isdigit():
                print("Digite apenas números (use ponto para decimais).")
            else:
                tamanhoMB = float(tamanhoTexto)
                if tamanhoMB <= 0:
                    print("O tamanho deve ser maior que zero.")
                else:
                    break

        # ---------- NOME DO ARQUIVO ----------
        while True:
            nomeArquivo = input("Digite o nome do arquivo (ex: santxo.mp3):\n")
            if nomeArquivo != "":
                break
            print("O nome do arquivo não pode estar vazio")

        # ---------- REGRA DE APROVAÇÃO DO UPLOAD ----------
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
            mesLancamento,
            anoLancamento,
            horaLancamento,
            minutoLancamento,
            autores,
            produtores,
            arquivoTipo,
            tamanhoMB,
            nomeArquivo,
            status,
        ]
        musicas.append(novasMusicas)

        print("Upload registrado! ID da musica:", proximo_id)
        if status == "enviado":
            print("Status: ENVIADO com sucesso.")
        else:
            print("Status: FALHOU (arquivo acima do limite).")

        proximo_id = proximo_id + 1

    elif opcao == "2":
        # ============ LISTAR MÚSICAS ============
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
                    "| ID:",
                    musica_atual[IND_ID],
                    "|",
                    musica_atual[IND_NOME],
                    "| Artista:",
                    musica_atual[IND_ARTISTA],
                    "| Gênero:",
                    musica_atual[IND_GENERO],
                    "| Duração:",
                    duracao_texto,
                    "| Status:",
                    musica_atual[IND_STATUS],
                )
                contador = contador + 1
            print(f"Total: {len(musicas)} música(s).")

        print()

    elif opcao == "3":
        # ============ BUSCAR MÚSICA ============
        if len(musicas) == 0:
            print("Nenhuma música cadastrada ainda.")
        else:
            print("---- BUSCA ----")
            print("1 - Buscar por ID")
            print("2 - Buscar por Artista")
            print("3 - Buscar por Nome")
            print("4 - Buscar por Gênero")
            print("5 - Busca Combinada (gênero e duração mínima)")
            tipo_busca = input("Escolha o tipo de busca:\n")

            if tipo_busca == "1":
                # ---------- Busca por ID ----------
                idTexto = input("Digite o ID:\n")

                if not idTexto.isdigit():
                    print("ID inválido! Digite apenas números.")
                else:
                    id_busca = int(idTexto)
                    posicao_encontrada = -1

                    for i in range(len(musicas)):
                        if musicas[i][IND_ID] == id_busca:
                            posicao_encontrada = i
                            break

                    if posicao_encontrada == -1:
                        print("Nenhuma música foi encontrada com ID", id_busca, ".")
                    else:
                        print("Encontrada na posição", posicao_encontrada, ":")
                        print(
                            musicas[posicao_encontrada][IND_NOME],
                            "-",
                            musicas[posicao_encontrada][IND_ARTISTA],
                            "-",
                            musicas[posicao_encontrada][IND_STATUS],
                        )

            elif tipo_busca == "2" or tipo_busca == "3" or tipo_busca == "4":
                # ---------- Busca por texto ----------
                if tipo_busca == "2":
                    indice_campo = IND_ARTISTA
                    termo_busca = input("Digite parte do artista:\n")
                elif tipo_busca == "3":
                    indice_campo = IND_NOME
                    termo_busca = input("Digite parte do nome:\n")
                else:
                    indice_campo = IND_GENERO
                    termo_busca = input("Digite o gênero:\n")

                termo_busca = termo_busca.lower()
                resultados = []

                for musica_atual in musicas:
                    campo = musica_atual[indice_campo].lower()
                    if isinstance(campo, str) and termo_busca in campo:
                        resultados.append(musica_atual)

                if len(resultados) == 0:
                    print("Nenhum resultado para '", termo_busca, "'.")
                else:
                    print(f"{len(resultados)} resultado(s):")
                    for musica_achada in resultados:
                        print(
                            "ID:",
                            musica_achada[IND_ID],
                            "|",
                            musica_achada[IND_NOME],
                            "|",
                            musica_achada[IND_ARTISTA],
                            "|",
                            musica_achada[IND_GENERO],
                        )

            elif tipo_busca == "5":
                # ---------- Busca combinada ----------
                genero_busca = input("Digite o gênero:\n")
                genero_busca = genero_busca.lower()

                duracaoTextoMin = input("Duração mínima em segundos:\n")

                if not duracaoTextoMin.isdigit():
                    print("Digite apenas números.")
                else:
                    duracao_minima = int(duracaoTextoMin)
                    resultados = []

                    for musica_atual in musicas:
                        if (
                            musica_atual[IND_GENERO].lower() == genero_busca
                            and musica_atual[IND_DURACAO_SEG] >= duracao_minima
                        ):
                            resultados.append(musica_atual)

                    if len(resultados) == 0:
                        print("Nenhuma música combina com os 2 critérios.")
                    else:
                        for musica_achada in resultados:
                            print(
                                musica_achada[IND_NOME],
                                "-",
                                musica_achada[IND_DURACAO_SEG],
                                "segundos",
                            )

            else:
                print("Tipo de busca inválida.")

    elif opcao == "4":
        # ============ ATUALIZAR MÚSICA ============
        if len(musicas) == 0:
            print("Nenhuma música cadastrada.")
        else:
            # ---------- Busca por ID ----------
            idTexto = input("Digite o ID da música que você está procurando:\n")

            if not idTexto.isdigit():
                print("ID inválido! Digite apenas números.")
            else:
                id_busca = int(idTexto)
                posicao_encontrada = -1

                for i in range(len(musicas)):
                    if musicas[i][IND_ID] == id_busca:
                        posicao_encontrada = i
                        break

                if posicao_encontrada == -1:
                    print("Nenhuma música com ID", id_busca, ".")
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
                    print("1 - Gêneros")
                    print("2 - Artista")
                    print("3 - Nome da Musica")
                    print("4 - Duração")
                    print("5 - Data De Lançamento")
                    print("6 - Hora De Lançamento")
                    print("7 - Auotores")
                    print("8 - Produtores")
                    print("9 - Tipo De Arquivo")
                    print("10 - Nome Do Arquivo")
                    campo_escolhido = input(
                        "\nQual campo deseja alterar? (0 para cancelar):\n"
                    )

                    if campo_escolhido == "0":
                        print("Atualização cancelada.")

                    elif campo_escolhido == "1":
                        while True:
                            genero_atlz = input(
                                f"Gêneros disponíveis {generos_validos}\nDigite o gênero:\n"
                            )
                            if genero_atlz not in generos_validos:
                                print("Gênero inválido! Escolha um da lista.")
                            else:
                                break
                        musicas[posicao_encontrada][IND_GENERO] = genero_atlz
                        print("Música atualizada com sucesso!")

                    elif campo_escolhido == "2":
                        while True:
                            artista_atlz = input("Novo artista:\n")
                            if artista_atlz != "":
                                break
                            print("O artista não pode ficar vazio.")
                        musicas[posicao_encontrada][IND_ARTISTA] = artista_atlz
                        print("Música atualizada com sucesso!")

                    elif campo_escolhido == "3":
                        while True:
                            nomeMusica_atlz = input("Novo nome da música:\n")
                            if nomeMusica_atlz != "":
                                break
                            print("O nome não pode ficar vazio.")
                        musicas[posicao_encontrada][IND_NOME] = nomeMusica_atlz
                        print("Música atualizada com sucesso!")

                    elif campo_escolhido == "4":
                        while True:
                            duracaoTexto_atlz = input("Nova duração em segundos:\n")
                            if not duracaoTexto_atlz.isdigit():
                                print("Digite apenas números.")
                            else:
                                duracaoSeg_atlz = int(duracaoTexto_atlz)
                                if duracaoSeg_atlz <= 0:
                                    print("A duração deve ser maior que zero.")
                                else:
                                    break
                        musicas[posicao_encontrada][IND_DURACAO_SEG] = duracaoSeg_atlz
                        print("Música atualizada com sucesso!")

                    elif campo_escolhido == "5":
                        while True:
                            diaTexto = input("Novo dia de lançamento:\n")
                            mesTexto = input("Novo mês de lançamento:\n")
                            anoTexto = input("Novo ano de lançamento:\n")

                            if (
                                not diaTexto.isdigit()
                                or not mesTexto.isdigit()
                                or not anoTexto.isdigit()
                            ):
                                print("Digite apenas números na data.")
                            else:
                                dia_atlz = int(diaTexto)
                                mes_atlz = int(mesTexto)
                                ano_atlz = int(anoTexto)
                                if (
                                    dia_atlz < 1
                                    or dia_atlz > 31
                                    or mes_atlz < 1
                                    or mes_atlz > 12
                                    or ano_atlz < 1900
                                ):
                                    print(
                                        "Data inválida! Dia 1-31, mês 1-12, ano <1900."
                                    )
                                else:
                                    break
                        musicas[posicao_encontrada][IND_DIA] = dia_atlz
                        musicas[posicao_encontrada][IND_MES] = mes_atlz
                        musicas[posicao_encontrada][IND_ANO] = ano_atlz
                        print("Música atualizada com sucesso!")

                    elif campo_escolhido == "6":
                        while True:
                            horaTexto = input("Nova hora de lançamento:\n")
                            minutoTexto = input("Novo minuto de lançamento:\n")

                            if not horaTexto.isdigit() or not minutoTexto.isdigit():
                                print("Digite apenas números na hora.")
                            else:
                                hora_atlz = int(horaTexto)
                                minuto_atlz = int(minutoTexto)
                                if (
                                    hora_atlz < 0
                                    or hora_atlz > 23
                                    or minuto_atlz < 0
                                    or minuto_atlz > 59
                                ):
                                    print("Hora inválida! Hora 0 a 23, minutos 0 a 59.")
                                else:
                                    break
                        musicas[posicao_encontrada][IND_HORA] = hora_atlz
                        musicas[posicao_encontrada][IND_MINUTO] = minuto_atlz
                        print("Música atualizada com sucesso!")

                    elif campo_escolhido == "7":
                        autores = []
                        while True:
                            autor_atlz = input("Digite um autor (ou 'fim'):\n")
                            if autor_atlz != "fim" and autor_atlz != "":
                                autores.append(autor_atlz)
                            if autor_atlz == "fim":
                                break
                        musicas[posicao_encontrada][IND_AUTORES] = autores
                        print("Música atualizada com sucesso!")

                    elif campo_escolhido == "8":
                        produtores = []
                        while True:
                            produtor_atlz = input("Digite um produtor (ou 'fim'):\n")
                            if produtor_atlz != "fim" and produtor_atlz != "":
                                produtores.append(produtor_atlz)
                            if produtor_atlz == "fim":
                                break
                        musicas[posicao_encontrada][IND_PRODUTORES] = produtores
                        print("Música atualizada com sucesso!")

                    elif campo_escolhido == "9":
                        # ---------- tipo + tamanho: recalcula o STATUS ----------
                        while True:
                            arquivoTipo_atlz = input(
                                f"Tipos aceitos: {tipos_permitidos}\nTipo de arquivo:\n"
                            )
                            arquivoTipo_atlz = arquivoTipo_atlz.lower()
                            if arquivoTipo_atlz not in tipos_permitidos:
                                print("Tipo inválido! Use um da lista.")
                            else:
                                break

                        while True:
                            tamanhoTexto_atlz = input("Novo tamanho em MB (ex: 8.5):\n")

                            if not tamanhoTexto_atlz.replace(".", "", 1).isdigit():
                                print(
                                    "Digite apenas números (use ponto para decimais)."
                                )
                            else:
                                tamanhoMB_atlz = float(tamanhoTexto_atlz)
                                if tamanhoMB_atlz <= 0:
                                    print("O tamanho deve ser maior que zero.")
                                else:
                                    break

                        # regra de aprovação reaplicada (mesma do Dia 2)
                        if tamanhoMB_atlz <= 50:
                            musicas[posicao_encontrada][IND_STATUS] = "enviado"
                        else:
                            musicas[posicao_encontrada][IND_STATUS] = "falhou"

                        musicas[posicao_encontrada][IND_TIPO_ARQ] = arquivoTipo_atlz
                        musicas[posicao_encontrada][IND_TAMANHO_MB] = tamanhoMB_atlz
                        print("Música atualizada com sucesso!")

                    elif campo_escolhido == "10":
                        while True:
                            nomeArquivo_atlz = input("Novo nome do arquivo:\n")
                            if nomeArquivo_atlz != "":
                                break
                            print("O nome do arquivo não pode ficar vazio.")
                        musicas[posicao_encontrada][IND_NOME_ARQ] = nomeArquivo_atlz
                        print("Música atualizada com sucesso!")

                    else:
                        print("Campo inválido. Nada foi alterado.")

    elif opcao == "5":
        # ============ EXCLUIR MÚSICA ============
        if len(musicas) == 0:
            print("Nenhuma música cadastrada.")
        else:
            idTexto = input("Digite o ID da música que deseja excluir:\n")

            if not idTexto.isdigit():
                print("ID inválido! Digite apenas números.")
            else:
                id_busca = int(idTexto)
                posicao_encontrada = -1

                for i in range(len(musicas)):
                    if musicas[i][IND_ID] == id_busca:
                        posicao_encontrada = i
                        break

                if posicao_encontrada == -1:
                    print("Nenhuma música com ID", id_busca, ".")
                else:
                    print("Você está prestes a excluir:")
                    print(
                        musicas[posicao_encontrada][IND_NOME],
                        "-",
                        musicas[posicao_encontrada][IND_ARTISTA],
                    )

                    # ---------- Confirmação s/n ----------
                    while True:
                        confirmacao = input("Confirma a exclusão? (s/n):\n")
                        confirmacao = confirmacao.lower()
                        if confirmacao == "s" or confirmacao == "n":
                            break
                        print("Responda apenas 's' ou 'n'.")

                    if confirmacao == "s":
                        musicaRemovida = musicas.pop(posicao_encontrada)
                        print("Música excluída com sucesso.")
                        # OBS: proximo_id NÃO volta atrás — IDs nunca se repetem
                    else:
                        print("Exclusão cancelada.")

    elif opcao == "6":
        # ============ OPÇÃO 6 - SAIR ============
        print("Encerrando o programa. Até mais!")
        break
    elif opcao == "7":
        if musicas == 0:
            print("Nenhuma música cadastrada.")
        else:
            print("======= RELATÓRIOS ========")
            print("1 - Resumo Geral")
            print("2 - Música mais longa e mais curta")
            print("3 - Quantidade por gênero")
            print("4 - Enviadas vs Falhas")
            tipo_relatorio = int(input("Escolha:\n"))
            
            if tipo_relatorio == 1:
                #---------- RESUMO GERAL ----------
                # total, soma e média de duração, soma de MB
                
                soma_duracao = 0
                soma_mb = 0
                
                for musica_atual in musicas:
                    soma_duracao = soma_duracao + musica_atual [IND_DURACAO_SEG]
                    soma_mb = soma_mb + musica_atual [IND_TAMANHO_MB]
                    
                
                total = len(musicas)
                media_duracao = soma_duracao / total
                media_mb = soma_mb / total
                
                print("Total de músicas:", total)
                print("Duração somada:", soma_duracao, "segundos")
                print("Média de duração:", media_duracao,"segundos" )
                print("Espaço somado:", soma_mb, "MB")
                print("Média de espaço:", soma_mb % total, "MB por")
                
            elif tipo_relatorio == 2:
                    #---------- MAIS LONGA E MAIS CURTA ----------
                    # gurada a POSIIÇÃO, não o valor - para poder mostrar o nome depois
                    pos_longa = 0
                    pos_curta = 0
                    
                    for i in range(len(musicas)):
                        if musicas[i][IND_DURACAO_SEG] > musicas[pos_longa][IND_DURACAO_SEG]:
                            pos_longa = i
                        if musicas[i][IND_DURACAO_SEG] < musicas[pos_curta][IND_DURACAO_SEG]:
                            pos_curta = i
                            print("Mais longa:",musicas[pos_longa][IND_NOME], "-",
                                  musicas [pos_longa][IND_DURACAO_SEG], "segundos")
                            print("Mais curta:", musicas[pos_curta][IND_NOME], "-",
                                  musicas[pos_curta][IND_DURACAO_SEG], "segundos")
                            
                        
            elif tipo_relatorio == 3:
                #---------- QUANTIDADE POR GÊNERO ----------
                # um contador por gênero
                for genero_valido in generos_validos:
                    contador_genero = 0
                    for musica_atual in musicas:
                        if musica_atual[IND_GENERO] == genero_valido:
                            contador_genero = contador_genero + 1       
                    print(generos_validos, ":", contador_genero, "música(s)")
            
            elif tipo_relatorio == 4:
                #---------- ENVIADAS VS. FALHAS ----------
                # dois contadores separados, decidios por um if no status
                
                qtd_enviadas = 0
                qtd_falhas = 0
                
                for musicas_atual in musicas:
                    if musicas_atual[IND_STATUS] == "enviado":
                        qtd_enviadas = qtd_enviadas + 1
                    else:
                        qtd_falhas = qtd_falhas + 1
                        
                    print("Enviadas:", qtd_enviadas)
                    print("Falhas:", qtd_falhas)
                    if len(musicas) > 0:
                        percentual = (qtd_enviadas * 100) / len(musicas)
                        print("Percentual de sucesso:", percentual, "%")
            else:
                print("Tipo de relatório inválido.")
    else:
        print("Opção inválida")            