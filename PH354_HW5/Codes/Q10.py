""" Exercise 10 """
"""All the results and graphs of the following code can be found in 'Outputs and Derivation' and 'Plots and Animations' directories"""
# Part A
"""Refer the Derivations.pdf file in Outputs and Derivations directory"""
# Part B
"""Refer the Derivations.pdf file in Outputs and Derivations directory"""
# Part C

from random import random
from math import acos, pi

def rand_gen():
    """ Generates random numbers θ and ϕ based in its probability distributions p(θ) and p(ϕ)
    
    Arguments: 
    None
    
    Returns:
    [θ,ϕ] -- An array containing the generated random variables
    """
    y1 = random()
    y2 = random()
    x1 = acos(1 - 2*y1)
    x2 = 2*pi*y2
    return[x1,x2]

print(f"The random number theta with distribution p(θ):",rand_gen()[0])
print(f"The random number theta with distribution p(ϕ):",rand_gen()[1])