#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 16:12:54 2022

@author: joao
"""
import numpy as np
import matplotlib.pyplot as plt

x0c =0
x0p =0

v0c = 700/ 36 # m/s conversão da velocidade para m/s 

v0p=0
ac =0
ap = 2 #m/s**2 aceleração do carro patrulha

t = np.linspace(0, 30, 100)
xtc = v0c * t #movimento uniforme carro A
xtp = t*t # movimento uniformenente acelerado carro patrulha

plt.plot(t,xtc, label= "X(t) Carro A")
plt.plot(t,xtp, label= "X(t) Carro patrulha")
plt.xlabel("t (s) ")
plt.ylabel("Posição (m) ")
plt.title("Gráfico da distância em função do tempo")
plt.legend()

t_intersect = v0c
x_intersect = v0c*v0c
print("O carro patrulha atinge o carro no instante t={:.2f} s, percorrendo X={:.1f} m.".format(t_intersect, x_intersect))
