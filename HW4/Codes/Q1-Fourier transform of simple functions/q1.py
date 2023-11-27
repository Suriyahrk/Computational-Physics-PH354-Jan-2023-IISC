import numpy as np
import matplotlib.pyplot as plt
import sys
sys.path.insert(0,'.')
from Modules.DFT import DFT


"""
The function DFT outputs a function which gives the discrete fourier transform for given value of k
and can be found in Modules -> DFT.py 
"""

# Part - a

"""
We will take N = 1000 for the square wave case, and for n = 0 to 500 the function is 1, and for the rest its 0. 
"""
N = 1000

def ya(n):
    if n <= 500 and n >= 0:
        return 1
    else:
        return 0
    

c_ka = DFT(ya, N)

K = np.linspace(0,100,101) # Only first few values of k are used in the plot as the function has a high peak at k = 0
C_ka = c_ka(K)
C_ka = C_ka / max(C_ka) # Normalizing the values


plt.plot(K, abs(C_ka))   # we are taking the absolute value of amplitude squared for given K 
plt.xlabel(" wavenumber(K) ")
plt.ylabel(" Amplitude ")
plt.title("Discrete fourier transform of square wave")
# plt.savefig("Q1-part-a.png")
plt.grid()
plt.show()


# Part - b

def yb(n):
    return n

c_kb = DFT(yb, N)

C_kb = c_kb(K)
C_kb = C_kb / max(C_kb)

plt.plot(K, abs(C_kb))   # we are taking the absolute value of amplitude for given K squared
plt.xlabel(" wavenumber(K) ")
plt.ylabel(" Amplitude ")
plt.title("Discrete fourier transform of Sawtooth function")
# plt.savefig("Q1-part-b.png")
plt.grid()
plt.show()


# Part - c

def yc(n):
    return np.sin(np.pi* n/ N )* np.sin(20* np.pi* n/ N )

c_kc = DFT(yc, N)

C_kc = c_kc(K)
C_kc = C_kc / max(C_kc)

plt.plot(K, abs(C_kc)**2 )   # we are taking the absolute value of amplitude for given K squared
plt.xlabel(" wavenumber(K) ")
plt.ylabel(" Amplitude ")
plt.title("Discrete fourier transform of product of two sine functions")
# plt.savefig("Q1-part-c.png")
plt.grid()
plt.show()