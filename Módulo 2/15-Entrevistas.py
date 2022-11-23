# '''
# Utilizando Programação Orientada a Objeto (POO):
# Desenvolve uma classe "Entrevistado" com os seguintes requisitos: 
# * Tenha os atributos: idade, cidade, estado, salário atual e escolaridade;
# * Tenha um método "Imprimir dados" que devolve as informação do entrevistado em uma
# string com os atributos separados por vírgula (Ex: 20, Rio de Janeiro, RJ, 1000, Superior);

class Entrevistado():
    def __init__(self, nome, idade, cidade, estado, salario, escolaridade):
        self.setnome(nome)
        self.setidade(idade)
        self.setcidade(cidade)
        self.setestado(estado)
        self.setsalario(salario)
        self.setescolaridade(escolaridade)

    
    def getnome(self):
        return self.nome

    def setnome(self,nome):
        self.nome = nome
    
    def getidade(self):
        return self.idade

    def setidade(self,idade):
        self.idade = idade
    
    def getcidade(self):
        return self.cidade

    def setcidade(self,cidade):
        self.cidade = cidade

    def getestado(self):
        return self.estado

    def setestado(self,estado):
        self.estado = estado

    def getesalario(self):
        return self.salario

    def setsalario(self,salario):
        self.salario = salario


    def getescolaridade(self):
        return self.escolaridade

    def setescolaridade(self,escolaridade):
        self.escolaridade = escolaridade

    def imprimir(self):
        print(f"{self.nome},{self.idade},{self.cidade},{self.estado},{self.salario},{self.escolaridade}")   


entrevistado = Entrevistado('Luiza',22,"São Gonçalo",'Rio de Janeiro', 3000,'Médio Completo')

entrevistado.imprimir()




        




