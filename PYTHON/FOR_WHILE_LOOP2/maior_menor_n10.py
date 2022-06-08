cont = 0
lista_numeros =[]


while cont != 4: #Para poder pegar 10 numeros
    numero = int(input('Digite um numero: '))
    lista_numeros.append(numero)
    cont = cont + 1

maior=max(lista_numeros) 
print(f'O mair numero é {maior}')
menor=min(lista_numeros)
print (f'O numero menor é {menor}')