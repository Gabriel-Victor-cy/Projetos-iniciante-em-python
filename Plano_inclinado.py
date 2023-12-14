import math

angulo = float(input("Digite o angulo do plano inclinado: "))
massa = float(input("Digite a massa do bloco: "))


def som_x():
    f_x = round((massa*10) * math.sin(math.radians(angulo)), 2)
    print("O valor da componente horizontal é: " + str(f_x)+" N")


def som_y():
    n = round((massa*10) * math.cos(math.radians(angulo)), 2)
    print("O valor da normal é: " + str(n)+" N")


def atrito():
    f_x = round((massa*10) * math.sin(math.radians(angulo)), 2)

    n = round((massa*10) * math.cos(math.radians(angulo)), 2)

    u = round((f_x/n), 2)
    print("O coeficiente de atrito é: " + str(u))

    fat = round((u*n), 2)
    print("A força de atrito é: " + str(fat))


som_x()
som_y()
atrito()
