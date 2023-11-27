import numpy as np
import sympy as smp
import matplotlib.pyplot as plt
import pandas as pd
import cmath as cm
import sys
sys.path.insert(0,'.')
from Integration_techniques import *
import scipy.constants as sc

# part a 

Data = pd.read_csv("stm.txt", sep=" ", header = None)

lenY = 663
lenX = 676
h = 2.5

dw_dx = np.zeros([lenX,lenY])

for i in np.arange(0,lenX):
    for j in np.arange(0,lenY):
        if i == lenX-1:
            dw_dx[i][j] =  (Data[i][j] - Data[i-1][j])/h
        else:
            dw_dx[i][j] =  (Data[i+1][j] - Data[i][j])/h
        
dw_dy = np.zeros([lenX,lenY])

for i in np.arange(0,lenX):
    for j in np.arange(0,lenY):
        if j == lenY-1:
            dw_dy[i][j] =  (Data[i][j] - Data[i][j-1])/h
        else:
            dw_dy[i][j] =  (Data[i][j+1] - Data[i][j])/h

# part - b

I = np.zeros([lenX,lenY])

phi = np.pi/4

for i in np.arange(0,lenX):
    for j in np.arange(0,lenY):
        I[i][lenY-1-j] = -(np.cos(phi)*dw_dx[i][j]+np.sin(phi)*dw_dy[i][j])/(np.sqrt(dw_dx[i][j]**2 + dw_dy[i][j]**2 + 1 ))

plt.pcolormesh(I.transpose())
# plt.savefig("q19-part-c-surface.png")
plt.colorbar()
plt.show()

