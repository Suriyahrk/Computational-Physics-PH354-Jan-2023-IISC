import numpy as np
import sympy as smp
import matplotlib.pyplot as plt
import scipy.constants as sc
import sys
sys.path.insert(0,'.')
from Root_finding import *
from linear_alg import *

"""
I have used the modified gram schmidt orthonormalization to determine the QR decomposistion of the given matrix. The code for it is 
available in linear_alg.py

"""

# Part - b

A = np.array( [[1,4,8,4],
               [4,2,3,7],
                [8,3,6,9],
                [4,7,9,2]] )

Q1,R1 = Modified_Gram_schmidt(A)


print(f"Original matrix A = {A}")
print(f" The QR decomposistion of the matrix A is \n Q = {Q1} \n R = {R1}")


"""
Verifying the QR decomposistion by recovering the original matrix
"""
 
Aprime = np.dot(Q1, R1)
print(f"The computed matrix A is {Aprime} ")


# Output

"""

Original matrix
A =
[[1 4 8 4]
[4 2 3 7]
[8 3 6 9]
[4 7 9 2]]

The QR decomposistion of the matrix A is 
Q =
[[ 0.10153462  0.558463    0.80981107  0.1483773 ]
[ 0.40613847 -0.10686638 -0.14147555  0.8964462 ]
[ 0.81227693 -0.38092692  0.22995024 -0.37712564]
[ 0.40613847  0.72910447 -0.5208777  -0.17928924]] 

R = 
[[ 9.8488578   6.49821546 10.55960012 11.37187705]
[ 0.          5.98106979  8.4234836  -0.484346  ]
[ 0.          0.          2.74586406  3.27671222]
[ 0.          0.          0.          3.11592335]]

The computed matrix A is 
[[1. 4. 8. 4.]
[4. 2. 3. 7.]
[8. 3. 6. 9.]
[4. 7. 9. 2.]]

Same as the original matrix!. hence the Qr decomposition works.


"""

# Part - C

"""
Determining the Eigen value matrix and Eigen values
"""

D ,E_v = Eigen(A, 10**(-6), 100 )

print(f"The Eigenvalue Diagonal matrix is  \n D =  {D}  ")
print(f"The Eigenvector matrix is  \n E_v =  {E_v}  ")

# Output

"""
The Eigenvalue Diagonal matrix is
D =  
[[ 2.10000000e+01  7.36068000e-07  3.45152416e-14 -2.16976381e-14]
[ 7.36067998e-07 -8.00000000e+00  5.99038979e-08  8.85107004e-15]
[ 1.76373367e-14  5.99038974e-08 -3.00000000e+00 -2.06493955e-08]
[ 5.69063112e-23  9.58659066e-16 -2.06493983e-08  1.00000000e+00]]

The Eigenvector matrix is

E_v =  
[[ 0.43151698 -0.38357064 -0.77459666 -0.25819889]
[ 0.38357063  0.43151698 -0.2581989   0.77459667]
[ 0.62330228  0.52740965  0.25819889 -0.51639778]
[ 0.52740965 -0.62330227  0.51639779  0.25819889]]


The Eigenvalues are indeed 21, -8, -3, 1

"""

    




