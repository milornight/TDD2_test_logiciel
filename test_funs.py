import funcs
import unittest

class TestFuncs(unittest.TestCase):

    def test_miroir(self):
        self.assertEqual(funcs.miroir("shfenk",4),"shfennefhs")
        self.assertEqual(funcs.miroir("s",0),"ss")
        self.assertFalse(funcs.miroir("sdhj",5)) # indice trop grand
        self.assertEqual(funcs.miroir("",0),None) # string empty

if __name__ == '__main__':
    unittest.main()