from cgi import print_directory
import string
import math

# le format de s est [f(x0+h), f(x0)] ou [f(x0+h), f(x0), h]
def deriver(s):
    if (s==None):
        return None
    l = len(s)
    res = 0
    # parcour la liste s pour verifier le type des elements
    if l < 2 or l > 3:
        return None
    else :
        for item in s:
            if( type(item) != float):
                print(item)
                return False
        # calcule la derivee de s
        if l == 2:
            # h est 1 par defaut
            return s[0]-s[1]
        else :

            return round((s[0]-s[1])/s[2],2)


       

