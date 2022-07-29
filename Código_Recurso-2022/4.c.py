# -*- coding: utf-8 -*-1
"""
Created on Mon May  9 17:30:26 2022

@author: joão
v =-A*w*sin(wt+d)
A =-A*w**2*cos(wt+d)
"""

import matplotlib.pyplot as plt
import numpy as np


def maxminv(xm1,xm2,xm3,ym1,ym2,ym3):
# Máximo ou mínimo usando o polinómio de Lagrange
# Dados (input): (x0,y0), (x1,y1) e (x2,y2)
# Resultados (output): xm, ymax
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

t0 = 0.0
tf = 10
dt = 0.0001
n = int((tf-t0)/dt)
k = 4
m = 0.5
x0 = 2
v0 = 0
xEq = 1.5

t = np.zeros(n+1)
x = np.zeros(n+1)
vx = np.zeros(n+1)
ax = np.zeros(n+1)
emec = np.zeros(n+1)


x[0] = x0
vx[0] = v0


for i in range(n):
    t[i+1] = t[i] + dt
    ax[i] = (-2*k*x[i]*(x[i]**2-xEq**2)   )/m
    vx[i+1] = vx[i] + ax[i] * dt
    x[i+1] = x[i] + vx[i+1] * dt
    emec[i] = 0.5*m*vx[i]**2 + 0.5*k*(x[i]**2 - xEq**2)**2 # Emec = Ec + EpotElastica

emec[i+1] = 0.5*m*vx[i+1]**2 + 0.5*k*(x[i+1]**2 - xEq**2)**2 

plt.title("Posição x tempo")
plt.plot(t,x)
plt.grid()
plt.show()

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


xp = x[indMax[0]:indMax[1]]  # slices
tp = t[indMax[0]:indMax[1]]

it1 = int((tp[len(tp)-1]-tp[0])/dt)

print("Energia mecânica: ", emec[0])
plt.title("Energia mecância x tempo")
axis = plt.gca()
axis.set_ylim(0,50)
plt.plot(t,emec)
plt.show()