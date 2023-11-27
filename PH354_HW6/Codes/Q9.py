""" Exercise 9 """

# Note: The results, derivations and comments asked for each questions is in the 'Outputs and Derivation' directory.
# Note: The plots for each of the questions is in the 'Plots and Animations' directory

import numpy as np
import sys
import matplotlib.pyplot as plt
sys.path.insert(0,'.')
from modules.leap_frog_method import *

a = 0
b = 50
h = 0.001
N = int((b-a)/h)

y_init = [1, 0]
half_y_init = []
"""Note that the initial conditions for the half_y_init case was found using the Eulers method"""
half_y_init.append(y_init[0] + 0*h/2)
half_y_init.append(y_init[1] + (-1-5)*(h/2)) # here (-1-5) is the value of d^x/dt^2 at t = 0

# defining the system
def f1(t, x):
    return x[1]

def f2(t, x):
    return x[1]**2 - x[0] -5

fsys = [f1, f2]

x,y = leap_frog(fsys,a,b,y_init,half_y_init,N)

plt.plot(x, y[:,0])
plt.xlabel("t")
plt.ylabel("x")
plt.title("Leap Frog Method")
plt.grid()
plt.savefig("Q9.png")
plt.show()