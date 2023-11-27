import numpy as np
import sympy as smp
import matplotlib.pyplot as plt
import pandas as pd
import sys
sys.path.insert(0,'.')
from Integration_techniques import *

def Relative_Intensity(x,z):    

    u = x*np.sqrt(2/z)

    def c(t):
        return np.cos(np.pi*t**2/2) 
    
    def s(t):
        return np.sin(np.pi*t**2/2)

    C_u = GQ(0,u,c,50)
    S_u = GQ(0,u,s,50)


    return (1/8)*((2*C_u + 1)**2 + (2*S_u + 1)**2)

x = np.linspace(-5,5,100)

R = []

for i in np.arange(0,100):
    R.append(Relative_Intensity(x[i],3))

plt.plot(x,R)
plt.xlabel("x-Coordinate")
plt.ylabel("Relative intensity")
plt.title("Relative intensity as a function of x-coordinate")
# plt.savefig("q11.png")
plt.show()
