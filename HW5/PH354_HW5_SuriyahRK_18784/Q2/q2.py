import numpy as np
import matplotlib.pyplot as plt

Arr_Bi_213 = []
Arr_Pb_209 =[]
Arr_Tl_209 = []
Arr_Bi_209 = []

Bi_213 = 10000
Pb_209 = 0
Tl_209 = 0
Bi_209 = 0

time = 20000
# we will be using the binomial distribution for all the atoms in a time instant  instead of performing bernoulli trials for each atoms

for i in range(0, time):

    decay1 = np.random.binomial(n = Pb_209, p = 2**(-i/ (3.3* 60) )*np.log(2) / (3.3*60), size = 1)
    Pb_209 = Pb_209 - decay1
    Bi_209 = Bi_209 + decay1

    decay2 = np.random.binomial(n = Tl_209, p = 2**(-i/(4.4* 60) )*np.log(2) / (4.4*60), size = 1)
    Tl_209 = Tl_209 - decay2
    Pb_209 = Pb_209 + decay2

    decay3 = np.random.binomial(n = Bi_213, p = 2**(-i/(46* 60) )*np.log(2) / (46*60), size = 1)
    choice = np.random.binomial(n = decay3, p = 2.09 / 100, size=1 )
    
    Bi_213 = Bi_213 - decay3
    Tl_209 = Tl_209 + choice
    Pb_209 = Pb_209 + decay3 - choice

    Arr_Bi_213.append(Bi_213)
    Arr_Bi_209.append(Bi_209)
    Arr_Pb_209.append(Pb_209)
    Arr_Tl_209.append(Tl_209)

t = np.arange(1, time + 1)

plt.plot(t, Arr_Bi_213)
plt.plot(t, Arr_Bi_209)
plt.plot(t, Arr_Tl_209)
plt.plot(t, Arr_Pb_209)
plt.xlabel("Time")
plt.ylabel("No of atoms")
plt.title("No of atoms in each species as a function of time")
plt.legend([" Bi_213", " Bi_209", "Tl_209", "Pb_209"])
# plt.savefig("Q2.png")
plt.show()




