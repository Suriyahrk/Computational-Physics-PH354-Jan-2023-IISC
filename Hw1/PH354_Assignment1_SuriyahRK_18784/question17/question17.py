import numpy as np
import sympy as smp
import matplotlib.pyplot as plt
import pandas as pd

n = 1000 # density of grid
I = 100 # no of iterations
Z = np.zeros([n,n])
C = np.zeros([n,n])
x = np.linspace(-2,2,n)
y = np.linspace(-2,2,n)

X,Y = np.meshgrid(x,y)
for i in np.arange(0,n):
    for m in np.arange(0,n):
        k = 0
        z = 0 + 0*1j
        while k <= I and np.absolute(z) <= 2 :
            z = z**2 -(-2*i + 2*(n-i))/n -((-2*m + 2*(n-m))/n)*1j
            k = k + 1
            C[i][m] = k
        if np.absolute(z) <= 2 :
            Z[i][m] = 1
        else:
            continue

plt.pcolormesh(X,Y,Z.transpose(), cmap = 'Greys')
plt.title("Mandelbrot set - black and white")
plt.show()

plt.pcolormesh(X,Y,C.transpose(), cmap = 'hot')
plt.title("Mandelbrot set - Hot")
plt.show()


plt.pcolormesh(X,Y,C.transpose(), cmap = 'jet')
plt.title("Mandelbrot set - jet")
plt.show()