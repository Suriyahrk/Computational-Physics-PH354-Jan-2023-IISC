import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import seaborn as sns
sns.set_style("dark")

# Set the dimensions of the plate
length = 1.0
width = 1.0
dx = 0.01
dy = 0.01
Nx = int(length/dx)
Ny = int(width/dy)
D = 1.0

# Set the initial temperature distribution of the plate
T0 = np.zeros((Ny, Nx))

X = np.linspace(0, length, Nx)
Y = np.linspace(0, width, Ny)

for i in range(0, Ny):
    for j in range(0, Nx):
        T0[i][j] = np.sin(2*np.pi*X[j] / length)*np.sin(2*np.pi*Y[i]/ width)

# Set the time step and the total simulation time
dt = 0.00001
t_final = 1000* 0.00001

Nt = int(t_final/dt)  # number of time steps

# set up plot
fig, ax = plt.subplots()
im = ax.imshow(T0, cmap = 'jet')

f = 20 # frequency

T = np.copy(T0)

def update(i):
    global T

    # Diffusion equation
    for j in range(f):
        T[1:-1, 1:-1] += (D*dt/dx**2) * (T[2:, 1:-1] - 2*T[1:-1, 1:-1] + T[:-2, 1:-1]) + (D*dt/dy**2) * (T[1:-1, 2:] - 2*T[1:-1, 1:-1] + T[1:-1, :-2])

    # Update plot
    im.set_data(T)
    ax.set_title('Time = {:.2f}'.format(i*f*dt))
    return [im]


ani = FuncAnimation(fig, update, frames=Nt, blit=True, interval=10)
# ani.save('animation.gif', writer='pillow', fps=60)
plt.xlabel('X')
plt.ylabel('Y')
plt.colorbar(im)
plt.show()
