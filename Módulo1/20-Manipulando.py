# * Utilize o seguinte código em Python que guarda uma string:
#     * dado = 'X-DSPAM-Confidence:0.8475'
# * Extraia a porção da string depois do sinal de dois pontos, converta a string extraída em um número e multiplique por 100, exiba o resultado em tela. 

str1 = 'X-DSPAM-Confidence:0.8475'
str2 = (str1.find(':')+1) ## O : é o padrão que vem antes de qualquer número. E o +1 é pra começar no caractere dps dos ':'
str3 = (str1[str2:])
str4 = (float(str3)) ## conversão da str3
 
print (str4*100)



