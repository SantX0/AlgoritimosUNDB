def calculadoura_basica():
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
     #finalizei a calculadora básica.
def calcular_bhaskara():
    a = float(input("Digite o valor de a: "))
    b = float(input("Digite o valor de b: "))
    c = float(input("Digite o valor de c: "))
    delta =b**2 - 4*a*c
    if delta < 0:
        print("Não existem raizes reais")
    elif delta == 0:
        raiz = -b / (2*a)
        print ("Existe uma raiz real: ", raiz)
    else:
        raiz1 = (-b + delta**0.5) / (2*a)
        raiz2 = (-b -delta**0.5) / (2*a)
        print("Extistem duas raizes reais : ", raiz1, "e", raiz2)
print("Escolha uma opção:")
print("1 - Calculadoura básica")
print("2 - Calcular Bhaskara")
opcao = input("Digite o numero da opção desejada:")
if opcao == "1":
    calculadoura_basica()
elif opcao == "2":
    calcular_bhaskara()
else:
    print ("Opção invalida. Por favor, escolha 1 ou 2:")
     #incluindo a calculadoura de bhaskara. 