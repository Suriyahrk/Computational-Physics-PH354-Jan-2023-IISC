import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

"""
We need to perform the fourier transform for each value of K
"""
def fft_power2(A):
    N = len(A)
    C = np.zeros(N, dtype=np.complex128)

    def sub_func(B ,k):
        if len(B) == 1:
            return B[0]
        
        else:
            B_even = []
            B_odd = []

            for i in range(0, int (len(B) / 2)):
                B_even.append(B[2*i])
                B_odd.append(B[2*i +1])
        
            C_even = sub_func(B_even, k)
            C_odd = sub_func(B_odd, k)

            return C_even + np.exp(-1j* 2* np.pi* k/ len(B))* C_odd
        
    for k in range(0, N):
        C[k] = sub_func(A, k)

    return C 

Data = pd.read_csv("pitch.txt", sep=" ", header= None )

A = np.squeeze(Data)

C = fft_power2(A)               # obtained from above function
C_fft = np.fft.fft(A)           # obtained from numpy fft function
x = np.linspace(1,len(A),len(A))

fig, axs = plt.subplots(2, 1, sharex=True)

# Plot the first graph in the first subplot
axs[0].plot(x, abs(C_fft))
axs[0].set_ylabel('Amplitudes')
axs[0].set_title(" My fft function")


# Plot the second graph in the second subplot
axs[1].plot(x, abs(C_fft), color='red')
axs[1].set_ylabel('Amplitude')
axs[1].set_xlabel('x')
axs[1].set_title("numpy fft function")

# plt.savefig("Q6.png")
plt.show()







