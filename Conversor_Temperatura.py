import math

escolha = input("Digite 1 para converter Fahrenheit ou 2 para Celsius: ")
resultado = float(escolha)


def farenheit(graus):
    try:
        # F_temp=input("Digite a temperatura em graus Fahrenheit: ")
        Celsius = (5 * (float(graus) - 32) / 9)

        print("\nTemperatura em graus Celsius: " + str(Celsius) + "°")
    except:
        print("\nErro!,apenas entradas numericas são admitidas")


def Celsius(graus):
    try:
        # F_temp=input("Digite a temperatura em graus Celsius: ")
        Celsius = ((float(graus) * 9 / 5) + 32)

        print("\nTemperatura em graus Farenheit: " + str(Celsius) + "°")
    except:
        print("\nErro!,apenas entradas numericas são admitidas")


if resultado == 1:
    graus = input("digite a temperatura em Farenheit: ")
    farenheit(graus)

if resultado == 2:
    graus = input("digite a temperatura em Celsius: ")
    Celsius(graus)

elif resultado != 1 and resultado != 2:
    print("\nErro! digite valores entre 1 e 2")
