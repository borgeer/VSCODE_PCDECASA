from random import randint


def sortear_dado():
    return randint(1, 6)


for i in range(1, 7):
    if i % 2 == 1:
        continue    #nao valida numeros impar 

    if sortear_dado() == 1:
        print("Acertou", i)
        break  #quando acha o que precisa para
else:
    print("Nao acertou o numero ")
