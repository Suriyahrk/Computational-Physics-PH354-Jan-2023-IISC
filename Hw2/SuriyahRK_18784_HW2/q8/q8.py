import numpy as np
import sympy as smp
import matplotlib.pyplot as plt
import pandas as pd
import sys
sys.path.insert(0,'.')
from Integration_techniques import *

# part - a
x = smp.symbols("x")
f = (smp.sin(smp.sqrt(100*x)))**2

I = CI(0,1,f,x,2,2)
N = 2
print(f"The value of the integral using Composite Simpson for 2 slice is {smp.N(I)}")
e=10
while (abs(e) > 10**(-6)):
    N  = 2*N
    Iprime  = CI(0,1,f,x,N,2)
    e = (N/2)**4*(I - Iprime)/((N/2)**4-N**4)
    print(f"The value of the integral using Composite Simpson for {N} slice is {smp.N(Iprime)} with error {smp.N(e)}")
    I = Iprime

# output

"""

The value of the integral using Composite Simpson for 2 slice is 0.384316048893082
The value of the integral using Composite Simpson for 4 slice is 0.574633165028951 with error 0.0126878077423913
The value of the integral using Composite Simpson for 8 slice is 0.366568981063221 with error -0.0138709455977154
The value of the integral using Composite Simpson for 16 slice is 0.439138676233580 with error 0.00483797967802396
The value of the integral using Composite Simpson for 32 slice is 0.454518431285044 with error 0.00102531700343094
The value of the integral using Composite Simpson for 64 slice is 0.455745686358011 with error 0.0000818170048644602
The value of the integral using Composite Simpson for 128 slice is 0.455827028758611 with error 0.00000542282670663986
The value of the integral using Composite Simpson for 256 slice is 0.455832187146721 with error 3.43892540699708E-7

We notice the composite simpsons method reaches desired accuracy in 128 slices


Observation :
        We can see number of slices for simpsons is less than trapizoid but slightly bigger than romberg clearly reflecting the theory
     
"""