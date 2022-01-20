import func2
import unittest

class TestFuncs(unittest.TestCase):

    def test_deriver(self):
        # Entrée n'est pas une liste float
        # Entrée ne contient qu'une seul valeur
        self.assertEqual(func2.deriver([2]), None) 
        self.assertEqual(func2.deriver(["a"]), None) 
        self.assertEqual(func2.deriver([1+2j]), None) 
        self.assertEqual(func2.deriver([2.0]), None) 
        # La taille de l'entrée est correcte, mais contient une élément non compatible
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
        # la taille d'entrée est trop grande
        self.assertEqual(func2.deriver([5.0, 2.5, 3.0, 4.5]), None)
        self.assertEqual(func2.deriver([5.0, 2.5, 3.0, 4.5, 6.0]), None)
        # Entrée est une liste vide
        self.assertIsNone(func2.deriver([]))
        # Entrée est vide
        self.assertIsNone(func2.deriver(None))

        # Test pour les résultats
        self.assertEqual(func2.deriver([3.0, 2.5]), 0.5)
        self.assertEqual(func2.deriver([2.5, 3.0, 4.5]), -0.11)
        self.assertEqual(func2.deriver([1.0, 5.0, 2.5]), -1.6)
        self.assertEqual(func2.deriver([3.9, 1.0, 5.0]), 0.58)