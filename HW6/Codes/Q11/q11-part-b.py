import numpy as np
import matplotlib.pyplot as plt
import sys
sys.path.insert(0, '.')
from Methods.Runge_katta_system import Runge_Katta_system
from Methods.Root_finding import secant
import scipy.constants as sc


# anharmonic oscillator
hbar = sc.h /(2* np.pi)
m = sc.electron_mass
V_0 = 50*sc.electron_volt
a  = 10**(-11) 

x_ini = -10*a
x_final = 10*a
h = 0.01* a
n_sys = 2
Initial_conditions = [0, 1]

# writing a function that will output the value of the wavefunction at the endpoint
def Allowed_energies(E):

    def f1(x, Y):
        return Y[1]

    def f2(x, Y):
        return -(E - V_0 *(x/a)**4)* Y[0]* 2*m/hbar**2 

    System_ODE = [f1, f2]

    x, Y = Runge_Katta_system(x_ini, x_final, h, n_sys, System_ODE, Initial_conditions )

    return Y[:, 0][-1]

# Using root finding to determine the value of E at which this function go zero which will represent an actual solution

E_ini = 100* sc.electron_volt
E_final = 200* sc.electron_volt

e = 0.1* sc.electron_volt

E_0 = secant(E_ini, E_final, e, Allowed_energies)
E_1 = secant(3* E_0 , 3.3* E_0  , e, Allowed_energies)
E_2 = secant(5* E_0, 5.5* E_0, e, Allowed_energies)

print(f"The ground state energy of The harmonic oscillator is {E_0 / sc.electron_volt} eV")
print(f"The first excited state energy of The harmonic oscillator is {E_1 / sc.electron_volt} eV")
print(f"The second excited state energy of The harmonic oscillator is {E_2 / sc.electron_volt} eV")

"""
Output:
The ground state energy of The harmonic oscillator is 205.30182919363594 eV
The first excited state energy of The harmonic oscillator is 735.6730598457116 eV
The second excited state energy of The harmonic oscillator is 1443.5337139574522 eV

"""


