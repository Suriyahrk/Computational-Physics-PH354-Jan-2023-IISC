import numpy as np
import pandas as pd
import matplotlib.pylab as plt


# part - a

Data = pd.read_csv("blur.txt", sep=" ", header= None)

N = Data.shape[0] # same x and y dimensions

flip = np.zeros([N,N])

for i in range(0,N):
    for j in np.arange(0,N):
        flip[i][j] = Data[i][N-1-j]

Blur = flip.transpose()    

plt.pcolormesh(Blur, cmap='gray')
plt.title("Original blurred photo")
# plt.savefig("Q8-a.png")
plt.show()

# part - b

sigma = 25
def f(x,y):
    return np.exp(-(x**2 + y**2) / (2* sigma**2 ) )

Point_spread = np.zeros([N,N])

# Defining the point spread function

for i in range(0, N):
    for j in range(0, N):
        if 0 <= i <= N/2 and 0 <= j <= N/2 :
            Point_spread[i][j] = f(i, j) 
        elif 0 <= i <= N/2 and N/2 <= j <= N :
            Point_spread[i][j] = f(i, N - j)
        elif N/2 <= i <= N and 0 <= j <= N/2 :
            Point_spread[i][j] = f(N - i, j)  
        else:
            Point_spread[i][j] = f(N - i, N - j)
            


plt.pcolormesh(Point_spread, cmap='gray')
plt.title("Point spread function")
# plt.savefig("Q8-b.png")
plt.show()

# part - c

e = 10**(-3)

Blur_ft = np.fft.rfft2(Blur)
gaussian_ft = np.fft.rfft2(Point_spread)
a = gaussian_ft.shape[0]
b = gaussian_ft.shape[1]

original_ft = np.zeros([a,b], dtype=np.complex128)

for i in range(0, a):
    for j in range(0, b):
        if gaussian_ft[i][j] <= e :
            original_ft[i][j] = Blur_ft[i][j] / N**2 
        else:
            original_ft[i][j] = Blur_ft[i][j] / (N**2 * gaussian_ft[i][j] )

Original = np.fft.irfft2(original_ft)

plt.pcolormesh(abs(Original),cmap='gray')
plt.title("Deconvoluted unblured image")
# plt.savefig("Q8-c.png")
plt.show()

# Part - d

"""
Explanation:
    The obtained image appears to have some blurriness, which can be attributed to the fact that we have excluded the zeros from
    the Fourier Transform of the Point Spread Function (PSF). Including these zeros can result in Fourier coefficients of the
    deconvoluted image going to infinity, which is not computationally feasible. Thus, obtaining a perfect image from a blurred 
    image is not possible. However, by neglecting the near-zero coefficients, we can still obtain a fairly good approximation,
    as can be seen in the resulting image.
"""
