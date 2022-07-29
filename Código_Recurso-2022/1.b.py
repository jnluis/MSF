# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 23:22:36 2022

@author: João Luís
"""

import numpy as np
import matplotlib.pyplot as plt

A=np.array([10.07,6.293,3.831,2.500,1.409,0.8775,0.5369,0.3522,0.2173,0.1357])
t=np.array([0,5,10,15,20,25,30,35,40,45])



#Truque para não ter de alterar o código abaixo: identificar x e y corretamente
x=t
y=np.log(A)

plt.scatter(x,y)
plt.xlabel("t (semanas) ")
plt.ylabel("log (mCi) ")

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
x_g = np.arange(0,50,0.5)
l_g =result[0] * x_g + result[1]
plt.plot(x_g,l_g, "--")