""" Exercise 2 """

import numpy as np
import pandas as pd
import matplotlib.pylab as plt

import sys
sys.path.insert(0,'.')
from res.coeff import *


# Part A

Data = pd.read_csv("Codes/data/sunspots.txt", sep="\t", header= None)
Data = pd.DataFrame(Data)

Data = np.array(Data)

x = Data[:,0]
y = Data[:,1]

plt.plot(x,y)
plt.xlabel("Months")
plt.ylabel("Number of sunspots")
plt.title("Plot of the sunspots data")
plt.grid()
#plt.savefig("Q2_a.png")
plt.show()

"""Just by eyeballing from the graph we can estimate the period to be about 140 months"""

# Part B

N = len(y)

c_k = [c_k(y,N,k) for k in range(1000)]

plt.xlabel("k")
plt.ylabel("|c_k|^2")
plt.title("FFT of sunspots")
plt.plot(abs(np.array(c_k))**2)
plt.grid()
#plt.savefig("Q2_b.png")
plt.show()

# Part C

""" The value of k corresponding to the peak in the FFT graph is k = 23, and we know that the frequency is given by f = k/N where
N is the sample size hence f = 136.652 months which is close to the estimated value, 140 months"""