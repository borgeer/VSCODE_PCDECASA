"""
lista1 = list(range(11))
print (lista1)

---------------------------------------------------------

lista2 =list(range(5))
num= 8                  #colocado em varialvel se nao somente colocar o que quer, como numero ou letra 
if num  in lista2:
    print ("Foi encontrado o numero 8 ")
else:
    print ("Nao está na lista numero 8 ")

-------------------------------------------------

lista3 = ["Ariel Borger"]

letra= 'z'

if letra in lista3:
    print ("Encontrei a letra I ")
else:
    print ("Nao encontrei ")


#ordenar String e Numeros 
lista5 = ['A','r','i','e','l',' ','B','o','r','g','e', 'r']
lista5.sort()
print (lista5)

lista4 = [4,8,10,6,85,784,258,45]
lista4.sort()
print (lista4)

#Ordenar de trás pra frente
lista4 = [4,8,10,6,85,784,258,45]
lista4.reverse()
print(lista4)

----------------------------------------------------------------------------------

#contar letras e numeros dentro da lista, tem que ser escrito no print
lista6 = [4,8,10,6,85,784,8,9,0,8,258,45]
print (lista6.count(8))

-------------------------------------------------------------------------------------

#append adiciona somente 1 elemento por vez mas podendo adicionar uma lista dentro da outra
lista8 = [12,12,12]
lista7 = [1,2,3,4,5]
lista7.append(23)
print (lista7)
lista7.append(lista8)
print(lista7)
#Encontra somente uma lista dentro da outra
if [12,12,12] in lista7:
    print ("Encoontrei a lista8 ")
else:
    print ("Nao encontrei lista8 ")

--------------------------------------------------------------

#adiciona um a um e aceita mais numeros, nao aceita valor unico lista9.extend(45)
lista9= [10,14,4,4,14]
lista9.extend([12,21,67,8,75])
print (lista9)

--------------------------------------------------------------------------

#adicionar algo na posiçao que querer somente 1 elemente por vez
lista10 = list(range(8))
lista10.insert(1, 12)  #lista10.insert(1, 'ariel borger')
print (lista10)


#adiciona  uma lista na outra! 
lista11= [12,12,14]
lista12 = [45,76,45]
lista13= lista11 + lista12
print (lista13)


#copiar listas
lista=lista2.copy()
ptint (lista)

#vefiricar tamanho 
print(len(lista))

"""

 













