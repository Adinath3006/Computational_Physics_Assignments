""" Exercise 18 """

import cmath
import math
import numpy as np

def m_derivative(z,m,f,N):

    # Computing the sum
    sum = 0
    for k in range (0,N):
        z_k = cmath.exp(1j*(2*np.pi*k/N))
        sum += f(z_k)*cmath.exp(-1j*(2*np.pi*m*k/N))
    
    return (math.factorial(m)/N)*sum

def f(z):
    return math.e**(2*z)

print("The mth derivative of the function for each m is as follows:")

for k in range(1,21):
    print("The {}th derivative at z = 0 is {}".format(k,m_derivative(0,k,f,1000).real))

"""
The mth derivative of the function for each m is as follows:
The 1th derivative at z = 0 is 1.9999999999999978
The 2th derivative at z = 0 is 3.9999999999999982
The 3th derivative at z = 0 is 7.999999999999985
The 4th derivative at z = 0 is 16.0
The 5th derivative at z = 0 is 32.00000000000001
The 6th derivative at z = 0 is 63.999999999999964
The 7th derivative at z = 0 is 127.99999999999869
The 8th derivative at z = 0 is 255.9999999999803
The 9th derivative at z = 0 is 511.999999999951
The 10th derivative at z = 0 is 1023.9999999991169
The 11th derivative at z = 0 is 2047.9999999591387
The 12th derivative at z = 0 is 4095.9999999328834
The 13th derivative at z = 0 is 8192.000002590277
The 14th derivative at z = 0 is 16383.999980568917
The 15th derivative at z = 0 is 32767.998795431035
The 16th derivative at z = 0 is 65535.997189001006
The 17th derivative at z = 0 is 131072.02920286346
The 18th derivative at z = 0 is 262143.04369028722
The 19th derivative at z = 0 is 524211.3389932175
The 20th derivative at z = 0 is 1048164.0241144444"""