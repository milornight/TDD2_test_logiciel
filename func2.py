from cgi import print_directory
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
        else :
            for i in range(l-2, -1, -1):
                print("indice i est : ", i, "\n")
                print("element de s[i] est : ", s[i],"\n")
                res.append(s[i]*abs(i-l+1))
            for item in res:
                print("resultat est : ", item, " ")
            res.reverse()
            return res


       

