arquivo = open('PYTHON\MANIPULDANDO DADOS\pessoas.csv')

dados = arquivo.read()

arquivo.close()

for registro in dados.splitlines():
    print('Nome: {}, Idade: {}'.format(*registro.split(',')))
