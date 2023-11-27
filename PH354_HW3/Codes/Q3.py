""" Exercise 3 """

import numpy as np
import matplotlib.pyplot as plt

# Part A

import sys
sys.path.insert(0,'.')
from res.fixed_point import *

def Root_fixed_point(c):
    
    def f(x):
        return 1 - np.exp(-c*x)
    
    return fixed(1,1e-6,f)

print("The solution of this equation found using fixed point iteration is:",Root_fixed_point(2))

"""The solution of this equation found using fixed point iteration is: 0.7968133630966887"""

# Part B

c = np.arange(0,3+0.01,0.01)
x = [Root_fixed_point(i) for i in c]

plt.plot(c,x)
plt.xlabel("c")
plt.ylabel("x")
plt.title("Percolation transition")
plt.grid()
#plt.savefig("Q3.png")
plt.show()

# Part C

def acc_root_fixed_point(c):

    def g(x):
        return x - 1 + np.exp(-c*x)
    
    def gp(x):
        return 1 - c*np.exp(-c*x)
    
    return accelerated_fixed(1,1e-6,g,gp)

print("The solution of this equation found using accelerated fixed point iteration is:",acc_root_fixed_point(2))

"""
The solution of this equation found using fixed point iteration is: 0.7968133630966887
Root obtained at 0th iteration is 0.8144387474091372 with error 0.014517961973149333
Root obtained at 1th iteration is 0.7999207854359879 with error 0.0025356062279175643
Root obtained at 2th iteration is 0.7973851792080703 with error 0.00046660573598257955
Root obtained at 3th iteration is 0.7969185734720877 with error 8.66440000362326e-05
Root obtained at 4th iteration is 0.7968319294720515 with error 1.611561775200535e-05
Root obtained at 5th iteration is 0.7968158138542994 with error 2.998396626344378e-06
Root obtained at 6th iteration is 0.7968128154576731 with error 5.578996155163993e-07
The solution of this equation found using accelerated fixed point iteration is: 0.7968128154576731"""