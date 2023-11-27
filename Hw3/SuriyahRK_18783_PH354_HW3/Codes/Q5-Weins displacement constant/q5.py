import numpy as np
import sympy as smp
import matplotlib.pyplot as plt
import scipy.constants as sc
import sys
sys.path.insert(0,'.')
from Root_finding import *

# Part  - a 

x = smp.symbols("x")
h = sc.h
k_b = sc.k
c = sc.c
T = 1 # for convenience we pick T to be 1

I = x**(-5) / (smp.exp(h*c/(x*k_b*T)) - 1) 

"""
 We can neglect the constants multiplied in the front as they dont dont contribute when we equate the derivative to zero
"""

dI = smp.diff(I ,x)  # differentiating the expression using sympy

f = smp.lambdify(x, dI) # Making it a numpy function

Root = bisect(10**-2, 10**-3, 10**(-6), f)

print(f" The value of Wein's constant is {Root} ")

# output
"""
The value of Wein's constant is 0.00289788818359375 
"""

# Part  - b

l = 502 * 10 ** (-9)
print(f" The value of surface temperature of sun is {Root / l} in Kelvin ")

# output
"""
The value of surface temperature of sun is 5772.685624688745 in Kelvin
"""