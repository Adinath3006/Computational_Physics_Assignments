from math import fabs , cos , sin

def fpx ( x,f ):
    h = 1e-6
    return (f(x+h)-f(x-h))/(2*h)

def newton (a , eps , func ):
    maxiter = 100
    xi = a
    i = 0
    while ( abs ( func ( xi )) > eps and abs ( fpx ( xi,func )) > 1e-8 and i < maxiter ):
        i = i + 1
        xip = xi - func ( xi )/ fpx ( xi,func )
        xi = xip
    return xi

def newton2 (a , b , eps , func1 , func1p , func2 , func2p ):
	maxiter = 100
	xi = a
	yi = b
	i = 0
	while ( abs ( func1 (xi , yi )) > eps and abs( func2 ( xi , yi ) ) > eps and i < maxiter ):
		i = i + 1
		f1 = func1 (xi , yi )
		f2 = func2 (xi , yi )
		f1x , f1y = func1p (xi , yi )
		f2x , f2y = func2p (xi , yi )
		den = f1x * f2y - f1y * f2x
		xip = xi + ( f1y * f2 - f2y * f1 )/ den
		yip = yi + ( f2x * f1 - f1x * f2 )/ den
		xi = xip
		yi = yip
	return xi , yi

