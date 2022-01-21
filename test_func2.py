import func2
import unittest

class TestFuncs(unittest.TestCase):

    def test_deriver(self):
        # Entree n'est pas une liste float
        # Entree ne contient qu'une seul valeur
        self.assertEqual(func2.deriver([2]), None) 
        self.assertEqual(func2.deriver(["a"]), None) 
        self.assertEqual(func2.deriver([1+2j]), None) 
        self.assertEqual(func2.deriver([2.0]), None) 
        # La taille de l'entree est correcte, mais contient une element non compatible
        self.assertEqual(func2.deriver([1, 2.0]), False)
        self.assertEqual(func2.deriver(["a", 1.0]), False)
        self.assertEqual(func2.deriver([1+2j, 1.0]), False)
        self.assertEqual(func2.deriver([1.0, 2]), False) 
        self.assertEqual(func2.deriver([1.0, "a"]), False) 
        self.assertEqual(func2.deriver([1.0, 1+2j]), False) 
        self.assertEqual(func2.deriver([1, 2.0, 3.0]), False)
        self.assertEqual(func2.deriver([1.0, "a", 3]), False)
        self.assertEqual(func2.deriver([1.0, 3.0, 1+5j]), False) 
        self.assertEqual(func2.deriver([1.0, 3.0, "a"]), False)
        self.assertEqual(func2.deriver([1.0, 2.0, 3]), False)

        # Entree est une liste vide
        self.assertIsNone(func2.deriver([]))
        # Entree est vide
        self.assertIsNone(func2.deriver(None))

        # Test pour les resultats
        self.assertEqual(func2.deriver([3.0, 2.5]), [-5])
        self.assertEqual(func2.deriver([2.5, 3.0, 4.5]), [5, 15])
        self.assertEqual(func2.deriver([1.0, 5.0, 2.5]), [50, 25])
        self.assertEqual(func2.deriver([3.9, 1.0, 5.0]), [-29, 40])
        self.assertEqual(func2.deriver([5.0, 2.5, 3.0, 4.5]), [25, 5, 15])
        self.assertEqual(func2.deriver([5.0, 2.5, 3.0, 4.5, 6.0]), [25, 5, 15, 15])

if __name__ == '__main__':
    unittest.main()