# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 13:45:41 2024

@author: alvar
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 14:57:56 2024

@author: alvar
"""

# Function f is known

import numpy as np
import matplotlib.pyplot as plt
from ODE_Solver_Onestep import Implicit_Euler, Explicit_Euler
from Newton_Raphson_Analitica import newton_raphson

# Define parameters
def f(t,y): 
    return np.exp(-t)

def df(t,y):
    return -np.exp(-t)

a = 0
b = 10

h = 0.1 # Step size
t = np.arange(a, b + h, h) # Numerical grid
y0 = -1 # Initial Condition

# Explicit Euler Method
y = np.zeros(len(t))
y[0] = y0
y1 = Explicit_Euler(t, y, h, f)

#☼ Implicit Euler Method
y = np.zeros(len(t))
y[0] = y0
y2 = Implicit_Euler(t, y, h, f, df)

plt.figure(figsize = (10, 6))
plt.plot(t, y1, 'k--', label='Explicit Euler')
plt.plot(t, y2, 'y--', label='Implicit Euler')
plt.plot(t, -f(t,y), 'ro--', label='Exact Solution')
plt.title('Solution')
plt.xlabel('t')
plt.ylabel('f(t)')
plt.grid()
plt.legend(loc='lower right')
plt.show()

# Errores Explicito e Implicito
errorExp = np.abs(-f(t,y)-y1)
errorImp = np.abs(-f(t,y)-y2)
plt.figure(figsize = (10, 6))
plt.plot(t, errorExp, 'r', label='Error E_Explicito')
plt.plot(t, errorImp, 'k', label='Error E_Implicito')
plt.title('Error')
plt.xlabel('t')
plt.ylabel('e(t)')
plt.grid()
plt.legend(loc='lower right')
plt.show()