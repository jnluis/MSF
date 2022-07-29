# -*- coding: utf-8 -*-1
"""
Created on Mon May  9 17:30:26 2022

@author: joão
v =-A*w*sin(wt+d)
A =-A*w**2*cos(wt+d)
"""
import numpy as np

x0 = 2
v0 = 0
k = 4
xeq = 1.5
m = 0.5
b = 1

ti = 0
tf = 10
dt = 0.00001
n = int((tf-ti)/dt)

t = np.linspace(ti,tf,n+1)

def oscHarmSimp_1D(x0,v0,n,dt):
    x=np.empty(n+1)
    v=np.empty(n+1)
    a=np.empty(n+1)
    Em = np.empty(n+1)
    x[0]=x0
    v[0]=v0
    for i in range(n):
        a[i]=(-2*k*x[i]*((x[i]**2)-(xeq**2))-b*v[i]+10*np.cos(t[i]))/m
        v[i+1]=v[i]+a[i]*dt
        x[i+1]=x[i]+v[i+1]*dt
        Em[i] = 0.5*m*(v[i]**2) + 0.5*k*(((x[i]**2)-(xeq**2))**2)
    Em[n] = 0.5*m*(v[n]**2) + 0.5*k*(((x[n]**2)-(xeq**2))**2)
    return x,v,a,Em

def maxminv(xm1,xm2,xm3,ym1,ym2,ym3):
    xab=xm1-xm2
    xac=xm1-xm3
    xbc=xm2-xm3
    a=ym1/(xab*xac)
    b=-ym2/(xab*xbc)
    c=ym3/(xac*xbc)
    xmla=(b+c)*xm1+(a+c)*xm2+(a+b)*xm3
    xm=0.5*xmla/(a+b+c)
    xta=xm-xm1
    xtb=xm-xm2
    xtc=xm-xm3
    ymax=a*xtb*xtc+b*xta*xtc+c*xta*xtb
    return xm, ymax

def lim(t,x,n):
    indMax = []
    for i in range(n):
        if(x[i-1]<x[i] and x[i]>x[i+1] and t[i]>0):
            indMax.append(i)

    indMin = []
    for i in range(n):
        if(x[i-1]>x[i] and x[i]<x[i+1] and t[i]>0):
            indMin.append(i)

    tmax = np.zeros(len(indMax))
    xmax = np.zeros(len(indMax))
    tmin = np.zeros(len(indMin))
    xmin = np.zeros(len(indMin))
    c=0
    for i in indMax:
        tmax[c], xmax[c] = maxminv(t[i-1], t[i], t[i+1], x[i-1], x[i], x[i+1])
        c+=1

    j=0
    for i in indMin:
        tmin[j], xmin[j] = maxminv(t[i-1], t[i], t[i+1], x[i-1], x[i], x[i+1])
        j+=1

    amplitude = np.mean(xmax)
    print("Amplitude (Máximo):", amplitude) 
    minimo = np.mean(xmin)
    print("Mínimo:", minimo)
    periodo = tmax[1]-tmax[0]
    print("Período:", periodo)
    freq = 1/periodo
    print("Frequência:", freq)

values = oscHarmSimp_1D(x0,v0,n,dt)
x = values[0]
Em = values[3]

lim(t,x,n)