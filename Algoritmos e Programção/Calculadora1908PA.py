print ("Escolha uma opção: ")
print ("1 - Calculadoura Básica")
print ("2 - Calculadoura de Bhaskara")
opcao = input ("Digite a opção que deseja: ")
if opcao == "1":
    num1 = float(input("Digite o primeiro numero : "))
    num2 = float(input("Digite o segundo numero: "))
    adicao = num1 + num2
    multi = num1 * num2
    subtracao = num1 - num2
    if num2 != 0:
        divisao = num1 / num2
    else:
        divisao = "Não é possível dividir por zero"
    print("Resultado das operações:")
    print("Soma", adicao)
    print("Multiplicação", multi)
    print("Subtração", subtracao)
    print("Divisão", divisao)
     #finalizei a calculadora básica e realizei ajuste na parte da divisão para não dar erro caso o usuário digite 0.
elif opcao == "2":
    valordeA = float(input("Digite o valor de a: "))
    valordeB = float(input("Digite o valor de b: "))
    valordeC = float(input("Digite o valor de c: "))
    delta = valordeB**2 - 4 * valordeA * valordeC
    if delta < 0:
        print("Não existem raizes reais")
    elif delta == 0:
        raiz = -valordeB / (2*valordeA)
        print ("Existe uma raiz real: ", raiz)
    else:
        raiz1 = (-valordeB + delta**0.5) / (2*valordeA)
        raiz2 = (-valordeB -delta**0.5) / (2*valordeA)
        print("Extistem duas raizes reais : ", raiz1, "e", raiz2)
else:
    print("Opção inválida, digite 1 ou 2")
     #incluindo a calculadoura de bhaskara. 0