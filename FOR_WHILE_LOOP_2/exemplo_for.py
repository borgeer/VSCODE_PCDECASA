
#Range(valor_inicial , valor_final) pode se usar só Range(valor_final)
#OBS: Nao inclui o ultimo numero ---- range(1,5) == 1234
#OBS: range(valor_inicial, valor_final, qtd_passo) se for range(0,50,5) ira passar 0,5,10,15....
#OBS: range(valor_inicial, valor_final, passo) se for range(10,0,-1) ira ser contagem decrescente 

#for 'variavel que recebe interaçao' in 'variavel iterada' 

nome = 'Geek University'
lista = [1,3,5,7,9]
numeros = range(1, 10) #tem que transformar em lista 

#Ex.: 1
for letra in nome:
    print (letra)


#Ex.: 2

for numero in  lista:
    print (numero)


#EX.:
qtd= int(input("Quantas vezes deve rodar --- "))
soma = 0
for n in range(1,qtd+1):        #pra informar correto por range(1,qtd+1)
    num = int(input(f'Informe o valor de {n}/{qtd}: '))
    soma=soma+num
print(" A soma é ",soma)


#EX.:
nome='Ariel'
for letra in nome:
    print (letra, end='') #imprimir sem quebrar linha 


#IMPRIMIR EMOJIS 
#U+1F602  ====unicode
#U0001F602 === troca "+" por 3 "000"

for _ in range(3):   #executa o for 3x 
    for num in range(1,5):
        print ('\U0001F602' * num)

