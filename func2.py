import string
import math

def deriver(s):
    if (s==None):
        return None
    l = len(s)
    res = []
    # parcour la liste s à vérifier le type des éléments
    if l == 0:
        return None
    else :
        for item in s:
            if( type(item) != float):
                print(item)
                return False
        # calcule la dérivée de s
        if l == 1:
            return [0]

       

