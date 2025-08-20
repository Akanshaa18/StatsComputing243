def firstDerivative(x,f,h=1e-5):
    """find the first derivative of given function"""
    return (f(x + h) - f(x - h)) / (2 * h)

def secondDerivative(x,f,h=1e-5):
    """find the second derivative of given function"""
    return (f(x + h) - 2 * f(x) + f(x - h)) / (h ** 2)

def newtonUnivariate(x0,f,h, stoppingTolerance):
    """find the newton univariate"""
    x = x0
    max_iter = 100
    for i in range(max_iter):
        f_prime = firstDerivative(x,f,h)
        f_doublePrime = secondDerivative(x,f,h)
        if abs(f_doublePrime) < 1e-12:
            print("Second derivative is too small, stopping.")
            break
    
        x_new = x - f_prime / f_doublePrime
        # Stopping criterion for iteration
        if abs(x_new - x) < stoppingTolerance:
            print(f"Converged in {i+1} iterations.")
            return x_new

        x = x_new
        return x
        
def f(x):
    """function to test newton method"""
    return x**2 + 2*x + 1
    
if __name__ == '__main__':
    """main method"""
    x0= 5.0
    res = 0
    h = 1e-5
    stoppingTolerance = 1e-6
    res = newtonUnivariate(x0,f,h,stoppingTolerance)
    print(res)
