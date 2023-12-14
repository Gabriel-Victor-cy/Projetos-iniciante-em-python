sexo = input("Digite M para mulher ou H para homem: ")
altura = input("Digite sua altura em metros: ")


def peso_ideal_H(altura):
    Peso_ideal = (float(altura) * 72.7) - 58
    print("Seu peso ideal é: " + str(Peso_ideal))


def peso_ideal_M(altura):
    Peso_ideal = (float(altura) * 62.1) - 44.7
    print("Seu peso ideal é: " + str(Peso_ideal))


if str.upper(sexo) == 'H':
    peso_ideal_H(altura)

if str.upper(sexo) == 'M':
    peso_ideal_M(altura)


