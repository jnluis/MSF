import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5,5,100000)
k = 2
xeq = 0
alfa = -0.1
beta = 0.02
Epot = 0.5*k*x**2 + alfa * x**3 - beta*x**4

plt.plot(x,Epot)
axis = plt.gca()
axis.set_ylim(0,5)
plt.grid()
plt.show()