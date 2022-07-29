# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 23:22:36 2022

@author: João Luís
"""

import numpy as np
import matplotlib.pyplot as plt

T=np.array([200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100])
E=np.array([0.6950, 4.363, 15.53, 38.74, 75.08, 125.2, 257.9, 344.1,
557.4, 690.7])



#Truque para não ter de alterar o código abaixo: identificar x e y corretamente
x=T
y=E

plt.scatter(T,E)
plt.xlabel("T (K) ")
plt.ylabel("E (J) ")

def regressao_linear(x,y):
    npontos=x.size

    xy=x*y# element by element product
    x2=x*x
    y2=y*y

    sx=x.sum()
    sy=y.sum()
    sxy=xy.sum()
    sxx=x2.sum()
    syy=y2.sum()

    #print("sx,sy,sxy,sxx,syy")
    #print(sx,sy,sxy,sxx,syy)
    n=npontos
    rn=n*sxy-sx*sy
    rd=(n*sxx-sx**2)*(n*syy-sy**2)
    r2=rn**2/rd
    r=np.sqrt(r2)
    m=(n*sxy-sx*sy)/(n*sxx-sx**2)
    dm=abs(m)*np.sqrt((1/r**2-1)/(n-2))
    bn=sxx*sy-sx*sxy  
    bd=n*sxx-sx**2
    b=bn/bd
    db=dm*np.sqrt(sxx/n)
    print('m +/-dm= ',m ,"+/-", dm)
    print('b +/-db= ',b ,"+/-",db)
    print('r2= ',r2)
    return m,b

result = regressao_linear(x,y)
print("Através da análise do gráfico, podemos concluir que a energia emitida aumenta com o aumento da temperatura, em especial, a partir dos 600 K.")