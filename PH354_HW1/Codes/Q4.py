""" Exercise 4 """

# Part A    

""" Since the observer frame on Earth is at rest then he/she will measure the time period t to be x/v light years """

import numpy as np

x = float(input("Enter the value of distance in light years:"))
v = float(input("Enter the value of speed as a fraction of the speed of light c:"))

t_earth = x/v

print("Time observed by an observer at rest on Earth is {:.4f} years".format(t_earth))

# Part B

""" The observer on the ship will experience time dilation due to relativistic effects experienced in the observer's frame 
    The corresponding time will be t*gamma (gamma --> Lorentz factor)."""

t_ship = t_earth*np.sqrt(1-v**2)

print("Time observed by an observer on ship is {:.4f} years".format(t_ship))

""" Time observed by an observer at rest on Earth is 10.1010 years
    Time observed by an observer on ship is 1.4249 years"""