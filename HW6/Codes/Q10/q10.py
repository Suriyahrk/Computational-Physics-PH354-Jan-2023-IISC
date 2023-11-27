import numpy as np
import matplotlib.pyplot as plt
import sys
sys.path.insert(0, '.')
from Methods.verlet import verlet
import scipy.constants as sc


M = 1.98* 10**30
G = sc.G

t_ini = 0
t_final = 10 *365*24*60*60 # 10 years 
h = 1*60*60


def f(x, Y):
    return np.array([- G* M* Y[0] / ( Y[0]**2 + Y[1]**2)**(3/2), - G* M* Y[1] / ( Y[0]**2 + Y[1]**2)**(3/2)])


Initial_x = [1.4710* 10**(11), 0] # Assuming along x axis
Initial_v = [0, 3.028 * 10**4] # Along +y axis

X, Y, V, V_half = verlet(t_ini, t_final, h, f, Initial_x, Initial_v)

plt.plot(Y[:, 0], Y[:, 1],'.',  color = 'red')
plt.xlabel("X -coordinate")
plt.ylabel("Y - coordinate")
plt.title("Trajectory of Earth")
# plt.savefig("q10-part-a.png")
plt.show()

# Part - b

m = 5.9722* 10**24 
x = Y[:, 0]
y = Y[:, 1]
r = np.sqrt(x**2 + y**2)
v_x = V[:, 0]
v_y = V[:, 1]

Potenial = -G*m*M / r
Kinetic = m*(v_x**2 + v_y**2)/ 2
Total = Potenial + Kinetic

plt.plot(X, Potenial)
plt.plot(X, Kinetic)
plt.plot(X, Total)
plt.xlabel("time")
plt.ylabel("Energies")
plt.title("Energies as a function of time")
# plt.savefig("q10-part-b.png")
plt.show()

# part - c

plt.plot(X[1:], Total[1:])
plt.xlabel("time")
plt.ylabel("Total Energy")
plt.title("Total Energy as a function of time")
# plt.savefig("q10-part-c.png")
plt.show()


"""
We can see the energy oscillates a bit, but comes back to the original value after a full cycle. 
"""


