""" Exercise 9 """

import math
import numpy as np
import matplotlib.pyplot as plt
import sys
sys.path.insert(0,'.')
from res.Gauss_Quad import *
from scipy.constants import k

# Part A

# Computing the Heat Capacity function using the gaussian quadrature method

def cv(T):

    V = 1000e-6 # in (m^3)
    rho = 6.022e+28 # in (m^-3)
    theta_D  = 428 # in (K)
    N = 50
    k_b = k
    
    def f(x):
        return ((x**4)*(math.e)**x)/((math.e)**x - 1)**2

    val = 0
    x,w = gaussxwab(N,0,theta_D/T)
    for i in range(0,len(x)):
        val += w[i]*f(x[i])

    C_V = 9*V*rho*k_b*(T/theta_D)**3*val

    return C_V

# Part B

T = np.linspace(5,500,100,endpoint=False)
C_V = [cv(temp) for temp in T]

plt.plot(T,C_V)
plt.xlabel('Temperature (in K)')
plt.ylabel('Heat Capacity (in JK^-1)')
plt.title('Temperature dependence of Heat Capacity of solids')
#plt.savefig("Q9.png")
plt.show()
