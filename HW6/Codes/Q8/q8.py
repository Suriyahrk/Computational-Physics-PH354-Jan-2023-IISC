import numpy as np
import sys
sys.path.insert(0,'.')
import matplotlib.pyplot as plt
import scipy.constants as sc
from Methods.Runge_katta_system import Runge_Katta_system
from Methods.Adaptive_Runge_katta import Adaptive_Runge_katta

G = sc.G
M = 1.98 * 10**30 # (in Kg)

t_ini = 0
t_final = 100* 365* 24* 60 * 60 
h = 10**(-3) * 365* 24* 60 * 60 
delta = 1000 / (365* 24* 60 * 60 )
n_sys = 4

Initial_conditions = [4* 10**(12), 0, 0, 500]

def f1(x, Y):
    return Y[1]

def f2(x, Y):
    return - G*M* Y[0] / ( (Y[0]**2 + Y[2]**2)**(3/2) )

def f3(x, Y):
    return Y[3]

def f4(x, Y):
    return - G*M* Y[2] / ( (Y[0]**2 + Y[2]**2)**(3/2) )

System_ODE = [f1, f2, f3, f4]

X, Y = Runge_Katta_system(t_ini, t_final, h, n_sys, System_ODE, Initial_conditions)

plt.plot(Y[:, 0], Y[:, 2])
plt.xlabel(" X - coordinate")
plt.ylabel(" Y - Coordinate")
plt.title("Trajectory of comet")
# plt.savefig("Q8-part-a_10^(-4)_years.png")
plt.show()

"""
Part - b
    Several values of h has been tried for the program, we can see in case of h = 0.001 years the trajectories over-lap more or less, but the 
    overlap is very evident in case of h = 0.0001 years, confirming better h values gives a better representation of the trajectories. 
    The program did take more time in case of h = 0.0001 years compared to the prior, but it wasnt that significant . Higher values of h like 0.1 
    years and 1 years were also tried but, those graphs were completely off, and didnt depict any periodic behaviour, it can also be seen that the 
    comet completes one revolution in about 50 years, we have used t_final  = 100 years to depict two complete revolutions.

"""

# Part - c

X1, Y1, H1 = Adaptive_Runge_katta(t_ini, t_final, h, n_sys, System_ODE, Initial_conditions, delta)

size = len(Y1)
x_coord = []
y_coord = []


for i in range(0, size):
    x_coord.append(Y1[i][0])
    y_coord.append(Y1[i][2])


plt.plot(x_coord, y_coord)
plt.xlabel(" X - coordinate")
plt.ylabel(" Y - Coordinate")
plt.title("Adaptive Runge katta")
# plt.savefig("Q8-part-c.png")
plt.show()

"""
The graph obtained through adaptive runge-katta is much faster than obtained through fixed step size runge katta which can be noticed 
if the Q8.py file in run, thus showcasing us the advantage of Adaptive-step size method and also the trajectory obtained is highly accurate,
thus also making the method just faster but more accurate the fixed step size. we can see how the step size changes and the plot for part-d
of the question where more points are sampled when the comet is fast moving near the sun compared to further away from the sun. 
"""

# part - d

plt.plot(x_coord, y_coord, 'o', markersize = 0.9, color = 'red')
plt.xlabel(" X - coordinate")
plt.ylabel(" Y - Coordinate")
plt.title("Adaptive Runge katta scatter plot")
# plt.savefig("Q8-part-d.png")
plt.show()

""" 
We can see the points spread when the comet is away from origin, but highly dense near the origin
"""



