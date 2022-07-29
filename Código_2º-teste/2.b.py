#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 18:26:38 2022

@author: joao
"""

import numpy as np

m = 72
Cres = 0.9
A = 0.5
p = 1.225
u = 0.01
g = 9.8
P = 0.48 * 735.4975
vi = 0.5
t0 = 0
tf = 2000
dt = 0.001

n = int((tf-t0)/dt)
t = np.linspace(t0, tf, n)

a = np.empty(n)
v = np.empty(n)
x = np.empty(n)

a[0] = 0
v[0] = vi
x[0] = 0

for i in range(n-1):
    v[i] = np.sqrt(v[i]**2)
    a[i] = -u*g - (Cres/(2*m))*A*p*(v[i])*v[i] + P/(m*v[i])
    v[i+1] = v[i] + a[i]*dt
    x[i+1] = x[i] + v[i]*dt

    if x[i] < 2000 + dt and x[i+1] > 2000-dt:
        print("Tempo a percorrer 2km = ", t[i])
        break
