#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 15:14:53 2022

@author: joao
"""

import matplotlib.pyplot as plt
import numpy as np

#c) Se o jogador imprimir rotação à bola, em que ponto cai no chão? Considere a força de Magnus
#𝐹⃗𝑀𝑎𝑔𝑛𝑢𝑠 =1/2 𝐴 𝜌𝑎𝑟 𝑟 𝜔⃗⃗ × 𝑣⃗
#e a rotação inicial se mantêm durante toda a trajetória 𝜔⃗⃗ = (0,0,100) rad/s, o raio é 15 cm, 𝜌𝑎𝑟 = 1.225 kg/m3
#e a massa é 625 g. Considerou-se o sistema de eixos o eixo OX a horizontal e OY a vertical do movimento. 

v0 = 10 # m/s
teta = np.radians(45)
dt = 0.0001
g = 9.8
t0 = 0
tf =3

vt= 72/3.6 # m/s

n = int((tf-t0)/dt)
t = np.linspace(t0,tf,n)

vx = np.empty(n)
vy = np.empty(n)
vz = np.empty(n)

ax = np.empty(n)
ay = np.empty(n)
az = np.empty(n)

x = np.empty(n) 
y = np.empty(n)
z = np.empty(n)

v = np.empty(n)

x[0] = 0
y[0] = 2.5
z[0] = 0

vx[0] = v0*np.cos(teta)
vy[0] = v0*np.sin(teta)
vz[0] = 0

#Força Magnus -------------------
wz = 100
par = 1.225
r= 0.15 #m
A = np.pi*r**2
m= 0.625 #kg
c = 1/2 * A * par * r 
#--------------------------------

d = g/vt**2

floor = np.zeros(t.size)
for i in range(n-1):    
    v[i] = np.sqrt(vx[i]**2 + vy[i]**2)
    
    amx = -c*wz*vy[i] #Força magnus
    amy = c*wz*vx[i]  #Força magnus
    
    ax[i] = -d*vx[i]*abs(v[i]) + amx / m #Acelaração com Força magnus
    ay[i] = -d*abs(v[i])*vy[i]-g + amy / m #Acelaração com Força magnus
    az[i] = 0 
    
    vx[i+1] = vx[i] +ax[i]*dt
    vy[i+1] = vy[i] + ay[i]*dt
    vz[i+1] = vz[i] +az[i]*dt
    
    y[i+1] = y[i] + vy[i] * dt
    x[i+1] = x[i] + vx[i] * dt
    z[i+1] = z[i] + vz[i] * dt
    
    
for i in range(n-1):
    if (y[i+1]<y[i]):
        print("A altura max é {:0.2f} m".format(y[i]))
        plt.plot(x[i],y[i], "o", label="Altura máxima")
        break
    
for i in range(n-1):
    if (y[i+1]*y[i]<0):
        print("Alcance {:0.2f} m".format(x[i]))
        plt.plot(x[i],y[i], "o", label="Alcance")
        break
    
plt.plot(x,y, label= "bola de basket")
plt.plot(x, floor, color="peru",label="Floor") # com color, pode-se meter as cores todas do CSS
plt.xlabel("x (m) ")
plt.ylabel("y (m)")
plt.title("Bola de basket com ângulo de 45º com rotação (0,0,100)")
plt.grid()
plt.legend()