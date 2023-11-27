""" Exercise 4 """

import numpy as np
import math as mt
import pandas as pd
import matplotlib.pylab as plt

# Part A

Data = pd.read_csv("Codes/data/dow.txt", sep=" ", header= None)
Data = np.squeeze(Data)

plt.plot(Data)
plt.xlabel("Business Day")
plt.ylabel("Daily closing value")
plt.title("Dow Jones Industrial Data")
#plt.savefig("Q4_a.png")
plt.show()

# Part B

c_k = np.fft.rfft(Data)
N = len(c_k)

# Part C

for i in range(int(0.1*N),N,1):
    c_k[i] = 0

# Part D

y_1 = np.fft.irfft(c_k)

plt.plot(Data)
plt.plot(y_1)
plt.xlabel("Business Day")
plt.ylabel("Daily closing value")
#plt.title("Dow Jones Industrial Data")
plt.legend([" Original function" , " Smoothened function (10% FFT) "])
plt.savefig("Q4_d.png")
plt.show()

"""The process of setting all but the 10% of the data implies that the fourier coefficient of values above some cutoff k is made zero.
Thus we lose information while inverse transforming the data. In general lower values of fourier coefficient induces the general 
structure of the function, wheras as we go higher in the value of the coefficient we add the details in the graph like the amplitude 
of the point relative to the base structure of the graph. Thus by performing this method we get rid of the random noise in the data
and only preserve the nature of the graph."""

# Part E

c_k = np.fft.rfft(Data)
N = len(c_k)

for i in range(int(0.02*N),N,1):
    c_k[i] = 0

y_2 = np.fft.irfft(c_k)

plt.plot(Data)
plt.plot(y_2)
plt.xlabel("Business Day")
plt.ylabel("Daily closing value")
plt.title("Dow Jones Industrial Data")
plt.legend([" Original function" , " Smoothened function (2% FFT) "])
#plt.savefig("Q4_e.png")
plt.show()

# Part F

def f(x):
    if mt.floor(2*x)%2 == 0:
        return 1
    elif mt.floor(2*x)%2 == 1:
        return -1

N = 1000
x = np.linspace(0,1,N)

y = [f(i) for i in x]

c_k_f = np.fft.rfft(y)

K = int(N/2+1)

for k in range(10,K):
    c_k_f[k] = 0
    
y_new = np.fft.irfft(c_k_f)

plt.plot(x,y,label="Original function")
plt.plot(x,y_new,label="Smoothened function (1st 10 non-zero)")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
#plt.savefig("Q4_f.png")
plt.show()

"""We can see that the constant region after smoothening contrary to our expectations gives a non constant oscillating graph. This 
is an artifact due to the fact that we have removed values higher values of the fourier coefficient, hence we have lost information
as it is impossible to obtain a constant graph using a finite number of plane waves. Hence as we increase the number of plane waves
we get retrieve the orginal constant function"""