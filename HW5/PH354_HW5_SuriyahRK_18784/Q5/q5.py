import numpy as np
from math import gamma

N = 10**6
d = 10
X = np.random.uniform(-1, 1, size=(d, N))

def f(x):
    if x <= 1:
        return 1
    else:
        0

k = 0
for i in range(0, N):
    if f( (np.linalg.norm(X[:, i]))**2 ) == 1 :
        k = k + 1
    else:
        continue

print(f"The volume of a unit hyper sphere of {d} dimensions calculated using monte carlo method is {2**(d)*(k/N)}")
print(f"The volume of {d} dimensionsal unit sphere  computed using the actual formula is {np.pi**(d/2) / (gamma(d/2 + 1))}")

"""
Output:

The volume of a unit hyper sphere of 10 dimensions calculated using monte carlo method is 2.596864
The volume of 10 dimensionsal unit sphere  computed using the actual formula is 2.550164039877345

"""

