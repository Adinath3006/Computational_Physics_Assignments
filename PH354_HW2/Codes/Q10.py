""" Exercise 10 """

# Part A

"""Refer file Output.pdf"""

# Part B

"""The time period is given by the formula T/4 = int_{a}^{0} dx/sqrt((2/m)*(E-V(x))) here amp = a, thus E = V(a)"""

import numpy as np
import matplotlib.pyplot as plt
import sys
sys.path.insert(0,'.')
from res.Gauss_Quad import *

def V(x):
    return x**4

m = 1

def Time_Period(a):
    def f(x):
        return 1/(np.sqrt((2/m)*(V(a)-V(x))))
    
    val = 0
    x,w = gaussxwab(20,0,a)
    for i in range(0,len(x)):
        val += w[i]*f(x[i])

    return 4*val

a = np.linspace(0,2,100,endpoint=False)
Time = [Time_Period(amp) for amp in a]

plt.plot(a,Time)
#plt.savefig('Q10_1.png')
plt.xlabel('a')
plt.ylabel('Time')
plt.title('Dependence of time period of oscillation on amplitude')
plt.show()