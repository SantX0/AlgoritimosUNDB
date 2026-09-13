print(" Identificador ")
print(" Escolha uma das opcoes abaixo: ")
print(" 1 - Teste1 ")
print(" 2 - Teste2")
print(" 3 - Teste3")
entradaA = int
entradaB = int
temp = int
opcao = int
try:
    opcao = int(input("Digite a opcao desejada: "))
except ValueError:
    print("Opcao invalida, digite um numero inteiro.")
    exit()
if opcao == 1:
    try:
        entradaA = int(input("Digite o primeiro numero: "))
        entradaB = int(input("Digite o segundo numero: "))
    except ValueError:
        print("Entrada invalida, digite numeros inteiros.")
        exit()
    if entradaA > entradaB:
        print(" Ele é maior ")
    elif entradaA < entradaB:
        print(" Ele é menor ")
    else:
        print("Os numeros sao iguais")
elif opcao == 2:
    try:
        entradaA = int(input("Digite o primeiro valor: "))
        entradaB = int(input("Digite o segundo valor: "))
    except ValueError:
        print("Entrada invalida, digite numeros inteiros.")
        exit()
    if entradaA > 10 and entradaB <= 4:
        print("Esta correto")
    elif entradaA < 10 and entradaB >= 4:
        print("Esta incorreta")
    else:
        print("Teste 2 nao valido")
elif opcao == 3:
    try:
        temp = int(input("Digite a temperatura: "))
    except ValueError:
        print("Entrada invalida, digite um numero inteiro.")
        exit()
    if temp > 30:
        print("Esta esta calor")
    else:
        print("Esta frio")
else:
    print("Opcao invalida")