#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 17:17:00 2022

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
dt = 0.001

#velocidade inicial
v0 =0
n =int( (tf -t0) / dt)

#vetor velcoidade (empty e não zeros para não alterar muito o resultado, e é fácil de ver se estiver mal)
v = np.empty(n)

#Introduzir v0 no vetor velocidade
v[0]= v0

#vetor tempo (ver se é n ou n+1 por causa do último número)
t = np.linspace(0, 4, n)

#Preencher o vetor v
for i in range(n-1):
    #v0 aqui é  a velocidade inicial desde o último ponto
    # v = v0 + a * t
    v[i+1]= v[i] +g *dt

y = g*t + v0 

#Calcular a velocidade no instante pretendido (t=3s)
for i in range(n-1):
    if ((t[i] > (3-dt) and t[i+1] < (3+dt))):
        print('dt, t, vy = ', dt, t[i+1], v[i+1])
        
plt.plot(t,v, label= "v(t) do objeto")
plt.xlabel("t (s) ")
plt.ylabel("Velocidade (m/s) ")
plt.title("Objeto largado de uma altura elevada (sem Resistência do ar)")
plt.grid()
plt.legend()
print("A velocidade em 3 segundos é ",v)
#comparar as outras alíneas com o resultado exato
v= -29.40000000000001

print("O passo menor tem o resultado mais exato")
