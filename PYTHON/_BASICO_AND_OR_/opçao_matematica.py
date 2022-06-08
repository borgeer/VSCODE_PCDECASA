print ("1 = Soma \n")
print ("2 = Divisão \n")
print ("3 = Multiplicacao \n")
print ("4 = Potencia \n")

op = int(input("Digite a opcao --- "))

if op == 1:
    n1 = int(input("Digite numero 1 --- "))
    n2 = int(input("Digite numero 2 --- "))
    soma = n1+n2
    print ("A soma é ", soma)
elif op ==2:
    n1 = int(input("Digite numero 1 --- "))
    n2 = int(input("Digite numero 2 --- "))
    soma = n1/n2
    print ("A divisao é ", soma)
elif op == 3:
    n1 = int(input("Digite numero 1 --- "))
    n2 = int(input("Digite numero 2 --- "))
    soma = n1*n2
    print ("A multiplicação é ", soma)
elif op == 4:
    n1 = int(input("Digite numero 1 --- "))
    n2 = int(input("Digite a potencia --- "))
    soma = pow(n1,n2)
    print ("A potencia é ", soma)
elif op <=0 or op >4:
    print ("Digite uma opçao valida")