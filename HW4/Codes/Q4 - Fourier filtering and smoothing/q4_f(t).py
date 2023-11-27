import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import rfft, irfft


def f(t):
    if int(2*t) % 2 == 0 :
        return 1
    else:
        return -1

X = np.linspace(0,1,1000)
F = []

for i in range(0,1000):
    F.append(f(X[i]))

C = np.fft.rfft(F)

for i in range(10,501):
    C[i] = 0

Fprime = irfft(C)

plt.plot(X,F)
plt.plot(X,Fprime)
plt.xlabel("X- axis")
plt.ylabel("f(x)")
plt.title("Stepfunction and fourier superposition of initial 10 modes")
plt.legend([" Original function" , " Filtered function "])
# plt.savefig("Q4_f(t).png")
plt.show()


"""
Observation:
    We can notice that the inverted values obtained from the inverse fourier transform, do not perfectly match the original square wave.
    In particular, we can observe significant changes near the discontinuous portion of the function. 
    This discrepancy can be attributed to us excluding most of the fourier coefficients and only retained the first
    10 terms. Since the final fourier transform of the function is a sum of finite number of sine waves, we cannot expect the 
    final obtained function to exactly match the initial step function. Therefore, the wiggles and other artifacts arise due
    to considering only a few / finite terms of the series. The series will converge to the step function only when an 
    infinite number of fourier terms are taken into account.

"""