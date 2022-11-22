# Implemente as funções abaixo:
# -> Uma função que acrescenta uma quantidade X de elementos a fila;
# -> Uma função que verifica a quantidade de elementos na fila;
# -> Uma função que verifica se a fila está vazia ou não;

def adc_fila(fila):
    while True:
        adicionando = input('O que você deseja adicionar?')
        fila.append(adicionando)
        if adicionando == 'Sair':
            fila.remove(adicionando)
            break

def cont_fila(fila):
        print (f'Quantidade de elementos na lista: {(len(fila))}')


def verif_vazio(lista):
    if len(lista) == 0:
        print ('A lista ta vazia.')
    else:
        print('A lista não esta vazia.')

        
fila = []

verif_vazio(fila)
adc_fila(fila)   
print(fila)
cont_fila(fila)