# * Implemente as funções abaixo:
# -> Uma função que retire uma quantidade X de elementos da pilha;
# -> Uma função que verifica a quantidade de elementos na pilha;
# -> Uma função que verifica se a pilha está vazia ou não;


def adc_pilha(pilha):
    while True:
        adicionando = input('O que você deseja adicionar?')
        pilha.append(adicionando)
        if adicionando == 'Sair':
            pilha.remove(adicionando)
            break


def remove_pilha(pilha):
    return pilha.pop(-1)


def cont_pilha(pilha):
    print (f'Quantidade de elementos na lista: {(len(pilha))}')


def verif_vazio(lista):
    if len(lista) == 0:
        print ('A lista ta vazia.')
    else:
        print('A lista não esta vazia.')


pilha = []


adc_pilha(pilha)

print(pilha)

cont_pilha(pilha)

remove_pilha(pilha)

print(pilha)

cont_pilha(pilha)
