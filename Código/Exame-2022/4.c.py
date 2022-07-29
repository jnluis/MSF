# -*- coding: utf-8 -*-1
"""
Created on Mon May  9 17:30:26 2022

@author: joão
v =-A*w*sin(wt+d)
A =-A*w**2*cos(wt+d)
"""
'''
import matplotlib.pyplot as plt
import numpy as np
#   Faça o diagrama de energia desta energia potencial.


m = 0.5
alpha = -0.1
beta = 0.02
k = 2

#t = np.arange(0, 200+dt, dt) Outra maneira de fazer o t
#Tmpo inicial e final
ti =0
tf=5
dt = 0.00001
n = int((tf-ti) / dt)
t = np.linspace(ti, tf, n)

x = np.zeros(t.size)
v = np.zeros(t.size)
a= np.empty(n)
Ep = np.empty(n)
Ec = np.empty(n)
Em = np.empty(n)

x[0] = 1.5
v[0] = 0.5
a[0] = (-3*alpha*(x[0]**2) +4*beta*(x[0]**3) - k * x[0] ) /m

    
for i in range(n-1):
    a[i+1] = (-3*alpha*(x[i]**2) +4*beta*(x[i]**3) - k * x[i] ) /m
    v[i+1] = v[i] + a[i+1]*dt
    x[i+1] = x[i]+v[i+1]*dt  # Pelo método de Euler, não funcionava

#Calcular a Energia Mecanica  
Ep =  0.5 * k*(x**2) + alpha* (x**3) - beta* (x**4)
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
'''

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
tf = 5
dt = 0.00001
n = int((tf-t0)/dt)
k = 2.0
m = 0.5
x0 = 1.5
v0 = 0.5
beta = 0.02
alfa = -0.1


t = np.zeros(n+1)
x = np.zeros(n+1)
vx = np.zeros(n+1)
ax = np.zeros(n+1)
emec = np.zeros(n+1)


x[0] = x0
vx[0] = v0


for i in range(n):
    t[i+1] = t[i] + dt
    ax[i] = (-k*x[i] - 3*alfa*x[i]**2 + 4*beta*x[i]**3)/m
    vx[i+1] = vx[i] + ax[i] * dt
    x[i+1] = x[i] + vx[i+1] * dt
    emec[i] = 0.5*m*vx[i]**2 + 0.5*k*x[i]**2 + alfa* x[i]**3 - beta * x[i]**4  # Emec = Ec + EpotElastica

emec[i+1] = 0.5*m*vx[i+1]**2 + 0.5*k*x[i+1]**2 + beta * x[i+1]**3

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