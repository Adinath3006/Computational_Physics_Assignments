""" Exercise 8 """

import numpy as np
import sys
sys.path.insert(0,'.')
from res.Int_Methods import Composite_Integration

def f(x):
    return (np.sin(np.sqrt(100*x)))**2

I = Composite_Integration(f,1,0,1,2)

""" We calculate the error on the integral using the method devised in problem 6. Error = (I_2 - I_1)*h2**2/(h_1**2 - h_2**2)"""

N = 2

print("Composite Simpsons \n")
print("The value of the integral for {} slice is {}".format(N,I))

error = 1 # > 1e-6

while abs(error) > 1e-6:
    h_1 = 1/N
    N = 2*N
    h_2 =1/N
    I_N = Composite_Integration(f,1,0,1,N)
    error = (I_N - I)*h_2**4/(h_1**4 - h_2**4)
    print("The value of the integral for {} slice is {} with error {}".format(N,I_N,error))
    I = I_N

"""
Composite Simpsons 

The value of the integral for 2 slice is 0.38431604889308213
The value of the integral for 4 slice is 0.5746331650289502 with error 0.012687807742391206
The value of the integral for 8 slice is 0.36656898106322056 with error -0.013870945597715312
The value of the integral for 16 slice is 0.4391386762335799 with error 0.004837979678023955
The value of the integral for 32 slice is 0.4545184312850443 with error 0.0010253170034309625
The value of the integral for 64 slice is 0.45574568635801105 with error 8.181700486444842e-05
The value of the integral for 128 slice is 0.45582702875861086 with error 5.422826706654357e-06
The value of the integral for 256 slice is 0.45583218714672064 with error 3.4389254065144335e-07

Thus the target accuracy is reached at 128 with error 5.422826706654357e-06

Thus we can see that the target accuracy is reached faster than trapezoidal method with N = 128 but it is still larger than Romberg 
integration which has N = 64
"""