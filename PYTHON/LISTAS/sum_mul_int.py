#Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números. 

from math import prod


num=[]
for n in range (1,5):
    num.append(int(input(f'Digite os numero {n}º ')))

n=sum(num)

n1=prod(num)

print (f'A soma dos 4 numeros é {n}')
print (f'A multiplicaç;ao dos 4 numeros é {n1}')
print (f'Os numeros da lista sao {num}')