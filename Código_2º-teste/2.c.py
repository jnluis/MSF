#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 11:51:56 2022

@author: joao
"""

import matplotlib.pyplot as plt
import numpy as np

u = 0.01
m = 60+12
Area = 0.5
par = 1.225
g=9.8
Cres = 0.9

teta = np.radians(4)

P = 0.48*735.49875 #potencia

t0 = 0
tf =500
dt = 0.001

n = int((tf-t0)/dt)
t = np.linspace(t0,tf,n)

fAtrito=-u*m*g*np.cos(teta)
#fAtrito=-mu*massa*g #segundo sugetsoa do Torres. Ver apontamentos

vx = np.empty(n)
v = np.empty(n)
ax = np.empty(n)
x = np.empty(n)

aresx=np.empty(n)
fcil=np.empty(n)

vx[0] = 0.5
x[0] = 0

tolerancia=0.00000001
pesoX=-m*g*np.sin(teta)


for i in range(n-1):   
    
    v[i] = np.sqrt(vx[i]**2)
    aresx[i] = -Cres/(2*m)*Area*par*v[i]*vx[i]
    fcil[i] = P/(m*v[i])
    ax[i+1] = fAtrito/m+aresx[i]+fcil[i]+pesoX/m
    vx[i+1] = vx[i] +ax[i]*dt
    x[i+1] = x[i] + vx[i] * dt
    
v[n-1] = np.sqrt(vx[n-1]**2)

for i in range(n-1):
    if (x[i]>1500-dt and x[i]>1500+ dt): #é 1500m
        metro1500 = t[i]
        print("tempo aos 1500m = {:0.2f}".format( t[i]))
        break

teta = np.radians(1)

fAtrito=-u*m*g*np.cos(teta)
#fAtrito=-mu*massa*g #segundo sugetsoa do Torres. Ver apontamentos

vx = np.empty(n)
v = np.empty(n)
ax = np.empty(n)
x = np.empty(n)

aresx=np.empty(n)
fcil=np.empty(n)

vx[0] = 0.5
x[0] = 0

tolerancia=0.00000001
pesoX=m*g*np.sin(teta)

for i in range(n-1):   
    
    v[i] = np.sqrt(vx[i]**2)
    aresx[i] = -Cres/(2*m)*Area*par*v[i]*vx[i]
    fcil[i] = P/(m*v[i])
    ax[i+1] = fAtrito/m+aresx[i]+fcil[i]+pesoX/m
    vx[i+1] = vx[i] +ax[i]*dt
    x[i+1] = x[i] + vx[i] * dt
    
v[n-1] = np.sqrt(vx[n-1]**2)

for i in range(n-1):
    if (1500-dt<x[i]<2000-dt and 1500+dt<x[i]<2000+dt ): #é 5500m
        metro500 = t[i]
        print("tempo aos 500 = {:0.2f}".format( t[i]))
        break

print("tempo aos 2000 = {:0.2f}".format( metro1500+metro500))
plt.plot(t,v)
plt.xlabel("t (s)")
plt.ylabel("v (m/s)")
plt.title("Velocidade Terminal")
plt.show()