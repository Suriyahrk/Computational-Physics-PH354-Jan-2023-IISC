import numpy as np
import matplotlib.pyplot as plt
import sys
sys.path.insert(0, '.')
from Methods.leapfrog import leap_frog

t_ini = 0
t_final = 50
h = 0.001
n_sys = 2

"""
we will compute the value of x and dx/dt at the t = h/2 using euler method
x(h/2) = x(0) + (dx(0)/dt)*h/2 =>  x(h/2) = 1 
dx(h/2)/dt = dx(0)/dt + (d2x(0)/dt2)* h/2

Using the ODE, d2x(0)/dt2 = -6
=> dx(h/2)/dt = -6*h/2

"""

Initial_conditions = [1, 0]
Initial_conditions_half  = [1, -6*h/2]

def f1(x, Y):
    return Y[1]

def f2(x, Y):
    return Y[1]**2 - Y[0] -5

System_ODE = [f1, f2]

X, Y = leap_frog(t_ini, t_final, h, n_sys, System_ODE, Initial_conditions, Initial_conditions_half)

plt.plot(X, Y[:, 0])
plt.xlabel("time")
plt.ylabel("X-coordinate")
plt.title("Leap - frog method")
# plt.savefig("Q9.png")
plt.show()