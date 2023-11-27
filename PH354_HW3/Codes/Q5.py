""" Exercise 5 """

from scipy.constants import h,k,c
from math import pi
import sympy as sym

import sys
sys.path.insert(0,'.')
from res.bisection import *

# Part A

"""When the emitted radiation is the strongest this implies that the intensity is maximum and we find the maxima of the function I(lambda)"""

T = 1 # We pick this value for ease of calculation

x = sym.symbols("x")
I = (2*pi*(c**2)*x**(-5)) / (sym.exp(h*c/(x*k*T)) - 1) 

dI_dx = sym.diff(I,x)

dI_dx_num = sym.lambdify(x,dI_dx) 

print(f"The wavelength which emits maximum radiation is {bisect(1e-2,1e-3,1e-6,dI_dx_num)} m")
print(f"The value of Wein's constant obtained is {bisect(1e-2,1e-3,1e-6,dI_dx_num)} K-m")

"""
The wavelength which emits maximum radiation is 0.00289788818359375 m
The value of Wein's constant obtained is 0.00289788818359375 K-m"""

# Part B

Lambda = 502e-9 # m
b = bisect(1e-2,1e-3,1e-6,dI_dx_num)
Temp = b/Lambda

print(f"The temperature of the surface of sun estimated using this method is {Temp} K")

"""The temperature of the surface of sun estimated using this method is 5772.685624688745 K"""