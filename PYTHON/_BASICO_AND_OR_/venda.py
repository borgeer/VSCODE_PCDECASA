venda=float(input("Qual valor da venda: "))

print(f'Caso a venda for a vista o valor fica {venda-10.0}')
print (f'Caso a venda for parcelado em 3x o valor fica {venda/3:.2f}')

valord = venda-10.0

print(f'A comissão do vendedor é {valord/5.0:.2f}')