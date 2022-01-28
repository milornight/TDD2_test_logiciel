import func4
import math
import unittest

class TestFuncs(unittest.TestCase):

    def test_entrees(self):
        # Test les parametres
        # Test pour les parametres insuffisant
        self.assertEqual(func4.appro(None, 3.0, 0.1), 200)
        self.assertEqual(func4.appro(math.sin, None, None), 200) 
        self.assertEqual(func4.appro(math.sin, 3.0, None), 200)

        # Test pour le premier parametre non valid
        # 1er parametre n'est pas une fonction
        self.assertEqual(func4.appro(4, 3.0, 0.01), 210)
        self.assertEqual(func4.appro(3.0, 3.0, 0.01), 210)
        self.assertEqual(func4.appro("a", 3.0, 0.01), 210)
        self.assertEqual(func4.appro(1+2j, 3.0, 0.01), 210)

        # Test pour le 2e parametre
        # 2e parametre n'est pas un float
        self.assertEqual(func4.appro(math.sin, 3, 0.01), 220)
        self.assertEqual(func4.appro(math.sin, "a", 0.01), 220)
        self.assertEqual(func4.appro(math.sin, 1+2j, 0.01), 220)
        self.assertEqual(func4.appro(math.sin, [3.0], 0.01), 220)

        # Test pour le 3e parametre
        # ce n'est pas un ordre de grandeur
        self.assertEqual(func4.appro(math.sin, 3.0, 1), 230)
        self.assertEqual(func4.appro(math.sin, 3.0, "a"), 230)
        self.assertEqual(func4.appro(math.sin, 3.0, 1+2j), 230)
        self.assertEqual(func4.appro(math.sin, 3.0, [3]), 230)
        self.assertEqual(func4.appro(math.sin, 3.0, 0.02), 231)
        self.assertEqual(func4.appro(math.sin, 3.0, 1.0), 231)

    def test_fonc_arrondi(self):
        # Test pour la fonction d'arrondi
        self.assertEqual(func4.arrondi(1.456, 0.1), 1.5)
        self.assertEqual(func4.arrondi(1.456, 0.01), 1.46)
        self.assertEqual(func4.arrondi(1.456, 0.001), 1.456)
        self.assertEqual(func4.arrondi(1.456, 0.0001), 1.456)
        self.assertEqual(func4.arrondi(1.454, 0.01), 1.45)
        self.assertEqual(func4.arrondi(1.499, 0.1), 1.5)
        self.assertEqual(func4.arrondi(1.499, 0.01), 1.50)

    def test_approximation(self):
        # Test pour le resultat
        self.assertEqual(func4.appro(math.sin, 3.0, 0.1), -1.0)
        self.assertEqual(func4.appro(math.sin, 3.0, 0.01), -0.99) # avec un ordre de grandeur plus petit
        self.assertEqual(func4.appro(math.exp, 3.5, 0.01), 33.12)
        self.assertEqual(func4.appro(math.log, 3.5, 0.01), 0.29)
        self.assertEqual(func4.appro(math.sqrt, 3.5, 0.01), 0.27) 
        self.assertEqual(func4.appro(math.cos, 3.5, 0.01), 0.35) 
        
if __name__ == '__main__':
    unittest.main()