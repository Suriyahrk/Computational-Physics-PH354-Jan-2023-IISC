import numpy as np
import sys
sys.path.insert(0,'.')
from Methods.Runge_katta_system import Runge_Katta_system
import matplotlib.pyplot as plt

# Defining our dynamical variable

sigma = 10
r = 28
b = 8/3
t_ini = 0
t_final = 50
h = 0.001
Initial_conditions = [0, 1, 0]
n_sys = 3

"""
Note here: Y[0] = x,  Y[1] = y,  Y[2] = z
"""

def f1(x, Y):
    return sigma* (Y[1] - Y[0] )

def f2(x, Y):
    return r* Y[0] - Y[1] - Y[0]* Y[2]

def f3(x, Y):
    return Y[0]* Y[1] - b* Y[2]

System_ODE = [f1, f2, f3]

X, Y = Runge_Katta_system(t_ini, t_final, h, n_sys, System_ODE, Initial_conditions )


plt.plot(X, Y[:, 1])
plt.xlabel("time")
plt.ylabel("y")
plt.title("Y as function of time")
# plt.savefig("Q3-part-a.png")
plt.show()

# Part b 

plt.plot(Y[:, 0], Y[:, 2])
plt.xlabel("x")
plt.ylabel("z")
plt.title("z as function of x")
# plt.savefig("Q3-part-b.png")
plt.show()