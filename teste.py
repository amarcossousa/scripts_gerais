from unittest import TestCase, main
from cap06 import distance
from aleatorio import Calculadora
from func_ack import ack
from palindrome import teste_string, last

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
        
        

if __name__ == '__main__':
    main()
    
