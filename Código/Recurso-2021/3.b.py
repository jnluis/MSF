#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 18:26:38 2022

@author: joao
"""
#aceleração gravítica
g =9.8

#velocidade inicial
v0 =90 / 3.6 # para coonverter para m/s # i
v0ii = 130/ 3.6 # ii

u = 0.004
m= 1200
Cres = 0.9
Af = 3
densidade_ar= 1.225
vx = 90/3.6

P = u*m*g*vx + (Cres * Af * densidade_ar* vx**2 * vx) / 2
print("Potência = ", P, " W")

P2 = u*m*g*v0ii + (Cres * Af * densidade_ar* v0ii**2 * v0ii) / 2
print("Potência para 130 km/h = ", P2, " W")