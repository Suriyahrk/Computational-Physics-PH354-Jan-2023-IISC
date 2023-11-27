import numpy as np
import sympy as smp
import matplotlib.pyplot as plt

# part a)

def catalan(n):

    if n == 0 :
        return 1
    else:
        return ((4*n-2)/(n+1))*catalan(n-1)

print(f"catalan number C_100 = {catalan(100)} ")

# output 
# catalan number C_100 = 8.965199470901317e+56 

# part b)

def gcd(m,n):

    if n == 0:
       return m 
    else:
        return gcd(n,m % n)

print(f"The GCD of 192 and 108 is {gcd(192,108)}")


