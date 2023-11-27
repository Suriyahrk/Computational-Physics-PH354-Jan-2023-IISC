import numpy as np

# part - a

def f(x):
    return (np.sin(1 / (x* (2-x)) ))**2

"""
The function can have a maximum value of 1
"""
A = 2 * 1
N = 10000
X = np.random.uniform(0, 2, N)
Y = np.random.uniform(0, 1, N)

k = 0
for i in range(0, N):
    if Y[i] <= f(X[i]):
        k = k + 1
    else:
        continue

I_montecarlo = k*A/N

print(f"The estimate for the integral using hit or miss monte - carlo method is {I_montecarlo} and \n the expected error is {np.sqrt(I_montecarlo*(A - I_montecarlo)/N)} ") 

"""
The estimate for the integral using hit or miss monte - carlo method is 1.4696 
The expected error is 0.008828792895973945 
"""

# part - b
b = 2
a = 0
Z = np.random.uniform(0, 2, N)
F = f(Z)
Sum = np.sum(F)
Variance = np.var(F)
I_meanvalue = ((b - a)/ N)*(Sum)

print(f"The estimate for the integral using mean value method is {I_meanvalue} and \n the expected error is {(b-a)*np.sqrt(Variance/N)}")


"""
The estimate for the integral using mean value method is 1.4523916348443255 
The expected error is 0.005303214747201358

We can see the meanvalue method has a smaller error than monte carlo method
"""