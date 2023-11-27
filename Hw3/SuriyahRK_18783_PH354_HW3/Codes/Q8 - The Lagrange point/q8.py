import numpy as np
import sympy as smp
import matplotlib.pyplot as plt
import scipy.constants as sc
import sys
sys.path.insert(0,'.')
from Root_finding import *

G = sc.G
M = 5.974* 10**(24)
m = 7.348*10**(22)
R = 3.844 * 10**(8)
w = 2.662*10**(-6)

def f(r):
    return G*M / (r**2) - G*m / ((R-r)**2) - (w**2)*r 

e = 0.5* 10**(-3)

print(f"The distance of L_1 from Earth computed to 4 decimal place is {secant(0.5*R, 1.1*R, e, f)}") 

# Output

"""
The distance of L_1 from Earth computed to 4 decimal place is 328164147.64873964
"""