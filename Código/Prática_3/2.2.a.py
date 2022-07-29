#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 16:58:04 2022

@author: joao
"""

import numpy as np
import matplotlib.pyplot as plt

vt = 6.8 #m/s
g = 9.8 #M/s**2
t = np.linspace(0, 4, 100)
y = ((vt**2)/g) * np.log(np.cosh((g*t)/  vt))


plt.plot(t,y, label= "Y(t) do volante")
#plt.plot(t,xtp, label= "X(t) Carro patrulha")
plt.xlabel("t (s) ")
plt.ylabel("Posição (m) ")
plt.title("Gráfico do movimento do volante de badminton")
plt.grid()
plt.legend()