"""
1 - TUPLAS SÃO REPRESENTADAS POR ()         LISTA REPRESENTA []
(1,2,3,4,6) pode ser também somente 1,2,3,4,6
OBS.: Tupla não pode ser adicionada nem tirada nada
OBS.: Se for somente (3) é considerado int tem que por (3,) pra ser tupla
OBS.: É possivel fazer a junçao de tupla com "tupla=tupla1+tupla2" ou print(tupla+tupla2)
print (tupla1)

tupla2 = ('Ariel', 'borger',)  #separando o conteudo da tupla por variavel 
nome, sobrenome = tupla2
print(nome)  
print(sobrenome)

tupla2 = (1,1.,5,5,8,)   #somente inteiros e float 
print (sum(tupla2))
print (max(tupla2))
print (min(tupla2))
print (len(tupla2))


tupla2 = (1,1.,5,5,8,)
print(1 in tupla2)   #verificar se numero esta na tupla


tupla2 = (1,1,5,5,8,)
for n in tupla2:
    print (n)

tupla2 = (1,1,5,5,8,)
print (tupla2.count(1))      #Contar elementos da tupla  para letras 'a' 


"""



tupla = tuple()

print(type(tupla))



tupla2 = (1,1,5,5,8,)

