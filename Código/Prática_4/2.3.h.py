#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 18:33:24 2022

@author: joao
"""

import numpy as np
import matplotlib.pyplot as plt

n = 10

xCalc = -19.6

X = np.empty(n)

for i in range(n):
    X[i] = 0.1 / 2 ** i

Y = np.empty(n)

for num in range(len(X)):
    # Gravidade
    g = 9.8

    # Tempo inicial e final
    ti = 0
    tf = 3

    # Velocidade inicial
    v0 = 0
    y0 = 0

    # Aceleração
    a = -g

    # dt incremento do tempo e n numero de intervalos
    dt = X[num]
    n = int((tf - ti) / dt)

    # Vetor tempo (n+1 para garantir que nao falta o ultimo dado (Ex: t[10]))
    t = np.linspace(ti, tf, n + 1)

    # Vetor velocidade (empty e não zeros para não alterar 
    # muito o resultado se faltar analisar um dado)
    v = np.empty(n + 1)
    y = np.empty(n + 1)

    # Introduzir v0 no vetor velocidade
    v[0] = v0
    y[0] = y0

    # Preencher o vetor v
    for i in range(n):
        # v0 aqui é a velocidade inicial desde o ultimo ponto
        #   v    =  v0  + a * t
        v[i + 1] = v[i] + a * dt
        y[i + 1] = y[i] + v[i] * dt

    # Encontrar um ponto pretendido no vetor v
    # Tempo pretendido
    tp = 2
    # Se t[i] estiver entre o tempo pretendido - incremento
    #                       e tempo pretendido + incremento
    for i in range(n + 1):
        if ( t[i] > (tp - dt) and (tp + dt) > t[i] ):
            Y[num] = abs(xCalc - y[i])
            break



# Plot
plt.plot(X, Y, label="Desvio")
#plt.plot(X, Y, label="Desvio",  linestyle='-', linewidth=3, color="blue", markersize=10)
plt.ylabel("desvio")
plt.xlabel("dt")
plt.legend()         # Legenda só aparece com isto
plt.grid()