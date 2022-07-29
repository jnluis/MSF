#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 18:26:38 2022

@author: joao
"""

import numpy as np
import matplotlib.pyplot as plt

# Gravidade
g = 9.8

# Massa

m = 0.057

# Tempo inicial e final
ti = 0
tf = 1.25

# Velocidade terminal (paraquedas fechado)
vtx = 100 * 1000 / 3600
vty = 100 * 1000 / 3600
vtz = 100 * 1000 / 3600

# Angulo inicial
alpha = 7

# Posição inicial
xx0 = 0
xy0 = 0

# Velocidade inicial
v0 = 100 * 1000 / 3600

vx0 = v0 * np.cos(np.deg2rad(alpha))
vy0 = v0 * np.sin(np.deg2rad(alpha))



# Calcular D para a resistencia do ar
Dx = g / (vtx * np.abs(vtx))
Dy = g / (vty * np.abs(vty))


# dt incremento do tempo e n numero de intervalos
dt = 0.001
n = int((tf - ti) / dt)

# Vetor tempo (n+1 para garantir que nao falta o ultimo dado (Ex: t[10]))
t = np.linspace(ti, tf, n + 1)

# Vetor velocidade (empty e não zeros para não alterar 
# muito o resultado se faltar analisar um dado)
xx = np.empty(n + 1)
vx = np.empty(n + 1)
ax = np.empty(n + 1)

xy = np.empty(n + 1)
vy = np.empty(n + 1)
ay = np.empty(n + 1)

Emec = np.empty(n + 1)

axRes = np.empty(n + 1)
ayRes= np.empty(n + 1)
f = np.empty(n + 1)
workRes = np.empty(n + 1)


# Introduzir x0 e v0 nos vetores da posição e velocidade
xx[0] = xx0
vx[0] = vx0

xy[0] = xy0
vy[0] = vy0



# Preencher os vetores x, v, a
for i in range(n):
    vTotal = np.sqrt(vx[i] ** 2 + vy[i] ** 2)
        
    ax[i] = - Dx * np.abs(vTotal) * vx[i]
    xx[i + 1] = xx[i] + vx[i] * dt
    vx[i + 1] = vx[i] + ax[i] * dt
    
    ay[i] = - Dy * np.abs(vTotal) * vy[i] - g
    xy[i + 1] = xy[i] + vy[i] * dt
    vy[i + 1] = vy[i] + ay[i] * dt
    
    Emec[i] = 0.5 * m * vTotal**2 + m * g * xy[i]
    
    
    axRes[i] = - Dx * np.abs(vTotal) * vx[i]
    ayRes[i] = - Dy * np.abs(vTotal) * vy[i]
    
    f[i] = (m * axRes[i] * vx[i] + m * ayRes[i] * vy[i])
    workRes[i] = ((f[0] + f[i]) * 0.5 + np.sum(f[1:i])) * dt #Integração trapezoidal    
 
    
vTotal = np.sqrt(vx[-1] ** 2 + vy[-1] ** 2)
Emec[-1] = 0.5 * m * vTotal**2 + m * g * xy[-1]
        

axRes[-1] = - Dx * np.abs(vTotal) * vx[-1]
ayRes[-1] = - Dy * np.abs(vTotal) * vy[-1]

f[-1] = (m * axRes[-1] * vx[-1] + m * ayRes[-1] * vy[-1])
workRes[-1] = ((f[0] + f[-1]) * 0.5 + np.sum(f[1:-1])) * dt     
   
    
# Encontrar os dados do paraquedista quando ele chega ao solo (x = 0)
for i in range(n):
    if (vy[i] > (0 - dt) and vy[i + 1] < (0 + dt)):
        print("Vy = 0:")
        print("t >               |     xx >        |     xy >         |   vy >")
        print(t[i], xx[i], xy[i], vy[i])
        print("")
        plt.plot(xx[i], xy[i], "o", markersize="10", linewidth=5, color="red")
        
    if (xy[i] > (0 - dt) and xy[i + 1] < (0 + dt)):
        print("Xy = 0:")
        print("t > |    xx >          |     xy >           |   vy >")
        print(t[i], xx[i], xy[i], vy[i])
        print("")
        plt.plot(xx[i], xy[i], "o", markersize="10", linewidth=5, color="red")



# Plot
plt.plot(xx, xy, label="x",  linestyle='-', linewidth=3, color="turquoise")
plt.xlabel("x (t)")
plt.ylabel("y (t)")
plt.legend()         # Legenda só aparece com isto
plt.grid()
plt.show()


# Plot
plt.plot(t, f, label="x",  linestyle='-', linewidth=3, color="turquoise")
plt.xlabel("x (t)")
plt.ylabel("y (t)")
plt.legend()         # Legenda só aparece com isto
plt.grid()
plt.show()
        
# Encontrar os dados do paraquedista quando ele chega ao solo (x = 0)
for i in range(n):
    if ((0 - dt) < t[i] < (0 + dt)) or ((0.4 - dt) < t[i] < (0.4 + dt)) or ((0.98 - dt) < t[i] < (0.98 + dt)):
        print("T =", t[i],":")
        print("t >  | workRes >")
        print(t[i],"  " , workRes[i])
        print("t >  |   Emec >")
        print(t[i],"  " , Emec[i])
        print("")
        plt.plot(t[i], workRes[i], "o", markersize="10", linewidth=5, color="red")
        


# Plot
plt.plot(t, 0 * xy, linestyle='-', linewidth=3, color="red")
plt.plot(t, workRes, label="Emec",  linestyle='-', linewidth=3, color="turquoise")
plt.xlabel("t (s)")
plt.ylabel("Emec (J)")
plt.legend()         # Legenda só aparece com isto
plt.grid()


