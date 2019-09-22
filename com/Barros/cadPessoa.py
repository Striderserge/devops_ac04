import time


class Pessoa:
    def __init__(self, nome, sobrenome, nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.nascimento = nascimento

    def idade(self):
        ano_a, mes_a = time.gmtime()[:2]
        mes_n, ano_n = self.nascimento[1:]
        idade = ano_a - ano_n

        if mes_a < mes_n:
            return idade - 1

        return idade
        