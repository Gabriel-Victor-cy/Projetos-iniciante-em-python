try:
    num_1 = int(input("Digite 1: "))
    num_2 = int(input("Digite 2: "))


    def entre_valores(num1, num2):

        if num_2 > num_1:
            for contador in range(num_1 + 1, num_2):
                print(contador)
        if num_1 > num_2:
            for contador in range(num_2 + 1, num_1):
                print(contador)


    entre_valores(num_1, num_2)
except:
    print("Erro! Digite apenas entradas inteiras")
