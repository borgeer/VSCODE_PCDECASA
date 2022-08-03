#EXEMPLOS DA AULA DE FUNÇAO

#comentado pois gera diversoso erros por estar somente como exemplo 


#Funçoes com retorno 

"""
return que faz o retorno do resultado
return finaliza a funçao 
pode ter mais de um return em def 
nao executa nada apos o retorno 


#Exemplo funçao 

def quadrado_de_sete():
    return (7*7)

#nao precisa disso, pode retornar direto print(quadrado_de_sete)
ret = quadrado_de_sete()


print(ret)
#nao retorna nada, somente printa --- print (f'retorno de {ret}')

def diz_oi():
    return 'oi'

print(diz_oi())


#funçao para cara ou coroa 
#random print entre 0 e 1 

from random import random

def cara_coroa():
    valor=random()
    print (valor)
    if valor >0.5:
        return 'cara'
    return 'coroa'
print (cara_coroa())

"""