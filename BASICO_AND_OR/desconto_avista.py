valor = float(input("Qual valor da compra: "))

op = int(input("Se for a vista, op = 1 se não op = 2 "))

if op ==1:
    valorf= valor - 12.0
    print(f'O valor a vista ficou R${valorf:.2f}')
if op>1:
    print ("Produto não sofre alteração de valor R$", valor)