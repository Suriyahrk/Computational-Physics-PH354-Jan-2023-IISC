import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

Data = pd.read_csv("dow.txt",sep= " ",header= None)

def Filtering_FFT(Arr , name , set_zero ):

    N = Arr.shape[0]
    A = np.squeeze(Arr) # For removing all the 1 - dimensional components of the array
    X =np.linspace(1,N,N)

    plt.plot(X,A)
    plt.xlabel("n")
    plt.ylabel("Price")
    plt.title(f"Initial data of {name}")
    # plt.savefig(f"Q4_{name}.png")
    plt.show()

    C = np.fft.rfft(A)
    K = int(N/2 + 1)

    # Setting the final 90 percent of the data to 0

    for i in range(int( K* set_zero/100), K):
        C[i] = 0
    
    Aprime = np.fft.irfft(C)

    plt.plot(X,A)
    plt.plot(X, Aprime, color = 'red')
    plt.xlabel("n")
    plt.ylabel("Price")
    plt.title(f"Normal and filtered data of {name} for {set_zero} %")
    plt.legend(["Original",f"{set_zero} % smoothening"])
    # plt.savefig(f"Q4_filtered_{name}_{set_zero}%.png")
    plt.show()

    
Filtering_FFT(Data, "dow", 10)
Filtering_FFT(Data, "dow", 2)

"""
Observation:
    We can observe when we set the higher k values to be zero we are basically, setting the amplitudes corresponding to high frequency
    to be zero, high frequency are the ones that gives high intricate detail, while the low frequencies gives the general structure of
    the data (essentially the shape of the graph), thus by setting amplitudes corresponding to high frequencies to zero, we get
    rid of highly chaotic/dynamic behaviour and only retain smooth shape.
"""