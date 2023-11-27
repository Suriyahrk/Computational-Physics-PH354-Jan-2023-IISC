import numpy as np
import sympy as smp
import matplotlib.pyplot as plt
import sys
sys.path.insert(0,'.')
import pandas as pd

def Simpsons(a,b,f,n):
    h = (b-a)/n
    J = f(a) + f(b)

    if n%2 == 1 :
        print("Even number of slices not allowed in case of Simpsons")
    
    else:
        for j in np.arange(1,n):
            if j%2 == 0:
                J = J + 2*f(a + j*h)
            else:
                J = J + 4*f(a+j*h)
        return J*(h/3)

def J_(m,x):  # for given value of m and x we need to perform the integral on theta

    def f(theta):
        return  np.cos(m*theta-x*np.sin(theta))

    return Simpsons(0,np.pi,f,1000)

x = np.arange(0,20,0.1)

J_0 = []
J_1 = []
J_2 = []


for i in np.arange(0,200):
    J_0.append(J_(0,i*0.1))

for i in np.arange(0,200):
    J_1.append(J_(1,i*0.1))

for i in np.arange(0,200):
    J_2.append(J_(2,i*0.1))

plt.plot(x,J_0)
plt.plot(x,J_1)
plt.plot(x,J_2)
plt.xlabel("x")
plt.ylabel("J_m(x)")
plt.title("Bessel functions")
plt.legend(["J_0(x)","J_1(x)","J_2(x)"])
# plt.savefig("q4_part-a.png")
plt.show()

# part - b)

n = 100
I = np.zeros([n,n])

for i in np.arange(0,n):
    for j in np.arange(0,n):
        if np.sqrt( ((2*i-n)/n)**2 + ((2*j-n)/n)**2 ) == 0: # setting the limit for midpoint
            I[i][j] = 1/4
        else:
            I[i][j] = (J_( 1, (2*np.pi/(500*10**(-3))) * np.sqrt( ((2*i-n)/n)**2 + ((2*j-n)/n)**2 ) ) / ((2*np.pi/(500*10**(-3))) * np.sqrt( ((2*i-n)/n)**2 + ((2*j-n)/n)**2 )))**2
        
x = np.linspace(-2,2,n)
y = np.linspace(-2,2,n)
X,Y = np.meshgrid(x,y)

plt.pcolormesh(X,Y,I,vmax=0.01)
plt.colorbar()
plt.xlabel("x")
plt.ylabel("y")
plt.title("Diffraction pattern by a circular aperture")
# plt.savefig("q4-part-b")
plt.show()

# note the following program take atleast 50 seconds to load