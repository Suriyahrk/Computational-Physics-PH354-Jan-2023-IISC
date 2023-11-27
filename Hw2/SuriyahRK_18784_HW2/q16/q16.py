import numpy as np
import sympy as smp
import matplotlib.pyplot as plt
import pandas as pd
import cmath as cm
import sys
sys.path.insert(0,'.')
from Integration_techniques import *
import scipy.constants as sc


# part - a

"""
Considering you get maxmimum transmission when you are directly infront of a slit, the ditance between two slits noting but the period of 
sin^2(x) which is pi/2.
a*d  = pi
a = pi/d

"""


# part - b
def q(u):
    d = 20*10**(-6)
    a = np.pi/d
    return  (np.sin(a*u))**2

def I(x):
    l = 500*10**(-9)
    f = 1
    def Integrand(u):
        return  np.sqrt(q(u))*np.exp(1j*2*np.pi*x*u/(l*f))
    
    return (abs(GQ(-90*10**(-6),90*10**(-6),Integrand,100)))**2

# there are 10 slits so 9 seperations each of length 20 um so the total width of grating is 180 um
L = 0.1
X = np.linspace(-L/2,L/2,10000)
Y = np.linspace(1,20,20)
I_ = I(X)


"""
        In evaluating the integral we have used Gaussian quadrature as its highly efficient and using N = 100 ensures we get a 
        an output of high degree of accuracy to actual value cause, gaussian quadrature will evaluate the integral exatly till x**99 
        in the taylor series expansion of integrand which is a very good approximation for a convergent series.
        
"""
# part - c

plt.plot(X,I_)
plt.xlabel("x-Coordinate(in m)")
plt.ylabel("Intensity")
plt.title("Intensity as a function of distance from central axis")
 # plt.savefig("q16-part-c.png")
plt.show()

# part - d

A = np.zeros([20,10000])

for i in np.arange(0,20):   
    A[i] = I_

plt.pcolormesh(X,Y,A,vmax = 12e-10)
plt.colorbar()
 # plt.savefig("q16-part-d-density plot.png")
plt.show()

# part-e-(i)

def q1(u):
    d = 20*10**(-6)
    a = np.pi/d
    return  ((np.sin(a*u))**2)*((np.sin((a/2)*u))**2)    

def I1(x):
    l = 500*10**(-9)
    f = 1
    def Integrand1(u):
        return  np.sqrt(q1(u))*np.exp(1j*2*np.pi*x*u/(l*f))
    
    return (abs(GQ(-90*10**(-6),90*10**(-6),Integrand1,100)))**2


I1_ = I1(X)
# there are 10 slits so 9 seperations each of length 20 um so the total width of grating is 180 um

plt.plot(X,I1_)
plt.xlabel("x-Coordinate(in m)")
plt.ylabel("Intensity")
plt.title("Intensity as a function of distance from central axis")
# plt.savefig("q16-part-e-i-Intensity_plot.png")
plt.show()

A1 = np.zeros([20,10000])

for i in np.arange(0,20):   
    A1[i] = I1_

plt.pcolormesh(X,Y,A1,vmax = 12e-10)
plt.colorbar()
 #plt.savefig("q16-part-e-i-density_plot.png")
plt.show()


# part-e-(ii)

def q2(u):
    if (0 <= u <= 30*10**(-6)) or (- 30*10**(-6) <= u  <= 0) or (40*10**(-6) <= u <= 90*10**(-6)) or (-90*10**(-6) <= u <= -50*10**(-6)) :
        return 0
    else:
        return 1

def I2(x):
    l = 500*10**(-9)
    f = 1
    def Integrand2(u):
        return  np.sqrt(q2(u))*np.exp(1j*2*np.pi*x*u/(l*f))
    
    return (abs(GQ(-90*10**(-6),90*10**(-6),Integrand2,100)))**2


I2_ = I2(X)
# there are 10 slits so 9 seperations each of length 20 um so the total width of grating is 180 um

plt.plot(X,I2_)
plt.xlabel("x-Coordinate(in m)")
plt.ylabel("Intensity")
plt.title("Intensity as a function of distance from central axis")
# plt.savefig("q16-part-e-ii-Intensity_plot.png")
plt.show()

A2 = np.zeros([20,10000])

for i in np.arange(0,20):   
    A2[i] = I2_

plt.pcolormesh(X,Y,A2)
plt.colorbar()
 # plt.savefig("q16-part-e-ii-density_plot.png")
plt.show()


