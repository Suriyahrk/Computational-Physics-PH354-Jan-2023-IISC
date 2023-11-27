import numpy as np
import sympy as smp
import matplotlib.pyplot as plt
import scipy.constants as sc
import sys
sys.path.insert(0,'.')
from Root_finding import *
import cmath as cm




R1 = 10**3 
R3 = 10**3 
R5 = 10**3 
R2 = 2 * 10**3 
R4 = 2 * 10**3 
R6 = 2 * 10**3 
C1 = 10**(-6) 
C2 = 0.5 * 10**(-6) 
x_plus = 3 
w = 1000 

a1 = np.array([1/R1 + 1/R4 + 1j*w*C1, -1j*w*C1, 0])
a2 = np.array([-1j*w*C1, 1/R2 + 1/R5 + 1j*w*(C1 + C2), -1j*w*C2])
a3 = np.array([0, -1j*w*C2, 1/R3 + 1/R6 + 1j*w*C2])

A = np.array([a1, a2, a3])
y = np.array([x_plus/R1, x_plus/R2, x_plus/R3])
x = np.linalg.solve(A, y)

print(f"The magnitute and phase of V1 is \n A =  {cm.polar(x[0])[0]} \n theta = {cm.polar(x[0])[1] * 180 / np.pi} ")
print(f"The magnitute and phase of V2 is \n A =  {cm.polar(x[1])[0]} \n theta = {cm.polar(x[1])[1] *180 / np.pi}  ")
print(f"The magnitute and phase of V3 is \n A =  {cm.polar(x[2])[0]} \n theta = {cm.polar(x[2])[1]* 180 / np.pi} ")

# Output

"""
The magnitute and phase of V1 is 
A     =  1.70
theta = -5.46 (in deg)
The magnitute and phase of V2 is 
A     =  1.48
theta = 11.58 (in deg)
The magnitute and phase of V3 is 
A     =  1.86 
theta = -4.16 (in deg)
"""