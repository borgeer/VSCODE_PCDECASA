arquivo = open('PYTHON\MANIPULDANDO DADOS\pessoas.csv')

for registro in arquivo:
    print('Nome : {} Idade: {}'.format(*registro.strip().split(',')))
arquivo.close()
