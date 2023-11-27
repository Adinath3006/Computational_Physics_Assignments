import math

# Defining the function which uses Regula Falsi method to compute the root
def Regula(x0,x1,rTOL,N,f):
    # Check if the initial conditions satisfy the condition
    if f(x0)*f(x1)>0:
        print("The initial conditions do not contain the root between!")
    else:
        i = 1 # iterating variable
        while i <= N:
            m = (f(x1)-f(x0))/(x1-x0) # The slope of the line joining f(x1) and f(x0)
            x = x0-(f(x0)/m) # The x intercept of the line joining f(x1) and f(x0)
            if f(x)*f(x0)<0: # If the initial intercept and x0 contains the root the code proceeds this way
                if f(x)==0 or math.isclose(x,x1,rel_tol = rTOL): # x can either be the proper root or satisfy the relative error condition
                    print("The root of the equation with relative tolerance of",rTOL,"is",x)
                    print("The number of iterations taken to achieve this value is",i)
                    return x
                else: # If the "if" condition is not satisfied then it should proceed to try the x-intercept formed by f(x0) and f(x)
                    x1 = x # Change the value of x1 to x
                i = i+1 # Incrementing the iterating variable
                if i > N: # When the maximum number of iterations is reached and we still don't get the solution, we display a message
                    print("")
                    print("Maximum number of iterations reached!")
                    print("No value satisfying the condition is found!")
                    break
                else:
                    continue
            else: # If the initial intercept and x1 contains the root the code proceeds this way
                if f(x)==0 or math.isclose(x,x0,rel_tol = rTOL): # x can either be the proper root or satisfy the relative error condition
                    print("The root of the equation with relative tolerance of",rTOL,"is",x)
                    print("The number of iterations taken to achieve this value is",i)
                    return x
                else: # If the "if" condition is not satisfied then it should proceed to try the x-intercept formed by f(x) and f(x1)
                    x0 = x
                i = i+1
                if i > N: # When the maximum number of iterations is reached and we still don't get the solution, we display a message
                    print("")
                    print("Maximum number of iterations reached!")
                    print("No value satisfying the condition is found!")
                    break
                else:
                    continue
