#Faça um Programa que leia dois vetores com 10 elementos cada. 
#Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores. 

list1=[]
list2=[]
list3=[] 
i=5

for n in range(i):
    list1.append(input("Digite os 5 numeros da 1º lista "))


for n in range(i):
    list2.append(input("Digite os numeros 5 da 2º lsita "))


for n in range(i):
    list3.append(list1[n])
    list3.append(list2[n])

print ("A primeira lista é ", list1)
print ("A segunda lista é ", list2)
print ("A terceira lista mesclada é ", list3)