import numpy as np
import sympy as smp
import matplotlib.pyplot as plt
import pandas as pd
import sys
sys.path.insert(0,'.')
from Integration_techniques import *

# part - a
x = smp.symbols("x")
f = (smp.sin(smp.sqrt(100*x)))**2

I = CI(0,1,f,x,1,1)
N = 1
print(f"The value of the integral using composite trapizoidal rule for 1 slice is {I}")
e=10

# Note : The error intrapizoidal method is calculated using the technique in q-6 by subtracting adjacent Integration values of n**2 
# and (n/2)**2

while (abs(e) > 10**(-6)):
    N  = 2*N
    Iprime  = CI(0,1,f,x,N,1)
    e = (N/2)**2*(I - Iprime)/((N/2)**2-N**2)


    print(f"The value of the integral composite trapizoidal rule  for {N} slice is {Iprime} with error {e}")
    I = Iprime

# output

"""
The value of the integral using composite trapizoidal rule for 1 slice is 0.147979484546652
The value of the integral composite trapizoidal rule  for 2 slice is 0.325231907806475 with error 0.0590841410866075
The value of the integral composite trapizoidal rule  for 4 slice is 0.512282850723332 with error 0.0623503143056191
The value of the integral composite trapizoidal rule  for 8 slice is 0.402997448478249 with error -0.0364284674150278
The value of the integral composite trapizoidal rule  for 16 slice is 0.430103369294747 with error 0.00903530693883288
The value of the integral composite trapizoidal rule  for 32 slice is 0.448414665787470 with error 0.00610376549757428
The value of the integral composite trapizoidal rule  for 64 slice is 0.453912931215376 with error 0.00183275514263529
The value of the integral composite trapizoidal rule  for 128 slice is 0.455348504372802 with error 0.000478524385808680
The value of the integral composite trapizoidal rule  for 256 slice is 0.455711266453241 with error 0.000120920693479687
The value of the integral composite trapizoidal rule  for 512 slice is 0.455802199651664 with error 0.0000303110661409867
The value of the integral composite trapizoidal rule  for 1024 slice is 0.455824948132420 with error 0.00000758282691878017
The value of the integral composite trapizoidal rule  for 2048 slice is 0.455830636201645 with error 0.00000189602307498760
The value of the integral composite trapizoidal rule  for 4096 slice is 0.455832058278270 with error 4.74025541670938E-7


We notice for 2048 slices the trapizoidal rule reaches desired accuracy

"""

# part - b

def f(x):
    return (np.sin(np.sqrt(100*x)))**2

eps = 10**(-6)
R, j, e = romberg(0,1,eps,20,f)

for i in np.arange(0,j+1):
    print(R[i][0:i])

print(f" The final estimate for Romberg integration with {2**(j)} slices is {R[j][j]} with error {e[j]}")

# output

"""
0.32523191
0.51228285 0.57463317
0.40299745 0.36656898 0.35269804
0.43010337 0.43913868 0.44397666 0.44542552
0.44841467 0.45451843 0.45554375 0.45572735 0.45576775
0.45391293 0.45574569 0.4558275  0.45583201 0.45583242 0.45583248

The final estimate for Romberg integration with 64 slices is 0.4558324944613787 with error 1.3428278877370225e-08

"""