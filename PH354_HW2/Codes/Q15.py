""" Exercise 15 """

from scipy.constants import G
import math
import numpy as np
import matplotlib.pyplot as plt
import sys
sys.path.insert(0,'.')
from res.Gauss_Quad import *

# Part A

def f(a,x):
    return x**(a-1)*(math.e**(-x))

x = np.linspace(0,5,100,endpoint=False)
f_a_2 = [f(2,i) for i in x]
f_a_3 = [f(3,i) for i in x]
f_a_4 = [f(4,i) for i in x]

plt.plot(x,f_a_2,label = 'a=2')
plt.plot(x,f_a_3,label = 'a=3')
plt.plot(x,f_a_4,label = 'a=4')
plt.legend()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Plot of the integrand of Gamma function for different a')
#plt.savefig('Q15.png')
plt.show()

# Part B
"""Refer file Output.pdf"""
# Part C
"""Refer file Output.pdf"""
# Part D
"""Refer file Output.pdf"""
# Part E

def gamma(a):
    def h(z):
        x = (a-1)*z/(1-z)
        return (math.e**((a-1)*(np.log(x)) - x))*((a-1)/(1-z)**2)
    
    val = 0
    x,w = gaussxwab(100,0,1)
    for i in range(0,len(x)):
        val += w[i]*h(x[i])

    return val

print("The user defined gamma function has passed the test for gamma(3/2):",gamma(1.5))

# Part F

print("Gamma(3):",gamma(3))
print("Gamma(6):",gamma(6))
print("Gamma(10):",gamma(10))

"""
The user defined gamma function has passed the test for gamma(3/2): 0.8862269613087213
Gamma(3): 2.0000000000000013
Gamma(6): 119.99999999999997
Gamma(10): 362879.99999999977"""