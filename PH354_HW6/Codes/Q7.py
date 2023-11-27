""" Exercise 7 """

# Note: The results, derivations and comments asked for each questions is in the 'Outputs and Derivation' directory.
# Note: The plots for each of the questions is in the 'Plots and Animations' directory

import sympy as smp
import numpy as np
import sys
import matplotlib.pyplot as plt
sys.path.insert(0,'.')
from modules.RK4_system import *

# Part A

def coupled_oscillator(k , mass , N , t_init , t_fin , omega, intervals , init, collate_graph = True):
    """ Calculates the approximate solution of a system of coupled harmonic oscillators using RK4 method
    
    Arguments:
    k -- spring constant
    mass -- mass of the particles
    N -- number of particles
    t_init -- initial time
    t_fin -- final time
    omega -- frequency of the driving force
    intervals -- value of N in the N+1 evenly spaced intervals
    init -- array containing the initial values of the system
    collate_graph -- boolean value specifying if the graphs of different particles should be collated
    
    Returns:
    The graphs of the position of individual particles over time
    """
    
    W = smp.symbols(f'W(0:{2*N+1})')
    """Let the variables be t, ξ1, ξ2,..., ξN, ξ'1, ξ'2,..., ξ'N"""
    
    # defining the system of differential equations
    fsys = []
    for i in range(1,N+1):
        fsys.append(W[N+i])
    for i in range(1,N+1):
        if i == 1:
            fsys.append((1/mass)*(k*(W[2] - W[1]) + smp.cos(omega*W[0])))
        elif i == N:
            fsys.append((1/mass)*(k*(W[N-1] - W[N])))
        else:
            fsys.append((1/mass)*(k*(W[i+1] - W[i]) + k*(W[i-1] - W[i])))
    
    # solving the differential equation
    soln = system_solver(fsys = fsys, a = t_init, b = t_fin, m = 2*N, N = intervals, init = init)
    
    # plotting graphs
    t_plot = np.linspace(t_init, t_fin, intervals+1)
    if collate_graph:
        for i in range(0,N):
            x_plot = soln[:,i]
            plt.plot(t_plot, x_plot, label = f'$x_{i+1}$')
        plt.title(f"System of coupled oscillators")
        plt.xlabel("t")
        plt.ylabel("x")
        plt.grid()
        plt.legend()
        plt.savefig("Q7.png")
        plt.show()
    else:
        for i in range(0,N):
            x_plot = soln[:,i]
            plt.plot(t_plot, x_plot, label = f'$x_{i+1}$')
            plt.title(f"System of coupled oscillators")
            plt.xlabel("t")
            plt.ylabel("x")
            plt.grid()
            plt.legend()
            plt.savefig(f"Q7_ξ_{i+1}.png")
            plt.show()
            
init = []
for i in range(10):
    init.append(0)
coupled_oscillator(k = 6 , mass = 1 , N = 5 , t_init  = 0 , t_fin = 20 , omega = 2 , intervals = 500 , init = init)