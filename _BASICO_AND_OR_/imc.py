altura = float(input("Digite a altura --- "))
esc = int(input("Se for homem digite 1, se for muler 2 --- "))

print (esc)

if esc == 1:
    cal = (72.7 * altura) - 58
    print ("Seu peso ideal seria ---",cal)

if esc == 2:
    cal2 = (62.1*altura)-44.7
    print ("Seu peso ideal seria ---",cal2)