""" Exercise 11 """

from numpy import array,empty

import sys
sys.path.insert(0,'.')
from res.gausselim import *

# Part A

A = array([[ 4,-1,-1,-1 ],
           [-1,3,0,-1 ],
           [ -1,0,3,-1 ],
           [ -1,-1,-1,4 ]],float)
v = array([ 5,0,5,0 ],float)

print(gausselim_partial_pivot(A,v))

"""[3.         1.66666667 3.33333333 2.        ]"""

# Part B

A1 = array([[0,1,4,1],
            [3,4,-1,-1],
            [1,-4,1,5],
            [2,-2,1,3]],float)
v1 = array([-4,3,9,7],float)

print(gausselim_partial_pivot(A1,v1))
print(gausselim(A1,v1))

"""[ 1.61904762 -0.42857143 -1.23809524  1.38095238]
Whereas without pivoting we get the output None"""
