

import numpy as np
import sympy as smp
import matplotlib.pyplot as plt
import pandas as pd
import cmath as cm
import sys
sys.path.insert(0,'.')
from Integration_techniques import *
import scipy.constants as sc

# part - c

q_0 = 100
L = 0.1

def sigma(x,y):

    return q_0*(np.sin(2*np.pi*x)/L)*(np.sin(2*np.pi*y)/L)

def V_xy(x,y):

    def f(xprime):

        def g(yprime):
             return sigma(xprime,yprime)/(np.sqrt( (x - xprime )**2 + (y - yprime)**2 ))
        
        return GQ(-L/2,L/2,g,2)
    
    return GQ(-L/2,L/2,f,2)

n = 100
x = np.linspace(-0.5,0.5,n+1)
y = np.linspace(-0.5,0.5,n+1)
X,Y = np.meshgrid(x,y)  

V = np.zeros([n+1,n+1])

for i in np.arange(0,n+1):
    for j in np.arange(0,n+1):

        x1 = 0.5*(1*i - (n-i)*(1))/n
        y1 = 0.5*(1*j - (n-j)*(1))/n

        if (x1 == 0.05 and y1 == 0) or (x1 == -0.05 and y1 == 0) :
            V[j][i] = 0 
        else:
            V[j][i] = V_xy(x1,y1)

plt.pcolormesh(X,Y,V,vmax = 1, vmin = -1)
plt.colorbar()
plt.title("Potential as a function of (x,y)")
# plt.savefig("q17part-c-Potential.png")
plt.show()

h = 1/n

E_x = np.zeros([n+1,n+1])

for i in np.arange(0,n+1):
    for j in np.arange(0,n+1):
        if j == n :
            E_x[i][j] = (V[i][j] - V[i][j-2])/(2*h)
        elif j == 0 :
            E_x[i][j] = (V[i][j+2] - V[i][j])/(2*h)
        else: 
            E_x[i][j] = (V[i][j+1] - V[i][j-1])/(2*h)

E_y = np.zeros([n+1,n+1])

for i in np.arange(0,n+1):
    for j in np.arange(0,n+1):
        if i == n :
            E_y[i][j] = (V[i][j] - V[i-2][j])/(2*h)
        elif i == 0 :
            E_y[i][j] = (V[i+2][j] - V[i][j])/(2*h)   
        else:
            E_y[i][j] = (V[i+1][j] - V[i-1][j])/(2*h)

Mag = np.zeros([n+1,n+1])

for i in np.arange(0,n+1):
    for j in np.arange(0,n+1):
        Mag[i][j] = np.sqrt(E_x[i][j]**2 + E_y[i][j]**2)

Max_value = Mag.max()   # normalizing matrix value

plt.pcolormesh(X,Y,Mag/Max_value,vmax = 0.07,cmap = 'jet') 
plt.colorbar()
plt.title("Magnitude of Electric field as a function of (x,y)")
# plt.savefig("q17part-c-magnitude.png")
plt.show()         

Dir = np.zeros([n+1,n+1])

for i in np.arange(0,n+1):
    for j in np.arange(0,n+1):
        Dir[i][j] = np.arctan2(E_y[i][j],-E_x[i][j])
 
plt.pcolormesh(X,Y,Dir,cmap='hsv')
plt.colorbar()
plt.title("Direction of Electric field as a function of (x,y)")
 # plt.savefig("q17-part-c-Direction.png")
plt.show()         

# vector field plot

plt.streamplot(X,Y,-E_x,-E_y, density=1 , linewidth=None, color='blue')
 # plt.savefig("vector_field_for_charge_plate.png")
plt.show()