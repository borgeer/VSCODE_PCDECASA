"""
Sair de loop de maneira forçada/projetada

"""

#Exemplo 

for numero in range(1,11):
    if numero ==6:
        break
    else:
        print(numero)
print ("Sai do loop")


#Exemplo 

while True:
    comando= input("Digite 'sair' para sair: ")
    if comando=='sair':
        break
    