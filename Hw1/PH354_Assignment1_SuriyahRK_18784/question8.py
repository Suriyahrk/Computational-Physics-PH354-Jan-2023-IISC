import numpy as np
import sympy as smp
import matplotlib as plt

L = 100
M_c = 0

for i in np.arange(-L,L+1):
    for j in np.arange(-L,L+1):
        for k in np.arange(-L,L+1):
            if i == 0 and j ==0 and k==0 :
                continue
            elif (i+j+k)%2 == 0 :
                M_c = M_c + 1/np.sqrt(i**2+j**2+k**2)
            else:
                 M_c = M_c - 1/np.sqrt(i**2+j**2+k**2)

print(f"The approximate value of Madelung constant is {M_c}")
        
    # Value from wikipedia                 : 	±1.747565
    # Value determined through computation :