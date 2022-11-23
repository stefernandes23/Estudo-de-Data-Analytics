# Utilizando Programação Orientada a Objeto (POO):
# Desenvolva uma página que "emula" um computador de bordo de automovel. Para isso, seu algoritmo deve:
# -> Possuir um método que represente um carro com as característica: cor, capacidade 
# do tanque, quantidade de combustível no tanque, consumo médio (Km/Litro);
# -> O carro deve possuir métodos que:
# * Forneçam a previsão de quantos KM espera-se rodar com a quantidade de
#  combustível e o consumo médio;
# * Ande uma determinada quantidade em KM (argumento) e diminua a quantidade de 
# gasolina no tanque a partir de quantidade de km rodados e a média de consumo;

import os 
import time 

class Computador():

    def __init__(self,cor,modelo,consumo,combustivel):
        self.setcor(cor)
        self.setmodelo(modelo)
        self.setconsumo(consumo)
        self.setcombustivel(combustivel)


    def setcor(self,cor):
        self.cor = cor
    
    def setmodelo(self,modelo):
        self.modelo = modelo

    def setconsumo(self,consumo):
        self.consumo = consumo
    
    def getconsumo(self):
        return self.consumo
    
    def setcombustivel(self,combustivel):
        self.combustivel = combustivel 
    
    def getcombustivel(self):
        return self.combustivel


    def qnt_km(self):
        consumo_medio =  self.getcombustivel() * self.getconsumo()
        return print(f'O carro pode andar {consumo_medio} KM')


    def andou(self,kms):
        print (f'O carro só poderá andar {((self.getcombustivel() * self.getconsumo())-kms)} KM, pois ele só tem {self.getcombustivel() -(kms/self.getconsumo())} litros de gasolina.')
        self.setcombustivel(self.getcombustivel() -(kms/self.getconsumo()))
    

        
cor = input('Qual a cor do carro? ')
modelo = input('Qual o modelo do carro? ')
consumo_medio = float(input('Qual o consumo médio do carro? '))
combustivel = float(input('Qual a quantidade de combústivel no tanque? '))

carro = Computador(cor,modelo,consumo_medio,combustivel)


while True:
    menu = int(input('O que deseja fazer?\n[1] Visualizar a previsão de quilometragem\n[2] Andar \n[3] Visualizar quanto resta de combustivel\n[4] Sair\n'))
    if menu == 1:
        carro.qnt_km()
        time.sleep(3)
        os.system('cls')
    elif menu == 2:
        kms = float(input('Quanto você deseja andar?'))
        carro.andou(kms)
        time.sleep(3)
        os.system('cls')
    elif menu == 3:
        print(carro.getcombustivel())
        time.sleep(3)
        os.system('cls')
    elif menu == 4:
        print('Opção inválida')
        break

