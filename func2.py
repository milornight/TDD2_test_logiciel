from cgi import print_directory
import string
import math

# le format de s est [f(x0), f(x0+h), f(x0+2h), ...]
# h = 0.1 par defaut
def deriver(s):
    if (s==None):
        return None
    l = len(s)
    # parcour la liste s pour verifier le type des elements
    if l < 2 :
        return None
    else :
        for item in s:
            if( type(item) != float):
                print(item)
                return False
        # calcule la derivee de s
        res = []
        if l == 2:
            res.append(round((s[1]-s[0])/0.1, 2))
            return res
        else :
            for i in range(l-1) :
                print("s[",i,"] est : ", s[i])
                print("s[",i+1,"] est : ", s[i+1])
                res.append(round((s[i+1]-s[i])/0.1, 2))
            return res


       

