import numpy as np
import matplotlib.pyplot as plt

# part - a

L = 201
anchored_particles = []
no_of_particles = 1000
it_max = 1000

while ( [int((L - 1)/2) , int((L - 1)/2) ] not in anchored_particles) :
    X = int( (L - 1) / 2)
    Y = int( (L - 1) / 2)

    for i in range(0, it_max):
        
        if X == L:
            anchored_particles.append([X, Y])
            break
        elif X == 0:
            anchored_particles.append([X, Y])
            break
        elif Y == 0:
            anchored_particles.append([X, Y])
            break
        elif Y == L:
            anchored_particles.append([X, Y])
            break
        elif [X + 1, Y] in anchored_particles:
            anchored_particles.append([X,Y])
            break
        elif [X - 1, Y] in anchored_particles:
            anchored_particles.append([X, Y])
            break
        elif [X, Y + 1] in anchored_particles:
            anchored_particles.append([X, Y])
            break
        elif [X, Y - 1] in anchored_particles:
            anchored_particles.append([X, Y])
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
plt.title("Modified DLA")
plt.colorbar()
# plt.savefig("ModifiedDLA.png")
plt.show()

"""
Note: The Older particles are blusih while the newer particles are yellowish
"""





        


            