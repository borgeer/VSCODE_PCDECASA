notas=[]
p=[]
p=0
r=0
n=7.0

for x in range (0,4):
    notas.append(float(input("Digite a media dis alunos ")))

if n in notas:
    p.append(notas[n])
    print ("aluno passou acima da media ")

else:
    r+=1
    print("aluno reprovou ")
    print (r)

print(p)
print (r)
