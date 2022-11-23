# Elabore um algoritmo que cria duas tuplas de dez posições e faça a
# multiplicação dos elementos de mesmo índice, colocando o resultado em uma
# terceira tupla, que deve ser mostrada como saída.


tupla = (1,2,3,4,5,6,7,8,9,10)
tupla_2 = (11,12,13,14,15,16,17,18,19,20)

tupla_result = tuple(tupla[x] * tupla_2[x] for x in range(0,len(tupla)))

print(tupla_result)

