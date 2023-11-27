import numpy as np
import sympy as smp
import matplotlib.pyplot as plt
import pandas as pd

Data = pd.read_csv("stm.txt",sep = " ", header = None)
plt.pcolormesh(Data)
 # plt.pcolormesh(Data,cmap = 'inferno')
plt.title("Density plot for the surfacce of silicon (111) crystal")
plt.show()


plt.pcolormesh(Data,cmap = 'inferno')
plt.title("Density plot for the surfacce of silicon (111) crystal")
plt.show()