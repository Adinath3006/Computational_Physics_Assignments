""" Exercise 1 """

# Part A

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('velocities.txt',sep='\s+',header=None)
data = pd.DataFrame(data)

def Trapezoidal_Int(a,b,f,h):

    # Computing the sum f(x_1) + ... + f(x_n-1) and x_i = a + i*h where x_n = b and x_0 = a
    Sum_f_x_i = 0
    i = 1
    while i<=b-1:
        Sum_f_x_i = Sum_f_x_i + f[i]
        i = i+1

    # Computing the integral
    Integral = (h/2)*(f[a] + 2*Sum_f_x_i + f[b])

    return Integral

time = data[0]
velocity = np.transpose(data[1])

t = float(input("Enter the time at which the distance is calculated:"))

d = Trapezoidal_Int(time[0],t,velocity,1)

print("The distance travelled by the particle from time {} to {} is {:.5f}".format(time[0],t,d))

# Part B

distance = [Trapezoidal_Int(time[0],T,velocity,1) for T in time]
plt.plot(time,distance,label = 'distance')
plt.plot(time,velocity,'--',label = 'velocity')
plt.xlabel('Time (in secs)')
plt.title('Particle kinematics')
plt.legend()
plt.show()

"""
Enter the time at which the distance is calculated:3
The distance travelled by the particle from time 0 to 3.0 is 0.30934"""

