import matplotlib.pyplot as plt
import numpy as np

m = 1
k = 1
g=9.8

L = 1

t0 = 0
tf =20
dt = 0.0001

angulo = np.radians(1)

n = int((tf-t0)/dt)
t = np.linspace(t0,tf,n)

teta = np.empty(n)
w = np.empty(n)
a = np.empty(n)

teta[0] = angulo
w[0] = 0

a[0] = -g/L * np.sin(teta[0])

for i in range(n-1):   
    a[i+1] = -g/L * np.sin(teta[i])
    w[i+1] = w[i] +a[i+1]*dt 
    teta[i+1] = teta[i] +w[i+1]*dt
    
arrayMaximos = []
temposMax = []

for i in range(n-1):
    if (teta[i-1]<teta[i]>teta[i+1] and i>0 ): 
        arrayMaximos.append(teta[i])
        temposMax.append(t[i])
        
periodos = []

for i in range(len(temposMax)-1):
    periodos.append(temposMax[i+1] - temposMax[i])


periodoMedia = sum(periodos)/len(periodos)

print("O periodo médio é {:.3f} s".format(periodoMedia))
    

plt.plot(t, np.degrees(teta))
plt.xlabel("t (s)")
plt.ylabel("teta (º)")
plt.title("Lei do movimento")
plt.show()