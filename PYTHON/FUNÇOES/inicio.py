"""
Difinindo funçoes

-Funçoes sao pequenas partes de codigos que realizam tarefas especificas
"""


#exemplo de utilizaçao

#cores= ['verde', 'azul', 'branco']

#utilizando a funçao integrada (built in) do Python print()

#print (cores)

"""
def nome_da_funçao(parametros_de_entrada):
    bloco_da_funçao


onde:

nome_da_funcao -> SEMPRE, com letras minusculas, e se for nome composto separar por _ (underline)
parametros_de_entrada ->  opcionais, onde tendo mais de um separa por virgula
bloco_da_funçao -> também chamado de corpo da funçao é onde o processamente da funçao acontece, neste bloco pode ter ou nao retorno da funçao 


OBS: Veja que para definir uma funçao, utilizamos uma palavra reservada "def", informando ao pyhton que estamos definindo uma funçao e abrimos o bloco de codigo com :  que é utilizado em pyhton para definir blocos 
"""



def diz_oi():
    print ('oi')

#chamada de execuçao
diz_oi()

"""
OBS: veja que dentro das nossas funçoes podemos utilizar outras funçoes;
veja que nossa funçao só executa uma tarefa ou seja a unica coisa que ela faz é dizer "oi" 


"""





def cantar_parabens():
    print ("parabens pra voce")
    print ("muitas feli")

cantar=4 +9
cantar_parabens() 