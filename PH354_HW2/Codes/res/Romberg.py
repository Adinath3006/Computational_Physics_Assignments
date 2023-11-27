import numpy as np

def romberg (a, b, eps , nmax , func ):
    h = np. zeros ( nmax )

    for i in range (0, nmax ):
        h[i] = (b - a )/(2**i)

    r = np. zeros (( nmax , nmax ))
    r[0 ,0] = (b - a)*( func (a) + func (b ))/2.
    
    error = np.zeros(nmax)

    for j in range (1, nmax ):
        subtotal = 0

        for i in range (0 ,2**(j -1)):
            subtotal = subtotal + func (a +(2*i +1)* h[j])

        r[j ,0] = r[j -1 ,0]/2. + h[j]* subtotal

        for k in range (1,j +1):
            r[j,k] = (4**(k)*r[j,k -1] -r[j -1,k -1])/(4**(k) -1)
        
        error[j] = abs((r[j,j-1]- r[j-1,j-1])/(2**(2*j)-1))

        if error[j]<= eps:
            break
    return r,j,error