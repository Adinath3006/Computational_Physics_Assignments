""" Exercise 12 """

# Part A

# Part B

from scipy.constants import hbar,c,k,sigma
import math
import numpy as np
import matplotlib.pyplot as plt
import sys
sys.path.insert(0,'.')
from res.Gauss_Quad import *

# Part A

"""Refer file Output.pdf"""

# Part B

# Computing the integral

def f(x):
    return (x**3)/(math.e**x - 1)

val = 0
x,w = gaussxwab(50,0,100)
for i in range(0,len(x)):
    val += w[i]*f(x[i])

print("The value of the integral obtain using the gaussian quadrature method is:",val)
print("The actual value calculated using Mathematica is:", (np.pi)**4/15)
print('Thus the error is:',abs((np.pi)**4/15-val))

"""We have used the gaussian quadrature method to evaluate the integral and the number of sample points used for doing so is N = 100, 
as it has high accuracy and converges to actual value, computed using Mathematica, very quickly, thus we can see the error to be
 very small, i.e., 4.432010314303625e-13"""

# Computing W(T) using the 

def W(T,val):
    return ((k**4)*(T**4))/(4*(np.pi**2)*(c**2)*(hbar**3))*val

# Part C

""" From Stefan's Law we have W = (sigma)T**4, thus for T = 1K we have W = sigma (Stefan Boltzmann constant)"""

print("The value of the Stefan Boltzmann constant computed using the method given is:",W(1,val))
print("The literature value of the Stefan Boltzmann constant is:",sigma)
print("The error percentage in the computed value from literature value is:",(W(1,val)-sigma)*100/sigma)
