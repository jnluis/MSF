#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 10:11:25 2022

@author: joao
"""

import numpy as np
import matplotlib.pyplot as plt


dt = 0.0001

t = np.arange(0,40+dt, dt)

Axeq = 1.0
Bxeq = 1.2

Ax = np.zeros(t.size)
Bx = np.zeros(t.size)

Av = np.zeros(t.size)
Bv = np.zeros(t.size)

Ax[0] = Axeq + 0.05
Bx[0] = Bxeq

phi1 = 0
phi2 = 0
A1 = 0.025
A2 = 0.025

m = 1

k = 1
kder = 0.5

w1 = np.sqrt(k/m)
w2 = np.sqrt((k+2*kder)/m)

Ax1 = np.zeros(t.size-1)
Bx1 = np.zeros(t.size-1)

for i in range(t.size-1):
    Aacc = (-k*(Ax[i]-Axeq)-kder*((Ax[i]-Axeq)-(Bx[i]-Bxeq)))/m
    Bacc = (-k*(Bx[i]-Bxeq)+kder*((Ax[i]-Axeq)-(Bx[i]-Bxeq)))/m
    
    Av[i+1] = Av[i] + Aacc*dt
    Bv[i+1] = Bv[i] + Bacc*dt
    
    Ax[i+1] = Ax[i] + Av[i+1]*dt
    Bx[i+1] = Bx[i] + Bv[i+1]*dt
    
    Ax1[i] = Axeq + A1*np.cos(w1*t[i]+phi1) + A2*np.cos(w2*t[i]+phi2)
    Bx1[i] = Bxeq + A1*np.cos(w1*t[i]+phi1) - A2*np.cos(w2*t[i]+phi2)


plt.plot(t,Ax, label="Ax")
plt.plot(t,Bx, label="Bx")

plt.plot(t[:-1],Ax1, label="Sobreposiçao Ax")
plt.plot(t[:-1],Bx1, label="Sobreposiçao Bx")
plt.legend()