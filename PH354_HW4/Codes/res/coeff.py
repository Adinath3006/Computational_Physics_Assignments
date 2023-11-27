import numpy as np

def c_k(y,N,k):
    sum  = 0
    for i in range(N):
        sum += y[i]*np.exp(-1j*(2*np.pi*k*i)/N)
    return sum