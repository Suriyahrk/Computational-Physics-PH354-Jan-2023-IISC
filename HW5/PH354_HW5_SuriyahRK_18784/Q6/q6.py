import numpy as np

# generating the uniform distribution

N = 10**6
Z = np.random.uniform(0, 1, N)

# Using Inversion formula
def I(x):
    return x**2

# New random numbers with desired probability distribution

X = I(Z)

def f(x):
    return 1 / (np.exp(x) + 1)

F = f(X)

"""
The integral of the weight function in the interval is 2, whose derivation can be seen by the images in the folder
"""

I_importance_sampling = (sum(F) / N)*  2

print(f"The value of the integral computed using importance sampling is {I_importance_sampling}")

"""
Output:
The value of the integral computed using importance sampling is 0.8389675972399766
"""