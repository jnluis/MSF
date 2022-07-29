import matplotlib.pyplot as plt
import numpy as np

y0 = 800
v0 =0

vtSL = 60 #m/s
vtPA = 5  #m/s

p = 1.225 #kg/m^3

g = 9.8 #m/s^2
dt = 0.001

t0 = 0.00 ##tempo inicial
tf = 203 ##tempo final

n = int((tf-t0)/dt)

D1 = g/vtPA**2
D2 = g/vtSL**2

n = int((tf-t0)/dt)
t = np.linspace(t0,tf,n)
v = np.empty(n)
y = np.empty(n)
a = np.empty(n)

v[0] = v0
y[0] = y0

for i in range(n-1):
    if(t[i]<10):
        a[i] = -D2 * v[i]*abs(v[i]) - g
        v[i+1] = v[i] + a[i]*dt
        y[i+1] = y[i] + v[i] * dt
    else:
        a[i] = -D1 * v[i]*abs(v[i]) - g
        v[i+1] = v[i] + a[i]*dt
        y[i+1] = y[i] + v[i] * dt
    
    
for i in range(n-1):
    if (y[i]>(0-dt) and y[i+1] <(0+dt)):
        print("dt, t, y = ", dt, t[i+1], y[i+1])
        print("Chega ao solo em {:.2f} s a {:.2f}m/s".format(t[i+1], abs(v[i+1])))
        plt.plot(t[i+1],y[i+1], "o")
        break

plt.plot(t, y, label="Método de Euler")
plt.xlabel("t (s)")
plt.ylabel("y(t) m")
plt.show()
