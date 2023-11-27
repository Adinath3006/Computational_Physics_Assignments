""" Exercise 11 """

# Note: The results, derivations and comments asked for each questions is in the 'Outputs and Derivation' directory.
# Note: The plots for each of the questions is in the 'Plots and Animations' directory

import numpy as np
import matplotlib.pyplot as plt
import sys
sys.path.insert(0, '.') 
from modules.rk4_system_numerical import *
from modules.secant import *
from modules.Int_Methods import *
from scipy.constants import hbar, electron_mass, electron_volt

V_0 = 50*electron_volt #eV
a = 1e-11 # m

x_init = -10*a
x_final = 10*a
N = 1000
init = [0,1]

def boundary_psi(E):
    def f1(W):
        return W[2]
    def f2(W):
        return -(E - V_0 *(W[0]/a)**2)* W[1]* 2*electron_mass/hbar**2 
    fsys = [f1,f2]
    soln = system_solver(fsys,a=x_init,b=x_final,m=2,N=N,init=init)
    return soln[N][0]

E_0 = Secant(100*electron_volt, 200*electron_volt, 0.1*electron_volt, boundary_psi)
E_1 = Secant(3* E_0 , 3.3* E_0  , 0.1*electron_volt, boundary_psi)
E_2 = Secant(5* E_0, 5.5* E_0, 0.1*electron_volt, boundary_psi)

print(f"The ground state energy is {E_0 /electron_volt} eV")
print(f"The first excited state energy is {E_1 /electron_volt} eV")
print(f"The second excited state energy is {E_2 /electron_volt} eV")

"""
The approximate solution obtained in 21 iteration is 2.2113468372787014e-17
The approximate solution obtained in 4 iteration is 6.634040517639403e-17
The approximate solution obtained in 6 iteration is 1.1056734215419297e-16

Energies of the corresponding states are:
The ground state energy is 138.02141351655123 eV
The first excited state energy is 414.0642409118671 eV
The second excited state energy is 690.1070693944035 eV

The results are in accordance with the theoretical values of the corresponding energy levels. This is verified from the fact that the 
difference in energy levels between:

First excited energy level - Ground state energy level = 276.042827395316 eV
Second excited energy level - First excited energy level = 276.042828482536 eV

We can see that this difference is linear and has high degree of precision."""

# Part B

def boundary_psi_anharmonic(E):
    def f1(W):
        return W[2]
    def f2(W):
        return -(E - V_0 *(W[0]/a)**4)* W[1]* 2*electron_mass/hbar**2 
    fsys = [f1,f2]
    soln = system_solver(fsys,a=x_init,b=x_final,m=2,N=N,init=init)
    return soln[N][0]

E_0 = Secant(100*electron_volt, 200*electron_volt, 0.1*electron_volt, boundary_psi_anharmonic)
E_1 = Secant(3* E_0 , 3.3* E_0  , 0.1*electron_volt, boundary_psi_anharmonic)
E_2 = Secant(5* E_0, 5.5* E_0, 0.1*electron_volt, boundary_psi_anharmonic)

print("Anharmonic Oscillator")
print(f"The ground state energy is {E_0 /electron_volt} eV")
print(f"The first excited state energy is {E_1 /electron_volt} eV")
print(f"The second excited state energy is {E_2 /electron_volt} eV")

"""
The approximate solution obtained in 10 iteration is 3.289297935557324e-17
The approximate solution obtained in 8 iteration is 1.1786781930878334e-16
The approximate solution obtained in 10 iteration is 2.312796032263229e-16

Anharmonic Oscillator:
The ground state energy is 205.30182913386093 eV
The first excited state energy is 735.6730638026728 eV
The second excited state energy is 1443.5337422747791 eV"""

# Part C

def boundary_psi_anharmonic(E):
    def f1(W):
        return W[2]
    def f2(W):
        return -(E - V_0 *(W[0]/a)**4)* W[1]* 2*electron_mass/hbar**2 
    fsys = [f1,f2]
    soln = system_solver(fsys,a=x_init,b=x_final,m=2,N=N,init=init)
    return soln[:,0]

y_0 = boundary_psi_anharmonic(E_0)
y_1 = boundary_psi_anharmonic(E_1)
y_2 = boundary_psi_anharmonic(E_2)

def graph(x,y,even=True):
    n = len(x)
    x_integration = x[x<0]
    # Composite Trapezoidal Integration
    h = -(x[0] - x_integration[-1])/(n-1)
    # Computing the sum f(x_1) + ... + f(x_n-1) and x_i = lowlim + i*h
    Sum_f_x_i = 0
    i = 1
    while i<=n-1:
        if x[i] < 0:
            Sum_f_x_i = Sum_f_x_i + y[i]**2
            i = i+1
        else:
            break
    # Computing the integral
    Integral = (h/2)*(y[0] + 2*Sum_f_x_i + y[i-1])
    
    # Normalization
    y *= 1/(np.sqrt(2*Integral))
    
    y_plot = np.zeros(n)
    if even:
        for i in range((n-1)//2):
            y_plot[i] = y[i]
            y_plot[n-2-i] = y[i]
    else:
        for i in range((n-1)//2):
            y_plot[i] = y[i]
            y_plot[n-2-i] = -y[i]
            
    plt.plot(x,y_plot)
    
x_plot = np.linspace(x_init,x_final,N+1)
graph(x_plot, y_0)
graph(x_plot, y_1, even= False)
graph(x_plot, y_2)
plt.xlabel("x")
plt.ylabel("$\psi$(x)")
plt.legend(['ground state', 'first excited state', 'second excited state'])
plt.grid()
plt.savefig("Q11_c.png")
plt.show()