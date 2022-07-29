#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 18:26:38 2022

@author: joao
"""
import matplotlib.pyplot as plt
import numpy as np

v0 = 328/3.6 # m/s
teta = np.radians(30)
dt = 0.0001
g = 9.8
t0 = 0
tf =9

n = int((tf-t0)/dt)
t = np.linspace(t0,tf,n)

vx = np.empty(n)
vy = np.empty(n)


ax = np.empty(n)
ay = np.empty(n)


x = np.empty(n) 
y = np.empty(n)
z = np.empty(n)

v = np.empty(n)

x[0] = 0
y[0] = 0


vx[0] = v0*np.cos(teta)
vy[0] = v0*np.sin(teta)


#Força Magnus -------------------
#wz = 100
par = 1.225
r= 0.0427/2 #m
A = np.pi*r**2
m= 0.0459 #kg
Cres = 0.5
#--------------------------------

floor = np.zeros(t.size)
for i in range(n-1):    
    v[i] = np.sqrt(vx[i]**2 + vy[i]**2)

    ax[i]=-(Cres/(2*m))*A*par*v[i]*vx[i]
    ay[i]=-g-(Cres/(2*m))*A*par*v[i]*vy[i]
    
    vx[i+1] = vx[i] +ax[i]*dt
    vy[i+1] = vy[i] + ay[i]*dt

    
    y[i+1] = y[i] + vy[i] * dt
    x[i+1] = x[i] + vx[i] * dt

    
    
for i in range(n-1):
    if (y[i+1]<y[i]):
        print("A altura max é {:0.2f} m".format(y[i]))
        plt.plot(x[i],y[i], "o", label="Altura máxima")
        break
    
for i in range(n-1):
    if (y[i+1]*y[i]<0):
        print("Alcance {:0.2f} m".format(x[i]))
        print("Chegou ao chão no instante {:0.2f} s.".format(t[i]))
        plt.plot(x[i],y[i], "o", label="Alcance")
        break
    
plt.plot(x,y, label= "bola de golfe")
plt.plot(x, floor, color="peru",label="Floor") # com color, pode-se meter as cores todas do CSS
plt.xlabel("x (m) ")
plt.ylabel("y (m)")
plt.title("Bola de golfe com ângulo de 30º com rotação nula")
plt.grid()
plt.legend()