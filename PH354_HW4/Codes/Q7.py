""" Exercise 7 """

import numpy as np
import matplotlib.pyplot as plt
import cmath

s = 20e-6 # m
w = 200e-6 # m
N = 500
W = 10*w # m
Lambda = 500e-9 # m
f = 1 # m

def q1(u):
    return (np.sin(np.pi*u/s))**2

y_ = []
for n in range(N):
    if n <= 0.1*N:
        y_.append(np.sqrt(q1((n*w)/(0.1*N) - w/2)))
    else:
        y_.append(0)

c_k = np.fft.fft(y_)

k_max = int((5e-2*W)/(Lambda*f))

I_ = [(W/N)**2*abs(c_k[abs(int(k-k_max))])**2 for k in range(2*k_max)]
x_ = [(Lambda*f*(k-k_max))/(W) for k in range(2*k_max)]


# Plot from the previous assignment

from res.Gauss_Quad import *

def q(u):
    alpha = np.pi/20e-6 # in (m^-1)
    return (np.sin(alpha*u))**2


"""The method used here to evaluate the integral is Gaussian quadrature with number sample points = 100. The reason is that the integral 
is evaluated to very high orders of x, thus N = 100 serves as a good and optimal approximate for the integral"""

def I(y,x,w,q):
    Lambda = 500e-9 # in (m)
    f = 1 # in (m)
    def h(u):
        return np.sqrt(q(u))*(cmath.exp(1j*(2*np.pi*y*u/(Lambda*f))))
    
    val = 0
    for i in range(0,len(x)):
        val += w[i]*h(x[i])

    return (abs(val))**2

x1,w1 = gaussxwab(100,-9*10e-6,9*10e-6)

L = 10e-2 # in (m)
x = np.linspace(-L/2,L/2,1000)
I_x = [I(k,x1,w1,q) for k in x]

fig , ax = plt.subplots(2,1)

ax[0].plot(x_,I_)
ax[0].set_title("Intensity plot using FFT method")
ax[0].set_xlabel("x")
ax[0].set_ylabel("Relative Intensity")

ax[1].plot(x,I_x)
ax[1].set_title("Intensity plot from the previous assignment")
ax[1].set_xlabel("x")
ax[1].set_ylabel("Relative Intensity")

fig.subplots_adjust(hspace=0.5)

#plt.savefig("Q7.png")
plt.show()