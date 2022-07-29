#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 16:51:15 2022

@author: joao
"""

import matplotlib.pyplot as plt
import numpy as np


#b) Calcule a amplitude do movimento e o seu período, usando os resultados numéricos.

m = 1
k = 1
g=9.8

t0 = 0
tf =50
dt = 0.01

n = int((tf-t0)/dt)
t = np.linspace(t0,tf,n)

x = np.empty(n)
v = np.empty(n)
a = np.empty(n)

x[0] = 4
v[0] = 0

a[0] = -k/m*x[0]

arrayMaximos = []
temposMax = []
periodos = []

for i in range(n-1):   
    a[i+1] = -k/m*x[i]
    v[i+1] = v[i] +a[i+1]*dt #a[i+1] - euler cromer
    x[i+1] = x[i] +v[i+1]*dt #v[i+1] - euler cromer

for i in range(n-1):
    if (x[i-1]<x[i]>x[i+1] and i>0 ): 
        arrayMaximos.append(x[i])
        temposMax.append(t[i])
        
for i in range(len(temposMax)-1):
    periodos.append(temposMax[i+1] - temposMax[i])     

amplitude = sum(arrayMaximos)/len(arrayMaximos)
PeriodoMedia = sum(periodos) / len(periodos)

print("A amplitude média é {:.4f} m".format(amplitude))
print("O período médio é {:.4f} m".format(PeriodoMedia))

plt.plot(t,x)
plt.xlabel("t (s)")
plt.ylabel("x (m)")
plt.title("Lei do movimento")
plt.show()