# -*- coding: utf-8 -*-

# Regressão linear
# Equações do formulário

import numpy as np
import matplotlib.pyplot as plt
L=np.array([222.0,207.5,194,171.5,153.0,133.0,113.0,92.0])
X=np.array([2.3,2.2,2.0,1.8,1.6,1.4,1.2,1.0])

plt.plot(L,X,"ob")
plt.xlabel("L (cm) ")
plt.ylabel("X (cm) ")
def fun(x,y):
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

# print('m +/-dm= ',m ,"+/-", dm)
# print('b +/-db= ',b ,"+/-",db)
# print('r2= ',r2)
result_regression = fun(L,X)
m = result_regression[0]
b = result_regression[1]

x_g = np.arange(80,240,10)
l_g =m * x_g + b
plt.plot(x_g,l_g, "--")

X=np.array([2.3,2.2,2.0,1.8,2.5,1.4,1.2,1.0])

plt.plot(L,X,"og")
plt.xlabel("L (cm) ")
plt.ylabel("X (cm) ")

result_regression = fun(L,X)
m = result_regression[0]
b = result_regression[1]

x_g = np.arange(80,240,10)
l_g_new =m * x_g + b
plt.plot(x_g,l_g, "--")

plt.plot(x_g,l_g, "--", label= " Ajuste com os pontos originais")
plt.plot(x_g,l_g_new, "-", label= " Ajuste com os pontos modificados")
plt.legend()