""" Exercise 16 """

import numpy as np
import matplotlib.pyplot as plt
import cmath
import sys
sys.path.insert(0,'.')
from res.Gauss_Quad import *

# Part A

"""Refer file Output.pdf"""

# Part B

def q(u):
    alpha = np.pi/20e-6 # in (m^-1)
    return (np.sin(alpha*u))**2

# Part C

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

plt.plot(x,I_x)
plt.xlabel("x (in m)")
plt.ylabel('Relative Intensity')
#plt.savefig('Q16_1_1.png')
plt.show()

# Part D

I_xy = np.zeros([5,len(x)])

for h in range(0,5):
    I_xy[h] = I_x

plt.imshow(I_xy,vmax = 1.2e-9,aspect=0.5,extent=[-.05,0.05,0,0.05])
plt.title('Diffraction Pattern')
#plt.savefig('Q16_1_2.png')
plt.show()

# Part E
#(i)

def q_new(u):
    alpha = np.pi/20e-6 # in (m^-1)
    beta =  alpha/2
    return ((np.sin(alpha*u))**2)*((np.sin(beta*u))**2)

I_new_x = [I(k,x1,w1,q_new) for k in x]

plt.plot(x,I_new_x)
plt.xlabel("x (in m)")
plt.ylabel('Relative Intensity')
#plt.savefig('Q16_2_1.png')
plt.show()


I_new_xy = np.zeros([5,len(x)])

for h in range(0,5):
    I_new_xy[h] = I_new_x

plt.imshow(I_new_xy,vmax = 1.2e-9,aspect=0.5,extent=[-.05,0.05,0,0.05])
plt.title('Diffraction Pattern')
#plt.savefig('Q16_2_2.png')
plt.show()

#(ii)

def q_piece(u):
    if (u<-30e-6 and u>-40e-6) or (u>30e-6 and u<50e-6):
        return 1
    else:
        return 0

I_piece_x = [I(k,x1,w1,q_piece) for k in x]

plt.plot(x,I_piece_x)
plt.xlabel("x (in m)")
plt.ylabel('Relative Intensity')
#plt.savefig('Q16_3_1.png')
plt.show()

I_piece_xy = np.zeros([5,len(x)])

for h in range(0,5):
    I_piece_xy[h] = I_piece_x

plt.imshow(I_piece_xy,vmax = 1e-9,aspect=0.5,extent=[-.05,0.05,0,0.05])
plt.title('Diffraction Pattern')
#plt.savefig('Q16_3_2.png')
plt.show()
