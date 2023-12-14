num1 = input("Digite o 1: ")
num2 = input("Digite o 2: ")
num3 = input("Digite o 3: ")
lista = [num1, num2, num3]

try:
    for item in lista:
        resultado = max(lista, key=float)

    print("o maior valor é " + str(resultado))

except:
    print("\nErro!,apenas entradas numericas são admitidas")
