# -*- coding: utf-8 -*-1
"""
Created on Mon May  9 17:30:26 2022

@author: joão
"""
#c) Calcule a energia mecânica. É constante ao longo do tempo?
import matplotlib.pyplot as plt
import numpy as np

k = 1
m = 1

#t = np.arange(0, 200+dt, dt) Outra maneira de fazer o t
#Tmpo inicial e final
ti =0
tf=30
dt = 0.0001
n = int((tf-ti) / dt)
t = np.linspace(ti, tf, n)

x = np.empty(n)
v = np.empty(n)
a= np.empty(n)
Em = np.empty(n)

x[0] = 4
v[0] = 0
a[0] = -k/m*x[0]

ampsMax= []
temposMax = []
periodos = []

for i in range(n-1):
    a[i+1] = -k/m*x[i]
    v[i+1] = v[i] +a[i+1]*dt #a[i+1] - euler cromer
    x[i+1] = x[i] +v[i+1]*dt #v[i+1] - euler cromer

    v[i+1] = v[i] + a[i]*dt # Pelo método de Euler, não funcionava
    x[i+1] = x[i]+v[i+1]*dt

Em = 0.5*m* v**2 + 0.5*k*(x**2) #alínea C   
for i in range(n-1):
    if (x[i-1]<x[i]>x[i+1] and i>0 ): 
        ampsMax.append(x[i])
        temposMax.append(t[i])
    
AmplitudeMédia = sum(ampsMax) / len(ampsMax)
print(AmplitudeMédia)    
#alinea b        
for i in range(len(temposMax)-1):
    periodos.append(temposMax[i+1] - temposMax[i])       
    
PeriodoMedia = sum(periodos) / len(periodos)
print(PeriodoMedia)   

   
plt.plot(t,Em)
plt.ylim(7,9) # Para corrigir  a linha estar toda torta, e passar a direito. (Apenas visual!!!)
plt.xlabel("t (s) ")
plt.ylabel("Em (J)")
plt.title("Energia Mecânica")
plt.grid()