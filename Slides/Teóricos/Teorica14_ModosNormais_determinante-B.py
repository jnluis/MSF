#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 15:07:03 2022

@author: joao
"""

from numpy import linalg as LA
import numpy as np

ti =0
tf=50
dt = 0.0001
n = int((tf-ti) / dt)


k= 0
klinha = 0.5
m= 1

matdyn = [ [((k+klinha) /m), -klinha/m,0], [-klinha/m,2*klinha/m, -klinha/m], [0,-klinha/m,((k+klinha) /m) ]   ]
v = np.empty(n)
w = np.empty(n)

w, v = LA.eig(matdyn)

print(np.sqrt(w),v)


#Para o caso em que m= 2kg
m=2

matdyn = [ [((k+klinha) /m), -klinha/m,0], [-klinha/m,2*klinha/m, -klinha/m], [0,-klinha/m,((k+klinha) /m) ]   ]

w, v = LA.eig(matdyn)
print("")
print(np.sqrt(w),v)
