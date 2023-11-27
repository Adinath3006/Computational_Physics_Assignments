import numpy as np
import sys
import matplotlib.pyplot as plt
sys.path.insert(0,'.')
from modules.rk4_system_numerical import *


# defining the constants in lorenz equations
sigma = 10
r = 28
b = 8/3

def f1(W):
    return sigma*(W[2]- W[1]) 
def f2(W):
    return r*W[1] - W[2] - W[1]*W[3] 
def f3(W):
    return W[1]*W[2] - b*W[3]

fsys = [f1,f2,f3]    
    #fsys = [sigma*(W[2]- W[1]) , r*W[1] - W[2] - W[1]*W[3] , W[1]*W[2] - b*W[3]]    

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


plt.plot(x_plot, z_plot)
plt.title(f"Lorenz equations (Strange Attractor)")
plt.xlabel("x")
plt.ylabel("z")
plt.grid()
#plt.savefig("Q3_b.png")
plt.show()