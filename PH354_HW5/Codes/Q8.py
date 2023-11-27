import numpy as np
import random
import matplotlib.pyplot as plt
"""All the results and graphs of the following code can be found in 'Outputs and Derivation' and 'Plots and Animations' directories"""
# Part A

# define the objective function
def f(x):
    return x**2 - np.cos(4*np.pi*x)

# define the simulated annealing algorithm
def simulated_annealing(x0, T0, Tf, tau, f, sigma):
    """ Performs simulated annealing method to find the minima
    
    Arguments:
    x0 -- initial value
    T0 -- initial temperature
    Tf -- final temperature
    tau --  time constant
    f -- objective function
    
    Returns:
    x -- minima point of the function
    xs -- array of values of x for each iteration
    """
    x = x0
    T = T0
    xs = [x]
    while T > Tf:
        dx = random.gauss(0, sigma)
        x_new = x + dx
        dE = f(x_new) - f(x)
        if np.exp(-dE/T) > random.uniform(0, 1):
            x = x_new
        xs.append(x)
        T *= np.exp(-tau)
    return x, xs

x0 = 2
T0 = 10
Tf = 1e-3
tau = 1e-4

x_min, xs = simulated_annealing(x0, T0, Tf, tau, f, sigma=1)
print(f"Minimum found at x = {x_min:.4f}")

plt.plot(xs, ".", label="x values")
plt.axhline(x_min, color="r", label="minimum")
plt.legend()
plt.title("Minimum of a function x^2 - cos 4πx")
plt.savefig("Q8_a.png")
plt.show()

# Part B

# define the objective function
def g(x):
    return np.cos(x) + np.cos(np.sqrt(2)*x) + np.cos(np.sqrt(3)*x)

x0 = 18 
T0 = 1
Tf = 1e-3
tau = 1e-4

x_min_1, xs_1 = simulated_annealing(x0, T0, Tf, tau, g, sigma=0.1)
print(f"Minimum found at x = {x_min_1:.4f}")

plt.plot(xs_1, ".", label="x values")
plt.axhline(x_min_1, color="r", label="minimum")
plt.legend()
plt.title("Minimum of a function cos x + cos √2x + cos √3x")
plt.savefig("Q8_b.png")
plt.show()