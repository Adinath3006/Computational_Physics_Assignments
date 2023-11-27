""" Exercise 2 """

# Part A

def f(x):
    return x*(x-1)

def derivative_diff(f,x,delta):
    return (f(x+delta)-f(x))/(delta)

print(f"The derivative of f at x = 1 computed using this method with delta 1e-{2} is {derivative_diff(f,1,1e-2)}")

"""
The derivative of f at x = 1 computed using this method is 1.010000000000001. 
The derivative of f at x = 1 computed analytically is 1. We can observe that the two values agree upto 2 significant figures. They don't
agree perfectly because the analytic solution is the one at which Delta tends to 0, here our Delta is 0.01 which is considerably
greater than 0. Hence they dont agree perfectly."""

# Part B

for i in range(2,8):
    print(f"The derivative of f at x = 1 computed using this method with delta 1e-{2*i} is {derivative_diff(f,1,10**(-2*i))}")

"""
The derivative of f at x = 1 computed using this method with delta 1e-2 is 1.010000000000001
The derivative of f at x = 1 computed using this method with delta 1e-4 is 1.0000999999998899
The derivative of f at x = 1 computed using this method with delta 1e-6 is 1.0000009999177333
The derivative of f at x = 1 computed using this method with delta 1e-8 is 1.0000000039225287
The derivative of f at x = 1 computed using this method with delta 1e-10 is 1.000000082840371
The derivative of f at x = 1 computed using this method with delta 1e-12 is 1.0000889005833413
The derivative of f at x = 1 computed using this method with delta 1e-14 is 0.9992007221626509"""

"""The value closest to the actual value is when delta is 1e-8 with the derivative being 1.0000000039225287, we can the values deviating
from 1 in an increasing fashion, this caused because of the truncation error which arises as a result of dividing with very small values
namely 1e-10, 1e-12, 1e-14."""