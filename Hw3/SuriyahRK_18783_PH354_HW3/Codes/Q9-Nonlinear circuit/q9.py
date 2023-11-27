import numpy as np
import sympy as smp
import matplotlib.pyplot as plt
import scipy.constants as sc
import sys
sys.path.insert(0,'.')
from Root_finding import *

I0 = 3*10**-9
Vplus = 5
R1 = 1*10**3
R2 = 4*10**3
R3 = 3*10**3
R4 = 2*10**3
V_T = 0.05

#  Defining the functions

x = smp.symbols('x')
y = smp.symbols('y')

Id = I0*( smp.exp((x - y)/ V_T ) - 1)

f = (x - Vplus)/R1 +  x/R2 + Id 

dxf = smp.diff(f,x)
dyf = smp.diff(f,y)

fn = smp.lambdify( [x,y], f)

dxf_n = smp.lambdify( [x,y], dxf)
dyf_n = smp.lambdify( [x,y], dyf)

def grad_fn(x,y):
    return dxf_n( x, y), dyf_n( x, y)

g = (y - Vplus)/R3 + y/R4 - Id

dxg = smp.diff(g,x)
dyg = smp.diff(g,y)

gn = smp.lambdify( [x,y], g)

dxg_n = smp.lambdify( [x,y], dxg)
dyg_n = smp.lambdify( [x,y], dyg)

def grad_gn(x,y):
    return dxg_n( x, y), dyg_n( x, y)

"""
We will be using the TWO - variable newtons method to solve this set of equations

"""
V1,V2 = newton2(2.5,2.5 , 10**(-4), fn, grad_fn, gn, grad_gn) 

print(f"The potential V1 and V2 are \n V1 = {V1} \n V2 = {V2} ")

# Output

"""
The potential V1 and V2 are 
 V1 = 3.4478107805980587 
 V2 = 2.8282838291029155 
 We can see V1 - V2 = 0.6195269514951431 which agrees with the forward diode voltage
"""