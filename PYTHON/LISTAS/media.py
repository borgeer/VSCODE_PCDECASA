n1 = float(input("Nota 1 "))
n2 = float(input("Nota 2 "))
n3 = float(input("nota 3 "))

lista = [n1,n2,n3]

soma = sum(lista)

media = soma/3

print (f'A média das 3 notas {n1}, {n2}, {n3} é {media:.2f} ')
