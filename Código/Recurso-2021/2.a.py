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
alpha = np.radians(45) #degrees

#Tmpo inicial e final
ti =0
tf=2
dt = 0.001
n = int((tf-ti) / dt)

#velocidade inicial
v0 =10 
VT = 20 # em m/s
#Arrays precisam ser todos definidos
t = np.linspace(ti, tf, n)

vx = np.empty(n)
ax = np.empty(n)
x = np.empty(n)

vy= np.empty(n)
ay = np.empty(n)
y = np.empty(n)


vx[0] = v0*np.cos(alpha)
vy[0] = v0*np.sin(alpha)
v= np.empty(n)

omega_z =100
x[0] = 0
y[0] = 2.5
D =g/(VT**2)
floor = np.zeros(t.size)
#Preencher o vetor v
for i in range(n-1):
    v[i] = np.sqrt((vx[i]**2) + (vy[i]**2))
    ay[i+1] =- D* abs(v[i])* vy[i] -g # tem i+1 apenas para minimizar o erro. Não se deve pôr. também porque a[0] está definido
    ax[i+1] =-D * vx[i] * abs(v[i])
    
    vx[i+1] = vx[i] +ax[i]*dt
    vy[i+1] = vy[i] + ay[i]*dt
    
    x[i+1] = x[i] + vx[i]*dt
    y[i+1] = y[i] + vy[i]*dt
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
        print("Chegou ao chão no instanste {:0.2f} s.".format(t[i]))
        plt.plot(x[i+1],y[i+1], "o", label="Alcance")
        break    
    
plt.plot(x,y, label= "bola de basket")
plt.plot(x, floor, color="peru",label="Floor") # com color, pode-se meter as cores todas do CSS
plt.xlabel("x (m) ")
plt.ylabel("y (m)")
plt.title("Bola de basket com ângulo de 45º com rotação nula")
plt.grid()
plt.legend()

