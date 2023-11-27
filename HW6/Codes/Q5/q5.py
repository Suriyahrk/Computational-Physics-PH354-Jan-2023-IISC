import numpy as np
import sys
sys.path.insert(0,'.')
from Methods.Runge_katta_system import Runge_Katta_system
import matplotlib.pyplot as plt

R = 8 * 10**(-2)
pi = np.pi
rho = 1.22
C = 0.47
m = 1
g = 9.8
h = 0.01
t_ini = 0
t_final = 9
n_sys = 4

"""
Note : The variables we will be using are x = y0, dx/dt = y1, y = y2, dy/dt = y3

The canon ball is shot at an angle of 30 degrees at 100 kms per second and initial assumed to be at the ground.

"""
Initial_conditions = [0, 50* np.sqrt(3) , 0, 50]

for m in range(1, 5):

    k = (pi * R **2 * C *rho ) / (2*m)

    def f1(x, Y):
        return Y[1]

    def f2(x, Y):
        return -k* Y[1]* np.sqrt(Y[1]**2 + Y[3]**2) 

    def f3(x, Y):
        return Y[3]

    def f4(x, Y):
        return -g -k* Y[3]* np.sqrt(Y[1]**2 + Y[3]**2) 

    System_ODE = [f1, f2, f3, f4]

    X, Y = Runge_Katta_system(t_ini, t_final, h, 4, System_ODE, Initial_conditions )

    x_t = []
    y_t = []
    N = X.shape[0]
    value = 0


    for i in range(0, N):
        if Y[i][2] < 0 :    
            value += 1
        
        if value == 1:
            break

        x_t.append(Y[i][0])
        y_t.append(Y[i][2])


    plt.plot(x_t, y_t)

plt.xlabel("X - axis (in m)")
plt.ylabel("Y - axis (in m)")
plt.title(" Trajectory of canonball")
plt.legend(["m = 1"," m = 2"," m = 3","m = 4" ])
# plt.savefig("Q5-part-c.png")
plt.show()

"""
Part - c
The decrease in distance travelled with an increase in mass can be attributed to the fact that the drag force acting on the object does
not depend on the mass of the object but only on its velocity. While increasing the mass does not affect the gravitational acceleration,
the acceleration due to air drag is reduced. This causes the more massive object to lose velocity at a slower rate and therefore travel a
longer distance. This trend is evident from the graph.
"""