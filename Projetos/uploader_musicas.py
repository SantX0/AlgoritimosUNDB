# ============ UPLOADER DE MÚSICAS - CRUD ============
import json
from calendar import monthrange
from collections import Counter
from math import isfinite
from pathlib import Path
from tempfile import NamedTemporaryFile
# ============ MENU PRINCIPAL ============
def main():
    try:
        musicas, proximo_id = carregar_catalogo()
    except (OSError, ValueError, KeyError, TypeError) as erro:
        print(f"Não foi possível carregar o catálogo: {erro}")
        return 1

    consultas = {"2": listar_musicas, "3": buscar_musicas, "7": gerar_relatorio}
    while True:
        print(
            "===== UPLOADER DE MÚSICAS =====\n"
            "1 - Cadastrar música (upload)\n"
            "2 - Listar músicas\n"
            "3 - Buscar músicas\n"
            "4 - Atualizar música\n"
            "5 - Excluir música\n"
            "6 - Sair\n"
            "7 - Relatórios\n"
            "====================================="
        )
        opcao = input("Escolha uma opção:\n").strip()

        try:
            if opcao == "1":
                proximo_id = cadastrar_musica(musicas, proximo_id)
            elif opcao in consultas:
                consultas[opcao](musicas)
            elif opcao == "4":
                atualizar_musica(musicas, proximo_id)
            elif opcao == "5":
                excluir_musica(musicas, proximo_id)
            elif opcao == "6":
                print("Encerrando o programa. Até mais!")
                return 0
            else:
                print("Opção inválida! Digite um número de 1 a 7.")
        except OSError as erro:
            print(f"Não foi possível salvar o catálogo: {erro}")

# ---------- LISTAS DE VALIDAÇÃO ----------
GENEROS_VALIDOS = ("Rock", "Pop", "Sertanejo", "Rap", "Eletronica", "MPB")
FORMATOS_PERMITIDOS = ("mp3", "wav", "flac", "m4a")
LIMITE_MB = 50
ARQUIVO_CATALOGO = Path(__file__).resolve().with_name("musicas.json")


def carregar_catalogo():
    try:
        with ARQUIVO_CATALOGO.open(encoding="utf-8") as arquivo:
            catalogo = json.load(arquivo)
    except FileNotFoundError:
        return [], 1

    musicas = catalogo["musicas"]
    proximo_id = catalogo["proximo_id"]
    if not isinstance(musicas, list) or type(proximo_id) is not int or proximo_id < 1:
        raise ValueError("Estrutura do catálogo inválida.")
    if proximo_id <= max((musica["id"] for musica in musicas), default=0):
        raise ValueError("O próximo ID deve ser maior que os IDs cadastrados.")
    return musicas, proximo_id


def salvar_catalogo(musicas, proximo_id):
    catalogo = {"musicas": musicas, "proximo_id": proximo_id}
    caminho_temporario = None
    try:
        with NamedTemporaryFile(
            mode="w", encoding="utf-8", dir=ARQUIVO_CATALOGO.parent, delete=False
        ) as arquivo:
            caminho_temporario = Path(arquivo.name)
            json.dump(catalogo, arquivo, ensure_ascii=False, indent=2)
            arquivo.write("\n")
        caminho_temporario.replace(ARQUIVO_CATALOGO)
        caminho_temporario = None
    finally:
        if caminho_temporario is not None:
            caminho_temporario.unlink(missing_ok=True)


def ler_texto(pergunta, erro):
    while True:
        texto = input(pergunta).strip()
        if texto:
            return texto
        print(erro)


def ler_opcao(pergunta, opcoes, erro):
    opcoes_normalizadas = {opcao.casefold(): opcao for opcao in opcoes}
    while True:
        escolha = input(pergunta).strip().casefold()
        if escolha in opcoes_normalizadas:
            return opcoes_normalizadas[escolha]
        print(erro)


def ler_genero():
    return ler_opcao(
        f"Gêneros disponíveis: {', '.join(GENEROS_VALIDOS)}\nDigite o gênero:\n",
        GENEROS_VALIDOS,
        "Gênero inválido! Escolha um da lista.",
    )


