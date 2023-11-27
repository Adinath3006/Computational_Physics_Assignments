""" Exercise 4 """

# Note: The results, derivations and comments asked for each questions is in the 'Outputs and Derivation' directory.
# Note: The plots for each of the questions is in the 'Plots and Animations' directory

import sympy as smp
import numpy as np
import sys
import matplotlib.pyplot as plt
sys.path.insert(0,'.')
from modules.rk4_system_numerical import *

# Part A

# defining the constants 
omega = 1

# defining the system of differential equations
def f1(W):
    return W[2]

def f2(W):
    return -omega**2*W[1]

fsys = [f1 , f2]

# bounds on t
t_init = 0
t_fin = 50
# initial condition 
init = [1 , 0]
# total intervals
"""Note: Reduce the value of N to obtain the plots faster"""
N = 1000 

# solving the system
soln = system_solver(fsys = fsys, a = t_init, b = t_fin, m = 2, N = N, init = init)

t_plot = np.linspace(t_init, t_fin, N+1)
x_plot_A = soln[:,0]

plt.plot(t_plot, x_plot_A)
plt.title(f"Standard Oscillator")
plt.xlabel("Time")
plt.ylabel("x(t)")
plt.grid()
#plt.savefig("Q4_a.png")
plt.show()

# Part B

# initial condition
init = [2 , 0]

# solving the system
soln = system_solver(fsys = fsys, a = t_init, b = t_fin, m = 2, N = N, init = init)

x_plot_B = soln[:,0]

plt.plot(t_plot, x_plot_A, label = 'Initial x = 1')
plt.plot(t_plot, x_plot_B, label = 'Initial x = 2')
plt.title(f"Standard Oscillator")
plt.xlabel("Time")
plt.ylabel("x(t)")
plt.grid()
plt.legend()
#plt.savefig("Q4_b.png")
plt.show()

# Part C

# defining the system of differential equations
def f1(W):
    return W[2]

def f2(W):
    return -omega**2*W[1]**3

fsys = [f1 , f2]

# initial condition 1
init = [1 , 0]
# solving the system
soln_C_1 = system_solver(fsys = fsys, a = t_init, b = t_fin, m = 2, N = N, init = init)

# initial condition 2
init = [2 , 0]
# solving the system
soln_C_2 = system_solver(fsys = fsys, a = t_init, b = t_fin, m = 2, N = N, init = init)

x_plot_C_1 = soln_C_1[:,0]
dx_plot_C_1 = soln_C_1[:,1]
x_plot_C_2 = soln_C_2[:,0]

plt.plot(t_plot, x_plot_C_1)
plt.title(f"Anharmonic Oscillator")
plt.xlabel("Time")
plt.ylabel("x(t)")
plt.grid()
#plt.savefig("Q4_c_1.png")
plt.show()

plt.plot(t_plot, x_plot_C_1, label = 'Initial x = 1')
plt.plot(t_plot, x_plot_C_2, label = 'Initial x = 2')
plt.title(f"Anharmonic Oscillator")
plt.xlabel("Time")
plt.ylabel("x(t)")
plt.grid()
plt.legend()
#plt.savefig("Q4_c_1.png")
plt.show()

# Part D

plt.plot(x_plot_B, soln[:,1])
plt.title(f"Harmonic Oscillator: Phase Space")
plt.xlabel("x")
plt.ylabel("dx/dt")
plt.grid()
#plt.savefig("Q4_d_Harmonic.png")
plt.show()

plt.plot(x_plot_C_1, dx_plot_C_1)
plt.title(f"Anharmonic Oscillator: Phase Space")
plt.xlabel("x")
plt.ylabel("dx/dt")
plt.grid()
#plt.savefig("Q4_d_Anharmonic.png")
plt.show()

# Part E

# defining the constants in van der Pol oscillator
omega = 1
mu = 1

W = smp.symbols('W(0:3)')
# defining the system of differential equations
def f1(W):
    return W[2]

def f2(W):
    return mu*(1-W[1]**2)*W[2] - omega**2*W[1]

fsys = [f1 , f2]

# bounds on t
t_init = 0
t_fin = 20
# initial condition 
init = [1 , 0]
# total intervals
"""Note: Reduce the value of N to obtain the plots faster"""
N = 1000 

# solving the system
soln = system_solver(fsys = fsys, a = t_init, b = t_fin, m = 2, N = N, init = init)

t_plot_E = np.linspace(t_init, t_fin, N+1)
x_plot_E = soln[:,0]
dx_plot_E = soln[:,1]

plt.plot(x_plot_E, dx_plot_E)
plt.title(f"van der Pol oscillator: Phase space")
plt.xlabel("x")
plt.ylabel("dx/dt")
plt.grid()
#plt.savefig("Q4_e_1.png")
plt.show()

for u in [1,2,4]:
    # defining the system of differential equations
    def f1(W):
        return W[2]

    def f2(W):
        return u*(1-W[1]**2)*W[2] - omega**2*W[1]

    fsys = [f1 , f2]
    
    # solving the system
    soln = system_solver(fsys = fsys, a = t_init, b = t_fin, m = 2, N = N, init = init)
    
    x_plot_E = soln[:,0]
    dx_plot_E = soln[:,1]
    
    plt.plot(x_plot_E, dx_plot_E, label = f'$\mu = {u}$')
plt.title(f"van der Pol oscillator: Phase space")
plt.xlabel("x")
plt.ylabel("dx/dt")
plt.grid()
plt.legend()
#plt.savefig("Q4_e_2.png")
plt.show()