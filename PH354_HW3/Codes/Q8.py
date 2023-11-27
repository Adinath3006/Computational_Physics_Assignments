""" Exercise 8 """

import numpy as np
import matplotlib.pyplot as plt

import sys
sys.path.insert(0,'.')
from res.secant import *

# Part A

G = 6.674e-11 # m^3kg^-1s^-2
M_e = 5.974e+24 # kg
M_m =  7.348e+22 # kg
R = 3.844e+8 # m
w = 2.662e-6 # s^-1

def f(r):
    return (G*M_e)/(r**2) - (G*M_m)/((R-r)**2) - r*w**2

"""We plot the graph to get an idea of where the root of the equation lies and choose two values which seem to be reasonably close to the
root and they bracket the root in order to reduce the computation time required to compute root, eventhough it can be done for any two 
arbitrary points."""

x = np.linspace(0,R,200)
y = [f(i) for i in x]

plt.plot(x,y)
plt.axhline(0.0,color="black")
plt.title("Lagrange point")
plt.xlabel('r')
plt.ylabel('f(r)')
plt.grid()
#plt.savefig("Q8.png")
plt.show()

"""The root of the above equation lies between 3.822e+8 and 3.825e+8"""

r_L = Secant(3.6e+8,3.825e+8,5e-5,50,f)

print("The distance of the Lagrange point from the center of the Earth is {:.3e} m".format(r_L))

"""The distance of the Lagrange point from the center of the Earth is 3.262e+08 m"""