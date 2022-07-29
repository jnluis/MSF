#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 15:05:11 2022

@author: joao
"""
import numpy as np
import matplotlib.pyplot as plt

t0 = 0
x0 = 0
v0 = 0
g = 9.8
dt = 0.25       
n = 20
t= np.linspace(0, n*dt,n+1)
x= np.linspace(0, n*dt,n+1)
vx = g*t
xexat= 0.5*g*t*t

for i in range(n): #Método de Euler
    t[i+1]= t[i] +dt
    x[i+1] = x[i] + vx[i] *dt

plt.plot(t,xexat, label= "posição exata")
plt.plot(t,x, "x", label="Met Euler dt = 0.25s")
plt.xlabel("t (s) ")
plt.ylabel("Posição (m) ")


n = 10
dt = 0.5
t= np.linspace(0, n*dt,n+1)
x= np.linspace(0, n*dt,n+1)
vx = g*t
xexat= 0.5*g*t*t

for i in range(n): #Método de Euler
    t[i+1]= t[i] +dt
    x[i+1] = x[i] + vx[i] *dt
plt.plot(t,x, "go", label="Met Euler dt = 0.5s")

plt.legend()

#definir o método de euler pelas funções
''' def euler(dt):
    t0=0
    tf = 5.0
    x0=0
    v0x=0
    g=9.80
    n=np.int((tf-t0)/dt+0.1)
    t=np.linspace(0, n*dt, n+1)
    x=np.linspace(0, n*dt, n+1)
    
    t[0]=t0 
    x[0]=x0

    vx=g*t
    original = 0.5*g*t*t
    for i in range(n): # Método de Euler
        t[i+1]=t[i]+dt
        x[i+1]=x[i]+vx[i]*dt
    return original, t, x 

original = euler(0.25)[0]
t = euler(0.25)[1]
x = euler(0.25)[2]

plt.plot(t, original, label= "posição exata")
plt.plot(t, x, "+",  label= "Met Euler dt = 0.25s")

t = euler(0.50)[1]
x = euler(0.50)[2]

plt.plot(t, x, "o",  label= "Met Euler dt = 0.5s")

plt.xlabel("Tempo (s)")
plt.ylabel("Posição (m)")
plt.legend()'''

