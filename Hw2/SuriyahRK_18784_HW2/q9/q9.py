import numpy as np
import sympy as smp
import matplotlib.pyplot as plt
import pandas as pd
import sys
sys.path.insert(0,'.')
from Integration_techniques import GQ

# part - a 

def g(x) :
    return x**4*np.exp(x)/(np.exp(x)-1)**2

def Cv(T):
    V = 1000*10**(-6)
    rho = 6.022*10**(28)
    k_b = 1.380649*10**(-23)
    O_D= 428

    return (9*V*rho*k_b*(T/O_D)**3)*(GQ(0,O_D/T,g,50))

# part - b

T_ = np.linspace(5,500,100)
C_V = []

for i in np.arange(1,101):
    C_V.append(Cv(5*i))

plt.plot(T_,C_V)
plt.xlabel("Temperature(T)")
plt.ylabel("Heat capacity (CV)")
plt.title("Heat capacity as a function of temperature")
# plt.savefig("q9-part-b.png")
plt.show()