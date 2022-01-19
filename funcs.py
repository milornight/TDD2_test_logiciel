import string
import math

def miroir(s,n):
    l = len(s)
    miroir = ''
    if l == 0:
        return None
    elif l <= n:
        return False
    else:
        miroir = s[0:n+1]
        for i in range(n,-1,-1):   
            miroir = miroir + s[i]
        return miroir