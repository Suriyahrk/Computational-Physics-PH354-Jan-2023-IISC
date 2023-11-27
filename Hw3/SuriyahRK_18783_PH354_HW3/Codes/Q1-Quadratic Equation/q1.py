import numpy as np
import sympy as smp
import matplotlib.pyplot as plt





def f(x):
    return a*x**2 + b*x + c


# Part - a

def Quad_Roots(a,b,c):  
    return (-b + np.sqrt(b**2 - 4*a*c) )/(2* a) ,(-b - np.sqrt(b**2 - 4*a*c) )/(2* a) 


"""
    The given equation is 0.001*x**2 + 1000*x + 0.001 = 0
"""
a = 0.001
b = 1000
c = 0.001

x,y = Quad_Roots(a,b,c)

print(f"The roots of the Quadratic equation are {x} and {y}")

# output

"""
   The roots of the Quadratic equation are -9.999894245993346e-07 and -999999.999999

"""


# Part - b

def Updated_Quad_Roots(a,b,c):
    return (-b + np.sqrt(b**2 - 4*a*c) )/(2* a), (-b - np.sqrt(b**2 - 4*a*c) )/(2* a), 2*c / (-b - np.sqrt(b**2 - 4*a*c) ), 2*c / (-b + np.sqrt(b**2 - 4*a*c) )

x1,x2,y1,y2 = Updated_Quad_Roots(a,b,c)

print(f"The roots of the Quadratic equation from the new formula {y1} and {y2}")

# Output

"""
The roots of the Quadratic equation from the new formula -1.000000000001e-06 and -1000010.5755125057

"""

"""
 Now we check the f(x) values for these roots to determine which roots are better. Let x1 and x2 be the original roots computed and y1 and y2 
 be the new roots computed

"""
print(f"f(x1) = {f(x1)}")
print(f"f(x2) = {f(x2)}")
print(f"f(y1) = {f(y1)}")
print(f"f(y2) = {f(y2)}")


# Output

"""

f(x1) = 1.0575401665491313e-08
f(x2) = 7.247924804689582e-08
f(y1) = 0.0
f(y2) = 10575.62534720993


The divergence for the value of y2 can be explained by having a very small number in the denominator while we are performing
division which causes truncation error cause the root to be Inaccurate.
"""

# Part - C

"""
Observing the roots we can pick the root "x" whose "f(x)" value is closes to zero for each cases. Hence our modified fuction would be,
 
"""

def Modified_Quad_Roots(a,b,c):

    x1,x2,y1,y2 = Updated_Quad_Roots(a,b,c)

    if abs(f(x1)) <= abs(f(y1)) :
        X1 = x1
    else:
        X1 = y1

    if abs(f(x2)) <= abs(f(y2)):
        X2 = x2
    else:
        X2 = y2

    return X1,X2

X1,X2 = Modified_Quad_Roots(a,b,c)

print(f"The best roots comparing their f(x) values are {X1} and {X2} \n")

print(f" With corresponding f(x) values \n f({X1}) = {f(X1)} ")
print(f" f({X2}) = {f(X1)} \n")

# Output

"""
The best roots comparing their f(x) values are -1.000000000001e-06 and -999999.999999

 With corresponding f(x) values
 f(-1.000000000001e-06) = 0.0
 f(-999999.999999) = 0.0
 
"""