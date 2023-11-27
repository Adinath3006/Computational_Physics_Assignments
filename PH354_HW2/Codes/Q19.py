""" Exercise 19 """

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('altitude.txt',sep='\s+',header=None)
data = pd.DataFrame(data)

dim_y,dim_x = data.shape

h = 30000 # in (m)

# Part A

# Computing the partial derivative

def partial(data,h):

    dim_y,dim_x = data.shape
    dw_dx = np.zeros([dim_x,dim_y])
    dw_dy = np.zeros([dim_x,dim_y])

    for i in range(0,dim_x):
        for j in range(0,dim_y):
            if j == dim_y-1:
                # Backward difference for the endpoint
                dw_dx[i][j] = (data[i][j] - data[i][j-1])/h
            else:
                # Forward difference for the other points
                dw_dx[i][j] = (data[i][j+1] - data[i][j])/h

    for i in range(0,dim_x):
        for j in range(0,dim_y):
            if i == dim_x-1:
                # Backward difference for the endpoint
                dw_dx[i][j] = (data[i][j] - data[i-1][j])/h
            else:
                # Forward difference for the other points
                dw_dx[i][j] = (data[i+1][j] - data[i][j])/h
    
    return dw_dx,dw_dy

# Part B

dw_dx,dw_dy = partial(data,h)
phi = np.pi/4

def Intensity(dw_dx,dw_dy,phi,data):

    dim_y,dim_x = data.shape
    I = np.zeros([dim_x,dim_y])

    for i in range(0,dim_x):
        for j in range(0,dim_y):
            I[i][dim_y-1-j] = (np.cos(phi)*dw_dx[i][j] + np.sin(phi)*dw_dy[i][j])/(np.sqrt(dw_dx[i][j]**2 + dw_dy[i][j]**2 + 1))
    
    return I

plt.pcolormesh(-Intensity(dw_dx,dw_dy,phi,data).transpose(),cmap = 'gray')
plt.colorbar()
#plt.savefig('Q19_b.png')
plt.show()

# Part C

data1 = pd.read_csv('stm.txt',sep='\s+',header=None)
data1 = pd.DataFrame(data1)

dim_y1,dim_x1 = data1.shape

h1 = 2.5

dw_dx1,dw_dy1 = partial(data1,h1)

plt.pcolormesh(-Intensity(dw_dx1,dw_dy1,phi,data1).transpose())
plt.colorbar()
#plt.savefig('Q19_c.png')
plt.show()
