import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("dark")
# Parameters
L = 1.0     # Length of rod (m)
T = 1     # Time interval (s)
D = 0.1     # Diffusivity constant (m^2/s)
N = 100    # Number of grid points
dx = L/N    # Grid spacing
dt = 0.00001  # Time step

x = np.linspace(0, L, N + 1)

# Initial condition

u0 = np.sin(2*np.pi* x)


N_t = int(T/dt)
u = np.copy(u0)
Map = np.zeros((N_t,  N+1))

for i in range(N_t):
    Map[i] = u
    # periodic boundry conditions are enforced

    u[0] += D*dt/dx**2 *(u[-1] -2*u[0] + u[1])  
    u[-1] += D*dt/dx**2 *(u[0] -2*u[-1] + u[-2])  
    u[1:-1] += D*dt/dx**2 * (u[:-2] - 2*u[1:-1] + u[2:])

# line plot
plt.plot(x, u0, label='Initial')
plt.plot(x, u, label='Final')
plt.xlabel('Position (m)')
plt.ylabel('Temperature')
plt.legend()
plt.show()

#P-colormesh showing the evolution along the time axis
plt.pcolormesh(Map, cmap='jet')
plt.colorbar()
plt.show()