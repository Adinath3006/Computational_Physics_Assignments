def fixed (a , eps , func ):
    maxiter = 100
    xi = a
    i = 0
    while ( abs ( func ( xi ) - xi ) > eps and i < maxiter ):
        i = i + 1
        xin = func ( xi )
        xi = xin
    return xi

def accelerated_fixed(a,eps,func,funcp):
    maxiter = 100
    r0 = -1/funcp(a)
    xi = a
    i = 0
    while ( abs( r0 * func(xi)) > eps and i < maxiter ):
        xi = xi + r0*func(xi)
        print(f"Root obtained at {i}th iteration is {xi} with error {abs( r0 * func(xi))}") 
        i += 1
    return xi
