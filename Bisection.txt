%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

def f(x): 
    x**3 + 1
    
    def bisection(a,b,tol):
        while(np.abs(a - b) >= tol):
            c = (a + b) / 2.0
            prod = a * c
            if prod < tol: 
              return c

        answer = bisection(-5,5,1e-10)

        print(answer)