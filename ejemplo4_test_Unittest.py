import unittest

class Test_String(unittest.TestCase):

   @unittest.skip("check skipped tests") # skip() describe el salto
   def test_upper(self):

      self.assertEqual('PRUEBA'.lower(), 'prueba')
   def test_islower(self):

      self.assertTrue('prueba'.islower())
      self.assertFalse('Prueba'.islower())

if __name__ == '__main__':
   unittest.main()

# Al ejecutar va a dar una .s esto indica que se omite una prueba