import numpy as np
import matplotlib.pyplot as plt

# part - a 



def Simulated_annealing(f, total_moves, x_ini, x_max, x_min, Tau,  T_ini, T_final = 0):

    X = np.zeros(total_moves)
    X[0] = x_ini


    for t in range(0, total_moves - 1):

        T = T_ini* np.exp( -t / Tau )
        beta = 1 / T

        # Making sure the temperature doesnt go below the lowest temperature allowed
        if T <= T_final:
            break

        # We will be using normal distribution to pick out our deltas with mean = 0 and standard deviation  = 1

        delta = np.random.normal(loc = 0, scale = 1)

        # Making sure the points remain inside the interval of concern
        if (X[t] + delta >= x_max) or (X[t] + delta <= x_min):
            delta = -delta
        

        if ( f(X[t] + delta) <= f(X[t]) ):
            p = 1
        else:
            change = f(X[t] + delta) - f(X[t]) 
            p = np.random.binomial(1, np.exp( -beta* (change)))

        if p == 1:
            X[t + 1] = X[t] + delta
        else:
            X[t + 1] = X[t]
    
    return X

t_max = 10**5
x_ini = 2
T_ini = 5
Tau = 5*10**3
x_max = 10
x_min = -10

def f(x):
    return x**2 - np.cos(4* np.pi* x)

steps = np.arange(0,t_max)
X = Simulated_annealing(f, t_max, x_ini, x_max, x_min, Tau, T_ini)

print(f" THe minima of the function obtained through Simulated annealing for part - a {X[t_max - 1]}")

plt.plot(steps, X, '.')
plt.xlabel("Steps")
plt.ylabel("Approximation to minima")
plt.title("Progress towards minima as function of no of steps")
# plt.savefig("Q8_part_a.png")
plt.show()

# part - b

def g(x):
    root2 = np.sqrt(2)
    root3 = np.sqrt(3)
    return np.cos(x) + np.cos(root2* x) + np.cos(root3* x)

t_max1 = 10**5
x_ini1 = 10
x_max1 = 50
x_min1 = 0
T_ini1 = 5
Tau1 = 10**4

steps1 = np.arange(t_max)
X1 = Simulated_annealing(g, t_max1, x_ini1, x_max1, x_min1, Tau1, T_ini1)

print(f" THe minima of the function obtained through Simulated annealing for part - b {X1[t_max - 1]}")

plt.plot(steps1, X1, '.')
plt.xlabel("Steps")
plt.ylabel("Approximation to minima")
plt.title("Progress towards minima as function of no of steps")
# plt.savefig("Q8_part_b.png")
plt.show()

"""
Output:

The minima of the function obtained through Simulated annealing for part - a is  1.0041258771731644e-05
The minima of the function obtained through Simulated annealing for part - b is 15.95357418126446

"""













