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
alpha = np.radians(16) #degrees

#Tmpo inicial e final
ti =0
tf=2
dt = 0.001
n = int((tf-ti) / dt)
m= 0.45

r = 0.11
A = np.pi* (r**2) #porque é a área do círculo

c= 0.5*A*1.225*r / m


#velocidade inicial
v0 =100 / 3.6 # para coonverter para m/s
VT = 100 /3.6 # em m/s
#Arrays precisam ser todos definidos
t = np.linspace(ti, tf, n)

vx = np.empty(n)
ax = np.empty(n)
x = np.empty(n)

vy= np.empty(n)
ay = np.empty(n)
y = np.empty(n)

vz= np.empty(n)
az = np.empty(n)
z = np.empty(n)

vx[0] = v0*np.cos(alpha)
vy[0] = v0*np.sin(alpha)
vz[0] = 0
v= np.empty(n)

omega_z =-10
x[0] = 0
y[0] = 0
z[0] =0
D =g/(VT**2)
floor = np.zeros(t.size)
#Preencher o vetor v
for i in range(n-1):
    v[i] = np.sqrt((vx[i]**2) + (vy[i]**2))
    amx = (-c*omega_z*vy[i]) 
    amy = (c *omega_z* vx[i])
    ay[i+1] =- D* abs(v[i])* vy[i] -g + amy
    ax[i+1] =-D * vx[i] * abs(v[i]) +amx
    az[i+1] = 0
    
    vx[i+1] = vx[i] +ax[i]*dt 
    vy[i+1] = vy[i] + ay[i]*dt 
    vz[i+1] = vz[i] + az[i]*dt
    
    x[i+1] = x[i] + vx[i]*dt
    y[i+1] = y[i] + vy[i]*dt
    z[i+1] = z[i] + vz[i]*dt
'''  
for para dar os valores todos 
for i in range(n):
    if (vy[i] > (0 - dt) and vy[i + 1] < (0 + dt)):
        print("Vy = 0:")
        print("t >              | xx >              | yy >          |     vy >")
        print(t[i], x[i], y[i], vy[i])
        print("")
        plt.plot(x[i+1],y[i+1], "o", label= "Altura máxima")
        break

for i in range(n):
    if (y[i] > (0 - dt) and y[i + 1] < (0 + dt)):
        print("Xy = 0:")
        print("t >              | xx >              | yy >          |     vy >")
        print(t[i], x[i], y[i], vy[i])
        print("")
        plt.plot(x[i+1],y[i+1], "o", label= "Alcance")
        break
'''   
for i in range(n-1):
    if (y[i+1]<y[i]):
        print("A altura max é {:0.2f} m".format(y[i]))
        plt.plot(x[i+1],y[i+1], "o", label="Altura máxima")
        break
    
for i in range(n-1):
    if (y[i+1]*y[i]<0):
        print("Alcance {:0.2f} m".format(x[i]))
        plt.plot(x[i+1],y[i+1], "o", label="Alcance")
        break    

for i in range(n-1):
    if (x[i] < 20 < x[i+1]):
        print("y[{:0.2f}] = {:0.2f} m".format( t[i],y[i]))
        plt.plot(x[i],y[i], "o", label="x=20m")
    
plt.plot(x,y, label= "bola de ténis")
plt.plot(x, floor, color="peru",label="Floor") # com color, pode-se meter as cores todas do CSS
plt.xlabel("x (m) ")
plt.ylabel("y (m)")
plt.title("Bola de futebol com angulo de 16º e rotação (0,0,-10)")
plt.grid()
plt.legend()
plt.show()

