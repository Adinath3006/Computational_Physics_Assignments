""" Exercise 4 """
"""All the results and graphs of the following code can be found in 'Outputs and Derivation' and 'Plots and Animations' directories"""
import numpy as np
import random

# Part A
# Hit or Miss method

def f(x):
    return (np.sin(1/((x)*(2-x))))**2

N = 10000
k = 0

for n in range(N):
    x = random.uniform(0,2)
    y = random.uniform(0,1)
    if y < f(x):
        k += 1
        
"""We know that using the hit or miss method we can evaluate the integral by I = kA/N, here our region of interest is x ∈ [0,2] and
y ∈ [0,1], hence the area A is 2."""

I_hit_miss = k*2/N

"""The expected error on the integral is given by sqrt((I*(A-I))/N)"""

error = np.sqrt((I_hit_miss*(2-I_hit_miss))/N) 

print("The value of the integral evaluated using the hit-or-miss method is {} with an error of {:.5f} %".format(I_hit_miss,error*100))

"""
The value of the integral evaluated using the hit-or-miss method is 1.4544 with an error of 0.89079 %"""

# Part B
# Mean Value Method

"""Using the mean value method the integral is evaluated through the formula I = ((b-a)/N)*Σf(xi) for N points, where again the expected
error in the integral is given by ((b-a)/N)*(sqrt(N*var_f))"""

b,a = 2,0

sum_avg = 0
sum_avg_2 = 0
for n in range(N):
    xn = random.uniform(0,2)
    sum_avg += f(xn)
    sum_avg_2 += f(xn)**2

var_f = sum_avg_2/N - (sum_avg/N)**2

I_mean_value = (b-a)*sum_avg/N

error_mean = ((b-a)/N)*(np.sqrt(N*var_f))

print("The value of the integral evaluated using the mean value method is {:.5f} with an error of {:.5f} %".format(I_mean_value,error_mean*100))

"""
The value of the integral evaluated using the mean value method is 1.45131 with an error of 0.52757 %"""

"""
Hence we can see that the integral evaluated using the mean value method is more accurate than hit or miss method which is apparent from 
the error in the integral as 0.52757 % < 0.89079 %. """