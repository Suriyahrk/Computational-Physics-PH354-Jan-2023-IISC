import numpy as np
import sympy as smp
import matplotlib.pyplot as plt
import pandas as pd
import sys
sys.path.insert(0,'.')
from Integration_techniques import CI

# part - a)

# CI is the composite integration function containing both simpsons and trapizoidal method which can be found in 
# integration technique's file (it takes symbolic function as input)

x = smp.symbols("x")
f = x**4 -2*x + 1

print(f"The value of the integral calculated using Simpsons rule with 10 slices is {CI(0,2,f,x,10,2)} with fractional error {(CI(0,2,f,x,10,2)-4.4)/4.4}") 

# part - b)

# Output
# The value of the integral calculated using Simpsons rule with 10 slices is 4.40042666666667

# part - c)

print(f"The value of the integral calculated using Simpsons rule with 100 slices is {CI(0,2,f,x,100,2)} with fractional error {(CI(0,2,f,x,100,2)-4.4)/4.4}") 
print(f"The value of the integral calculated using Simpsons rule with 1000 slices is {CI(0,2,f,x,1000,2)} with fractional error {(CI(0,2,f,x,1000,2)-4.4)/4.4}")

print(f"The value of the integral calculated using Trapizoidal rule with 10 slices is {CI(0,2,f,x,10,1)} with fractional error {(CI(0,2,f,x,10,1)-4.4)/4.4}")
print(f"The value of the integral calculated using Trapizoidal  rule with 100 slices is {CI(0,2,f,x,100,1)} with fractional error {(CI(0,2,f,x,100,1)-4.4)/4.4}")
print(f"The value of the integral calculated using Trapizoidal  rule with 1000 slices is {CI(0,2,f,x,1000,1)} with fractional error {(CI(0,2,f,x,1000,1)-4.4)/4.4}")



# Output
 
# The value of the integral calculated using Simpsons rule with 10 slices is 4.40042666666667 with fractional error 0.0000969696969697267
# The value of the integral calculated using Simpsons rule with 100 slices is 4.40000004266667 with fractional error 9.69696969186564E-9
# The value of the integral calculated using Simpsons rule with 1000 slices is 4.40000000000427 with fractional error 9.69527488595387E-13
# The value of the integral calculated using Trapizoidal rule with 10 slices is 4.50656000000000 with fractional error 0.0242181818181820
# The value of the integral calculated using Trapizoidal  rule with 100 slices is 4.40106665600000 with fractional error 0.000242421818181995
# The value of the integral calculated using Trapizoidal  rule with 1000 slices is 4.40001066666560 with fractional error 0.00000242424218214894


# We can see the more number of slices we use more close the value of integral gets to the original value of 4.4
# and its also observed for a given number of slices the simpsons method performs much better than the Trapizoidal method
# concluding simpsons is a better integration technique than trapizoidal.