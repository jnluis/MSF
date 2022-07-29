#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 16:51:15 2022

@author: joao
"""
import matplotlib.pyplot as plt
import numpy as np
def abfourier(tp,xp,it0,it1,nf):
#
# cálculo dos coeficientes de Fourier a_nf e b_nf
#       a_nf = 2/T integral ( xp cos( nf w) ) dt   entre tp(it0) e tp(it1)
#       b_nf = 2/T integral ( xp sin( nf w) ) dt   entre tp(it0) e tp(it1)    
# integracao numerica pela aproximação trapezoidal
# input: matrizes tempo tp   (abcissas)
#                 posição xp (ordenadas) 
#       indices inicial it0
#               final   it1  (ao fim de um período)   
#       nf índice de Fourier
# output: af_bf e bf_nf  
# 
    dt=tp[1]-tp[0]
    per=tp[it1]-tp[it0]
    ome=2*np.pi/per

    s1=xp[it0]*np.cos(nf*ome*tp[it0])
    s2=xp[it1]*np.cos(nf*ome*tp[it1])
    st=xp[it0+1:it1]*np.cos(nf*ome*tp[it0+1:it1])
    soma=np.sum(st)
    
    q1=xp[it0]*np.sin(nf*ome*tp[it0])
    q2=xp[it1]*np.sin(nf*ome*tp[it1])
    qt=xp[it0+1:it1]*np.sin(nf*ome*tp[it0+1:it1])
    somq=np.sum(qt)
    
    intega=((s1+s2)/2+soma)*dt
    af=2/per*intega
    integq=((q1+q2)/2+somq)*dt
    bf=2/per*integq
    return af,bf

def graficoBarras(ii,lst,xlabel,ylabel):
    plt.figure()
    plt.xlabel(xlabel) 
    plt.ylabel(ylabel)
    plt.bar(ii,np.abs(lst))
    plt.grid(True)
    plt.show()

m = 0.5
k = 2

xeq = 0
alpha = -0.1
beta = 0.02

x0=1.5
v0=0.5

t0 = 0
tf =20
dt = 0.0001

n = int((tf-t0)/dt)
t = np.linspace(t0,tf,n)

x = np.empty(n)
v = np.empty(n)
a = np.empty(n)
Ep = np.empty(n)
Ec = np.empty(n)
EM = np.empty(n)

x[0] = x0
v[0] = v0

a[0] = (-3*alpha*(x[0]**2) +4*beta*(x[0]**3) - k * x[0] ) /m

countMax = 0 
ind = np.transpose([0 for i in range(1000)])

for i in range(n-1):  
    a[i+1] = (-3*alpha*(x[i]**2) +4*beta*(x[i]**3) - k * x[i] ) /m
    v[i+1] = v[i] +a[i+1]*dt #a[i+1] - euler cromer
    x[i+1] = x[i] +v[i+1]*dt
    
    #Ep[i] = 0.5*k*(x[i]**2) + alfa*(x[i]**3)
    #EM[i] = 0.5*m*v[i]**2 + Ep[i]
    
    if (t[i]>0 and x[i-1]<x[i]>x[i+1] and i>0 ):
        countMax = countMax+1
        ind[countMax] = int(i)
    
#Ep[n-1] = 0.5*k*(x[n-1]**2) + alfa*(x[n-1]**3)
#EM[n-1] = 0.5*m*v[n-1]**2 + Ep[n-1]

print("-----------------Alinea (c)-------------------")
arrayMaximos = []
arrayMinimos= []
temposMax = []
temposMin = []

for i in range(n-1):
    if (x[i-1]<x[i]>x[i+1] and i>0 ): 
        arrayMaximos.append(x[i])
        temposMax.append(t[i])
    if (x[i-1]>x[i]<x[i+1] and i>0 ): 
        arrayMinimos.append(x[i])
        temposMin.append(t[i])
        
periodos = []

for i in range(len(temposMax)-1):
    periodos.append(temposMax[i+1] - temposMax[i])


amplitude = sum(arrayMaximos)/len(arrayMaximos)
minimo = sum(arrayMinimos)/len(arrayMinimos)

periodoMedia = sum(periodos)/len(periodos)

#15 é um numero arbitario e calculo as 5 primeiras frequencias
afo=np.zeros(15)
bfo=np.zeros(15)
raiz=np.zeros(15)
    
li=np.linspace(0,14,15)

t0 = ind[countMax-1]
t1 = ind[countMax]

for i in range(15):
    af, bf = abfourier(t,x,t0,t1,i)
    afo[i]= af
    bfo[i]= bf
    raiz[i]= np.sqrt(af**2+bf**2)
    
for i in range(len(afo)-10):
    print
    print("an[{:d}] = {:.3f} / bn[{:d}] = {:.3f} / raiz[{:d}] = {:.3f} /".format(i, afo[i],i, bfo[i], i,raiz[i]))
    
    
    
#print("afo= ", i, af, bf, np.sqrt(af**2 + bf**2))

graficoBarras(li,afo,'n','| a_n |')
graficoBarras(li,bfo,'n','| b_n |')
graficoBarras(li,raiz,'n','np.sqrt(af**2 + bf**2)')