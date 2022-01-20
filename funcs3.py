import math

# intervalle de temps: 1s
def derive2(x):
    l = len(x)
    d1 = []
    d2 = []
    if l < 3: 
        return None
    else: 
        if not isinstance(x[0], float):
            return False
        else:
            for i in range(1,l):
                if not isinstance(x[i], float):
                    return False
                s =  round(((x[i]-x[i-1])/1.0),1)
                d1.append(s)
            for n in range(1, len(d1)):
                s = round(((d1[n]-d1[n-1])/1.0),1)
                d2.append(s)
            return d2