import numpy as np
import sympy as smp
import matplotlib.pyplot as plt
import pandas as pd
import sys
sys.path.insert(0,'.')
from Integration_techniques import CT
# part- a)

Data = pd.read_csv("velocities.txt", sep="\t", header = None)

time = Data[0]
velocity = Data[1]
Distance = []

# CT - composite trapizoidal method function
for i in np.arange(0,101):
    Distance.append(CT(0,i,velocity,i))

# part - b) 

# plotting distance and velocity as a function of time    

plt.plot(time,Distance)
plt.plot(time,velocity,'r')
plt.xlabel("Time (in seconds)")
plt.legend(["Distance","velocity"])
plt.title("Distance and velocity as a function of time")
# plt.savefig("q1-part-b.png")
plt.grid()
plt.show()


