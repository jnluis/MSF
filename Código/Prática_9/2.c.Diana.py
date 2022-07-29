#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 18:26:38 2022

@author: joao
"""

import numpy as np
import matplotlib.pyplot as plt
#Calcular Potência

u = 0.004
m = 75
Area = 0.3
par = 1.225
g=9.8
Cres = 0.9

P = 0.4 * 745.715

t0 = 0
tf =200
dt = 0.001

n = int((tf-t0)/dt)
t = np.linspace(t0,tf,n)

vx = np.empty(n)
v = np.empty(n)
ax = np.empty(n)
x = np.empty(n)

vx[0] = 1
ax[0] = 0
x[0] = 0


for i in range(n-1):   
    
    v[i] = np.sqrt(vx[i]**2)
    ax[i+1] = -u*g - (Cres*Area*par*v[i]*vx[i])/(2*m) + P/(m*v[i])
    vx[i+1] = vx[i] +ax[i]*dt
    x[i+1] = x[i] + vx[i] * dt
    
v[n-1] = np.sqrt(vx[n-1]**2)


#Calcular velocidade terminal
vt = 11.68 * 0.9 #90%

for i in range(n-1):
    if (x[i]>2000-dt and x[i]>2000+ dt): #é 2000m
        print("Percorre 2 km no instante = {:0.2f} s".format( t[i]))
        plt.plot(t[i],x[i], "o", label="posição 2")
        break

    
plt.plot(t,x)
plt.xlabel("t (s)")
plt.ylabel("v (m/s)")
plt.title("Velocidade Terminal")
plt.grid()
plt.legend()
plt.show()
