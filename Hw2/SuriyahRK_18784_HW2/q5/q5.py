import numpy as np
import sympy as smp
import matplotlib.pyplot as plt
import pandas as pd
import sys
sys.path.insert(0,'.')
from Integration_techniques import CI

# Note CI take symbolic functions as inputs

x = smp.symbols("x")
f = x**4-2*x+1

# for n  = 10 slices

I_1 = CI(0,2,f,x,10,1) # method = 1 is trapizoid
I_2 = CI(0,2,f,x,20,1)
h_1 = 0.2
h_2 = 0.1
# From the question we know I = I_1 + c*h_1**2 , I = I_2 + c*h_2**2

Error = (h_2**2/(h_1**2-h_2**2))*(I_2-I_1)

print(f"The error computed using the method given in question {-Error} ")
print(f"The error from difference from actual value {-4.4 + I_2}")

# output

# The error computed using the method given in question 0.0266333333333331 
# The error from difference from actual value 0.0266600000000015

# Explanation

"""
W can see the errors aggrees to 3 decimal places which is reasonably high accuracy. Mathematically both the errors are not the same as 
as we neglect the higher order terms in the taylor series expansion for the method mentioned in question, this can be interpreted 
truncation error and there might also be computaional error.

"""
