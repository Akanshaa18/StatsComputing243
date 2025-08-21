#practice forking and PRs EO
import numpy as np

def newtonMultivariate(x0,f,h,epsilon,stoppingTolerance):
    return 0

def f(x):
    """function to test newton method"""
    return x**2 + 2*x + 1

if __name__ == "__main__":
    """main method"""
    x0= 5.0
    res = 0
    epsilon = 1e-5
    stoppingTolerance = 1e-6
    res = newtonMultivariate(x0,f,h,epsilon,stoppingTolerance)
    print(res)
    