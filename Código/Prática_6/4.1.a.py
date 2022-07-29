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
tf=1
dt = 0.01
n = int((tf-ti) / dt)

#Para as analiticas
x0 = 0
y0 = 0
#velocidade inicial
v0 =100 / 3.6 # para coonverter para m/s

#Arrays precisam ser todos definidos
t = np.linspace(ti, tf, n)

vx = np.empty(n)
ax = np.empty(n)
x = np.empty(n)

vy= np.empty(n)
ay = np.empty(n)
y = np.empty(n)

vx[0] = v0*np.cos(alpha)
vy[0] = v0*np.sin(alpha)


floor = np.zeros(t.size)

#Preencher o vetor v
for i in range(n-1):
    ay[i] = -g
    ax[i] = 0
    vx[i+1] = vx[i] +ax[i]*dt
    vy[i+1] = vy[i] + ay[i]*dt
    x[i+1] = x[i] + vx[i]*dt
    y[i+1] = y[i] + vy[i]*dt
    x_anali = vx[0]*t + x0
    y_anali = vy[0]*t - (0.5*g*t**2) +y0
        
plt.plot(x,y, label= "bola")
plt.plot(x_anali, y_anali, label ="Resultado analítico")
plt.xlabel("x (m) ")
plt.ylabel("y (m)")
plt.title("Bola de futebol com ângulo de 10º")
plt.grid()
plt.legend()

