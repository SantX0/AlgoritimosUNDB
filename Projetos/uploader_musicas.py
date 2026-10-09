# ============ UPLOADER DE MÚSICAS - CRUD SEM LISTAS ============
# Usa apenas: variáveis simples, if/elif/else, while, for..range,
# input/print, int(), float(), str(), try/except e operadores.
# Capacidade fixa: 3 músicas (slots), cada um com variáveis próprias.

# ---------- LISTAS DE VALIDAÇÃO (viraram comparações) ----------
# gêneros aceitos: Rock, Pop, Sertanejo, Rap, Eletronica, MPB
# tipos aceitos:   mp3, wav, flac, m4a

# ---------- ARMAZENAMENTO (3 slots, 1 bloco de variáveis por slot) ----------
# slot 1
id1 = 0
genero1 = ""
artista1 = ""
nome1 = ""
durSeg1 = 0
diaLanc1 = 0
mesLanc1 = 0
anoLanc1 = 0
horaLanc1 = 0
minLanc1 = 0
autor1a = ""
autor1b = ""
prod1a = ""
prod1b = ""
tipoArq1 = ""
tamMB1 = 0.0
nomeArq1 = ""
status1 = ""
ocupado1 = 0
# slot 2
id2 = 0
genero2 = ""
artista2 = ""
nome2 = ""
durSeg2 = 0
diaLanc2 = 0
mesLanc2 = 0
anoLanc2 = 0
horaLanc2 = 0
minLanc2 = 0
autor2a = ""
autor2b = ""
prod2a = ""
prod2b = ""
tipoArq2 = ""
tamMB2 = 0.0
nomeArq2 = ""
status2 = ""
ocupado2 = 0
# slot 3
id3 = 0
genero3 = ""
artista3 = ""
nome3 = ""
durSeg3 = 0
diaLanc3 = 0
mesLanc3 = 0
anoLanc3 = 0
horaLanc3 = 0
minLanc3 = 0
autor3a = ""
autor3b = ""
prod3a = ""
prod3b = ""
tipoArq3 = ""
tamMB3 = 0.0
nomeArq3 = ""
status3 = ""
ocupado3 = 0

