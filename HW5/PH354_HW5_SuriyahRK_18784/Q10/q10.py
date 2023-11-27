import numpy as np
from math import acos

"""
The inverse transformation to which we can feed the uniform distribution can be found in Q10_derivations
"""

z_theta = np.random.uniform(0, 1)
z_phi  = np.random.uniform(0, 1)

theta = acos(2*z_theta - 1)
phi  =  2* np.pi* z_phi

print(f" The random value of theta generated from sin(theta) /2 distribution is {theta}")
print(f" The random value of phi generated from 1 / (2* pi) distribution is {phi}")

"""
One random output:

The random value of theta generated from sin(theta) /2 distribution is 2.0200461586622205
The random value of phi generated from 1 / (2* pi) distribution is 0.3642369921705396

"""