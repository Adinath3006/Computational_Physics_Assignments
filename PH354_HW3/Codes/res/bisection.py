def bisect (a , b , eps , func ):
    if ( func ( a )* func ( b )) > 0 :
        return 9999999
    xl = a
    xr = b
    while ( abs( xl - xr ) > eps ):
        xm = ( xl + xr ) / 2.0
        if func ( xl )* func ( xm ) < 0 :
            xr = xm
        else :
            xl = xm
    return xm