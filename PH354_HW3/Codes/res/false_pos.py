def false_p (a, b, eps , func ):
    if ( func (a)* func (b)) > 0 :
        return 9999999
    xl = a
    xr = b
    xm = a
    while (abs( func (xm )) > eps ):
        xm = (xl* func (xr) - xr* func (xl ))/( func (xr)- func (xl ))
        if func (xl )* func (xm) < 0 :
            xr = xm
        else :
            xl = xm
    return xm