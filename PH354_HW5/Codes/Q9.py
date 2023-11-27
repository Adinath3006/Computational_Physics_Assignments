""" Exercise 9 """
"""All the results and graphs of the following code can be found in 'Outputs and Derivation' and 'Plots and Animations' directories"""
from random import randint, choice, random
import matplotlib.pyplot as plt
import matplotlib.animation as ani
import numpy as np
        
def dimer_covering(T_0, i_max, j_max, title, exp_cooling = False, tau = 5, max_iter = 10**3, update_freq = 30):
    """Solving the dimer covering problem using simulated annealing
    
    Arguments:
    T_0 -- Initial temperature
    i_max -- Length of the lattice grid along x axis
    j_max -- Length of the lattice grid along y axis
    title -- A string containing the title of gif
    exp_cooling -- Boolean variable which specifies if the exponential cooling should be performed
    tau -- A positive constant
    max_iter -- Maximum iterations to be performed
    update_freq -- Frequency of updating the animation
    
    Returns:
    animation -- Gif of the dimer 
    len(dimer_pos) -- Total number of dimers in the lattice
    """
    # Initializing an empty lattice which stores the dimer nodes and empty nodes as 1's and 0's respectively
    lattice = np.zeros((i_max,j_max))

    # Array to store the position of dimers in the lattice
    dimer_pos = []
    
    fig = plt.figure()
    ax = plt.gca()
    x_plot = np.arange(-0.5, i_max)
    y_plot = np.arange(-0.5, j_max)
    
    # Initial empty grid with no dimer occupied
    def init_lattice():
        ax.set_xlim(-0.6, i_max - 0.4)
        ax.set_ylim(-0.6, j_max - 0.4)
        ax.vlines(x_plot, ymin = -0.6, ymax = j_max - 0.4, color = 'blue', linewidth = 0.2)
        ax.hlines(y_plot, xmin = -0.6, xmax = i_max - 0.4, color = 'blue', linewidth = 0.2)
        
    def animate(k):
        for l in range(update_freq):
            if exp_cooling:
                T = T_0 * np.exp(-(k*update_freq + l) / tau)
            else:
                T = T_0
            beta = 1 / T

            i = randint(0,i_max-1)
            j = randint(0,j_max-1)
            # Computing the increment in the index i
            if i == 0:
                rand_i = choice([0,1])
            elif i == i_max-1:
                rand_i = choice([-1,0])
            else:
                rand_i = choice([-1,0,1])
            # Computing the increment in the index j
            if rand_i == 0:
                if j == 0:
                    rand_j = 1
                elif j == j_max-1:
                    rand_j = -1
                else:
                    rand_j = choice([-1,1])
            else:
                rand_j = 0        

            if [[i,j], [i+rand_i,j+rand_j]] in dimer_pos:
                """Note: Here we have not explicitly computed dE because in the Markov Chain we remove a dimer hence the energy which
                is the negative of the sum of all dimers is then increased by one. Thus dE = E_fin - E_init = 1. Thus the metropolis 
                acceptance is exp(-beta*(dE=1))"""
                if random() < np.exp(-beta):
                    dimer_pos.remove([[i,j], [i+rand_i,j+rand_j]])
                    lattice[i][j] = 0
                    lattice[i+rand_i][j+rand_j] = 0
                    
            elif [[i+rand_i,j+rand_j],[i,j]] in dimer_pos:
                """Note: Here we have not explicitly computed dE because in the Markov Chain we remove a dimer hence the energy which
                is the negative of the sum of all dimers is then increased by one. Thus dE = E_fin - E_init = 1. Thus the metropolis 
                acceptance is exp(-beta*(dE=1))"""
                if random() < np.exp(-beta):
                    dimer_pos.remove([[i+rand_i,j+rand_j],[i,j]])
                    lattice[i][j] = 0
                    lattice[i+rand_i][j+rand_j] = 0
            
            elif lattice[i][j] == 0 and lattice[i+rand_i][j+rand_j] == 0:
                """Note: Here we have not explicitly computed dE because in the Markov Chain we add a dimer which then decreases the 
                energy of the system by one, thus is automatically accepted by the metropolis acceptance as dE < 0"""
                dimer_pos.append([[i,j], [i+rand_i,j+rand_j]])
                lattice[i][j] = 1
                lattice[i+rand_i][j+rand_j] = 1
        
        ax.cla()
        ax.set_title(title)
        ax.vlines(x_plot, ymin = -0.6, ymax = j_max - 0.4, color = 'blue', linewidth = 0.2)
        ax.hlines(y_plot, xmin = -0.6, xmax = i_max - 0.4, color = 'blue', linewidth = 0.2)
        for d in dimer_pos:
            i1 = d[0][0]
            i2 = d[1][0]
            j1 = d[0][1]
            j2 = d[1][1]
            ax.plot([i1, i2], [j1, j2], color = 'black', marker = '.', markersize = 4, linewidth = 0.75)
    
    animation = ani.FuncAnimation(fig, animate, frames = max_iter // update_freq, interval = 10**(-2), init_func = init_lattice, repeat = False)
    plt.show()
    return animation, len(dimer_pos)

animate_1, tot_dimer_1 = dimer_covering(T_0= 1, i_max=  50, j_max= 50, title = "Simulation of Dimer Covering Problem without cooling", exp_cooling = False, max_iter= 10**4, update_freq= 100)
animate_2, tot_dimer_2 = dimer_covering(T_0= 1, i_max=  50, j_max= 50, title= "Simulation of Dimer Covering problem with cooling: tau = 10^4", exp_cooling= True, max_iter= 10**5, update_freq= 1000, tau= 10**4)
animate_3, tot_dimer_3 = dimer_covering(T_0= 1, i_max=  50, j_max= 50, title= "Simulation of Dimer Covering problem with cooling: tau = 10^2", exp_cooling= True, max_iter= 10**4, update_freq= 100, tau= 10**2)
#animate_1.save(r"dimer_sim_without_cooling.gif", fps = 60)
#animate_2.save(r"dimer_sim_with_cooling_tau_10000.gif", fps = 60)
#animate_3.save(r"dimer_sim_with_cooling_tau_100.gif", fps = 60)


print(f"The number of dimers in the first simulation (without cooling) is: {tot_dimer_1}")
print(f"The number of dimers in the second simulation (with slow cooling) is: {tot_dimer_2}")
print(f"The number of dimers in the third simulation (with fast cooling) is: {tot_dimer_3}")