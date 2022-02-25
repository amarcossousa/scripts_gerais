from unittest import TestCase, main
from cap06 import distance
from aleatorio import Calculadora

class TestFunc(TestCase):
    
    def test_dist(self):
        self.assertEqual(distance(1, 1, 1 , 1), 0)
    
    def teste_operacao(self):
        self.assertEqual(Calculadora.__init__(1, 1,), 2)
        


if __name__ == '__main__':
    main()
    
