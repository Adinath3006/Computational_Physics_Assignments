""" Exercise 12 """

# Note: The results, derivations and comments asked for each questions is in the 'Outputs and Derivation' directory.
# Note: The plots for each of the questions is in the 'Plots and Animations' directory

import numpy as np
import matplotlib.pyplot as plt
import sys
sys.path.insert(0, '.')
from modules.adaptive_rk4 import *

G = 1
t_init = 0
t_final = 2
h_ini = 0.001
delta = 10**(-3)
m1 = 150
m2 = 200
m3 = 250

init = np.array([3, 1, -1, -2, -1, 1, 0, 0, 0, 0, 0, 0])

# Defining the functions

def f1(W):
    return W[7]

def f2(W):
    return W[8]

def f3(W):
    return W[9]

def f4(W):
    return W[10]

def f5(W):
    return W[11]

def f6(W):
    return W[12]

def f7(W):
    r1 = np.sqrt( (W[3] - W[1])**2 + (W[4] - W[2])**2 )
    r2 = np.sqrt( (W[5] - W[1])**2 + (W[6] - W[2])**2 )
    return G* m2* (W[3] - W[1])/(r1)**3 + G* m3* (W[5] - W[1])/(r2)**3

def f8(W):
    r1 = np.sqrt( (W[3] - W[1])**2 + (W[4] - W[2])**2 )
    r2 = np.sqrt( (W[5] - W[1])**2 + (W[6] - W[2])**2 )
    return G* m2* (W[4] - W[2])/(r1)**3 + G* m3* (W[6] - W[2])/(r2)**3

def f9(W):
    r1 = np.sqrt( (W[3] - W[1])**2 + (W[4]- W[2])**2 )
    r2 = np.sqrt( (W[5] - W[3])**2 + (W[6] - W[4])**2 )
    return G* m1* (W[1] - W[3])/(r1)**3 + G* m3* (W[5] - W[3])/(r2)**3

def f10(W):
    r1 = np.sqrt( (W[3] - W[1])**2 + (W[4]- W[2])**2 )
    r2 = np.sqrt( (W[5] - W[3])**2 + (W[6] - W[4])**2 )
    return G* m1* (W[2] - W[4])/(r1)**3 + G* m3* (W[6] - W[4])/(r2)**3

def f11(W):
    r1 = np.sqrt( (W[5] - W[1])**2 + (W[6] - W[2])**2 )
    r2 = np.sqrt( (W[5] - W[3])**2 + (W[6] - W[4])**2 )
    return G* m1* (W[1] - W[5])/(r1)**3 + G* m2* (W[3] - W[5])/(r2)**3

def f12(W):
    r1 = np.sqrt( (W[5] - W[1])**2 + (W[6] - W[2])**2 )
    r2 = np.sqrt( (W[5] - W[3])**2 + (W[6] - W[4])**2 )
    return G* m1* (W[2] - W[6])/(r1)**3 + G* m2* (W[4] - W[6])/(r2)**3

fsys = [f1, f2, f3, f4, f5, f6 ,f7, f8, f9, f10, f11, f12]

x, y, h = adaptive_rk4(fsys=fsys, a = t_init, b=t_final, init=init,  h_init=h_ini, eps= delta)

plt.plot(y[:, 0], y[:, 1],label='planet 1')
plt.scatter(y[:, 0][-1], y[:, 1][-1])
plt.plot(y[:, 2], y[:, 3],label='planet 2')
plt.scatter(y[:, 2][-1], y[:, 3][-1])
plt.plot(y[:, 4], y[:, 5],label='planet 3')
plt.scatter(y[:, 4][-1], y[:, 5][-1])
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid()
plt.title("Three body problem")
plt.savefig("Q12.png")
plt.show()