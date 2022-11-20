## Fórmula utilizada = z**2 * p(1-p)/e**2 / 1+ (z**2.p(1-p)/e**2.N      
    ## O p é um valor fixo que se trata do desvio padrão. Nesse caso valerá 0.5. 
print(' ')
print(' '*32 +'CALCULE O TAMANHO DA SUA AMOSTRA')
print(' '*37 +'Grau de confiança: 95%') # O Grau de confiança de 95% é o padrão do setor.  

## Dados que serão fornecidos pelo usuário para que o cálculo possa ser rodado. 
tamanho_população  = int(input('Digite o tamanho da populaçao: ')) ## Corresponde a variável N na fórmula. 
margem_de_erro  = float(input('Digite a margem de erro: '))/100 ## Corresponde a variável E na fórmula. O usuário fornecerá a margem de erro em porcentagem e o programa coverterá o valor para decimal.
escore  = (1.96**2) ## Corresponde ao z na fórmula. Se trata de um valor fixo nesse caso pois é determinado pelo Grau de confiança. 

## Divisão da fórmula em duas partes.
formula1 = (escore * 0.5 * (1- 0.5)) / ((margem_de_erro)**2)
formula2 = 1+((escore * 0.5 * (1- 0.5))) / ((margem_de_erro)**2 * tamanho_população)

## Função que divide a fórmula1 pela fórmula2.
def divisão(x,y):
    return x/y
resultado = divisão(formula1,formula2)

print('')
print(f'Tamanho da Amostra: {round(resultado)}')

