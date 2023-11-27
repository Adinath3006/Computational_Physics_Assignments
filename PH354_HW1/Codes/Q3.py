""" Exercise 3 """

""" Using the cartesian to polar transformation we have x = r cos(theta) and y = r sin(theta), thus we can find theta 
    using arctan(y/x) = theta, and the value of r follows from sqrt((x**2) + (y**2)) = r. We also have to carefully solve the caveat
    where at x = 0, the machine does not compute the angle no matter the value of y and also for the case x < 0. """

import numpy as np
import math

x = float(input("Enter x coordinate:"))
y = float(input("Enter y coordinate:"))

if x == 0 and y == 0:
    
    print(" The corresponding polar coordinates are r = 0 and theta is undefined")

elif x == 0:

    r = np.sqrt((x**2) + (y**2))

    print(" The corresponding polar coordinates are r = {:.6f} and theta = {:.1f} degrees".format(r,math.copysign(90,y)))

else:

    theta = np.arctan(y/x)
    r = np.sqrt((x**2) + (y**2))
    theta_deg = (theta*180)/(np.pi)

    if x > 0 and y >= 0:
        print(" The corresponding polar coordinates are r = {:.6f} and theta = {:.6f} degrees".format(r,theta_deg))
    elif x > 0 and y <= 0:
        print(" The corresponding polar coordinates are r = {:.6f} and theta = {:.6f} degrees".format(r,360+theta_deg))
    else:
        print(" The corresponding polar coordinates are r = {:.6f} and theta = {:.6f} degrees".format(r,180+theta_deg))
