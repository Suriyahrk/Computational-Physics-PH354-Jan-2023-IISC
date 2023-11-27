
import numpy as np
import sympy as smp
import matplotlib.pyplot as plt
import pandas as pd

# part - a)

D = pd.read_csv("millikan.txt", sep=" ", header = None)
x = np.array(D[0])
y = np.array(D[1])

plt.scatter(x,y)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Scatter plot")
plt.show()

# part - b)

N = len(x)

E_x = np.sum(x)/N
E_y = np.sum(y)/N
E_xx = np.sum(np.power(x,2))/N
E_xy = np.sum(x*y)/N

m = (E_xy-E_x*E_y)/(E_xx - E_x**2)
c = (E_xx*E_y - E_x*E_xy)/(E_xx - E_x**2)

print(f"The values of m and c from least square approximation are {m} and {c} respectively")

# output

# The values of m and c from least square approximation are 4.088227358517516e-15 and -1.7312358039813558 respectively

# part -c)

y1 = m*x + c

plt.plot(x,y1,'red')
plt.scatter(x,y)
plt.xlabel("x")
plt.ylabel("y")
plt.legend(["Linear fit","original data points"])
plt.title("data points and corresponding linear least square fit")
plt.show()

#part - d)

# we know the relationship between voltage and frequency is given by V = (h/e)f - phi from our linear least square fit we have already 
# determined a good approximation for m = h/e therefore
e = 1.602*10**(-19)

h = m*e
h_actual = 6.62607015*10**(-34)

print(f"Actual value of plancks constant h : {h_actual}")
print(f"Least square fit vaue of h  : {h}")

print(f"percentage of error {(h_actual- h)*100/h_actual} %")

# output

# Actual value of plancks constant h : 6.62607015e-34
# Least square fit vaue of h  : 6.549340228345061e-34
# percentage of error 1.1580004424634536 %