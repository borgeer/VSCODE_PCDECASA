"""
VARIAVEIS DO TIPO FLOAT 
"""

#Errado do ponto de vista do Float, mas gera tuplas
valor = 1, 44
print (valor)
print(type(valor))


#Certo do ponto de vista Float
valor = 1.44
print(valor)
print(type(valor))


#Converter um Float para Int 
"""
OBS: Ao converter valores float em int perdemos precisao
"""
res = int(valor)
print(res)
print (type(res))
