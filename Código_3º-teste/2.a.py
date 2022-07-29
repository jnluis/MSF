import matplotlib.pyplot as plt
import numpy as np


m = 1
k = 1


b=0.05 #kg
f=7.5
wf=1.4

t0 = 0
tf =400
dt = 0.0001

n = int((tf-t0)/dt)
t = np.linspace(t0,tf,n)

x = np.empty(n)
v = np.empty(n)
a = np.empty(n)

x[0] = 2
v[0] = 4

a[0] = (-k*x[0] - b * v[0] + f*np.cos(wf*t[0]))/m

for i in range(n-1):   
    a[i+1] = (-k*x[i] - b * v[i] + f*np.cos(wf*t[i]))/m
    v[i+1] = v[i] +a[i+1]*dt 
    x[i+1] = x[i] +v[i+1]*dt
    
arrayMaximos = []
temposMax = []

for i in range(n-1):
    
    if (t[i]>200 and x[i-1]<x[i]>x[i+1] and i>0 ): 
        arrayMaximos.append(x[i])
        temposMax.append(t[i])
        
periodos = []

for i in range(len(temposMax)-1):
    periodos.append(temposMax[i+1] - temposMax[i])


amplitude = sum(arrayMaximos)/len(arrayMaximos)

periodoMedia = sum(periodos)/len(periodos)

print("A amplitude média é {:.3f} m".format(amplitude))
print("O periodo médio é {:.3f} s".format(periodoMedia))    

plt.plot(t,x)
plt.xlabel("t (s)")
plt.ylabel("x (m/s)")
plt.title("Oscilador Harmónico")
plt.grid()
plt.show()