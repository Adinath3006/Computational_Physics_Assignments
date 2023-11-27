""" Exercise 6 """

""" The semi-major axis a is given by a = 1/((2/l1) - (v1**2/(G*Mass_Sun))) using which we find the eccentricity e = 1 - l1/a"""

import numpy as np
from astropy.constants import G, M_sun

Mass_Sun = M_sun.value
G = G.value

l1 = float(input("Enter the perihelion distance (in m): "))
v1 = float(input("Enter the perihelion velocity at perihelion (in m/s): "))

semi_major = 1/((2/l1) - (v1**2/(G*Mass_Sun)))
ecc = 1 - l1/semi_major
l2 = semi_major*(1+ecc)
v2 = l1*v1/l2

"""The extra factor 3.15576e7 is divided to obtain T in years"""

T = np.sqrt(4*np.pi**2/(G*Mass_Sun)*semi_major**3)/3.15576e7

print("The Aphelion distance: {:.4f} m".format(l2))
print("The Aphelion velocity: {:.4f} m/s".format(v2))
print("The Orbital period: {:.4f} year".format(T))
print("The Eccentricity: {:.4f}".format(ecc))

"""
    Earth:
    The Aphelion distance: 152111350728.5926 m
    The Aphelion velocity: 29289.1864 m/s
    The Orbital period: 1.0001 year
    The Eccentricity: 0.0167
    
    Hailey's Comet:
    The Aphelion distance: 5371566481143.3535 m
    The Aphelion velocity: 891.5988 m/s
    The Orbital period: 77.9457 year
    The Eccentricity: 0.9678"""