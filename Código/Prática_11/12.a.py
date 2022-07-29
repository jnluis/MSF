# -*- coding: utf-8 -*-1
"""
Created on Mon May  9 17:30:26 2022

@author: joão
v =-A*w*sin(wt+d)
A =-A*w**2*cos(wt+d)
"""

import matplotlib.pyplot as plt
import numpy as np
#Calcule numericamente a lei do movimento, no caso em que a velocidade inicial é nula e a posição inicial 4 m.
dt = 0.01

k = 1
m = 1
xEq = 1.5

#t = np.arange(0, 200+dt, dt) Outra maneira de fazer o t
#Tmpo inicial e final
ti =0
tf=200
dt = 0.01
n = int((tf-ti) / dt)
t = np.linspace(ti, tf, n)

x = np.zeros(t.size)
v = np.zeros(t.size)
a= np.empty(n)
Ep = np.empty(n)
Ec = np.empty(n)
Em = np.empty(n)

x[0] = 4
v[0] =0
a[0] = -k/m*x[0]
    
for i in range(n-1):
    a[i+1] = -2*k/m*(x[i]**2-xEq**2)*x[i]
    v[i+1] = v[i] + a[i+1]*dt
    x[i+1] = x[i]+v[i+1]*dt  # Pelo método de Euler, não funcionava
    Ep[i] = 0.5 * k *(x[i]**2-xEq**2)**2                    
    Ec[i] = 0.5 *m * v[i] **2
    Em[i] = 0.5 * k* (x[i]**2 - xEq**2)**2

plt.plot(x, Em)    
plt.xlabel("x (m)")
plt.ylabel("Em (J)")
plt.title("Energia Potencial")
plt.grid()