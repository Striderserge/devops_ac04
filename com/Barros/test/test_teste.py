from unittest import TestCase
from com.Barros.divisao import Teste 

class Teste(TestCase):
    def setUp(self):
        self.Divisao = Divisao()
    
    def test_divisao(self):
        self.assertEqual(self.Divisao.div_2(10),5,"deve ser 5")