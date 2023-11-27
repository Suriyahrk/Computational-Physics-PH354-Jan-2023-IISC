import numpy as np
import sympy as smp
import matplotlib.pyplot as plt
import pandas as pd
import cmath as cm
import sys
sys.path.insert(0,'.')
from Integration_techniques import *
import scipy.constants as sc
from math import factorial

def f(z):
    return np.exp(2*z)

def dfm(m):
    N = 10000
    S = 0
    for k in np.arange(0,10000):
        S = S + f(np.exp(1j*2*np.pi*k/N))*(np.exp(-1j*2*np.pi*k*m/N))

    return (factorial(m)/N)*S

for m in np.arange(1,21):
    print(f"The {m}th derivative of exp(2z) is {dfm(m).real}")

# output

"""
The 1th derivative of exp(2z) is 1.9999999999999925
The 2th derivative of exp(2z) is 3.9999999999999907
The 3th derivative of exp(2z) is 8.000000000000005
The 4th derivative of exp(2z) is 16.000000000000025
The 5th derivative of exp(2z) is 32.00000000000009
The 6th derivative of exp(2z) is 64.00000000000028
The 7th derivative of exp(2z) is 128.00000000000227
The 8th derivative of exp(2z) is 256.0000000000046
The 9th derivative of exp(2z) is 512.0000000000758
The 10th derivative of exp(2z) is 1024.000000002165
The 11th derivative of exp(2z) is 2048.0000000172995
The 12th derivative of exp(2z) is 4095.999999909272
The 13th derivative of exp(2z) is 8192.000001073206
The 14th derivative of exp(2z) is 16383.999994002997
The 15th derivative of exp(2z) is 32768.00000054964
The 16th derivative of exp(2z) is 65536.00535630442
The 17th derivative of exp(2z) is 131072.02920286346
The 18th derivative of exp(2z) is 262145.8249330606
The 19th derivative of exp(2z) is 524320.2999079637
The 20th derivative of exp(2z) is 1048748.3182413138

"""



