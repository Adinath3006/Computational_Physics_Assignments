""" Exercise 8 """

import numpy as np

L = 100
M = 0

for i in range(-L,L+1):
    for j in range(-L,L+1):
        for k in range(-L,L+1):
            if i == 0 and j == 0 and k == 0:
                M = M
            else:
                if (i+j+k)%2 == 0:
                    M = M + 1/(np.sqrt(i**2 + j**2 + k**2)) 
                else:
                    M = M - 1/(np.sqrt(i**2 + j**2 + k**2))

print("The value of Madelung constant for NaCl is: ",M)

""" The value of Madelung constant for NaCl is:  -1.7418198158396654 """