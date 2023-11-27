""" Exercise 14 """

# Part A

import numpy as np
import matplotlib.pyplot as plt

theta_a = np.linspace(0,2*np.pi,1000,endpoint=False)

x_a = 2*np.cos(theta_a) + np.cos(2*theta_a)
y_a = 2*np.sin(theta_a) - np.sin(2*theta_a)

plt.plot(x_a,y_a)
plt.title("Deltoid curve")
plt.savefig("Q14_a.png")
plt.show()

# Part B

theta_b = np.linspace(0,10*np.pi,1000)

r_b = np.power(theta_b,2)

x_b = np.multiply(r_b,(np.cos(theta_b)))
y_b = np.multiply(r_b,(np.sin(theta_b)))

plt.plot(x_b,y_b)
plt.title("Galilean Spiral")
plt.savefig("Q14_b.png")
plt.show()

# Part C

theta_c = np.linspace(0,24*np.pi,1000)

r_c = np.power(np.e,np.cos(theta_c)) - 2*np.cos(4*theta_c) + np.power(np.sin(theta_c/12),5)

x_c = np.multiply(r_c,(np.cos(theta_c)))
y_c = np.multiply(r_c,(np.sin(theta_c)))

plt.plot(x_c,y_c)
plt.title("Fey Function")
plt.savefig("Q14_c.png")
plt.show()