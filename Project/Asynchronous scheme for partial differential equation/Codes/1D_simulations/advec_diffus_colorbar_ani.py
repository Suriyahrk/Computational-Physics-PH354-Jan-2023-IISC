import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import seaborn as sns
sns.set_style("dark")

# Parameters
L = 1.0     # Length of rod (m)
T = 1000 * 0.0001     # Time interval (s)
C = 1       # Coefficient of convections
D = 0.1     # Diffusivity constant (m^2/s)
N = 100     # Number of grid points
dx = L/N    # Grid spacing
dt = 0.0001  # Time step

# Initial condition
x = np.linspace(0, L, N + 1)
u0 = np.sin(2* np.pi*x)

# Set up the plot
fig = plt.figure(figsize = (12, 3))
ax = plt.gca()

u = np.copy(u0)

# For the thinkness of rod
u_2D = np.empty((len(u0)//4, len(u0)))
for j in range(u_2D.shape[0]):
    u_2D[j] = np.copy(u0)
ax.pcolormesh(u_2D)

# setting frequency
f = 60

u = np.copy(u0)

# Define the update function for the animation
def update(i):
    global u
    u_2D = np.empty((len(u0)//4, len(u0)))

    for j in range(f):
        u[0] += D*dt/dx**2 *(u[-1] -2*u[0] + u[1]) + C*(dt/2*dx)* (u[1] - u[-1])
        u[-1] += D*dt/dx**2 *(u[0] -2*u[-1] + u[-2]) + C*(dt/2*dx)* (u[0] - u[-2])
        u[1:-1] += D*dt/dx**2 * (u[:-2] - 2*u[1:-1] + u[2:]) + C*(dt/(2*dx))* (u[2:] - u[:-2])

    for j in range(u_2D.shape[0]):
        u_2D[j] = np.copy(u)
    
    ax.cla()
    ax.pcolormesh(u_2D, vmin = min(u0), vmax = max(u0), cmap= 'jet')
    ax.set_title('Time = {:.3f}'.format(i*f*dt))
    return None

# Initialize the animation
ani = FuncAnimation(fig, update, frames = int(T/dt), interval=1)
# ani.save('animation.gif', writer='pillow', fps=30)

plt.xlabel('Position (m)')
plt.ylabel('Temperature')
plt.show()