vetor = []
par=[]
impar=[] 

for x in range (0, 5):
    vetor.append(int(input("Digite um numero: ")))

for x in range (0,5):
    if vetor[x] %2==0:
        par.append(vetor[x])
    else:
        impar.append(vetor[x])

print ("Os numeros digitados foram ", vetor)
print ("Os numeros pares foram ", par)
print ("Os numeros impares foram ", impar)
