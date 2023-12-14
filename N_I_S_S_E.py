nome = str(input("Digite seu nome: "))
idade = int(input("Digite sua idade: "))
salario = float(input("Digite seu salario: "))
sexo = [str(input("Digite F para feminino ou M para masculino: "))]
estado_civil = [str(input("Digite seu estado civil S , C , V , D: "))]

#lista = [nome, idade, salario, sexo, estado_civil]

# print(lista)

if len(nome) > 3:
    print(nome)

else:
    print("Seu nome contem menos de 3 caracteres")

if idade <= 150:
    print(idade)
else:
    print("Idade maior que 150")

if salario > 0:
    print(salario)
else:
    print("Salario menor que 0")


if sexo == ['F'] or sexo == ['M']:
    print(str(sexo))

else:
    print("Sexo invalido")

if estado_civil==['S'] or estado_civil==['C'] or estado_civil==['V'] or estado_civil==['D']:

    print(str(estado_civil))

else:
    print("Estado civil invalido")
