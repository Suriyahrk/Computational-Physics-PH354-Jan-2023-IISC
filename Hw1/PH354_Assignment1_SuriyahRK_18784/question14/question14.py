import numpy as np
import sympy as smp
import matplotlib.pyplot as plt
import pandas as pd


# part -a)

theta = np.arange(0,2*np.pi,0.001)
n = len(theta)
x = []
y = []

for i in np.arange(0,n):
    x.append( 2*np.cos(theta[i]) + np.cos(2*theta[i]))
    y.append( 2*np.sin(theta[i]) - np.sin(2*theta[i]))

plt.plot(x,y)
plt.xlabel("x")
plt.ylabel("y = f(x)")
plt.title("y as a function of x for Q-14 part-a)")
plt.show()

# part -b)

theta1 = np.arange(0,10*np.pi,0.001)
n1 = len(theta1)

r1 = []
for i in np.arange(0,n1):
    r1.append(theta1[i]**2)

x1 = []
y1 = []

for j in np.arange(0,n1):
    x1.append(r1[j]*np.cos(theta1[j]))
    y1.append(r1[j]*np.sin(theta1[j]))

plt.plot(x1,y1)
plt.xlabel("x")
plt.ylabel("y = f(x)")
plt.title(" r = theta**2")
plt.show()

#part - c)

theta2 = np.arange(0,24*np.pi,0.001)
n2 = len(theta2)

r2 = []
for i in np.arange(0,n2):
    r2.append(np.exp(np.cos(theta2[i])) - 2*np.cos(4*theta2[i]) + (np.sin(theta2[i]/12))**5)

x2 = []
y2 = []

for j in np.arange(0,n2):
    x2.append(r2[j]*np.cos(theta2[j]))
    y2.append(r2[j]*np.sin(theta2[j]))

plt.plot(x2,y2)
plt.xlabel("x")
plt.ylabel("y = f(x)")
plt.title("Fey's Function")
plt.show()

    