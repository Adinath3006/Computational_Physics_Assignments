""" Exercise 8 """

import numpy as np
import matplotlib.pyplot as plt

import pandas as pd

# Part A

data = pd.read_csv('Codes/data/blur.txt',sep='\s+',header=None)
data = pd.DataFrame(data)

temp = np.zeros(data.shape)
dim_y,dim_x = data.shape
for i in range(dim_x):
    for j in range(dim_y):
        temp[i][j] = data[dim_x-1-i][dim_y-j-1]
dat = temp.transpose()

plt.pcolormesh(dat)
plt.title("Blurred Image")
#lt.savefig("Q8_a.png")
plt.show()

# Part B
sigma = 25

def gauss(x,y):
    return np.exp((-x**2 - y**2)/(2*sigma**2))

I_spread = np.zeros(data.shape)
for i in range(dim_x):
    for j in range(dim_y):
        if i < dim_x/2 and j < dim_y/2:
            I_spread[i][j] = gauss(i,j)
        elif i >= dim_x/2 and j < dim_y/2:
            I_spread[i][j] = gauss(dim_x - i,j)
        elif i < dim_x/2 and j >= dim_y/2:
            I_spread[i][j] = gauss(i,dim_y - j)
        else:
            I_spread[i][j] = gauss(dim_x - i,dim_y - j)

plt.pcolormesh(I_spread,cmap='gray')
#plt.savefig("Q8_b.png")
plt.show()

# Part C

c_k_1 = np.fft.rfft2(dat)
c_k_2 = np.fft.rfft2(I_spread)

c_k = np.zeros(I_spread.shape, dtype=np.complex128)

for i in range(c_k_2.shape[0]):
    for j in range(c_k_2.shape[1]):
        if c_k_2[i][j] <= 1e-3 :
            c_k[i][j] = c_k_1[i][j] / dim_x**2 
        else:
            c_k[i][j] = c_k_1[i][j] / (dim_x**2 * c_k_2[i][j] )
            
sharp_imag = np.fft.irfft2(c_k)

plt.pcolormesh(abs(sharp_imag))
plt.title("Sharp and Clear Image")
#plt.savefig("Q8_c.png")
plt.show()

# Part D

"""The image obtained thorugh this method is not very sharp, this is due to the fact we have neglected terms with small values in the 
FFT, i.e., e = 1e-3 in our case, hence we have loss in information. Thus in order to create a sharp and clear image we have to decrease
the error which requires our machine to be capable of handling very small numbers with large precision which arise in the gaussian
distribution. Thus theoretically we can see that e must approach zero for a perfectly sharp image hence allowing numbers of very small
order which is impossible to implement physically in computer."""