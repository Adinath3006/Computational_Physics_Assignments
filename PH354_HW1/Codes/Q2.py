""" Exercise 2 """

""" The time period of a satellite at a height h from the Earth's surface is given by T = ((2*pi)/sqrt(G*M_E))*(R_E+h)**1.5 where 
    G is the Gravitational constant ; M_E is the mass of Earth ; R_E is the Radius of Earth. Thus we can find the height h by 
                                        h = cbrt((G*M_E)*(T/2*pi)**2) - R_E """

from astropy.constants import G, M_earth, R_earth
import numpy as np

# Part A

G = G.value
M_E = M_earth.value
R_E = R_earth.value

T = float(input("Enter the time period of the satellite in seconds:"))

h = np.cbrt((G*M_E)*(T/(2*np.pi))**2) - R_E

if h > 0:
    print("The altitude of the satellite is {:.4f} meters".format(h))
else:
    print("This time period is not physically possible!")

# Part B

""" 1 day (86400 sec) : The altitude of the satellite is 35862994.1977 meters 
    90 minutes (5400 sec) : The altitude of the satellite is 274455.4688 meters
    45 minutes (2700 sec) : This time period is not physically possible!
    
    Thus the trend that we observe here is time period increases with height and there exists a lower bound on T_min such that values 
    of T < T_min are not physically realisable as it implies that h is negative which is against our initial assumption. Thus 45 minutes 
    is one such example of T < T_min """

# Part C

""" The sidereal day is the time required for the Earth to rotate once relative to the background of the stars (which remains fixed) —i.e., 
    the time between two observed passages of a star over the same meridian of longitude. This is 23.94 hours long. However a solar day 
    is when the Earth completes one full rotation with respect to Sun, but it is longer than sidereal day as the Earth also revolves 
    around the Sun so we have to consider the extra rotation for the Earth to reach the initial position. This is 24 hours long. Hence 
    a sidereal day is the true time period of rotation of the Earth
    
    1 sidereal day (86184 sec) : The altitude of the satellite is 35792563.0073 meters
    1 solar day (86400 sec) :  The altitude of the satellite is 35862994.1977 meters 
    
    Thus there is a difference of 70,431.1904 meters 
    
    Hence a geosyncronous satellite is placed at a height of 35792563.0073 meters """
