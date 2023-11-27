import numpy as np

import sys
sys.path.insert(0, '.')
from res.gram_schmidt import *

def eigenval(A,eps):
    maxiter = 50
    check = 0
    N = A.shape[0]
    D = np.copy(A)
    V = np.identity(N)
    for i in range(0,maxiter):
        Q,R = modified_gram_schmidt(D)
        D = np.dot(R,Q)
        V = np.dot(V,Q)
        max_el = 0
        for j in range(N):
            for k in range(N):
                if j != k and abs(D[j][k]) > max_el:
                    max_el = abs(D[j][k])
        if max_el < eps:
            check = 1
            break
    if check == 0:
        print("Program has failed to converge")
    else:
        return D,V
        
