# -*- coding: utf-8 -*-

# Regressão linear
# Equações do formulário

import numpy as np
import matplotlib.pyplot as plt
L=np.array([222.0,207.5,194,171.5,153.0,133.0,113.0,92.0])
X=np.array([2.3,2.2,2.0,1.8,1.6,1.4,1.2,1.0])

# plt.scatter(L,X)
# plt.xlabel("L (cm) ")
# plt.ylabel("X (cm) ")

#Truque para não ter de alterar o código abaixo: identificar x e y corretamente
x=L
y=X


npontos=x.size

xy=x*y# element by element product
x2=x*x
y2=y*y

sx=x.sum()
sy=y.sum()
sxy=xy.sum()
sxx=x2.sum()
syy=y2.sum()

print("sx,sy,sxy,sxx,syy")
print(sx,sy,sxy,sxx,syy)