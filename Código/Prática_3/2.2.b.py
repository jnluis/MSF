#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 16:58:04 2022

@author: joao
"""
import sympy as sym
import numpy as np
import matplotlib.pyplot as plt


t = sym.Symbol('t')
v = sym.Symbol('v')
vt = sym.Symbol('vt')
g = sym.Symbol('g')
d = sym.Symbol('D')
a = sym.Symbol('a')
aS = sym.Symbol('aS')

d = sym.Derivative(vt**2 / 2 * sym.log(sym.cosh(g/vt*t)), t, evaluate = True)
print("dy/dt=", d)
v = sym.simplify(d) #simplifica a expressão printada em cima
print("dy/dt=",v)


vt = 6.8 #m/s
grav = 9.8 #M/s**2

temp = np.linspace(0, 4, 100)
y = vt*np.tanh(grav*temp/vt)


plt.plot(temp,y, label= "v(t) do volante")
plt.xlabel("t (s) ")
plt.ylabel("Velocidade (m/s) ")
plt.title("Queda volante com vY(0)=0")
plt.grid()
plt.legend()