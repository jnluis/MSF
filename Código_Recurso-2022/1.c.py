# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 16:21:15 2022

@author: hf_co
"""

import numpy as np
import matplotlib.pyplot as plt

A=np.array([10.07,6.293,3.831,2.500,1.409,0.8775,0.5369,0.3522,0.2173,0.1357])
#t=np.array([0,5,10,15,20,25,30,35,40,45]) semanas. O professor fez para dias e isso faz com que dê diferente

t=np.array([0,35,70,105,140,175,210,245,280,315]) # as semanas convertidas para dias

#Truque para não ter de alterar o código abaixo: identificar x e y corretamente
x=np.exp(1)**(-0.0137*t) #np.exp(1) é o número de Euler -> e
y=A

plt.scatter(x,y)
plt.xlabel("exp(-declive*tempo)")
plt.ylabel("Atividade")

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
x_g = np.arange(0,1.2,0.5) #ajustar para vermos no grafico
l_g =result[0] * x_g + result[1]
plt.plot(x_g,l_g)#, "--")