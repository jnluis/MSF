#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 18:26:38 2022

@author: joao
"""

import numpy as np
import matplotlib.pyplot as plt

#Se partir com a velocidade de 1 m/s, qual a lei do movimento (espaço percorrido em função do tempo)?
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
dt = 0.01

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
    

print("Distância percorrida em km-->",x[-1])   

#b- Depois de perder toda a energia (sem motor) qual a distância suplementar percorrida pelo carro? 
v0 = v[-2] #velocidade que vai passar a ser a inicial calculada pela a alinea a

m = 1500
Cres = 0.9
A = 1.8*1.3
p = 1.225
u = 0.1
g = 9.8 # em m/s²
vi = 1
t0 = 0
tf = 50
dt = 0.0001

n = int((tf-t0)/dt)

#Arrays precisam ser todos definidos
t = np.linspace(t0, tf, n)

v = np.zeros(n)
vx = np.zeros(n)
ax = np.zeros(n)
ay = np.zeros(n)
x = np.zeros(n)

vx[0] = v0
v[0] = v0
ax[0] = 0

for i in range(n-1):
    v[i] = np.sqrt(vx[i] **2)
    ax[i] = -u*g - (Cres*A*p*v[i]*vx[i])/(2*m) 
    ay[i] = 0 # O peso corta com a normal
    vx[i+1] = vx[i] +ax[i]*dt  
    x[i+1] = x[i] + v[i]*dt  
    if vx[i] <= 0.0:
        print("Distância suplementar percorrida pelo carro",x[i])
        break
        #frol= 0
        #ax[i]=  - (Cres*A*p*v[i]*vx[i])/(2*m) Maneira do professor. Não percebi
        
plt.plot(t,vx) #grafico da velocidade após desligar o carro

#plt.plot(t,x) # para fazer o grafico em horas e km
plt.xlabel("t (s) ")
plt.ylabel("v (m/s)")
plt.title("Velocidade sem bateria")
plt.grid()

#alinea c
print("A energia gasta pelo carro é ",P*10800," Joules")


