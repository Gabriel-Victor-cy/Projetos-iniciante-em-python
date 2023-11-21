meuVetor = []

n_digitos = int(input("Digite a quantidade de caracteres: "))

while n_digitos != 0:
    digitos = int(input("Digite o caractere: "))

    conversor = digitos*pow(2, n_digitos-1)
    meuVetor.append(conversor)
    n_digitos = n_digitos - 1

print(sum(meuVetor))
