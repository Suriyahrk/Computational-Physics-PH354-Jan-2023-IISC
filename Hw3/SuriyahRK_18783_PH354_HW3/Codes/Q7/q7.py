import numpy as np
import sympy as smp
import matplotlib.pyplot as plt
import scipy.constants as sc
import sys
sys.path.insert(0,'.')
from Root_finding import *

# Part - a

x = smp.symbols('x')

f = 924*x**6 - 2772*x**5 + 3150*x**4 - 1680*x**3 + 420*x**2 - 42*x + 1 

df = smp.diff(f,x)

func = smp.lambdify(x,f)
dfunc = smp.lambdify(x,df)

X = np.linspace(0,1,101)
Y = func(X)

plt.plot(X,Y)
plt.xlabel("x")
plt.ylabel("P(x)")
plt.title("GIven polynomial between 0 and 1")
plt.grid()
 # plt.savefig("q7_part-a.png")
plt.show()

"""
From the graph we can guess the approximate roots.The guess are 

"""
x1 = 0.04
x2 = 0.177
x3 = 0.374
x4 = 0.608
x5 = 0.839
x6 = 0.967


# part - b

""""
Now using newtons method, with epsilon  = 0.5*10**(-9) for 10 decimal places

"""
e = 0.5*10**(-9)

print(f" The 1st root using newtons method is {newton(x1,e,func,dfunc)}  ")
print(f" The 2nd root using newtons method is {newton(x2,e,func,dfunc)}  ")
print(f" The 3rd root using newtons method is {newton(x3,e,func,dfunc)}  ")
print(f" The 4th root using newtons method is {newton(x4,e,func,dfunc)}  ")
print(f" The 5th root using newtons method is {newton(x5,e,func,dfunc)}  ")
print(f" The 6th root using newtons method is {newton(x6,e,func,dfunc)}  ")

# Output

"""
 The 1st root using newtons method is 0.03376524289842399  
 The 2nd root using newtons method is 0.16939530676685538  
 The 3rd root using newtons method is 0.3806904069417079  
 The 4th root using newtons method is 0.6193095930415993  
 The 5th root using newtons method is 0.8306046932331124  
 The 6th root using newtons method is 0.9662347571015834  

"""