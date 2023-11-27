import numpy as np

def leap_frog(a, b, h, m, f, s, s_half):

    N = int( (b - a) / h) + 1
    X  = np.zeros(N)
    Y = np.zeros((N, m))
    Y_half = np.copy(Y)

    for i in range(0, N):
        X[i] = a + i*h

    Y[0] = s
    Y_half[0] = s_half

    for i in range(1, N):
        temp1 = np.zeros(m)
        temp2 = np.zeros(m)

        for j in range(0, m):
            temp1[j]  = f[j]( X[i - 1] + h/2, Y_half[i - 1] )

        Y[i] = Y[i - 1] + temp1* h

        for j in range(0, m):
            temp2[j] = f[j]( X[i], Y[i] )

        Y_half[i] = Y_half[i - 1] + h* temp2

    return X, Y
        
           


