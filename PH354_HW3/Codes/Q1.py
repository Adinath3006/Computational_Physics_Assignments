""" Exercise 1 """

# Part A

import cmath

a = float(input("Enter the value of 'a' in ax^2 + bx + c :"))
b = float(input("Enter the value of 'b' in ax^2 + bx + c :"))
c = float(input("Enter the value of 'c' in ax^2 + bx + c :"))

"""Using the formula for finding the root of a quadratic equation: x = (-b ± sqrt(b**2 - 4*a*c))/(2*a)"""

x1 = (-b + cmath.sqrt(b**2 - 4*a*c))/(2*a)
x2 = (-b - cmath.sqrt(b**2 - 4*a*c))/(2*a)

if x1.imag == 0:
    x1 = x1.real
if x2.imag == 0:
    x2 = x2.real
    
print(f"The roots of the quadratic equation {a}x^2 + {b}x + {c} are {x1} and {x2}")

"""
Enter the value of 'a' in ax^2 + bx + c :0.001
Enter the value of 'b' in ax^2 + bx + c :1000
Enter the value of 'c' in ax^2 + bx + c :0.001
The roots of the quadratic equation 0.001x^2 + 1000.0x + 0.001 are -9.999894245993346e-07 and -999999.999999"""

# Part B

x_new_1 = (2*c)/(-b - cmath.sqrt(b**2 - 4*a*c))
x_new_2 = (2*c)/(-b + cmath.sqrt(b**2 - 4*a*c))

if x_new_1.imag == 0:
    x_new_1 = x_new_1.real
if x_new_2.imag == 0:
    x_new_2 = x_new_2.real

print(f"The roots of the quadratic equation {a}x^2 + {b}x + {c} using the new method are {x_new_1} and {x_new_2}")

"""
Enter the value of 'a' in ax^2 + bx + c :0.001
Enter the value of 'b' in ax^2 + bx + c :1000
Enter the value of 'c' in ax^2 + bx + c :0.001
The roots of the quadratic equation 0.001x^2 + 1000.0x + 0.001 are -9.999894245993346e-07 and -999999.999999
The roots of the quadratic equation 0.001x^2 + 1000.0x + 0.001 using the new method are -1.000000000001e-06 and -1000010.5755125057"""


"""We now compute f(xi) for each of the roots found in both cases"""

def f(x):
    return a*x**2 + b*x + c

print(f"f({x1}) using method given in Part A is {f(x1)}")
print(f"f({x2}) using method given in Part A is {f(x1)}")
print(f"f({x_new_1}) using method given in Part B is {f(x_new_1)}")
print(f"f({x_new_2}) using method given in Part B is {f(x_new_2)}")

"""
f(-9.999894245993346e-07) using method given in Part A is 1.0575401665491313e-08
f(-999999.999999) using method given in Part A is 1.0575401665491313e-08
f(-1.000000000001e-06) using method given in Part B is 0.0
f(-1000010.5755125057) using method given in Part B is 10575.62534720993"""

"""The value of the function f(-1000010.5755125057) diverges from 0 by a very big margin because (-b + sqrt(b**2 - 4*a*c)) in the eqauation
x = (2*c)/(-b ∓ sqrt(b**2 - 4*a*c)) is a very small number which causes trunctation error when dividing it, hence the root diverges """

# Part C

def Quad_root_solver(func):

    p1 = (-b + cmath.sqrt(b**2 - 4*a*c))/(2*a)
    q1 = (-b - cmath.sqrt(b**2 - 4*a*c))/(2*a)

    p2 = (2*c)/(-b - cmath.sqrt(b**2 - 4*a*c))
    q2 = (2*c)/(-b + cmath.sqrt(b**2 - 4*a*c))

    """We check the closeness of the value of the function at the computed roots to zero"""

    if abs(func(p1)) < abs(func(p2)):
        root_1 = p1
    else:
        root_1 = p2

    if abs(func(q1)) < abs(func(q2)):
        root_2 = q1
    else:
        root_2 = q2

    if root_1.imag == 0:
        root_1 = root_1.real
    if root_2.imag == 0:
        root_2 = root_2.real

    return root_1,root_2

print(Quad_root_solver(f))

"""
Thus the roots obtained using the new modified method are (-1.000000000001e-06, -999999.999999) we check the function values 
f(-999999.999999) using method given in Part A is 1.0575401665491313e-08
f(-1.000000000001e-06) using method given in Part B is 0.0 """