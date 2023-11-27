""" Exercise 5 """
"""All the results and graphs of the following code can be found in 'Outputs and Derivation' and 'Plots and Animations' directories"""
from random import uniform

"""The 10 dimensional hypersphere will be given as x1^2 + x2^2 + ... + x10^2 = 1,  The integral for a general N dimensions is 
given by I = V/N*Σf(x1i,x2i,....,x10i)"""

V = 2**10
N = 1000000
sum = 0

for n in range(N):
    y = 0
    for i in range(10):
        xi = uniform(-1,1)
        y += xi**2
    if y <= 1:
        sum += 1
        
I = V*sum/N

print("The volume of a 10-dimensional hypersphere of unit radius is {:.5f}".format(I))

"""The volume of a 10-dimensional hypersphere of unit radius is 2.54157"""