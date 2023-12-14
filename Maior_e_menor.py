num1 = input("Digite o 1: ")
num2 = input("Digite o 2: ")
num3 = input("Digite o 3: ")
lista = [num1, num2, num3]
maior=[]
menor=[]

try:
    for item in lista:
        maior = max(lista, key=float)
        menor = min(lista, key=float)

    print("\no maior valor é " + str(maior))
    print("\no menor valor é " + str(menor))

except:
    print("\nErro!,apenas entradas numericas são admitidas")
