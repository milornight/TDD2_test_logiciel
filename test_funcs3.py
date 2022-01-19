import funcs3
import unittest

class TestFuncs(unittest.TestCase):

    def test_derive2(self):
        self.assertEqual(funcs3.derive2([]),None) # liste empty

        # liste entre ne sont pas forcement une liste float
        self.assertFalse(funcs3.derive2(["d","fhe","1.48"])) 
        self.assertFalse(funcs3.derive2([3, 4, 6, 8])) 

        self.assertEqual(funcs3.derive2([0.0]),None) # trop peu de points pour determiner la derive seconde 

        self.assertEqual(funcs3.derive2([1.0, 2.0, 3.0]),[0.0])
        self.assertEqual(funcs3.derive2([2.3, 5.7, 10.0]),[0.9])
        self.assertEqual(funcs3.derive2([1.0, 2.3, 5.7, 10.2, 29.6]),[2.1, 1.1, 14.9])

if __name__ == '__main__':
    unittest.main()