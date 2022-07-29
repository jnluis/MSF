#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 10:02:30 2022

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

for i in range(t.size-1):
    Aacc = (-k*(Ax[i]-Axeq)-kder*((Ax[i]-Axeq)-(Bx[i]-Bxeq)))/m
    Bacc = (-k*(Bx[i]-Bxeq)+kder*((Ax[i]-Axeq)-(Bx[i]-Bxeq)))/m
    
    Av[i+1] = Av[i] + Aacc*dt
    Bv[i+1] = Bv[i] + Bacc*dt
    
    Ax[i+1] = Ax[i] + Av[i+1]*dt
    Bx[i+1] = Bx[i] + Bv[i+1]*dt


plt.plot(t,Ax)
plt.plot(t,Bx)
plt.grid()
plt.title("2 Osciladores Harmonicos Simples Acoplados")
