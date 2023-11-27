""" Exercise 13 """

import numpy as np
import matplotlib.pyplot as plt
import math
import sys
sys.path.insert(0,'.')
from res.Gauss_Quad import *

# Part A

""" Here we must use iterative computation rather than recursive computation, as H_n = 2*x*H_n-1 - 2*(n-1)*H_n-2 we can see that in 
    recursive method we call H(n,x) 2 times for each step, namely H_n-1 and H_n-2 thus computation time will increase in powers of 2.
    Which is very inefficient when compared to computing one element at a time for each step."""

def H(n,x):
    H_n = []
    H_n.append(1)
    if n >= 1:
        H_n.append(2*x)
    if n >= 2:
        for i in range(2,n+1):
            H_n.append(2*x*H_n[i-1] - 2*(i-1)*H_n[i-2])
    return H_n

def psi(n,x):
    return (1/(np.sqrt((2**n)*(math.factorial(n))*(np.sqrt(np.pi)))))*(math.e**(-0.5*x**2))*H(n,x)[n]

x = np.linspace(-4,4,150,endpoint=False)
psi_0 = [psi(0,k) for k in x]
psi_1 = [psi(1,k) for k in x]
psi_2 = [psi(2,k) for k in x]
psi_3 = [psi(3,k) for k in x]

plt.plot(x,psi_0,label ='Psi_0')
plt.plot(x,psi_1,label ='Psi_1')
plt.plot(x,psi_2,label ='Psi_2')
plt.plot(x,psi_3,label ='Psi_3')
plt.legend()
plt.xlabel('x')
plt.ylabel('Wavefunction')
plt.title('Eigenstates of Harmonic Oscillator')
#plt.savefig('Q13_a.png')
plt.grid()
plt.show()

# Part B

x = np.linspace(-10,10,300,endpoint=False)
psi_30 = [psi(30,k) for k in x]

plt.plot(x,psi_30,label ='Psi_30')
plt.legend()
plt.xlabel('x')
plt.ylabel('Wavefunction')
plt.title('Eigenstate (n=30) of Harmonic Oscillator')
#plt.savefig('Q13_b.png')
plt.grid()
plt.show()

# Part C

def exp_x_square(n):
    
    def f(x):
        return (x**2)*(psi(n,x))**2
    
    val = 0
    x,w = gaussxwab(100,-5,5)
    for i in range(0,len(x)):
        val += w[i]*f(x[i])
    
    return val

print("The uncertainity in position for n = 5 is {}".format(np.sqrt(exp_x_square(5))))

"""The uncertainity in position for n = 5 is 2.3451896081212955. We have used the integration limits to be -5 to 5 as for large values
of limits the exponential function in the wavefunction overflows and underflows, also for |x|>5 the wavefunction goes to zero. Thus 
we can use the above limits  """