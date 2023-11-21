
lado = input("Digite o lado de um quadrado: ")

try:

    area = pow(float(lado), 2)
    dobro = pow(float(area), 2)
    print("\nÁrea do quadrado "+str(area))
    print("\nDobro dessa área "+str(dobro))

except:
    print("\nErro!,Apenas entradas numericas são validas")
