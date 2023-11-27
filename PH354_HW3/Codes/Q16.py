""" Exercise 16 """

import numpy as np
import sys
sys.path.insert(0,'.')
from res.gram_schmidt import *
from scipy.constants import hbar, e, m_e
from res.Int_Methods import *
import matplotlib.pyplot as plt

# Part A

"""Refer the file Results.pdf"""

# Part B

a = 10 * e # in J
L = 5 * 10**(-10) # in m

def H_mn(m,n):
    if m == n :
        return (n*hbar*np.pi)**2/(2*m_e*L**2) + a / 2
    elif (m % 2) == (n % 2) :
        return 0
    else:
        return -8*a*m*n/(np.pi**2*(m**2 - n**2)**2)
    
# Part C

dim = 10
H = np.zeros([dim,dim])

for m in range(dim):
    for n in range(dim):
        H[m,n] = H_mn(m + 1,n + 1)

eigenval = np.sort(np.linalg.eigvals(H)/e) # eV
print("Calculating the first ten enrgy levels using 10x10 matrix method")
for i in range(dim):
    print(f"The {i} state energy is : {eigenval[i]} eV")

"""
Calculating the first ten enrgy levels using 10x10 matrix method

The 0 state energy is : 5.836376902706757 eV
The 1 state energy is : 11.18109290629752 eV
The 2 state energy is : 18.662891578380517 eV
The 3 state energy is : 29.14419775590048 eV
The 4 state energy is : 42.655074845333516 eV
The 5 state energy is : 59.185257819333145 eV
The 6 state energy is : 78.72936018850429 eV
The 7 state energy is : 101.28548383437379 eV
The 8 state energy is : 126.8513857454442 eV
The 9 state energy is : 155.55532885350138 eV"""

# Part D

dim = 100
H2 = np.zeros([dim,dim])

for m in range(dim):
    for n in range(dim):
        H2[m,n] = H_mn(m + 1,n + 1)

eigenval2 = np.sort(np.linalg.eigvals(H2)/e) # eV
print("Calculating the first ten enrgy levels using 100x100 matrix method")
for i in range(10):
    print(f"The {i} state energy is : {eigenval2[i]} eV")

print("The relative difference between the two methods are:")
for i in range(10):
    print(f"For the {i} state energy the difference between 10x10 and 100x100 method is : {eigenval[i] - eigenval2[i]} eV")

"""
Calculating the first ten enrgy levels using 100x100 matrix method
The 0 state energy is : 5.8363765020361384 eV
The 1 state energy is : 11.181091583031925 eV
The 2 state energy is : 18.66288970736844 eV
The 3 state energy is : 29.144188956249522 eV
The 4 state energy is : 42.65506572522523 eV
The 5 state energy is : 59.18520523633897 eV
The 6 state energy is : 78.72930836144975 eV
The 7 state energy is : 101.28485290329287 eV
The 8 state energy is : 126.8505534197182 eV
The 9 state energy is : 155.42570638517662 eV"""

"""
The relative difference between the two methods are:
For the 0 state energy the difference between 10x10 and 100x100 method is : 4.0067061846116303e-07 eV
For the 1 state energy the difference between 10x10 and 100x100 method is : 1.3232655948769434e-06 eV
For the 2 state energy the difference between 10x10 and 100x100 method is : 1.8710120777143402e-06 eV
For the 3 state energy the difference between 10x10 and 100x100 method is : 8.79965095634816e-06 eV
For the 4 state energy the difference between 10x10 and 100x100 method is : 9.120108288129813e-06 eV
For the 5 state energy the difference between 10x10 and 100x100 method is : 5.258299417221224e-05 eV
For the 6 state energy the difference between 10x10 and 100x100 method is : 5.182705453421477e-05 eV
For the 7 state energy the difference between 10x10 and 100x100 method is : 0.0006309310809200497 eV
For the 8 state energy the difference between 10x10 and 100x100 method is : 0.0008323257260087757 eV
For the 9 state energy the difference between 10x10 and 100x100 method is : 0.12962246832475444 eV"""

"""Hence we can observe that 10x10 method agrees very closely with 100x100 method with only a considerable discrepancy at higher energy
levels."""

# Part E

eignval, eignvec = np.linalg.eig(H)

def psi_n(x,eignvec):

    def sin_2(x):
        return np.sin(1* np.pi * x / L)**2
    
    # Normalization for the Sinosoidal function
    val = Composite_Integration(sin_2,1,0,L,20)
    
    def psi(x):
        y = 0
        for i in range(len(eignvec)):
            y += eignvec[i] * np.sin(i * np.pi * x / L)
        return y/np.sqrt(val)    

    # Normalized wavefunction
    return psi(x)

x = np.linspace(0, L, 1001)

plt.plot(x / L, [psi_n(i,eignvec[0])**2 for i in x], label = 'Ground State')
plt.plot(x / L, [psi_n(i,eignvec[1])**2 for i in x], label = '1st excited State')
plt.plot(x / L, [psi_n(i,eignvec[2])**2 for i in x], label = '2nd excited State')
plt.axhline(0, c = 'k')
plt.axvline(0, c = 'k')
plt.axvline(1, c = 'k')
plt.title("Probability distribution")
plt.xlabel("x/L")
plt.ylabel("Psi**2(x)")
plt.grid()
plt.legend()
#plt.savefig("Q16.png")
plt.show()

def psi_norm(eignvec):
    def sin_2(x):
        return np.sin(1* np.pi * x / L)**2
    
    # Normalization for the Sinosoidal function
    val = Composite_Integration(sin_2,1,0,L,20)
    
    def psi(x):
        y = 0
        for i in range(len(eignvec)):
            y += eignvec[i] * np.sin(i * np.pi * x / L)
        return y/np.sqrt(val) 
    
    def psi_2(x):
        return psi(x)**2
    
    val1 = Composite_Integration(psi_2,1,0,L,20)

    return np.sqrt(val1)

for i in range(3):
    print(f"The value of integral psi**2 for the {i} state is {psi_norm(eignvec[i])}")

"""
The value of integral psi**2 for the 0 state is 0.9999999984333351
The value of integral psi**2 for the 1 state is 0.999999999846115
The value of integral psi**2 for the 2 state is 0.999999976569353.

Hence the wavefunction is normalized."""