import func2
import unittest

class TestFuncs(unittest.TestCase):

    def test_deriver(self):
        self.assertEqual(func2.deriver([2.5,3,4.5]),[6.25,3])
        self.assertEqual(func2.deriver([2.5,3,4.5]),[2.5*2.5,3])
        self.assertEqual(func2.deriver([3,2.5],[3]))
        self.assertEqual(func2.deriver([2.5]),[0])
        self.assertFalse(func2.deriver([2],None)) # return est vide au lieu de la liste [0]
        self.assertEqual(func2.deriver(["a"],False)) # Entrée n'est pas une liste float
        self.assertEqual(func2.deriver([],None)) # Entrée est une liste vide

if __name__ == '__main__':
    unittest.main()