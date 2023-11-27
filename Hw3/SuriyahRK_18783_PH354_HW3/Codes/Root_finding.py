import numpy as np
import sympy as smp
"""
Main file containing all the root finding methods
"""

def bisect (a, b, eps , f ):
    if ( f (a)* f (b)) > 0 :
        return None
    xl = a  
    xr = b
    while (abs(xl -xr) > eps ):
        xm = (xl + xr) / 2.0
        if f (xl )* f (xm) < 0 :
            xr = xm
        else :
            xl = xm
    return xm


def false_p (a, b, eps , n_max, f ):
    if ( f (a)* f (b)) > 0 :
        return 9999999
    xl = a
    xr = b
    xm = a
    i = 0
    while ( (abs( f (xm)) > eps) and (i < n_max) ):
        xm = (xl* f (xr) - xr* f (xl ))/( f (xr)- f (xl ))
        if f (xl )* f (xm) < 0 :
            xr = xm
        else :
            xl = xm
        i = i + 1
    return xm



def newton (a, eps , f , funcp ):
    maxiter = 100
    xi = a
    i = 0
    while (abs ( f (xi )) > eps and abs( funcp (xi )) > 1e-8 and i < maxiter ):
        i = i + 1
        xip = xi - f (xi )/ funcp (xi)
        xi = xip
    return xi

def secant (a, b, eps , f ):
    maxiter = 100
    xi = a
    xim = b
    i = 0
    while (abs( f (xi )) > eps and abs ( f (xi)- f (xim )) > eps and i < maxiter ):
        i = i + 1
        xip = ( xim* f (xi) - xi* f (xim ))/ ( f (xi)- f ( xim ))
        xim = xi
        xi = xip
    return xi

def newton2 (a, b, eps , func1 , func1p , func2 , func2p ):
    maxiter = 100
    xi = a
    yi = b
    i = 0
    while ( abs (func1 (xi , yi )) > eps and abs(func2 (xi , yi)) > eps and i < maxiter ):
        i = i + 1
        f1 = func1 (xi , yi)
        f2 = func2 (xi , yi)
        f1x , f1y = func1p (xi , yi)
        f2x , f2y = func2p (xi , yi)
        den = f1x * f2y - f1y *f2x
        xip = xi + (f1y *f2 - f2y *f1 )/ den
        yip = yi + (f2x *f1 - f1x *f2 )/ den
        xi = xip
        yi = yip
    return xi , yi  


def false_position(f, a, b, e, N):

    if(f(a)==0):
        return a
    elif (f(b) == 0):
        return b
    
    left = a
    right = b
    x1 = left - f(left) * (right - left) / (f(right) - f(left))

    if (f(x1)*f(a) < 0):
        left = a
        right = b
    else:
        left = b
        right = a
    i = 1


    while(i < N):

        x1 = left - f(left) * (right - left) / (f(right) - f(left))

        if ((f(x1) == 0)) or (abs( (right- x1)/(x1) ) <= e):
            return x1
        else:
            right = x1
        i = i + 1
    
    return x1