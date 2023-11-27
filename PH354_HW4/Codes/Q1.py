""" Exercise 1 """

import numpy as np
import matplotlib.pylab as plt

import sys
sys.path.insert(0,'.')
from res.coeff import *

# Part A

# Square Wave
def f1(n):
    if n <= 500 and n >= 0:
        return 1
    else:
        return 0

y1 = [f1(n) for n in range(1000)]
K = np.linspace(0,500,1000)
c_k_1 = np.array([c_k(y1,1000,k) for k in K])

plt.plot(K,abs(c_k_1)**2)
plt.xlabel("k")
plt.ylabel("|c_k|^2")
plt.title("FFT of square wave")
#plt.savefig("Q1_a.png")
plt.show()

# Part B

# Sawtooth function
def f2(n):
    return n

y2 = [f2(n) for n in range(1000)]
K = np.linspace(0,500,1000)
c_k_2 = np.array([c_k(y2,1000,k) for k in K])

plt.plot(K,abs(c_k_2)**2)
plt.xlabel("k")
plt.ylabel("|c_k|^2")
plt.title("FFT of sawtooth wave")
#plt.savefig("Q1_b.png")
plt.show()

# Part C

# Modulated sine function
def f3(n):
    return np.sin((np.pi*n)/1000)*np.sin((20*np.pi*n)/1000)

y3 = [f3(n) for n in range(1000)]
K = np.linspace(0,500,1000)
c_k_3 = np.array([c_k(y3,1000,k) for k in K])

plt.plot(K,abs(c_k_3)**2)
plt.xlabel("k")
plt.ylabel("|c_k|^2")
plt.title("FFT of square wave")
#plt.savefig("Q1_c.png")
plt.show()
