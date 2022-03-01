from unittest import TestCase, main
from cap06 import distance
from aleatorio import Calculadora
from func_ack import ack

class TestFunc(TestCase):
    
    def test_dist(self):
        self.assertEqual(distance(1, 1, 1 , 1), 1)
    
    def teste_operacao(self):
        self.assertEqual(Calculadora.__init__(1, 1,), 2)
    
    def teste_teste(self):
        pass
    
    def teste_ack(self):
        self.assertEqual(ack(3, 6), 509)


if __name__ == '__main__':
    main()
    
