""" Exercise 9 """

Z = int(input("Enter the Atomic Number: "))
A = float(input("Enter the Mass Number: "))

def Binding_Energy(A,Z):
    a1 = 15.67
    a2 = 17.23
    a3 = 0.75
    a4 = 93.2
    if A%2 == 1:
        a5 = 0
        return a1*A - a2*(A**(2/3)) - a3*((Z**2)/(A**(1/3))) - a4*((A-2*Z)**2/A) + a5*(1/(A**(1/2)))
    elif A%2 == 0 and Z%2 == 0:
        a5 = 12
        return a1*A - a2*(A**(2/3)) - a3*((Z**2)/(A**(1/3))) - a4*((A-2*Z)**2/A) + a5*(1/(A**(1/2)))
    elif A%2 == 0 and Z%2 == 1:
        a5 = -12
        return a1*A - a2*(A**(2/3)) - a3*((Z**2)/(A**(1/3))) - a4*((A-2*Z)**2/A) + a5*(1/(A**(1/2)))

B = Binding_Energy(A,Z)

# Part A

print(f"The binding energy of an atom with A = {A} and Z = {Z} is {B} MeV")

"""The binding energy of an atom with A = 58.0 and Z = 28 is 493.93560680136824 MeV"""

# Part B

print(f"The binding energy per nucleon of an atom with A = {A} and Z = {Z} is {B/A} MeV")

"""The binding energy per nucleon of an atom with A = 58.0 and Z = 28 is 8.516131151747729 MeV"""

# Part C

def Stable_A(Z):
    for a in range(Z,3*Z+1):
        if a == Z:
            B_stable = Binding_Energy(a,Z)/a
            A_stable = a
        else:
            if Binding_Energy(a,Z)/a > B_stable:
                B_stable = Binding_Energy(a,Z)/a
                A_stable = a
            else:
                continue
    return [A_stable,B_stable]

print("The most stable mass number for Z = {} is A = {} and the corresponding binding energy per nucleon is {:.5f} MeV".format(Z,Stable_A(Z)[0],Stable_A(Z)[1]))

"""The most stable mass number for Z = 28 is A = 58 and the corresponding binding energy per nucleon is 8.51613 MeV"""

# Part D

Most_stable_BE = 0
Most_stable_z = 0
Most_stable_A = 0

for z in range(1,101):
    A_des = Stable_A(z)
    if Most_stable_BE < A_des[1]:
        Most_stable_BE = A_des[1]
        Most_stable_A = A_des[0]
        Most_stable_z = z
    print("The maximum binding energy per nucleon for Z = {} is {:.4f} with corresponding A = {}".format(z,A_des[1],A_des[0]))

print("The element with the maximum binding energy per nucleon is Z = {} with A = {} and corresponding binding energy per nucleon is {:.5f} MeV".format(Most_stable_z,Most_stable_A,Most_stable_BE)) 

"""Refer the complied output pdf to view the output"""