import matplotlib.pyplot as plt
import numpy as np

m = 1
k = 1
g=9.8

xeq = 0
b=0.05
f=7.5
wf=1

t0 = 0
tf =400
dt = 0.0001

n = int((tf-t0)/dt)
t = np.linspace(t0,tf,n)

x = np.empty(n)
v = np.empty(n)
a = np.empty(n)
Ep = np.empty(n)
Ec = np.empty(n)
EM = np.empty(n)


x[0] = 0
v[0] = 0

a[0] = (-k*x[0] - b * v[0] + f*np.cos(wf*t[0]))/m

for i in range(n-1):   
    a[i+1] = (-k*x[i] - b * v[i] + f*np.cos(wf*t[i]))/m
    v[i+1] = v[i] +a[i+1]*dt 
    x[i+1] = x[i] +v[i+1]*dt
    Ep[i] = 0.5*k* x[i]**2
    Ec[i] = m*0.5*v[i]**2
    EM[i] = Ec[i] + Ep[i]
    
Ep[n-1] = 0.5*k*x[n-1]**2
Ec [n-1]= m*0.5*v[n-1]**2
EM[n-1] = Ec[n-1] + Ep[n-1]


plt.plot(t,EM)
plt.xlabel("t (s)")
plt.ylabel("EM (j)")
plt.title("")
plt.show()

#Não conserva a energia mecânica
