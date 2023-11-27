""" Exercise 3 """
"""All the results and graphs of the following code can be found in 'Outputs and Derivation' and 'Plots and Animations' directories"""
import random
import matplotlib.pyplot as plt

L = 101 # side of a square

i_pos,j_pos = (L-1)/2,(L-1)/2

def point_assign(dir,i,j):
    if dir == 1:
        return [i+1,j]
    elif dir == 2:
        return [i,j+1]
    elif dir == 3:
        return [i-1,j]
    else:
        return [i,j-1]
        
def brownian(i_pos,j_pos,N):
    # Initializing the array which stores the position of particle
    i = []
    j = []
    i.append(i_pos)
    j.append(j_pos)
    for step in range(N):
    # Assign direction for the next point according to the current location
        if i_pos == 0:
            if j_pos == 0:
                dir = random.choice([1,2])
            elif j_pos == L:
                dir = random.choice([1,4])
            else:
                dir = random.choice([1,2,4])
        elif i_pos == L:
            if j_pos == 0:
                dir = random.choice([2,3])
            elif j_pos == L:
                dir = random.choice([3,4])
            else:
                dir = random.choice([2,3,4])
        else:
            if j_pos == 0:
                dir = random.choice([1,2,3])
            elif j_pos == L:
                dir = random.choice([1,3,4])
            else:
                dir = random.choice([1,2,3,4])
        # Make the corresponding movement
        move = point_assign(dir,i_pos,j_pos)
        i_pos = move[0]
        j_pos = move[1]
        i.append(i_pos)
        j.append(j_pos)
    return i,j

i1,j1 = brownian(i_pos,j_pos,N=1000)        

plt.plot(i1,j1)
plt.title("Brownian Motion N = 1000")
plt.xlim(0,101)
plt.ylim(0,101)
plt.savefig("Q3_thousand.png")
plt.show()

i2,j2 = brownian(i_pos,j_pos,N=1000000)        

plt.plot(i2,j2)
plt.title("Brownian Motion N = 1000000")
plt.xlim(0,101)
plt.ylim(0,101)
plt.savefig("Q3_million.png")
plt.show()