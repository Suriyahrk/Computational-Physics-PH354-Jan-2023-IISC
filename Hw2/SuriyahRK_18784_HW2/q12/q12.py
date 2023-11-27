import numpy as np
import sympy as smp
import matplotlib.pyplot as plt
import pandas as pd
import sys
sys.path.insert(0,'.')
from Integration_techniques import *
import scipy.constants as sc

# part - b and c

# we will using gaussian quadrature as its highly accurate and converges resonably quick it also requires considerably less number of 
# iteration then other methods to reach the same level of accuracy. We will take N = 100

N = 100

def f(x):
    return  x**3/(np.exp(x)-1)

I = GQ(0,200,f,100)

# Note the upperlimit is cannot be set to infinity, and as the Integrand goes to zero relatively quickly any number greater than 100 wou
# be a good approximate. We are using 200 as the upper limit

print(f"The value of the integral calculated from GQ is {I} and throught analytical method is {np.pi**4/15}")

# The value of the integral calculated from GQ is 6.493939402266824 and throught analytical method is 6.493939402266828


k_b = sc.k
c = sc.c
hbar = sc.hbar

sigma_computed = ((k_b)**4)*I/(4*(np.pi**2)*(c**2)*(hbar**3))

print(f"The computed value of Stephan's constant from the integral is {sigma_computed} and literature value is {sc.sigma} with error percentage of {(sigma_computed- sc.sigma)*100/sc.sigma} %")

# Output

"""
The computed value of Stephan's constant from the integral is 5.6703744191844255e-08 and literature value is 5.670374419e-08 with 
 error percentage of 3.2524402935174654e-09 %
 """
