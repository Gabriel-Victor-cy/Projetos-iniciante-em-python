
operador=input("Digite um valor: ")
valor = int(operador)


def fatorial(valor):
    if valor<=1:
        return 1
    else:
        return valor*fatorial(valor-1)

print(fatorial(valor))
