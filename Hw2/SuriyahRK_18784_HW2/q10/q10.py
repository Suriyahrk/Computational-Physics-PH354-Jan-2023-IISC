import numpy as np
import sympy as smp
import matplotlib.pyplot as plt
import pandas as pd
import sys
sys.path.insert(0,'.')
from Integration_techniques import *

# part - a

def Timeperiod(a):

    def f(x):
        return 4/(np.sqrt(2*(a**4-x**4)))
    
    return -GQ(a,0,f,20)

# part - b

A = np.linspace(0,2,100)
T = []

for i in np.arange(0,100):
    T.append(Timeperiod(A[i]))

plt.plot(A,T)
plt.xlabel("Amplitude")
plt.ylabel("Timeperiod")
plt.title("TIme period as a function of amplitude")
# plt.savefig("q10-part-b")
plt.show()

# part - c 

# explanation

""" 
    At distance "a" we can see the force goes as a**3 but distance only goes as order a using , 1/2 a t^2  we rougly approximate
    the time would go as 1/a atleast upto first order, which is exactly what we observe in our graph. Thus for larger values of a 
    time period decrease, i.e. the particle gets faster

    As for diverging behaviour near near x = 0 the potenial behaves like a constant potential i.e. if no initial velocity is given 
    the time period is very high also reflected by 1/a behaviour near x = 0.

"""

