# * Leia a entrada com temperatura do usuário até que ele digite 'sair'.
# * Exiba na tela: 
# "você está com febre. Tome um remédio e repouse" quando a temperatura estiver entre 38 e 39 graus;
# "Você está com febre. Tome um remédio e procure um médico." para qualquer temperatura acima disso;
# e "Nada de febre" caso contrário
temperatura = input(' Digite sua temperatura: ')

while temperatura != 'sair' :
    temperatura2 = int(temperatura)
    if temperatura2 >= 38 and temperatura2 < 39:
        print ('Você esta com febre, tome um remédio e repouse.')
    elif temperatura2 > 39:
        print('Tome remédio e procure um médico')
    else:
        print('Nada de febre ')
    
    temperatura = input(' Digite sua temperatura: ')
    
   
    

print('fim')




