""" Exercise 14 """

from scipy.constants import G
import math
import numpy as np
import matplotlib.pyplot as plt
import sys
sys.path.insert(0,'.')
from res.Gauss_Quad import *

# Part A

"""Refer file Output.pdf"""

# Part B

def F_z(z):
    L = 10 # in (m)
    sigma = (10000)/(100) # 10000kg/100m^2 is the surface density

    def f(x,y):
        return z/(x**2 + y**2 + z**2)**(3/2)
    
    # Computing the integral using double gaussian quadrature

    x1,w1 = gaussxwab(100,-L/2,L/2)
    x2,w2 = gaussxwab(100,-L/2,L/2)

    val = 0
    for i in range(0,len(x1)):
        for j in range(0,len(x2)):
            val += w1[i]*w2[j]*f(x1[i],x2[j])
    
    return G*sigma*val

z = np.linspace(0,10,200)
F = [F_z(k) for k in z]

plt.plot(z,F)
plt.xlabel('z (in m)')
plt.ylabel('Force (in N)')
plt.title("The variation of z component of force")
#plt.savefig('Q14.png')
plt.show()

