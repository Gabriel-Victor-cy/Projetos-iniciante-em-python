"""Decimal_to_binary by Gabriel Victor && Paulo Ricardo"""

meuVetor = []
meuVetor_2 = []


def conversor(n_decimal):
    if n_decimal == 0:
        meuVetor.append(0)
    while n_decimal >= 1:
        resultado = int(n_decimal / 2)
        meuVetor.append((n_decimal % 2))
        n_decimal = resultado

    meuVetor.reverse()


ponto_decimal = str(input(" O valor possui ponto decimal S/N ? "))


def conversor_ponto_decimal(p_decimal):

    resultado = float(p_decimal) * 2
    for contador in range(w):

        if resultado >= 1:
            resultado = resultado - 1
            resultado = resultado * 2
            meuVetor_2.append(1)

        else:
            meuVetor_2.append(0)
            resultado = resultado*2

    print(meuVetor, ",", meuVetor_2)


if ponto_decimal == "N" or ponto_decimal == "n":
    n_decimal = int(input(" Digite o valor decimal: "))
    conversor(n_decimal)
    print(meuVetor)

if ponto_decimal == "S" or ponto_decimal == "s":
    n_decimal = int(input(" Digite o valor decimal: "))
    p_decimal = str(input(" Digite o ponto decimal: "))
    w = int(input("Digite o numero de casas decimais: "))
    conversor(n_decimal)
    (conversor_ponto_decimal(p_decimal))
