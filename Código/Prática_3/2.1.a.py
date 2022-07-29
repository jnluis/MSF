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

v0c = 700/ 36

v0p=0
ac =0
ap = 2

t = np.linspace(0, 30, 100)
xtc = v0c * t
xtp = t*t

plt.plot(t,xtc, label= "X(t) Carro A")
plt.plot(t,xtp, label= "X(t) Carro patrulha")
plt.xlabel("t (s) ")
plt.ylabel("Posição (m) ")
plt.legend()