import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys
sys.path.insert(0,'.')
from Modules.dcst import *

# part - a

Data = pd.read_csv("dow2.txt",sep= " ",header= None)

dow2 = np.squeeze(Data)

plt.plot(dow2)
plt.xlabel("n")
plt.ylabel("Price")
plt.title("Initial plot of dow2.txt")
plt.grid()
# plt.savefig("Q5-a-original.png")
plt.show()


fft_dow2 = np.fft.rfft(dow2)

K = fft_dow2.shape[0]

for i in range(int(K * 2 /100) , K):
    fft_dow2[i] = 0

filtered_dow2 = np.fft.irfft(fft_dow2)

plt.plot(dow2)
plt.plot(filtered_dow2)
plt.xlabel("n")
plt.ylabel("Price")
plt.title("Plot with first 2 % of fourier coeff kept non zero in DFT")
plt.legend([" Smoothened graph by DFT "])
# plt.savefig("Q5-a-filtered.png")
plt.show()

# part - b

fft_cos = dct(dow2)

K_cos = fft_cos.shape[0]

for i in range(int(K_cos * 2 /100) , K_cos):
    fft_cos[i] = 0

filtered_cos  = idct(fft_cos)

plt.plot(dow2)
plt.plot(filtered_cos)
plt.xlabel("n")
plt.ylabel("Price")
plt.title("Plot with first 2 % of fourier coeff kept non zero in DCT")
plt.legend([" Smoothened graph by DCT "])
# plt.savefig("Q5-b-filtered.png")
plt.show()
