
def rk4_1_step(fsys,x,y,h):
    
    import numpy as np
    
    m = len(y)
    k = np.zeros([4,m+1])
    soln = np.zeros(m)
    array_w = np.zeros(m+1)
    
    k[0][0] = h
    k[1][0] = h
    k[2][0] = h
    k[3][0] = h
    
    array_w[0] = x 
    for j in range(1,m+1):
        array_w[j] = y[j-1]   
    
    # Compute k1_j
    for j in range(1,m+1):
        k[0][j] = h*fsys[j-1](array_w) 
    # Compute k2_j
    for j in range(1,m+1):
        k[1][j] = h*fsys[j-1](array_w + (1/2)*k[0])
    # Compute k3_j
    for j in range(1,m+1):
        k[2][j] = h*fsys[j-1](array_w + (1/2)*k[1])
    # Compute k4_j
    for j in range(1,m+1):
        k[3][j] = h*fsys[j-1](array_w + k[2])
    # Compute w_j
    for j in range(1,m+1):
        array_w[j] = array_w[j] + ( k[0][j] + 2*k[1][j]+ 2*k[2][j]+ k[3][j] )/6
        soln[j-1] = array_w[j]

    return soln

def adaptive_rk4(fsys, a, b, init, h_init, eps):
    
    import numpy as np
    
    x = [a]
    y = [init]
    h = [h_init]
    
    while x[-1] <= b:
        h_curr = h[-1]
        x_curr = x[-1]
        y_curr = y[-1]
        
        y_h_1 = rk4_1_step(fsys=fsys, x=x_curr, y=y_curr, h=h_curr)
        y_h_2 = rk4_1_step(fsys=fsys, x=x_curr + h_curr, y=y_h_1, h=h_curr)
        y_2h = rk4_1_step(fsys=fsys, x=x_curr, y=y_curr, h=2*h_curr)
        
        err = np.linalg.norm(y_2h - y_h_2)
        rho = 30*h_curr*eps/err
        
        if rho >= 16 :
            x.append(x_curr + h_curr)
            x.append(x_curr + 2*h_curr)
            y.append(y_h_1)
            y.append(y_h_2)
            h.append(2*h_curr)

        elif rho >= 1:
            x.append(x_curr + h_curr)
            x.append(x_curr + 2*h_curr)
            y.append(y_h_1)
            y.append(y_h_2)
            h.append(h_curr*rho**(1/4))

        else:
           h[-1] = h[-1]*rho**(1/4)
           
    return x,np.array(y),np.array(h)