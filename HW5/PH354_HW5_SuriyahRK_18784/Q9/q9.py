import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as ani

def Dimer_Covering_function( L, no_moves,  T_ini, Cooling  = 0, Tau = 10):

    pos_dimer = []
    coord_pos = []

    fig = plt.figure()
    ax = plt.gca()
    xcoords = np.arange(-0.5, L)
    ycoords = np.arange(-0.5, L)

    # we will define the backgorund lattice at the start upon which the dimers are getting stuck

    def background_lattice():
        ax.set_xlim(-0.6, L - 0.4)
        ax.set_ylim(-0.6, L - 0.4)
        ax.vlines(xcoords, ymin = -0.6, ymax = L - 0.4, linewidth = 0.1 )
        ax.hlines(ycoords, xmin = -0.6, xmax = L - 0.4, linewidth = 0.1 )


    # We will be defining the function that updates the lattice points once every " freq " no of steps are over, wher freq can
    # manually set by us

    freq = 30

    def update_lattice(i):
        for t in range(0, freq):
            if Cooling == True:
                T = T_ini* np.exp( - (i * freq + t) / Tau)
            else:
                T = T_ini

            beta =  1 / T

            # Choosing a random point in the lattice to keep one end of the dimer
            x = np.random.randint(0, L)
            y = np.random.randint(0, L)

            directions = [0, 1, 2, 3]

            # Alloting the possible choice for the second part of the dimer to be in
            if x == 0:
                if y == 0:
                    del directions[2]
                    del directions[1]
                elif y == L:
                    del directions[2]
                    del directions[2]
                else:
                    del directions[2]
            
            elif x == L:
                if y == 0:
                    del directions[0]
                    del directions[0]
                elif y == L:
                    del directions[0]
                    del directions[2]
                else:
                    del directions[0]

            else:
                if y == 0:
                    del directions[1]
                elif y == L:
                    del directions[3]

            # choosing the position of second lattice point

            second_pos = np.random.choice(directions)

            if second_pos == 0 :
                x_second = x + 1
                y_second = y
            elif second_pos == 1:
                x_second = x
                y_second = y - 1
            elif second_pos == 2:
                x_second = x - 1
                y_second = y
            else:
                x_second = x
                y_second = y + 1

            if [[x, y], [x_second, y_second]] in pos_dimer:
                # This exact choice we obtained is already a dimer
                # we use the acceptance formula
                stick = np.random.binomial(1, np.exp(-beta))

                if stick == 1:
                    pos_dimer.remove(  [[x, y], [x_second, y_second]] ) 
                    coord_pos.remove([x, y])
                    coord_pos.remove([x_second, y_second])

            elif [ [x_second, y_second] , [x, y] ] in pos_dimer:
                # This exact choice we obtained is already a dimer
                # we use the acceptance formula
                stick = np.random.binomial(1, np.exp(-beta))

                if stick == 1:
                    pos_dimer.remove( [[x_second, y_second] , [x, y]] ) 
                    coord_pos.remove([x, y])
                    coord_pos.remove([x_second, y_second])


            elif([x,y] not in coord_pos):
                if ( [x_second, y_second] not in coord_pos):
                    # both of the position are free now we are allowed to adda dimer in that position we need
                    # to make sure to add in both of lists dimer_pos and coord_pos

                    pos_dimer.append( [[x, y], [x_second, y_second]] ) 
                    coord_pos.append([x , y])
                    coord_pos.append([x_second, y_second])

        # now we will be fixing our dimers to the axis
        ax.cla()
        ax.vlines(xcoords, ymin = -0.6, ymax = L - 0.4, linewidth = 0.1 )
        ax.hlines(ycoords, xmin = -0.6, xmax = L - 0.4, linewidth = 0.1 )

        for element in pos_dimer:
            x1 = element[0][0]
            x2 = element[1][0]
            y1 = element[0][1]
            y2 = element[1][1]

            ax.plot([x1, x2], [y1, y2], color = 'red', marker = '.', markersize= 5, linewidth = 0.75)

    
    anim = ani.FuncAnimation(fig, update_lattice, frames= no_moves// freq, interval= 10**(-2), init_func= background_lattice, repeat =False )
    plt.show()
    return anim, pos_dimer

animation1, pos_dimer1 = Dimer_Covering_function(50, 10**4, 1, Cooling = False)
# animation1.save(r"Q9_DimerCovering.gif", fps=60)

animation2, pos_dimer2 = Dimer_Covering_function(50, 10**4, 1, Cooling = True, Tau=10**2)
# animation2.save(r"Q9_DimerCovering_cooling_tau=10^2.gif", fps=60)

animation3, pos_dimer3 = Dimer_Covering_function(50, 10**4, 1, Cooling = True, Tau= 10**3)
# animation3.save(r"Q9_DimerCovering_cooling_tau=10^3.gif", fps=60)

print(f"The total number of dimers stuck in no cooling is {len(pos_dimer1)}")
print(f"The total number of dimers stuck in cooling with tau  = 10^3 is {len(pos_dimer2)}")
print(f"The total number of dimers stuck in cooling with tau = 10^2 is  {len(pos_dimer3)}")

"""
Output:
The total number of dimers stuck in no cooling is 955
The total number of dimers stuck in cooling with tau  = 10^2 is 1111
The total number of dimers stuck in cooling with tau = 10^3 is  1118

Note: The program takes a lot of time to load and produce the gifs these are one of runs that was done.

The results show a clear trend where a higher number of dimers adhere to the lattice with exponential cooling,as compared to a constant
temperature.This is expected because higher temperatures provide more energy for the dimers to escape the lattice. Additionally, it can 
be observed that a slower cooling rate, indicated by a higher value of Tau,results in more particles sticking to the lattice than a 
faster cooling rate with a lower value of Tau.

"""







