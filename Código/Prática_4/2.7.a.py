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


#velocidade inicial
vi =10
n =40

#vetor posição (empty e não zeros para não alterar muito o resultado, e é fácil de ver se estiver mal)
y = np.empty(n)

y0 = 0
y[0] = y0
#vetor tempo (ver se é n ou n+1 por causa do último número)
t = np.linspace(0, 2.2, n)
y_ch = np.zeros(t.size)
#Preencher o vetor v
for i in range(n-1):
    #v0 aqui é  a velocidade inicial desde o último ponto
    # y = (0.5*g * t**2) + y0 + v0t
    y = t*(10.0 - 4.9*t)

        
plt.plot(t,y, label= "y(t) do objeto")
plt.plot(t,y_ch, label= "Y=0")
plt.xlabel("t (s) ")
plt.ylabel("Altura (m)")
plt.title("Objeto lançado verticalmente para cim (sem Resistência do ar)")
plt.grid()
plt.legend()

