# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from matplotlib import pyplot as plt
import numpy as np
#x = np.array([])
#y = np.array([])

#v=6.8
#g=9.8
#t=0
#while t < 2.2:
#    y = np.append(y, v**2/g*np.log(np.cosh(g*t/v)))
#    x = np.append(x, t)
#    t = t+0.1
#plt.plot(x,y)

t = np.arange(0,2,0.1)
vt=6.80
g=9.80

plt.xlabel("t (s)")
plt.ylabel("y (m)")

y=(vt**2/g)*np.log(np.cosh((g*t)/vt))
plt.plot(t,y,"go")