""" Exercise 4 """

# Part A

import sys

sys.path.insert(0,'.')

from res.Int_Methods import Composite_Integration
import numpy as np
import matplotlib.pyplot as plt

# Computing the Bessel's Function using Simpson's rule for integration

def J(m,x):
    def f(t):
        return np.cos(m*t - x*np.sin(t))
    Integral = Composite_Integration(f,1,0,np.pi,1000)
    return (1/np.pi)*Integral

# Plotting J_0, J_1, J_2

x = np.arange(0,20,0.1)
y_0 = [J(0,i) for i in x]
y_1 = [J(1,i) for i in x]
y_2 = [J(2,i) for i in x]

plt.plot(x,y_0,label = 'J_0')
plt.plot(x,y_1,label = 'J_1')
plt.plot(x,y_2,label = 'J_2')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Bessel Functions')
plt.savefig('Q4_a.png')
plt.legend()
plt.show()

# Part B

# computing the Intensity 

def I(r):
    if r == 0:
        return 1/4
    else:
        Lambda = 500e-9 # in (m)
        k = (2*np.pi)/Lambda
        return (J(1,k*r)/(k*r))**2

# Density plot of the Intensity

R = 1e-6 # in (m)
x = np.linspace(-R,R,150)
y = np.linspace(-R,R,150)

map = np.zeros([len(x),len(y)])

for j in range(0,len(x)):
    for k in range(0,len(y)):
        r = np.sqrt(x[j]**2 + y[k]**2)
        map[j][k] = I(r)

plt.pcolormesh(x,y,map)
plt.colorbar
plt.title("Diffraction Pattern")
#plt.savefig('Q4_b1.png')
plt.show()

plt.pcolormesh(x,y,map,vmax=0.01)
plt.colorbar
plt.title("Diffraction Pattern")
#plt.savefig('Q4_b2.png')
plt.show()