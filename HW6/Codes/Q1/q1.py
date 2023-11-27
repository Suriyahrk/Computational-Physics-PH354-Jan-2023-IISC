import numpy as np
import matplotlib.pyplot as plt
import sys
sys.path.insert(0,'.')
from Methods.Runge_katta_4th_order import Runge_kutta_4


# part -a 

# Defining the parameters 
Values = [0.01, 0.1, 1]
a = 0
b = 10
h = 0.0001
s = 0

# Inupt function
def V_in(t):
    if int(2 * t) % 2 == 0 :
            return 1
    else:
         return -1

N = int( (b - a) / h )
X_square =  np.linspace(a, b, N)
Y_square = np.zeros(N)

for i in range(0, N):
    Y_square[i] = V_in( X_square[i] )

# loop to plot for all values of given RC
for i in range(0,3):

    RC = Values[i]

    def f(t , V_out):
        return (V_in(t) - V_out) / RC

    X, Y = Runge_kutta_4(a, b, h, f, s)

    plt.plot(X, Y)


plt.plot(X_square, Y_square)
plt.title("Amplitude as a function of time")
plt.legend(["RC = 0.01", "RC = 0.1", "RC = 1", "Input wave"])
# plt.savefig("Q1_h=0.0001_without_input_wave.png")
plt.show()

"""
Part - b

    We can notice for higher value of RC the output is deviating more from the input which can attributed to the fact the circuit behaves
    as a low pass filter and lower values of RC is weaker low pass filter, therfore more or less lets the input pass through but when we 
    reach the higher values, the filter is removing the higher frequency thus reducing the overall amplitude, which can be witnessed from 
    the graph. the non - diffrentiable points are still pressent, which implies the low pass filter is only reducing the amplitudes of 
    higher frequency and not completely removing thus keeping the general features of the input signal.
"""