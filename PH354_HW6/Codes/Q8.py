""" Exercise 8 """

# Note: The results, derivations and comments asked for each questions is in the 'Outputs and Derivation' directory.
# Note: The plots for each of the questions is in the 'Plots and Animations' directory

import sys
import numpy as np
sys.path.insert(0,'.')
from modules.rk4_system_numerical import *
from modules.adaptive_rk4 import *
from scipy.constants import G 
import matplotlib.pyplot as plt

# Part A

M = 1.98e+30 # kg

""" W--> W[0] = t, W[1] = x, W[2] = y, W[3] = dx_dt, W[4] = dy_dt"""

def f1(W):
    return W[3]

def f2(W):
    return W[4]

def f3(W):
    r = np.sqrt(W[1]**2 + W[2]**2)
    return -G*M*W[1]/r**3

def f4(W):
    r = np.sqrt(W[1]**2 + W[2]**2)
    return -G*M*W[2]/r**3

fsys = [f1, f2, f3, f4]

# Part B

init = [4e+12,0,0,500]
a = 0 # sec
b = 100*365*24*60*60 # sec
for i in [0.01,0.001,0.0005]:
    h = i*365*24*60*60
    N = int((b-a)/h)

    soln = system_solver(fsys=fsys, a=a, b=b, m=4, N=N, init=init)

    plt.plot(soln[:, 0], soln[:, 1])
    plt.xlabel(" x")
    plt.ylabel(" y")
    plt.title(f"Cometary Orbits, step h = {i}")
    plt.grid()
    plt.savefig(f"Q8_b_fixed_step_h_{i}.png")
    plt.show()
    
# Part C

delta = 1000/(365*24*60*60)

x, soln, h = adaptive_rk4(fsys=fsys, a=a, b=b, init=init, h_init=0.001*365*24*60*60, eps=delta)

plt.plot(soln[:, 0], soln[:, 1])
plt.xlabel(" x")
plt.ylabel(" y")
plt.title("Cometary Orbits, adaptive step")
plt.grid()
plt.savefig("Q8_c_adaptive_step.png")
plt.show()

# Part D

plt.plot(soln[:, 0], soln[:, 1],'.')
plt.xlabel(" x")
plt.ylabel(" y")
plt.title("Cometary Orbits, adaptive step")
plt.grid()
plt.savefig("Q8_d_adaptive_step_scatter.png")
plt.show()