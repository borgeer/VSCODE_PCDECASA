"""
Listas iguais vetores e recebe qualquer tipo de variavel 
"""

lista = [1, 2, 9, 4, 5, 8, 7,3,6]
lista2 = ['a', 'r', 'i', 'e', 'l']
lista3 = []
lista4 = list(range(11))
lista5 = list('ariel')

#Pode ser checado algum valor na lista 
num = 5
if num in lista4:
    print (f'Encontrei o numero {num}')
else:
    print (f'Nao encontrei {num}')

if 'e' in lista5:
    print ("Encontrei letra")
else:
    print("Nao encontrei")



#Ordenar uma lista 
lista.sort()
print(lista)

lista2.sort()
print(lista2)


#Contar de ocorrencia de um valor em uma lista 
print(lista.count(1))  #count(string, int que quer contar)

#adicionar elementos em listas 
"""
Para adicionar valores em lista, utilizamos a funcao apppend
OBS: com append só consegue adicionar um valor por vez
"""
lista.append(23)
print(lista)
#Para passar mais valoress 
lista.append([1,2,3,4])
print(lista)
#Adicionar indivudal os valores mas nao aceita valor unico 
lista.extend([1,2,3,555])
print(lista)