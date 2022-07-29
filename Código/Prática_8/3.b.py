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
alpha = np.radians(10) #degrees

#Tmpo inicial e final
ti =0
tf=1
dt = 0.001
n = int((tf-ti) / dt)
m= 0.057

r = 0.067/2
A = np.pi* (r**2) #porque é a área do círculo

c= 0.5*A*1.225*r / m


#velocidade inicial
v0 =100 / 3.6 # para coonverter para m/s
VT = 100 /3.6 # em m/s
#Arrays precisam ser todos definidos
t = np.linspace(ti, tf, n)

v = np.empty(n)
vx = np.empty(n)
ax = np.empty(n)
x = np.empty(n)

vy= np.empty(n)
ay = np.empty(n)
y = np.empty(n)
Em = np.empty(n)


vx[0] = v0*np.cos(alpha)
vy[0] = v0*np.sin(alpha)

v= np.empty(n)



omega_z =100
x[0] = 0
y[0] = 0


D =g/(VT**2)
floor = np.zeros(t.size)
#Preencher o vetor v
for i in range(n-1):
    v[i] = np.sqrt((vx[i]**2) + (vy[i]**2)) 
    ax[i] = -D * abs(v[i]) * vx[i]
    ay[i] = -D * abs(v[i]) * vy[i] -g

    vx[i+1] = vx[i] +ax[i]*dt 
    vy[i+1] = vy[i] + ay[i]*dt 
    
    x[i+1] = x[i] + vx[i]*dt
    y[i+1] = y[i] + vy[i]*dt
    Em[i] = 0.5*m* v[i]**2 + m*g* y[i]
    
v[n-1] = np.sqrt((vx[n-1]**2) + (vy[n-1]**2))    
Em[n-1] =  0.5*m* v[n-1]**2 + m*g* y[n-1]  

for i in range(n-1):
    if (i==0):
        print("t[{:0.2f}] = {:0.2f} Em[{:0.2f}] = {:0.2f}".format(i,t[i], i, Em[i]))
        plt.plot(t[i],Em[i], "o", label="t=0")
    if (t[i] < 0.4 < t[i+1]):
        print("t[{:0.2f}] = {:0.2f} Em[{:0.2f}] = {:0.2f}".format(i,t[i], i, Em[i]))
        plt.plot(t[i],Em[i], "o", label="t=0.4")
    if (t[i] < 0.8 < t[i+1]):
        print("t[{:0.2f}] = {:0.2f} Em[{:0.2f}] = {:0.2f}".format(i,t[i], i, Em[i]))
        plt.plot(t[i],Em[i], "o", label="t=0.8")

plt.plot(t,Em)
plt.xlabel("t (s) ")
plt.ylabel("Em (J)")
plt.title("Energia Mecânica (t)")
plt.grid()
plt.show()

plt.plot(x,y)
plt.xlabel("t (s) ")
plt.ylabel("Em (J)")
plt.title("Trajetória da bola de ténis com resistência do ar")
plt.grid()



