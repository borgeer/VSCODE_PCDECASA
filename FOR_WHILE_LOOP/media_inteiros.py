media=0
soma=0
cont=1

while cont<=4:
    num=int(input(f'Dgite o numero {cont}: '))
    if num>=0:
        soma=soma+num
        media=soma/cont
    else:
        print(f'A média até aqui foi calculada mas RECOMECE')
        break

    cont=cont+1
print(f'A média é {media}') 
