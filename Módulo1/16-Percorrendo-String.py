## Escreva um loop que inicia no último caractere da string e caminha para o primeiro caractere,
# imprimindo cada letra em uma linha separada.


sentenca = str(input('Digite uma frase: '))


for i in range ((len(sentenca)-1),-1,-1): 
   print(sentenca[i]) 


