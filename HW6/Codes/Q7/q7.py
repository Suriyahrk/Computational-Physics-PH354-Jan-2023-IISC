import numpy as np
import sys
sys.path.insert(0,'.')
from Methods.Runge_katta_system import Runge_Katta_system
import matplotlib.pyplot as plt


k = 6
m = 1
omega = 2

"""
We denote the t = x, Xi_n = y_(2n- 2) and dXi_n / dt = y_(2n-1)
"""

# Defining the 2n first order differential equations
System_ODE = []
N_osc = 5

# Creating the starting boundry function and appending it to the array of function
def f_ini(x, Y):
    return Y[1]

def g_ini(x, Y):
    return k*(Y[2] - Y[0])/ m  + np.cos(omega* x) / m

System_ODE.append(f_ini)
System_ODE.append(g_ini)

# Creating a function that will give the two first order ODE for the i th mass
def ODE_at_i(i):
    
    def f(x, Y):
        return Y[2*i - 1]

    def g(x, Y):
        return k*( Y[2*i] - 2* Y[2*i - 2] +  Y[2*i - 4] ) / m

    return f, g 

# Appending it to the array of functions
for i in range(2, N_osc):

    fprime, gprime = ODE_at_i(i)

    System_ODE.append(fprime)
    System_ODE.append(gprime)


# Adding the boundry functions
def f_2n_minus_2(x, Y):
    return Y[2*N_osc - 1]

def f_2n_minus_1(x, Y):
    return k* ( Y[2*N_osc - 4] - Y[2*N_osc - 2] ) / m

System_ODE.append(f_2n_minus_2)
System_ODE.append(f_2n_minus_1)

Initial_Conditions = []

for i in range(0, 2* N_osc):
    Initial_Conditions.append(0)

t_ini = 0
t_final = 20
h = 0.01
n_sys = 2* N_osc

X, Y = Runge_Katta_system(t_ini, t_final, h, n_sys, System_ODE, Initial_Conditions)

for i in range(0, N_osc):
    plt.plot(X, Y[:, 2*i])

plt.xlabel("Time")
plt.ylabel("Displacement")
plt.title("Displacement of the coupled oscillators")
plt.legend(["i = 1", "i = 2", "i = 3", "i = 4", "i = 5"])
# plt.savefig("Q7.png")
plt.show()


    



