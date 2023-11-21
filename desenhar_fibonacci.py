import turtle
#import math

# distancia = input("digite o comprimento de cada lado: ")

laco = True



# valor=input("Digite o valor inicial da sequencia: ")
# n_termos=int(valor)

# n_termos = int(input("Digite o valor da sequencia: "))


def fibonacci(n_termos):
    if n_termos <= 1:
        return n_termos

    else:
        return fibonacci(n_termos - 1) + fibonacci(n_termos - 2)


def quadrado():
    linha_turtle = turtle.Turtle()
    linha_turtle.color("blue")
    linha_turtle.begin_fill()
    linha_turtle.forward(float(fibonacci(n_termos)))
    linha_turtle.right(90)
    linha_turtle.forward(float(fibonacci(n_termos)))
    linha_turtle.right(90)
    linha_turtle.forward(float(fibonacci(n_termos)))
    linha_turtle.right(90)
    linha_turtle.forward(float(fibonacci(n_termos)))
    linha_turtle.end_fill()

while laco:
    n_termos = int(input("Digite o valor da sequencia: "))
    quadrado()
    turtle.done()
