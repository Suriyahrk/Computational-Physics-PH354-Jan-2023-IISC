import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D
import seaborn as sns

sns.set_style("dark")

# Set the dimensions of the plate
length = 1.0
width = 1.0
height = 1.0
dx = 0.1
dy = 0.1
dz = 0.1
Nx = int(length/dx)
Ny = int(width/dy)
Nz = int(height/dz)
D = 0.01

C_x = 1
C_y = 0
C_z = 0

# Set the initial temperature distribution of the plate
T0 = np.zeros((Nz, Ny, Nx))

X = np.linspace(0, length, Nx)
Y = np.linspace(0, width, Ny)
Z = np.linspace(0, height, Nz)

for i in range(0, Nz):
    for j in range(0, Ny):
        for k in range(0, Nx):
            T0[i][j][k] = np.sin(2*np.pi*X[k] / length)*np.sin(2*np.pi*Y[j]/ width)*np.sin(2*np.pi*Z[i]/height)

# Set the time step and the total simulation time
dt = 0.0001
t_final = 1000* 0.0001

Nt = int(t_final/dt)  # number of time steps

# set up plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.grid(False)
X, Y, Z = np.meshgrid(X, Y, Z, indexing='ij')
im = ax.scatter(X, Y, Z, c=T0.flatten(), cmap='jet')

f = 100 # frequency

T = np.copy(T0)

def update(i):
    global T

    # Advection-Diffusion equation
    for j in range(f):
        diff_x = (D*dt/dx**2) * (T[:, :, 2:] - 2*T[:, :, 1:-1] + T[:, :, :-2])
        diff_y = (D*dt/dy**2) * (T[:, 2:, :] - 2*T[:, 1:-1, :] + T[:, :-2, :])
        diff_z = (D*dt/dz**2) * (T[2:, :, :] - 2*T[1:-1, :, :] + T[:-2, :, :])
        
        advec_x = C_x * (dt/(2*dx)) * (T[:, :, 2:] - T[:, :, :-2])
        advec_y = C_y * (dt/(2*dy)) * (T[:, 2:, :] - T[:, :-2, :])
        advec_z = C_z * (dt/(2*dz)) * (T[2:, :, :] - T[:-2, :, :])
        
        T[:, :, 1:-1] += diff_x + advec_x
        T[:, 1:-1, :] += diff_y + advec_y
        T[1:-1, :, :] += diff_z + advec_z

    # Update plot
    im.set_array(T.flatten())
    ax.set_title('Time = {:.2f}'.format(i*f*dt))
    return [im]


ani = FuncAnimation(fig, update, frames=Nt, blit=True, interval=10)

plt.xlabel('X')
plt.ylabel('Y')
ax.set_zlabel('Z')
plt.show()