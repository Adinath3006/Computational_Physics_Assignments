""" Exercise 10 """

# Note: The results, derivations and comments asked for each questions is in the 'Outputs and Derivation' directory.
# Note: The plots for each of the questions is in the 'Plots and Animations' directory

import numpy as np
import matplotlib.pyplot as plt
import sys
sys.path.insert(0, '.')
from modules.verlet_method import *
from scipy.constants import G 

# Part A

# Initializing the constants
M = 1.98e+30    

t_init = 0 # sec
t_final = 10*395*24*60*60 # sec 
h = 60*60 # sec
N = int((t_final-t_init)/h)

def f(x,y):
    return np.array([- G*M*y[0]/( y[0]**2 + y[1]**2)**(3/2), - G*M*y[1]/(y[0]**2 + y[1]**2)**(3/2)])

y_init = [1.471e+11,0]
half_v_init = [0,3.028e+4]

t,y,v,half_v = verlet(fsys=f,a=t_init,b=t_final,y_init=y_init,half_v_init=half_v_init,N=N)

plt.plot(y[:, 0], y[:, 1])
plt.xlabel("x")
plt.ylabel("y")
plt.title("Earth's trajectory")
plt.grid()
plt.savefig("Q10_part_a.png")
plt.show()

# Part B

m = 5.9722e+24
x = y[:, 0]
y = y[:, 1]
r = np.sqrt(x**2 + y**2)
vx = v[:, 0]
vy = v[:, 1]

V = -G*M*m/r
T = (1/2)*m*(vx**2 + vy**2)
E = T+V

plt.plot(t, V, label = 'Potential energy')
plt.plot(t, T, label = 'Kinetic energy')
plt.plot(t, E, label = 'Total energy')
plt.xlabel("t")
plt.ylabel("energy(t)")
plt.legend()
plt.grid()
plt.title("Plot of different energies")
plt.savefig("Q10_part_b.png")
plt.show()

# Part C

plt.plot(t[1:], E[1:]) # Omitting the first point as energy is zero in that point
plt.xlabel("t")
plt.ylabel("E(t)")
plt.title("Total Energy")
plt.grid()
plt.savefig("Q10_part_c.png")
plt.show()