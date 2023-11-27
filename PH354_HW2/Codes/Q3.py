""" Exercise 3 """

# Part A

import math

import sys

sys.path.insert(0,'.')

from res.Int_Methods import Composite_Integration
import numpy as np
import matplotlib.pyplot as plt

def f(t):
    return (math.e)**(-t**2)

def E(x):
    """Here we use the Simpson's method as it is a better approximation than Trapezoidal and the N we choose is even, for better accuracy
    we have N = 100"""

    # Using Simpsons Method using 100 slices
    return Composite_Integration(f,1,0,x,100)

x = np.arange(0,3,0.1)
y = [E(i) for i in x]

# Part B

plt.plot(x,y,label = "E(x)")
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
#plt.savefig('Q3.png')
plt.show()