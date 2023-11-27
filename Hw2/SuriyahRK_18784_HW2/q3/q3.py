import numpy as np
import sympy as smp
import matplotlib.pyplot as plt
import pandas as pd
import sys
sys.path.insert(0,'.')
from Integration_techniques import CI

# part - a)

x = smp.symbols("x")
f = smp.exp(-x**2)

E_x = []

x_ = np.arange(0,3.1,0.1)

# we will be using simpsons method to evaluate the integral as its a better integration technique. Note the number of slices will
# depend on the upperlimit as we are fixing the width of slice.
# CI is found in Integration technique's file
 
for i in np.arange(0,31):
    E_x.append(CI(0.0,i*0.1,f,x,i*100 + 2,2))

# part - b

plt.plot(x_,E_x)
plt.xlabel("x")
plt.ylabel("E(x)")
plt.title("Integral of the gaussian (Error function)")
# plt.savefig("q3-part-b.png")
plt.show()

# note the above program takes atleast 20 seconds to load due to using symbolic function.
