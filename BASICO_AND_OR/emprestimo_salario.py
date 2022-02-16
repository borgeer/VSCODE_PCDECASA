sal = float(input("Digite o salario --- "))
pres = float(input("Digite o valor da prestaçao --- "))

cal = sal * 0.20

if pres >cal:
    print ("Emprestimo nao autorizado")
else: 
    print ("Autorizado")