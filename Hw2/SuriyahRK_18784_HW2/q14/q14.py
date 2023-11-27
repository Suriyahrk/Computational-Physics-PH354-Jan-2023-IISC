import numpy as np
import sympy as smp
import matplotlib.pyplot as plt
import pandas as pd
import sys
sys.path.insert(0,'.')
from Integration_techniques import *
import scipy.constants as sc

def force_z(z) :
    L = 10
    G = sc.G
    sigma = 10**2

    def FX(x):

        def FY(y):
        
            return 1 / ((x**2 + y**2 + z**2)**(3/2))

        return GQ(-L/2,L/2,FY,100)

    return G*sigma*z*GQ(-L/2,L/2,FX,100)

Nprime = 100
Z = np.linspace(0,10,Nprime)
FZ = []

for i in np.arange(0,Nprime):
    FZ.append(force_z(i*0.2))


plt.plot(Z,FZ)
plt.xlabel("z-Coordinate")
plt.ylabel("Force along z direction")
plt.title("Force along z direction as function of z")
# plt.savefig("q14-part-b.png")
plt.show()

# Note the program takes atleast 50 seconds to run
        
