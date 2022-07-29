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

d= sym.Derivative(vt*sym.tanh(g*t/vt) , t, evaluate = True) #expressão, derivar em ordem a x (Derivar a formula da velocidade)
print("dy/dt=",d)
a_inst = sym.simplify(d)
print("dy/dt=",a_inst)

vt = 6.8 #m/s     velocidade terminal (é o declive da reta que o gráfico forma)
grav = 9.8 #M/s**2

temp = np.linspace(0, 4, 100) #(tempo inicial, tempo final, número de pontos)

#Calcular valor aceleração instantânea
acel = grav/np.cosh(grav*temp/vt)**2

plt.plot(temp,acel, "g",label= "a(t) do volante")
plt.xlabel("t (s) ")
plt.ylabel("Aceleração (m/s**2) ")
plt.title("Queda volante com vY(0)=0")
plt.grid()
plt.legend()