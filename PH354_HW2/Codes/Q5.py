""" Exercise 5 """

def f(x):
    return x**4 - 2*x + 1

import sys

sys.path.insert(0,'.')

from res.Int_Methods import Composite_Integration

I_2 = Composite_Integration(f,0,0,2,20)
h_2 = 0.1

print("The value of the integral computed using the Trapezoidal method with 20 slices is:",I_2)

I_1 = Composite_Integration(f,0,0,2,10)
h_1 = 0.2

"""We know that c is given by c = (I_2 - I_1)/(h_1**2 - h_2**2)"""

c = (I_2 - I_1)/(h_1**2 - h_2**2)

error = c*h_2**2

print("The error computed using this method is:", abs(error))
print("Direct computation error is {}".format(abs(4.4 - I_2)))

"""
The value of the integral computed using the Trapezoidal method with 20 slices is: 4.426660000000001
The error computed using this method is: 0.02663333333333314
Direct computation error is 0.026660000000000572

The method suggested in this question uses tatylor expansion, where we only consider terms till power h^2 (starts with this) and omitting 
the higher order terms, whereas in the direct computation error we include all the terms in the expansion as we directly subtract the 
actual value from  the computed value. Hence the two do not agree perfectly as we have omitted higher order terms in this method.Thus 
this error used in this problem is called truncation error."""
