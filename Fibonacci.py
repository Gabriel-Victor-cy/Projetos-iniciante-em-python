import math

# valor=input("Digite o valor inicial da sequencia: ")
# n_termos=int(valor)

n_termos = int(input("Digite o valor da sequencia: "))


def fibonacci(n_termos):
    if n_termos <= 1:
        return n_termos

    else:
        return fibonacci(n_termos - 1) + fibonacci(n_termos - 2)

'''
print(fibonacci(n_termos))
for contador in range(n_termos):
    print(fibonacci(n_termos))
'''