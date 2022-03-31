from unittest import TestCase, main
from cap06 import distance
from cap07 import mysqrt, square_math, teste_square_root
from aleatorio import Calculadora
from func_ack import ack
from palindrome import teste_string, last
from cap08 import exibe_letras

class TestFunc(TestCase):
    
    def test_dist(self):
        self.assertEqual(distance(1, 1, 1 , 1), 1)
    
    def teste_operacao(self):
        self.assertEqual(Calculadora.__init__(1, 1,), 2)
    
    def teste_ack(self):
        self.assertEqual(ack(3, 4), 125)
    
    def teste_str(self):
        self.assertEqual(teste_string('marcos'), 'marcos')
    
    def teste_mid(self):
        self.assertEqual(last('ba'), 'a')
        
    def teste_sqrt(self):
        self.assertEqual(mysqrt(4, 3), 2)

    def teste_square_math(self):
        self.assertEqual(square_math(4, 3), 2)
    
    def teste_exibe_letras(self):
        self.assertEqual(exibe_letras('banana'), 'ananab')
    
    


if __name__ == '__main__':
    main()
    
