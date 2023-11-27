import numpy as np
import matplotlib.pyplot as plt

t  = 1000000
X = np.zeros(t)
Y = np.zeros(t)
L = 101
X[0] = int( (L-1)/2 )
Y[0] = int( (L-1)/2 )
for i in range(0, t-1):

    if X[i] == L:
        if Y[i] == 0:
            p = np.random.choice([3,4])
        elif Y[i] == L:
            p = np.random.choice([2,3])
        else:
            p = np.random.choice([2,3,4])

    elif X[i] == 0:
        if Y[i] == 0:
            p = np.random.choice([1,4])
        elif Y[i] == L:
            p = np.random.choice([1,2])
        else:
            p = np.random.choice([2,1,4])
    
    else:
        if Y[i] == 0:
            p = np.random.choice([1,3,4])
        elif Y[i] == L:
            p = np.random.choice([1,2,3])
        else:
            p = np.random.choice([1,2,3,4])

    if p == 1:
        X[i + 1] = X[i] + 1
        Y[i + 1] = Y[i]
    elif p == 2:
        X[i + 1] = X[i]
        Y[i + 1] = Y[i] - 1
    elif p == 3:
        X[i + 1] = X[i] - 1
        Y[i + 1] = Y[i]
    else:
        X[i + 1] = X[i]
        Y[i + 1] = Y[i] + 1
            

plt.plot(X,Y)
plt.title("Random walk for  t = 1000000 s")
# plt.savefig("Q3_1000000.png")
plt.show()

