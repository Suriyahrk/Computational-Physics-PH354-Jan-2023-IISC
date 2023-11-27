import numpy as np
import sympy as smp
import matplotlib as plt

C = 1 # Initialization
n = 0
while (C < 10**9):
    print(f" The Catalan number C_{n} is {C}")
    C = ((4*n +2)/(n+2))*C
    n = n+1
