#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 18:26:38 2022

@author: joao
"""

import numpy as np
import matplotlib.pyplot as plt

vi = 10 # m/s
dt = 0.001

tf = 2.2+dt
t0=0
n = int((tf-t0)/dt)

g = 9.8
#vTkm/h = 100 #km/h
vT= 100 / 3.6 #m/s 
D = g/ (vT**2)

T = np.arange(0,2.2+dt, dt)
v = np.zeros(T.size)
y = np.zeros(T.size)
a= np.zeros(T.size)

v[0] = 10
y[0] =0  
#a[0] = -g 
#Vem da outra alínea
y1 = T*(10.0 - 4.9*T)

floor = np.zeros(T.size)

for i in range(0, T.size-1):
        #v[i+1] = v[i]+ (g-c*v[i]*abs(v[i]))*dt # velocidade no instante
        a[i] =- D* v[i] * abs(v[i])-g
        v[i+1] = v[i]+ a[i]* dt
        y[i+1] = y[i] + v[i] * dt # posiçao no instante
        #Calcular a altura máxima e o instante
        
        
tmax= 10/9.8

#SÓ PARA O GRAFICO FICAR BONITO NO FINAL E NÃO FUGIR
a[-1] = a[-2]


plt.plot(T, floor, label="Y = 0")
plt.plot(T, y, label="y")
plt.plot(T, y1, label="Sem Rar")
plt.xlabel("t (s) ")
plt.ylabel("Altura (m)")
plt.title("Objeto lançado verticalmente para cima (com Resistência do ar)")
plt.grid()
plt.legend()
plt.show()



plt.plot(T, v,"y", label= "Velocidade")
plt.xlabel("t (s) ")
plt.ylabel("Velocidade (m/s)")
plt.grid()
plt.legend()
plt.show()



plt.plot(T, a,"m", label =" aceleração")
plt.xlabel("t (s) ")
plt.ylabel("Aceleração (m/s**2)")
plt.grid()
plt.legend()
plt.show()




