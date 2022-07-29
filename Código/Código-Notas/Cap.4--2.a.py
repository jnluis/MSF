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
alpha = np.radians(10) #degrees

#Tmpo inicial e final
ti =0
tf=5
dt = 0.0001
n = int((tf-ti) / dt)

#Para as analiticas
x0 = 0
y0 = 3
#velocidade inicial
v0 =200 / 3.6 # para coonverter para m/s
VT = 6.8 # em m/s
#Arrays precisam ser todos definidos
t = np.linspace(ti, tf, n)

vx = np.empty(n)
ax = np.empty(n)
x = np.empty(n)

vy= np.empty(n)
ay = np.empty(n)
y = np.empty(n)
y[0] =y0
vx[0] = v0*np.cos(alpha)
vy[0] = v0*np.sin(alpha)
v= np.empty(n)

D =g/(VT**2)

#Preencher o vetor v
for i in range(n-1):
    ay[i] =-g-D*np.sqrt(vx[i]**2+vy[i]**2)*vy[i]
    ax[i] = -D*np.sqrt(vx[i]**2+vy[i]**2)*vx[i]
    vx[i+1] = vx[i] +ax[i]*dt
    vy[i+1] = vy[i] + ay[i]*dt

    x[i+1] = x[i] + vx[i]*dt
    y[i+1] = y[i] + vy[i]*dt


     
#Quanto tempo demorou a trajetória? 
for i in range(n-1):
    if (y[i+1]*y[i]<0):
        print("Demorou {:0.2f}s".format(t[i]))
        print("Alcance {:0.2f}m".format(x[i]))
        plt.plot(x[i],y[i], "o", label="y(t) = 0")
        break

plt.plot(x,y)
plt.xlabel("x (m) ")
plt.ylabel("y (m)")
plt.title("Trajetória volante a v0= 200km/h")
plt.grid()


