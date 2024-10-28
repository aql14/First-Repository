# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 14:12:47 2024

@author: alvar
"""

# Function f is known

import numpy as np
import matplotlib.pyplot as plt

# Define parameters
f = lambda t, y: np.exp(-t)

a = 0
b = 10

h = 0.5 # Step size
t = np.arange(a, b + h, h) # Numerical grid
y0 = -1 # Initial Condition

# Explicit Euler Method
y = np.zeros(len(t))
y[0] = y0

for i in range(0, len(t) - 1):
    y[i + 1] = y[i] + h*f(t[i], y[i])

plt.figure(figsize = (12, 8))
plt.plot(t, y, 'bo--', label='Approximate')
plt.plot(t, -f(t,y), 'g', label='Exact')
plt.title('Approximate and Exact Solution \
for Simple ODE')
plt.xlabel('t')
plt.ylabel('f(t)')
plt.grid()
plt.legend(loc='lower right')
plt.show()