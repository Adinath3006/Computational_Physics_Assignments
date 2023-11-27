""" Exercise 13 """

from numpy import array
import numpy as np
import cmath as cm

R1,R3,R5 = 1e+3,1e+3,1e+3 # ohms
R2,R4,R6 = 2e+3,2e+3,2e+3 # ohms
C1,C2 = 1e-6,0.5e-6 # fraday
x_plus = 3 # V
w = 1000 # s^-1

A = array([[(1/R1)+(1/R4)+1j*w*C1, -1j*w*C1, 0],
          [-1j*w*C1,(1/R2)+(1/R5)+1j*w*C1+1j*w*C2,-1j*w*C2],
          [0,-1j*w*C2,(1/R3)+(1/R6)+1j*w*C2]])
v = array([x_plus/R1, x_plus/R2, x_plus/R3])

x = np.linalg.solve(A,v)

print(f"Amplitude of V1 = {cm.polar(x[0])[0]} Volts and the phase is = {cm.polar(x[0])[1] * 180 / np.pi} degrees")
print(f"Amplitude of V1 = {cm.polar(x[1])[0]} Volts and the phase is = {cm.polar(x[1])[1] * 180 / np.pi} degrees")
print(f"Amplitude of V1 = {cm.polar(x[2])[0]} Volts and the phase is = {cm.polar(x[2])[1] * 180 / np.pi} degrees")

"""
Amplitude of V1 = 1.7014390658777336 Volts and the phase is = -5.469094970111936 degrees
Amplitude of V1 = 1.4806053465364062 Volts and the phase is = 11.583418604687067 degrees
Amplitude of V1 = 1.8607693200562134 Volts and the phase is = -4.164672651865924 degrees"""
