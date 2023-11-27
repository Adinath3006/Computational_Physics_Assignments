""" Exercise 7 """
"""All the results and graphs of the following code can be found in 'Outputs and Derivation' and 'Plots and Animations' directories"""
import numpy as np
import random
import matplotlib.pyplot as plt

# Define the lattice size and the number of iterations
N = 20
steps = 1000000

# Set the interaction constant J and the temperature T
J = 1
T = 1     

# Part A

def Energy(spin,J):
    """Calculate the energy of the Ising model on a square lattice.

    Arguments:
    spin -- a 2D numpy array of integers, representing the spins on the lattice.
    J -- a positive interaction constant.

    Returns:
    The total energy of the Ising model.
    """
    r,c = spin.shape
    energy = 0
    for i in range(r):
        for j in range(c):
            s = spin[i, j]
            """We need to sum the spins of the neighbouring 4 lattice points as per the formula. We also assume the periodic boundary 
            condition, i.e., for the lattice points in boundary the one set of neighbours are those on the opposite boundary."""
            neighbor_sum = spin[(i-1)%r, j] + spin[(i+1)%r, j] + spin[i, (j-1)%c] + spin[i, (j+1)%c] # a%b gives the modulo 
            energy += -J * s * neighbor_sum
    return energy

# Part B

l = np.log10(steps)

# Applying the Metropolis Algorithm
def metroplis_algorithm(T,J,run):
    """Calculates and plots the total magnetization using the Metropolis Algorithm
    
    Arguments:
    run -- the number of run
    T -- initial temperature value
    J -- interaction constant value
    
    Returns:
    The final value of total magnetization, the plot of magnetization vs time and the color plot of domains of magnetization
    """
    # Initialize the lattice with random spin values
    spin = np.random.choice([-1, 1], size = (N, N))
    r,c = spin.shape
    # Initialize an array which stores the sponatneous magentization            
    M = [] 
    # Storing the spin at t = 0
    spin_0 = np.copy(spin)
    
    for k in range(steps):
        # Choose a random spin to flip
        i,j = random.randrange(N),random.randrange(N)
        # Calculating the change in the energy
        
        """Here we don't use the function 'energy' to find the energy of the total spin state of the system rather find the change in 
        energy only on the random spin that is being flipped in the process, as the calling of function in each iteration requires the 
        program to compute the energy of the grid every time (1e+6 in our problem) 
        E1 = - J*spin[i,j]*( spin[(i-1)%r, j] + spin[(i+1)%r, j] + spin[i, (j-1)%c] + spin[i, (j+1)%c] ) + other terms
        E2 = - J*( -spin[i,j] )*( spin[(i-1)%r, j] + spin[(i+1)%r, j] + spin[i, (j-1)%c] + spin[i, (j+1)%c] ) + other terms
        
        dE = E2-E1 = 2*J*spin[i,j]*( spin[(i-1)%r, j] + spin[(i+1)%r, j] + spin[i, (j-1)%c] + spin[i, (j+1)%c] )"""
        
        dE = 2*J*spin[i,j]*(spin[(i-1)%r, j] + spin[(i+1)%r, j] + spin[i, (j-1)%c] + spin[i, (j+1)%c])
        # Applying the metropolis acceptance condition
        if random.random() < np.exp(-dE/T):
            # Accpet the flip
            spin[i,j] = -spin[i,j]
            M.append(np.sum(spin))
        else:   
            # Reject the flip
            M.append(np.sum(spin))
        
        # Storing the spin lattice at subsequent times
        if k <= int(10**(l/3)):
            spin_1 = np.copy(spin)
        elif k <= int(10**(2*l/3)):
            spin_2= np.copy(spin)
        else:
            spin_3 = np.copy(spin)
    
    # Printing the value of the total magnetization after completing all iterations
    print(f"The value of the total magnetization at T = {T} in run {run+1} is {M[-1]}")
            
    # Array containing the spin lattice at different times    
    spin_evo = [spin_0,spin_1,spin_2,(np.sign(M[-1]))*spin_3]
    
    # Plotting the total magnetization as a function of time    
    plt.plot(M)
    plt.title("Magnetization as a function of time")
    plt.xlabel("Time")
    plt.ylabel("Total Magnetization")
    ##plt.savefig(f"Q7_T_{T}_run_{run+1}")
    plt.show()
    
    # Plotting the colorplot of the various domains at different time intervals   
    xx, yy= np.meshgrid(range(N), range(N))
    fig, ax = plt.subplots(2, 2)
        
    for i in range(4):
        if i < 2:
            ax[0][i].pcolormesh(xx, yy, spin_evo[i])
            ax[0][i].set_title(f"t = {int(10**int(i*l/3))}")
        else:
            ax[1][i-2].pcolormesh(xx, yy, spin_evo[i])
            ax[1][i-2].set_title(f"t = {int(10**int(i*l/3))}")
    plt.subplots_adjust(wspace= 0.5,hspace=0.4)    
    fig.suptitle(f"Temperature = {T} K")
    #plt.savefig(f"Q7_domain_T_{T}_run_{run+1}")
    plt.show()
        
for i in range(1,4):
    for j in range(3):
        metroplis_algorithm(T = i,J = J,run= j)
        