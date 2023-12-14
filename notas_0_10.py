def loop(nota):
    while nota > 10 or nota < 0:
        print("Valor invalido")
        nota = int(input("Digite uma nota entre 0 e 10: "))
    print(str(nota))


try:
    nota = int(input("Digite uma nota entre 0 e 10: "))

    if nota <= 10 and nota >= 0:
        print(str(nota))

    elif nota < 10 and nota < 0:
        loop(nota)
    else:
        loop(nota)


except:
    print("\nErro!,Apenas entrada inteiras são validas")
