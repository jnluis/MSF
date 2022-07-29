#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 18:26:38 2022

@author: joao
"""
import numpy as np
import matplotlib.pyplot as plt

r0 = [0,0,0]
vi = 328000/3600
ang = np.radians(30)
vx0 = vi*np.cos(ang)
vy0 = vi*np.sin(ang)
v0 = [vx0,vy0,0]
cres = 0.5
r = 0.0427/2
m = 0.0459
dar = 1.225
A = np.pi*(r**2)
g = 9.8
a0 = [0,-g,0]
rot = [0,0,209]

ti = 0
tf = 8
dt = 0.001
n = int((tf-ti)/dt)

t = np.linspace(ti,tf,n+1)
floor = np.zeros(t.size)   
def prodExt(a,b):
    return (a[1]*b[2]-b[1]*a[2],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])

def magnus_3D(r0,v0,a0,rot,p_ar,r,n,dt,m):
    A=np.pi*r**2
    apr=0.5*p_ar*A*r

    x=np.empty(n+1)
    y=np.empty(n+1)
    z=np.empty(n+1)
    
    vx=np.empty(n+1)
    vy=np.empty(n+1)
    vz=np.empty(n+1)
    
    ax=np.empty(n+1)
    ay=np.empty(n+1)
    az=np.empty(n+1)
    
    x[0]=r0[0]
    y[0]=r0[1]
    z[0]=r0[2]
    
    vx[0]=v0[0]
    vy[0]=v0[1]
    vz[0]=v0[2]
    
    ax[0]=a0[0]
    ay[0]=a0[1]

    az[0]=a0[2]
     
    for i in range(n):
        vv=np.sqrt(vx[i]**2 +vy[i]**2 +vz[i]**2)
        rot_v=prodExt(rot,(vx[i],vy[i],vz[i]))

        mag_x=apr*rot_v[0]/m
        mag_y=apr*rot_v[1]/m
        mag_z=apr*rot_v[2]/m

        ax[i]=a0[0]-(cres/(2*m))*A*dar*abs(vv)*vx[i]+mag_x
        ay[i]=a0[1]-(cres/(2*m))*A*dar*abs(vv)*vy[i]+mag_y
        az[i]=a0[2]-(cres/(2*m))*A*dar*abs(vv)*vz[i]+mag_z
        
        vx[i+1]=vx[i]+ax[i]*dt
        vy[i+1]=vy[i]+ay[i]*dt
        vz[i+1]=vz[i]+az[i]*dt
        
        x[i+1]=x[i]+vx[i]*dt
        y[i+1]=y[i]+vy[i]*dt
        z[i+1]=z[i]+vz[i]*dt
    return (x,y,z),(vx,vy,vz),(ax,ay,az)

values = magnus_3D(r0,v0,a0,rot,dar,r,n,dt,m)
x = values[0][0]
y = values[0][1]

for i in range(n):
    if y[i]*y[i+1]<0:
        print("Ponto solo:", x[i], "m")
        print("Tempo:", t[i], "s")
        break
    
plt.plot(x,y, label= "bola de golfe")
plt.plot(x, floor, color="peru",label="Floor") # com color, pode-se meter as cores todas do CSS
plt.xlabel("x (m) ")
plt.ylabel("y (m)")
plt.title("Bola de golfe com ângulo de 30º com w(0,0,209) rad/s")
plt.grid()
plt.legend()