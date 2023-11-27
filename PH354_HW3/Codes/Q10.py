from numpy import array,empty

# Part A

"""Refer the file Results.pdf"""

# Part B

"""Using the nodal analysis of the circuit we have the final system of linear equations written in form of a matrix given below"""

A = array([[ 4,-1,-1,-1 ],
           [-1,3,0,-1 ],
           [ -1,0,3,-1 ],
           [ -1,-1,-1,4 ]],float)
v = array([ 5,0,5,0 ],float)
N = len(v)

# Gaussian elimination
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

print("Thus the potential of each of the nodes are:")

for i in range(N):
     print(f"V{i} = {x[i]} Volts")	

"""
Thus the potential of each of the nodes are:
V0 = 3.0 Volts
V1 = 1.6666666666666665 Volts
V2 = 3.3333333333333335 Volts
V3 = 2.0 Volts"""