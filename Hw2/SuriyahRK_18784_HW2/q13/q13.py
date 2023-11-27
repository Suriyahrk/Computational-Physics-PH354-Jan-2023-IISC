import numpy as np
import sympy as smp
import matplotlib.pyplot as plt
import pandas as pd
import sys
sys.path.insert(0,'.')
from Integration_techniques import *
import scipy.constants as sc
from math import factorial

# part - a

def H(n,x):
    if n == 0:
        return 1
    elif n == 1:
        return 2*x
    
    else:
        temp0 = 1
        temp1 = 2*x

        for i in np.arange(2,n+1):
            final = 2*x*temp1 - 2*(i-1)*temp0
            temp0 = temp1
            temp1 = final

        return final 


def psi(n,x):
    C = 1/(np.sqrt( (2**n) *factorial(n)* np.sqrt(np.pi)))
    
    return C*np.exp(-x**2/2)*H(n,x)

N = 1000
X = np.linspace(-4,4,N+1)

H_0 = []
H_1 = []
H_2 = []
H_3 = []

for i in np.arange(0,N+1):
    H_0.append(psi(0,(4*i - (N-i)*4)/N))

for i in np.arange(0,N+1):
    H_1.append(psi(1,(4*i - (N-i)*4)/N))

for i in np.arange(0,N+1):
    H_2.append(psi(2,(4*i - (N-i)*4)/N))

for i in np.arange(0,N+1):
    H_3.append(psi(3,(4*i - (N-i)*4)/N))


plt.plot(X,H_0)
plt.plot(X,H_1)
plt.plot(X,H_2)
plt.plot(X,H_3)
plt.xlabel("x-Coordinate")
plt.ylabel("Wave function (psi)")
plt.title("First 4 wavefunctions od Harmonic oscillator")
plt.legend(["n = 0","n = 1","n = 2","n = 3"])
plt.grid()
#plt.savefig("q13-part-a.png")
plt.show()

# part - b 

X_l = np.linspace(-10,10,N+1)

H_30 = []

for i in np.arange(0,N+1):
    H_30.append(psi(30,(10*i - (N-i)*10)/N))

plt.plot(X,H_30)
plt.xlabel("x-Coordinate")
plt.ylabel("Wave function (psi)")
plt.title("n = 30 wave function of harmonic oscillator")
plt.grid()
#plt.savefig("q13-part-b.png")
plt.show()

# part - c

def rmsp(n): # root mean square position

    def f(x):
        return (x**2)*(psi(n,x)**2)      

    return np.sqrt(GQ(-5,5,f,100))  

print(f"The uncertainity in the wave function n = {5} is {rmsp(5)} m")

# The are taken fromo -5 to 5 instead of -Infinity to Infinity as the function reaches zero very quickly so higher imits are not needed,
# infact higher limits will give a worser estimate due to underflow as the e^(-x**2) will reach extremely low values causing the 
# float variable to behave randomly.
    
# output

"""
The uncertainity in the wave function n = 5 is 2.3451896081212955 m

"""