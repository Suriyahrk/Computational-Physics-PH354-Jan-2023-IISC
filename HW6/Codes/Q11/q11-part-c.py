import numpy as np
import matplotlib.pyplot as plt
import sys
sys.path.insert(0, '.')
from Methods.Runge_katta_system import Runge_Katta_system
from Methods.Integration_techniques import CT
import scipy.constants as sc


# anharmonic oscillator
hbar = sc.h /(2* np.pi)
m = sc.electron_mass
V_0 = 50*sc.electron_volt
a  = 10**(-11) 

x_ini = -10*a
x_final = 10*a
h = 0.01* a
n_sys = 2
Initial_conditions = [0, 1]

# writing a function that will output the value of the wavefunction at the endpoint
def Allowed_energies(E):

    def f1(x, Y):
        return Y[1]

    def f2(x, Y):
        return -(E - V_0 *(x/a)**4)* Y[0]* 2*m/hbar**2 

    System_ODE = [f1, f2]

    x, Y = Runge_Katta_system(x_ini, x_final, h, n_sys, System_ODE, Initial_conditions )

    return x, Y[:,0]

E_0 = 205.30182919363594* sc.electron_volt
E_1 = 735.6730598457116* sc.electron_volt
E_2 = 1443.5337139574522* sc.electron_volt

X_0, Y_0 = Allowed_energies(E_0)
X_1, Y_1 = Allowed_energies(E_1)
X_2, Y_2 = Allowed_energies(E_2)


def plot_graph(X, Y, flip):
    n = len(X)
    temp = X[X < 0]
    N1 = CT(X[0], temp[-1], Y[X < 0]**2, len(temp) - 1)

    # Normalization
    Y = Y / (np.sqrt(2* N1))

    Y_cor = np.zeros(n)

    if flip :
        for i in range(0, n//2):
            Y_cor[i] = Y[i] 
            Y_cor[n - i - 1] = -Y[i]
    
    else:
        for i in range(0, n//2):
            Y_cor[i] = Y[i] 
            Y_cor[n - i - 1] = Y[i]

    plt.plot(X, Y_cor)

N = len(X_0)



plot_graph(X_0[N//4:3*N//4], Y_0[N//4:3*N//4], 0)
plot_graph(X_1[N//4:3*N//4], Y_1[N//4:3*N//4], 1)
plot_graph(X_2[N//4:3*N//4], Y_2[N//4:3*N//4], 0)
plt.xlabel("x - axis")
plt.ylabel("Wavefunction")
plt.legend([" Ground state", "First excited state", "Second Excited state"])
# plt.savefig("Q11-part-11.png")
plt.show()


"""
Explanation :
    We observe that the value of the wavefunction in the few elements of the array blows up, this can be explained as an underflow error,
    as the wavefunction becomes increasingly smaller and smaller, hence causing python to underfow.

"""