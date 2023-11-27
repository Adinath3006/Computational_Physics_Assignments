""" Exercise 12 """

# Part A

""" We generate the catalan numbers recursively """

def Catalan_Num(i):
    if i == 0:
        return 1
    else:
        return ((4*i - 2)/(i + 1))*Catalan_Num(i-1)

print("The 100th Catalan Number is: ",int(Catalan_Num(100)))

"""The 100th Catalan Number is:  896519947090131678185430741499021921911623568450622849024"""

# Part B

""" We obtain the GCD of two numbers recursively """

def GCD(m,n):
    if n == 0:
        return m
    else:
        return GCD(n,m%n)

print("The GCD of 108 and 192 is ",GCD(192,108))

"""The GCD of 108 and 192 is  12"""