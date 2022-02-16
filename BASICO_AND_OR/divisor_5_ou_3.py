n1 =  int(input("Digite numero --- "))

if n1%3==0:
    print ("Numero divisor de 3 ")
if n1%5==0:
    print ("Numero divisor de 5 \n")
elif n1%3==0 and n1%5==0:
    print ("Esse numero é divisor de 5 e 3")
if n1%3>=1 and n1%5>=1:
    print ("Não é divisor de nenhum ")