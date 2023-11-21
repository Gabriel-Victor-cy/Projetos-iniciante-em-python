import math

raio = input("Informe o raio de um circulo: ")
try:
    area = math.pi * (pow(float(raio), 2))

    print("A area do circulo é " + str(area))

except:
    print("\nApenas valores numericos são admitidos ")
