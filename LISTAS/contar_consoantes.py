caract = []

vogais= ['a', 'e', 'i','o','u']
contvogal=0

for x in range(10):
    entrada = input("digite a letra ")
    caract.append(entrada)
    if entrada in vogais:
        contvogal+=1
print ("Consoantes: ",(len(caract))-contvogal)