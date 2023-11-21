saida = True
resposta = "S"

while saida:
    metros = input("\nDigite uma distância em metros: ")
    if saida:
        try:
            distancia = float(metros) * 100

            print("\nA distância em centimetros é " + str(distancia) + " cm")
            resposta = str(input("\nDeseja fazer mais alguma conversão ? S/N: "))
            if resposta == str.lower("S") or resposta == str.upper("s"):
                saida = True

            else:
                if resposta == str.lower("N") or resposta == str.upper("n"):
                    saida = False
                else:
                    print("\nErro!, entrada invalida")
                    saida = False
        except:
            print("\nErro!, entrada apenas em valores numericos")