def ler_duracao():
    while True:
        duracao = ler_inteiro("Duração em segundos:\n", "Digite apenas números.")
        if duracao is None:
            continue
        if duracao > 0:
            return duracao
        print("A duração deve ser maior que zero.")


def ler_inteiro(pergunta, erro):
    texto = input(pergunta).strip()
    if texto.isdecimal():
        try:
            return int(texto)
        except ValueError:
            pass
    print(erro)
    return None


def ler_data():
    erro = "Data inválida! Informe uma data existente com ano a partir de 1900."
    while True:
        dia = input("Dia de lançamento:\n").strip()
        mes = input("Mês de lançamento:\n").strip()
        ano = input("Ano de lançamento:\n").strip()

        if not all(valor.isdecimal() for valor in (dia, mes, ano)):
            print("Digite apenas números na data.")
            continue
        try:
            dia, mes, ano = int(dia), int(mes), int(ano)
        except ValueError:
            print(erro)
            continue
        if ano >= 1900 and 1 <= mes <= 12 and 1 <= dia <= monthrange(ano, mes)[1]:
            return {"dia": dia, "mes": mes, "ano": ano}
        print(erro)


def ler_hora():
    erro = "Hora inválida! Verifique a hora (0 a 23) e os minutos (0 a 59)."
    while True:
        hora = input("Hora de lançamento:\n").strip()
        minuto = input("Minuto de lançamento:\n").strip()
        if not hora.isdecimal() or not minuto.isdecimal():
            print("Digite apenas números na hora.")
            continue
        try:
            hora, minuto = int(hora), int(minuto)
        except ValueError:
            print(erro)
            continue
        if 0 <= hora <= 23 and 0 <= minuto <= 59:
            return {"hora": hora, "minuto": minuto}
        print(erro)


def ler_nomes(funcao):
    nomes = []
    while True:
        nome = input(f"Digite {funcao} (ou 'fim' para encerrar):\n").strip()
        if nome.casefold() == "fim":
            return nomes
        if nome:
            nomes.append(nome)


def ler_tamanho():
    while True:
        texto = input("Tamanho do arquivo em MB (ex: 8,5 ou 8.5):\n")
        texto = texto.strip().replace(",", ".")
        if not texto.replace(".", "", 1).isdecimal():
            print("Digite um número usando vírgula ou ponto para decimais.")
            continue
        tamanho = float(texto)
        if not isfinite(tamanho) or tamanho <= 0:
            print("O tamanho deve ser maior que zero e finito.")
            continue
        return tamanho


def ler_dados_upload():
    formato = ler_opcao(
        f"Tipos aceitos: {', '.join(FORMATOS_PERMITIDOS)}\nTipo de arquivo:\n",
        FORMATOS_PERMITIDOS,
        "Tipo inválido! Use um da lista.",
    )
    tamanho = ler_tamanho()
    status = "enviado" if tamanho <= LIMITE_MB else "falhou"
    return {"formato": formato, "tamanho_mb": tamanho, "status": status}


def cadastrar_musica(musicas, proximo_id):
    print("----- NOVO UPLOAD -----")
    musica = {
        "id": proximo_id,
        "genero": ler_genero(),
        "artista": ler_texto("Artista:\n", "O nome do artista não pode ficar vazio."),
        "titulo": ler_texto("Nome da música:\n", "O nome da música não pode ficar vazio."),
        "duracao_seg": ler_duracao(),
        **ler_data(),
        **ler_hora(),
        "autores": ler_nomes("autor/a"),
        "produtores": ler_nomes("produtor/a"),
        **ler_dados_upload(),
        "nome_arquivo": ler_texto(
            "Digite o nome do arquivo (ex: musica.mp3):\n",
            "O nome do arquivo não pode ficar vazio.",
        ),
    }

    salvar_catalogo([*musicas, musica], proximo_id + 1)
    musicas.append(musica)
    print("Upload registrado! ID da música:", proximo_id)
    if musica["status"] == "enviado":
        print("Status: ENVIADO com sucesso.")
    else:
        print(f"Status: FALHOU (arquivo acima do limite de {LIMITE_MB} MB).")
    return proximo_id + 1


