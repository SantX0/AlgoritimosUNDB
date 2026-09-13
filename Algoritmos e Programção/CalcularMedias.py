print(" -----Calculadoura de Medias------ ")
print(" Digite os valores de cada semestre: ")

periodo1 = float(input("Digite a nota do Periodo 1: "))
peso1 = float (input ("Digite o peso : "))

periodo2 = float(input("Digite a nota do Periodo 2: "))
peso2 = float (input ("Digite o peso : "))

periodo3 = float(input("Digite a nota do Periodo 3: "))
peso3 = float (input ("Digite o peso : "))

periodo4 = float(input("Digite a nota do Periodo 4: "))
peso4 = float (input ("Digite o peso : "))

maiornota = periodo1
if periodo2 > maiornota:
    maiornota = periodo2
if periodo3 > maiornota:
    maiornota = periodo3
if periodo4 > maiornota:
    maiornota = periodo4

notasComPesos = (periodo1 * peso1) + (periodo2 * peso2) + (periodo3 * peso3) + (periodo4 * peso4)
somapesos = peso1 + peso2 + peso3 + peso4
mediaGeral = notasComPesos / somapesos
print(" ------ Resultados ----- ")
print(" Soma das notas com pesos:", notasComPesos)
print(" Soma dos pesos:", somapesos)
print(" Maior nota: ", maiornota)
print(" Media Geral: ", mediaGeral)

if mediaGeral > 7:
    print(" Aprovado ")
elif mediaGeral < 5:
    print(" Reprovado ")
else:
    print(" Prova Final ")