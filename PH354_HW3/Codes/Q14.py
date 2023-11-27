""" Exercise 14 """

# Part A

"""Refer the file Results.pdf"""

import numpy as np
import sys
sys.path.insert(0,'.')
from res.banded import *
from res.gausselim import *

def A_n(N):
    A = np.zeros((N, N))
    A[0][0] = 3
    A[0][1] = -1
    A[0][2] = -1

    for i in range(1,N-1):
        A[i][i-1] = -1
        A[i][i] = 4
        A[i][i+1] = -1
        if i != 1:
            A[i][i-2] = -1
        if i != N-2:
            A[i][i+2] = -1

    A[N-1][N-1] = 3
    A[N-1][N-2] = -1
    A[N-1][N-3] = -1

    return A

# Part B

V_plus = 5 # in V
N = 6

A = A_n(N)
V_init = np.zeros(N)
V_init[0] = V_plus
V_init[1] = V_plus

V = gausselim_partial_pivot(A,V_init)

for i in range(N):
    print(f"V{i+1} = {V[i]} volts")

"""
V1 = 3.725490196078432 volts
V2 = 3.4313725490196085 volts
V3 = 2.745098039215687 volts
V4 = 2.2549019607843146 volts
V5 = 1.5686274509803926 volts
V6 = 1.2745098039215692 volts"""

# Part C

V_plus = 5 # in V
N = 10000

A1 = A_n(N)
V_init = np.zeros(N)
V_init[0] = V_plus
V_init[1] = V_plus

V1 = gausselim_banded(A1,V_init,2)

output = open("potential.txt",'w')
for i in range(N):
    output.write(f"V{i} = {V1[i]} volts\n")
output.close()
