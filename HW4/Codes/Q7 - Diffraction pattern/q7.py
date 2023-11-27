import numpy as np
import matplotlib.pyplot as plt

def q(u):
    a = np.pi / (20* 10 **(-6))
    return np.sin(a*u)**2


w = 200 * 10**(-6)
W = 2* 10**(-3)
l = 500* 10**(-9)
f = 1
x_max = 5*10**(-2) 

N = 500          # no of sampling points among which only first 10 percent or the actual values and remaining are zeros
Y_n = np.zeros(N)

for n in range(0, N):
    if n <= int(N* 0.1):
        Y_n[n] = np.sqrt( q( n* w / (0.1* N) - w/2) )
    else:
        continue

C_k = abs(np.fft.fft( Y_n ))

K_max = int( W* x_max / (l * f) ) # maximum possible value of K reached for the maximum value of x

X = np.linspace(-x_max,x_max, 2*K_max)

I = np.zeros(2*K_max)

for i in range(0, 2*K_max):
    I[i] = (W/N)**2 * (C_k[abs(int( i - K_max))])**2


plt.plot(X, I, color = 'red')
plt.xlabel("x - axis")
plt.ylabel("Intensity")
plt.title("Diffraction patter determined using FFT to evaluate the integral")
plt.grid()
# plt.savefig("Q7.png")
plt.show()