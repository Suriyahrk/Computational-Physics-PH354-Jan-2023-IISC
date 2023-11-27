import numpy as np
import sympy as smp
import matplotlib.pyplot as plt
import pandas as pd
import sys
sys.path.insert(0,'.')
from Integration_techniques import *
import scipy.constants as sc

# part - a

def I(a,x):
    return (x**(a-1))*(np.exp(-x))

X = np.linspace(0,5,101)

I_2 = []
I_3 = []
I_4 = []


for i in np.arange(0,101):
    I_2.append(I(2,i/20))

for i in np.arange(0,101):
    I_3.append(I(3,i/20))

for i in np.arange(0,101):
    I_4.append(I(4,i/20))

plt.plot(X,I_2)
plt.plot(X,I_3)
plt.plot(X,I_4)
plt.xlabel("x-Coordinate")
plt.ylabel("Integrand")
plt.title("Integrand as a function of x for differnet values of a")
plt.legend(["a = 2","a = 3","a = 4"])
 # plt.savefig("q15-part-a.png")
plt.show()

# part - e

def gamma(a):

    def f(z):
        t = (a-1)*z/(1-z)
        return (np.exp((a-1)*np.log(t) - t))*((a-1)*(1)/(1-z)**2)

    return GQ(0,1,f,100)

print(f"The value of gamma(3/2) is {gamma(3/2)} with error from actual value of pi^(1/2)/2 is {(gamma(3/2 )- np.pi**(1/2)/2)/(np.pi**(1/2)/2)}")


# output 

"""
The value of gamma(3/2) is 0.8862269613087213 with error from actual value of pi^(1/2)/2 is 4.0459122014662456e-08

"""
# part  - f 

print(f" gamma(3) = {gamma(3)}")
print(f" gamma(6) = {gamma(6)}")
print(f" gamma(10) = {gamma(10)}")

# output

"""
gamma(3) = 2.0000000000000013
gamma(6) = 119.99999999999999
gamma(10) = 362879.99999999994

"""
