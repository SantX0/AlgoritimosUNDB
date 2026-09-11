# ============ LISTAS DE VALIDAÇÃO ============
generos_validos = ["Rock","Pop","Sertanejo", "Rap", "Eletronica", "MPB"]
tipos_permitidos = ["mp3", "wav", "flac", "m4a"]

# ---------- ARMAZENAMENTO ----------
opcao = []
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
IND_NOME_ARQ = 14
IND_STATUS = 15

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

    opcao = input("Escolha uma opção: ")

    if not opcao.isdigit():
        print("Opção Invalida! Digite um numero de 1 a 6.")
    elif int (opcao) < 1 or int (opcao) > 6:
        print("Opção inválida! Digite um número de 1 a 6")
    elif int (opcao) == 1:
        print("Cadastrar")
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