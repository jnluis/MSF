#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 18:26:38 2022

@author: joao
"""

import numpy as np
import matplotlib.pyplot as plt

#a- Se partir com a velocidade de 1 m/s, qual a lei do movimento (espaço percorrido em função do tempo)?
#Qual a distância percorrida em 3 horas?
m = 1500
Cres = 0.9
A = 1.8*1.3
p = 1.225
u = 0.1
g = 9.8 # em m/s²
vi = 1
t0 = 0
tf = 10800
dt = 0.001

n = int((tf-t0)/dt)

#Arrays precisam ser todos definidos
t = np.linspace(t0, tf, n)

v = np.empty(n)
vx = np.empty(n)
ax = np.empty(n)
ay = np.empty(n)
x = np.empty(n)

vx[0] = 1
v[0] = 1
ax[0] = 0
tolerancia = 0.00001

P = 283 *735.4975
print(P ,"Watts")

for i in range(n-1):
    v[i] = np.sqrt(vx[i] **2)
    ax[i] = -u*g - (Cres*A*p*v[i]*vx[i])/(2*m) + P/(m*v[i])
    ay[i] = 0 # O peso corta com a normal
    vx[i+1] = vx[i] +ax[i]*dt  
    x[i+1] = x[i] + v[i]*dt
    '''
    if vx[i+1]-vx[i] < tolerancia:
        print("vT = {:0.2f}".format(vx[i]))
        plt.plot(t[i],vx[i], "o",label="vT") # se fosse para calcular a velocidade
        break
    '''
#v[n-1] = np.sqrt(vx[n-1]**2)
plt.plot(t/3600,x*10**(-3)) # para fazer o grafico em horas e km
print(x[-1])
#plt.plot(t[1:i],vx[1:i])
plt.xlabel("t (h) ")
plt.ylabel("x (km)")
plt.title("Lei do Movimento ")
plt.grid()
plt.show()
