#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 18:26:38 2022

@author: joao
"""

import numpy as np
import matplotlib.pyplot as plt


#aceleração gravítica
g =-9.8
#tempo inicial e tempo final
t0= 0
tf =4
# dt incremento do tempo e n número de intervalos
dt = 0.1

#velocidade inicial
v0 =0
n =int( (tf -t0) / dt)

#vetor velcoidade (empty e não zeros para não alterar muito o resultado, e é fácil de ver se estiver mal)
v = np.empty(n)
y = np.empty(n)

#Introduzir v0 no vetor velocidade
v[0]= v0
y0 = 0
y[0] = y0
#vetor tempo (ver se é n ou n+1 por causa do último número)
t = np.linspace(0, 4, n)

#Preencher o vetor v
for i in range(n-1):
    #v0 aqui é  a velocidade inicial desde o último ponto
    # v = v0 + a * t
    v[i+1]= v[i] +g *dt
    y[i+1]= y[i]+ v[i]*dt 

#Calcular a velocidade no instante pretendido (t=2s)
for i in range(n-1):
    if ((t[i] > (2-dt) and t[i+1] < (2+dt))):
        print('dt, t, vy = ', dt, t[i+1], v[i+1])
        
plt.plot(t,y, label= "y(t) do objeto")
plt.xlabel("t (s) ")
plt.ylabel("Altura (m)")
plt.title("Objeto largado de uma altura elevada (sem Resistência do ar)")
plt.grid()
plt.legend()