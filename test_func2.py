import func2
import unittest

class TestFuncs(unittest.TestCase):

    def test_deriver(self):
        # Entrée n'est pas une liste float
        self.assertEqual(func2.deriver([2]), False) # Entrée int
        self.assertEqual(func2.deriver(["a"]), False) # Entrée char
        self.assertEqual(func2.deriver([1+2j]), False) # Entrée complex
        self.assertEqual(func2.deriver([1.0, 1+5j, 3.0]), False)
        self.assertEqual(func2.deriver([1.0, "a", 3.0]), False)
        self.assertEqual(func2.deriver([1.0, 2, 3.0]), False)
        # Entrée est une liste vide
        self.assertIsNone(func2.deriver([]))
        # Entrée est vide
        self.assertIsNone(func2.deriver(None))
        # Test pour les résultats
        self.assertEqual(func2.deriver([2.5]), [0])
        self.assertEqual(func2.deriver([3.0, 2.5]), [3.0])
        self.assertEqual(func2.deriver([2.5, 3.0, 4.5]), [2*2.5, 3.0])
        self.assertEqual(func2.deriver([2.5, 3.0, 4.5]), [2*2.5, 3.0])
        
        


if __name__ == '__main__':
    unittest.main()