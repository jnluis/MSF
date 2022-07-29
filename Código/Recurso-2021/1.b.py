# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 23:22:36 2022

@author: João Luís
"""

import numpy as np
import matplotlib.pyplot as plt

T=np.array([0.5, 1.5, 2.5, 3.5, 4.5,5.5,6.5, 7.5, 8.5, 9.5,10.5])
S=np.array([0.121,0.997, 2.55, 6.09, 9.31, 15.8, 17.1, 25.5, 26.5, 38.8, 41.9])



#Truque para não ter de alterar o código abaixo: identificar x e y corretamente
x=np.log(T)
y=np.log(S)
plt.scatter(x,y)

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

plt.xlabel("log(t) (s) ")
plt.ylabel("log(s) (m) ")


x_g = np.arange(-1,3,0.5)
l_g =result[0] * x_g + result[1]
plt.plot(x_g,l_g, "--")