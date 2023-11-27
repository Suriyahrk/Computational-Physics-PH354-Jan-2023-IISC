import numpy as np
import sympy as smp
import sys
sys.path.insert(0,'.')
from Methods.Runge_katta_system import Runge_Katta_system
import matplotlib.pyplot as plt
# part - a

"""
Here y[0] = x, and y[1] = y 
Defining the dynamical quantities of the system
"""
y0, y1 = smp.symbols('y0 y1')
alpha = 1
beta = 0.5
gamma = 0.5
delta = 2

# Defining the system of ODE to solve
def f_1(x, Y):
    return alpha* Y[0] - beta* Y[0]* Y[1]

def f_2(x, Y):
    return gamma* Y[0]* Y[1] - delta* Y[1]


System_ODE = [f_1, f_2]
t_ini = 0
t_final = 30
Initial_condition  = [2, 2]
h = 0.001
n_sys = 2

X, Y = Runge_Katta_system(t_ini, t_final, h, n_sys, System_ODE, Initial_condition)

N = X.shape[0] 
rabbit = []
fox = []

for i in range(0, N):
    rabbit.append(Y[i][0])
    fox.append(Y[i][1])

plt.plot(X, rabbit)
plt.plot(X, fox )
plt.xlabel(" Time ")
plt.ylabel(" Population ")
plt.legend(["No of Rabbit", "No of fox"])
plt.title("Evolution of Lotka - Volterra equation")
# plt.savefig("Q2.png")
plt.show()

# part -b

"""
The graphs reveal that there is a recurring pattern in the population of rabbits and foxes. The general trend is such that when the
rabbit population rises, it results in an increase in the fox population as they have more food to consume. However, the peak of the
fox population lags a few time steps behind the peak of the rabbit population, providing time for the fox population to grow.
When the fox population becomes too large and the rabbit population is scarce, the foxes start to die due to lack of food.
This absence of predators for the rabbits causes a boom in their population, thus starting the cycle again. The periodic nature
of this cycle is evident from the graph, and it is interesting to note that the peak of the fox population is slightly
to the left of the peak of the rabbit population, which can be explained through a rough sketch of how the populations behave.

"""