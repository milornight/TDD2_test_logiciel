import func4
import unittest

class TestFuncs(unittest.TestCase):

    def test_approximatipn(self):
        # Test les parametres
        # Test pour les parametres insuffisant
        self.assertEqual(func4.appro([4], None, None), None) 
        self.assertEqual(func4.appro([4], 3.0, None), None)

        # Test pour le premier parametre non valid
        # 1er parametre n'est pas une liste
        self.assertEqual(func4.appro(4, 3.0, 0.01), None)
        self.assertEqual(func4.appro(3.0, 3.0, 0.01), None)
        self.assertEqual(func4.appro("a", 3.0, 0.01), None)
        self.assertEqual(func4.appro(1+2j, 3.0, 0.01), None)

        # la liste n'est pas de type float
        self.assertEqual(func4.appro(["a"], 3.0, 0.01), None)
        self.assertEqual(func4.appro([1+2j], 3.0, 0.01), None)
        self.assertEqual(func4.appro([4], 3.0, 0.01), None)
        self.assertEqual(func4.appro([], 3.0, 0.01), None)

        # Test pour le 2e parametre
        # 2e parametre n'est pas un float
        self.assertEqual(func4.appro([4.0], 3, 0.01), None)
        self.assertEqual(func4.appro([4.0], "a", 0.01), None)
        self.assertEqual(func4.appro([4.0], 1+2j, 0.01), None)
        self.assertEqual(func4.appro([4.0], [3.0], 0.01), None)

        # Test pour le 3e parametre
        # ce n'est pas un ordre de grandeur
        self.assertEqual(func4.appro([4.0], 3.0, 1), None)
        self.assertEqual(func4.appro([4.0], 3.0, "a"), None)
        self.assertEqual(func4.appro([4.0], 3.0, 1+2j), None)
        self.assertEqual(func4.appro([4.0], 3.0, [3]), None)
        self.assertEqual(func4.appro([4.0], 3.0, 0.02), None)

        
        
        

if __name__ == '__main__':
    unittest.main()