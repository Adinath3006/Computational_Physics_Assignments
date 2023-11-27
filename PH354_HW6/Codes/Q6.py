""" Exercise 6 """

# Note: The results, derivations and comments asked for each questions is in the 'Outputs and Derivation' directory.
# Note: The plots for each of the questions is in the 'Plots and Animations' directory

import sympy as smp
import numpy as np
import sys
import matplotlib.pyplot as plt
sys.path.insert(0,'.')
from modules.RK4_system import *

# Part A

# Part B

# defining the constants for the system
G = 1
M = 10
L = 2

W = smp.symbols('W(0:5)')
# defining the system of differential equations
r_square = (W[1]**2 + W[2]**2)
fsys = [W[3] , W[4] , -G*M*(W[1])/(r_square*(r_square + L**2/4)**(0.5)) , -G*M*(W[2])/(r_square*(r_square + L**2/4)**(0.5))]

# bounds on t
t_init = 0
t_fin = 10
# initial condition 
init = [1 , 0 , 0 , 1]
# total intervals
"""Note: Reduce the value of N to obtain the plots faster"""
N = 1000 

# solving the system
soln = system_solver(fsys = fsys, a = t_init, b = t_fin, m = 4, N = N, init = init)

t_plot = np.linspace(t_init, t_fin, N+1)
x_plot = soln[:,0]
y_plot = soln[:,1]

plt.plot(x_plot, y_plot)
plt.title(f"Space Garbage Motion")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.savefig("Q6.png")
plt.show()