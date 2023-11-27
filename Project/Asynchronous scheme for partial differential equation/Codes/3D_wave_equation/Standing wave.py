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
c = 1  # wave speed

# Set the initial conditions of the wave equation
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

# Set up plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.grid(False)
X, Y, Z = np.meshgrid(X, Y, Z, indexing='ij')
im = ax.scatter(X, Y, Z, c=T0.flatten(), cmap='jet')

f = 60
T = np.copy(T0)
T_b = np.copy(T0)

# Define the wave equation
def update(i):
    global T
    global T_b

    # Compute second derivatives
    for j in range(f):
        d2udx2 = np.zeros((Nz, Ny, Nx))
        d2udy2 = np.zeros((Nz, Ny, Nx))
        d2udz2 = np.zeros((Nz, Ny, Nx))

        d2udx2[:, :, 1:-1] = (T[:, :, 2:] - 2*T[:, :, 1:-1] + T[:, :, :-2]) / dx**2
        d2udy2[:, 1:-1, :] = (T[:, 2:, :] - 2*T[:, 1:-1, :] + T[:, :-2, :]) / dy**2
        d2udz2[1:-1, :, :] = (T[2:, :, :] - 2*T[1:-1, :, :] + T[:-2, :, :]) / dz**2

        # Compute the Laplacian
        laplace = d2udx2 + d2udy2 + d2udz2

        # Update the solution using the wave equation
        
        temp = T
        T = 2*T - T_b + (dt**2)*c**2 *laplace
        T_b = temp

    # update plot
    im.set_array(T.flatten())
    ax.set_title('Time = {:.2f}'.format(i*f*dt))
    return [im]


ani = FuncAnimation(fig, update, frames=Nt, blit=True, interval=10)


plt.xlabel('X')
plt.ylabel('Y')
ax.set_zlabel('Z')
plt.show()
