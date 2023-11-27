from numpy import array,empty

import sys
sys.path.insert(0,'.')
from res.gram_schmidt import *
from res.eigenval import *

# Part A

"""Modified Gram-Schmidt method is used for the QR decomposition."""

A = np.array( [[1,4,8,4],
               [4,2,3,7],
                [8,3,6,9],
                [4,7,9,2]] )
v = array([ 5,0,5,0 ],float)

Q,R = modified_gram_schmidt(A)
print("A = ",A)
print("Q = ",Q)
print("R = ",R)
print("QR = ",np.dot(Q,R))
print("Hence A and QR are the same.")

"""
A =  [[1 4 8 4]
 [4 2 3 7]
 [8 3 6 9]
 [4 7 9 2]]
Q =  [[ 0.10153462  0.558463    0.80981107  0.1483773 ]
 [ 0.40613847 -0.10686638 -0.14147555  0.8964462 ]
 [ 0.81227693 -0.38092692  0.22995024 -0.37712564]
 [ 0.40613847  0.72910447 -0.5208777  -0.17928924]]
R =  [[ 9.8488578   6.49821546 10.55960012 11.37187705]
 [ 0.          5.98106979  8.4234836  -0.484346  ]
 [ 0.          0.          2.74586406  3.27671222]
 [ 0.          0.          0.          3.11592335]]
QR =  [[1. 4. 8. 4.]
 [4. 2. 3. 7.]
 [8. 3. 6. 9.]
 [4. 7. 9. 2.]]
Hence A and QR are the same."""

D,V = eigenval(A,1e-6)
e_val = [D[i][i] for i in range(D.shape[0])]

print(f"Eigenvalues of A are: {e_val}")
print("Eigenvectors of A are: ",V)

"""
Eigenvalues of A are: [20.99999999999998, -7.999999999999982, -3.0, 0.9999999999999997]
Eigenvectors of A are:  [[ 0.43151698 -0.38357064 -0.77459666 -0.25819889]
 [ 0.38357063  0.43151698 -0.2581989   0.77459667]
 [ 0.62330228  0.52740965  0.25819889 -0.51639778]
 [ 0.52740965 -0.62330227  0.51639779  0.25819889]]"""

