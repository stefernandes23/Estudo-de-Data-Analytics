# Elabore um algoritmo que cria duas listas de dez posições e faça a 
# multiplicação dos elementos de mesmo índice, colocando o resultado em uma
# terceira lista, que deve ser mostrada como saída

lista_1 = [1,2,3,4,5,6,7,8,9,10]
lista_2 = [11,12,13,14,15,16,17,18,19,20]
lista_result = []

for num in range(0,10):
    lista_result.append(lista_1[num]*lista_2[num])

print(lista_result)