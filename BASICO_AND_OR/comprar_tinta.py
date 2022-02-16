area = float(input("Qual tamanhoa da area que vai ser pintada: "))
litro = area/3

preçol=80.0
capa=18

tinta = litro/capa

total = tinta*preçol

print (f'Você usar {tinta:.2f} latas de tinta e pagara R${total:.2f}')