def listar_musicas(musicas):
    if not musicas:
        print("Nenhuma música cadastrada.")
        return

    print("===== LISTA DE MÚSICAS =====")
    for posicao, musica in enumerate(musicas):
        minutos, segundos = divmod(musica["duracao_seg"], 60)
        print(
            f"{posicao} | ID: {musica['id']} | {musica['titulo']} | "
            f"Artista: {musica['artista']} | Gênero: {musica['genero']} | "
            f"Duração: {minutos}:{segundos:02d} | Status: {musica['status']}"
        )
    print(f"Total: {len(musicas)} música(s).")


def buscar_posicao(musicas, pergunta):
    id_busca = ler_inteiro(pergunta, "ID inválido! Digite apenas números.")
    if id_busca is None:
        return None
    for posicao, musica in enumerate(musicas):
        if musica["id"] == id_busca:
            return posicao
    print(f"Nenhuma música com ID {id_busca}.")
    return None


def buscar_musicas(musicas):
    if not musicas:
        print("Nenhuma música cadastrada.")
        return

    print(
        "---- BUSCA ----\n"
        "1 - Buscar por ID\n"
        "2 - Buscar por artista\n"
        "3 - Buscar por nome\n"
        "4 - Buscar por gênero\n"
        "5 - Busca combinada (gênero e duração mínima)"
    )
    tipo = input("Escolha o tipo de busca:\n").strip()

    if tipo == "1":
        posicao = buscar_posicao(musicas, "Digite o ID:\n")
        if posicao is not None:
            musica = musicas[posicao]
            print(f"Encontrada na posição {posicao}:")
            print(f"{musica['titulo']} - {musica['artista']} - {musica['status']}")
        return

    if tipo == "5":
        genero = input("Digite o gênero:\n").strip().casefold()
        duracao = ler_inteiro("Duração mínima em segundos:\n", "Digite apenas números.")
        if duracao is None:
            return
        resultados = [
            musica for musica in musicas
            if musica["genero"].casefold() == genero and musica["duracao_seg"] >= duracao
        ]
        if not resultados:
            print("Nenhuma música combina com os 2 critérios.")
        for musica in resultados:
            print(f"{musica['titulo']} - {musica['duracao_seg']} segundos")
        return

    campos = {
        "2": ("artista", "Digite parte do artista:\n"),
        "3": ("titulo", "Digite parte do nome:\n"),
        "4": ("genero", "Digite o gênero:\n"),
    }
    if tipo not in campos:
        print("Tipo de busca inválido.")
        return

    campo, pergunta = campos[tipo]
    termo = input(pergunta).strip().casefold()
    resultados = [musica for musica in musicas if termo in musica[campo].casefold()]
    if not resultados:
        print(f"Nenhum resultado para '{termo}'.")
        return

    print(f"{len(resultados)} resultado(s):")
    for musica in resultados:
        print(f"ID: {musica['id']} | {musica['titulo']} | {musica['artista']} | {musica['genero']}")


def exibir_detalhes(musica):
    print(
        "Música encontrada:\n"
        f"Gênero: {musica['genero']} | Artista: {musica['artista']} | "
        f"Nome: {musica['titulo']} | Duração: {musica['duracao_seg']} segundos\n"
        f"Data: {musica['dia']:02d}/{musica['mes']:02d}/{musica['ano']} | "
        f"Hora: {musica['hora']:02d}:{musica['minuto']:02d}\n"
        f"Autores: {', '.join(musica['autores'])} | "
        f"Produtores: {', '.join(musica['produtores'])}\n"
        f"Tipo/Tamanho: {musica['formato']} - {musica['tamanho_mb']} MB | "
        f"Arquivo: {musica['nome_arquivo']} | Status: {musica['status']}"
    )


