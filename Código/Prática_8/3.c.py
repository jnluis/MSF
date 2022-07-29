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

#Alínea C
#aceleração resistencia do ar
aresx = np.empty(n)
aresy= np.empty(n)
fun = np.empty(n)
integracao_trapezoidal = np.empty(n)


vx[0] = v0*np.cos(alpha)
vy[0] = v0*np.sin(alpha)

x[0] = 0
y[0] = 0


D =g/(VT**2)
#Preencher o vetor v
for i in range(n-1):
    v[i] = np.sqrt((vx[i]**2) + (vy[i]**2)) 
    aresx[i] = -D * abs(v[i]) * vx[i]
    ax[i] = aresx[i]
    
    aresy[i] = -D * abs(v[i]) * vy[i]
    ay[i] = aresy[i] -g

    vx[i+1] = vx[i] +ax[i]*dt 
    vy[i+1] = vy[i] + ay[i]*dt 
    
    x[i+1] = x[i] + vx[i]*dt
    y[i+1] = y[i] + vy[i]*dt
    Em[i] = 0.5*m* v[i]**2 + m*g* y[i]
    
    fun[i] = m* aresx[i] * vx[i] + m* aresy[i] * vy[i]
    integracao_trapezoidal[i] = dt * ((fun[0]* fun[i]) *0.5 + np.sum(fun[1:n]))


v[n-1] = np.sqrt(vx[n-1]**2 + vy[n-1]**2)
Em[n-1] =  0.5*m* v[n-1]**2 + m*g* y[n-1]  

fun[n-1] = m* aresx[n-1] * vx[n-1] + m* aresy[n-1] * vy[n-1]
integracao_trapezoidal[n-1] = dt * ((fun[0]* fun[n-1]) *0.5 + np.sum(fun[1:n-1]))

for i in range(n-1):
    if (i==0):
        print("t[{:0.2f}] = {:0.2f} Em[{:0.2f}] = {:0.2f}".format(i,t[i], i, integracao_trapezoidal[i]))
        plt.plot(t[i],integracao_trapezoidal[i], "o", label="t=0")
    if (t[i] < 0.4 < t[i+1]):
        print("t[{:0.2f}] = {:0.2f} Em[{:0.2f}] = {:0.2f}".format(i,t[i], i, integracao_trapezoidal[i]))
    if (t[i] < 0.8 < t[i+1]):
        print("t[{:0.2f}] = {:0.2f} Em[{:0.2f}] = {:0.2f}".format(i,t[i], i, integracao_trapezoidal[i]))
        plt.plot(t[i],integracao_trapezoidal[i], "o", label="t=0.8")

plt.plot(t,integracao_trapezoidal)
plt.xlabel("t (s) ")
plt.ylabel("Em (J)")
plt.title("Energia Mecânica (t)")
plt.grid()
plt.show()




