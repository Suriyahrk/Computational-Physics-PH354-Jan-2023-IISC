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

I_1 = CI(0,2,f,x,10,2) # method = 1 is trapizoid
I_2 = CI(0,2,f,x,20,2)
h_1 = 0.2
h_2 = 0.1
# For simpsons rule I = I_1 + c*h_1**4 , I = I_2 + c*h_2**4

Error = (h_2**4/(h_1**4-h_2**4))*(I_2-I_1)

print(f"The error computed using the method given in question {Error} ")
print(f"The error from difference from actual value {4.4 - I_2}")

# output

# The error computed using the method given in question -0.0000266666666666637 
# The error from difference from actual value -0.0000266666666668414

# explanation

# we can see the similar to trapizoidal method both agrees to high accuracy but are slightly varied explained by truncation error