proximo_id = 1

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

    opcao = -1
    try:
        opcao = int(input("Escolha uma opção:\n"))
    except ValueError:
        opcao = -1

    if opcao < 1 or opcao > 7:
        print("Opção inválida! Digite um número de 1 a 7.")

    elif opcao == 1:
        # ============ CADASTRAR MÚSICA ============
        print("----- NOVO UPLOAD -----")

        # ---------- achar slot livre ----------
        slot_livre = 0
        if ocupado1 == 0:
            slot_livre = 1
        elif ocupado2 == 0:
            slot_livre = 2
        elif ocupado3 == 0:
            slot_livre = 3

        if slot_livre == 0:
            print("Armazenamento cheio! Sem listas a capacidade é fixa em 3 músicas.")
        else:
            # ---------- GÊNERO (validação por comparação, sem lista) ----------
            while True:
                generoNome = input("Gêneros aceitos: Rock, Pop, Sertanejo, Rap, Eletronica, MPB\nDigite o gênero:\n")
                if generoNome != "Rock" and generoNome != "Pop" and generoNome != "Sertanejo" and generoNome != "Rap" and generoNome != "Eletronica" and generoNome != "MPB":
                    print("Gênero inválido! Escolha um da lista (escreva exatamente igual).")
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

            # ---------- DURAÇÃO (try/except no lugar do isdigit) ----------
            while True:
                try:
                    duracaoSeg = int(input("Duração em segundos:\n"))
                    if duracaoSeg <= 0:
                        print("A duração deve ser maior que zero.")
                    else:
                        break
                except ValueError:
                    print("Digite apenas números.")

            # ---------- DATA DE LANÇAMENTO ----------
            while True:
                try:
                    diaLancamento = int(input("Dia de lançamento:\n"))
                    mesLancamento = int(input("Mês de lançamento:\n"))
                    anoLancamento = int(input("Ano de lançamento:\n"))
                    if (
                        diaLancamento < 1
                        or diaLancamento > 31
                        or mesLancamento < 1
                        or mesLancamento > 12
                        or anoLancamento < 1900
                    ):
                        print("Data inválida! Dia 1-31, mês 1-12, ano <1900.")
                    else:
                        break
                except ValueError:
                    print("Digite apenas números na data.")

            # ---------- HORA DE LANÇAMENTO ----------
            while True:
                try:
                    horaLancamento = int(input("Hora de lançamento:\n"))
                    minutoLancamento = int(input("Minuto de lançamento:\n"))
                    if (
                        horaLancamento < 0
                        or horaLancamento > 23
                        or minutoLancamento < 0
                        or minutoLancamento > 59
                    ):
                        print("Hora inválida! Hora 0 a 23, minutos 0 a 59.")
                    else:
                        break
                except ValueError:
                    print("Digite apenas números na hora.")

            # ---------- AUTORES (máximo 2, sem lista) ----------
            autorA = input("Digite o 1º autor (Enter se não houver):\n")
            querOutro = input("Deseja adicionar outro autor? (s/n):\n")
            while querOutro != "s" and querOutro != "S" and querOutro != "n" and querOutro != "N":
                querOutro = input("Responda 's' ou 'n':\n")
            if querOutro == "s" or querOutro == "S":
                autorB = input("Digite o 2º autor:\n")
            else:
                autorB = ""

            # ---------- PRODUTORES (máximo 2, sem lista) ----------
            produtorA = input("Digite o 1º produtor (Enter se não houver):\n")
            querOutro = input("Deseja adicionar outro produtor? (s/n):\n")
            while querOutro != "s" and querOutro != "S" and querOutro != "n" and querOutro != "N":
                querOutro = input("Responda 's' ou 'n':\n")
            if querOutro == "s" or querOutro == "S":
                produtorB = input("Digite o 2º produtor:\n")
            else:
                produtorB = ""

            # ---------- TIPO DE ARQUIVO (comparação encadeada, sem lista) ----------
            while True:
                arquivoTipo = input("Tipos aceitos: mp3, wav, flac, m4a\nTipo de arquivo:\n")
                if arquivoTipo != "mp3" and arquivoTipo != "wav" and arquivoTipo != "flac" and arquivoTipo != "m4a":
                    print("Tipo inválido! Use um da lista (escreva em minúsculas).")
                else:
                    break

            # ---------- TAMANHO DO ARQUIVO ----------
            while True:
                try:
                    tamanhoMB = float(input("Tamanho do arquivo em MB (ex: 8.5):\n"))
                    if tamanhoMB <= 0:
                        print("O tamanho deve ser maior que zero.")
                    else:
                        break
                except ValueError:
                    print("Digite apenas números (use ponto para decimais).")

            # ---------- NOME DO ARQUIVO ----------
            while True:
                nomeArquivo = input("Digite o nome do arquivo (ex: santxo.mp3):\n")
                if nomeArquivo != "":
                    break
                print("O nome do arquivo não pode estar vazio")

            # ---------- REGRA DE APROVAÇÃO DO UPLOAD ----------
            if tamanhoMB <= 50:
                statusNovo = "enviado"
            else:
                statusNovo = "falhou"
                print("Arquivo muito grande! Limite de 50 MB.")

            # ---------- GRAVA NO SLOT LIVRE (sem append: atribuição por slot) ----------
            if slot_livre == 1:
                id1 = proximo_id
                genero1 = generoNome
                artista1 = artistasNome
                nome1 = musicaNome
                durSeg1 = duracaoSeg
                diaLanc1 = diaLancamento
                mesLanc1 = mesLancamento
                anoLanc1 = anoLancamento
                horaLanc1 = horaLancamento
                minLanc1 = minutoLancamento
                autor1a = autorA
                autor1b = autorB
                prod1a = produtorA
                prod1b = produtorB
                tipoArq1 = arquivoTipo
                tamMB1 = tamanhoMB
                nomeArq1 = nomeArquivo
                status1 = statusNovo
                ocupado1 = 1
            elif slot_livre == 2:
                id2 = proximo_id
                genero2 = generoNome
                artista2 = artistasNome
                nome2 = musicaNome
                durSeg2 = duracaoSeg
                diaLanc2 = diaLancamento
                mesLanc2 = mesLancamento
                anoLanc2 = anoLancamento
                horaLanc2 = horaLancamento
                minLanc2 = minutoLancamento
                autor2a = autorA
                autor2b = autorB
                prod2a = produtorA
                prod2b = produtorB
                tipoArq2 = arquivoTipo
                tamMB2 = tamanhoMB
                nomeArq2 = nomeArquivo
                status2 = statusNovo
                ocupado2 = 1
            else:
                id3 = proximo_id
                genero3 = generoNome
                artista3 = artistasNome
                nome3 = musicaNome
                durSeg3 = duracaoSeg
                diaLanc3 = diaLancamento
                mesLanc3 = mesLancamento
                anoLanc3 = anoLancamento
                horaLanc3 = horaLancamento
                minLanc3 = minutoLancamento
                autor3a = autorA
                autor3b = autorB
                prod3a = produtorA
                prod3b = produtorB
                tipoArq3 = arquivoTipo
                tamMB3 = tamanhoMB
                nomeArq3 = nomeArquivo
                status3 = statusNovo
                ocupado3 = 1

            print("Upload registrado! ID da musica:", proximo_id)
            if statusNovo == "enviado":
                print("Status: ENVIADO com sucesso.")
            else:
                print("Status: FALHOU (arquivo acima do limite).")
            proximo_id = proximo_id + 1

    elif opcao == 2:
        # ============ LISTAR MÚSICAS ============
        totalMusicas = ocupado1 + ocupado2 + ocupado3
        if totalMusicas == 0:
            print("Nenhuma música cadastrada ainda")
        else:
            print("===== LISTA DE MÚSICAS =====")
            contador = 0
            # slot 1
            if ocupado1 == 1:
                minutos = durSeg1 // 60
                segundos = durSeg1 % 60
                if segundos < 10:
                    segTexto = "0" + str(segundos)
                else:
                    segTexto = str(segundos)
                print(contador, "| ID:", id1, "|", nome1, "| Artista:", artista1, "| Gênero:", genero1, "| Duração:", str(minutos) + ":" + segTexto, "| Status:", status1)
                contador = contador + 1
            # slot 2
            if ocupado2 == 1:
                minutos = durSeg2 // 60
                segundos = durSeg2 % 60
                if segundos < 10:
                    segTexto = "0" + str(segundos)
                else:
                    segTexto = str(segundos)
                print(contador, "| ID:", id2, "|", nome2, "| Artista:", artista2, "| Gênero:", genero2, "| Duração:", str(minutos) + ":" + segTexto, "| Status:", status2)
                contador = contador + 1
            # slot 3
            if ocupado3 == 1:
                minutos = durSeg3 // 60
                segundos = durSeg3 % 60
                if segundos < 10:
                    segTexto = "0" + str(segundos)
                else:
                    segTexto = str(segundos)
                print(contador, "| ID:", id3, "|", nome3, "| Artista:", artista3, "| Gênero:", genero3, "| Duração:", str(minutos) + ":" + segTexto, "| Status:", status3)
                contador = contador + 1
            print("Total:", totalMusicas, "música(s).")
        print()

    elif opcao == 3:
        # ============ BUSCAR MÚSICA ============
        totalMusicas = ocupado1 + ocupado2 + ocupado3
        if totalMusicas == 0:
            print("Nenhuma música cadastrada ainda.")
        else:
            print("---- BUSCA ----")
            print("1 - Buscar por ID")
            print("2 - Buscar por Artista")
            print("3 - Buscar por Nome")
            print("4 - Buscar por Gênero")
            print("5 - Busca Combinada (gênero e duração mínima)")
            try:
                tipo_busca = int(input("Escolha o tipo de busca:\n"))
            except ValueError:
                tipo_busca = -1

            if tipo_busca == 1:
                # ---------- Busca por ID ----------
                try:
                    id_busca = int(input("Digite o ID:\n"))
                except ValueError:
                    id_busca = -1

                slot_achado = 0
                if ocupado1 == 1 and id1 == id_busca:
                    slot_achado = 1
                elif ocupado2 == 1 and id2 == id_busca:
                    slot_achado = 2
                elif ocupado3 == 1 and id3 == id_busca:
                    slot_achado = 3

                if slot_achado == 0:
                    print("Nenhuma música foi encontrada com ID", id_busca, ".")
                else:
                    if slot_achado == 1:
                        print("Encontrada:", nome1, "-", artista1, "-", status1)
                    elif slot_achado == 2:
                        print("Encontrada:", nome2, "-", artista2, "-", status2)
                    else:
                        print("Encontrada:", nome3, "-", artista3, "-", status3)

            elif tipo_busca == 2 or tipo_busca == 3 or tipo_busca == 4:
                # ---------- Busca por texto (comparação com o operador in) ----------
                if tipo_busca == 2:
                    termo_busca = input("Digite parte do artista:\n")
                elif tipo_busca == 3:
                    termo_busca = input("Digite parte do nome:\n")
                else:
                    termo_busca = input("Digite o gênero:\n")

                qtdAchadas = 0
                # slot 1
                if ocupado1 == 1:
                    if tipo_busca == 2:
                        campoTexto = artista1
                    elif tipo_busca == 3:
                        campoTexto = nome1
                    else:
                        campoTexto = genero1
                    if termo_busca in campoTexto:
                        print("ID:", id1, "|", nome1, "|", artista1, "|", genero1)
                        qtdAchadas = qtdAchadas + 1
                # slot 2
                if ocupado2 == 1:
                    if tipo_busca == 2:
                        campoTexto = artista2
                    elif tipo_busca == 3:
                        campoTexto = nome2
                    else:
                        campoTexto = genero2
                    if termo_busca in campoTexto:
                        print("ID:", id2, "|", nome2, "|", artista2, "|", genero2)
                        qtdAchadas = qtdAchadas + 1
                # slot 3
                if ocupado3 == 1:
                    if tipo_busca == 2:
                        campoTexto = artista3
                    elif tipo_busca == 3:
                        campoTexto = nome3
                    else:
                        campoTexto = genero3
                    if termo_busca in campoTexto:
                        print("ID:", id3, "|", nome3, "|", artista3, "|", genero3)
                        qtdAchadas = qtdAchadas + 1

                if qtdAchadas == 0:
                    print("Nenhum resultado para '", termo_busca, "'.")

            elif tipo_busca == 5:
                # ---------- Busca combinada ----------
                genero_busca = input("Digite o gênero:\n")
                try:
                    duracao_minima = int(input("Duração mínima em segundos:\n"))
                except ValueError:
                    duracao_minima = -1

                qtdAchadas = 0
                if ocupado1 == 1 and genero1 == genero_busca and durSeg1 >= duracao_minima:
                    print(nome1, "-", durSeg1, "segundos")
                    qtdAchadas = qtdAchadas + 1
                if ocupado2 == 1 and genero2 == genero_busca and durSeg2 >= duracao_minima:
                    print(nome2, "-", durSeg2, "segundos")
                    qtdAchadas = qtdAchadas + 1
                if ocupado3 == 1 and genero3 == genero_busca and durSeg3 >= duracao_minima:
                    print(nome3, "-", durSeg3, "segundos")
                    qtdAchadas = qtdAchadas + 1

                if qtdAchadas == 0:
                    print("Nenhuma música combina com os 2 critérios.")

            else:
                print("Tipo de busca inválida.")

    elif opcao == 4:
        # ============ ATUALIZAR MÚSICA ============
        totalMusicas = ocupado1 + ocupado2 + ocupado3
        if totalMusicas == 0:
            print("Nenhuma música cadastrada.")
        else:
            try:
                id_busca = int(input("Digite o ID da música que você está procurando:\n"))
            except ValueError:
                id_busca = -1

            slot_achado = 0
            if ocupado1 == 1 and id1 == id_busca:
                slot_achado = 1
            elif ocupado2 == 1 and id2 == id_busca:
                slot_achado = 2
            elif ocupado3 == 1 and id3 == id_busca:
                slot_achado = 3

            if slot_achado == 0:
                print("Nenhuma música com ID", id_busca, ".")
            else:
                # ---------- Mostrar a música atual ----------
                if slot_achado == 1:
                    print("Gênero:", genero1, "| Artista:", artista1, "| Nome:", nome1, "| Duração(seg):", durSeg1, "| Data:", str(diaLanc1) + "/" + str(mesLanc1) + "/" + str(anoLanc1), "| Hora:", str(horaLanc1) + ":" + str(minLanc1), "| Autores:", autor1a, "e", autor1b, "| Produtores:", prod1a, "e", prod1b, "| Tipo/Tamanho:", tipoArq1, "-", tamMB1, "MB", "| Arquivo:", nomeArq1)
                elif slot_achado == 2:
                    print("Gênero:", genero2, "| Artista:", artista2, "| Nome:", nome2, "| Duração(seg):", durSeg2, "| Data:", str(diaLanc2) + "/" + str(mesLanc2) + "/" + str(anoLanc2), "| Hora:", str(horaLanc2) + ":" + str(minLanc2), "| Autores:", autor2a, "e", autor2b, "| Produtores:", prod2a, "e", prod2b, "| Tipo/Tamanho:", tipoArq2, "-", tamMB2, "MB", "| Arquivo:", nomeArq2)
                else:
                    print("Gênero:", genero3, "| Artista:", artista3, "| Nome:", nome3, "| Duração(seg):", durSeg3, "| Data:", str(diaLanc3) + "/" + str(mesLanc3) + "/" + str(anoLanc3), "| Hora:", str(horaLanc3) + ":" + str(minLanc3), "| Autores:", autor3a, "e", autor3b, "| Produtores:", prod3a, "e", prod3b, "| Tipo/Tamanho:", tipoArq3, "-", tamMB3, "MB", "| Arquivo:", nomeArq3)

                # ---------- Submenu: qual campo alterar ----------
                print("1 - Gênero")
                print("2 - Artista")
                print("3 - Nome da Música")
                print("4 - Duração")
                print("5 - Data De Lançamento")
                print("6 - Hora De Lançamento")
                print("7 - Autores")
                print("8 - Produtores")
                print("9 - Tipo De Arquivo (e tamanho)")
                print("10 - Nome Do Arquivo")
                try:
                    campo_escolhido = int(input("Qual campo deseja alterar? (0 para cancelar):\n"))
                except ValueError:
                    campo_escolhido = -1

                if campo_escolhido == 0:
                    print("Atualização cancelada.")

                elif campo_escolhido == 1:
                    while True:
                        generoNovo = input("Gêneros aceitos: Rock, Pop, Sertanejo, Rap, Eletronica, MPB\nDigite o gênero:\n")
                        if generoNovo != "Rock" and generoNovo != "Pop" and generoNovo != "Sertanejo" and generoNovo != "Rap" and generoNovo != "Eletronica" and generoNovo != "MPB":
                            print("Gênero inválido! Escolha um da lista.")
                        else:
                            break
                    if slot_achado == 1:
                        genero1 = generoNovo
                    elif slot_achado == 2:
                        genero2 = generoNovo
                    else:
                        genero3 = generoNovo
                    print("Música atualizada com sucesso!")

                elif campo_escolhido == 2:
                    while True:
                        artistaNovo = input("Novo artista:\n")
                        if artistaNovo != "":
                            break
                        print("O artista não pode ficar vazio.")
                    if slot_achado == 1:
                        artista1 = artistaNovo
                    elif slot_achado == 2:
                        artista2 = artistaNovo
                    else:
                        artista3 = artistaNovo
                    print("Música atualizada com sucesso!")

                elif campo_escolhido == 3:
                    while True:
                        nomeNovo = input("Novo nome da música:\n")
                        if nomeNovo != "":
                            break
                        print("O nome não pode ficar vazio.")
                    if slot_achado == 1:
                        nome1 = nomeNovo
                    elif slot_achado == 2:
                        nome2 = nomeNovo
                    else:
                        nome3 = nomeNovo
                    print("Música atualizada com sucesso!")

                elif campo_escolhido == 4:
                    while True:
                        try:
                            duracaoNova = int(input("Nova duração em segundos:\n"))
                            if duracaoNova <= 0:
                                print("A duração deve ser maior que zero.")
                            else:
                                break
                        except ValueError:
                            print("Digite apenas números.")
                    if slot_achado == 1:
                        durSeg1 = duracaoNova
                    elif slot_achado == 2:
                        durSeg2 = duracaoNova
                    else:
                        durSeg3 = duracaoNova
                    print("Música atualizada com sucesso!")

                elif campo_escolhido == 5:
                    while True:
                        try:
                            diaNovo = int(input("Novo dia de lançamento:\n"))
                            mesNovo = int(input("Novo mês de lançamento:\n"))
                            anoNovo = int(input("Novo ano de lançamento:\n"))
                            if diaNovo < 1 or diaNovo > 31 or mesNovo < 1 or mesNovo > 12 or anoNovo < 1900:
                                print("Data inválida! Dia 1-31, mês 1-12, ano <1900.")
                            else:
                                break
                        except ValueError:
                            print("Digite apenas números na data.")
                    if slot_achado == 1:
                        diaLanc1 = diaNovo
                        mesLanc1 = mesNovo
                        anoLanc1 = anoNovo
                    elif slot_achado == 2:
                        diaLanc2 = diaNovo
                        mesLanc2 = mesNovo
                        anoLanc2 = anoNovo
                    else:
                        diaLanc3 = diaNovo
                        mesLanc3 = mesNovo
                        anoLanc3 = anoNovo
                    print("Música atualizada com sucesso!")

                elif campo_escolhido == 6:
                    while True:
                        try:
                            horaNova = int(input("Nova hora de lançamento:\n"))
                            minutoNovo = int(input("Novo minuto de lançamento:\n"))
                            if horaNova < 0 or horaNova > 23 or minutoNovo < 0 or minutoNovo > 59:
                                print("Hora inválida! Hora 0 a 23, minutos 0 a 59.")
                            else:
                                break
                        except ValueError:
                            print("Digite apenas números na hora.")
                    if slot_achado == 1:
                        horaLanc1 = horaNova
                        minLanc1 = minutoNovo
                    elif slot_achado == 2:
                        horaLanc2 = horaNova
                        minLanc2 = minutoNovo
                    else:
                        horaLanc3 = horaNova
                        minLanc3 = minutoNovo
                    print("Música atualizada com sucesso!")

                elif campo_escolhido == 7:
                    autorA = input("Digite o 1º autor (Enter se não houver):\n")
                    querOutro = input("Deseja adicionar outro autor? (s/n):\n")
                    while querOutro != "s" and querOutro != "S" and querOutro != "n" and querOutro != "N":
                        querOutro = input("Responda 's' ou 'n':\n")
                    if querOutro == "s" or querOutro == "S":
                        autorB = input("Digite o 2º autor:\n")
                    else:
                        autorB = ""
                    if slot_achado == 1:
                        autor1a = autorA
                        autor1b = autorB
                    elif slot_achado == 2:
                        autor2a = autorA
                        autor2b = autorB
                    else:
                        autor3a = autorA
                        autor3b = autorB
                    print("Música atualizada com sucesso!")

                elif campo_escolhido == 8:
                    produtorA = input("Digite o 1º produtor (Enter se não houver):\n")
                    querOutro = input("Deseja adicionar outro produtor? (s/n):\n")
                    while querOutro != "s" and querOutro != "S" and querOutro != "n" and querOutro != "N":
                        querOutro = input("Responda 's' ou 'n':\n")
                    if querOutro == "s" or querOutro == "S":
                        produtorB = input("Digite o 2º produtor:\n")
                    else:
                        produtorB = ""
                    if slot_achado == 1:
                        prod1a = produtorA
                        prod1b = produtorB
                    elif slot_achado == 2:
                        prod2a = produtorA
                        prod2b = produtorB
                    else:
                        prod3a = produtorA
                        prod3b = produtorB
                    print("Música atualizada com sucesso!")

                elif campo_escolhido == 9:
                    # ---------- tipo + tamanho: recalcula o STATUS ----------
                    while True:
                        tipoNovo = input("Tipos aceitos: mp3, wav, flac, m4a\nTipo de arquivo:\n")
                        if tipoNovo != "mp3" and tipoNovo != "wav" and tipoNovo != "flac" and tipoNovo != "m4a":
                            print("Tipo inválido! Use um da lista.")
                        else:
                            break
                    while True:
                        try:
                            tamanhoNovo = float(input("Novo tamanho em MB (ex: 8.5):\n"))
                            if tamanhoNovo <= 0:
                                print("O tamanho deve ser maior que zero.")
                            else:
                                break
                        except ValueError:
                            print("Digite apenas números (use ponto para decimais).")

                    if tamanhoNovo <= 50:
                        statusNovo = "enviado"
                    else:
                        statusNovo = "falhou"

                    if slot_achado == 1:
                        tipoArq1 = tipoNovo
                        tamMB1 = tamanhoNovo
                        status1 = statusNovo
                    elif slot_achado == 2:
                        tipoArq2 = tipoNovo
                        tamMB2 = tamanhoNovo
                        status2 = statusNovo
                    else:
                        tipoArq3 = tipoNovo
                        tamMB3 = tamanhoNovo
                        status3 = statusNovo
                    print("Música atualizada com sucesso!")

                elif campo_escolhido == 10:
                    while True:
                        nomeArquivoNovo = input("Novo nome do arquivo:\n")
                        if nomeArquivoNovo != "":
                            break
                        print("O nome do arquivo não pode ficar vazio.")
                    if slot_achado == 1:
                        nomeArq1 = nomeArquivoNovo
                    elif slot_achado == 2:
                        nomeArq2 = nomeArquivoNovo
                    else:
                        nomeArq3 = nomeArquivoNovo
                    print("Música atualizada com sucesso!")

                else:
                    print("Campo inválido. Nada foi alterado.")

    elif opcao == 5:
        # ============ EXCLUIR MÚSICA (exclusão lógica: o slot é liberado) ============
        totalMusicas = ocupado1 + ocupado2 + ocupado3
        if totalMusicas == 0:
            print("Nenhuma música cadastrada.")
        else:
            try:
                id_busca = int(input("Digite o ID da música que deseja excluir:\n"))
            except ValueError:
                id_busca = -1

            slot_achado = 0
            if ocupado1 == 1 and id1 == id_busca:
                slot_achado = 1
            elif ocupado2 == 1 and id2 == id_busca:
                slot_achado = 2
            elif ocupado3 == 1 and id3 == id_busca:
                slot_achado = 3

            if slot_achado == 0:
                print("Nenhuma música com ID", id_busca, ".")
            else:
                if slot_achado == 1:
                    print("Você está prestes a excluir:", nome1, "-", artista1)
                elif slot_achado == 2:
                    print("Você está prestes a excluir:", nome2, "-", artista2)
                else:
                    print("Você está prestes a excluir:", nome3, "-", artista3)

                while True:
                    confirmacao = input("Confirma a exclusão? (s/n):\n")
                    if confirmacao == "s" or confirmacao == "S" or confirmacao == "n" or confirmacao == "N":
                        break
                    print("Responda apenas 's' ou 'n'.")

                if confirmacao == "s" or confirmacao == "S":
                    if slot_achado == 1:
                        ocupado1 = 0
                    elif slot_achado == 2:
                        ocupado2 = 0
                    else:
                        ocupado3 = 0
                    print("Música excluída com sucesso.")
                    # OBS: proximo_id NÃO volta atrás — IDs nunca se repetem
                else:
                    print("Exclusão cancelada.")

    elif opcao == 6:
        # ============ OPÇÃO 6 - SAIR ============
        print("Encerrando o programa. Até mais!")
        break

    elif opcao == 7:
        # ============ RELATÓRIOS ============
        totalMusicas = ocupado1 + ocupado2 + ocupado3
        if totalMusicas == 0:
            print("Nenhuma música cadastrada.")
        else:
            print("======= RELATÓRIOS ========")
            print("1 - Resumo Geral")
            print("2 - Música mais longa e mais curta")
            print("3 - Quantidade por gênero")
            print("4 - Enviadas vs Falhas")
            try:
                tipo_relatorio = int(input("Escolha:\n"))
            except ValueError:
                tipo_relatorio = -1

            if tipo_relatorio == 1:
                #---------- RESUMO GERAL ----------
                soma_duracao = 0
                soma_mb = 0.0
                if ocupado1 == 1:
                    soma_duracao = soma_duracao + durSeg1
                    soma_mb = soma_mb + tamMB1
                if ocupado2 == 1:
                    soma_duracao = soma_duracao + durSeg2
                    soma_mb = soma_mb + tamMB2
                if ocupado3 == 1:
                    soma_duracao = soma_duracao + durSeg3
                    soma_mb = soma_mb + tamMB3

                media_duracao = soma_duracao / totalMusicas
                media_mb = soma_mb / totalMusicas

                print("Total de músicas:", totalMusicas)
                print("Duração somada:", soma_duracao, "segundos")
                print("Média de duração:", media_duracao, "segundos")
                print("Espaço somado:", soma_mb, "MB")
                print("Média de espaço:", media_mb, "MB por música")

            elif tipo_relatorio == 2:
                #---------- MAIS LONGA E MAIS CURTA ----------
                # acumulador de posição: -1 = "nenhuma ainda"; passa por todos os slots
                pos_longa = 0
                dur_longa = -1
                pos_curta = 0
                dur_curta = -1

                if ocupado1 == 1 and durSeg1 > dur_longa:
                    pos_longa = 1
                    dur_longa = durSeg1
                if ocupado2 == 1 and durSeg2 > dur_longa:
                    pos_longa = 2
                    dur_longa = durSeg2
                if ocupado3 == 1 and durSeg3 > dur_longa:
                    pos_longa = 3
                    dur_longa = durSeg3

                if ocupado1 == 1 and (dur_curta == -1 or durSeg1 < dur_curta):
                    pos_curta = 1
                    dur_curta = durSeg1
                if ocupado2 == 1 and (dur_curta == -1 or durSeg2 < dur_curta):
                    pos_curta = 2
                    dur_curta = durSeg2
                if ocupado3 == 1 and (dur_curta == -1 or durSeg3 < dur_curta):
                    pos_curta = 3
                    dur_curta = durSeg3

                if pos_longa == 1:
                    print("Mais longa:", nome1, "-", durSeg1, "segundos")
                elif pos_longa == 2:
                    print("Mais longa:", nome2, "-", durSeg2, "segundos")
                else:
                    print("Mais longa:", nome3, "-", durSeg3, "segundos")

                if pos_curta == 1:
                    print("Mais curta:", nome1, "-", durSeg1, "segundos")
                elif pos_curta == 2:
                    print("Mais curta:", nome2, "-", durSeg2, "segundos")
                else:
                    print("Mais curta:", nome3, "-", durSeg3, "segundos")

            elif tipo_relatorio == 3:
                #---------- QUANTIDADE POR GÊNERO ----------
                # o contador se ancora nos gêneros válidos, um por vez
                gAtual = ""
                g = 1
                while g <= 6:
                    if g == 1:
                        gAtual = "Rock"
                    elif g == 2:
                        gAtual = "Pop"
                    elif g == 3:
                        gAtual = "Sertanejo"
                    elif g == 4:
                        gAtual = "Rap"
                    elif g == 5:
                        gAtual = "Eletronica"
                    else:
                        gAtual = "MPB"

                    contador_genero = 0
                    if ocupado1 == 1 and genero1 == gAtual:
                        contador_genero = contador_genero + 1
                    if ocupado2 == 1 and genero2 == gAtual:
                        contador_genero = contador_genero + 1
                    if ocupado3 == 1 and genero3 == gAtual:
                        contador_genero = contador_genero + 1

                    print(gAtual, ":", contador_genero, "música(s)")
                    g = g + 1

            elif tipo_relatorio == 4:
                #---------- ENVIADAS VS. FALHAS ----------
                qtd_enviadas = 0
                qtd_falhas = 0
                if ocupado1 == 1:
                    if status1 == "enviado":
                        qtd_enviadas = qtd_enviadas + 1
                    else:
                        qtd_falhas = qtd_falhas + 1
                if ocupado2 == 1:
                    if status2 == "enviado":
                        qtd_enviadas = qtd_enviadas + 1
                    else:
                        qtd_falhas = qtd_falhas + 1
                if ocupado3 == 1:
                    if status3 == "enviado":
                        qtd_enviadas = qtd_enviadas + 1
                    else:
                        qtd_falhas = qtd_falhas + 1

                print("Enviadas:", qtd_enviadas)
                print("Falhas:", qtd_falhas)
                percentual = (qtd_enviadas * 100) / totalMusicas
                print("Percentual de sucesso:", percentual, "%")

            else:
                print("Tipo de relatório inválido.")
