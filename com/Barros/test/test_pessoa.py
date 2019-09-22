import unittest

from com.Barros.cadPessoa import Pessoa


class TestPessoa(unittest.TestCase):
    def setUp(self):
        self.pessoa = Pessoa("Sergio", "Barros", (25, 7, 1990))

    def testatributos(self):
        self.assertEqual(self.pessoa.nome, "Sergio")
        self.assertEqual(self.pessoa.sobrenome, "Barros")
        self.assertEqual(self.pessoa.nascimento, (25, 7, 1990))

    def testidasde(self):
        self.assertEqual(self.pessoa.idade(), 29, "Deve ser 29")
