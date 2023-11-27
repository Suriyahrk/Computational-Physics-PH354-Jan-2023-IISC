import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("dark")

def Error_func(No_of_gridpoints, p_given = 0.0, time_step = 10**(-5)):
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

    # Choosing two boundries in the interval
    P1 = N//3
    P2 = 2* N//3

    for i in range(N_t):

        # two choices for 2 PEs
        choice1 = np.random.binomial(n = 1, p = p_given)
        choice2 = np.random.binomial(n = 1, p = p_given)

        Map[i] = u
        
        # Periodic boundry condition
        u[0] += D*(dt/(dx**2)) *(u[-1] -2*u[0] + u[1])  + C*(dt/(2*dx))* (u[1] - u[-1])
        u[-1] += D*(dt/(dx**2)) *(u[0] -2*u[-1] + u[-2])  + C*(dt/(2*dx))* (u[0] - u[-2])

        # Interior points without async
        u[1:-1] += D*(dt/(dx**2))* (u[:-2] - 2*u[1:-1] + u[2:])  + C*(dt/(2*dx))* (u[2:] - u[:-2])

        # Introducing delays
        if choice1 == 0:
                u[P1] = Map[i][P1] + D*(dt/(dx**2)) *(Map[i][P1 - 1] -2* Map[i][P1] + Map[i - 1][P1 + 1])  + C*(dt/(2*dx))* (Map[i - 1][P1 + 1] - Map[i][P1 - 1])    

        if choice2 == 0:        
                u[P2] = Map[i][P2] + D*(dt/(dx**2)) *(Map[i][P2 - 1] -2* Map[i][P2] + Map[i - 1][P2 + 1])  + C*(dt/(2*dx))* (Map[i - 1][P2 + 1] - Map[i][P2 - 1]) 


    # Actual solution can be found by solving the equation, which we will compare with our numerical results to understnad how the errors evolve for 
    # two different method

    def func_array(i):
            X = np.linspace(0, L, N + 1)
            return np.exp(- D* (2*np.pi)**2 * i /N_t)* np.sin(2*np.pi* X - C* i / N_t )
    

    t_point  = 10

    Error = np.linalg.norm(Map[t_point]- func_array(t_point))/ No_of_gridpoints
    
    return Error


L = 10

NG = [100, 200, 300, 400, 500, 600, 700]
ng = len(NG)
# Recovering order
t = []

for i in range(0, ng ):
    t.append( (L / NG[i])**3 )


Error_p0 = np.zeros(ng)
Error_p1 = np.zeros(ng)
Error_p2 = np.zeros(ng)

for i in range(0, ng):
    Error_p0[i] = Error_func(NG[i], p_given=0, time_step=t[i])
    Error_p1[i] = Error_func(NG[i], p_given=0.5, time_step=t[i])
    Error_p2[i] = Error_func(NG[i], p_given=1, time_step=t[i])
    


slope1, intercept1 = np.polyfit(np.log(NG), np.log(Error_p0), 1 )

slope2, intercept2 = np.polyfit(np.log(NG), np.log(Error_p1), 1 )

slope3, intercept3 = np.polyfit(np.log(NG), np.log(Error_p2), 1 )



plt.plot(np.log10(NG), slope1* np.log10(NG) + intercept1, color = 'r' )
plt.plot(np.log10(NG), slope2* np.log10(NG) + intercept2, color = 'b' )
plt.plot(np.log10(NG), slope3* np.log10(NG) + intercept3, color = 'm')
plt.plot(np.log10(NG), -2* np.log10(NG) + 6, color = 'k', linestyle = 'dashed', label = 'Slope  = -2')


plt.xlabel("log10(N)")
plt.ylabel("log10(Avg(E))")
plt.title("Recovering the order of error lost in asynchronous schemes")
plt.legend()
plt.show()
    

