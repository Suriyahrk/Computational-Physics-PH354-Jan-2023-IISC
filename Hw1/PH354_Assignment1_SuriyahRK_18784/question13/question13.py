
import numpy as np
import sympy as smp
import matplotlib.pyplot as plt
import pandas as pd


# part-a)

time = []
no_of_sunspots = []

D = pd.read_csv("sunspots.txt", sep="\t", header = None)
time = D[0] 
no_of_sunspots= D[1]

plt.plot(time,no_of_sunspots)
plt.xlabel("Time (in months)")
plt.ylabel("No of sunspots")
plt.title("No of sunspots vs time")
plt.show()

# part-b)

time1 = D[0][0:1000 ]
no_of_sunspots1 = D[1][0:1000]

plt.plot(time1,no_of_sunspots1)
plt.xlabel("Time (in months)")
plt.ylabel("No of sunspots")
plt.title("No of sunspots vs time first 1000 datapoints")
plt.show()

# part-c)

RA = np.zeros(1000)
k = 0
for i in np.arange(5,1005):
    for j in np.arange(-5,6):
        RA[i-5] = RA[i-5] + D[1][i+j]/(10) 

plt.plot(time1,no_of_sunspots1,'r')
plt.plot(time1,RA)
plt.xlabel("Time (in months)")
plt.ylabel("No of sunspots")
plt.legend(["original","Running average"])
plt.title("No of sunspots vs time first 1000 datapoints (original vs running average)")
plt.show()

       


