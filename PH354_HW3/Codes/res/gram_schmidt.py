import numpy as np

def modified_gram_schmidt(A):

    v = []
    n = len(A[0])
    Q = np.zeros([n,n])
    R = np.zeros([n,n])

    for i in range(n):
        v.append(A[:,i])

    for i in range(0,n):
        R[i][i] = (np.linalg.norm(v[i]))
        Q[:,i] = v[i]/R[i][i]
        for j in range(i+1,n):
            R[i][j] = np.dot(Q[:,i],v[j])
            v[j] = v[j] - R[i][j] * Q[:,i]
    
    return Q,R
