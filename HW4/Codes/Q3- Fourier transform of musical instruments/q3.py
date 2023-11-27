import numpy as np
from numpy.fft import rfft
import pandas as pd
import matplotlib.pyplot as plt

# part - a

Trumpet_ = pd.read_csv("trumpet.txt", sep= " ", header = None)
piano_ = pd.read_csv("piano.txt", sep= " ", header = None)

"""
The following function FFT_plot will take the fourier transform of a given data and will plot it
"""
Trumpet = np.squeeze(Trumpet_)
piano = np.squeeze(piano_)

def FFT_plot(A, N_plot, name ):

    N = A.shape[0]
    d_ = 1/44100

    plt.plot(A)
    plt.xlabel("n")
    plt.ylabel("Amplitude")
    plt.title(f"waveform of {name}")
    # plt.savefig(f"Q3_{name}.png")
    plt.grid()
    plt.show()

    C_k = np.fft.fft(A)
    f = np.fft.fftfreq(N, d = d_ )

    plt.plot( f[0:N_plot], abs( C_k[0:N_plot] )**2 )
    plt.xlabel("k")
    plt.ylabel("Amplitude")
    plt.title(f"FFT amplitudes of {name}")
    # plt.savefig(f"Q3_FFT_{name}.png")
    plt.grid()
    plt.show()

    return  f[np.argmax( abs(C_k)**2)]
        
freq_max_trumpet = FFT_plot(Trumpet, 10000, "Trumpet" )
freq_max_piano = FFT_plot(piano, 10000, "Piano")

print(f"The frequency corresponding to maximum amplitude in trumpet is {freq_max_trumpet} Hz")
print(f"The frequency corresponding to maximum amplitude in piano is {freq_max_piano} Hz")

# Output

"""
The frequency corresponding to maximum amplitude in trumpet is 1043.847 Hz
The frequency corresponding to maximum amplitude in piano is 524.79 Hz
"""

# part - b

"""
We see the maximum frequency in case of trumpet is higher than that of piano which is expected.

The trumpet is playing the musical note C6 which has a frequency 1046.50 Hz, very close to what we observe.
The piano is playing the musical note C5 which has a frequency 523.25 HZ, very close to what is observed.

"""


    

