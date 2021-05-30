# Se importa el Modulo Unittest
# Se van a usar tres metodos de cadena de Pruebas
#test_string_equality, test_string_case, test_is_string_upper
import unittest
class TestingStringMethods(unittest.TestCase):

   # Este método prueba si dos cadenas son iguales
   def test_string_equality(self):
      self.assertEqual('ssp' * 6, 'sspsspsspsspsspssp')

   # Este método prueba si dos casos de cadena son iguales
   def test_string_case(self):
      self.assertEqual('tutorialspoint'.upper(), 'TUTORIALSPOINT')

   # Este método prueba si la cadena está en mayúsculas o no
   def test_is_string_upper(self):
      self.assertTrue('TUTORIALSPOINT'.isupper())
      self.assertFalse('TUTORIALSpoint'.isupper())

if __name__ == '__main__':
	unittest.main()
