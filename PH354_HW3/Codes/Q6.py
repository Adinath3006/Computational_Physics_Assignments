""" Exercise 6 """

"""The derivation is explained in the file Results.pdf"""

import numpy as np
from scipy.constants import electron_mass, electron_volt, hbar

import sys
sys.path.insert(0,'.')
from res.false_pos import *
from res.RegulaFalsi import *

m = electron_mass
e = electron_volt

w = 1e-9 # m
V = 20 # eV
eps = 0.001 # eV

def even_state(x):
    return np.sqrt((V-x)/x) - np.tan((np.sqrt(2*m*x*e)*w)/(2* hbar))

def odd_state(x):
    return np.sqrt((V-x)/x) + 1/(np.tan((np.sqrt(2*m*x*e)*w)/(2* hbar)))

E0 = (2*np.pi*hbar)**2/(2*e*m*w**2) 

# We use the final inequality which bounds the Energy to bracket the root for our method

for i in range(6):
    if i%2 == 0:
        Emin = (i**2)*E0 + 0.0001
        Emax = ((i+0.5)**2)*E0 - 0.0001
    else:
        Emin = ((i+0.5)**2)*E0 + 0.001
        Emax = ((i+1)**2)*E0 - 0.001
    
    if Emin >= V:
        max_n = i
        break

    if Emax >= V:
        Emax = V

    if i%2 == 0:    
        E = false_p(Emin,Emax,eps,even_state)
        print(f"Energy of {i} state is: {E} eV")
    else:
        E = false_p(Emin,Emax,eps,odd_state)
        print(f"Energy of {i} state is: {E} eV")

print("The number of bound states for the given system is ",max_n)

'''
The root of the equation with relative tolerance of 0.001 is 0.2215915919709077
The number of iterations taken to achieve this value is 372
Energy of 0 state is: 0.2215915919709077 eV
The root of the equation with relative tolerance of 0.001 is 3.3883121584093012
The number of iterations taken to achieve this value is 1
Energy of 1 state is: 3.3883121584093012 eV
The root of the equation with relative tolerance of 0.001 is 6.016798101397323
The number of iterations taken to achieve this value is 1
Energy of 2 state is: 6.016798101397323 eV
The root of the equation with relative tolerance of 0.001 is 19.13287495941614
The number of iterations taken to achieve this value is 4
Energy of 3 state is: 19.13287495941614 eV
The number of bound states for the given system is  4'''