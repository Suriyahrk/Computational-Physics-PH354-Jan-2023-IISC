import numpy as np
import sympy as smp
import matplotlib.pyplot as plt
import scipy.constants as sc
import sys
sys.path.insert(0,'.')
from Root_finding import *
from linear_alg import *

# Part - b
"""
Code for gaussian elimination is found in linear_alg.py
"""
Vplus = 5

A = np.array([[ 4,  -1,  -1,  -1 ],
              [ -1,  3, 0, -1 ],
              [ -1, 0,  3,  -1 ],
              [ -1, -1,  -1,  4 ]],float)

y = np.array([ Vplus, 0, Vplus, 0 ],float)


print(f"The values of the potenial are \n")

x_ = gauss_elim(A,y)

for i in np.arange(1,5):
    print(f"V{i} = {x_[i-1]}")

# Output

"""
The values of the potenial are 
V1 = 3.0
V2 = 1.6666666666666665
V3 = 3.3333333333333335
V4 = 2.0

"""