#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 18:26:38 2022

@author: joao
"""

import numpy as np

m = 1000*1000
P = 7000*1000
v0 = 0.5
x0 = 0
cres = 0.9
dar = 1.225
A = 3.12*4.88
u = 0.001

ti = 0
tf = 10000
dt = 0.1
n = int((tf-ti)/dt)

t = np.linspace(ti,tf,n+1)

def planoInclinado_res_1D(x0,v0,n,dt,cres,u,A,m,P,ang=0):
    x=np.empty(n+1)
    vx=np.empty(n+1)
    ax=np.empty(n+1)
    aresx=np.empty(n+1)
    
    fun = np.empty(n)
    int_trab_res = np.empty(n)
    
    p_ar=1.225
    g=9.8
    
    x[0]=x0
    vx[0]=v0
    ax[0]=0
    
    for i in range(n):
        vv=np.abs(vx[i])
        aresx
        aresx[i]=-u*g*np.cos(ang) -(0.5*cres*A*p_ar*vx[i]*vv)/m 
        ax[i]=-g*np.sin(ang) + P/(m*vx[i])+aresx[i]
        vx[i+1]=vx[i]+ax[i]*dt
        x[i+1]=x[i]+vx[i]*dt

        fun[i] = m*aresx[i]*vx[i]
        int_trab_res[i] = dt*((fun[0] + fun[i])/2 + np.sum(fun[1:i]))
    return x,vx,ax,int_trab_res

values = planoInclinado_res_1D(x0,v0,n,dt,cres,u,A,m,P,ang=0)
x = values[0]
vx = values[1]
trab_res = values[3]

for i in range(n):
    if (2*60*60-dt)<t[i]<(2*60*60+dt):
        ti = i
        break

print("Trabalho:", trab_res[i])
print("Energia consumida:", P*2*60*60)
