import numpy as np
import sympy as smp
import matplotlib.pyplot as plt

# part a)

Z = float(input("Enter the atomic number Z : "))
A = float(input("Enter the Mass number A : "))

a1 = 15.67
a2 = 17.23
a3 = 0.75
a4 = 93.2

if A % 2 == 1  :
    B = a1*A - a2*A**(2/3) - a3*Z**2/(A**(1/3)) - a4*(A-2*Z)**2/(A) 
    print(f"The binding energy B (in MeV) : {B}")

elif A % 2 ==0 and Z % 2 == 0:
    B = a1*A - a2*A**(2/3) - a3*Z**2/(A**(1/3)) - a4*(A-2*Z)**2/(A) + 12/(A)**(1/2)
    print(f"The binding energy B (in MeV) : {B}")

else:
    B = a1*A - a2*A**(2/3) - a3*Z**2/(A**(1/3)) - a4*(A-2*Z)**2/(A) - 12/(A)**(1/2)
    print(f"The binding energy B (in MeV) : {B}")

# For Z = 28 and A = 58 we get B = 493.93 MeV

# part b)

print(f"The binding energy per nucleon B/A : {B/A}")

# Binding energy per nucleon : 8.51 MeV for the above example

# part c)
# We define a function

def B(Z,A):
    a1 = 15.67
    a2 = 17.23
    a3 = 0.75
    a4 = 93.2
    

    if A % 2 == 1  :
        B = a1*A - a2*A**(2/3) - a3*Z**2/(A**(1/3)) - a4*(A-2*Z)**2/(A) 
        return B/A

    elif A % 2 ==0 and Z % 2 == 0:
        B = a1*A - a2*A**(2/3) - a3*Z**2/(A**(1/3)) - a4*(A-2*Z)**2/(A) + 12/(A)**(1/2)
        return B/A

    else:
        B = a1*A - a2*A**(2/3) - a3*Z**2/(A**(1/3)) - a4*(A-2*Z)**2/(A) - 12/(A)**(1/2)
        return B/A


Z = int(input("Enter the  atmoic number : "))

Be = np.zeros(int(2*Z + 1))

for i in np.arange(Z,3*Z+1):
    Be[i-Z] = B(Z,i)

Max_BE = max(Be)

print(f"The maximum binding energy per nucleon B/A for atomic number {Z}: {Max_BE}")

for j in np.arange(0,2*Z+1):
    if Be[j] == Max_BE :
        print(f"The Corresponding mass number : {j + Z}")
    else :
        continue
       

# Output
# The maximum binding energy per nucleon B/A for atomic number 28: 8.516131151747729
# The Corresponding mass number : 58

# part d)

# Again defining a function to output Maximum Binding energy and Atomic number

def Max_B(Z):

    Be = np.zeros(int(2*Z + 1))

    for i in np.arange(Z,3*Z+1):
        Be[i-Z] = B(Z,i)

    Max_BE = max(Be)

    R = [Max_BE,0]      # first element is the Maximum binding energy per nucleon and the second element is the corresponding atomic number A

    for j in np.arange(0,2*Z+1):
        if Be[j] == Max_BE :
            R[1] = j + Z
        else:
            continue
    return R

for i in np.arange(1,101):            # priniting out the most stable value of A for each Z from 1 to 100
    F = Max_B(i)
    print(f"The most stable value of A for Atomic number {i} with binding energy {F[0]} is {F[1]}")

# Finding out the Z for Maximum binding energy per nucleon

K = np.zeros(100)   

for i in np.arange(1,101):
   M = Max_B(i)
   K[i-1] = M[0]

K_max = max(K)

for i in np.arange(0,100):
   if K[i] == K_max:
       print(f" The Atomic number Z with maximum binding energy is {i+1}")
   else:
      continue
