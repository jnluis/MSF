# -*- coding: utf-8 -*-1
"""
Created on Mon May  9 17:30:26 2022

@author: joão
v =-A*w*sin(wt+d)
A =-A*w**2*cos(wt+d)
"""

import matplotlib.pyplot as plt
import numpy as np
#   Faça o diagrama de energia desta energia potencial.

k= 4
xEq = 1.5
ti =0
tf=10
dt = 0.01
n = int((tf-ti) / dt)  



x = np.linspace(-2, 2,n)  
Ep = 0.5 * k*(x**2 - xEq**2)**2
plt.plot(x, Ep)

plt.axhline(y =2,color="green") #Para a Ep que quisermos intersetar  

plt.xlabel("x (m)")
plt.ylabel("Ep (J)")
plt.title("Energia Potencial")
plt.grid()
plt.show()
