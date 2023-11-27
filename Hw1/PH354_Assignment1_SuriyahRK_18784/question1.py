import numpy as np
import sympy as smp
import matplotlib as plt


# The time taken by the ball to reach ground is given by t = sqrt(2h/g)

h = float(input("Enter the height of the tower (in meters) :"))
g = 9.8
t = np.sqrt(2*h/g)

print(f"Time taken by the ball to reach ground is {t} seconds")

# Thus the time taken by the ball to reach the ground when dropped from 100m is 4.518 sec