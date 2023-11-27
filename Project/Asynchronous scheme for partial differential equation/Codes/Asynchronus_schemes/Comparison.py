import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("dark")

T = 1
L = 1
D = 0.1
C = 1
N = 100
dx = L / N
dt = 0.00001


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

        choice1 = np.random.binomial(n = 1, p = 0.0)
        choice2 = np.random.binomial(n = 1, p = 0.0)

        Map_async[i] = u_async
        
        u_async[0] += D*dt/dx**2 *(u_async[-1] -2*u_async[0] + u_async[1])  + C*(dt/(2*dx))* (u_async[1] - u_async[-1])
        u_async[-1] += D*dt/dx**2 *(u_async[0] -2*u_async[-1] + u_async[-2])  + C*(dt/(2*dx))* (u_async[0] - u_async[-2])
        u_async[1:-1] += D*dt/dx**2 * (u_async[:-2] - 2*u_async[1:-1] + u_async[2:])  + C*(dt/(2*dx))* (u_async[2:] - u_async[:-2])

        # Introducing the irregularities
        if choice1 == 0:
                u_async[P1] = Map_async[i][P1] + D*dt/dx**2 *(Map_async[i][P1 - 1] -2* Map_async[i][P1] + Map_async[i - 5][P1 + 1])  + C*(dt/(2*dx))* (Map_async[i][P1 + 1] - Map_async[i - 5][P1 + 1])    

        if choice1 == 0:        
                u_async[P2] = Map_async[i][P2] + D*dt/dx**2 *(Map_async[i][P2 - 1] -2* Map_async[i][P2] + Map_async[i - 5][P2 + 1])  + C*(dt/(2*dx))* (Map_async[i][P2 + 1] - Map_async[i - 5][P2 + 1]) 



# Actual solution can be found using solving the equation, which we will compare with our numerical results to understnad how the errors evolve for 
# two different method

def func_array(i):
        X = np.linspace(0, L, N + 1)
        return np.exp(- D* (2*np.pi)**2 * i /N_t)* np.sin(2*np.pi* X - C* i / N_t )



plt.plot(X, Map_async[0], color = 'k',  label = 'Asynchronous scheme')
plt.plot(X, Map_async[1000], color = 'k')
plt.plot(X, Map_async[2000], color = 'k')
plt.plot(X, Map_async[3000], color = 'k')
plt.plot(X, Map_async[4000], color = 'k')


plt.plot(X, Map_sync[0], color = 'red',  linestyle = 'dashed', label = 'Synchronous scheme')
plt.plot(X, Map_sync[1000], color = 'red',  linestyle = 'dashed')
plt.plot(X, Map_sync[2000], color = 'red',  linestyle = 'dashed')
plt.plot(X, Map_sync[3000], color = 'red',  linestyle = 'dashed')
plt.plot(X, Map_sync[4000], color = 'red',  linestyle = 'dashed')

plt.title("Asynchronous vs synchronus solution")
plt.ylabel('Temperature')
plt.xlabel('x')
plt.legend()
plt.show()

# plt.plot(X,func_array(0), color = 'blue')


# plt.plot(X, Map_async[0] -func_array(0), color = 'k')
plt.plot(X, Map_async[20] - func_array(20) , color = 'k',  label = 'Asynchronous scheme' )
plt.plot(X, Map_async[50]- func_array(50), color = 'k')
plt.plot(X, Map_async[100]- func_array(100), color = 'k')
plt.plot(X, Map_async[200]- func_array(200), color = 'k')

# plt.plot(X, Map_sync[0] - func_array(0) , color = 'red', linestyle = 'dashed')
plt.plot(X, Map_sync[20]- func_array(20), color = 'red', linestyle = 'dashed', label = 'Synchronous scheme')
plt.plot(X, Map_sync[50]- func_array(50), color = 'red', linestyle = 'dashed')
plt.plot(X, Map_sync[100]- func_array(100), color = 'red', linestyle = 'dashed')
plt.plot(X, Map_sync[200]- func_array(200), color = 'red', linestyle = 'dashed')

plt.title("Asynchronus vs synchronus errors")
plt.ylabel('u - u_a ')
plt.xlabel('x')
plt.legend()
plt.show()


plt.plot(X, Map_async[0] - Map_sync[0] , color = 'k')
plt.plot(X, Map_async[20] - Map_sync[20] , color = 'k')
plt.plot(X, Map_async[50]- Map_sync[50], color = 'k')
plt.plot(X, Map_async[100]- Map_sync[100], color = 'k')
plt.plot(X, Map_async[200]- Map_sync[200], color = 'k')
plt.scatter(2*L/3, 0, color= 'r', label = 'Position of PEs')
plt.scatter(L/3, 0, color= 'r')
plt.legend()
plt.ylabel('u - u_a ')
plt.xlabel('x')
plt.title("Deviation at the PE boundries")
plt.show()

                






 

 