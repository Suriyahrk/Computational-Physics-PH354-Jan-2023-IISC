import numpy as np
import scipy.constants as sc
import sys
sys.path.insert(0,'.')
from Root_finding import *



"""
Using the expressions derived in HW3_Explanations.pdf. We will be finding the first  five ground state energy levels of finite square
well using false position method.

"""
hbar = sc.hbar
m = sc.electron_mass
e = sc.electron_volt
w = 10**(-9)
Error = 0.001
V = 20
pi = np.pi
i = 0 # for inititalizing


def f_even(x):
        return np.sqrt( (V - x) / x ) - np.tan( w* (np.sqrt(2* m * x * e) ) / (2* hbar) )

def f_odd(x):
        return np.sqrt( (V - x) / x ) + 1 / (np.tan( w* (np.sqrt(2* m *x * e) ) / (2* hbar) ) )
    
F = np.array([f_even,f_odd])

k =  np.pi**2 * hbar**2 /( 2* m * e * w**2)   

for i in np.arange(0,6):
    
    if i%2 == 0:
        # adjusting the value by slight amounts to avoid blowing up at 0
        a =  (2* i)**2 * k + 0.001
        b =  (2*i + 1 )**2 * k -0.001
    
    else :
        a =  (2* i + 1)**2 * k + 0.001
        b =  (2*i + 2 )**2 * k -0.001


    if (a >= V):
        print(f"No more Bound states")
        break 

    elif (b >= V): # Searching for roots only in real region
         b = V
    
    print(f" The energy of the {i}th state is {false_p(a ,b ,e, 100, F[i%2])} eV")

# Output 

"""
    The energy of the 0th state is 0.2942543432594435 eV
    The energy of the 1th state is 3.654342287297148 eV
    The energy of the 2th state is 6.216713432676319 eV
    The energy of the 3th state is 19.13449054913013 eV

    No more Bound states
"""









