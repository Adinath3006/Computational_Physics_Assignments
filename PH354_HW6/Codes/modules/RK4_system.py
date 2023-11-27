def system_solver(fsys, a, b, m, N, init, disp = False):
    """ Calculates the approximate solution of mth prder system of differential equations for N+1 evenly separated points using fourth 
    order Runge-Kutta method
    
    Arguments:
    fsys -- an array which stores the symolic expressions of the system of differential equations, [f1(...), f2(...), ...]
    a -- input specifying the lower bound on t 
    b -- input specifying the upper bound on t
    m -- input specifying the order of the system
    N -- input specifying the N+1 evenly spaced points
    init -- an array which stores the initial values of the variables
    disp -- boolean function specifying if the title should be displayed
    
    Returns:
    soln -- a numpy array containing the solutions of the system at each interval"""

    import numpy as np
    import sympy as sym

    # Initializing the parameters
    h = (b-a)/N
    t = a
    W = sym.symbols(f'W(0:{m+1})') # W[0] -> t, W[i] -> x_i
    # Creating a array which stores the values w_i
    array_w = np.zeros(m+1)
    k = np.zeros([4,m+1])
    k[0][0] = h
    k[1][0] = h
    k[2][0] = h
    k[3][0] = h
    soln = np.zeros([N+1,m])
    array_w[0] = t

    for j in range(1,m+1):
        array_w[j] = init[j-1]
        soln[0][j-1] = array_w[j]

    for i in range(1,N+1):
        # Compute k1_j
        for j in range(1,m+1):
            k[0][j] = h*fsys[j-1].subs({W[i]:array_w[i] for i in range(0,m+1)}) 
        # Compute k2_j
        for j in range(1,m+1):
            k[1][j] = h*fsys[j-1].subs({W[i]:array_w[i] + (1/2)*k[0][i] for i in range(0,m+1)})
        # Compute k3_j
        for j in range(1,m+1):
            k[2][j] = h*fsys[j-1].subs({W[i]:array_w[i] + (1/2)*k[1][i] for i in range(0,m+1)})
        # Compute k4_j
        for j in range(1,m+1):
            k[3][j] = h*fsys[j-1].subs({W[i]:array_w[i] + k[2][i] for i in range(0,m+1)})
        # Compute w_j
        for j in range(1,m+1):
            array_w[j] = array_w[j] + ( k[0][j] + 2*k[1][j]+ 2*k[2][j]+ k[3][j] )/6
            soln[i][j-1] = array_w[j]
        t = a + i*h
        array_w[0] = t
    # Output to be displayed
    if disp:
        print("")
        print("-------------------------------------------------")
        print("                 Runge-Kutta Method              ")
        print("-------------------------------------------------")
        print("")
        print(soln)
        return soln
    else:
        return soln