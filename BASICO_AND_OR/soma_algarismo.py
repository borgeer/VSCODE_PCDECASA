n1= int(input("Digite um numero maior que 0 --- "))
soma=0 


if n1<0:
    print ("Numero invalido")
else:
    while (n1>0):
        soma += n1%10
        n1 = int (n1/10)
print (soma)
