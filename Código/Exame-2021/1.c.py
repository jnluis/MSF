# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 23:22:36 2022

@author: João Luís
"""

import numpy as np
import matplotlib.pyplot as plt

R=np.array([3.389,3.924,4.459,4.993,5.528,6.062,6.597,7.131,7.666,8.200])
a=np.array([3.522,2.793,2.098,1.681,1.557,1.089,1.050,0.896,0.669,0.640])



#Truque para não ter de alterar o código abaixo: identificar x e y corretamente
x=R**(-1.96) 
y=a

plt.scatter(x,y)
plt.xlabel("R^-1.96 (10⁶m)")
plt.ylabel("a (m/s²)")

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
x_g = np.arange(0,0.11,0.5)
l_g =result[0] * x_g + result[1]
plt.plot(x_g,l_g, "--")

print("Para a relação escrever a expressão obtida na alinea b, com o m deste grafico a ser o c e depois acrescentar o b obtido também.")
print("Não esquecer de colocar também os respetivos erros associados ao m e ao b")