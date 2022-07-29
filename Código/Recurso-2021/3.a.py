#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 18:26:38 2022

@author: joao
"""

import numpy as np
import matplotlib.pyplot as plt

m = 1200
Cres = 0.9
A = 3
p = 1.225
u = 0.004
g = 9.8 # em m/s²
vi = 1
t0 = 0
tf = 100
dt = 0.001

n = int((tf-t0)/dt)

#Arrays precisam ser todos definidos
t = np.linspace(t0, tf, n)

v = np.empty(n)
vx = np.empty(n)
ax = np.empty(n)
ay = np.empty(n)
x = np.empty(n)

vx[0] = 1
v[0] = 1
ax[0] = 0
tolerancia = 0.00001

P = 60 *735.4975
print(P ,"Watts")

for i in range(n-1):
    v[i] = np.sqrt(vx[i] **2)
    ax[i] = -u*g - (Cres*A*p*v[i]*vx[i])/(2*m) + P/(m*v[i])
    ay[i] =-g
    vx[i+1] = vx[i] +ax[i]*dt  
    x[i+1] = x[i] + v[i]*dt
    
    if vx[i+1]-vx[i] < tolerancia:
        print("vT = {:0.2f}".format(vx[i]))
        plt.plot(t[i],vx[i], "o",label="vT")
        break
    
v[n-1] = np.sqrt(vx[n-1]**2)

plt.plot(t[1:i],vx[1:i])
plt.xlabel("t (s) ")
plt.ylabel("v (m/s)")
plt.title("Evolução temporal da velocidade ")
plt.legend()
plt.grid()
plt.show()
