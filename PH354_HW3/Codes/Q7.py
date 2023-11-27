""" Exercise 7 """

import numpy as np
import matplotlib.pyplot as plt

import sys
sys.path.insert(0,'.')
from res.newton import newton

# Part A

def P(x):
    return 924*x**6 - 2772*x**5 + 3150*x**4 - 1680*x**3 + 420*x**2 - 42*x + 1

x_ax = np.linspace(0,1,101)
y_ax = [P(i) for i in x_ax]

plt.plot(x_ax,y_ax)
plt.axhline(0.0,color="black")
plt.title("Roots of a polynomial")
plt.xlabel('x')
plt.ylabel('P(x)')
plt.grid()
#plt.savefig("Q7.png")
plt.show()

"""The rough values of the roots are 0.033, 0.17, 0.379, 0.619, 0.830, 0.965"""

# Part B

x_approx = [0.033,0.17,0.379,0.619,0.830,0.965] # Approximate values of the roots of the polynomial P(x)
x_newton = [newton(i,1e-10,P) for i in x_approx] # Roots computed using the Newton's method

print("The value of the six roots computed using Newton's method are:")
for i in range(0,6):
    print(x_newton[i])

"""
The value of the six roots computed using Newton's method are:
0.033765242898423975
0.16939530676505093
0.38069040695770584
0.6193095930415944
0.8306046932349631
0.9662347571015738"""

