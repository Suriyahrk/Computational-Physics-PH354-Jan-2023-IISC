import numpy as np
import sys
sys.path.insert(0,'.')
from Methods.Runge_katta_system import Runge_Katta_system
import matplotlib.pyplot as plt

# Part - a - Simple harmonic Oscillator

t_ini = 0
t_final = 50
h = 0.001
Initial_conditions = [1, 0]
n_sys = 2
omega  = 1
Initial_conditions = [1, 0]

"""
We will rewrite the second order ODE as two first order ODE by considering the derivative of x to be a new variable 
"""
def f1(x, Y):
    return Y[1]

def f2(X, Y):
    return -omega**2 * Y[0]

System_ODE = [f1, f2]
X, Y  = Runge_Katta_system(t_ini, t_final, h, n_sys, System_ODE, Initial_conditions )

plt.plot(X, Y[:,0])
plt.xlabel("Time")
plt.ylabel(" Displacement ")
plt.title(" Simple Harmonic Oscillator")
# plt.savefig("Q4-part-a.png")
plt.show()

# Part - b

Initial_conditions1 = [2, 0]
X1, Y1  = Runge_Katta_system(t_ini, t_final, h, n_sys, System_ODE, Initial_conditions1 )

plt.plot(X, Y[:,0])
plt.plot(X1, Y1[:,0])
plt.xlabel("Time")
plt.ylabel(" Displacement ")
plt.title(" Simple Harmonic Oscillator")
plt.legend(["A = 1", "A = 2"])
# plt.savefig("Q4-part-b.png")
plt.show()

"""
We can see when we increase the amplitude the frequency remains the same
"""

# part - c

# Anharmonic Oscillator

def f1(x, Y):
    return Y[1]

def f2(X, Y):
    return -omega**2 * Y[0]**3

System_ODE = [f1, f2]
X3, Y3  = Runge_Katta_system(t_ini, t_final, h, n_sys, System_ODE, Initial_conditions )

plt.plot(X, Y[:,0])
plt.plot(X3, Y3[:,0])
plt.xlabel("Time")
plt.ylabel(" Displacement ")
plt.title(" Anharmonic Harmonic Oscillator")
plt.legend(["Harmonic Oscillator", "Anharmonic Oscillator"])
# plt.savefig("Q4-part-c.png")
plt.show()

# Higher/ Lower amplitudes

Initial_conditions2 = [0.5, 0]


X4, Y4  = Runge_Katta_system(t_ini, t_final, h, n_sys, System_ODE, Initial_conditions1 )
X5, Y5  = Runge_Katta_system(t_ini, t_final, h, n_sys, System_ODE, Initial_conditions2 )

plt.plot(X3, Y3[:,0])
plt.plot(X4, Y4[:,0])
plt.plot(X5, Y5[:,0])
plt.xlabel("Time")
plt.ylabel(" Displacement ")
plt.title(" Anharmonic Harmonic Oscillator")
plt.legend(["A = 1", "A = 2", "A = 0.5"])
# plt.savefig("Q4-part-c_Changes_amplitudes.png")
plt.show()

"""
We can see the frequency is higher for higher amplitudes in case of harmonic oscillator
"""

# part - d

plt.plot(Y[:,0], Y[:,1])
plt.plot(Y3[:,0], Y3[:,1])
plt.ylabel("Velocity")
plt.xlabel(" Displacement ")
plt.title(" Phase Space Diagram")
plt.legend(["Simple Harmonic Oscillator", "Anharmonic Oscillator"])
# plt.savefig("Q4-part-d.png")
plt.show()

# part - e
# Vander - pol - Oscillator
"""
d2x/dt2 - mu*(1 -x**2)* dx/ dt + omega**2 * x = 0 

"""
# defining the dynamical variable 

mu = [1, 2, 4]
h = 0.001
t_final = 20

for i in range(0, 3):

    def f1(x, Y):
        return Y[1]

    def f2(X, Y):
        return mu[i]*(1 - Y[0]**2)*Y[1]  - omega**2 * Y[0]

    System_ODE = [f1, f2]

    X_v, Y_v  = Runge_Katta_system(t_ini, t_final, h, n_sys, System_ODE, Initial_conditions)

    plt.plot(Y_v[:,0], Y_v[:,1])


plt.ylabel("Velocity")
plt.xlabel(" Displacement ")
plt.title(" Phase Space Diagram")
plt.legend(["mu = 1", "mu = 2", "mu = 0.5"])
# plt.savefig("Q4-part-e.png")
plt.show()

