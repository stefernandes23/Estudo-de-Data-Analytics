class Cachorro():
    nome = ''
    cor = ''
    raca = ''
    idade = 0
    nascimento = ""

    def inserirDados(self, nome_entrada, cor_entrada, raca_entrada, idade_entrada, nascimento_entrada):
        self.nome = nome_entrada
        self.cor = cor_entrada
        self.raca = raca_entrada
        self.idade = idade_entrada
        self.nascimento = nascimento_entrada

    def latir(self):
        return "AU AU AU AU\nO cachorro latiu!"

    def comer(self):
        return "O cachorro comeu!"

cao = Cachorro()
latindo = cao.latir()
print(latindo)