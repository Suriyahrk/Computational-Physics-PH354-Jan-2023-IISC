import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("dark")

def Error_func(No_of_gridpoints, time_step = 10**(-6)):
    T = 1
    L = 10
    D = 1
    C = 1
    N = No_of_gridpoints
    dx = L / N
    dt = time_step

    # We will have only two choices for the PE boundry point, that is either i or i - 1 and the PE boundry is evenly spaced in the interval
    X = np.linspace(0, L, N + 1)
    N_t = int(T / dt)

    u0 = np.sin(2*np.pi* X)

    u = np.copy(u0)

    Map = np.zeros((N_t, N + 1))

    for i in range(N_t):
        Map[i] = u
        u[0] += D*dt/dx**2 *(u[-1] -2*u[0] + u[1])  + C*(dt/2*dx)* (u[1] - u[-1])
        u[-1] += D*dt/dx**2 *(u[0] -2*u[-1] + u[-2])  + C*(dt/2*dx)* (u[0] - u[-2])
        u[1:-1] += D*dt/dx**2 * (u[:-2] - 2*u[1:-1] + u[2:])  + C*(dt/(2*dx))* (u[2:] - u[:-2])


    # Actual solution can be found by solving the equation, which we will compare with our numerical results to understnad how the errors evolve for 
    # two different method

    def func_array(i):
            X = np.linspace(0, L, N + 1)
            return np.exp(- D* (2*np.pi)**2 * i /N_t)* np.sin(2*np.pi* X - C* i / N_t )
    

    t_point  = 100

    Error = np.linalg.norm(Map[t_point]- func_array(t_point))/ No_of_gridpoints
    
    return Error


NO_grids = np.array([16, 32, 64, 128, 256])

n_p = len(NO_grids)
Error_p0 = np.zeros(n_p)

for i in range(0, n_p):    
    Error_p0[i] = Error_func(NO_grids[i])


slope1, intercept1 = np.polyfit(np.log10(NO_grids), np.log10(Error_p0), 1 )
plt.plot(np.log10(NO_grids), slope1* np.log10(NO_grids) + intercept1, color = 'r')


plt.plot( np.log10(NO_grids), np.log10(Error_p0) ,'.', color = 'r')

print(slope1)
plt.xlabel("log10(N)")
plt.ylabel("log10(Avg(E))")
plt.show()
    

