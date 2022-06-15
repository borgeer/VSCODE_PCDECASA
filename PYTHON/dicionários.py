"""
DICIONARIOS: obs: em alguma linguagens é conhecido como mapa 
dicionário é representado por {}  -  print(type({}))

OBS.:
    -Chave e valor sao separados por dois pnto 'chave:valor'
    -Tanto chave quanto valor podem ser de qualque tipo de dado
    -Podemos misturar tipos de dados 

#CRIAÇAO DOS DISCIONARIOS 
#Forma 1 (mais comum)

paises = {'br':'brasil', 'eua':'Estados Unidos', 'py':'Paraguai' }
print (paises)


#Forma 2 (menos comum)

paises1 = dict(br='Brasil', eua='Estados Unidos', py='Paraguai')
print (paises1)
--------------------------------------------------------------------
#Acessando elemnetos 
#Forma 1 - Acessando via chave, da mesma forma que lista/tupla

print(paises['br'])
print(paises['py'])

#Forma 2 - Acessando via get - RECOMENDADO

print(paises.get('br'))                - se o get nao achar vai resultar como None

----------------------------------------------- 

pais = paises.get('ru')
#se colocar == pais = paises.get('ru') - dá como pais nao encontrado

if pais:
    print (f'Encontrei o pais {pais}')
else:
    print("Nao encontrei")


--------------------------------
#Podemos definir um valor padrao para caso nao encontremos o objeito na cheve encontrada
pais = paises.get('py', 'nao encontrado')
print (f'Encontrei o pais {pais}')

------------------------------------------------------
#verificar se determinada chave se encontra em um dicionario 
print('br' in paises)
print ('ru' in paises)
print ('Estadus unidos' in paises)  #encontra somente CHAVE e nao busca VALOR 

if 'ru' in paises:
    russia = paises['ru']


-------------------------------------------------------------

#Podemos utilizar qualquer tipo de dado (int, float, string, boolean), inclusice lsita, tuplas, dicionarios
#como chave
#USANDO TULAS NAS CHAVES 
localidades={
    (35.678, 39.454545): 'Escritorio em Toquio',
    (88.698, 14.123545): 'Escritorio em Nova York',
    (12.895, 56.887545): 'Escritorio em toquio' ,
}

print(localidades)

--------------------------------------
#adicionar elementos em um dicionario ou atualiar dados. EM dicionario nao pode ter chaves repetidas
receita = {'Jan':100, 'fev':120, 'mar':300}

#forma 1 -- Mais comum
receita['abr']=350

#forma 2 
novo_dado= {'mai':500}    
receita.update(novo_dado)   # mesma coisa que -- reiceita.update({'mai':500})

print(receita)

#Atualizar dados em um dicionario 

#forma 1
receita ['mai'] = 500
print (receita)

#Forma 2
receita.update({'mai':600})
print(receita)
------------------------------------------------------
#remover dados de um dicionario 

#forma 1
ret =receita.pop('mar')      #informar a chave caso noa encontrar irá dar KeyError
print (ret)   #a chave é removida e é retornado o valor  
print (receita)

#fomar 2
del receita['fev']
print(receita)





"""

carinho =[]

produto1= {'nome': 'PlayStation', 'quantidade':1, 'preço':2300.00}
produto2= {'nome':'God of War', 'quantidade':1, 'preço':150.00}

carinho.append(produto1)
carinho.append(produto2)

print (carinho)










