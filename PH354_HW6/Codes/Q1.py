""" Exercise 1 """

# Note: The results, derivations and comments asked for each questions is in the 'Outputs and Derivation' directory.
# Note: The plots for each of the questions is in the 'Plots and Animations' directory

import sys
import numpy as np
import math
import matplotlib.pyplot as plt
sys.path.insert(0,'.')
from modules.RK4 import *

# Part A

# bounds on t
t_init = 0
t_fin = 10
# initial condition 
V_out_0 = 0
# step size
h = 0.01

for RC in [0.01,0.1,1]:
    # defining the function f(t,y)
    def f(t,V_out):
        if math.floor(2*t) % 2 == 0:
            return (1/RC)*(1 - V_out)
        else:
            return (1/RC)*(-1 - V_out)    
        
    y_plot = Runge_Kutta(f = f, a = t_init, b = t_fin, y_0 = V_out_0, h = h)
    t_plot = np.arange(t_init,t_fin+h,h)
    
    plt.plot(t_plot,y_plot)
    plt.title(f"Low pass filter, RC = {RC}")
    plt.xlabel("Time (in sec)")
    plt.ylabel("V$_{out}$ (in Volts)")
    plt.grid()
    #plt.savefig(f"Q1_RC_{RC}.png")
    plt.show()