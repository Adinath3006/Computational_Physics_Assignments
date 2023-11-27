""" Exercise 7 """

# Part A

import numpy as np
import sys
sys.path.insert(0,'.')
from res.Int_Methods import Composite_Integration
from res.Romberg import *
def f(x):
    return (np.sin(np.sqrt(100*x)))**2

I = Composite_Integration(f,0,0,1,1)

""" We calculate the error on the integral using the method devised in problem 6. Error = (I_2 - I_1)*h2**2/(h_1**2 - h_2**2)"""

N = 1

print("Trapezoidal Method \n")
print("The value of the integral for {} slice is {}".format(N,I))

error = 1 # > 1e-6

while abs(error) > 1e-6:
    h_1 = 1/N
    N = 2*N
    h_2 =1/N
    I_N = Composite_Integration(f,0,0,1,N)
    error = (I_N - I)*h_2**2/(h_1**2 - h_2**2)
    print("The value of the integral for {} slice is {} with error {}".format(N,I_N,error))
    I = I_N

"""
Trapezoidal Method 

The value of the integral for 1 slice is 0.147979484546652
The value of the integral for 2 slice is 0.3252319078064746 with error 0.05908414108660753
The value of the integral for 4 slice is 0.5122828507233315 with error 0.06235031430561896
The value of the integral for 8 slice is 0.40299744847824825 with error -0.036428467415027734
The value of the integral for 16 slice is 0.43010336929474696 with error 0.009035306938832902
The value of the integral for 32 slice is 0.4484146657874698 with error 0.00610376549757428
The value of the integral for 64 slice is 0.45391293121537596 with error 0.0018327551426353856
The value of the integral for 128 slice is 0.45534850437280205 with error 0.0004785243858086985
The value of the integral for 256 slice is 0.45571126645324095 with error 0.00012092069347963141
The value of the integral for 512 slice is 0.4558021996516643 with error 3.031106614111619e-05
The value of the integral for 1024 slice is 0.45582494813241997 with error 7.582826918558124e-06
The value of the integral for 2048 slice is 0.4558306362016465 with error 1.8960230755057002e-06
The value of the integral for 4096 slice is 0.45583205827827056 with error 4.740255413563747e-07

Thus the target accuracy is reached at 2048 with error 1.8960230755057002e-06"""

# Part B

print("Romberg Integration \n")

r,j,e = romberg(0,1,1e-6,20,f)

for i in range(0,j+1):
    for k in range(0,i):
        if k == i-1:
            print(r[i][k])  
        else:
            print(r[i][k],end=' ')

print(" The for {} slices is {} with error {} is the final approximation".format(2**j,r[j][j],e[j]))

"""
Romberg Integration

0.3252319078064746
0.5122828507233315 0.5746331650289505
0.4029974484782483 0.3665689810632206 0.3526980354655053
0.43010336929474696 0.4391386762335798 0.44397665591160373 0.4454255229028117
0.4484146657874699 0.45451843128504427 0.4555437482884752 0.45572735292937794 0.45576775226281546
0.4539129312153758 0.4557456863580111 0.45582750336287553 0.45583200741167557 0.4558324178214101 0.4558324810330998
 The for 64 slices is 0.4558324944613787 with error 1.3428278877370225e-08 is the final approximation"""