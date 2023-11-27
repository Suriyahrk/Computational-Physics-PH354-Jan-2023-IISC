import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("dark")
# Parameters
L = 1.0     # Length of rod (m)
T = 2     # Time interval (s)
D = 0.1     # Diffusivity constant (m^2/s)
N = 100     # Number of grid points
dx = L/N    # Grid spacing
dt = 0.0001 # Time step

# Initial condition
x = np.linspace(0, L, N+1)
u0 = np.sin(np.pi*x)

N_t = int(T/dt)
Map = np.zeros((N_t, N + 1 ))
# Solve the diffusion equation using forward-time central-space (FTCS) method
u = u0.copy()

for i in range(0, N_t):
    Map[i] = u
    u[1:-1] += D*dt/dx**2 * (u[:-2] - 2*u[1:-1] + u[2:])


# Plot the results
plt.plot(x, u0, label='Initial')
plt.plot(x, u, label='Final')

plt.xlabel('Position (m)')
plt.ylabel('Temperature')
plt.legend()
plt.show()

# Plotting the heat map of the rod
plt.pcolormesh(Map, cmap='jet')
plt.colorbar()
plt.show()



