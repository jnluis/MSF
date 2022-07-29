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

#velocidade inicial
v0 =30 / 3.6 # para coonverter para m/s

u = 0.004
m= 75
Cres = 0.9
Af = 0.3
densidade_ar= 1.225

#Tmpo inicial e final
ti =0
tf=60
dt = 0.001
n = int((tf-ti) / dt)


#Arrays precisam ser todos definidos
t = np.linspace(ti, tf, n)

v = np.empty(n)
vx = np.empty(n)
ax = np.empty(n)
x = np.empty(n)

vx[0] = 1
v[0] = 1
ax[0] = 0
tolerancia = 0.00001

P = 0.4 * 745.698872
print(P)

for i in range(n-1):
    v[i] = np.sqrt(vx[i] **2)
    ax[i] = -u*g - (Cres*Af*densidade_ar*v[i]*vx[i])/(2*m) + P/(m*v[i])

    vx[i+1] = vx[i] +ax[i]*dt  
    
    if vx[i+1]-vx[i] < tolerancia:
        print("vT = {:0.2f}".format(vx[i]))
        plt.plot(t[i],vx[i], "o",label="vT")
        break
    
v[n-1] = np.sqrt(vx[n-1]**2)


print("Velocidade terminal = ",v[n-1]) #Valor da velocidade terminal (último valor do array) não funcmina
plt.plot(t[1:i],vx[1:i]) # Cegada inventada pelo Diogo
plt.xlabel("t (s) ")
plt.ylabel("v (m/)")
plt.title("Velocidade terminal ")
plt.legend()
plt.grid()
plt.show()
