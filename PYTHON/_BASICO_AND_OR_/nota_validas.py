nota = float(input("Digite a primeira nota --- "))

if nota >=0 and nota <=10:
    nota2 = float(input("Digite a segunda nota --- "))
    if nota2 >=0 and nota2 <=10:
        media =  (nota + nota2) /2
        print (media)
    else:
        print ("Nota invalida")
else:
    print("nota invalida")
