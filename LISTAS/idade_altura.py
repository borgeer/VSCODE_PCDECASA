# Faça um Programa que peça a idade e a altura de 5 pessoas, 
# armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida
id=[]
alt=[]



for n in range(1,5):
    id.append(int(input(f'Digite a idade da {n}º pessoa ')))

for n in range(1,5):
    alt.append(float(input(f'Digite a altura da {n}º pessoa ')))

alt.reverse()
id.reverse()

print (f'A idade de forma reversa é {id}')
print (f'A altura de forma reversa é {alt}')