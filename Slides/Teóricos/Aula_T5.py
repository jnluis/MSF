#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 18:26:38 2022

@author: joao
"""

import numpy as np
import matplotlib.pyplot as plt


#aceleração gravítica
g =-9.8

dt = 0.0001
t = np.arange(0,1+dt,dt)
y = np.zeros(t.size)

x= np.zeros(t.size)

#velocidade inicial
vx = np.zeros(t.size)
vy = np.zeros(t.size)


vx[0] = 27.36
vy[0] = 4.82 
acx =0
#Preencher o vetor v
for i in range(0,t.size-1):
    vy[i+1] = vy[i] + g*dt # velocidade no instante
    y[i+1] = y[i] + vy[i] *dt
    vx[i+1] = vx[i] + acx *  dt 
    x[i+1] = x[i] + vx[i] * dt
    
plt.plot(x,y, label= "pos")
#chão (y=0 m)
plt.plot([0,28],[0,0], label= "Y=0")


plt.xlabel("t (s) ")
plt.ylabel("Altura (m)")
plt.title("Objeto lançado verticalmente para cima (sem Resistência do ar)")
plt.grid()
plt.legend()

