""" Exercise 9 """

import numpy as np

import sys
sys.path.insert(0,'.')
from res.newton import newton2

# Part A

# Initial values
Vplus,VT=5,0.05
R1,R2,R3,R4=1e+3,4e+3,3e+3,2e+3
I0=3e-9

def f(x,y):
    return (x-Vplus)/R1+I0*np.exp((x-y)/VT)+x/R2

def g(x,y):
    return (y-Vplus)/R3-I0*np.exp((x-y)/VT)+y/R4

# Analytically calculating the partial derivatives of the function for each variable 

def fp(x,y):
    return (1./R1+1./R2)+I0/VT*np.exp((x-y)/VT),-I0/VT*np.exp((x-y)/VT)

def gp(x,y):
    return -I0/VT*np.exp((x-y)/VT),(1./R3+1./R4)+I0/VT*np.exp((x-y)/VT)

V1,V2= newton2(2.5,2.5,1e-5,f,fp,g,gp)

print (f"The values of the voltages are, V1 = {V1} Volts and V2 = {V2} Volts")

"""The values of the voltages are, V1 = 3.446971806506484 Volts and V2 = 2.829542290240274 Volts"""

# Part B

print(f"The potential difference across the diode is V1-V2 = {V1-V2} Volts")

"""The potential difference across the diode is V1-V2 = 0.6174295162662098 Volts. Thus this is close to the approximation, 0.6 Volts, used by engineers."""