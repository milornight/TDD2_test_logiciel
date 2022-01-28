import string
import math
from decimal import *
from sympy import *
from sympy.utilities.lambdify import lambdify, implemented_function
from scipy import misc

# les entrees sont (fonc, point, ordre)
# fonc : type liste float [3.5, 4.0, 4.5, 3.0] = 3.5x^3 + 4.0*x^2 + 4.5*x + 3.0
# point : type float
# ordre : type float
x = symbols('x')
list_ordre = [0.1, 0.01, 0.001, 0.0001, 0.00001, 0.000001, 0.0000001]
function = [math.sin, math.cos, math.tan, math.exp, math.expm1,\
            math.log, math.log2, math.log10, math.sqrt]
func_symbolic = [sin(x), cos(x), tan(x), exp(x), exp(x)-1,\
                log(x), log(x)/log(2), log(x)/log(10), sqrt(x)]
def appro(fonc, point, ordre):
    # "Error: Missing parameters"
    if (fonc == None or point == None or ordre == None):
        return 200 
    
     # "Error: The first parameter is not a mathematic function"
    if fonc not in function :
        return 210 
    
    # "Error: The second parameter is not a float"
    if not isinstance(point, float) :
        return 220

    # "Error: The third parameter is not a float"
    if  not isinstance(ordre, float) :
        return 230
    else :
        # "Error: The third parameter is not a order of magnitude"
        if ordre not in list_ordre:
            return 231
        else :
        #calculer l'approximation de la derivee de la fonction
            expr = func_symbolic[function.index(fonc)] # recuperer fonction symbolique correspondante
            exp_deriv = expr.diff(x) # calculer la derivee
            #print("expression de derivee", exp_deriv)
            exp_deriv = lambdify(x, exp_deriv)  # rend la variable calculable
            #print("expression de derivee en point", exp_deriv(point))
            res = arrondi(exp_deriv(point), ordre)
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

