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

        # Test pour le resultat
        self.assertEqual(func4.appro([4.0], 3.0, 0.1), 0.0)
        self.assertEqual(func4.appro([4.0], 3.0, 0.01), 0.00)
        

if __name__ == '__main__':
    unittest.main()