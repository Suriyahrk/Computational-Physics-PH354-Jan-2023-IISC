import numpy as np
import matplotlib.pyplot as plt
from numpy import cos, sin 


L = 101
anchored_particles = [ [ int( (L-1)/ 2 ), int( (L-1)/ 2 ) ] ]
pi = np.pi
r = 2
Random_choosen_X = []
Random_choosen_Y = []

while (r <= L/4 ):

    theta = np.random.uniform(0, 2*np.pi)

    X = np.ceil(r* cos(theta)) + int( (L-1)/ 2 )
    Y = np.ceil(r* sin(theta)) + int( (L-1)/ 2 )

    Random_choosen_X.append(X)
    Random_choosen_Y.append(Y)

    while (np.sqrt( (X - (int( (L-1)/ 2)) )**2 + (Y - (int( (L-1)/ 2)))**2 ) <= 2*r): 

        if [X + 1, Y] in anchored_particles:
            anchored_particles.append([X, Y])
            r = r + 1
            break
        elif [X - 1, Y] in anchored_particles:
            anchored_particles.append([X, Y])
            r = r + 1
            break
        elif [X, Y + 1] in anchored_particles:
            anchored_particles.append([X, Y])
            r = r + 1
            break
        elif [X, Y - 1] in anchored_particles:
            anchored_particles.append([X, Y])
            r = r + 1
            break
        else:
            pos_directions = [0, 1, 2, 3]
            D = np.random.choice(pos_directions)

            if D == 0 :
                X = X + 1
            elif D == 1 :
                Y = Y - 1
            elif D == 2 :
                X = X - 1
            else:
                Y = Y + 1 


X_anchor = []
Y_anchor = []

N = len(anchored_particles)

for i in range(N):
    X_anchor.append(anchored_particles[i][0])
    Y_anchor.append(anchored_particles[i][1])

xcoords = np.arange(-0.5, L)
ycoords = np.arange(-0.5, L)

Color = np.arange(N)
plt.vlines(xcoords, ymin = -0.6, ymax = L - 0.4, linewidth = 0.1 )
plt.hlines(ycoords, xmin = -0.6, xmax = L - 0.4, linewidth = 0.1 )
plt.scatter(X_anchor, Y_anchor,marker='.', c = Color)
plt.title("Original DLA")
plt.colorbar()
# plt.savefig("OriginalDLA.png")
plt.show()

plt.vlines(xcoords, ymin = -0.6, ymax = L - 0.4, linewidth = 0.1 )
plt.hlines(ycoords, xmin = -0.6, xmax = L - 0.4, linewidth = 0.1 )
plt.scatter(Random_choosen_X,Random_choosen_Y, marker='.', c = 'k')
plt.title("Randomly choosen points on circle r")
plt.colorbar()
# plt.savefig("Random_points_circle.png")
plt.show()

"""
Note: The newer particles are more yellowish whereas the old particles are bluish

Conclusion:
We can see the random points choosen gets aggregated to center, by random walk

"""

    


    
    

