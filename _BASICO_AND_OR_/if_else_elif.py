idade = int(input("Digite a idade \n"))

if idade >= 18: 
    print("Maior de idade", idade)
else:
    print ("Menor de idade", idade)

#-------------------

idade = int(input("Digite a idade \n"))

if idade > 18: 
    print("Maior de idade", idade)
elif idade == 18:
    print("Tem 18 anos")
else:
    print ("Menor de idade", idade)