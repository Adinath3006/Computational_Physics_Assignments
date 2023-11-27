""" Exercise 2 """
import sys

sys.path.insert(0,'.')

from res.Int_Methods import Composite_Integration

act_val = 4.4
print(f"The actual value of the integral is {act_val}")

# Part A

print("\n SIMPSON'S METHOD \n")

def f(x):
    return x**4 - 2*x + 1

val = Composite_Integration(f,1,0,2,10)
print("The approximate value for the integral using the Simpson's method with 10 slices is ",val)

# Part B

fract_error = (val - act_val)/act_val

print("The fractional error on numerical integration (Simpson) with 10 slices is {}".format(fract_error))

# Part C

val_100 = Composite_Integration(f,1,0,2,100)
fract_error_100 = (val_100 - act_val)/act_val
val_1000 = Composite_Integration(f,1,0,2,1000)
fract_error_1000 = (val_1000 - act_val)/act_val

print("The approximate value for the integral using the Simpson's method with 100 slices is ",val_100)
print("The fractional error on numerical integration (Simpson) with 100 slices is {}".format(fract_error_100))
print("The approximate value for the integral using the Simpson's method with 1000 slices is ",val_1000)
print("The fractional error on numerical integration (Simpson) with 1000 slices is {}".format(fract_error_1000))

"""Now we compute the integral using the Trapezoidal Rule"""

print("\n TRAPEZOIDAL METHOD \n")

Trap_Val = Composite_Integration(f,0,0,2,10)
Trap_Val_100 = Composite_Integration(f,0,0,2,100)
Trap_Val_1000 = Composite_Integration(f,0,0,2,1000)

Trap_fract_error = (Trap_Val - act_val)/act_val
Trap_fract_error_100 = (Trap_Val_100 - act_val)/act_val
Trap_fract_error_1000 = (Trap_Val_1000 - act_val)/act_val

print("The approximate value for the integral using the Trapezoidal method with 10 slices is ",Trap_Val)
print("The fractional error on numerical integration (Trapezoidal) with 10 slices is {}".format(Trap_fract_error))
print("The approximate value for the integral using the Trapezoidal method with 100 slices is ",Trap_Val_100)
print("The fractional error on numerical integration (Trapezoidal) with 100 slices is {}".format(Trap_fract_error_100))
print("The approximate value for the integral using the Trapezoidal method with 1000 slices is ",Trap_Val_1000)
print("The fractional error on numerical integration (Trapezoidal) with 1000 slices is {}".format(Trap_fract_error_1000))

"""
The actual value of the integral is 4.4

 SIMPSON'S METHOD 

The approximate value for the integral using the Simpson's method with 10 slices is  4.400426666666667
The fractional error on numerical integration (Simpson) with 10 slices is 9.696969696972666e-05
The approximate value for the integral using the Simpson's method with 100 slices is  4.400000042666668
The fractional error on numerical integration (Simpson) with 100 slices is 9.696969893724372e-09
The approximate value for the integral using the Simpson's method with 1000 slices is  4.400000000004267
The fractional error on numerical integration (Simpson) with 1000 slices is 9.697293473271367e-13

 TRAPEZOIDAL METHOD 

The approximate value for the integral using the Trapezoidal method with 10 slices is  4.50656
The fractional error on numerical integration (Trapezoidal) with 10 slices is 0.024218181818181812
The approximate value for the integral using the Trapezoidal method with 100 slices is  4.401066656
The fractional error on numerical integration (Trapezoidal) with 100 slices is 0.00024242181818179273
The approximate value for the integral using the Trapezoidal method with 1000 slices is  4.4000106666656
The fractional error on numerical integration (Trapezoidal) with 1000 slices is 2.4242421817452255e-06

Thus we can see that for both methods as we increase the number of slices the accuracy of the integral improves. Also for each every 
numver of slices the error in the integral is very less in the case of Simpson's method when compared to Trapezoidal method"""