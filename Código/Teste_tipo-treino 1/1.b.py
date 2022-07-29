# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 23:22:36 2022

@author: João Luís
"""

import numpy as np
import matplotlib.pyplot as plt

T=np.array([1.21, 1.40, 1.26, 1.05, 1.60, 1.78, 2, 2.11, 2.22, 2.33])
M=np.array([0.15, 0.20,0.16,0.11,0.25,0.32,0.40,0.45,0.50,0.55])



#Truque para não ter de alterar o código abaixo: identificar x e y corretamente
x=np.log(M)
y=np.log(T)



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

plt.scatter(x,y)
plt.xlabel("Log(M) (kg) ")
plt.ylabel("Log(T) (s) ")

x_g = np.arange(-2.6,0,0.2)
l_g = result[0]*x_g + result[1]
plt.plot(x_g,l_g,"tab:orange")