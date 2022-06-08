hora = float(input("Quantas horas foram trabalhadas: "))
valor = float(input("Quanto você ganha por hora: "))

salario = hora*valor

print(f'Seu sálario bruto esse mês será de {salario:.2f}')

salarioir = 0.11 * salario 
salarioin = 0.08 * salario
salariosi = 0.05 * salario
salarioli = salario - (salarioir + salarioin +salariosi)

print ("IMPOSTO DE RENDA R$",salarioir)
print ("IMPOSTO INSS R$",salarioin)
print ("SALARIO SINDICATO R$", salariosi)
print("Seu salario liquido sera de ", salarioli)