def atualizar_musica(musicas, proximo_id):
    if not musicas:
        print("Nenhuma música cadastrada.")
        return

    posicao = buscar_posicao(musicas, "Digite o ID da música que deseja atualizar:\n")
    if posicao is None:
        return

    musica = musicas[posicao].copy()
    exibir_detalhes(musica)
    print(
        "1 - Gênero\n"
        "2 - Artista\n"
        "3 - Nome da música\n"
        "4 - Duração\n"
        "5 - Data de lançamento\n"
        "6 - Hora de lançamento\n"
        "7 - Autores\n"
        "8 - Produtores\n"
        "9 - Tipo e tamanho do arquivo\n"
        "10 - Nome do arquivo"
    )
    campo = input("Qual campo deseja alterar? (0 para cancelar):\n").strip()

    if campo == "0":
        print("Atualização cancelada.")
        return
    elif campo == "1":
        musica["genero"] = ler_genero()
    elif campo == "2":
        musica["artista"] = ler_texto("Novo artista:\n", "O artista não pode ficar vazio.")
    elif campo == "3":
        musica["titulo"] = ler_texto("Novo nome da música:\n", "O nome não pode ficar vazio.")
    elif campo == "4":
        musica["duracao_seg"] = ler_duracao()
    elif campo == "5":
        musica.update(ler_data())
    elif campo == "6":
        musica.update(ler_hora())
    elif campo == "7":
        musica["autores"] = ler_nomes("autor/a")
    elif campo == "8":
        musica["produtores"] = ler_nomes("produtor/a")
    elif campo == "9":
        musica.update(ler_dados_upload())
    elif campo == "10":
        musica["nome_arquivo"] = ler_texto(
            "Novo nome do arquivo:\n", "O nome do arquivo não pode ficar vazio."
        )
    else:
        print("Campo inválido. Nada foi alterado.")
        return

    atualizadas = musicas.copy()
    atualizadas[posicao] = musica
    salvar_catalogo(atualizadas, proximo_id)
    musicas[posicao] = musica
    print("Música atualizada com sucesso!")


def excluir_musica(musicas, proximo_id):
    if not musicas:
        print("Nenhuma música cadastrada.")
        return

    posicao = buscar_posicao(musicas, "Digite o ID da música que deseja excluir:\n")
    if posicao is None:
        return

    musica = musicas[posicao]
    print(f"Você está prestes a excluir: {musica['titulo']} - {musica['artista']}")
    confirmacao = ler_opcao(
        "Confirma a exclusão? (s/n):\n", ("s", "n"), "Responda apenas 's' ou 'n'."
    )
    if confirmacao == "n":
        print("Exclusão cancelada.")
        return

    restantes = musicas.copy()
    restantes.pop(posicao)
    salvar_catalogo(restantes, proximo_id)
    musicas.pop(posicao)
    print("Música excluída com sucesso.")


def gerar_relatorio(musicas):
    if not musicas:
        print("Nenhuma música cadastrada.")
        return

    print(
        "======= RELATÓRIOS ========\n"
        "1 - Resumo geral\n"
        "2 - Música mais longa e mais curta\n"
        "3 - Quantidade por gênero\n"
        "4 - Enviadas e falhas"
    )
    tipo = input("Escolha:\n").strip()
    total = len(musicas)

    if tipo == "1":
        soma_duracao = sum(musica["duracao_seg"] for musica in musicas)
        soma_mb = sum(musica["tamanho_mb"] for musica in musicas)
        print(f"Total de músicas: {total}")
        print(f"Duração somada: {soma_duracao} segundos")
        print(f"Média de duração: {soma_duracao / total:g} segundos")
        print(f"Espaço somado: {soma_mb:g} MB")
        print(f"Média de espaço: {soma_mb / total:g} MB por música")
    elif tipo == "2":
        mais_longa = max(musicas, key=lambda musica: musica["duracao_seg"])
        mais_curta = min(musicas, key=lambda musica: musica["duracao_seg"])
        print(f"Mais longa: {mais_longa['titulo']} - {mais_longa['duracao_seg']} segundos")
        print(f"Mais curta: {mais_curta['titulo']} - {mais_curta['duracao_seg']} segundos")
    elif tipo == "3":
        quantidades = Counter(musica["genero"] for musica in musicas)
        for genero in GENEROS_VALIDOS:
            print(f"{genero}: {quantidades[genero]} música(s)")
    elif tipo == "4":
        quantidades = Counter(musica["status"] for musica in musicas)
        print(f"Enviadas: {quantidades['enviado']}")
        print(f"Falhas: {quantidades['falhou']}")
        print(f"Percentual de sucesso: {quantidades['enviado'] / total:.2%}")
    else:
        print("Tipo de relatório inválido.")


if __name__ == "__main__":
    raise SystemExit(main())
