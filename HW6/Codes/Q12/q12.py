import numpy as np
import matplotlib.pyplot as plt
import sys
sys.path.insert(0, '.')
from Methods.Adaptive_Runge_katta import Adaptive_Runge_katta

G = 1
t_ini = 0
t_final = 3
h_ini = 0.001
delta = 10**(-3)
m1 = 150
m2 = 200
m3 = 250
n_sys = 12
"""
We will take x1 = Y[0], y1 = Y[1], x2 = Y[2], y2 = Y[3], x3 = Y[4], y3 = Y[5]
for first derivatives x1dot = Y[6], y1dot = Y[7], x2dot = Y[8], y2dot = Y[9], x3dot = Y[10], y3dot = Y[11]

"""
Initial_conditions = np.array([3, 1, -1, -2, -1, 1, 0, 0, 0, 0, 0, 0])

# Defining the functions

def f1(x, Y):
    return Y[6]

def f2(x, Y):
    return Y[7]

def f3(x, Y):
    return Y[8]

def f4(x, Y):
    return Y[9]

def f5(x, Y):
    return Y[10]

def f6(x, Y):
    return Y[11]

def f7(x, Y):
    r1 = np.sqrt( (Y[2] - Y[0])**2 + (Y[3] - Y[1])**2 )
    r2 = np.sqrt( (Y[4] - Y[0])**2 + (Y[5] - Y[1])**2 )
    return G* m2* (Y[2] - Y[0])/(r1)**3 + G* m3* (Y[4] - Y[0])/(r2)**3

def f8(x, Y):
    r1 = np.sqrt( (Y[2] - Y[0])**2 + (Y[3] - Y[1])**2 )
    r2 = np.sqrt( (Y[4] - Y[0])**2 + (Y[5] - Y[1])**2 )
    return G* m2* (Y[3] - Y[1])/(r1)**3 + G* m3* (Y[5] - Y[1])/(r2)**3

def f9(x, Y):
    r1 = np.sqrt( (Y[2] - Y[0])**2 + (Y[3] - Y[1])**2 )
    r2 = np.sqrt( (Y[4] - Y[2])**2 + (Y[5] - Y[3])**2 )
    return G* m1* (Y[0] - Y[2])/(r1)**3 + G* m3* (Y[4] - Y[2])/(r2)**3

def f10(x, Y):
    r1 = np.sqrt( (Y[2] - Y[0])**2 + (Y[3] - Y[1])**2 )
    r2 = np.sqrt( (Y[4] - Y[2])**2 + (Y[5] - Y[3])**2 )
    return G* m1* (Y[1] - Y[3])/(r1)**3 + G* m3* (Y[5] - Y[3])/(r2)**3

def f11(x, Y):
    r1 = np.sqrt( (Y[4] - Y[0])**2 + (Y[5] - Y[1])**2 )
    r2 = np.sqrt( (Y[4] - Y[2])**2 + (Y[5] - Y[3])**2 )
    return G* m1* (Y[0] - Y[4])/(r1)**3 + G* m2* (Y[2] - Y[4])/(r2)**3

def f12(x, Y):
    r1 = np.sqrt( (Y[4] - Y[0])**2 + (Y[5] - Y[1])**2 )
    r2 = np.sqrt( (Y[4] - Y[2])**2 + (Y[5] - Y[3])**2 )
    return G* m1* (Y[1] - Y[5])/(r1)**3 + G* m2* (Y[3] - Y[5])/(r2)**3

System_ODE = [f1, f2, f3, f4, f5, f6 ,f7, f8, f9, f10, f11, f12]

x, Y, H = Adaptive_Runge_katta(t_ini, t_final, h_ini, n_sys,System_ODE, Initial_conditions, delta)

Y = np.array(Y)

plt.plot(Y[:, 0], Y[:, 1])
plt.plot(Y[:, 2], Y[:, 3])
plt.plot(Y[:, 4], Y[:, 5])
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Three body problem")
# plt.savefig("Q12-part-b.png")
plt.show()


