valor = int(input("Digite um valor: "))
divisor = 1
lista = []
loop = True


def num_primos(valor):
    for contador in range(1, valor + 1):
        if valor % contador == 0:
            lista.append(valor)
        if len(lista) > 2:
            print("\nvalor " + str(valor) + " não é primo")
            break

    if len(lista) == 2:
        print("\nvalor " + str(valor) + " é primo")
    if valor == 1:
        print("\nvalor " + str(valor) + " não é primo")


num_primos(valor)
