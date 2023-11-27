import numpy as np
import sympy as smp
import matplotlib.pyplot as plt

#   Part - b 

"""
We will try to solve the non-linear system of equation using fixed point method for the given expressions in Q4-part b

x = y(a + x**2) ; y = b/(a + x**2)

"""

a = 1
b = 2
N = 50

xi = 0
yi = 0

for i in np.arange(0,N):
    xd = xi
    yd = yi

    xi = yd*( a + xd**2)
    yi = b/(a + xd**2)

print(f"Computed roots are x = {xi} and y = {yi} \n Analytically determined roots x = {b} and  y = {b /(a + b**2)}")

# Output

"""
Computed roots are x = 39.29214832470747 and y = 0.020918090005889015 
Analytically determined roots x = 2 and  y = 0.4

We notice even after 50 iterations the roots dont converge, hence above set of expressions are not suitable for fixed point method
"""

# Part - C

"""
Using the expressions 

"""
def f(x,y):
    return np.sqrt(b/y - a)

def g(x,y):
    return x /(a + x**2)
xi = 1
yi = 1

N_ = 50
for k in np.arange(0,N_):
    xd = xi
    yd = yi
    xi = f(xd,yd)
    yi = g(xd,yd)

print(f"Computed roots are x = {xi} and y = {yi} \n Analytically determined roots x = {b} and  y = {b /(a + b**2)}")

# Output

"""
Computed roots are x = 1.9999999999846148 and y = 0.4000000000049233
Analytically determined roots x = 2 and  y = 0.4

The both agree to high order of accuracy
"""






