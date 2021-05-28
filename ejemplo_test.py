import unittest

def doblar(a): return a*2
def sumar(a,b): return a+b  

class PruebasFuncionesMatematicas(unittest.TestCase):

    def test_doblar(self):
        self.assertEqual(doblar(10), 20)
        self.assertEqual(doblar('Ab'), 'AbAb')

    def test_sumar(self):
        self.assertEqual(sumar(5, 7), 12)
        self.assertEqual(sumar('Ab' ,'cd'), 'Abcd')


if __name__ == '__main__':
    unittest.main()


