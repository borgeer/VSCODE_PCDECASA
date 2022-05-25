


saltos=[]

nome= str(input("Digite o nome do atleta: "))

if nome != int:
    for n in range(1,5):
        saltos.append(float(input(f'Digite o {n}º salto do atleta: ')))


        saltos1=sum(saltos)/n
    
    print("O resultado final foi ")
    print (f'O atleta {nome}')
    for n in range(len(saltos)):
        print(f'O {n+1}º salto foi {saltos[n]} ')
    print(f'A media foi {saltos1 :.2f} ')
else:
    print("Informe o nome corretamente ")

    print ("Desaja informar o nome corretamente? 1= SIM e 2=NAO ")
    opcao=int(input("Opçao "))
    if opcao==1:
        nome=input("Qual no mdo atleta")
    else:
        print ("Obeigado")
