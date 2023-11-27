import numpy as np
import sympy as smp
import matplotlib.pyplot as plt
import scipy.constants as sc
import sys
sys.path.insert(0,'.')
from Root_finding import *
from linear_alg import *

# Part - b

# Defining the matrices and vectors

Vplus = 5

A = np.array([[ 3, -1, -1, 0, 0, 0 ],
     [-1, 4, -1, -1, 0, 0],
     [-1, -1, 4, -1, -1, 0],
     [0,-1, -1, 4, -1, -1],
     [0, 0, -1, -1, 4, -1],
     [0, 0, 0, -1, -1, 3]],float)

w = np.array([Vplus, Vplus, 0, 0, 0, 0],float)

v = gauss_elim(A,w)

for i in np.arange(1,7):
    print(f"V{i} = {v[i-1]}")


# Output

"""
Volatage at each junctions

V1 = 3.725490196078432
V2 = 3.4313725490196085
V3 = 2.745098039215687
V4 = 2.2549019607843146
V5 = 1.5686274509803926
V6 = 1.2745098039215692

"""

# Part - c

"""
Code for banded gaussian can be found in linear_alg.py

"""

N = 10000
M = np.zeros((N,N))

for i in np.arange(0,N):
        if i == 0 :
            M[i][0] = 3
            M[i][1] = -1
            M[i][2] = -1

        elif i == N-1:
            M[i][N-1] = 3
            M[i][N-2] = -1
            M[i][N-3] = -1

        elif i == 1:
            M[i][0] = -1
            M[i][1] = 4
            M[i][2] = -1
            M[i][3] = -1

        elif i == N-2 :
            M[i][N-4] = -1
            M[i][N-3] = -1
            M[i][N-2] = 4
            M[i][N-1] = -1
             
        else :
            M[i][i-2] = -1
            M[i][i-1] = -1
            M[i][i] = 4
            M[i][i+1] = -1
            M[i][i+2] = -1

             
Y = np.zeros(N)
Y[0] = Vplus
Y[1] = Vplus

X = gauss_elim_banded(M,Y,2)

f = open('potentials.txt', 'w')
f.seek(0) # to avoid rewriting

for i in np.arange(0, N):
    f.write(f"V_{i + 1} = {X[i]} \n")
    
f.close()


