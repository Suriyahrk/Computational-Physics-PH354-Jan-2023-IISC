import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("dark")

def Error_func(No_of_gridpoints, p_given = 0.0):
    T = 1
    L = 10
    D = 1
    C = 1
    N = No_of_gridpoints
    dx = L / N
    dt = 10**(-5)

    # We will have only two choices for the PE boundry point, that is either i or i - 1 and the PE boundry is evenly spaced in the interval

    X = np.linspace(0, L, N + 1)
    N_t = int(T / dt)

    u0 = np.sin(2*np.pi* X)

    u_sync = np.copy(u0)
    u_async = np.copy(u0)

    Map_sync = np.zeros((N_t, N + 1))
    Map_async = np.zeros((N_t, N + 1))



    # Choosing two boundries in the interval
    P1 = N//3
    P2 = 2* N//3

    for i in range(N_t):
        Map_sync[i] = u_sync 
        u_sync[0] += D*dt/dx**2 *(u_sync[-1] -2*u_sync[0] + u_sync[1])  + C*(dt/(2*dx))* (u_sync[1] - u_sync[-1])
        u_sync[-1] += D*dt/dx**2 *(u_sync[0] -2*u_sync[-1] + u_sync[-2])  + C*(dt/(2*dx))* (u_sync[0] - u_sync[-2])
        u_sync[1:-1] += D*dt/dx**2 * (u_sync[:-2] - 2*u_sync[1:-1] + u_sync[2:])  + C*(dt/(2*dx))* (u_sync[2:] - u_sync[:-2])

        choice1 = np.random.binomial(n = 1, p = p_given)
        choice2 = np.random.binomial(n = 1, p = p_given)

        Map_async[i] = u_async
        
        u_async[0] += D*dt/dx**2 *(u_async[-1] -2*u_async[0] + u_async[1])  + C*(dt/(2*dx))* (u_async[1] - u_async[-1])
        u_async[-1] += D*dt/dx**2 *(u_async[0] -2*u_async[-1] + u_async[-2])  + C*(dt/(2*dx))* (u_async[0] - u_async[-2])
        u_async[1:-1] += D*dt/dx**2 * (u_async[:-2] - 2*u_async[1:-1] + u_async[2:])  + C*(dt/(2*dx))* (u_async[2:] - u_async[:-2])

        # Introducing the irregularities we are going 10 steps to clearly see the variation in error
        if choice1 == 0:
                u_async[P1] = u_async[P1] + D*dt/dx**2 *(u_async[P1 - 1] -2* u_async[P1] + Map_async[i - 10][P1 + 1])  + C*(dt/2*dx)* (u_async[P1 + 1] - Map_async[i - 10][P1 + 1])    

        if choice2 == 0:        
                u_async[P2] = u_async[P2] + D*dt/dx**2 *(u_async[P2 - 1] -2* u_async[P2] + Map_async[i - 10][P2 + 1])  + C*(dt/2*dx)* (u_async[P2 + 1] - Map_async[i - 10][P2 + 1]) 


    # Actual solution can be found using solving the equation, which we will compare with our numerical results to understnad how the errors evolve for 
    # two different method

    def func_array(i):
            X = np.linspace(0, L, N + 1)
            return np.exp(- D* (2*np.pi)**2 * i /N_t)* np.sin(2*np.pi* X - C* i / N_t )
    

    n = len(Map_sync)
    t_point  = 100

    Error_sync = np.linalg.norm(Map_sync[t_point] - func_array(t_point))/ No_of_gridpoints
    Error_async = np.linalg.norm(Map_async[t_point]- func_array(t_point))/ No_of_gridpoints 
    
    return Error_sync, Error_async


NO_grids = np.array([500, 600, 700, 800, 900, 1000])

n_p = len(NO_grids)
Error_sync = np.zeros(n_p)
Error_async = np.zeros(n_p)
Error_async_3 = np.zeros(n_p)
Error_async_6 = np.zeros(n_p)


for i in range(0, n_p):    
    x1, y1 = Error_func(NO_grids[i])
    Error_sync[i] = x1
    Error_async[i] = y1
    Error_async_3[i] = Error_func(NO_grids[i], 0.3)[1]
    Error_async_6[i] = Error_func(NO_grids[i], 0.6)[1]


slope1, intercept1 = np.polyfit(np.log(NO_grids), np.log(Error_sync), 1 )

slope2, intercept2 = np.polyfit(np.log(NO_grids), np.log(Error_async), 1 )

slope3, intercept3 = np.polyfit(np.log(NO_grids), np.log(Error_async_3), 1 )

slope4, intercept4 = np.polyfit(np.log(NO_grids), np.log(Error_async_6), 1 )




plt.plot(np.log(NO_grids), slope1* np.log(NO_grids) + intercept1, color = 'r')
plt.plot(np.log(NO_grids), slope2* np.log(NO_grids) + intercept2, color = 'm')
plt.plot(np.log(NO_grids), slope3* np.log(NO_grids) + intercept3, color = 'b')
plt.plot(np.log(NO_grids), slope4* np.log(NO_grids) + intercept4, color = 'g')


plt.xlabel("log(N)")
plt.ylabel("log(Avg(E))")
plt.title("Behaviour of error with No of grid points")
plt.legend()
plt.show()
    
"""
The code takes 30 to 60 seconds to generate a plot.
"""
