import func2
import unittest

class TestFuncs(unittest.TestCase):

    def test_deriver(self):
        self.assertEqual(func2.deriver([2.5,3,4.5]),[6.25,3])
        self.assertEqual(func2.deriver([3,2.5],[3]))
        self.assertEqual(func2.deriver([2.5]),[0])
        self.assertFalse(func2.deriver([2],None)) # return est vide

if __name__ == '__main__':
    unittest.main()