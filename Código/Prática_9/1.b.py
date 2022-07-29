#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 18:26:38 2022

@author: joao
"""
#aceleração gravítica
g =9.8

#velocidade inicial
v0 =30 / 3.6 # para coonverter para m/s

u = 0.004
m= 75
Cres = 0.9
Af = 0.3
densidade_ar= 1.225
vx = 40/3.6

P = u*m*g*vx + (Cres * Af * densidade_ar* vx**2 * vx) / 2
print("Potência = ", P, " W")

