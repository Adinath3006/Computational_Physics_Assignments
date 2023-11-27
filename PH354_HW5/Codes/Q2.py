""" Exercise 2 """
"""All the results and graphs of the following code can be found in 'Outputs and Derivation' and 'Plots and Animations' directories"""
import numpy as np
import matplotlib.pyplot as plt
import random

N = 10000
dt = 1 # sec

tau_Bi = 46*60 # sec
tau_Tl = 2.2*60 # sec
tau_Pb = 3.3*60 # sec

"""The probability that a particle decays in time t and t + dt is p(t) = 1 - 2^(-t/τ) and p(t+dt). Thus the probabilty that the particle
will decay between time t and t + dt is p(t+dt) - p(t) = d/dt(p(t))*dt = log(2)*(2**(-t/τ))/τ*dt. After discretizing the time, the 
probability that a particle decays in time t and t + Δt is p(t) = log(2)*(2**(-t/τ))/τ*Δt, where Δt is 1 sec in our case."""

# Initializing the number of particles
N_Bi = [] # Bi213
N_Tl = [] # Tl209
N_Pb = [] # Pb209
Time = []
N_Bi_fin = [] # Bi209

Bi = N # Bi213
Tl = 0 # Tl209
Pb = 0 # Pb209
Final = 0 # Bi209

T = 20000

for t in range(T):
    # Pb decay
    Pb_decay = np.random.binomial(n = Pb, p = np.log(2)*(2**(-t/tau_Pb))/tau_Pb)
    Pb -= Pb_decay
    Final += Pb_decay
    # Tl decay
    Tl_decay = np.random.binomial(n = Tl, p = np.log(2)*(2**(-t/tau_Tl))/tau_Tl)
    Tl -= Tl_decay
    Final += Tl_decay
    # Bi decay
    Bi_decay = np.random.binomial(n = Bi, p = np.log(2)*(2**(-t/tau_Bi))/tau_Bi)
    # Two pathways
    branch = np.random.binomial(n = Bi_decay, p = 2.09 / 100)
    Bi -= Bi_decay
    Tl += branch
    Pb += Bi_decay - branch
    # Storing the result of decay after 1 sec 
    N_Bi.append(Bi)
    N_Tl.append(Tl)
    N_Pb.append(Pb)
    N_Bi_fin.append(Final)
    Time.append(t)

# Plotting the graph
plt.plot(N_Bi,label="Bi213")
plt.plot(N_Tl,label="Tl209")
plt.plot(N_Pb,label="Pb209")
plt.plot(N_Bi_fin,label="Bi209")
plt.xlabel("Time (in sec)")
plt.ylabel("Number of particles")
plt.title("Decay of Bi213 isotope")
plt.grid()
plt.legend()
plt.savefig("Q2.png")
plt.show()