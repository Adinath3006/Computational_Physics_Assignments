""" Exercise 11 """

import numpy as np
import matplotlib.pyplot as plt
import sys
sys.path.insert(0,'.')
from res.Gauss_Quad import *

"""The intensity is given as I = (I_0/8)*([2*C(u)+1]**2 + [2*S(u)+1]**2)"""

# Computing C(u) using the formula given in the problem set

def C(u):

    def f(t):
        return np.cos(0.5*np.pi*t**2)
    
    val = 0
    x,w = gaussxwab(50,0,u)
    for i in range(0,len(x)):
        val += w[i]*f(x[i])
    
    return val

# Computing S(u) using the formula given in the problem set

def S(u):

    def f(t):
        return np.sin(0.5*np.pi*t**2)
    
    val = 0
    x,w = gaussxwab(50,0,u)
    for i in range(0,len(x)):
        val += w[i]*f(x[i])
    
    return val

z = 3 # in (m)
Lambda = 1 # in (m)
x = np.linspace(-5,5,500,endpoint=False) # in (m)
u = x*np.sqrt(2/(Lambda*z))

# Computing I/I_0 using the above formula

rel_I = [(1/8)*((2*C(k)+1)**2 + (2*S(k)+1)**2) for k in u]

# Plotting the graph

plt.plot(x,rel_I)
plt.xlabel('x (in m)')
plt.ylabel('I/I_0')
plt.title('Variation in intensity')
#plt.savefig("Q11.png")
plt.show()
