import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.animation import FuncAnimation
sns.set_style("dark")

# Parameters
L = 1.0     # Length of rod (m)
T = 1000* 0.0001     # Time interval (s)
C = 1     # Advection constant
D = 0.01    # Diffusivity constant (m^2/s)
N = 100     # Number of grid points
dx = L/N    # Grid spacing
dt = 0.0001 # Time step

# Initial condition
x = np.linspace(0, L, N+1)
u0 = np.sin(2*np.pi*x)

# Set up the plot
fig = plt.figure()
ax = plt.gca()

u = np.copy(u0)
ax.plot(u0)

# Setting frequency
f = 100

# Define the update function for the animation
def update(i):
    global u

    for j in range(f):
        u[0] += D*dt/dx**2 *(u[-1] -2*u[0] + u[1])  + C*(dt/2*dx)* (u[1] - u[-1])
        u[-1] += D*dt/dx**2 *(u[0] -2*u[-1] + u[-2])  + C*(dt/2*dx)* (u[0] - u[-2])
        u[1:-1] += D*dt/dx**2 * (u[:-2] - 2*u[1:-1] + u[2:])  + C*(dt/(2*dx))* (u[2:] - u[:-2])

    ax.cla()
    ax.plot(u)
    ax.set_title('Time = {:.3f}'.format(f*i*dt))
    ax.set_ylim(min(u0), max(u0))
    return None

# Initialize the animation
ani = FuncAnimation(fig, update, frames=int(T/dt), interval=1)

# ani.save('animation.gif', writer='pillow', fps=30)
plt.xlabel('Position (m)')
plt.ylabel('Temperature')
plt.show()
