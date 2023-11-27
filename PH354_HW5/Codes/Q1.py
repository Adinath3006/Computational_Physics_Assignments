""" Exercise 1 """
"""All the results and graphs of the following code can be found in 'Outputs and Derivation' and 'Plots and Animations' directories"""
# Part A

import random

rand = random.randint(1,6)

print(f"The output obtained from a dice roll is: {rand}")

# Part B

N = 1000000
success = 0
for i in range(N):
    dice_1 = random.randint(1,6)
    dice_2 = random.randint(1,6)
    if (dice_1 == 6 and dice_2 == 6):
        success += 1
        
print(f"The fraction of times that we obtain a double six is {success/N}")

"""
The output obtained from a dice roll is: 6
The fraction of times that we obtain a double six is 0.02783.

We can see that this fraction is very close to the theoretical value of the probability of the given event, 1/36 approximation 0.027777
"""