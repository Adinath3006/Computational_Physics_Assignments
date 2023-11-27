""" Exercise 2 """

# Note: The results, derivations and comments asked for each questions is in the 'Outputs and Derivation' directory.
# Note: The plots for each of the questions is in the 'Plots and Animations' directory

import sympy as smp
import numpy as np
import sys
import matplotlib.pyplot as plt
sys.path.insert(0,'.')
from modules.RK4_system import *

# Part A

# defining the constants in lotka-volterra equations
alpha = 1
beta = 0.5
gamma = 0.5
delta = 2

W = smp.symbols('W(0:3)')
# defining the system of differential equations
fsys = [alpha*W[1] - beta*W[1]*W[2] , gamma*W[2]*W[1] - delta*W[2]]

# bounds on t
t_init = 0
t_fin = 30
# initial condition 
init = [2 , 2]
# total intervals
N = 1000

# solving the system
soln = system_solver(fsys = fsys, a = t_init, b = t_fin, m = 2, N = N, init = init)

t_plot = np.linspace(t_init, t_fin, N+1)
x_plot = soln[:,0]
y_plot = soln[:,1]

plt.plot(t_plot,y_plot,label = 'fox population')
plt.plot(t_plot,x_plot,label = 'rabbit population')
plt.title(f"Lotka-Volterra Model")
plt.xlabel("Time")
plt.ylabel("Population")
plt.legend()
plt.grid()
#plt.savefig("Q2.png")
plt.show()
