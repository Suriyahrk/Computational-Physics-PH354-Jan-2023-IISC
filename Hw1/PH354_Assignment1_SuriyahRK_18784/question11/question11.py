import numpy as np
import sympy as smp
import matplotlib as plt

p =[2]


for i in np.arange(3,10001):
    check_prime = 1
    j=0
    while j < len(p) and p[j] <= int(np.sqrt(i)):
        if i % p[j] == 0:
            check_prime = 0
            break
        else:
            j = j+1
    if check_prime == 1:
        p.append(i)

print(f"The list of prime numbers are {p}")



            

        