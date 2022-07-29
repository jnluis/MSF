#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 18:26:38 2022

@author: joao
"""

#c) Qual o ângulo com a horizontal que o jogador deve bater, para obter o máximo alcance?
# Fazer um "loop" de ângulos
import numpy as np

dt = 0.001
dphi = 0.1
angle = 10

angleArr = []
alcanceArr = []

while angle < 45:
    angleArr.append(angle)
    ang0 = angle/180*np.pi
    g = -9.8
    t0 =0
    tf =10
    
    n = int((tf-t0)/dt)
    t = np.linspace(t0,tf,n)
    
    x = np.empty(n)
    y = np.empty(n)

    vx = np.empty(n)
    vy = np.empty(n)
    v0 = 230/3.6

    D = -g/(6.8**2) #-g/vt**2
    
    y[0] = 2.5

    vx[0] = v0*np.cos(ang0)
    vy[0] = v0*np.sin(ang0)

    for i in range(n-1):
        vv = np.sqrt(vx[i]**2+vy[i]**2)
    
        ax = -D*vv*vx[i]
        ay = g-D*vv*vy[i]
        
        vx[i+1] = vx[i] + ax * dt
        vy[i+1] = vy[i] + ay * dt
    
        x[i+1] = x[i] + vx[i] * dt
        y[i+1] = y[i] + vy[i] * dt
        if y[i+1] < 0:
            break

    t = t[:i+2]
    vx = vx[:i+2]
    vy = vy[:i+2]
    x = x[:i+2]
    y = y[:i+2]

    angle += dphi
    alcanceArr.append(x[-1])
    
max_index = alcanceArr.index(max(alcanceArr))
print("Alcance máximo: {:.3f} m".format(alcanceArr[max_index]))
print("Ângulo: {:.3f} º".format(angleArr[max_index]))