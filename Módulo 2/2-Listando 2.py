# * Reutilize a lista de nomes montada na atividade anterior;
# * Crie uma nova lista com mais 3 nomes,
#  concatene com a anterior e verifique se os nomes dos facilitadores estão continos nessas listas;

nomes_1 = ['Luiza','Lucas','Dayson','Esli','Marisa']
nomes_2 = ['Yas','Ana','Rafa']
nomes_concat = nomes_1 + nomes_2

for nome in nomes_concat:
    if nome in ['Dayson','Esli','Marisa','Rafa']:
        print (f'{nome} é uma pessoa facilitadora!')
    elif nome in ['Ana','Yas']:
        print(f'{nome} não é uma pessoa facilitadora, mas faz parte do nosso time de engajamento!')
    else:
        print(f'{nome} não é uma pessoa facilitadora')

