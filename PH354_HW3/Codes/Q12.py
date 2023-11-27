""" Exercise 12 """

from numpy import array,empty
import numpy as np

# Part A

A = array([[ 4,-1,-1,-1 ],
           [-1,3,0,-1 ],
           [ -1,0,3,-1 ],
           [ -1,-1,-1,4 ]],float)
v = array([ 5,0,5,0 ],float)

# Using numpy function to solve the problem

print(np.linalg.solve(A,v))

"""The solution to the given system of equations is [3.         1.66666667 3.33333333 2.        ], hence it is consistent with the solution
obtained in problem 10"""