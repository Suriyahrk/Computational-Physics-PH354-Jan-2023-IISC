import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("dark")

def Error_func(No_of_gridpoints, time_step, p_given = 0.0):
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

        # Introducing the irregularities
        if choice1 == 0:
                u_async[P1] = Map_async[i][P1] + D*dt/dx**2 *(Map_async[i][P1 - 1] -2* Map_async[i][P1] + Map_async[i - 1][P1 + 1])  + C*(dt/(2*dx))* (Map_async[i-1][P1 - 1] - Map_async[i][P1 + 1])    

        if choice2 == 0:        
                u_async[P2] = Map_async[i][P2] + D*dt/dx**2 *(Map_async[i][P2 - 1] -2* Map_async[i][P2] + Map_async[i - 1][P2 + 1])  + C*(dt/(2*dx))* (Map_async[i-1][P2 - 1] - Map_async[i][P2 + 1]) 

    # Actual solution can be found using solving the equation, which we will compare with our numerical results to understnad how the errors evolve for 
    # two different method

    def func_array(i):
            X = np.linspace(0, L, N + 1)
            return np.exp(- D* (2*np.pi)**2 * i /N_t)* np.sin(2*np.pi* X - C* i / N_t )
    

    n = len(Map_sync)
    t_point  = 10 # point at which we are calculating the error

    Error_sync = np.linalg.norm(Map_sync[t_point] - func_array(t_point))/ No_of_gridpoints
    Error_async = np.linalg.norm(Map_async[t_point]- func_array(t_point))/ No_of_gridpoints 
    
    return Error_sync, Error_async


NO_grids = np.array([800, 900, 1000, 1200])

n_p = len(NO_grids)


sync1 = np.zeros(n_p)
async1 = np.zeros(n_p)
sync2 = np.zeros(n_p)
async2 = np.zeros(n_p)
sync3 = np.zeros(n_p)
async3 = np.zeros(n_p)


for i in range (0, n_p ):
    x1, y1 = Error_func(NO_grids[i], 10**(-4))
    sync1[i] = x1
    async1[i] = y1
    x2, y2 = Error_func(NO_grids[i], 5*10**(-5))
    sync2[i] = x2
    async2[i] = y2
    x3, y3 = Error_func(NO_grids[i], 10**(-5))
    sync3[i] = x3
    async3[i] = y3


plt.plot(np.log(NO_grids), np.log(sync1), color = 'r')
plt.plot(np.log(NO_grids), np.log(sync1), marker = 'o',  color = 'r')
plt.plot(np.log(NO_grids), np.log(sync2), color = 'r')
plt.plot(np.log(NO_grids), np.log(sync2), marker = 's', color = 'r')
plt.plot(np.log(NO_grids), np.log(sync3), color = 'r')
plt.plot(np.log(NO_grids), np.log(sync3), marker = 'D',  color = 'r')

plt.plot(np.log(NO_grids), np.log(async1), color = 'b')
plt.plot(np.log(NO_grids), np.log(async1),'o',  color = 'b')
plt.plot(np.log(NO_grids), np.log(async2), color = 'b')
plt.plot(np.log(NO_grids), np.log(async2), marker = 's', color = 'b')
plt.plot(np.log(NO_grids), np.log(async2), color = 'b')
plt.plot(np.log(NO_grids), np.log(async3), marker = 'D',  color = 'b')


plt.xlabel("No of grid points (log scale)")
plt.ylabel("Average Error (log scale) ")
plt.title("Behabiour of error in large values of Grid points")
plt.show()

"""
Although there will be errors due to double scalar overflow while generating the plot, the plot itself will still be generated. 
"""



    