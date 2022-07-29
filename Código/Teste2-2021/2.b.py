# -*- coding: utf-8 -*-1
"""
Created on Mon May  9 17:30:26 2022

@author: joão
v =-A*w*sin(wt+d)
A =-A*w**2*cos(wt+d)
"""

import matplotlib.pyplot as plt
import numpy as np
#   Faça o diagrama de energia desta energia potencial.


m = 1.5
alpha = -0.01
k = 1.2

#t = np.arange(0, 200+dt, dt) Outra maneira de fazer o t
#Tmpo inicial e final
ti =0
tf=10
dt = 0.01
n = int((tf-ti) / dt)
t = np.linspace(ti, tf, n)

x = np.zeros(t.size)
v = np.zeros(t.size)
a= np.empty(n)
Ep = np.empty(n)
Ec = np.empty(n)
Em = np.empty(n)

x[0] = 3.5
v[0] =2
a[0] = -k/m*x[0]

    
for i in range(n-1):
    a[i+1] = (-3*alpha*(x[i]**2) - k * x[i] ) /m
    v[i+1] = v[i] + a[i+1]*dt
    x[i+1] = x[i]+v[i+1]*dt  # Pelo método de Euler, não funcionava

#Calcular a Energia Mecanica  
Ep = 0.5 * k*(x**2) + alpha* (x**3)
Ec = 0.5 *m * v **2
Em = Ep +Ec
    
plt.plot(t, x)    
plt.xlabel("t (s)")
plt.ylabel("x (m)")
plt.title("Lei do Movimento")
plt.grid()
plt.show()

plt.plot(t, Em, color="purple")    
plt.xlabel("t (s)")
plt.ylabel("Em (J)")
plt.title("Energia Mecãnica")
plt.grid()


#Entre que limites se efetua o movimento

print("O valo máximo de x(t) é ",max(x))
print("O valo mínimo de x(t) é ",min(x))


#Calcular a frequência e o período do movimento
# f = 1/T
arrayMaximos = []
temposMax = []
periodo = []



for i in range(t.size-1):
    if (x[i-1]<x[i]>x[i+1] and i>0):
        arrayMaximos.append(x[i])
        temposMax.append(t[i])

for i in range(0,len(temposMax)-1):
    periodo.append(temposMax[i+1]-temposMax[i])


print("Periodo ->",np.mean(periodo))
#print("Amplitude ->" ,np.mean(arrayMaximos))
print("A frequencia do movimento é: ",(1/np.mean(periodo)))
