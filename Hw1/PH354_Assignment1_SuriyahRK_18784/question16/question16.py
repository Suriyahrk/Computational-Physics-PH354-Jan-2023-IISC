import numpy as np
import sympy as smp
import matplotlib.pyplot as plt
import pandas as pd

r = np.arange(1,4,0.01)
n = len(r)
x = []

for i in np.arange(0,n):
    x.append(0.5)

x = np.array(x)

for j in np.arange(0,1000): # for stability
    x = r*x*(1-x)

for j in np.arange(0,1000): # storing values
    x = r*x*(1-x)
    plt.plot(r,x)

plt.xlabel("r")
plt.ylabel("rx(1-x) for 1000 iterations")
plt.title("Feigenbaum plot")
plt.show()
