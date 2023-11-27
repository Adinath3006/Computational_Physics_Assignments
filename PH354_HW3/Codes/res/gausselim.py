from numpy import array,empty

A = array([[ 2,  1,  4,  1 ],
           [ 3,  4, -1, -1 ],
           [ 1, -4,  1,  5 ],
           [ 2, -2,  1,  3 ]],float)
v = array([ -4, 3, 9, 7 ],float)
N = len(v)

# Gaussian elimination
def gausselim(A,v):
    for m in range(N):

        # Divide by the diagonal element
        div = A[m,m]
        A[m,:] /= div
        v[m] /= div

        # Now subtract from the lower rows
        for i in range(m+1,N):
            mult = A[i,m]
            A[i,:] -= mult*A[m,:]
            v[i] -= mult*v[m]

    # Backsubstitution
    x = empty(N,float)
    for m in range(N-1,-1,-1):
        x[m] = v[m]
        for i in range(m+1,N):
            x[m] -= A[m,i]*x[i]

    return

# Gaussian Elimination with Partial Pivoting

from numpy import array,empty
import numpy as np

def gausselim_partial_pivot(A,v):

    r,c = A.shape

    for j in range(0,c):

        # Switching rows with the maximal element
        for i in range(j,r):
            if abs(A[i][j])>abs(A[j][j]):   
                temp1 = np.copy(A[j])
                temp2 = np.copy(v[j])
                A[j] = np.copy(A[i])
                v[j] = np.copy(v[i])
                A[i] = np.copy(temp1)
                v[i] = np.copy(temp2)
            else:
                continue

        # Divide by the diagonal element            
        div = A[j,j]
        A[j,:] /= div
        v[j] /= div

        # Now subtract from the lower rows
        for i in range(j+1,len(v)):
            mult = A[i,j]
            A[i,:] -= mult*A[j,:]
            v[i] -= mult*v[j]
        
    # Backsubstitution
    x = empty(len(v),float)
    for m in range(len(v)-1,-1,-1):
        x[m] = v[m]
        for i in range(m+1,len(v)):
            x[m] -= A[m,i]*x[i]

    return x

# Gaussian elimination
def gausselim_banded(A,v,band):
    N = A.shape[0]
    for m in range(N):

        # Divide by the diagonal element
        div = A[m,m]
        A[m,:] /= div
        v[m] /= div

        n = min(m + 1 + band, N)

        # Now subtract from the lower rows
        for i in range(m+1,n):
            mult = A[i,m]
            A[i,:] -= mult*A[m,:]
            v[i] -= mult*v[m]

    # Backsubstitution
    x = empty(N,float)
    for m in range(N-1,-1,-1):
        x[m] = v[m]
        for i in range(m+1,N):
            x[m] -= A[m,i]*x[i]

    return x
