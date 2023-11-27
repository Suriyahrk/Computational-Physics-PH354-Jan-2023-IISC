import numpy as np
import sympy as smp
import matplotlib.pyplot as plt



# part - a
"""
 Initial guess a, c - parameter in the function, e is the error bound, N is the maximum number of iteration

"""

def fixed_point_method(a,c,e,N):
    
    def g(x,c):
        return  1 - np.exp(-c*x)
    
    x_ = a
    
    for i in np.arange(0,N):
        x_ = g(x_, c)

        if abs(g(x_, c) - x_) <= e:
            break

    return x_

a = 1
c = 2
e = 10**(-6)
N = 50

print(f" The root of equation computed using fixed point method {fixed_point_method(a,c,e,N)}")

# output

"""
The root of equation computed using fixed point method 0.796813363096688
"""

# part - b

def Multi_fixed_point(a,e,N):

    X = []

    for i in np.arange(0,301):
        X.append(fixed_point_method(a,i/100,e,N))

    return X


C = np.arange(0,3.01,0.01)
X = Multi_fixed_point(a,e,N)

plt.plot(C,X)
plt.xlabel("parameter - c")
plt.ylabel("Root from fixed point method")
plt.title("Percolation transistion graph")
 # plt.savefig("q3_part-b.png")
plt.show()
        
# part - C

"""
The below function is for acceralated fixed point method, which finds the root of the function f(x), with initial guess a,
Error bound e and Maximum number of iteration N
"""
def f(x,c):
    return x - 1 + np.exp(-c*x)

def df(x,c):
    return 1 - c*np.exp(-c*x)

def Accelerated_fixed_point(a,e,N):

    r_0 = -1 / (df(a,c))
    x_i = a

    for i in np.arange(0,N):

        x_i = x_i + r_0 * f(x_i , c)
        print(f"The value of the root at {i}th iteration is {x_i}  with error {abs( r_0 * f(x_i , c))}")

        if abs( r_0 * f(x_i , c)) <= e :
            break

    return x_i

print(f"The Root determined using Accelerated fixed point method is {Accelerated_fixed_point(1,10**(-6),50)} ")

# Output 

"""
The value of the root at 0th iteration is 0.8144387474091372  with error 0.014517961973149333
The value of the root at 1th iteration is 0.7999207854359879  with error 0.0025356062279175643
The value of the root at 2th iteration is 0.7973851792080703  with error 0.00046660573598257955
The value of the root at 3th iteration is 0.7969185734720877  with error 8.66440000362326e-05
The value of the root at 4th iteration is 0.7968319294720515  with error 1.611561775200535e-05
The value of the root at 5th iteration is 0.7968158138542994  with error 2.998396626344378e-06
The value of the root at 6th iteration is 0.7968128154576731  with error 5.578996155163993e-07

The Root determined using Accelerated fixed point method is 0.7968128154576731

"""






    
    


