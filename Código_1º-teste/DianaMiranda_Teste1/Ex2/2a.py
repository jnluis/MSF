import matplotlib.pyplot as plt
import numpy as np

y0 = 800
v0 =0

vtSL = 60 #m/s
vtPA = 5  #m/s


p = 1.225 #kg/m^3

g = 9.8 #m/s^2
dt = 0.01

t0 = 0.00 ##tempo inicial
tf = 25 ##tempo final

n = int((tf-t0)/dt)

D = g/vtSL**2

n = int((tf-t0)/dt)
t = np.linspace(t0,tf,n)
v = np.empty(n)
y = np.empty(n)
a = np.empty(n)

v[0] = v0
y[0] = y0

## Ciclo que implementa o Método de Euler, e atualiza o array tempo para podemos fazer um plot
for i in range(n-1):  
    a[i] = -D * v[i]*abs(v[i]) - g
    v[i+1] = v[i] + a[i]*dt
    y[i+1] = y[i] + v[i] * dt
    
for i in range(n-1):
    if (y[i]>(0-dt) and y[i+1] <(0+dt)):
        print("dt, t, y = ", dt, t[i+1], y[i+1])
        print("Chega ao solo em {:.2f}s e a {:0.2f}m/s".format(t[i+1], abs(v[i+1])))
        plt.plot(t[i+1],y[i+1], "o")
        break

plt.plot(t, y, label="Método de Euler")
plt.xlabel("t (s)")
plt.ylabel("y(t) m")
plt.grid()
plt.show()
