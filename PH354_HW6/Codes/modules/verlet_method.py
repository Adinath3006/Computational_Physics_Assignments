import numpy as np

def verlet(fsys,a,b,y_init,half_v_init,N):
    """Solves the given ODE using the verlet method
    
    Arguments:
    fsys -- a function conatining the RHS of the ODE
    a -- initial point
    b -- final point
    y_init -- initial value of the function, y(a)
    half_v_init -- value of the function, v(a + h/2)
    N -- number steps to be taken 
    
    Returns:
    x -- the array containing the equally spaced points at which the ode is solved
    y -- the array containing the solutions at points in the array x"""
    
    x = np.linspace(a,b,N+1)
    n = len(y_init)
    
    h = (b-a)/N
    
    y = np.zeros((N+1,n))
    v = np.zeros((N+1,n))
    half_v = np.zeros((N+1,n))
    
    # Initializing the solution array
    y[0] = y_init
    v[0] = half_v_init
    half_v[0] = half_v_init
    
    for i in range(1,N+1):
        y[i] = y[i-1] + h*half_v[i-1]
        k = h*fsys(x[i],y[i])
        v[i] = half_v[i-1] + k/2
        half_v[i] = half_v[i-1] + k
        
    return x,y,v,half_v