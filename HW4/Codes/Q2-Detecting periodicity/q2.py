import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys
sys.path.insert(0,'.')
from Modules.DFT import DFT


# part - a
Data = pd.read_csv("sunspots.txt", sep="\t", header = None)

D = np.array(Data)
N = D.shape[0]   # 3143

Time = D[:, 0].transpose()
no_of_sunspots = D[:, 1].transpose()

plt.plot(Time,no_of_sunspots )
plt.xlabel(" Time (in months)")
plt.ylabel("No of sunspots")
plt.title("No of sunsopts as function of time")
# plt.savefig("Q2-part-a.png")
plt.grid()
plt.show()

"""
From the graph we can see the estimate for the time period is about 140 months 
"""

# part b 

"""
Defining a function to take the Discrete fourier transform
"""

def no_sunspots(n):
    return no_of_sunspots[n]

c_k = DFT(no_sunspots, N)

K = np.linspace(0,N//2,N)
power = abs(c_k(K))**2

plt.plot(K, power)
plt.xlabel("k")
plt.ylabel("Power spectrum")
plt.grid()
# plt.savefig("Q2-part-b.png")
plt.show()


# part - c

"""
From the fourier transform graph we can see there is a peak at k = 22 which will correspond to a frequency f = k/n where N is 3143 in our 
sample. Hence the time period is T = 1/f = 3143/22 = 142 months

"""