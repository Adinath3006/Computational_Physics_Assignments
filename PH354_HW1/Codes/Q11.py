""" Exercise 11 """

import numpy as np

prime = []

"""The first prime: 2"""
prime.append(2)

def Append_Prime(n):
    if n != 2:       
        for i in range(3,n+1):
            j = 0
            
            """The additional conditon imposes that the loop runs only till the prime factor is less than or equal to sqrt(n)"""

            while j < len(prime) and prime[j] <= np.sqrt(n):  
                if i % prime[j] == 0:
                    j = -1
                    break
                else:
                    j = j+1
            
            if j >= 0:
                prime.append(i)

Append_Prime(10000)
print(prime)

"""Refer the complied output pdf to view the output"""
