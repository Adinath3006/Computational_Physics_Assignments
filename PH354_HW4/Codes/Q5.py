""" Exercise 5 """

import numpy as np
import pandas as pd
import matplotlib.pylab as plt

import sys
sys.path.insert(0,'.')
from res.dcst import *

Data = pd.read_csv("Codes/data/dow2.txt", sep=" ", header= None)
Data = np.squeeze(Data)

plt.plot(Data)
plt.title("Plot of the Dow Jones Data")
plt.xlabel("Day")
plt.ylabel("Dow Jones Average")
#plt.savefig("Q5_a_1.png")
plt.grid()
plt.show()

c_k_1 = np.fft.rfft(Data)

N = c_k_1.shape[0]
for i in range(int(0.02*N),N,1):
    c_k_1[i] = 0
    
y_1 = np.fft.irfft(c_k_1)

plt.plot(Data,label="Original data")
plt.plot(y_1,label="Smoothened data(2% FFT)")
plt.title("Plot of the Dow Jones Data")
plt.xlabel("Day")
plt.ylabel("Dow Jones Average")
plt.grid()
plt.legend()
#plt.savefig("Q5_a_2.png")
plt.show()

# Part B

c_k_2 = dct(Data)

N = c_k_2.shape[0]
for i in range(int(0.02*N),N,1):
    c_k_2[i] = 0
    
y_2 = idct(c_k_2)

plt.plot(Data,label="Original data")
plt.plot(y_2,label="Smoothened data(2% DCT)")
plt.title("Plot of the Dow Jones Data")
plt.xlabel("Day")
plt.ylabel("Dow Jones Average")
plt.legend()
plt.grid()
#plt.savefig("Q5_b.png")
plt.show()