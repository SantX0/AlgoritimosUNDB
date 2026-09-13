# ============ LISTAS DE VALIDAÇÃO ============
generos_validos = ["Rock","Pop","Sertanejo", "Rap", "Eletronica", "MPB"]
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
while True :
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
    elif int (opcao) < 1 or int (opcao) > 6:
        print("Opção inválida! Digite um número de 1 a 6")
    elif int (opcao) == 1:
        # CADASTRAR MÚSICA
        print("----- NOVO UPLOAD -----")
        while True:
            generosNome = input(f"Generos disponíveis {generos_validos}\nDigite o gênero:\n")
            if generosNome not in generos_validos:
                print("Gênero inválido! Escolha um da lista.")
            else:
                break
        # ---------- GÊNERO ----------
        while True:
            artistasNome= input("Artistas:\n")
            if artistasNome == "" :
                print("O nome do artista não pod ficar vazio!")
            else:
                break
        #---------- NOME DA MÚSICA ----------
        while True:
            musicaNome = input("Nome Music:\n")
            if musicaNome == "":
                print("O nome da música não pode ficar vazio.")
            else:
                break
        # ---------- DURAÇÃO ----------
        while True:
            durocaoMusica  = int (input("Duração em segundos:\n"))
            if durocaoMusica not in int :
                print("Digite apnes números. ")
            else:
                duracaoSeg = int
                if duracaoSeg <= 0:
                    print("A duração deve ser maor que zero.")
                else:
                    break
        #---------- DATA DE LANÇAMENTO ----------
        while True:
            diaLancamento = int(input("Dia de lançamento"))
            mesLançamento = int (input("Mês de lançamento"))
            anoLançamento = int (input ("Ano de lançamento"))
            if diaLancamento < 1 or diaLancamento > 31 or mesLançamento < 1 or mesLançamento > 31 or anoLançamento < 1900:
                print("Data invalida! Verifique o dia (1-31), o mês (1-12) e o ano (<1900)")
            else:
                break
        #---------- HORA DE LANÇAMENTO ----------
        while True:
            horaLancamento = int(input("Hora de lançamento:\n"))
            minutoLancamento = int (input("Minuto de lançamento:\n"))
            segundosLancamento = int(input ("Minuto de lançamento:\n"))
            if horaLancamento < 0 or horaLancamento > 23 or minutoLancamento < 0 or minutoLancamento > 59 or segundosLancamento < 0 or segundosLancamento > 59:
                print("Hora inválida! Verifique a hora (0 a 23), os minutos (0 a 59) e os segundos (0 a 59) ")
            else:
                break
        #---------- AUTORES ----------
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
        #---------- TIPO DE ARQUIVO ----------
        while True :
            arquivoTipo = input (f"Tipos aceitos:{tipos_permitidos}\nTipo de arquivo:" )
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
        #---------- MONTA A MÚSICA E GUARDA ----------
        novasMusicas = [proximo_id, generosNome, artistasNome, musicaNome, duracaoSeg, diaLancamento, mesLançamento, anoLançamento, horaLancamento, minutoLancamento, autoresMusic, prodMusic, arquivoTipo, tamanhoMB, nomeArquivo, status]
        musicas.append(novasMusicas)
        print("Upload registrado! ID da musica: ", proximo_id)
        if status == "enviado":
            print("Status: ENVIADO com sucesso")
        else:
            print("Status: FALHOU (arquivo acima do limite).")
        proximo_id == proximo_id + 1
        
    elif int (opcao) == 2:
        print("Listar")
    elif int (opcao) == 3:
        print("Buscar")
    elif int (opcao) == 4:
        print("Atualizar")
    elif int (opcao) == 5:
        print("Excluir")
    else:
        print("Encerrando o programa. Até uma proximma!")
        break