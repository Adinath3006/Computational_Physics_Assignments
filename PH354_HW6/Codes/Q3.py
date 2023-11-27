""" Exercise 3 """

# Note: The results, derivations and comments asked for each questions is in the 'Outputs and Derivation' directory.
# Note: The plots for each of the questions is in the 'Plots and Animations' directory

import sympy as smp
import numpy as np
import sys
import matplotlib.pyplot as plt
sys.path.insert(0,'.')
from modules.RK4_system import *

# Part A

# defining the constants in lorenz equations
sigma = 10
r = 28
b = 8/3

W = smp.symbols('W(0:4)')
# defining the system of differential equations
fsys = [sigma*(W[2]- W[1]) , r*W[1] - W[2] - W[1]*W[3] , W[1]*W[2] - b*W[3]]

# bounds on t
t_init = 0
t_fin = 50
# initial condition 
init = [0 , 1 , 0]
# total intervals
"""Note: Reduce the value of N to obtain the plots faster"""
N = 10000 

# solving the system
soln = system_solver(fsys = fsys, a = t_init, b = t_fin, m = 3, N = N, init = init)

t_plot = np.linspace(t_init, t_fin, N+1)
x_plot = soln[:,0]
y_plot = soln[:,1]
z_plot = soln[:,2]

plt.plot(t_plot, y_plot)
plt.title(f"Lorenz equations")
plt.xlabel("Time")
plt.ylabel("y")
plt.grid()
#plt.savefig("Q3_a.png")
plt.show()

# Part B

plt.plot(x_plot, z_plot)
plt.title(f"Lorenz equations (Strange Attractor)")
plt.xlabel("x")
plt.ylabel("z")
plt.grid()
#plt.savefig("Q3_b.png")
plt.show()