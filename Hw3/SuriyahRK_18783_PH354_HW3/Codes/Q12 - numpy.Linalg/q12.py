import numpy as np

"""
Solving the resistor problem using numpy.linalg

"""
Vplus = 5

A = np.array([[ 4,  -1,  -1,  -1 ],
              [ -1,  3, 0, -1 ],
              [ -1, 0,  3,  -1 ],
              [ -1, -1,  -1,  4 ]],float)

y = np.array([ Vplus, 0, Vplus, 0 ],float)  

X = np.linalg.solve(A,y)

for i in np.arange(1,5):
    print(f"V{i} = {X[i-1]}")

# Output

"""
V1 = 2.9999999999999996
V2 = 1.6666666666666665
V3 = 3.3333333333333326
V4 = 2.0

We can see the final output is very close to the output we got using gaussian elimination
"""