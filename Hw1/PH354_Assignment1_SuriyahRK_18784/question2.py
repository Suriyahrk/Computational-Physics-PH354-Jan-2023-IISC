import numpy as np
import sympy as smp
import matplotlib as plt


# Q2 - part a)

# The distance of the orbit from a centre of earth for a given time period is given by (GM)**(1/3)*(T/(2*pi))**(2/3)
# Every calculation is done in SI units

T = float(input("Enter the time period of orbit (in sec):" ))

G = 6.6743*10**(-11)  # Newtonian gravitational constant
M = 6*10**24          # Mass of earth
R = 6.38*10**6        # Radius of earth

h = (G*M)**(1/3)*(T/(2*np.pi))**(2/3) - R

print(f"The altitude for a stable circular orbit for a time period {T} sec is {h}")

#  Q2 - part b)

# Altitude for geosynchronus orbit (T = 86400 sec) is 35926611.34 m
# Altitude for time period 90 minutes (T = 5400) is 282873.77 m
# Altitude for time period 45 minutes (T = 2700) is -2182652.54 m (Not possible)

# We can observe that the Altitude for a time period of 45 minutes comes out to be negative, this is due to the fact the earth has a non zero 
# radius and not a point particle so we cannot have orbits with radius lesser than the radius of earth, the smallest possble radius would be the
# radius of earth itself

#  Q2 - part c)

# A sidereal day is defined to be the time taken by earth to rotate about its own axis once with respect to the distant stars or the background
# it is the true time period of Earth's rotation about its axis which is equal to 23.94 hours which is very close to 24 hours. The usual day which
# we follow is the solar day which is the time taken by sun to do 1 complete rotation around us as viewed from earth. As we are also revolving 
# around the sun this time period does reflect the true time period of Earth but involver both rotation and revolution of Earth around the sun

# Altitude for the time period of 1 Solar day (T = 86400 sec) is 35926611.34 m
# Altitude for the time period of 1 Sidereal day (T = 86184sec) is 35856070.91 m

# Height differnce is 70540.43 m

# So for the geosynchronus orbits to be accurate they should be placed at the altitude for sidereal day