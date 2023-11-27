import numpy as np
import sympy as smp
import matplotlib.pyplot as plt
import pandas as pd
import cmath as cm
import sys
sys.path.insert(0,'.')
from Integration_techniques import *
import scipy.constants as sc

epsilon_0 = sc.epsilon_0
k = 1/(4*np.pi*epsilon_0)

def V_xy(x,y):
    return k*( 1/np.sqrt((x-0.05)**2 + (y)**2) - 1/np.sqrt((x+0.05)**2 + (y)**2) )

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



plt.pcolormesh(X,Y,V,vmax = k, vmin = -k)
plt.colorbar()
plt.title("Potential as a function of (x,y)")
 # plt.savefig("q17-Potential.png")
plt.show()

def E_x(x,y) :
    return k*( (x-0.05)/(((x-0.05)**2 + (y)**2)**(3/2)) - (x+0.05)/(((x+0.05)**2 + (y)**2)**(3/2)))

def E_y(x,y) :
    return k*( y/((x-0.05)**2 + (y)**2)**(3/2) - y/((x+0.05)**2 + (y)**2)**(3/2))

E_xg = ( (X-0.05)/(((X-0.05)**2 + (Y)**2)**(3/2)) - (X+0.05)/(((X+0.05)**2 + (Y)**2)**(3/2)))

E_yg = ( Y/((X-0.05)**2 + (Y)**2)**(3/2) - Y/((X+0.05)**2 + (Y)**2)**(3/2))


Mag = np.zeros([n+1,n+1])

for i in np.arange(0,n+1):
    for j in np.arange(0,n+1):
         x1 = 0.5*(1*i - (n-i)*(1))/n
         y1 = 0.5*(1*j - (n-j)*(1))/n

         if (x1 == 0.05 and y1 == 0) or (x1 == -0.05 and y1 == 0) :
            Mag[j][i] = 0
         else:
            Mag[j][i] = np.sqrt(E_x(x1,y1)**2 + E_y(x1,y1)**2)

plt.pcolormesh(X,Y,Mag,vmax = 500*k,cmap='jet')
plt.colorbar()
plt.title("Magnitude of Electric field as a function of (x,y)")
 # plt.savefig("q17-magnitude.png")
plt.show()         

Dir = np.zeros([n+1,n+1])

for i in np.arange(0,n+1):
    for j in np.arange(0,n+1):

         Dir[i][j] = np.arctan2(E_yg[i][j],E_xg[i][j])

plt.pcolormesh(X,Y,Dir,cmap='hsv')
plt.colorbar()
plt.title("Direction of Electric field as a function of (x,y)")
 # plt.savefig("q17-Direction.png")
plt.show()         

# vector field plot

# red - positive charge
# blue -  negative charge

plt.streamplot(X,Y,E_xg,E_yg, density= 1 , linewidth=None, color='blue')
plt.plot(-0.05,0,'-ob')
plt.plot(0.05,0,'-or')
 #plt.savefig("q17-vector_electricfield")
plt.show()

