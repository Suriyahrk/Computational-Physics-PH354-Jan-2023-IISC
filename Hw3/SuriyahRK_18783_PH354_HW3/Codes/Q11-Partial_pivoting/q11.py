import numpy as np
import sympy as smp
import matplotlib.pyplot as plt
import scipy.constants as sc
import sys
sys.path.insert(0,'.')
from Root_finding import *
from linear_alg import *


# part - A

"""
Solving the linear system using partial pivoting .Code for partial pivoting is found in linear_alg.py
"""
Vplus = 5

A = np.array([[ 4,  -1,  -1,  -1 ],
              [ -1,  3, 0, -1 ],
              [ -1, 0,  3,  -1 ],
              [ -1, -1,  -1,  4 ]],float)

y = np.array([ Vplus, 0, Vplus, 0 ],float)

x_ = gauss_elim_partial_pivot(A,y)

for i in np.arange(1,5):
    print(f"V{i} = {x_[i-1]}")

# Output

"""
V1 = 3.0
V2 = 1.6666666666666665
V3 = 3.3333333333333335
V4 = 2.0


We can see we get the same solution using partial pivoting
"""

# Part  - b

B = np.array([[ 0,  1,  4,  1 ],
              [ 3,  4, -1, -1 ],
              [ 1, -4,  1,  5 ],
              [ 2, -2,  1,  3 ]],float)

yprime = np.array([ -4, 3, 9, 7 ],float)

x1 = gauss_elim_partial_pivot(B,yprime)

print(f"The solution obtained using partial pivoting is {x1}")

# Output

"""
The solution obtained using partial pivoting is 
[ 1.61904762
-0.42857143 
-1.23809524 
1.38095238]

"""