n1 = int(input("Digite o primeiro numero --- "))
n2 = int(input("Digite o segundo numero --- "))

if n1>n2:
    print("Numero maior é --- ",n1)
else:
    print ("Numero maior é --- ",n2)

if n1>n2:
    n1 = n1-n2 
    print("A diferenca entre eles é --- ",n1)
else:
    n2= n2-n1
    print("A diferenca entre eles é --- ",n2)