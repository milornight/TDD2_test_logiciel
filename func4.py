from binascii import b2a_base64
import string
import math
from decimal import *

# les entrees sont (fonc, point, ordre)
# fonc : type liste float [3.5, 4.0, 4.5, 3.0] = 3.5x^3 + 4.0*x^2 + 4.5*x + 3.0
# point : type float
# ordre : type float
list_ordre = [0.1, 0.01, 0.001, 0.0001, 0.00001, 0.000001, 0.0000001]
def appro(fonc, point, ordre):
    if (fonc == None or point == None or ordre == None):
        return "Error: Missing parameters"
    if not isinstance(fonc, list) :
        return "Error: The first parameter is not a list"
    if not isinstance(point, float) :
        return "Error: The second parameter is not a float"
    if  not isinstance(ordre, float) :
        return "Error: The third parameter is not a float"
    else :
        if ordre not in list_ordre:
            return "Error: The third parameter is not a order of magnitude"
        else :
            arr = str(ordre)
    length = len(fonc)
    if length == 0:
        return "Error: The first parameter is empty"
    else :
        for item in fonc:
            if( not isinstance(item, float)):
                print(item)
                return "Error: Elements in the first parameter are not float"
        res = 0
        if( length == 1 ) :
            return Decimal(0).quantize(Decimal(arr))
        else :
            x_add_h = point + ordre
            x_moins_h = point - ordre
            for i in range(length-1):
                expo = length-i-1
                a = x_add_h
                b = x_moins_h
                c = 0
                for x in range(expo-1):
                    a *= x_add_h
                    b *= x_moins_h
                a = a * fonc[i]
                b = b * fonc[i]
                c = a - b
                res +=c
            res = res / (2*ordre)
            res = arrondi(res, ordre)
            return res

def arrondi(val, arr):
    arr_str = str(arr)
    digits_location = arr_str.find('.')
    nombre = len(arr_str[digits_location + 1:])
    val_str = str(val)
    if ( len(val_str) < len(arr_str)) :
        return float(val_str)
    else :
        return round(val, nombre)

