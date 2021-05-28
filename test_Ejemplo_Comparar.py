# test para probar si son iguales
import unittest

class ClassTest(unittest.TestCase):
	"""docstring for ClassName"""
	def test_neg_method(self):
  		valor="barcelona"
  		valor2="barcelona"
  		mensaje="El valor1 no es igual al valor2"
  		self.assertEqual(valor,valor2,mensaje)

if __name__ == '__main__':
	unittest.main()