import numpy as np

def leap_frog(fsys,a,b,y_init,half_y_init,N):
    """Solves the given ODE using the leap frog method
    
    Arguments:
    fsys -- an array conatining the system of equations
    a -- initial point
    b -- final point
    y_init -- initial value of the function, y(a)
    half_y_init -- value of the function, y(a + h/2)
    N -- number steps to be taken 
    
    Returns:
    x -- the array containing the equally spaced points at which the ode is solved
    y -- the array containing the solutions at points in the array x"""
    
    x = np.linspace(a,b,N+1)
    n = len(y_init)
    
    h = (b-a)/N
    
    y = np.zeros((N+1,n))
    half_y = np.zeros((N+1,n))
    
    # Initializing the solution array
    y[0] = y_init
    half_y[0] = half_y_init
    
    for i in range(1,N+1):
        val_1 = np.zeros(n)
        val_2 = np.zeros(n)
        for j in range(n):
            val_1[j] = h*fsys[j](x[i - 1] + h/2, half_y[i - 1])
        y[i] = y[i-1] + val_1        
        for j in range(n):
            val_2[j] = h*fsys[j](x[i], y[i])
        half_y[i] = half_y[i-1] + val_2
        
    return x,y