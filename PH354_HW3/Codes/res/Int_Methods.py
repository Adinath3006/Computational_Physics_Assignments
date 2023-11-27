def Composite_Integration(f,method,lowlim,upplim,n):
    
    # Method = 0 ==> Composite Trapezoidal rule
    # Method = 1 ==> Composite Simpson's rule
    
    if method == 0:
        h = (upplim - lowlim)/n
        
        # Computing the sum f(x_1) + ... + f(x_n-1) and x_i = lowlim + i*h
        Sum_f_x_i = 0
        i = 1
        while i<=n-1:
            x_i = lowlim + i*h
            Sum_f_x_i = Sum_f_x_i + f(x_i)
            i = i+1
            
        # Computing the integral
        Integral = (h/2)*(f(lowlim) + 2*Sum_f_x_i + f(upplim))
        
        return Integral
    
    elif method == 1:
        
        # n must be even for this method 
        if n%2 == 0:
            h = (upplim - lowlim)/n
        
            # Computing the sum f(x_2) + ... + f(x_n-2) and x_i = lowlim + i*h
            Sum_f_x_i = 0
            i = 1
            while i<= n/2 -1:
                x_i = lowlim + 2*i*h
                Sum_f_x_i = Sum_f_x_i + f(x_i)
                i = i+1
            
            # Computing the sum f(x_1) + ... + f(x_n-1) and x_i = lowlim + i*h
            Sum_f_x_j = 0
            j = 1
            while j<= n/2:
                x_j = lowlim + (2*j-1)*h
                Sum_f_x_j = Sum_f_x_j + f(x_j)
                j = j+1
                
            # Computing the integral
            Integral = (h/3)*(f(lowlim) + 2*Sum_f_x_i + 4*Sum_f_x_j + f(upplim))
            
            return Integral
        
        else:
            print("Invalid input! n must be an even integer")