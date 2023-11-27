""" Exercise 5 """

# Note: The results, derivations and comments asked for each questions is in the 'Outputs and Derivation' directory.
# Note: The plots for each of the questions is in the 'Plots and Animations' directory

import numpy as np
import sys
import matplotlib.pyplot as plt
sys.path.insert(0,'.')
from modules.rk4_system_numerical import *

# Part A

# defining the constants in the system 
R = 8e-2 # in m
rho = 1.22 # kg-m^-3
C = 0.47
m = 1 # in m
K = (np.pi*R**2*C*rho)/(2*m) # SI units
g = 9.8 # m-s^-2

# defining the system of differential equations
def f1(W):
    return W[3]

def f2(W):
    return W[4]

def f3(W):
    return -K*W[3]*((W[3]**2 + W[4]**2)**(0.5))

def f4(W):
    return - g - K*W[4]*((W[3]**2 + W[4]**2)**(0.5))

fsys = [f1, f2, f3, f4]

# bounds on t
t_init = 0
t_fin = 30
# initial condition 
init = [0 , 0 , 50*np.sqrt(3) , 50]
# total intervals
N = 500 

# solving the system
soln = system_solver(fsys = fsys, a = t_init, b = t_fin, m = 4, N = N, init = init)

x_plot = soln[:,0]
y_plot = soln[:,1]

plt.plot(x_plot, y_plot)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Trajectory')
plt.grid()
#plt.savefig('Q5.png')
plt.show()

# Plot for different masses

for k in [1,2,3]:
    K = (np.pi*R**2*C*rho)/(2*k)
    def f1(W):
        return W[3]

    def f2(W):
        return W[4]

    def f3(W):
        return -K*W[3]*((W[3]**2 + W[4]**2)**(0.5))

    def f4(W):
        return - g - K*W[4]*((W[3]**2 + W[4]**2)**(0.5))

    fsys = [f1, f2, f3, f4]
    
    soln = system_solver(fsys = fsys, a = t_init, b = t_fin, m = 4, N = N, init = init)

    x_plot = soln[:,0]
    y_plot = soln[:,1]

    plt.plot(x_plot, y_plot)
    
plt.xlabel('x')
plt.ylabel('y')
plt.title('Trajectory')
plt.legend(['m=1','m=2','m=3'])
plt.grid()
#plt.savefig('Q5_different_mass.png')
plt.show()