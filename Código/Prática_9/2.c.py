#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 18:26:38 2022

@author: joao
"""

import numpy as np
import matplotlib.pyplot as plt
#aceleração gravítica
g =9.8

u = 0.004
m= 75
Cres = 0.9
Af = 0.3
densidade_ar= 1.225


#Tmpo inicial e final
ti =0
tf=200
dt = 0.001
n = int((tf-ti) / dt)


#Arrays precisam ser todos definidos
t = np.linspace(ti, tf, n)

v = np.empty(n)
vx = np.empty(n)
ax = np.empty(n)
x = np.empty(n)

vx[0] = 1
v[0] = 1
ax[0] = 0
x[0] = 0

P = 0.4 * 745.698872
print(P)

for i in range(n-1):   
    
    v[i] = np.sqrt(vx[i]**2)
    ax[i+1] = -u*g - (Cres*Af*densidade_ar*v[i]*vx[i])/(2*m) + P/(m*v[i])
    vx[i+1] = vx[i] +ax[i]*dt
    x[i+1] = x[i] + vx[i] * dt

#Calcular velocidade terminal
vt = 11.68 * 0.9 #90%

for i in range(n-1):
    if (x[i]>2000-dt and x[i]>2000+ dt): #é 2000m
        print("Percorre 2 km no instante = {:0.2f} s".format( t[i]))
        plt.plot(t[i],x[i], "o", label="posição 2 km")
        break

#Plot
plt.plot(t,x, color= "yellow")
plt.xlabel("t (s) ")
plt.ylabel("v (m/)")
plt.title("Tempo para percorrer 2 km ")
plt.grid()
plt.legend()
plt.show()
