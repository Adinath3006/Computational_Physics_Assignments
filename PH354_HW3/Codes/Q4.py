""" Exercise 4 """

import numpy as np

# Part A

"""Refer the file Results.pdf"""

# Part B

"""The system of equations for which we use fixed point iteration is x = y*(a + x**2) and y = b/(a + x**2)"""

a = 1
b = 2
maxiter = 100
i = 0
xi = 0
yi = 0

while i < maxiter:
    xin = xi
    yin = yi
    xi = yin*(a + xin**2)
    yi = b/(a + xin**2)
    i = i+1

print(f"Roots computed using fixed point iteration are x = {xi} and y = {yi}")
print(f"Roots computed analytically are x = {b} and  y = {b /(a + b**2)}")

"""
Roots computed using fixed point iteration are x = 0.636383990038212 and y = 1.999928171652484
Roots computed analytically are x = 2 and  y = 0.4
Thus we can see that even after 100 iterations the roots don't converge to the analytic value hence this method is not very efficient."""

# Part C

i = 0
xi = 1
yi = 1

while i < maxiter:
    xin = xi
    yin = yi
    xi = np.sqrt(b/yin - a)
    yi = xin/(a + xin**2)
    i = i+1

print(f"Roots computed using fixed point iteration are x = {xi} and y = {yi}")
print(f"Roots computed analytically are x = {b} and  y = {b /(a + b**2)}")

"""
Roots computed using fixed point iteration are x = 2.0 and y = 0.4
Roots computed analytically are x = 2 and  y = 0.4"""