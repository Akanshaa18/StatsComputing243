import math

def firstDerivative(x,f,h=1e-5):
    return (f(x + h) - f(x - h)) / (2 * h)

def secondDerivative(x,f,h=1e-5):
    return (f(x + h) - 2 * f(x) + f(x - h)) / (h ** 2)

def newtonUnivariate(x0,f,h, stoppingTolerance):
    x = x0
    max_iter = 100
    for i in range(max_iter):
        f_prime = firstDerivative(x,f,h)
        f_doublePrime = secondDerivative(x,f,h)
        if abs(f_doublePrime) < 1e-12:
            print("Second derivative is too small, stopping.")
            break
    
        x_new = x - f_prime / f_doublePrime
        # Stopping criterion
        if abs(x_new - x) < stoppingTolerance:
            print(f"Converged in {i+1} iterations.")
            return x_new

        x = x_new
        return x

if __name__ == '__main__':
    x0= 5.0
    f = lambda x: x**2 + 2*x + 1
    res = 0
    h = 1e-5
    stoppingTolerance = 1e-6
    res = newtonUnivariate(x0,f,h,stoppingTolerance)
    print(res)