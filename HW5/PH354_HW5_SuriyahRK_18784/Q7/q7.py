import numpy as np
import matplotlib.pyplot as plt


N = 20
J = 1

def Energy(S):
    E = 0
    for i in range(0, N):
        for j in range(0, N):
            E = E - J*S[i, j]*( S[ int( (i+1) % N ), j] + S[ int( (i-1) % N ), j] + S[i, int( (j-1) % N )] + S[i, int( (j + 1) % N )] )
    return E/2

def magnetization(T, t_max):

    kb = 1
    b = 1 / (kb* T)
    M = np.empty(t_max)

    # Setting up the initial array of random spins
    S = np.random.choice([-1,1], size= (N,N))
    S_ini = np.copy(S)

    # Initializing the value of magnetization
    M[0] =  sum(sum(S))


    for t in range(0, t_max):

        # generating a random position to flip the spin
        x = np.random.randint(0,N)
        y = np.random.randint(0,N)

        # Instead of using the the Energy function to determine the change in energy which will go through all
        # the points in the latice which is highly inefficient we will just calculate the change in energy by 
        # considering the adjacent point

        change_E =  2* J* S[x, y]* (S[ (x + 1) % N , y] + S[ (x - 1) % N , y] + S[x,  (y - 1) % N ] + S[x, (y + 1) % N ])

        # Now we will be using the metropolis acceptance formula whether to accept or reject this change

        if change_E < 0 :
            temp = 1

        else:
            temp = np.random.binomial(1,  np.exp(-b* change_E))

        if temp == 1:
            S[x, y] = - S[x, y]

        M[t] = sum(sum(S))

        # We will try to return the spin matrices at log time scales as most of the time the matrices are in 
        # with spin up or spin down states

        if t <= int(t_max**(1/3)):
            S1 = np.copy(S)
        elif t <= int(t_max**(1/2)):
            S2 = np.copy(S)



    Time = np.arange(t_max)
    plt.plot(Time, M)
    plt.xlabel("Time")
    plt.ylabel("Magnetization")
    plt.title(f" Magnetization profile for t = {t_max} s ")    
    # plt.savefig(f"Q7_{t_max}_T={T}.png")
    plt.show()

    return S_ini, S1, S2, S



def splot(T, t_max, temperature):

    S_ini = T[0]
    S1 = T[1]
    S2 = T[2]
    S = T[3]

    M_sign = np.sign(np.sum(S))

    fig, axs = plt.subplots(2, 2, figsize= (8,8))

    axs[0,0].pcolormesh(S_ini)
    axs[0,0].set_title(" t = 0")

    axs[0,1].pcolormesh(S1)
    axs[0,1].set_title(f" t = {int(t_max**(1/3))}")

    axs[1,0].pcolormesh(S2)
    axs[1,0].set_title(f" t = {int(t_max**(1/2))}")

    axs[1,1].pcolormesh(S * M_sign)
    axs[1,1].set_title(f"t = {t_max}")

    plt.subplots_adjust(wspace=0.3, hspace=0.3)

    fig.suptitle(f"Temperature = {temperature}, t_max = {t_max}")
    # plt.savefig(f"Q7_part_e_{t_max}_T={temperature}.png")
    plt.show()


t_max = 1000000

for i in range(1,4):

    T = magnetization(i, t_max)
    splot(T, t_max, i)


"""
Note: The program takes atleast 2 mins to run
"""

# part - d 

"""
Observation:

Running the program several times we can see the the system after t = 10**6 s either has a completely positive magnetization 
or a completely negative magnetization. Which we would expect as the group of atoms having similar spins will also force the nearby 
atoms to have a simliar spin and eventually they will all have spin pointing in the same direction. Either all up or all down

"""
# part - e
"""
Observation:

As the temperature is increased, the randomness in the spin direction increases even after applying the Metropolis acceptance formula.
This means that at higher temperatures, there is a higher probability of spins randomly flipping, resulting in more diverse regions of
spins.This behavior can be described as more chaotic, as the system becomes more disordered and unpredictable with increasing
temperature.
"""





    