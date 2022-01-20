import func4
import unittest

class TestFuncs(unittest.TestCase):

    def test_approximatipn(self):
        # Test les parametres
        # Test pour les parametres insuffisant
        self.assertEqual(func4.appro(None, 3.0, 0.1), "Error: Missing parameters")
        self.assertEqual(func4.appro([4], None, None), "Error: Missing parameters") 
        self.assertEqual(func4.appro([4], 3.0, None), "Error: Missing parameters")

        # Test pour le premier parametre non valid
        # 1er parametre n'est pas une liste
        self.assertEqual(func4.appro(4, 3.0, 0.01), "Error: The first parameter is not a list")
        self.assertEqual(func4.appro(3.0, 3.0, 0.01), "Error: The first parameter is not a list")
        self.assertEqual(func4.appro("a", 3.0, 0.01), "Error: The first parameter is not a list")
        self.assertEqual(func4.appro(1+2j, 3.0, 0.01), "Error: The first parameter is not a list")

        # la liste n'est pas de type float
        self.assertEqual(func4.appro(["a"], 3.0, 0.01), "Error: Elements in the first parameter are not float")
        self.assertEqual(func4.appro([1+2j], 3.0, 0.01), "Error: Elements in the first parameter are not float")
        self.assertEqual(func4.appro([4], 3.0, 0.01), "Error: Elements in the first parameter are not float")
        self.assertEqual(func4.appro([4.0, 4], 3.0, 0.01), "Error: Elements in the first parameter are not float")
        self.assertEqual(func4.appro([4.0, "a"], 3.0, 0.01), "Error: Elements in the first parameter are not float")
        self.assertEqual(func4.appro([4.0, 1+2j], 3.0, 0.01), "Error: Elements in the first parameter are not float")
        self.assertEqual(func4.appro([], 3.0, 0.01), "Error: The first parameter is empty")

        # Test pour le 2e parametre
        # 2e parametre n'est pas un float
        self.assertEqual(func4.appro([4.0], 3, 0.01), "Error: The second parameter is not a float")
        self.assertEqual(func4.appro([4.0], "a", 0.01), "Error: The second parameter is not a float")
        self.assertEqual(func4.appro([4.0], 1+2j, 0.01), "Error: The second parameter is not a float")
        self.assertEqual(func4.appro([4.0], [3.0], 0.01), "Error: The second parameter is not a float")

        # Test pour le 3e parametre
        # ce n'est pas un ordre de grandeur
        self.assertEqual(func4.appro([4.0], 3.0, 1), "Error: The third parameter is not a float")
        self.assertEqual(func4.appro([4.0], 3.0, "a"), "Error: The third parameter is not a float")
        self.assertEqual(func4.appro([4.0], 3.0, 1+2j), "Error: The third parameter is not a float")
        self.assertEqual(func4.appro([4.0], 3.0, [3]), "Error: The third parameter is not a float")
        self.assertEqual(func4.appro([4.0], 3.0, 0.02), "Error: The third parameter is not a order of magnitude")
        self.assertEqual(func4.appro([4.0], 3.0, 1.0), "Error: The third parameter is not a order of magnitude")

        # Test pour la fonction d'arrondi
        self.assertEqual(func4.arrondi(1.456, 0.1), 1.5)
        self.assertEqual(func4.arrondi(1.456, 0.01), 1.46)
        self.assertEqual(func4.arrondi(1.456, 0.001), 1.456)
        self.assertEqual(func4.arrondi(1.456, 0.0001), 1.456)
        self.assertEqual(func4.arrondi(1.454, 0.01), 1.45)
        self.assertEqual(func4.arrondi(1.499, 0.1), 1.5)
        self.assertEqual(func4.arrondi(1.499, 0.01), 1.50)

        # Test pour le resultat
        self.assertEqual(func4.appro([4.0], 3.0, 0.1), 0.0)
        self.assertEqual(func4.appro([4.0], 3.0, 0.01), 0.00)
        self.assertEqual(func4.appro([1.0, 3.0], 3.5, 0.01), 1.00)
        self.assertEqual(func4.appro([1.0, 1.0, 3.0], 3.5, 0.01), 8.00)
        self.assertEqual(func4.appro([1.0, -1.0, 3.0], 3.5, 0.01), 6.00) # avec un coef negatif
        self.assertEqual(func4.appro([1.0, 1.0, 3.0], 3.5, 0.001), 8.000) # avec un ordre de grandeur plus petit
        self.assertEqual(func4.appro([1.0, 1.0, 1.0, 3.0], 3.5, 0.01), 44.75)
        self.assertEqual(func4.appro([2.0, 2.0, 1.0, 3.0], 3.5, 0.01), 88.50)
        
if __name__ == '__main__':
    unittest.main()