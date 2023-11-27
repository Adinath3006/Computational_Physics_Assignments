""" Exercise 16 """

"""The logistic map is given by x' = r*x*(1-x). We perform an iterative map of this and plot r vs x"""

import matplotlib.pyplot as plt
import numpy as np

r = np.arange(1,4,0.01)

def Logistic_map(r):

    # Initial value of x
    x = 0.5
    """Iterating the logistic map equation a thousand times so that it may settle down to a fixed point or limit cycle"""
    for i in range(0,1000):
        x = r*x*(1-x)
    """Iterating the logistic map for another thousand iterations and plot the points (r, x) on a graph"""
    x_r = np.zeros(1000)
    x_r[0] = x
    for i in range(1,1000):
        x_r[i] = r*x_r[i-1]*(1 - x_r[i-1])
    return x_r

fig, ax = plt.subplots()

for k in r:
    r_plt = k*np.ones(1000)
    ax.scatter(r_plt,Logistic_map(k), s=1,color='black')

plt.title('Feigenbaum plot')
plt.xlabel('r')
plt.ylabel('x') 
plt.savefig("Q16.png")
plt.show()

"""Part A

Fixed Points:
In the Feigenbaum plot the points at which for a given value of r there is a single value of x are called fixed points, the range of 
values of r which produces fixed point is approximately r = 1 to r = 3.

Limit cycles:
In the Feigenbaum plot the points at which for a given value of r the value of x oscillates between two values for r in the range 3 to 3.5
(approximately), similarly for values of r slightly above 3.5, x oscillates between 4 points, and again for greater values of r x 
oscillates between 8,16,32,... points. 

Chaos:
After a certain threshold of r, x now takes seemingly infinite values at each point, but we can always algorithmically obtain any point in 
the Feigenbaum plot using the logistic equation. Thus we call it deterministic chaos.

Part B 

The value at which the system moves from orderly behavior (fixed points or limit cycles) to chaotic behavior is(approximately) r = 3.57"""