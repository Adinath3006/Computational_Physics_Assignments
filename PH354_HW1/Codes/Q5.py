""" Exercise 5 """

""" When E > V we can derive the formula for the transmission and reflection coefficients of the wavefunction:

                                t_p = (2*k1)/(k1 + k2) and  r_p = t_p - 1 
                where,      k1 = np.sqrt(2*m*E)/hbar and k2 = np.sqrt(2*m*(E-V))/hbar 

    using this we can finally find the reflection and transmission probabilities of the wavefunction given by:
    
                                    R = r_p**2 and T = (t_p**2)*k2/k1"""
import numpy as np
from scipy.constants import hbar

E = 10
m = 9.11e-31
V = 9

# Momenta
k1 = np.sqrt(2*m*E)/hbar
k2 = np.sqrt(2*m*(E-V))/hbar

# The transmission and reflection coefficients
t_p = (2*k1)/(k1 + k2)
r_p = t_p - 1

# The transmission and reflection probabilities
T = (t_p**2)*k2/k1
R = r_p**2

print("For the given Energy and Step potential the transmission probability is {:.5f} and the reflection probability is {:.5f}".format(T,R))

"""For the given Energy and Step potential the transmission probability is 0.73013 and the reflection probability is 0.26987"""