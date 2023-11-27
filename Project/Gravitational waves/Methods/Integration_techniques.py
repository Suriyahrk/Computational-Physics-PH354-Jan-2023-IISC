import numpy as np
import sympy as smp



# Function to evaluate the Integral using composite trapizoidal rule, a - starting point, b - ending point,
# f - function values (array), n - number of intervals (Used in Question-1)

def CT(a,b,f,n):
    h = (b-a)/n
    I = 0

    for i in np.arange(0,n):
        I = I + (f[i] + f[i+1])*h/2
    
    return I


# Composite integration function used in Question - 2, Question - 3

def CI(a,b,f,x,n,method): # method = 1 : Trapizoid, Method = 2 : Simpson ; Note :  x should be given as a symbol
    h = (b-a)/n
    I = 0

    if method not in (1,2):
        print('Input a valid method')

    if method == 1 :
        for i in np.arange(0,n):
            I = I + (f.subs(x,a + h*i)+ f.subs(x,a + h*(i+1)))*h/2
        return I
    
    else:
        if n%2 == 1:
            print("Odd number of slices not possible for Simpsons method")
        else:
            J = f.subs(x,a) + f.subs(x,b)
            for j in np.arange(1,n):
                if j%2 == 0:
                    J = J + 2*f.subs(x,a + j*h)
                else:
                    J = J + 4*f.subs(x,a+j*h)
            return J*(h/3)

# Gaussian Quadrature Integration technique (Used in Question-9,Question-10  )

def gaussxw(N):
    
    a = np.linspace(3,4*N-1,N)/(4*N +2)   # Initial approximation to roots of the Legendre polynomial
    
    x = np.cos (np.pi*a +1/(8* N*N*np.tan(a)))

    # Find roots using Newton ’s method

    epsilon = 10**-15
    delta = 1.0

    while delta > epsilon :
        p0 = np.ones(N, float )
        p1 = np.copy(x)

        for k in range (1,N):
            p0 ,p1 = p1 ,((2* k +1)* x*p1 -k*p0 )/( k +1)

        dp = (N +1)*( p0 -x*p1 )/(1 -x*x)
        dx = p1/dp
        x  -= dx
        delta = max( abs(dx ))

    w = 2*( N +1)*( N +1)/( N*N*(1 -x*x)* dp*dp)
    return x,w


def gaussxwab (N,a,b):
    x,w = gaussxw (N)
    return 0.5*(b-a)*x +0.5*( b+a ), 0.5*(b-a)*w    



def GQ(a,b,f,N):   # The final gaussian function
    x,w = gaussxwab(N,a,b)
    S = 0
    for i in np.arange(0,N):
        S = S + w[i]*f(x[i])
    return S



def Trapizoidal_rule(a,b,f):
    return (f(a)+f(b))/2
   
def recursive_tsr(a,b,f,e,whole_integral): # Whole :=  value of the integral using trapizoidal method on the whole_integral interval
    c = (a+b)/2
    left_integral = Trapizoidal_rule(a,c,f)
    right_integral = Trapizoidal_rule(c,b,f)
    N = 1
    if abs( left_integral + right_integral - whole_integral ) <= 15*e:
        return left_integral + right_integral + ( left_integral + right_integral - whole_integral )/15 # the following value will within epsilon of correct value
    else:
        print(f"The value of the integral for {2**N} slices is ")
        N = N+1
        return recursive_tsr(f,a,c,e/2,left_integral ) + recursive_tsr (f,c,b,e/2,right_integral)

def adaptive_trapizoidal_rule (a,b,f,e):
    return recursive_tsr(f,a,b,e, Trapizoidal_rule(a,b,f))


def romberg (a, b, eps , nmax , func ):
    h = np. zeros ( nmax )

    for i in range (0, nmax ):
        h[i] = (b - a )/(2.** i)

    r = np. zeros (( nmax , nmax ))
    r[0 ,0] = (b - a)*( func (a) + func (b ))/2.
    
    e = np.zeros(nmax)

    for j in range (1, nmax ):
        subtotal = 0

        for i in range (0 ,2**(j -1)):
            subtotal = subtotal + func (a +(2* i +1)* h[j])

        r[j ,0] = r[j -1 ,0]/2. + h[j]* subtotal

        for k in range (1,j +1):
            r[j,k] = (4**( k)*r[j,k -1] -r[j -1,k -1])/(4**( k) -1)
        
        e[j] = abs((r[j,j-1]- r[j-1,j-1])/(2**(2*j)-1))

        if e[j]<= eps:
            break
    return r , j , e   
