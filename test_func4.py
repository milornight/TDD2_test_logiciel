import func4
import math
import unittest

class TestFuncs(unittest.TestCase):

    def test_approximatipn(self):
        # Test les parametres
        # Test pour les parametres insuffisant
        self.assertEqual(func4.appro(None, 3.0, 0.1), "Error: Missing parameters")
        self.assertEqual(func4.appro(math.sin, None, None), "Error: Missing parameters") 
        self.assertEqual(func4.appro(math.sin, 3.0, None), "Error: Missing parameters")

        # Test pour le premier parametre non valid
        # 1er parametre n'est pas une liste
        self.assertEqual(func4.appro(4, 3.0, 0.01), "Error: The first parameter is not a function")
        self.assertEqual(func4.appro(3.0, 3.0, 0.01), "Error: The first parameter is not a function")
        self.assertEqual(func4.appro("a", 3.0, 0.01), "Error: The first parameter is not a function")
        self.assertEqual(func4.appro(1+2j, 3.0, 0.01), "Error: The first parameter is not a function")

        # Test pour le 2e parametre
        # 2e parametre n'est pas un float
        self.assertEqual(func4.appro(math.sin, 3, 0.01), "Error: The second parameter is not a float")
        self.assertEqual(func4.appro(math.sin, "a", 0.01), "Error: The second parameter is not a float")
        self.assertEqual(func4.appro(math.sin, 1+2j, 0.01), "Error: The second parameter is not a float")
        self.assertEqual(func4.appro(math.sin, [3.0], 0.01), "Error: The second parameter is not a float")

        # Test pour le 3e parametre
        # ce n'est pas un ordre de grandeur
        self.assertEqual(func4.appro(math.sin, 3.0, 1), "Error: The third parameter is not a float")
        self.assertEqual(func4.appro(math.sin, 3.0, "a"), "Error: The third parameter is not a float")
        self.assertEqual(func4.appro(math.sin, 3.0, 1+2j), "Error: The third parameter is not a float")
        self.assertEqual(func4.appro(math.sin, 3.0, [3]), "Error: The third parameter is not a float")
        self.assertEqual(func4.appro(math.sin, 3.0, 0.02), "Error: The third parameter is not a order of magnitude")
        self.assertEqual(func4.appro(math.sin, 3.0, 1.0), "Error: The third parameter is not a order of magnitude")

        # Test pour la fonction d'arrondi
        self.assertEqual(func4.arrondi(1.456, 0.1), 1.5)
        self.assertEqual(func4.arrondi(1.456, 0.01), 1.46)
        self.assertEqual(func4.arrondi(1.456, 0.001), 1.456)
        self.assertEqual(func4.arrondi(1.456, 0.0001), 1.456)
        self.assertEqual(func4.arrondi(1.454, 0.01), 1.45)
        self.assertEqual(func4.arrondi(1.499, 0.1), 1.5)
        self.assertEqual(func4.arrondi(1.499, 0.01), 1.50)

        # Test pour le resultat
        self.assertEqual(func4.appro(math.sin, 3.0, 0.1), -1.0)
        self.assertEqual(func4.appro(math.sin, 3.0, 0.01), -0.99) # avec un ordre de grandeur plus petit
        self.assertEqual(func4.appro(math.exp, 3.5, 0.01), 33.12)
        self.assertEqual(func4.appro(math.log, 3.5, 0.01), 0.29)
        self.assertEqual(func4.appro(math.sqrt, 3.5, 0.01), 0.27) 
        self.assertEqual(func4.appro(math.cos, 3.5, 0.01), 0.35) 
        
if __name__ == '__main__':
    unittest.main()