#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 18:26:38 2022

@author: joao
"""

import numpy as np
import matplotlib.pyplot as plt

m = 200000
Cres = 0.9
A = 3.12*4.88
p = 1.225
u = 0.001
g = 9.8 # em m/s²
vi = 0.5
t0 = 0
tf = 7200
dt = 0.001

n = int((tf-t0)/dt)

#Arrays precisam ser todos definidos
t = np.linspace(t0, tf, n)

v = np.empty(n)
vx = np.empty(n)
ax = np.empty(n)
ay = np.empty(n)
x = np.empty(n)

vx[0] = 0.5
v[0] = 0.5
ax[0] = 0
tolerancia = 0.00001

P = 7000000
print(P ,"Watts")

for i in range(n-1):
    v[i] = np.sqrt(vx[i] **2)
    ax[i] = -u*g - (Cres*A*p*v[i]*vx[i])/(2*m) + P/(m*v[i])
    ay[i] = 0 # O peso corta com a normal
    vx[i+1] = vx[i] +ax[i]*dt  
    x[i+1] = x[i] + v[i]*dt
    ''' é preciso comentar a velocidade terminal para a distancia percorrida funcionar
    if vx[i+1]-vx[i] < tolerancia:
        print("vT = {:0.2f}".format(vx[i]))
        plt.plot(t[i],vx[i], "o",label="vT") # se fosse para calcular a velocidade
        break
    '''
plt.plot(t/3600,x*10**(-3)) # para fazer o grafico em horas e km
print(x[-1], " km percorridos" )
#plt.plot(t[1:i],vx[1:i]) grafico da velocidade terminal
plt.xlabel("t (h) ")
plt.ylabel("x (km)")
plt.title("Lei do Movimento ")
plt.grid()
plt.show()
