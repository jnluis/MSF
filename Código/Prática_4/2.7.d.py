#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 18:26:38 2022

@author: joao
"""

import numpy as np
import matplotlib.pyplot as plt

vi = 10 # m/s
dt = 0.001

g = -9.8

T = np.arange(0,2.2+dt, dt)
v = np.zeros(T.size)
y = np.zeros(T.size)

v[0] = 10
    
y1 = T*(10.0 - 4.9*T)

 # aceleraçao inicial

c = -g/(27.7778**2)

floor = np.zeros(T.size)

for i in range(0, T.size-1):
        v[i+1] = v[i]+ (g-c*v[i]*abs(v[i]))*dt # velocidade no instante
        y[i+1] = y[i] + v[i] * dt # posiçao no instante


fig = plt.figure()
ax = fig.add_subplot(1,1,1)

ax.set_xlabel('tempo (s)')
ax.set_ylabel('X (m)')
ax.plot(T, floor, label="Y = 0")
ax.plot(T, y, label="pos")
ax.plot(T, y1, label="analitical")

plt.legend()

