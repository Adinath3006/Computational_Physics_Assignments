def Runge_Kutta(f, a, b, y_0, h, disp = False):
    """Solves the differential equation using the fourth order Runge-Kutta method
    
    Arguments:
    f -- a function f such that y' = f(t,y)
    a -- input specifying the lower bound on t 
    b -- input specifying the upper bound on t
    y_0 -- input specifying the initial value of the problem y(a) = y_0
    h -- step size
    disp -- boolean function specifying if the title should be displayed
    
    Returns:
    array_w -- numpy array which has the values of y at equal step intervals of size h"""
    
    import numpy as np

    N = int((b-a)/h)
    # Creating a array which stores the values w_i
    array_w = np.zeros(N+1)
    t = a
    
    i = 0
    while i <= N:
        if i == 0:
            array_w[0] = y_0
        else:
            k_1 = h*f(t,array_w[i-1])
            k_2 = h*f(t+h/2,array_w[i-1]+k_1/2)
            k_3 = h*f(t+h/2,array_w[i-1]+k_2/2)
            k_4 = h*f(t+h,array_w[i-1]+k_3)
            array_w[i] = array_w[i-1] + (1/6)*(k_1 + 2*k_2 + 2*k_3 + k_4)
            t = a + i*h
        i = i+1
    # Output to be displayed
    if disp:
        print("")
        print("-------------------------------------------------")
        print("          Runge-Kutta Order 4  (h =",h,")        ")
        print("-------------------------------------------------")
        print("")
        print(array_w)
        return array_w
    else:
        return array_w
    