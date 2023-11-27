import numpy as np
import sympy as smp
import matplotlib.pyplot as plt


# Part - a

def f(x):
    return x*(x-1)

# Derivative using the difference formula

def Derivative(x,delta):
    return (f(x + delta) - f(x) )/ (delta)

print(f"The derivative of x(x-1) at x = 1 with Delta  = 10**(-2) is {Derivative(1,10**(-2))}")

# Output 

"""
The derivative of x(x-1) at x = 1 with Delta  = 10**(-1) is 1.010000000000001.

The derivative calculated using analytical differentiation is 1. Both values agree till second order. They dont agree perfectly because 
the value of derivative computed using the differnce formula will exactly match the analytical value only in the limit delta approaches 
zero. In fact thats how derivative at a point is defined.

"""

print(f"The derivative of x(x-1) at x = 1 with Delta  = 10**(-4) is {Derivative(1,10**(-4))}")
print(f"The derivative of x(x-1) at x = 1 with Delta  = 10**(-6) is {Derivative(1,10**(-6))}")
print(f"The derivative of x(x-1) at x = 1 with Delta  = 10**(-8) is {Derivative(1,10**(-8))}")
print(f"The derivative of x(x-1) at x = 1 with Delta  = 10**(-10) is {Derivative(1,10**(-10))}")
print(f"The derivative of x(x-1) at x = 1 with Delta  = 10**(-12) is {Derivative(1,10**(-12))}")
print(f"The derivative of x(x-1) at x = 1 with Delta  = 10**(-14) is {Derivative(1,10**(-14))}")

# Output 

"""

The derivative of x(x-1) at x = 1 with Delta  = 10**(-2) is 1.010000000000001
The derivative of x(x-1) at x = 1 with Delta  = 10**(-4) is 1.0000999999998899
The derivative of x(x-1) at x = 1 with Delta  = 10**(-6) is 1.0000009999177333
The derivative of x(x-1) at x = 1 with Delta  = 10**(-8) is 1.0000000039225287
The derivative of x(x-1) at x = 1 with Delta  = 10**(-10) is 1.000000082840371
The derivative of x(x-1) at x = 1 with Delta  = 10**(-12) is 1.0000889005833413
The derivative of x(x-1) at x = 1 with Delta  = 10**(-14) is 0.9992007221626509

We observe that the derivative is most accurate when Delta = 10**(-8) after which the values starts get worse, this can be attributed to 
the denominator in the difference formula getting smaller and smaller , causing truncation error which computing the division similar to
the first problem.

"""