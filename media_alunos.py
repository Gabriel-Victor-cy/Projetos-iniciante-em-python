import math
contador = 0
lista=[]
bimestre=0
try:
    for contador in range(1, 5):
        bimestre += float(input("Digite a nota do "+str(contador)+"º bimestre: "))

    lista.append(bimestre)

    media=sum(lista)/contador
    print(media)

except:
    print("Erro!, apenas entradas numericas são aceitas")


