""" Exercise 6 """
"""All the results and graphs of the following code can be found in 'Outputs and Derivation' and 'Plots and Animations' directories"""
import numpy as np
from random import uniform

# Part A

"""Refer the Derivations.pdf file in Outputs and Derivations directory"""

# Part B

N = 1000000

def f(x):
    return 1/((np.exp(x) + 1)*np.sqrt(x))

def w(x):
    return x**(-1/2)

# Generating the non-uniform distribution of random numbers using the transformation x = y**2
y = np.random.rand(N)
x = y**2
f_w = f(x)/w(x)

"""Using the formula I = 1/N * Σf(x)/w(x) * ∫w(x)dx, we also know that the integral ∫w(x)dx = 2"""

I = (1/N)*(np.sum(f_w))*(2)

print("The value of the integral computed using importance sampling method is {:.5f}".format(I))

"""The value of the integral computed using importance sampling method is 0.83901. Which is very close to the actual value of the integral
0.84"""