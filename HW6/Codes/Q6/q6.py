import numpy as np
import sys
sys.path.insert(0,'.')
from Methods.Runge_katta_system import Runge_Katta_system
import matplotlib.pyplot as plt


G = 1
M = 10
L = 2

t_ini = 0
t_final = 10
n_sys = 4
h = 0.01
Initial_conditions = [1, 0, 0, 1]

def f1(x, Y):
    return Y[1]

def f2(x, Y):
    return -G*M*Y[0] /( (Y[0]**2 + Y[2]**2) * ( np.sqrt(Y[0]**2 + Y[2]**2 + L**2/ 4 )) )

def f3(x, Y):
    return Y[3]

def f4(x, Y):
    return -G*M*Y[2] /( (Y[0]**2 + Y[2]**2) * ( np.sqrt(Y[0]**2 + Y[2]**2 + L**2/ 4 )) )

System_ODE = [f1, f2, f3, f4]

X, Y = Runge_Katta_system(t_ini, t_final, h, n_sys, System_ODE, Initial_conditions )

plt.plot(Y[:, 0], Y[:, 2])
plt.xlabel(" X coordinate")
plt.ylabel("Y coordinate")
plt.title(" Orbit of ball bearing")
# plt.savefig("Q6.png")
plt.show()

"""
We notice is the orbit is periodic but precises which can be explained by the fact of field not being 1/r^2, or The Runge-lenz vector
not beinf conserved along with the angular momentum.

"""